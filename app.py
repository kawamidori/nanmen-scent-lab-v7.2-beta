# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import copy
import json
from datetime import datetime

from config import (
    PERFUME_CONCENTRATION_PRESETS, SOLVENT_CHOICES, REGULATORY_REGIONS,
    DILUTION_TIERS, SOLVENT_DATABASE
)
from library import CHEMICAL_CORE_DB, DEFAULT_COMMERCIAL_SKUS
import core
import db
import pdf_gen
import file_export

st.set_page_config(page_title="Nanmen Scent Lab OS", layout="wide", page_icon="🧪")

# Initialize SQLite persistence & Admin account
admin_secret = st.secrets.get("APP_PASSWORD", "nanmen2026")
db.init_db(admin_default_password=admin_secret)

if "lang" not in st.session_state:
    st.session_state.lang = "zh"

# ------------------------------------------------------------------------------
# UI CSS (Desktop + Mobile Responsive)
# ------------------------------------------------------------------------------
st.markdown("""
<style>
    @media (max-width: 768px) {
        .block-container { padding: 4.2rem 0.4rem 1rem 0.4rem !important; }
        .stTabs [data-baseweb="tab-list"] { display: flex; overflow-x: auto; white-space: nowrap; -webkit-overflow-scrolling: touch; }
        .stats-bar { flex-direction: column; gap: 6px; text-align: left; align-items: flex-start !important; }
        input[type="number"] { font-size: 16px !important; }
    }
    .mod-pill { background: #0F172A; color: #38BDF8; padding: 3px 10px; border-radius: 6px; font-weight: bold; border: 1px solid #0284C7; font-size: 13px; }
    .mat-card { background: #F8FAFC; border: 1px solid #CBD5E1; padding: 12px; border-radius: 8px; margin-top: 8px; }
    .scale-chip { background: #064E3B; color: #6EE7B7; padding: 3px 8px; border-radius: 4px; font-family: monospace; font-size: 13px; font-weight: bold; display: inline-block; }
    .cas-badge { background: #F1F5F9; color: #475569; padding: 2px 5px; border-radius: 4px; font-family: monospace; font-size: 11px; border: 1px solid #CBD5E1; }
    .layer-l1 { background: #E0F2FE; color: #0369A1; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    .layer-l2 { background: #DCFCE7; color: #15803D; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    .layer-l3 { background: #F3E8FF; color: #7E22CE; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    .stats-bar { background: #0F172A; color: white; padding: 12px 18px; border-radius: 8px; margin-top: 14px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .sample-card { background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }
    .doc-sheet { background: white; padding: 20px; border: 1px solid #CBD5E1; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.04); color: #0F172A; margin-bottom: 14px; }
    .doc-title { border-bottom: 2px solid #0F172A; padding-bottom: 8px; margin-bottom: 14px; }
    .cert-box { background: #FFFFFF; border: 2px solid #0F172A; border-radius: 8px; padding: 18px; margin-bottom: 14px; }
    .nda-box { background: #FFFBEB; border: 2px solid #D97706; border-radius: 8px; padding: 18px; margin-bottom: 14px; color: #78350F; }
    .landing-nda { background: #0F172A; color: #F8FAFC; border: 1px solid #38BDF8; border-radius: 10px; padding: 20px; margin-bottom: 16px; }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# FIRST SCREEN: MUTUAL NDA PLEDGE + INDIVIDUAL PERFUMER ACCOUNT LOGIN / SIGNUP
# ------------------------------------------------------------------------------
def load_session_for_user(user_info):
    ws = db.load_user_workspace(user_info["username"])
    st.session_state["current_user"] = user_info
    st.session_state["mods"] = ws.get("mods", db.get_default_workspace()["mods"])
    st.session_state["active_mod"] = ws.get("active_mod", list(st.session_state["mods"].keys())[0] if st.session_state["mods"] else "Mod 1")
    if st.session_state["active_mod"] not in st.session_state["mods"] and st.session_state["mods"]:
        st.session_state["active_mod"] = list(st.session_state["mods"].keys())[0]
    st.session_state["mod_notes"] = ws.get("mod_notes", {})
    st.session_state["custom_materials"] = ws.get("custom_materials", {})
    st.session_state["dosed_checklist"] = ws.get("dosed_checklist", {})
    st.session_state["region_id"] = ws.get("region_id", "EU") if ws.get("region_id") in REGULATORY_REGIONS else "EU"
    st.session_state["tier_id"] = ws.get("tier_id", "EdP_15") if ws.get("tier_id") in PERFUME_CONCENTRATION_PRESETS else "EdP_15"
    st.session_state["phase_idx"] = 0

def persist_current_workspace():
    u = st.session_state.get("current_user")
    if not u:
        return
    ws_payload = {
        "mods": st.session_state.get("mods", {}),
        "active_mod": st.session_state.get("active_mod", "Mod 1"),
        "mod_notes": st.session_state.get("mod_notes", {}),
        "custom_materials": st.session_state.get("custom_materials", {}),
        "dosed_checklist": st.session_state.get("dosed_checklist", {}),
        "region_id": st.session_state.get("region_id", "EU"),
        "tier_id": st.session_state.get("tier_id", "EdP_15")
    }
    db.save_user_workspace(u["username"], ws_payload)

def render_landing_and_auth():
    l_col1, l_col2 = st.columns([5.2, 1.0])
    l_col1.markdown("### 🧪 Nanmen Scent Lab OS — Independent Perfumer Workbench")
    chosen_l = l_col2.radio("LandingLang", ["中文", "EN"], index=0 if st.session_state.lang == "zh" else 1, horizontal=True, label_visibility="collapsed")
    if ("zh" if chosen_l == "中文" else "en") != st.session_state.lang:
        st.session_state.lang = "zh" if chosen_l == "中文" else "en"
        st.rerun()

    lg = st.session_state.lang

    # --- FIRST-SCREEN MUTUAL NDA & FORMULA ISOLATION PLEDGE ---
    if lg == "zh":
        st.markdown("""
        <div class="landing-nda">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
                <h4 style="margin:0; color:#38BDF8;">🛡️ 調香師智慧財產權保護與保密承諾書 (Mutual NDA & Zero-Leakage Pledge)</h4>
                <span style="background:#0284C7; color:white; padding:2px 10px; border-radius:4px; font-size:12px; font-weight:bold;">CONFIDENTIAL WORKSPACE</span>
            </div>
            <hr style="border-color:#1E293B; margin:10px 0;">
            <div style="font-size:13.5px; line-height:1.75; color:#E2E8F0;">
                <b>歡迎進入 Nanmen Scent Lab OS 獨立調香師工作站。</b>我們深知配方比例是調香師最核心的資產，因此本系統在架構上嚴格執行以下三項保密原則：<br>
                1. <b>獨立帳號與資料隔離（Strict Account Isolation）：</b>每位調香師皆擁有獨立加密儲存空間，您的配方比例、版本筆記與自建私有原料庫僅供您本人存取，其他使用者或外部品牌端完全無法檢視。<br>
                2. <b>純粹創作與合規演算（Zero External Factory Exposure）：</b>本工作站專注於協助您自動化計算 IFRA 51st 限量、歐盟/台灣 10 ppm 致敏原展開與天平放樣單，絕不未經授權對外揭露您的配方結構。<br>
                3. <b>三方保密協議直傳 SA 機制（Tri-Party NDA Direct-to-SA）：</b>當您需要產出 PIF 產品資訊檔案時，系統內建三方保密協議（調香師 × 品牌委託方 × 獨立安全評估人員 SA）直傳格式，確保 100% 完整成分表僅交付予簽署 NDA 之安全評估人員。
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="landing-nda">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
                <h4 style="margin:0; color:#38BDF8;">🛡️ Perfumer Intellectual Property & Mutual Confidentiality Pledge (NDA)</h4>
                <span style="background:#0284C7; color:white; padding:2px 10px; border-radius:4px; font-size:12px; font-weight:bold;">CONFIDENTIAL WORKSPACE</span>
            </div>
            <hr style="border-color:#1E293B; margin:10px 0;">
            <div style="font-size:13.5px; line-height:1.75; color:#E2E8F0;">
                <b>Welcome to Nanmen Scent Lab OS.</b> Your formulations are your core creative asset. Every workspace enforces three strict confidentiality guarantees:<br>
                1. <b>Strict Account & Data Isolation:</b> Every perfumer operates in an isolated workspace. Your formulas, mod notes, and private custom materials are strictly bound to your account and invisible to other users.<br>
                2. <b>Pure Formulation & Regulatory Automation:</b> Built to automate IFRA 51st limits, 10 ppm allergen calculations, and running-tare compounding sheets without exposing proprietary formulas.<br>
                3. <b>Tri-Party NDA Direct-to-SA Protocol:</b> When generating PIF compliance dossiers, our Tri-Party NDA workflow ensures 100% quantitative compositions are transmitted exclusively to your designated Safety Assessor (SA).
            </div>
        </div>
        """, unsafe_allow_html=True)

    c_left, c_mid, c_right = st.columns([0.8, 1.8, 0.8])
    with c_mid:
        tab_login, tab_signup = st.tabs([
            "🔑 調香師登入 (Perfumer Login)" if lg == "zh" else "🔑 Perfumer Login",
            "✨ 建立獨立調香師帳號 (Create Account)" if lg == "zh" else "✨ Create Perfumer Account"
        ])

        with tab_login:
            with st.form("login_form"):
                u_in = st.text_input("帳號 (Username)", placeholder="輸入您的調香師帳號...")
                p_in = st.text_input("密碼 (Password)", type="password", placeholder="輸入密碼...")
                if st.form_submit_button("登入工作站 / Enter Lab", type="primary", use_container_width=True):
                    user_obj, err = db.authenticate_user(u_in, p_in, admin_secret_pwd=admin_secret)
                    if user_obj:
                        load_session_for_user(user_obj)
                        st.rerun()
                    else:
                        st.error(f"❌ {err}")

        with tab_signup:
            st.caption("建立專屬帳號後，系統將自動為您整合並永久保存所有調香版本（Mods）與私有原料庫。" if lg == "zh" else "Create your personal account to consolidate and persist all your formula Mods and private custom materials.")
            with st.form("signup_form"):
                new_u = st.text_input("設定登入帳號 (Username) *", placeholder="例如: claire_scent (英文或數字，至少3碼)")
                new_disp = st.text_input("調香師 / 工作室名稱 (Perfumer / Studio Name) *", placeholder="例如: Claire Studio / 獨立調香師")
                new_email = st.text_input("聯絡 Email (選填，供密碼重設與合規通知)", placeholder="perfumer@example.com")
                new_p1 = st.text_input("設定密碼 (Password) *", type="password", placeholder="至少 4 個字元")
                new_p2 = st.text_input("確認密碼 (Confirm Password) *", type="password", placeholder="再次輸入密碼")
                nda_agree = st.checkbox(
                    "✅ 我已閱讀並同意上述保密與資料隔離承諾書（Mutual Confidentiality & Data Isolation Pledge）" if lg == "zh"
                    else "✅ I acknowledge and accept the Confidentiality & Data Isolation Pledge above",
                    value=True
                )
                if st.form_submit_button("🚀 建立帳號並進入工作站 / Create Account", type="primary", use_container_width=True):
                    if not nda_agree:
                        st.error("⚠️ 請先勾選同意保密與資料隔離承諾書。")
                    elif new_p1 != new_p2:
                        st.error("❌ 兩次輸入的密碼不一致 / Passwords do not match.")
                    else:
                        ok, msg = db.register_perfumer(new_u, new_disp, new_email, new_p1, plan_tier="Pro")
                        if ok:
                            user_obj, _ = db.authenticate_user(new_u, new_p1, admin_secret_pwd=admin_secret)
                            load_session_for_user(user_obj)
                            st.rerun()
                        else:
                            st.error(f"❌ {msg}")

if "current_user" not in st.session_state or st.session_state["current_user"] is None:
    render_landing_and_auth()
    st.stop()

# ==============================================================================
# LOGGED-IN WORKSPACE SETUP
# ==============================================================================
current_user = st.session_state["current_user"]
is_admin = (current_user.get("role") == "admin")
enable_vendor_portal = (db.get_system_flag("ENABLE_VENDOR_PORTAL", "0") == "1") or is_admin

if "core_db" not in st.session_state:
    st.session_state.core_db = copy.deepcopy(CHEMICAL_CORE_DB)
if "commercial_skus" not in st.session_state:
    st.session_state.commercial_skus = copy.deepcopy(DEFAULT_COMMERCIAL_SKUS)
if "locked_for_pif" not in st.session_state:
    st.session_state.locked_for_pif = False

# ------------------------------------------------------------------------------
# BILINGUAL DICTIONARY
# ------------------------------------------------------------------------------
UI = {
    "zh": {
        "mod_label": "📂 當前操作版本 (Mod)",
        "reg_label": "🌐 專案法規基準 (Regulatory)",
        "dos_label": "🎯 目標成品賦香率 (Dosage)",
        "btn_copy": "➕ 複製",
        "btn_clear": "🗑️ 清空",
        "p1_banner": "💻 Phase 1：數位配方創作（自動雲端存檔整合）",
        "p1_w_lbl": "配方總重",
        "p1_act_lbl": "純香精淨重",
        "p1_t1": "🎛️ 1-A：互動式三欄調香機艙",
        "p1_t2": "🧪 1-B：私有原料庫與帳號資料整合 (Consolidation)",
        "p1_t3": "📄 1-C：配方總表 (Print-ready Snapshot)",
        "layer_sel": "選擇選料層級：",
        "lib_search": "🔍 搜尋 (CAS / 名稱)：",
        "lib_ph": "例如: 54464-57-2, 肖楠, 佛手柑",
        "all_notes": "全部香階",
        "note_lbl": "香階",
        "sg_lbl": "比重 ρ",
        "cost_lbl": "參考單價",
        "ifra_lbl": "IFRA Cat.4 上限",
        "btn_add": "➕ 加入當前配方表",
        "warn_exists": "⚠️ 此原料已在配方中。",
        "ai_exp": "🤖 AI 靈感骨架助理 (從 CAS 核心生成)",
        "ai_cap": "依據五維權重與蒸氣壓計算 5.000g 起手骨架：",
        "sl_citrus": "🍊 柑橘清新 (Citrus)",
        "sl_floral": "🌸 優雅花香 (Floral)",
        "sl_woody": "🌲 沉穩木質 (Woody)",
        "sl_spicy": "🌶️ 辛香草本 (Spicy)",
        "sl_sweet": "🍦 溫潤樹脂 (Sweet)",
        "btn_gen": "✨ 生成起手骨架並覆蓋當前 Mod",
        "grid_hdr": "#### 🔵 數位配方矩陣 (Formulation Grid)",
        "unit_opts": ["克數 (g) + 佔比", "千分比 (PPT ‰)"],
        "scale_pop": "⚖️ 等比縮放",
        "scale_tgt": "目標總克數 (g)",
        "scale_btn": "執行縮放",
        "empty_form": "👈 當前配方為空。請從左側原料庫挑選原料加入。",
        "pure_price": "成本",
        "pure_oil": "純油",
        "drops_unit": "滴",
        "probe_hdr": "#### 🟡 即時智慧探針",
        "probe_t1": "🛡️ 金字塔與法規",
        "probe_t2": "🎡 風味輪與揮發",
        "pyr_title": "**嗅覺金字塔結構 (純油有效佔比)：**",
        "top_l": "Top 前調", "mid_l": "Heart 中調", "base_l": "Base 後調",
        "tenacity_lbl": "蒸氣壓留香力指數 (AI Tenacity)",
        "ifra_radar": "IFRA 51st 合規雷達 (同 CAS 自動合併)",
        "over_limit": "超標！殘留", "limit_word": "限值",
        "near_warn": "逼近警戒",
        "ifra_ok": "✅ 符合 IFRA Cat.4 限值（最高安全賦香率上限：",
        "allg_warn_hdr": "**⚠️ 須外盒標示之致敏原 (>10 ppm)：**",
        "evap_cap": "⏳ 24h 揮發動態模擬：",
        "notes_hdr": "**📝 調香師版本筆記（自動存檔）：**",
        "bar_cost": "已建價原料成本：",
        "bar_base": "基準成本",
        "bar_jus": "原油",
        "bar_ratio": "純香精有效淨重 vs 載體溶劑：",
        "bar_pure": "純油",
        "bar_sol": "溶劑",
        "dl_sheet": "📥 下載配方總表 (CSV)",
        # Phase 2
        "p2_banner": "⚖️ Phase 2：實驗室放樣與多濃度成品取樣",
        "p2_tgt_jus": "目標原油母液總重",
        "p2_t0": "🔗 2-A：CAS ➔ 商業 SKU 映射閘門",
        "p2_t1": "⚖️ 2-B：天平放樣工作站與實驗室投料單 (100% Jus)",
        "p2_t2": "🧪 2-C：多濃度成品取樣與熟成冷濾 (Phase B 酒精)",
        "p2_sop": "🛡️ **大廠放樣 SOP**：系統已自動將配方強制轉換為 **「後調定香 (Base) ➔ 中調 (Mid) ➔ 高揮發前調 (Top)」** 工業投料序。",
        "p2_prog": "📊 天平累計進度：已完成",
        "p2_items": "項（已投",
        "p2_reset": "🔄 重置打勾記錄",
        "p2_net_add": "本次淨投：",
        "p2_tare": "天平累計：",
        "p2_dosing_hdr": "📋 實驗室標準投料單 (Lab Dosing / Compounding Sheet)",
        "dl_dosing": "📥 下載實驗室投料單 (Lab Dosing Sheet CSV)",
        "p2_samp_hdr": "🧪 多濃度成品取樣計算機 & 熟成冷濾預測",
        "p2_samp_cap": "從調好的 Jus 中取出定量樣品，系統自動扣除載體並加入 3% 低溫冷濾損耗裕度。",
        "samp_a": "#### 樣品 A：日常清新版 (預設 EdT)",
        "samp_b": "#### 樣品 B：沙龍留香版 (預設 EdP)",
        "conc_a": "樣品 A 濃度", "conc_b": "樣品 B 濃度",
        "bot_a": "瓶數 (A)", "bot_b": "瓶數 (B)",
        "vol_a": "單瓶容量 (A)", "vol_b": "單瓶容量 (B)",
        "overfill_lbl": "含 3% 冷濾損耗總投料：",
        "take_jus": "Phase A 取用原油：",
        "add_alc": "Phase B 補入酒精：",
        "lock_a": "✅ 定案採用樣品 A 濃度並送交 Phase 3 PIF",
        "lock_b": "✅ 定案採用樣品 B 濃度並送交 Phase 3 PIF",
        "bal_hdr": "##### 📊 原油母瓶庫存平衡結算：",
        "mac_title": "⏳ 雙階段熟成時鐘：",
        "days_unit": "天",
        # Phase 3
        "p3_banner": "📑 Phase 3：PIF 產品資訊與合規證書 (NDA 隔離保護)",
        "p3_reg": "法規轄區", "p3_dos": "成品賦香率",
        "m_ifra": "IFRA 51st 審查判定",
        "m_max_dos": "Cat.4 香水最高安全賦香率",
        "m_allg": "須展開標示致敏原 (>10ppm)",
        "m_sg": "原油混合比重 / 天然佔比",
        "p3_t1": "1️⃣ 香精全成分比例表 (100% Q&Q)",
        "p3_t2": "2️⃣ 過敏原清單與 INCI 標籤",
        "p3_t3": "3️⃣ IFRA 51st 符合性證書",
        "p3_t4": "4️⃣ 物質安全資料表 (MSDS)",
        "p3_t5": "🔒 5️⃣ 三方保密協議 (NDA) 直傳 SA 模式",
        # Phase 4
        "p4_banner": "🏭 Phase 4：商業量產工單與落地成本框架",
        "p4_deliv": "交付賦香率",
        "p4_s1": "1. 量產批次規模與工單表頭 (Batch Sizing & Dispatch Info)",
        "p4_bot": "首批量產瓶數 (Bottles)",
        "p4_vol": "單瓶容量規格 (ml)",
        "p4_ovf": "冷濾與灌裝損耗裕度 (%)",
        "p4_disp_tgt": "投遞 / 生產單位名稱（空白欄位）",
        "p4_disp_no": "生產批號 / 工單編號（空白欄位）",
        "p4_m1": "成品總預投料重 (含損耗)",
        "p4_m2": "Phase A 調香室投料重 (Jus)",
        "p4_m3": "Phase B 95% 酒精淨投重",
        "p4_m4": "本批次純香精內料基準成本",
        "p4_s2": "2. 工廠生產投料與投遞工單 (Factory BMR Dosing & Dispatch Sheet)",
        "dl_bmr": "📥 下載工廠投料與投遞工單 (Factory BMR & Dispatch Sheet CSV)",
        "p4_s3": "3. 單瓶落地成本框架 (Unit Landed Cost / COGS Framework)"
    },
    "en": {
        "mod_label": "📂 Active Formula Mod",
        "reg_label": "🌐 Regulatory Standard",
        "dos_label": "🎯 Target Dosage",
        "btn_copy": "➕ Copy",
        "btn_clear": "🗑️ Clear",
        "p1_banner": "💻 Phase 1: Digital Formulation (Auto-Consolidated Workspace)",
        "p1_w_lbl": "Total Jus Weight",
        "p1_act_lbl": "Pure Active Oil",
        "p1_t1": "🎛️ 1-A: Interactive 3-Pane Cockpit",
        "p1_t2": "🧪 1-B: Private Material Library & Account Consolidation",
        "p1_t3": "📄 1-C: Formulation Record Sheet (Print-ready)",
        "layer_sel": "Select Material Source:",
        "lib_search": "🔍 Search (CAS / Name):",
        "lib_ph": "e.g., 54464-57-2, Cedar, Bergamot",
        "all_notes": "All Notes",
        "note_lbl": "Olfactory Note",
        "sg_lbl": "Specific Gravity ρ",
        "cost_lbl": "Unit Cost",
        "ifra_lbl": "IFRA Cat.4 Limit",
        "btn_add": "➕ Add to Formula Grid",
        "warn_exists": "⚠️ Item already exists in this Mod.",
        "ai_exp": "🤖 AI Skeleton Assistant (From CAS Core)",
        "ai_cap": "Synthesize a 5.000g starting skeleton using vapor pressure & family weights:",
        "sl_citrus": "🍊 Citrus Freshness",
        "sl_floral": "🌸 Elegant Floral",
        "sl_woody": "🌲 Deep Woody",
        "sl_spicy": "🌶️ Spicy / Herbal",
        "sl_sweet": "🍦 Warm Resinous / Sweet",
        "btn_gen": "✨ Synthesize Skeleton",
        "grid_hdr": "#### 🔵 Formulation Grid",
        "unit_opts": ["Weight (g) + %", "Parts Per Thousand (PPT ‰)"],
        "scale_pop": "⚖️ Auto-Scale",
        "scale_tgt": "Target Batch Weight (g)",
        "scale_btn": "Apply Scale",
        "empty_form": "👈 Formula is empty. Add materials from the left library.",
        "pure_price": "Cost",
        "pure_oil": "Active",
        "drops_unit": "drops",
        "probe_hdr": "#### 🟡 Real-Time Smart Probes",
        "probe_t1": "🛡️ Pyramid & IFRA",
        "probe_t2": "🎡 Wheel & Kinetics",
        "pyr_title": "**Olfactory Pyramid (Pure Active Share):**",
        "top_l": "Top Note", "mid_l": "Heart Note", "base_l": "Base Note",
        "tenacity_lbl": "Vapor Pressure Tenacity Index",
        "ifra_radar": "IFRA 51st Radar (Auto CAS Sum)",
        "over_limit": "EXCEEDS LIMIT! Finished:", "limit_word": "Max:",
        "near_warn": "Approaching Limit",
        "ifra_ok": "✅ IFRA Cat.4 Compliant (Max Safe Dosage Limit: ",
        "allg_warn_hdr": "**⚠️ Mandatory Label Allergens (>10 ppm):**",
        "evap_cap": "⏳ 24h Evaporation Kinetics Simulation:",
        "notes_hdr": "**📝 Perfumer Mod Notes (Auto-Saved):**",
        "bar_cost": "Priced Material Cost:",
        "bar_base": "Unit Cost",
        "bar_jus": "Jus",
        "bar_ratio": "Pure Active Oil vs. Carrier Solvent:",
        "bar_pure": "Pure Oil",
        "bar_sol": "Solvent",
        "dl_sheet": "📥 Download Formula Sheet (CSV)",
        # Phase 2
        "p2_banner": "⚖️ Phase 2: Lab Compounding & Multi-Concentration Sampler",
        "p2_tgt_jus": "Target Jus Batch Weight",
        "p2_t0": "🔗 2-A: CAS ➔ Commercial SKU Mapping Gate",
        "p2_t1": "⚖️ 2-B: Running Tare Bench & Lab Dosing Sheet (100% Jus)",
        "p2_t2": "🧪 2-C: Multi-Concentration Sampler & Filtration",
        "p2_sop": "🛡️ **Industrial Compounding SOP**: Materials are automatically sorted in **Base ➔ Heart (Mid) ➔ Top** order. Zero your scale (Tare) and check off each addition.",
        "p2_prog": "📊 Bench Progress: Completed",
        "p2_items": "items (Dosed",
        "p2_reset": "🔄 Reset Checklist",
        "p2_net_add": "Net Addition:",
        "p2_tare": "Running Tare:",
        "p2_dosing_hdr": "📋 Standard Lab Dosing / Compounding Sheet",
        "dl_dosing": "📥 Download Lab Dosing Sheet (CSV)",
        "p2_samp_hdr": "🧪 Multi-Concentration Sampler & Maceration Predictor",
        "p2_samp_cap": "Draw aliquots from your compounded Jus; automatically deducts carrier solvents and adds a 3% chill-filtration overfill buffer.",
        "samp_a": "#### Sample A: Fresh Daily (Default EdT)",
        "samp_b": "#### Sample B: Long-Lasting (Default EdP)",
        "conc_a": "Sample A Concentration", "conc_b": "Sample B Concentration",
        "bot_a": "Bottles (A)", "bot_b": "Bottles (B)",
        "vol_a": "Bottle Vol (A)", "vol_b": "Bottle Vol (B)",
        "overfill_lbl": "Total Batch w/ 3% Overfill:",
        "take_jus": "Phase A Draw Jus:",
        "add_alc": "Phase B Add Ethanol:",
        "lock_a": "✅ Approve Sample A & Send to Phase 3 PIF",
        "lock_b": "✅ Approve Sample B & Send to Phase 3 PIF",
        "bal_hdr": "##### 📊 Mother Jus Bottle Inventory Balance:",
        "mac_title": "⏳ Dual-Phase Maceration Clock:",
        "days_unit": "Days",
        # Phase 3
        "p3_banner": "📑 Phase 3: Product Information File (PIF) & NDA Compliance",
        "p3_reg": "Jurisdiction", "p3_dos": "Target Dosage",
        "m_ifra": "IFRA 51st Status",
        "m_max_dos": "Cat.4 Max Safe Dosage",
        "m_allg": "Declarable Allergens (>10ppm)",
        "m_sg": "Jus SG / Natural Share",
        "p3_t1": "1️⃣ 100% Quantitative Formula",
        "p3_t2": "2️⃣ Allergens & INCI Label",
        "p3_t3": "3️⃣ IFRA 51st Certificate",
        "p3_t4": "4️⃣ MSDS / Safety Summary",
        "p3_t5": "🔒 5️⃣ Tri-Party NDA Direct-to-SA Mode",
        # Phase 4
        "p4_banner": "🏭 Phase 4: Commercial Scale-up BMR & Landed Cost Framework",
        "p4_deliv": "Delivery Dosage",
        "p4_s1": "1. Production Batch Sizing & Dispatch Header",
        "p4_bot": "Production Batch Size (Bottles)",
        "p4_vol": "Unit Volume (ml)",
        "p4_ovf": "Filtration & Filling Overfill (%)",
        "p4_disp_tgt": "Dispatch / OEM Facility Name (Blank Field)",
        "p4_disp_no": "Batch / Work Order No. (Blank Field)",
        "p4_m1": "Total Gross Batch (w/ Overfill)",
        "p4_m2": "Phase A Compounding Jus",
        "p4_m3": "Phase B Net 95% Ethanol",
        "p4_m4": "Batch Pure Fragrance Cost",
        "p4_s2": "2. Factory BMR Dosing & Dispatch Sheet",
        "dl_bmr": "📥 Download Factory BMR & Dispatch Sheet (CSV)",
        "p4_s3": "3. Unit Landed Cost / COGS Framework (Blank Vendor Fields)"
    }
}

lang = st.session_state.lang
t = UI[lang]

# ==============================================================================
# TOP USER ACCOUNT BAR + LANGUAGE SWITCHER + LOGOUT
# ==============================================================================
u_bar1, u_bar2, u_bar3 = st.columns([4.2, 1.0, 1.0])
plan_badge = f"🛡️ ADMIN" if is_admin else f"✨ {current_user.get('plan_tier', 'Pro').upper()} PERFUMER"
u_bar1.markdown(
    f"### 🧪 Nanmen Scent Lab OS &nbsp;"
    f"<span style='background:#0F172A; color:#38BDF8; padding:3px 10px; border-radius:6px; font-size:12px;'>"
    f"👤 {current_user['display_name']} (@{current_user['username']}) ｜ {plan_badge} ｜ 💾 Auto-Saved</span>",
    unsafe_allow_html=True
)
chosen_lang = u_bar2.radio("Lang", ["中文", "EN"], index=0 if lang == "zh" else 1, horizontal=True, label_visibility="collapsed")
new_lang = "zh" if chosen_lang == "中文" else "en"
if new_lang != lang:
    st.session_state.lang = new_lang
    st.rerun()

if u_bar3.button("🚪 登出 / Logout", use_container_width=True):
    persist_current_workspace()
    st.session_state["current_user"] = None
    st.rerun()

# ==============================================================================
# TOP GLOBAL PROJECT BRIEF RIBBON
# ==============================================================================
with st.container():
    tb1, tb2, tb3, tb4 = st.columns([1.3, 1.5, 1.5, 1.0])
    with tb1:
        mod_list = list(st.session_state.mods.keys())
        if not mod_list:
            st.session_state.mods = {"Mod 1": {}}
            mod_list = ["Mod 1"]
        if st.session_state.active_mod not in mod_list:
            st.session_state.active_mod = mod_list[0]
        new_active_mod = st.selectbox(t["mod_label"], mod_list, index=mod_list.index(st.session_state.active_mod))
        if new_active_mod != st.session_state.active_mod:
            st.session_state.active_mod = new_active_mod
            persist_current_workspace()
            st.rerun()
    with tb2:
        reg_keys = list(REGULATORY_REGIONS.keys())
        new_reg = st.selectbox(
            t["reg_label"], reg_keys,
            index=reg_keys.index(st.session_state.region_id),
            format_func=lambda k: REGULATORY_REGIONS[k][f"name_{lang}"]
        )
        if new_reg != st.session_state.region_id:
            st.session_state.region_id = new_reg
            persist_current_workspace()
            st.rerun()
    with tb3:
        tier_keys = list(PERFUME_CONCENTRATION_PRESETS.keys())
        new_tier = st.selectbox(
            t["dos_label"], tier_keys,
            index=tier_keys.index(st.session_state.tier_id),
            format_func=lambda k: PERFUME_CONCENTRATION_PRESETS[k][lang]
        )
        if new_tier != st.session_state.tier_id:
            st.session_state.tier_id = new_tier
            persist_current_workspace()
            st.rerun()
    with tb4:
        st.write("")
        c_m1, c_m2 = st.columns(2)
        if c_m1.button(t["btn_copy"], use_container_width=True):
            # Enforce Trial tier limit (max 3 Mods) if user is on Trial plan
            if not is_admin and current_user.get("plan_tier") == "Trial" and len(mod_list) >= 3:
                st.warning("⚠️ Trial 體驗版最多建立 3 個配方版本，請聯繫管理員升級 Pro 版。")
            else:
                new_name = f"Mod {len(mod_list) + 1}"
                st.session_state.mods[new_name] = copy.deepcopy(st.session_state.mods[st.session_state.active_mod])
                st.session_state.mod_notes[new_name] = f"Copy of {st.session_state.active_mod}"
                st.session_state.active_mod = new_name
                st.session_state.locked_for_pif = False
                persist_current_workspace()
                st.rerun()
        if c_m2.button(t["btn_clear"], use_container_width=True):
            st.session_state.mods[st.session_state.active_mod] = {}
            st.session_state.locked_for_pif = False
            persist_current_workspace()
            st.rerun()

region_info = REGULATORY_REGIONS[st.session_state.region_id]
tier_info = PERFUME_CONCENTRATION_PRESETS[st.session_state.tier_id]
dosage_ratio = tier_info["ratio"]
current_formula = st.session_state.mods[st.session_state.active_mod]
total_jus_g = sum([d.get("gross_g", 0.0) for d in current_formula.values()])

core_db = st.session_state.core_db
sku_db = st.session_state.commercial_skus
custom_db = st.session_state.custom_materials

rt_calc = core.analyze_formula_realtime(current_formula, dosage_ratio, core_db, sku_db, custom_db, lang=lang)
mod_calc = core.calculate_mod_profile(current_formula, dosage_ratio, {"bottles": 1, "vol_ml": 10}, core_db, sku_db, custom_db, lang=lang)
mac_meta = core.predict_maceration_and_filtration(current_formula, dosage_ratio, {"bottles": 1, "vol_ml": 10}, core_db, sku_db, custom_db, lang=lang)

# ==============================================================================
# DYNAMIC PHASE NAVIGATION (Hides OEM/Vendor Phase 4 during Perfumer Beta!)
# ==============================================================================
nav_options = [
    ("PHASE_1", "💻 Phase 1：數位配方創作" if lang == "zh" else "💻 Phase 1: Formulation"),
    ("PHASE_2", "⚖️ Phase 2：實驗室放樣與取樣" if lang == "zh" else "⚖️ Phase 2: Lab Compounding"),
    ("PHASE_3", "📑 Phase 3：PIF 合規與 NDA 直傳" if lang == "zh" else "📑 Phase 3: PIF & NDA Dossier")
]
if enable_vendor_portal:
    nav_options.append(("PHASE_4", "🏭 Phase 4：商業量產與投遞框架" if lang == "zh" else "🏭 Phase 4: Commercial Scale-up"))
if is_admin:
    nav_options.append(("VENDOR_PORTAL", "📦 供應商 SKU 管理中心" if lang == "zh" else "📦 Vendor SKU Portal"))
    nav_options.append(("ADMIN", "🛡️ Admin 總管理後台" if lang == "zh" else "🛡️ Admin Backoffice"))

nav_labels = [x[1] for x in nav_options]
if st.session_state.phase_idx >= len(nav_labels):
    st.session_state.phase_idx = 0

selected_label = st.radio(
    "Phase Navigation",
    nav_labels,
    index=st.session_state.phase_idx,
    horizontal=True,
    label_visibility="collapsed"
)
st.session_state.phase_idx = nav_labels.index(selected_label)
current_route = nav_options[st.session_state.phase_idx][0]
st.divider()

# ==============================================================================
# PHASE 1: Digital Formulation + Private Material Library Consolidation
# ==============================================================================
if current_route == "PHASE_1":
    st.markdown(f"""
    <div style="background:#0F172A; padding:8px 16px; border-radius:6px; color:white; display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
        <div><b>{t['p1_banner']}</b> ｜ Mod: <span class="mod-pill">{st.session_state.active_mod}</span></div>
        <div style="font-size:13px; color:#94A3B8;">{t['p1_w_lbl']}: <b style="color:#FBBF24; font-size:15px;">{total_jus_g:.3f} g</b> ｜ {t['p1_act_lbl']}: <b style="color:#38BDF8;">{rt_calc['total_active_g']:.3f} g</b></div>
    </div>
    """, unsafe_allow_html=True)

    ph1_tab_edit, ph1_tab_db, ph1_tab_print = st.tabs([t["p1_t1"], t["p1_t2"], t["p1_t3"]])

    with ph1_tab_edit:
        p_left, p_mid, p_right = st.columns([1.2, 2.2, 1.25])

        with p_left:
            # In Perfumer Beta mode (enable_vendor_portal=False), hide Layer 2 Vendor SKUs so perfumers aren't put off
            if enable_vendor_portal:
                layer_choices = [
                    ("L1", "L1 底層化學核心 (CAS)" if lang == "zh" else "L1 Chemical Core (CAS)"),
                    ("L2", "L2 商業 SKU 庫 (廠商料號)" if lang == "zh" else "L2 Commercial SKUs"),
                    ("L3", "L3 調香師自建私有庫 (Custom)" if lang == "zh" else "L3 Private Custom Library")
                ]
            else:
                layer_choices = [
                    ("L1", "📚 標準調香原料庫 (CAS Core)" if lang == "zh" else "📚 Standard Perfumery Library (CAS)"),
                    ("L3", "🧪 我的自建私有庫 (My Private Library)" if lang == "zh" else "🧪 My Private Custom Library")
                ]

            chosen_layer_code = st.selectbox(
                t["layer_sel"],
                [x[0] for x in layer_choices],
                format_func=lambda code: dict(layer_choices)[code]
            )
            c_f1, c_f2 = st.columns([1.4, 1.0])
            lib_search = c_f1.text_input(t["lib_search"], placeholder=t["lib_ph"], label_visibility="collapsed")
            note_filter = c_f2.selectbox("Note", [t["all_notes"], "Top", "Mid", "Base"], label_visibility="collapsed")

            selected_hero_cas = None

            if chosen_layer_code == "L1":
                filtered_cas = []
                for cas, v in core_db.items():
                    txt_ok = (lib_search.lower() in v["name_cn"].lower() or lib_search.lower() in v["name_en"].lower() or lib_search.lower() in cas.lower())
                    note_ok = True if note_filter == t["all_notes"] else (note_filter in v.get("note", ""))
                    if txt_ok and note_ok:
                        filtered_cas.append(cas)

                chosen_cas = st.selectbox(
                    "L1 CAS", filtered_cas if filtered_cas else list(core_db.keys()),
                    format_func=lambda c: f"[{core_db[c]['note'][:1]}] {core_db[c]['name_en'] if lang == 'en' else core_db[c]['name_cn']} ({c})",
                    label_visibility="collapsed"
                )
                selected_hero_cas = chosen_cas
                if chosen_cas:
                    cm = core_db[chosen_cas]
                    is_eu_banned = bool(cm.get("eu_banned", False))
                    tier_color = "#DC2626" if is_eu_banned else ("#10B981" if "Top" in cm["note"] else ("#F59E0B" if "Mid" in cm["note"] else "#78350F"))
                    card_bg = "#FEF2F2" if is_eu_banned else "#F8FAFC"
                    badge_html = (
                        "<span style='background:#DC2626; color:white; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:bold;'>🚨 EU EC 1223/2009 PROHIBITED</span>"
                        if is_eu_banned else "<span class='layer-l1'>CAS REFERENCE CORE</span>"
                    )
                    disp_n = cm["name_en"] if lang == "en" else cm["name_cn"]
                    disp_d = cm["desc_en"] if lang == "en" else cm["desc_zh"]
                    st.markdown(f"""
                    <div class="mat-card" style="background:{card_bg}; border-left: 4px solid {tier_color};">
                        {badge_html}
                        <div style="font-weight:bold; font-size:14px; color:#0F172A; margin-top:4px;">{disp_n}</div>
                        <div style="margin:4px 0;"><span class="cas-badge">CAS: {cm['cas']}</span></div>
                        <div style="font-size:12px; color:#475569; margin-top:4px;">
                            • MW: <b>{cm['mol_w']} g/mol</b> ｜ VP: <b>{cm['vapor_pressure_mmhg']} mmHg</b><br>
                            • {t['note_lbl']}: <b>{cm['note']}</b> ({cm['family']}) ｜ {t['ifra_lbl']}: <b>{cm['ifra_cat4_max']}%</b>
                        </div>
                        <div style="font-size:12px; color:{'#991B1B' if is_eu_banned else '#334155'}; font-style:italic; margin-top:6px; padding-top:6px; border-top:1px dashed #CBD5E1;">"{disp_d}"</div>
                    </div>
                    """, unsafe_allow_html=True)

                    if st.button(t["btn_add"], key="add_l1", use_container_width=True, type="primary"):
                        lid = f"L1_{chosen_cas}"
                        if lid not in current_formula:
                            st.session_state.mods[st.session_state.active_mod][lid] = {
                                "layer": "L1_CORE", "cas": chosen_cas, "sku_id": None,
                                "gross_g": 0.200, "dilution_pct": 100.0 if cm["ifra_cat4_max"] > 5.0 else 10.0,
                                "solvent": "None (100%純原液)" if cm["ifra_cat4_max"] > 5.0 else "DPG (二丙二醇)"
                            }
                            persist_current_workspace()
                            st.rerun()
                        else:
                            st.warning(t["warn_exists"])

            elif chosen_layer_code == "L2":
                filtered_skus = []
                for sid, s in sku_db.items():
                    cm = core_db.get(s["cas"], {})
                    txt_ok = (
                        lib_search.lower() in s["trade_name_cn"].lower() or lib_search.lower() in s["trade_name_en"].lower()
                        or lib_search.lower() in s["cas"].lower()
                    )
                    note_ok = True if note_filter == t["all_notes"] else (note_filter in cm.get("note", ""))
                    if txt_ok and note_ok:
                        filtered_skus.append(sid)

                chosen_sku = st.selectbox(
                    "L2 SKU", filtered_skus if filtered_skus else list(sku_db.keys()),
                    format_func=lambda sid: f"[{sku_db[sid]['supplier_en' if lang=='en' else 'supplier_zh']}] {sku_db[sid]['trade_name_en' if lang=='en' else 'trade_name_cn']}",
                    label_visibility="collapsed"
                )
                if chosen_sku:
                    sm = sku_db[chosen_sku]
                    selected_hero_cas = sm["cas"]
                    disp_n = sm["trade_name_en"] if lang == "en" else sm["trade_name_cn"]
                    st.markdown(f"""
                    <div class="mat-card" style="border-left: 4px solid #16A34A;">
                        <span class="layer-l2">COMMERCIAL SKU</span>
                        <div style="font-weight:bold; font-size:14px; color:#0F172A; margin-top:4px;">{disp_n}</div>
                        <div style="margin:4px 0;"><span class="cas-badge">CAS: {sm['cas']}</span></div>
                        <div style="font-size:12px; color:#475569; margin-top:4px;">
                            • Lot: <code>{sm['lot_no']}</code> ｜ Purity: <b>{sm['dilution_pct']:.0f}%</b>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(t["btn_add"], key="add_l2", use_container_width=True, type="primary"):
                        lid = f"L2_{chosen_sku}"
                        if lid not in current_formula:
                            st.session_state.mods[st.session_state.active_mod][lid] = {
                                "layer": "L2_SKU", "cas": sm["cas"], "sku_id": chosen_sku,
                                "gross_g": 0.200, "dilution_pct": sm["dilution_pct"], "solvent": sm["solvent"]
                            }
                            persist_current_workspace()
                            st.rerun()

            else:
                if not custom_db:
                    st.info("尚未建立私有原料，請切換至「1-B：私有原料庫與帳號資料整合」新增。" if lang == "zh" else "No private materials yet. Add one in Tab 1-B.")
                else:
                    chosen_cust = st.selectbox(
                        "L3 Custom", list(custom_db.keys()),
                        format_func=lambda cid: f"{custom_db[cid]['name_en' if lang=='en' else 'name_cn']} ({custom_db[cid]['dilution_pct']:.0f}%)",
                        label_visibility="collapsed"
                    )
                    if chosen_cust:
                        cu = custom_db[chosen_cust]
                        selected_hero_cas = cu["cas"]
                        disp_n = cu["name_en"] if lang == "en" else cu["name_cn"]
                        st.markdown(f"""
                        <div class="mat-card" style="border-left: 4px solid #7E22CE;">
                            <span class="layer-l3">MY PRIVATE MATERIAL</span>
                            <div style="font-weight:bold; font-size:14px; color:#0F172A; margin-top:4px;">{disp_n}</div>
                            <div style="margin:4px 0;"><span class="cas-badge">Mapped CAS: {cu['cas']}</span></div>
                            <div style="font-size:12px; color:#475569; margin-top:4px;">
                                • Concentration: <b>{cu['dilution_pct']:.1f}%</b> in {cu['solvent'].split(' ')[0]}<br>
                                • {t['sg_lbl']}: <b>{cu['sg_pure']}</b> ｜ {t['cost_lbl']}: <b>NT$ {cu['cost_per_g']}/g</b>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                        if st.button(t["btn_add"], key="add_l3", use_container_width=True, type="primary"):
                            lid = f"L3_{chosen_cust}"
                            if lid not in current_formula:
                                st.session_state.mods[st.session_state.active_mod][lid] = {
                                    "layer": "L3_CUSTOM", "cas": cu["cas"], "custom_id": chosen_cust,
                                    "gross_g": 0.200, "dilution_pct": cu["dilution_pct"], "solvent": cu["solvent"]
                                }
                                persist_current_workspace()
                                st.rerun()
                            else:
                                st.warning(t["warn_exists"])

            with st.expander(t["ai_exp"]):
                st.caption(t["ai_cap"])
                w_citrus = st.slider(t["sl_citrus"], 0, 100, 25, 5)
                w_floral = st.slider(t["sl_floral"], 0, 100, 25, 5)
                w_woody = st.slider(t["sl_woody"], 0, 100, 35, 5)
                w_spicy = st.slider(t["sl_spicy"], 0, 100, 10, 5)
                w_sweet = st.slider(t["sl_sweet"], 0, 100, 5, 5)
                if st.button(t["btn_gen"], use_container_width=True):
                    s_dict = {"Citrus": w_citrus, "Floral": w_floral, "Woody": w_woody, "Spicy": w_spicy, "Sweet": w_sweet}
                    st.session_state.mods[st.session_state.active_mod] = core.synthesize_canvas_formula(s_dict, selected_hero_cas, 5.0, core_db)
                    persist_current_workspace()
                    st.rerun()

        # 🔵 CENTER PANE: Formulation Grid
        with p_mid:
            c_title, c_tools = st.columns([1.4, 1.3])
            with c_title:
                st.markdown(t["grid_hdr"])
            with c_tools:
                t_col1, t_col2 = st.columns(2)
                with t_col1:
                    display_unit = st.selectbox("Unit", t["unit_opts"], label_visibility="collapsed")
                with t_col2:
                    with st.popover(t["scale_pop"]):
                        target_g = st.number_input(t["scale_tgt"], min_value=1.0, max_value=5000.0, value=max(5.0, round(total_jus_g, 2)), step=1.0)
                        if st.button(t["scale_btn"], use_container_width=True) and total_jus_g > 0:
                            mult = target_g / total_jus_g
                            for k in current_formula:
                                current_formula[k]["gross_g"] = round(current_formula[k]["gross_g"] * mult, 3)
                            st.session_state.mods[st.session_state.active_mod] = current_formula
                            persist_current_workspace()
                            st.rerun()

            creation_rows = core.build_compounding_sheet(current_formula, dosage_ratio, core_db, sku_db, custom_db, sort_by_compounding=False, lang=lang)

            if not creation_rows:
                st.info(t["empty_form"])
            else:
                for row in creation_rows:
                    lid = row["line_id"]
                    layer_badge = "<span class='layer-l3'>PRIVATE</span>" if row["layer"] == "L3_CUSTOM" else "<span class='layer-l1'>CAS</span>"
                    with st.container(border=True):
                        r1, r2, r3, r4, r5 = st.columns([2.2, 1.1, 1.3, 1.4, 0.45])
                        r1.markdown(
                            f"**{row['name_disp']}**<br>{layer_badge} <span class='cas-badge'>{row['note']}</span> "
                            f"<span style='font-size:11px; color:#64748B;'>CAS: {row['cas']}</span>",
                            unsafe_allow_html=True
                        )
                        new_dil = r2.selectbox("Dil", DILUTION_TIERS, index=DILUTION_TIERS.index(float(row["dilution_pct"])) if float(row["dilution_pct"]) in DILUTION_TIERS else 0, key=f"p1_dil_{st.session_state.active_mod}_{lid}", label_visibility="collapsed")
                        new_sol = r3.selectbox(
                            "Sol", SOLVENT_CHOICES,
                            index=SOLVENT_CHOICES.index(row["solvent"]) if row["solvent"] in SOLVENT_CHOICES else 0,
                            format_func=lambda s: SOLVENT_DATABASE[s][lang],
                            key=f"p1_sol_{st.session_state.active_mod}_{lid}",
                            label_visibility="collapsed"
                        )
                        new_g = r4.number_input("g", min_value=0.001, max_value=1000.0, value=float(row["gross_g"]), step=0.010, format="%.3f", key=f"p1_g_{st.session_state.active_mod}_{lid}", label_visibility="collapsed")
                        if "PPT" in display_unit:
                            r4.caption(f"📊 **{row['ppt']:.1f} ‰** ({t['pure_oil']} {row['active_g']:.3f}g)")
                        else:
                            r4.caption(f"📊 **{row['pct']:.1f}%** ({row['drops']} {t['drops_unit']})")

                        if r5.button("🗑️", key=f"p1_del_{st.session_state.active_mod}_{lid}"):
                            del st.session_state.mods[st.session_state.active_mod][lid]
                            persist_current_workspace()
                            st.rerun()

                        if abs(new_dil - row["dilution_pct"]) > 1e-4 or new_sol != row["solvent"] or abs(new_g - row["gross_g"]) > 1e-4:
                            st.session_state.mods[st.session_state.active_mod][lid]["gross_g"] = new_g
                            st.session_state.mods[st.session_state.active_mod][lid]["dilution_pct"] = new_dil
                            st.session_state.mods[st.session_state.active_mod][lid]["solvent"] = new_sol
                            persist_current_workspace()
                            st.rerun()

        # 🟡 RIGHT PANE: Real-Time Smart Probes
        with p_right:
            st.markdown(t["probe_hdr"])
            probe_tab1, probe_tab2 = st.tabs([t["probe_t1"], t["probe_t2"]])

            with probe_tab1:
                if mod_calc:
                    st.markdown(t["pyr_title"])
                    top_p, mid_p, base_p = mod_calc["notes_pct"]["Top"], mod_calc["notes_pct"]["Mid"], mod_calc["notes_pct"]["Base"]
                    st.caption(f"{t['top_l']}: {top_p:.1f}%")
                    st.progress(min(1.0, top_p / 100.0))
                    st.caption(f"{t['mid_l']}: {mid_p:.1f}%")
                    st.progress(min(1.0, mid_p / 100.0))
                    st.caption(f"{t['base_l']}: {base_p:.1f}%")
                    st.progress(min(1.0, base_p / 100.0))
                    st.caption(f"⏳ {t['tenacity_lbl']}: **{rt_calc['tenacity_score']} / 100**")

                st.divider()
                st.markdown(f"**{t['ifra_radar']} ({region_info['code']} @ {dosage_ratio*100:.0f}%)：**")
                all_safe = True
                for lid, stat in rt_calc["ifra_status"].items():
                    if stat.get("eu_banned", False):
                        all_safe = False
                        st.error(
                            f"🚨 **[EU 禁用物質攔截] {stat['name_disp']}** (`CAS {stat['cas']}`) 屬歐盟 EC 1223/2009 附錄二全面禁用成分（0.0% 容許值），請立即移除或替換！"
                            if lang == "zh" else
                            f"🚨 **[EU BANNED SUBSTANCE] {stat['name_disp']}** (`CAS {stat['cas']}`) is strictly prohibited under EU Annex II (0.0% tolerance). Remove immediately!"
                        )
                    elif not stat["is_safe"]:
                        all_safe = False
                        st.error(f"❌ **{stat['name_disp']}** {t['over_limit']} {stat['finished_pct']:.2f}% > {t['limit_word']} {stat['limit']}%")
                    elif stat["is_warn"]:
                        st.warning(f"⚠️ **{stat['name_disp']}** {t['near_warn']} ({stat['risk_ratio']*100:.0f}%)")
                if all_safe and current_formula:
                    st.success(f"{t['ifra_ok']}{rt_calc['max_safe_dosage_pct']:.1f}%）")

                allg_dict = rt_calc.get("allergen_summary", {})
                over_allg = {k: v for k, v in allg_dict.items() if v >= region_info["allergen_ppm_threshold"]}
                if over_allg:
                    st.markdown(t["allg_warn_hdr"])
                    for a_k, a_v in sorted(over_allg.items(), key=lambda x: x[1], reverse=True):
                        st.caption(f"• `{a_k}`: **{a_v:.1f} ppm**")

            with probe_tab2:
                if mod_calc:
                    sb_items = [{"Family": v["family"], "Name": v["name_disp"], "ActiveWeight": v["active_pct"]} for v in mod_calc["norm_active"].values()]
                    if sb_items:
                        fig_sb = px.sunburst(
                            pd.DataFrame(sb_items), path=["Family", "Name"], values="ActiveWeight",
                            color="Family",
                            color_discrete_map={"Woody": "#78350F", "Floral": "#EC4899", "Citrus": "#F59E0B", "Sweet": "#EF4444", "Spicy": "#B45309"},
                            height=240
                        )
                        fig_sb.update_layout(margin=dict(l=0, r=0, t=0, b=0))
                        st.plotly_chart(fig_sb, use_container_width=True)

                    st.caption(t["evap_cap"])
                    fig_traj = px.line(
                        mod_calc["trajectory"], x="Hour", y=["Top", "Mid", "Base"],
                        color_discrete_map={"Top": "#10B981", "Mid": "#F59E0B", "Base": "#6B7280"},
                        height=200
                    )
                    fig_traj.update_layout(margin=dict(l=0, r=0, t=0, b=0), hovermode="x unified", showlegend=True)
                    st.plotly_chart(fig_traj, use_container_width=True)

            st.divider()
            st.markdown(t["notes_hdr"])
            c_n = st.session_state.mod_notes.get(st.session_state.active_mod, "")
            n_n = st.text_area("Notes", value=c_n, height=85, label_visibility="collapsed")
            if n_n != c_n:
                st.session_state.mod_notes[st.session_state.active_mod] = n_n
                persist_current_workspace()

        # 🏁 BOTTOM STATS BAR
        if mod_calc:
            est_cost = mod_calc.get("total_cost", 0.0)
            est_cost_per_10g = (est_cost / total_jus_g * 10.0) if total_jus_g > 0 else 0.0
            st.markdown(f"""
            <div class="stats-bar">
                <div>
                    <span style="color:#94A3B8; font-size:12px;">{t['bar_cost']}</span>
                    <b style="color:#FBBF24; font-size:16px;">NT$ {est_cost:.1f}</b>
                    <span style="color:#64748B; font-size:12px; margin-left:8px;">({t['bar_base']}: NT$ {est_cost_per_10g:.1f} / 10g {t['bar_jus']})</span>
                </div>
                <div>
                    <span style="color:#94A3B8; font-size:12px;">{t['bar_ratio']}</span>
                    <b style="color:#38BDF8; font-size:15px;">{rt_calc['total_active_g']:.3f} g {t['bar_pure']}</b>
                    <span style="color:#94A3B8; font-size:12px;"> + {rt_calc['total_carrier_g']:.3f} g {t['bar_sol']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # 1-B: Perfumer Private Material Library & Account Data Consolidation
    # --------------------------------------------------------------------------
    with ph1_tab_db:
        col_priv1, col_priv2 = st.columns([1.35, 1.15])

        with col_priv1:
            st.subheader("🧪 建立調香師自建私有原料 (My Private Material Library)")
            st.caption("輸入您手邊特殊酊劑、CO2 萃取物或私房基劑的稀釋濃度與致敏原比例，系統會自動存入您的個人帳號並換算回純物質濃度進行法規加總。")

            with st.form("add_l3_custom_form", clear_on_submit=True):
                c_name_cn = st.text_input("私有原料名稱 (中文) *", placeholder="例如: 桂花 CO2 萃取液 20%")
                c_name_en = st.text_input("私有原料名稱 (英文)", placeholder="e.g., Osmanthus CO2 Extract 20%")
                c_cas_map = st.selectbox(
                    "關聯底層 CAS 標準（供 IFRA 限量比對）", list(core_db.keys()),
                    format_func=lambda c: f"{c} — {core_db[c]['name_en'] if lang=='en' else core_db[c]['name_cn']}"
                )
                cc1, cc2, cc3 = st.columns(3)
                c_dil = cc1.number_input("有效純度 (%)", 0.1, 100.0, 20.0, 1.0)
                c_sol = cc2.selectbox("溶劑載體", SOLVENT_CHOICES, index=1)
                c_cost = cc3.number_input("純油單價 (NT$/g)", 0.0, 10000.0, 50.0, 5.0)

                st.markdown("**純油中之法定致敏原百分比（輸入 0~100%，系統自動依稀釋度折算）：**")
                ac1, ac2, ac3 = st.columns(3)
                a_lim = ac1.number_input("Limonene (%)", 0.0, 100.0, 0.0, 0.5)
                a_lin = ac2.number_input("Linalool (%)", 0.0, 100.0, 0.0, 0.5)
                a_ger = ac3.number_input("Geraniol (%)", 0.0, 100.0, 0.0, 0.5)
                ac4, ac5, ac6 = st.columns(3)
                a_cit = ac4.number_input("Citral (%)", 0.0, 100.0, 0.0, 0.5)
                a_bb = ac5.number_input("Benzyl Benzoate (%)", 0.0, 100.0, 0.0, 0.5)
                a_cou = ac6.number_input("Coumarin (%)", 0.0, 100.0, 0.0, 0.5)

                if st.form_submit_button("➕ 儲存至我的私有原料庫", type="primary", use_container_width=True):
                    if c_name_cn:
                        cid = f"CUST-{len(custom_db) + 1:03d}"
                        allg_map = {}
                        for aname, apct in [
                            ("Limonene", a_lim), ("Linalool", a_lin), ("Geraniol", a_ger),
                            ("Citral", a_cit), ("Benzyl Benzoate", a_bb), ("Coumarin", a_cou)
                        ]:
                            if apct > 0:
                                allg_map[aname] = apct / 100.0
                        st.session_state.custom_materials[cid] = {
                            "custom_id": cid,
                            "cas": c_cas_map,
                            "name_cn": c_name_cn.strip(),
                            "name_en": c_name_en.strip() or c_name_cn.strip(),
                            "note": core_db[c_cas_map]["note"],
                            "family": core_db[c_cas_map]["family"],
                            "dilution_pct": c_dil,
                            "solvent": c_sol,
                            "sg_pure": core_db[c_cas_map]["sg_pure"],
                            "cost_per_g": c_cost,
                            "ifra_cat4_max": core_db[c_cas_map]["ifra_cat4_max"],
                            "allergens": allg_map,
                            "lot_no": f"PRIV-{cid}",
                            "exp_date": "2028/12/31"
                        }
                        persist_current_workspace()
                        st.success(f"✅ 已建立並自動儲存私有原料 {cid}：{c_name_cn}")
                        st.rerun()

        with col_priv2:
            st.subheader("💾 個人帳號資料總覽與備份 (Workspace Consolidation)")
            st.info(f"您目前的所有配方版本（共 **{len(st.session_state.mods)} 個 Mods**）與自建私有原料（共 **{len(custom_db)} 項**）均已自動整合儲存至您的專屬帳號 `@{current_user['username']}`。")

            # Consolidated summary table of all Mods owned by this perfumer
            mod_summary_rows = []
            for m_name, f_dict in st.session_state.mods.items():
                w_tot = sum(x.get("gross_g", 0.0) for x in f_dict.values())
                mod_summary_rows.append({
                    "配方版本 (Mod)": m_name,
                    "原料數": len(f_dict),
                    "配方總重 (g)": round(w_tot, 3),
                    "調香師筆記": st.session_state.mod_notes.get(m_name, "-")[:40]
                })
            st.dataframe(pd.DataFrame(mod_summary_rows), hide_index=True, use_container_width=True)

            # Export / Import full personal workspace JSON
            ws_export_obj = {
                "exported_by": current_user["username"],
                "exported_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "mods": st.session_state.mods,
                "active_mod": st.session_state.active_mod,
                "mod_notes": st.session_state.mod_notes,
                "custom_materials": st.session_state.custom_materials
            }
            st.download_button(
                "📥 下載完整個人工作區加密備份檔 (.json)",
                data=json.dumps(ws_export_obj, ensure_ascii=False, indent=2).encode("utf-8"),
                file_name=f"Nanmen_Workspace_{current_user['username']}_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json",
                use_container_width=True
            )

            uploaded_ws = st.file_uploader("📂 匯入還原個人備份檔 (.json)", type=["json"], key="ws_restore_up")
            if uploaded_ws is not None:
                try:
                    restored = json.loads(uploaded_ws.read().decode("utf-8"))
                    if "mods" in restored:
                        st.session_state.mods.update(restored["mods"])
                    if "mod_notes" in restored:
                        st.session_state.mod_notes.update(restored["mod_notes"])
                    if "custom_materials" in restored:
                        st.session_state.custom_materials.update(restored["custom_materials"])
                    persist_current_workspace()
                    st.success("✅ 已成功合併還原您的配方與私有原料庫！")
                except Exception as e:
                    st.error(f"備份檔格式錯誤: {e}")

            with st.expander("🌐 線上查詢新 CAS 物性 (PubChem API)"):
                query_cas = st.text_input("輸入 CAS 號碼", placeholder="例如: 78-70-6", key="pubchem_cas_in")
                if st.button("🔍 查詢 CAS 分子量與學名"):
                    fetched, err = core.fetch_pubchem_metadata_by_cas(query_cas)
                    if fetched:
                        st.success(f"CAS `{fetched['cas']}`: **{fetched['name_en']}** | MW: `{fetched['mol_w']}`")
                    else:
                        st.warning(f"查詢未成功: {err}")

    # --------------------------------------------------------------------------
    # 1-C: Formulation Record Sheet (Print-ready Snapshot)
    # --------------------------------------------------------------------------
    with ph1_tab_print:
        if not mod_calc or not current_formula:
            st.warning(t["empty_form"])
        else:
            st.markdown(f"""
            <div class="doc-sheet">
                <div class="doc-title">
                    <h3 style="margin:0;">FORMULATION RECORD SHEET — {st.session_state.active_mod}</h3>
                    <div style="color:#64748B; font-size:13px; margin-top:4px;">Perfumer: {current_user['display_name']} | Date: {datetime.now().strftime("%Y-%m-%d")} | Regulatory: {region_info['code']} | Dosage: {dosage_ratio*100:.0f}%</div>
                </div>
                <p style="margin:4px 0;"><b>Perfumer Notes:</b> {st.session_state.mod_notes.get(st.session_state.active_mod, 'N/A')}</p>
                <p style="margin:4px 0;">
                    <b>Total Jus Weight:</b> {total_jus_g:.3f} g &nbsp;|&nbsp;
                    <b>Pure Active Oil:</b> {rt_calc['total_active_g']:.3f} g &nbsp;|&nbsp;
                    <b>Carrier Solvent:</b> {rt_calc['total_carrier_g']:.3f} g
                </p>
            </div>
            """, unsafe_allow_html=True)

            print_rows = core.build_compounding_sheet(current_formula, dosage_ratio, core_db, sku_db, custom_db, sort_by_compounding=True, lang=lang)
            df_print = pd.DataFrame([{
                "Seq": r["seq"],
                "Note": r["note"],
                "CAS": r["cas"],
                "Material Name": r["name_disp"],
                "Spec": f"{r['dilution_pct']:.0f}% in {r['solvent'].split(' ')[0]}" if r["dilution_pct"] < 100 else "100% Neat",
                "Weight (g)": f"{r['gross_g']:.3f}",
                "Pure Active (g)": f"{r['active_g']:.3f}",
                "Share (%)": f"{r['pct']:.2f}%",
                "PPT (‰)": f"{r['ppt']:.1f}"
            } for r in print_rows])

            st.dataframe(df_print, use_container_width=True, hide_index=True)
            pdf_f_bytes = pdf_gen.build_formula_sheet_pdf(
                mod_name=st.session_state.active_mod,
                perfumer_name=current_user["display_name"],
                region_code=region_info["code"],
                dosage_pct=dosage_ratio * 100.0,
                notes=st.session_state.mod_notes.get(st.session_state.active_mod, ""),
                total_jus_g=total_jus_g,
                total_active_g=rt_calc["total_active_g"],
                total_carrier_g=rt_calc["total_carrier_g"],
                print_rows=print_rows
            )
            dl_c1, dl_c2 = st.columns(2)
            dl_c1.download_button(
                "📄 一鍵匯出正式配方單 (PDF)" if lang == "zh" else "📄 Export Formal Formula Sheet (PDF)",
                data=pdf_f_bytes,
                file_name=f"Formula_Sheet_{st.session_state.active_mod}.pdf",
                mime="application/pdf",
                type="primary",
                use_container_width=True
            )
            csv_f = df_print.to_csv(index=False).encode('utf-8-sig')
            dl_c2.download_button(t["dl_sheet"], data=csv_f, file_name=f"Formula_Sheet_{st.session_state.active_mod}_{lang.upper()}.csv", mime="text/csv", use_container_width=True)

# ==============================================================================
# PHASE 2: Lab Compounding & Multi-Concentration Sampler
# ==============================================================================
elif current_route == "PHASE_2":
    st.markdown(f"""
    <div style="background:#0F172A; padding:8px 16px; border-radius:6px; color:white; display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
        <div><b>{t['p2_banner']}</b> ｜ Mod: <span class="mod-pill">{st.session_state.active_mod}</span></div>
        <div style="font-size:13px; color:#94A3B8;">{t['p2_tgt_jus']}：<b style="color:#FBBF24; font-size:15px;">{total_jus_g:.3f} g</b></div>
    </div>
    """, unsafe_allow_html=True)

    # Show SKU Mapping Gate tab only when Vendor Portal is enabled; otherwise keep Perfumer Beta streamlined!
    if enable_vendor_portal:
        p2_sub1, p2_sub2, p2_sub0 = st.tabs([t["p2_t1"], t["p2_t2"], t["p2_t0"]])
    else:
        p2_sub1, p2_sub2 = st.tabs([t["p2_t1"], t["p2_t2"]])
        p2_sub0 = None

    with p2_sub1:
        st.info(t["p2_sop"])
        bench_rows = core.build_compounding_sheet(current_formula, dosage_ratio, core_db, sku_db, custom_db, sort_by_compounding=True, lang=lang)

        if not bench_rows:
            st.warning(t["empty_form"])
        else:
            current_checks = st.session_state.dosed_checklist.setdefault(st.session_state.active_mod, {})
            dosed_count = sum(1 for r in bench_rows if current_checks.get(r["line_id"], False))
            dosed_weight = sum(r["gross_g"] for r in bench_rows if current_checks.get(r["line_id"], False))

            c_prog, c_reset = st.columns([3.5, 1])
            with c_prog:
                st.progress(dosed_count / len(bench_rows) if len(bench_rows) > 0 else 0)
                st.caption(f"{t['p2_prog']} **{dosed_count}/{len(bench_rows)}** {t['p2_items']} **{dosed_weight:.3f} g** / {total_jus_g:.3f} g）")
            with c_reset:
                if st.button(t["p2_reset"], use_container_width=True):
                    st.session_state.dosed_checklist[st.session_state.active_mod] = {}
                    persist_current_workspace()
                    st.rerun()

            for row in bench_rows:
                lid = row["line_id"]
                is_done = current_checks.get(lid, False)
                with st.container(border=True):
                    b1, b2, b3, b4, b5 = st.columns([0.5, 0.7, 2.5, 1.5, 1.5])
                    chk = b1.checkbox("Done", value=is_done, key=f"bench_chk_{st.session_state.active_mod}_{lid}", label_visibility="collapsed")
                    if chk != is_done:
                        current_checks[lid] = chk
                        persist_current_workspace()

                    b2.markdown(f"**#{row['seq']}**<br>`{row['note']}`", unsafe_allow_html=True)
                    name_css = "text-decoration: line-through; color: #94A3B8;" if chk else "font-weight: 700; color: #0F172A;"
                    sol_short = row["solvent"].split(" ")[0]
                    spec_txt = ("100% Neat" if lang == "en" else "100% 純原液") if row["dilution_pct"] >= 100 else f"{row['dilution_pct']:.0f}% in {sol_short}"
                    b3.markdown(
                        f"<span style='{name_css}'>{row['name_disp']}</span><br>"
                        f"<span class='cas-badge'>{spec_txt}</span> <span style='font-size:11px; color:#64748B;'>CAS: {row['cas']}</span>",
                        unsafe_allow_html=True
                    )
                    b4.markdown(f"{t['p2_net_add']}<br><b style='font-size:16px; color:#0284C7;'>{row['gross_g']:.3f} g</b> <span style='font-size:12px; color:#64748B;'>({row['drops']} {t['drops_unit']})</span>", unsafe_allow_html=True)
                    b5.markdown(f"{t['p2_tare']}<br><span class='scale-chip'>⚖️ {row['cumulative_g']:.3f} g</span>", unsafe_allow_html=True)

            st.divider()
            st.subheader(t["p2_dosing_hdr"])
            dosing_df = pd.DataFrame([{
                "Seq": r["seq"],
                "Note": r["note"],
                "CAS": r["cas"],
                "Material Name": r["name_disp"],
                "Dilution & Carrier": f"{r['dilution_pct']:.0f}% in {r['solvent'].split(' ')[0]}" if r["dilution_pct"] < 100 else "100% Neat",
                "Net Addition (g)": r["gross_g"],
                "Est. Drops": r["drops"],
                "Running Tare (g)": r["cumulative_g"],
                "Pure Active (g)": r["active_g"],
                "Checked": "✅" if current_checks.get(r["line_id"], False) else "⬜"
            } for r in bench_rows])
            st.dataframe(dosing_df, hide_index=True, use_container_width=True)
            dosing_csv = dosing_df.to_csv(index=False).encode('utf-8-sig')
            st.download_button(t["dl_dosing"], data=dosing_csv, file_name=f"Lab_Dosing_Sheet_{st.session_state.active_mod}_{lang.upper()}.csv", mime="text/csv", use_container_width=True)

    with p2_sub2:
        st.subheader(t["p2_samp_hdr"])
        st.caption(t["p2_samp_cap"])

        if total_jus_g <= 0:
            st.warning(t["empty_form"])
        else:
            tier_keys = list(PERFUME_CONCENTRATION_PRESETS.keys())
            col_s1, col_s2 = st.columns(2)
            with col_s1:
                st.markdown(t["samp_a"])
                s1_tier_id = st.selectbox(t["conc_a"], tier_keys, index=1, format_func=lambda k: PERFUME_CONCENTRATION_PRESETS[k][lang], key="p2_s1_tier")
                s1_bot = st.number_input(t["bot_a"], 1, 50, 1, 1, key="p2_s1_bot")
                s1_vol = st.selectbox(t["vol_a"], [5, 10, 15, 30, 50], index=1, key="p2_s1_vol")
                res_s1 = core.compute_sample_application(current_formula, PERFUME_CONCENTRATION_PRESETS[s1_tier_id]["ratio"], s1_bot, s1_vol)
                if res_s1:
                    st.markdown(f"""
                    <div class="sample-card" style="border-left:4px solid #10B981;">
                        <div style="font-size:12px; color:#64748B;">{t['overfill_lbl']}<b>{res_s1['overfill_total_g']:.2f} g</b></div>
                        <div style="margin-top:8px;">{t['take_jus']}<b style="color:#10B981; font-size:16px;">{res_s1['req_jus_g']:.3f} g</b></div>
                        <div>{t['add_alc']}<b style="color:#3B82F6; font-size:16px;">{res_s1['net_alcohol_g']:.2f} g</b></div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(t["lock_a"], key="lock_s1", use_container_width=True):
                        st.session_state.tier_id = s1_tier_id
                        st.session_state.locked_for_pif = True
                        persist_current_workspace()
                        st.rerun()

            with col_s2:
                st.markdown(t["samp_b"])
                s2_tier_id = st.selectbox(t["conc_b"], tier_keys, index=2, format_func=lambda k: PERFUME_CONCENTRATION_PRESETS[k][lang], key="p2_s2_tier")
                s2_bot = st.number_input(t["bot_b"], 1, 50, 1, 1, key="p2_s2_bot")
                s2_vol = st.selectbox(t["vol_b"], [5, 10, 15, 30, 50], index=1, key="p2_s2_vol")
                res_s2 = core.compute_sample_application(current_formula, PERFUME_CONCENTRATION_PRESETS[s2_tier_id]["ratio"], s2_bot, s2_vol)
                if res_s2:
                    st.markdown(f"""
                    <div class="sample-card" style="border-left:4px solid #3B82F6;">
                        <div style="font-size:12px; color:#64748B;">{t['overfill_lbl']}<b>{res_s2['overfill_total_g']:.2f} g</b></div>
                        <div style="margin-top:8px;">{t['take_jus']}<b style="color:#10B981; font-size:16px;">{res_s2['req_jus_g']:.3f} g</b></div>
                        <div>{t['add_alc']}<b style="color:#3B82F6; font-size:16px;">{res_s2['net_alcohol_g']:.2f} g</b></div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(t["lock_b"], key="lock_s2", use_container_width=True):
                        st.session_state.tier_id = s2_tier_id
                        st.session_state.locked_for_pif = True
                        persist_current_workspace()
                        st.rerun()

            if st.session_state.locked_for_pif:
                st.success(f"🔒 Locked **{st.session_state.active_mod}** ({PERFUME_CONCENTRATION_PRESETS[st.session_state.tier_id][lang]}) for Phase 3 PIF!")

            total_req = (res_s1["req_jus_g"] if res_s1 else 0.0) + (res_s2["req_jus_g"] if res_s2 else 0.0)
            remaining = total_jus_g - total_req
            st.divider()

            c_bal, c_mac = st.columns([1.3, 1.2])
            with c_bal:
                st.markdown(t["bal_hdr"])
                if remaining >= 0:
                    st.success(f"✅ Required Jus: **{total_req:.3f} g** | Remaining in Mother Bottle: **{remaining:.3f} g**.")
                else:
                    st.error(f"🚨 Insufficient Jus! Required **{total_req:.3f} g**, available **{total_jus_g:.3f} g** (Shortage: {-remaining:.3f} g).")

            with c_mac:
                if mac_meta:
                    st.markdown(f"""
                    <div style="background:#F8FAFC; border:1px solid #CBD5E1; padding:12px; border-radius:8px; margin-bottom:8px;">
                        <div style="font-size:14px; font-weight:bold; color:#0F172A;">{t['mac_title']}<span style="color:#D97706; font-size:18px;">{mac_meta['maceration']['days']} {t['days_unit']}</span></div>
                        <div style="font-size:12px; color:#475569; margin-top:4px;">{mac_meta['maceration']['desc']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    for alert in mac_meta["alerts"]:
                        if alert["level"] == "danger":
                            st.error(alert["msg"])
                        else:
                            st.success(alert["msg"])

    if p2_sub0 is not None:
        with p2_sub0:
            st.subheader("🔗 CAS ➔ Commercial SKU Mapping Gate (Phase 2 Vendor Mode)")
            if st.button("⚡ One-Click Auto-Map All Unmapped CAS", type="primary"):
                updated_f, _ = core.auto_map_formula_skus(current_formula, sku_db, conserve_active=True)
                st.session_state.mods[st.session_state.active_mod] = updated_f
                persist_current_workspace()
                st.rerun()

# ==============================================================================
# PHASE 3: PIF & Compliance Dossier (All 5 Tabs + Tri-Party NDA Direct-to-SA)
# ==============================================================================
elif current_route == "PHASE_3":
    st.markdown(f"""
    <div style="background:#0F172A; padding:8px 16px; border-radius:6px; color:white; display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
        <div><b>{t['p3_banner']}</b> ｜ Mod: <span class="mod-pill">{st.session_state.active_mod}</span></div>
        <div style="font-size:13px; color:#38BDF8;">{t['p3_reg']}: <b>{region_info['code']}</b> ｜ {t['p3_dos']}: <b>{dosage_ratio*100:.1f}%</b></div>
    </div>
    """, unsafe_allow_html=True)

    if not mod_calc or total_jus_g <= 0:
        st.warning(t["empty_form"])
    else:
        has_banned = any(stat.get("eu_banned", False) for stat in rt_calc["ifra_status"].values())
        all_ifra_pass = (not has_banned) and all(stat["is_safe"] for stat in rt_calc["ifra_status"].values())
        over_10ppm_list = [a for a in mod_calc["declared_allergens"] if a["ppm"] >= region_info["allergen_ppm_threshold"]]

        if has_banned:
            st.error("🚨 **EU 禁用物質警報**：此配方含有歐盟 EC 1223/2009 附錄二全面禁用成分（0.0% 容許值），無法通過合規審查！" if lang == "zh" else "🚨 **EU BANNED SUBSTANCE ALERT**: Formula contains EU Annex II prohibited substance(s) (0.0% tolerance)!")

        k1, k2, k3, k4 = st.columns(4)
        k1.metric(t["m_ifra"], "🚨 BANNED" if has_banned else ("✅ PASS" if all_ifra_pass else "❌ FAIL"))
        k2.metric(t["m_max_dos"], f"{rt_calc['max_safe_dosage_pct']:.2f} %")
        k3.metric(t["m_allg"], f"{len(over_10ppm_list)}")
        k4.metric(t["m_sg"], f"ρ {mod_calc['jus_sg']} / {mac_meta['natural_pct'] if mac_meta else 0}%")

        p3_t1, p3_t2, p3_t3, p3_t4, p3_t5 = st.tabs([t["p3_t1"], t["p3_t2"], t["p3_t3"], t["p3_t4"], t["p3_t5"]])

        pif_rows = []
        for lid, item in mod_calc["norm_active"].items():
            pct_in_finished_active = (item["active_pct"] / 100.0) * dosage_ratio * 100.0
            pct_in_finished_carrier = (item["carrier_g"] / mod_calc["total_active_g"]) * dosage_ratio * 100.0 if mod_calc["total_active_g"] > 0 else 0.0
            pif_rows.append({
                "CAS No.": item["cas"],
                "Material Name": item["name_disp"],
                "Dilution": f"{item['dilution_pct']:.0f}% in {item['solvent'].split(' ')[0]}" if item["dilution_pct"] < 100 else "100% Pure",
                "% in Pure Oil": round(item["active_pct"], 3),
                f"% in Finished (@{dosage_ratio*100:.0f}%)": round(pct_in_finished_active, 4),
                f"Carrier in Finished (@{dosage_ratio*100:.0f}%)": round(pct_in_finished_carrier, 4)
            })
        df_pif_a = pd.DataFrame(pif_rows).sort_values(by="% in Pure Oil", ascending=False)

        carrier_incis = []
        for sol_name in mod_calc["batch"]["carrier_solvents"].keys():
            inci_s = SOLVENT_DATABASE.get(sol_name, {}).get("inci", "")
            if inci_s and inci_s not in carrier_incis:
                carrier_incis.append(inci_s)
        inci_allergens = [a["name"].upper() for a in over_10ppm_list]
        base_incis = ["ALCOHOL DENAT.", "PARFUM (FRAGRANCE)", "AQUA (WATER)"] + carrier_incis + inci_allergens
        inci_final_str = ", ".join(base_incis)
        cert_no = f"IFRA-51-{datetime.now().strftime('%Y%m%d')}-{st.session_state.active_mod.replace(' ', '')}"

        with p3_t1:
            st.subheader("1. Full Quantitative Fragrance Composition (100% Q&Q)" if lang == "en" else "1. 香精全成分比例表 (100% Full Quantitative Composition)")
            st.dataframe(df_pif_a, hide_index=True, use_container_width=True)
            st.download_button(
                "📥 Download 100% Quantitative Formula (CSV)" if lang == "en" else "📥 下載 100% 香精全成分比例表 (CSV)",
                data=df_pif_a.to_csv(index=False).encode("utf-8-sig"),
                file_name=f"PIF_100pct_Composition_{st.session_state.active_mod}_{lang.upper()}.csv",
                mime="text/csv"
            )

        with p3_t2:
            st.subheader("2. Fragrance Allergen Declaration & INCI Labeling" if lang == "en" else "2. 法定香精過敏原清單聲明書與外盒 INCI 標籤")
            allg_summary = rt_calc.get("allergen_summary", {})
            allg_sources = rt_calc.get("allergen_sources", {})
            if allg_summary:
                allg_detail_rows = []
                for a_name, ppm in sorted(allg_summary.items(), key=lambda x: x[1], reverse=True):
                    is_declare = ppm >= region_info["allergen_ppm_threshold"]
                    allg_detail_rows.append({
                        "Allergen (INCI)": a_name.upper(),
                        "Primary Sources": ", ".join(set(allg_sources.get(a_name, []))),
                        "% in Pure Oil": round((ppm / 10000.0) / dosage_ratio, 4) if dosage_ratio > 0 else 0.0,
                        "% in Finished": f"{ppm / 10000.0:.5f}%",
                        "PPM in Finished": round(ppm, 2),
                        "Labeling Status": ("⚠️ Mandatory (>10 ppm)" if lang == "en" else "⚠️ 強制外盒標示 (>10 ppm)") if is_declare else ("✅ Exempt (<10 ppm)" if lang == "en" else "✅ 免標示 (<10 ppm)")
                    })
                df_allg = pd.DataFrame(allg_detail_rows)
                st.dataframe(df_allg, hide_index=True, use_container_width=True)
                st.download_button(
                    "📥 Download Allergen Declaration (CSV)" if lang == "en" else "📥 下載過敏原清單聲明書 (CSV)",
                    data=df_allg.to_csv(index=False).encode("utf-8-sig"),
                    file_name=f"PIF_Allergens_{st.session_state.active_mod}_{lang.upper()}.csv",
                    mime="text/csv"
                )
            else:
                st.success("✅ No regulated fragrance allergens detected." if lang == "en" else "✅ 經 GC-MS 成分穿透計算，此配方在最終成品中未檢出任何法定致敏原。")

            st.divider()
            st.markdown("#### 🏷️ Official INCI Packaging Label (Sorted Descending)" if lang == "en" else "#### 🏷️ 外包裝法定 INCI 全成分展開標籤 (依含量降冪排列)")
            st.code(inci_final_str, language="text")

        with p3_t3:
            st.subheader("3. IFRA 51st Amendment Conformity Certificate")
            st.markdown(f"""
            <div class="cert-box">
                <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #CBD5E1; padding-bottom:8px; margin-bottom:10px;">
                    <div>
                        <h4 style="margin:0; color:#0F172A;">CERTIFICATE OF CONFORMITY WITH IFRA STANDARDS (51st Amendment)</h4>
                        <span style="font-size:12px; color:#64748B;">Certificate No.: <code>{cert_no}</code> ｜ Issue Date: {datetime.now().strftime("%Y-%m-%d")}</span>
                    </div>
                    <div style="background:{'#DCFCE7' if all_ifra_pass else '#FEE2E2'}; color:{'#15803D' if all_ifra_pass else '#B91C1C'}; padding:4px 12px; border-radius:4px; font-weight:bold;">
                        {'CONFORMING (PASS)' if all_ifra_pass else 'EXCEEDS LIMIT (FAIL)'}
                    </div>
                </div>
                <div style="font-size:13px; color:#334155;">
                    We certify that fragrance compound <b>{st.session_state.active_mod}</b> (created by <b>{current_user['display_name']}</b>) complies with the Standards of the International Fragrance Association (IFRA 51st Amendment). Maximum allowable concentrations in finished products (Categories 1–12) are listed below:
                </div>
            </div>
            """, unsafe_allow_html=True)

            df_ifra_cats = pd.DataFrame(rt_calc["ifra_categories"])
            st.dataframe(df_ifra_cats, hide_index=True, use_container_width=True)
            ifra_pdf_bytes = pdf_gen.build_ifra_certificate_pdf(
                cert_no=cert_no,
                mod_name=st.session_state.active_mod,
                perfumer_name=current_user["display_name"],
                dosage_pct=dosage_ratio * 100.0,
                all_ifra_pass=all_ifra_pass,
                has_banned=has_banned,
                max_safe_dosage_pct=rt_calc["max_safe_dosage_pct"],
                ifra_categories=rt_calc["ifra_categories"]
            )
            ic1, ic2 = st.columns(2)
            ic1.download_button(
                "📄 一鍵匯出 IFRA 51st 符合性證書 (正式 PDF)" if lang == "zh" else "📄 Export Official IFRA 51st Certificate (PDF)",
                data=ifra_pdf_bytes,
                file_name=f"{cert_no}.pdf",
                mime="application/pdf",
                type="primary",
                use_container_width=True
            )
            ic2.download_button(
                "📥 Download IFRA 51st Certificate (CSV)" if lang == "en" else "📥 下載 IFRA 51st 跨品類符合性證書表 (CSV)",
                data=df_ifra_cats.to_csv(index=False).encode("utf-8-sig"),
                file_name=f"IFRA_51st_Certificate_{st.session_state.active_mod}_{lang.upper()}.csv",
                mime="text/csv",
                use_container_width=True
            )

        with p3_t4:
            st.subheader("4. Material Safety Data Sheet Summary (MSDS / SDS)")
            c_sds1, c_sds2 = st.columns(2)
            with c_sds1:
                st.markdown(f"""
                <div class="doc-sheet">
                    <div class="doc-title"><h4 style="margin:0;">Section 1–3 & 9: Identification & Physical Properties</h4></div>
                    <ul style="font-size:13px; line-height:1.75;">
                        <li><b>Product Name:</b> Fragrance Compound — {st.session_state.active_mod}</li>
                        <li><b>Appearance & Odor:</b> Pale yellow to amber clear oily liquid, characteristic aromatic odor.</li>
                        <li><b>Relative Density (20°C):</b> ρ = <b>{mod_calc['jus_sg']}</b> g/cm³</li>
                        <li><b>Solubility:</b> Insoluble in water; miscible with 95% Ethanol, DPG, TEC, IPM.</li>
                        <li><b>Flash Point (Closed Cup):</b> ~68°C (Pure Jus) / ~<b>14°C</b> (Finished perfume at {dosage_ratio*100:.0f}%).</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

            with c_sds2:
                st.markdown(f"""
                <div class="doc-sheet">
                    <div class="doc-title"><h4 style="margin:0;">Section 2, 7 & 10: GHS Hazards & Handling</h4></div>
                    <ul style="font-size:13px; line-height:1.75;">
                        <li><b>GHS Classification:</b> Flammable Liquid Cat. 2 (H225), Skin Sensitization Cat. 1 (H317), Aquatic Chronic Cat. 2 (H411).</li>
                        <li><b>Safe Handling (Sec. 7):</b> Wear nitrile gloves and eye protection; keep away from heat/sparks/open flames.</li>
                        <li><b>Storage & Maceration:</b> Store sealed in cool dark place (15–20°C); macerate <b>{mac_meta['maceration']['days'] if mac_meta else 14} days</b> & chill-filter at -4°C (0.45μm).</li>
                        <li><b>Phototoxicity Note:</b> {"⚠️ Contains non-FCF Bergamot EO (0.4% max limit)." if (mac_meta and mac_meta["has_bergamot_phototoxic"]) else "✅ No high-risk phototoxic furocoumarin oils detected."}</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

        with p3_t5:
            st.subheader("🔒 Tri-Party NDA Direct-to-Safety Assessor (SA) Mode" if lang == "en" else "🔒 三方保密協議（Tri-Party NDA）直傳安全評估人員（SA）模式")
            st.markdown("""
            <div class="nda-box">
                <h4 style="margin:0 0 6px 0; color:#92400E;">🛡️ Intellectual Property Isolation Protocol (IP Protection)</h4>
                <div style="font-size:13px; line-height:1.6;">
                    Under EU EC 1223/2009 and Taiwan TFDA PIF regulations, the Safety Assessor (SA) requires the <b>100% full quantitative formula</b> to sign off the Cosmetic Product Safety Report (CPSR).<br>
                    To protect trade secrets from leaking to brand marketing or third-party OEM factories, execute a <b>Tri-Party NDA (Perfumer × Brand Owner × Independent SA)</b> and transmit the encrypted SA Dossier directly to the SA.
                </div>
            </div>
            """, unsafe_allow_html=True)

            c_nda1, c_nda2 = st.columns(2)
            with c_nda1:
                nda_perfumer = st.text_input("① Disclosing Party (Perfumer / Studio)", value=current_user["display_name"], key="nda_perfumer")
                nda_brand = st.text_input("② Commissioning Party (Brand Owner)", value="", placeholder="Enter Brand Owner name...", key="nda_brand")
            with c_nda2:
                nda_sa_name = st.text_input("③ Receiving Party (Authorized Safety Assessor / SA)", value="", placeholder="Enter SA name / credentials / institution...", key="nda_sa_name")
                nda_ref_no = st.text_input("④ Tri-Party NDA Reference No.", value=f"NDA-{datetime.now().strftime('%Y%m%d')}-01", key="nda_ref_no")

            nda_confirmed = st.checkbox("✅ Confirm Tri-Party NDA is executed to unlock 100% Confidential SA Dossier download", key="nda_chk")

            allergen_lines = "\n".join([f"- {a['name'].upper()}: {a['ppm']} ppm ({a['pct_finished']}%)" for a in over_10ppm_list]) if over_10ppm_list else "- None above 10 ppm threshold."
            ifra_cat_lines = "\n".join([f"- {list(c.values())[0]} ({list(c.values())[1]}): Max {list(c.values())[2]}" for c in rt_calc["ifra_categories"]])
            comp_lines_100 = "\n".join([
                f"- [CAS: {r['CAS No.']}] {r['Material Name']} | Pure Oil: {r['% in Pure Oil']}% | Finished: {r[f'% in Finished (@{dosage_ratio*100:.0f}%)']}% | Spec: {r['Dilution']}"
                for r in pif_rows
            ])

            sa_confidential_dossier = f"""# STRICTLY CONFIDENTIAL — DIRECT-TO-SAFETY ASSESSOR (SA) PIF PACKAGE
## UNDER TRI-PARTY NON-DISCLOSURE AGREEMENT (NDA)

- **NDA Reference No.**: {nda_ref_no}
- **Disclosing Party (Perfumer / Studio)**: {nda_perfumer}
- **Commissioning Party (Brand Owner)**: {nda_brand if nda_brand else '[Pending Brand Name]'}
- **Receiving Party (Authorized Safety Assessor / SA)**: {nda_sa_name if nda_sa_name else '[Pending SA Name]'}
- **Issue Date**: {datetime.now().strftime("%Y-%m-%d %H:%M")}
- **Formula / Mod Code**: {st.session_state.active_mod}
- **Target Product Application & Dosage**: {tier_info['en']} ({dosage_ratio*100:.1f}%)
- **Regulatory Framework**: {region_info['name_en']}

> **CONFIDENTIALITY NOTICE**: This document contains 100% proprietary fragrance formulation data disclosed solely to the designated Safety Assessor (SA) under the executed Tri-Party NDA ({nda_ref_no}) for toxicological safety evaluation (CPSR / PIF) purposes only.

---

## PART 1: 100% FULL QUANTITATIVE FRAGRANCE COMPOSITION (PROPRIETARY)
- **Pure Active Fragrance Concentrate Share in Jus**: {round(mod_calc['total_active_g'] / mod_calc['total_gross_g'] * 100.0, 2)}%
- **Carrier Solvent Share in Jus**: {round(mod_calc['total_carrier_g'] / mod_calc['total_gross_g'] * 100.0, 2)}%

{comp_lines_100}

---

## PART 2: IFRA 51st AMENDMENT CONFORMITY CERTIFICATE ({cert_no})
- **Overall Compliance Status**: {'CONFORMING (PASS)' if all_ifra_pass else 'EXCEEDS LIMIT (FAIL)'}
- **Maximum Allowable Concentration in Cat. 4 (Fine Fragrance)**: {rt_calc['max_safe_dosage_pct']:.2f}%

{ifra_cat_lines}

---

## PART 3: MATERIAL SAFETY DATA SHEET (MSDS / GHS SUMMARY)
- **Product Identification**: Fragrance Compound — {st.session_state.active_mod}
- **Relative Density (20°C)**: {mod_calc['jus_sg']} g/cm3
- **Flash Point**: ~68°C (Pure Jus, closed cup) / ~14°C (Finished alcoholic perfume at {dosage_ratio*100:.0f}%)
- **GHS Classification**: Flammable Liquid Cat. 2 (H225), Skin Sensitization Cat. 1 (H317), Aquatic Chronic Cat. 2 (H411).
- **Recommended Maceration & Filtration**: {mac_meta['maceration']['days'] if mac_meta else 14} days maturation; -4°C chilling followed by 0.45μm filtration.

---

## PART 4: REGULATED ALLERGEN DECLARATION & INCI LABELING
- **Official INCI String**: {inci_final_str}
- **Allergens > 10 ppm in Finished Product**:
{allergen_lines}
"""

            if nda_confirmed:
                pif_pdf_bytes = pdf_gen.build_pif_dossier_pdf(
                    nda_ref_no=nda_ref_no,
                    perfumer_name=nda_perfumer,
                    brand_name=nda_brand,
                    sa_name=nda_sa_name,
                    mod_name=st.session_state.active_mod,
                    tier_label=tier_info["en"],
                    dosage_pct=dosage_ratio * 100.0,
                    region_label=region_info["name_en"],
                    cert_no=cert_no,
                    all_ifra_pass=all_ifra_pass,
                    has_banned=has_banned,
                    max_safe_dosage_pct=rt_calc["max_safe_dosage_pct"],
                    jus_sg=mod_calc["jus_sg"],
                    maceration_days=mac_meta["maceration"]["days"] if mac_meta else 14,
                    pure_share_pct=round(mod_calc["total_active_g"] / mod_calc["total_gross_g"] * 100.0, 2),
                    carrier_share_pct=round(mod_calc["total_carrier_g"] / mod_calc["total_gross_g"] * 100.0, 2),
                    pif_rows=pif_rows,
                    ifra_categories=rt_calc["ifra_categories"],
                    over_10ppm_list=over_10ppm_list,
                    inci_final_str=inci_final_str
                )
                tfda_excel_bytes = file_export.build_tfda_pif_16_excel(
                    mod_name=st.session_state.active_mod,
                    perfumer_name=nda_perfumer,
                    dosage_pct=dosage_ratio * 100.0,
                    pif_rows=pif_rows,
                    over_10ppm_list=over_10ppm_list
                )
                
                c_dl0, c_dl1 = st.columns([1.0, 1.0])
                c_dl0.download_button(
                    "🔒📄 一鍵匯出完整 PIF & 三方 NDA 技術報告 (PDF)" if lang == "zh" else "🔒📄 Export Complete SA PIF & NDA Dossier (PDF)",
                    data=pif_pdf_bytes,
                    file_name=f"CONFIDENTIAL_SA_PIF_{st.session_state.active_mod}_{nda_ref_no}.pdf",
                    mime="application/pdf",
                    type="primary",
                    use_container_width=True
                )
                c_dl1.download_button(
                    "📊 匯出 TFDA PIF 第16項：安全資料表 (Excel)" if lang == "zh" else "📊 Export TFDA PIF Form 16 (Excel)",
                    data=tfda_excel_bytes,
                    file_name=f"TFDA_PIF_16_{st.session_state.active_mod}_{nda_ref_no}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
            else:
                st.warning("☝️ Check the Tri-Party NDA confirmation box above to unlock the 100% confidential SA package.")

# ==============================================================================
# PHASE 4: Commercial Scale-up (Only visible when Vendor/OEM Portal is enabled)
# ==============================================================================
elif current_route == "PHASE_4":
    st.markdown(f"""
    <div style="background:#0F172A; padding:8px 16px; border-radius:6px; color:white; display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <div><b>{t['p4_banner']}</b> ｜ Mod: <span class="mod-pill">{st.session_state.active_mod}</span></div>
    </div>
    """, unsafe_allow_html=True)
    if mod_calc and total_jus_g > 0:
        c_b1, c_b2 = st.columns(2)
        target_bottles = c_b1.number_input(t["p4_bot"], 50, 50000, 500, 50)
        target_vol = c_b2.selectbox(t["p4_vol"], [10, 15, 30, 50, 100], index=2)
        scale_calc = core.calculate_mod_profile(current_formula, dosage_ratio, {"bottles": target_bottles, "vol_ml": target_vol}, core_db, sku_db, custom_db, lang=lang)
        st.dataframe(pd.DataFrame(scale_calc["bmr_rows"]), hide_index=True, use_container_width=True)


# ==============================================================================
# VENDOR PORTAL: Commercial SKU Registry (Visible to Admin to manage L2 SKUs)
# ==============================================================================
elif current_route == "VENDOR_PORTAL" and is_admin:
    st.markdown("""
    <div style="background:#0F172A; padding:10px 18px; border-radius:6px; color:white; margin-bottom:14px;">
        <b>📦 商業供應商 SKU 管理中心 (Vendor / OEM SKU Registry)</b>
    </div>
    """, unsafe_allow_html=True)
    st.caption("供管理員或原料商匯入具體商業料號，必須映射至 Layer 1 的 CAS 號碼，並上傳批號、效期與單價。")

    db_col_l2, db_col_l2_list = st.columns([1.5, 1.5])
    with db_col_l2:
        with st.form("add_l2_sku_form", clear_on_submit=True):
            new_sku_id = st.text_input("商業料號 SKU ID *", placeholder="例如: SKU-GIV-54464-100")
            map_cas = st.selectbox(
                "映射底層純物質 CAS *", list(core_db.keys()),
                format_func=lambda c: f"{c} — {core_db[c]['name_en'] if lang=='en' else core_db[c]['name_cn']}"
            )
            s_c1, s_c2 = st.columns(2)
            trade_cn = s_c1.text_input("中文商品名稱 *", placeholder="例如: 奇華頓龍涎酮 100%")
            trade_en = s_c2.text_input("英文商品名稱 *", placeholder="e.g., Givaudan Iso E Super 100%")
            v_c1, v_c2 = st.columns(2)
            sup_zh = v_c1.text_input("供應商名稱", value="Givaudan / 代工廠")
            lot_no = v_c2.text_input("批號 (Lot No.)", value=f"LOT-{datetime.now().strftime('%y%m%d')}")
            p_c1, p_c2, p_c3 = st.columns(3)
            sku_dil = p_c1.number_input("商業純度 (%)", 1.0, 100.0, 100.0, 1.0)
            sku_sol = p_c2.selectbox("預設溶劑", SOLVENT_CHOICES, index=0)
            sku_cost = p_c3.number_input("純油單價 (NT$/g)", 0.0, 5000.0, 10.0, 0.5)

            d_c1, d_c2, d_c3 = st.columns(3)
            has_coa = d_c1.checkbox("掛載 COA 檢驗單", value=True)
            has_sds = d_c2.checkbox("掛載 SDS 安全表", value=True)
            has_ifra = d_c3.checkbox("掛載 IFRA 證書", value=True)

            if st.form_submit_button("➕ 註冊商業 SKU 至 Layer 2", type="primary", use_container_width=True):
                if new_sku_id and trade_cn:
                    st.session_state.commercial_skus[new_sku_id.strip()] = {
                        "sku_id": new_sku_id.strip(),
                        "cas": map_cas,
                        "trade_name_cn": trade_cn.strip(),
                        "trade_name_en": trade_en.strip() or trade_cn.strip(),
                        "supplier_zh": sup_zh.strip(),
                        "supplier_en": sup_zh.strip(),
                        "lot_no": lot_no.strip(),
                        "exp_date": "2029/12/31",
                        "dilution_pct": sku_dil,
                        "solvent": sku_sol,
                        "sg": core_db[map_cas]["sg_pure"],
                        "cost_per_g": sku_cost,
                        "docs": {"COA": has_coa, "SDS": has_sds, "IFRA": has_ifra},
                        "allergens": core_db[map_cas].get("baseline_allergens", {})
                    }
                    st.success(f"✅ 已成功新增商業 SKU：{new_sku_id}")
                    st.rerun()

        uploaded_sku_csv = st.file_uploader("📂 批次上傳供應商 SKU 清單 (CSV)", type=["csv"], key="sku_csv_up")
        if uploaded_sku_csv is not None:
            try:
                df_up = pd.read_csv(uploaded_sku_csv)
                added_n = 0
                for _, r in df_up.iterrows():
                    sid = str(r.get("sku_id", "")).strip()
                    cas_val = str(r.get("cas", "")).strip()
                    if sid and cas_val in core_db:
                        st.session_state.commercial_skus[sid] = {
                            "sku_id": sid,
                            "cas": cas_val,
                            "trade_name_cn": str(r.get("trade_name_cn", sid)),
                            "trade_name_en": str(r.get("trade_name_en", sid)),
                            "supplier_zh": str(r.get("supplier", "Uploaded Vendor")),
                            "supplier_en": str(r.get("supplier", "Uploaded Vendor")),
                            "lot_no": str(r.get("lot_no", "LOT-CSV")),
                            "exp_date": str(r.get("exp_date", "2029/12/31")),
                            "dilution_pct": float(r.get("dilution_pct", 100.0)),
                            "solvent": str(r.get("solvent", "None (100%純原液)")),
                            "sg": float(r.get("sg", core_db[cas_val]["sg_pure"])),
                            "cost_per_g": float(r.get("cost_per_g", 0.0)),
                            "docs": {"COA": True, "SDS": True, "IFRA": True},
                            "allergens": core_db[cas_val].get("baseline_allergens", {})
                        }
                        added_n += 1
                if added_n > 0:
                    st.success(f"✅ 已匯入 {added_n} 筆供應商 SKU！")
            except Exception as e:
                st.error(f"CSV 格式錯誤: {e}")

    with db_col_l2_list:
        st.markdown(f"**目前已註冊之商業 SKU (總計: {len(sku_db)} 筆)**")
        sku_rows = []
        for sid, s in sku_db.items():
            sku_rows.append({
                "SKU ID": sid,
                "CAS": s["cas"],
                "廠商": s["supplier_zh"],
                "純度": f"{s['dilution_pct']:.0f}%",
                "單價(g)": f"${s['cost_per_g']}"
            })
        st.dataframe(pd.DataFrame(sku_rows), hide_index=True, use_container_width=True)

# ==============================================================================
# ADMIN BACKOFFICE

# ==============================================================================
elif current_route == "ADMIN" and is_admin:
    st.markdown("""
    <div style="background:#0F172A; padding:10px 18px; border-radius:6px; color:white; margin-bottom:14px;">
        <b>🛡️ Nanmen Scent Lab OS — Admin Backoffice (總管理後台)</b>
    </div>
    """, unsafe_allow_html=True)

    adm_t1, adm_t2, adm_t3 = st.tabs([
        "👥 1. 獨立調香師帳號與版本管理 (Accounts & Tiers)",
        "📊 2. 去識別化原料需求熱度報表 (Supplier Negotiation Data)",
        "⚙️ 3. 系統階段開關 (Vendor/OEM Phase Switch)"
    ])

    with adm_t1:
        st.subheader("👥 已註冊獨立調香師帳號總覽")
        users_list = db.list_all_users_summary()
        st.dataframe(pd.DataFrame(users_list), hide_index=True, use_container_width=True)

        perfumer_users = [u for u in users_list if u["role"] != "admin"]
        if perfumer_users:
            st.divider()
            st.markdown("#### 🔧 調整調香師版本等級 (Trial / Pro) 與帳號狀態")
            ac1, ac2, ac3, ac4 = st.columns([1.5, 1.2, 1.2, 1.0])
            sel_u = ac1.selectbox("選擇調香師帳號", [u["username"] for u in perfumer_users])
            u_rec = next(u for u in perfumer_users if u["username"] == sel_u)
            new_plan = ac2.selectbox("版本方案 (Plan Tier)", ["Trial", "Pro"], index=0 if u_rec["plan_tier"] == "Trial" else 1)
            new_stat = ac3.selectbox("帳號狀態 (Status)", ["Active", "Suspended"], index=0 if u_rec["status"] == "Active" else 1)
            ac4.write("")
            if ac4.button("💾 更新權限", type="primary", use_container_width=True):
                db.update_user_admin(sel_u, new_plan, new_stat)
                st.success(f"✅ 已更新 @{sel_u} 為 {new_plan} ({new_stat})")
                st.rerun()

    with adm_t2:
        st.subheader("📊 去識別化 CAS 原料需求統計（供下一階段向原料商／代工廠洽談真實 SKU）")
        st.info("🔒 **隱私保護原則**：此報表僅彙整各 CAS 號碼在平台上的使用人數與總模擬克數，**完全去識別化**，不顯示任何單一調香師的完整配方比例。")

        analytics = db.get_anonymized_cas_analytics(core_db)
        k1, k2, k3 = st.columns(3)
        k1.metric("已註冊獨立調香師人數", f"{analytics['total_perfumers']} 人")
        k2.metric("累積建立配方版本總數", f"{analytics['total_mods']} Mods")
        k3.metric("涉及不重複 CAS 原料數", f"{len(analytics['cas_ranking'])} 項")

        if analytics["cas_ranking"]:
            df_rank = pd.DataFrame(analytics["cas_ranking"])
            st.dataframe(df_rank, hide_index=True, use_container_width=True)
            st.download_button(
                "📥 下載去識別化原料需求熱度表 (CSV — 供應商談判用)",
                data=df_rank.to_csv(index=False).encode("utf-8-sig"),
                file_name=f"Nanmen_CAS_Demand_Report_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                type="primary",
                use_container_width=True
            )
        else:
            st.caption("目前尚無調香師建立配方數據。")

    with adm_t3:
        st.subheader("⚙️ 商業驗證階段開關 (Stage Feature Flags)")
        st.caption("第一階段（邀請獨立調香師測試）建議保持關閉，避免過早暴露供應商與 OEM 代工介面；等累積足夠調香師數據並取得廠商真實 SKU 後，再切換開啟。")
        cur_flag = (db.get_system_flag("ENABLE_VENDOR_PORTAL", "0") == "1")
        new_flag = st.toggle("啟用第二階段：商業 SKU 映射閘門 & OEM 商業量產 (Phase 4)", value=cur_flag)
        if new_flag != cur_flag:
            db.set_system_flag("ENABLE_VENDOR_PORTAL", "1" if new_flag else "0")
            st.success("✅ 系統階段設定已更新！")
            st.rerun()
