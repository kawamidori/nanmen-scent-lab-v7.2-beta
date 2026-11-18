# db.py
import sqlite3
import json
import hashlib
import os
import copy
from datetime import datetime

DB_PATH = "nanmen_scent_lab.db"

def _get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def _hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16).hex()
    pwd_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 100_000).hex()
    return f"{salt}${pwd_hash}"

def _verify_password(password, stored_hash):
    if not stored_hash or "$" not in stored_hash:
        return False
    salt, _ = stored_hash.split("$", 1)
    return _hash_password(password, salt) == stored_hash

def init_db(admin_default_password="nanmen2026"):
    conn = _get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            display_name TEXT NOT NULL,
            email TEXT,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'perfumer',
            plan_tier TEXT NOT NULL DEFAULT 'Pro',
            status TEXT NOT NULL DEFAULT 'Active',
            nda_accepted_at TEXT,
            created_at TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS workspaces (
            username TEXT PRIMARY KEY,
            workspace_json TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS system_flags (
            flag_key TEXT PRIMARY KEY,
            flag_value TEXT NOT NULL
        )
    """)

    # Seed default system flags (Phase 1 Beta: Vendor/OEM portal hidden by default)
    cur.execute("INSERT OR IGNORE INTO system_flags (flag_key, flag_value) VALUES ('ENABLE_VENDOR_PORTAL', '0')")

    # Seed default admin account if not exists
    cur.execute("SELECT username FROM users WHERE username = 'admin'")
    if cur.fetchone() is None:
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(
            """INSERT INTO users (username, display_name, email, password_hash, role, plan_tier, status, nda_accepted_at, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            ("admin", "Nanmen Lab Admin", "admin@nanmenscent.com", _hash_password(admin_default_password), "admin", "Enterprise", "Active", now_str, now_str)
        )

    conn.commit()
    conn.close()

def get_default_workspace():
    return {
        "mods": {
            "Mod 1": {
                "L1_54464-57-2": {"layer": "L1_CORE", "cas": "54464-57-2", "sku_id": None, "gross_g": 1.500, "dilution_pct": 50.0, "solvent": "DPG (二丙二醇)"},
                "L1_24851-98-7": {"layer": "L1_CORE", "cas": "24851-98-7", "sku_id": None, "gross_g": 1.200, "dilution_pct": 50.0, "solvent": "DPG (二丙二醇)"},
                "L1_6790-58-5": {"layer": "L1_CORE", "cas": "6790-58-5", "sku_id": None, "gross_g": 0.300, "dilution_pct": 10.0, "solvent": "DPG (二丙二醇)"},
                "L1_8007-75-8": {"layer": "L1_CORE", "cas": "8007-75-8", "sku_id": None, "gross_g": 0.200, "dilution_pct": 50.0, "solvent": "DPG (二丙二醇)"},
                "L1_91770-58-0": {"layer": "L1_CORE", "cas": "91770-58-0", "sku_id": None, "gross_g": 0.400, "dilution_pct": 50.0, "solvent": "DPG (二丙二醇)"}
            }
        },
        "active_mod": "Mod 1",
        "mod_notes": {
            "Mod 1": "初始示範版：台灣肖楠與佛手柑清冷木質調（可自由修改或新增 Mod）。"
        },
        "custom_materials": {},
        "dosed_checklist": {},
        "region_id": "EU",
        "tier_id": "EdP_15"
    }

def register_perfumer(username, display_name, email, password, plan_tier="Pro"):
    clean_user = username.strip().lower()
    if not clean_user or len(clean_user) < 3:
        return False, "帳號長度至少需 3 個字元 / Username must be at least 3 characters."
    if not password or len(password) < 4:
        return False, "密碼長度至少需 4 個字元 / Password must be at least 4 characters."
    if clean_user == "admin":
        return False, "此帳號名稱為系統保留字 / Reserved username."

    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("SELECT username FROM users WHERE username = ?", (clean_user,))
    if cur.fetchone() is not None:
        conn.close()
        return False, "此帳號已被註冊，請更換帳號名稱 / Username already exists."

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(
        """INSERT INTO users (username, display_name, email, password_hash, role, plan_tier, status, nda_accepted_at, created_at)
           VALUES (?, ?, ?, ?, 'perfumer', ?, 'Active', ?, ?)""",
        (clean_user, display_name.strip() or clean_user, email.strip(), _hash_password(password), plan_tier, now_str, now_str)
    )
    default_ws = get_default_workspace()
    cur.execute(
        "INSERT INTO workspaces (username, workspace_json, updated_at) VALUES (?, ?, ?)",
        (clean_user, json.dumps(default_ws, ensure_ascii=False), now_str)
    )
    conn.commit()
    conn.close()
    return True, "註冊成功 / Account created successfully."

def authenticate_user(username, password, admin_secret_pwd="nanmen2026"):
    clean_user = username.strip().lower()
    if not clean_user or not password:
        return None, "請輸入帳號與密碼 / Please enter username and password."

    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (clean_user,))
    row = cur.fetchone()
    conn.close()

    if row is None:
        return None, "找不到此帳號 / Account not found."

    user_dict = dict(row)
    if user_dict.get("status") != "Active":
        return None, "此帳號已暫停使用，請聯繫管理員 / Account suspended."

    # Allow admin to log in with either stored hash or st.secrets APP_PASSWORD
    if clean_user == "admin" and password == admin_secret_pwd:
        return user_dict, None

    if _verify_password(password, user_dict["password_hash"]):
        return user_dict, None

    return None, "密碼錯誤 / Incorrect password."

def load_user_workspace(username):
    clean_user = username.strip().lower()
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("SELECT workspace_json FROM workspaces WHERE username = ?", (clean_user,))
    row = cur.fetchone()
    if row is None:
        ws = get_default_workspace()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(
            "INSERT INTO workspaces (username, workspace_json, updated_at) VALUES (?, ?, ?)",
            (clean_user, json.dumps(ws, ensure_ascii=False), now_str)
        )
        conn.commit()
        conn.close()
        return ws
    conn.close()
    try:
        data = json.loads(row["workspace_json"])
        base = get_default_workspace()
        for k, v in base.items():
            if k not in data:
                data[k] = v
        return data
    except Exception:
        return get_default_workspace()

def save_user_workspace(username, workspace_data):
    clean_user = username.strip().lower()
    conn = _get_conn()
    cur = conn.cursor()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = json.dumps(workspace_data, ensure_ascii=False)
    cur.execute(
        """INSERT INTO workspaces (username, workspace_json, updated_at)
           VALUES (?, ?, ?)
           ON CONFLICT(username) DO UPDATE SET workspace_json=excluded.workspace_json, updated_at=excluded.updated_at""",
        (clean_user, payload, now_str)
    )
    conn.commit()
    conn.close()

def get_system_flag(flag_key, default="0"):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("SELECT flag_value FROM system_flags WHERE flag_key = ?", (flag_key,))
    row = cur.fetchone()
    conn.close()
    return row["flag_value"] if row else default

def set_system_flag(flag_key, flag_value):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO system_flags (flag_key, flag_value) VALUES (?, ?)
           ON CONFLICT(flag_key) DO UPDATE SET flag_value=excluded.flag_value""",
        (flag_key, str(flag_value))
    )
    conn.commit()
    conn.close()

def list_all_users_summary():
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT u.username, u.display_name, u.email, u.role, u.plan_tier, u.status, u.nda_accepted_at, u.created_at,
               w.workspace_json, w.updated_at
        FROM users u
        LEFT JOIN workspaces w ON u.username = w.username
        ORDER BY u.created_at DESC
    """)
    rows = cur.fetchall()
    conn.close()

    results = []
    for r in rows:
        mods_cnt = 0
        custom_cnt = 0
        if r["workspace_json"]:
            try:
                ws = json.loads(r["workspace_json"])
                mods_cnt = len(ws.get("mods", {}))
                custom_cnt = len(ws.get("custom_materials", {}))
            except Exception:
                pass
        results.append({
            "username": r["username"],
            "display_name": r["display_name"],
            "email": r["email"] or "-",
            "role": r["role"],
            "plan_tier": r["plan_tier"],
            "status": r["status"],
            "nda_accepted_at": r["nda_accepted_at"] or "-",
            "created_at": r["created_at"],
            "updated_at": r["updated_at"] or "-",
            "mods_count": mods_cnt,
            "custom_count": custom_cnt
        })
    return results

def update_user_admin(username, plan_tier, status):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET plan_tier = ?, status = ? WHERE username = ? AND role != 'admin'",
        (plan_tier, status, username)
    )
    conn.commit()
    conn.close()

def get_anonymized_cas_analytics(core_db):
    """
    Aggregates strictly anonymized CAS usage statistics across all non-admin perfumers
    to help negotiate real commercial SKUs with suppliers without exposing any individual formula.
    """
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT u.username, w.workspace_json
        FROM users u
        JOIN workspaces w ON u.username = w.username
        WHERE u.role = 'perfumer'
    """)
    rows = cur.fetchall()
    conn.close()

    total_perfumers = len(rows)
    total_mods = 0
    cas_stats = {}  # cas -> {"perfumer_set": set(), "mod_appearances": 0, "total_active_g": 0.0}

    for r in rows:
        uname = r["username"]
        try:
            ws = json.loads(r["workspace_json"])
        except Exception:
            continue
        mods = ws.get("mods", {})
        total_mods += len(mods)
        for mod_name, formula in mods.items():
            for lid, entry in formula.items():
                gross = float(entry.get("gross_g", 0.0))
                if gross <= 0:
                    continue
                cas = entry.get("cas", "")
                if not cas:
                    continue
                dil = float(entry.get("dilution_pct", 100.0)) / 100.0
                act_g = gross * dil
                st_obj = cas_stats.setdefault(cas, {"perfumers": set(), "mod_count": 0, "total_active_g": 0.0})
                st_obj["perfumers"].add(uname)
                st_obj["mod_count"] += 1
                st_obj["total_active_g"] += act_g

    ranking = []
    for cas, info in cas_stats.items():
        cm = core_db.get(cas, {})
        ranking.append({
            "CAS No.": cas,
            "Material (EN)": cm.get("name_en", cas),
            "Material (ZH)": cm.get("name_cn", cas),
            "Note": cm.get("note", "-"),
            "Family": cm.get("family", "-"),
            "Active Perfumers Using": len(info["perfumers"]),
            "Formula Appearances": info["mod_count"],
            "Total Simulated Pure Oil (g)": round(info["total_active_g"], 3)
        })
    ranking.sort(key=lambda x: (x["Active Perfumers Using"], x["Total Simulated Pure Oil (g)"]), reverse=True)
    return {
        "total_perfumers": total_perfumers,
        "total_mods": total_mods,
        "cas_ranking": ranking
    }
