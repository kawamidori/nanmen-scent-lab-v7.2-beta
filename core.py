# core.py
import math
import numpy as np
import pandas as pd
from config import SOLVENT_DATABASE, DROP_VOLUME_ML

def calc_effective_sg(ing_sg, solvent_name, dilution_pct):
    sol_sg = SOLVENT_DATABASE.get(solvent_name, {}).get("sg", 1.000)
    dil = dilution_pct / 100.0
    return round((dil * ing_sg) + ((1.0 - dil) * sol_sg), 3)

def grams_to_drops(gross_g, eff_sg):
    if eff_sg <= 0:
        eff_sg = 1.0
    return max(1, int(round((gross_g / eff_sg) / DROP_VOLUME_ML)))

def drops_to_grams(drops, eff_sg):
    if eff_sg <= 0:
        eff_sg = 1.0
    return round(drops * DROP_VOLUME_ML * eff_sg, 3)

def resolve_formula_item(line_id, entry, core_db, sku_db, custom_db, lang="zh"):
    """
    Resolves a formula entry across the 3-Layer Metadata Architecture:
      - L1_CORE: Abstract CAS from CHEMICAL_CORE_DB (Design/Creation phase)
      - L2_SKU: Mapped Commercial Supplier SKU from COMMERCIAL_SKU_DB (Compounding/PIF/Scale-up)
      - L3_CUSTOM: Perfumer's Private Custom Material from CUSTOM_PRIVATE_LIBRARY
    """
    layer = entry.get("layer", "L1_CORE")
    cas = entry.get("cas", "")
    sku_id = entry.get("sku_id")
    custom_id = entry.get("custom_id")
    gross_g = float(entry.get("gross_g", 0.0))

    # Resolve Layer 1 core chemical metadata
    core_meta = core_db.get(cas, {
        "cas": cas or "-", "name_cn": cas, "name_en": cas,
        "note": "Mid", "family": "Woody", "type": "Custom Chemical",
        "mol_w": 200.0, "vapor_pressure_mmhg": 0.05, "sg_pure": 0.950,
        "ifra_cat4_max": 100.0, "baseline_allergens": {}
    })

    if layer == "L2_SKU" and sku_id and sku_id in sku_db:
        sku = sku_db[sku_id]
        dil_pct = float(entry.get("dilution_pct", sku.get("dilution_pct", 100.0)))
        solvent = entry.get("solvent", sku.get("solvent", "None (100%純原液)"))
        if solvent not in SOLVENT_DATABASE:
            solvent = "DPG (二丙二醇)"
        eff_sg = calc_effective_sg(core_meta.get("sg_pure", sku.get("sg", 1.0)), solvent, dil_pct)
        disp_name = sku["trade_name_en"] if lang == "en" else sku["trade_name_cn"]
        supplier = sku.get("supplier_en", sku.get("supplier_zh", "-")) if lang == "en" else sku.get("supplier_zh", "-")
        return {
            "line_id": line_id,
            "layer": "L2_SKU",
            "is_mapped": True,
            "cas": sku["cas"],
            "sku_id": sku_id,
            "lot_no": sku.get("lot_no", "-"),
            "exp_date": sku.get("exp_date", "-"),
            "docs": sku.get("docs", {"COA": False, "SDS": False, "IFRA": False}),
            "name_disp": disp_name,
            "core_name_disp": core_meta["name_en"] if lang == "en" else core_meta["name_cn"],
            "supplier": supplier,
            "note": core_meta.get("note", "Mid"),
            "family": core_meta.get("family", "Woody"),
            "type": core_meta.get("type", "Natural Essential Oil"),
            "mol_w": core_meta.get("mol_w", 200.0),
            "vapor_pressure_mmhg": core_meta.get("vapor_pressure_mmhg", 0.05),
            "ifra_cat4_max": core_meta.get("ifra_cat4_max", 100.0),
            "eu_banned": bool(core_meta.get("eu_banned", False)),
            "allergens": sku.get("allergens", core_meta.get("baseline_allergens", {})),
            "gross_g": gross_g,
            "dilution_pct": dil_pct,
            "solvent": solvent,
            "eff_sg": eff_sg,
            "cost_per_g": float(sku.get("cost_per_g", 0.0))
        }

    elif layer == "L3_CUSTOM" and custom_id and custom_id in custom_db:
        cust = custom_db[custom_id]
        dil_pct = float(entry.get("dilution_pct", cust.get("dilution_pct", 100.0)))
        solvent = entry.get("solvent", cust.get("solvent", "DPG (二丙二醇)"))
        if solvent not in SOLVENT_DATABASE:
            solvent = "DPG (二丙二醇)"
        eff_sg = calc_effective_sg(cust.get("sg_pure", 0.950), solvent, dil_pct)
        disp_name = cust["name_en"] if lang == "en" else cust["name_cn"]
        return {
            "line_id": line_id,
            "layer": "L3_CUSTOM",
            "is_mapped": True,
            "cas": cust.get("cas", cas or "CUSTOM"),
            "sku_id": custom_id,
            "lot_no": cust.get("lot_no", "PRIVATE-LOT"),
            "exp_date": cust.get("exp_date", "-"),
            "docs": {"COA": True, "SDS": True, "IFRA": True},
            "name_disp": f"[Custom] {disp_name}",
            "core_name_disp": core_meta["name_en"] if lang == "en" else core_meta["name_cn"],
            "supplier": "Private Library" if lang == "en" else "調香師私有庫",
            "note": cust.get("note", core_meta.get("note", "Mid")),
            "family": cust.get("family", core_meta.get("family", "Woody")),
            "type": "Custom Private Material",
            "mol_w": core_meta.get("mol_w", 200.0),
            "vapor_pressure_mmhg": core_meta.get("vapor_pressure_mmhg", 0.05),
            "ifra_cat4_max": float(cust.get("ifra_cat4_max", core_meta.get("ifra_cat4_max", 100.0))),
            "eu_banned": bool(core_meta.get("eu_banned", False)),
            "allergens": cust.get("allergens", {}),
            "gross_g": gross_g,
            "dilution_pct": dil_pct,
            "solvent": solvent,
            "eff_sg": eff_sg,
            "cost_per_g": float(cust.get("cost_per_g", 0.0))
        }

    else:
        # L1_CORE (Abstract CAS during Creation Phase)
        dil_pct = float(entry.get("dilution_pct", 100.0))
        solvent = entry.get("solvent", "None (100%純原液)")
        if solvent not in SOLVENT_DATABASE:
            solvent = "None (100%純原液)"
        eff_sg = calc_effective_sg(core_meta.get("sg_pure", 0.950), solvent, dil_pct)
        disp_name = core_meta["name_en"] if lang == "en" else core_meta["name_cn"]
        return {
            "line_id": line_id,
            "layer": "L1_CORE",
            "is_mapped": False,
            "cas": core_meta["cas"],
            "sku_id": None,
            "lot_no": "UNMAPPED",
            "exp_date": "-",
            "docs": {"COA": False, "SDS": False, "IFRA": False},
            "name_disp": disp_name,
            "core_name_disp": disp_name,
            "supplier": "Unmapped Core CAS" if lang == "en" else "待映射商業料號",
            "note": core_meta.get("note", "Mid"),
            "family": core_meta.get("family", "Woody"),
            "type": core_meta.get("type", "Aroma Chemical"),
            "mol_w": core_meta.get("mol_w", 200.0),
            "vapor_pressure_mmhg": core_meta.get("vapor_pressure_mmhg", 0.05),
            "ifra_cat4_max": core_meta.get("ifra_cat4_max", 100.0),
            "eu_banned": bool(core_meta.get("eu_banned", False)),
            "allergens": core_meta.get("baseline_allergens", {}),
            "gross_g": gross_g,
            "dilution_pct": dil_pct,
            "solvent": solvent,
            "eff_sg": eff_sg,
            "cost_per_g": 0.0
        }

def synthesize_canvas_formula(slider_weights, hero_cas, target_gross_g, core_db):
    """Generates an abstract Layer 1 CAS skeleton formula for the Creation Phase."""
    total_w = sum(slider_weights.values())
    norm_w = {k: 0.2 for k in slider_weights} if total_w <= 0 else {k: v / total_w for k, v in slider_weights.items()}
    family_pool = {}
    for cas, v in core_db.items():
        if v.get("eu_banned", False) or v.get("ifra_cat4_max", 100.0) <= 0.0:
            continue
        family_pool.setdefault(v.get("family", "Woody"), []).append((cas, v))

    formula = {}
    remaining_g = target_gross_g
    if hero_cas and hero_cas in core_db:
        hero = core_db[hero_cas]
        hero_g = round(target_gross_g * 0.25, 3)
        formula[f"L1_{hero_cas}"] = {
            "layer": "L1_CORE",
            "cas": hero_cas,
            "sku_id": None,
            "gross_g": hero_g,
            "dilution_pct": 100.0 if hero["ifra_cat4_max"] > 5.0 else 10.0,
            "solvent": "None (100%純原液)" if hero["ifra_cat4_max"] > 5.0 else "DPG (二丙二醇)"
        }
        remaining_g -= hero_g
        h_fam = hero.get("family", "Woody")
        norm_w[h_fam] = max(0.0, norm_w.get(h_fam, 0.2) - 0.25)
        sub_total = sum(norm_w.values())
        if sub_total > 0:
            norm_w = {k: v / sub_total for k, v in norm_w.items()}

    for fam, w in norm_w.items():
        fam_budget = remaining_g * w
        if fam_budget < 0.15:
            continue
        pool = [item for item in family_pool.get(fam, []) if item[0] != hero_cas]
        if not pool:
            continue
        if fam_budget >= 1.0 and len(pool) >= 2:
            for idx, share in [(0, 0.6), (1, 0.4)]:
                c_id, c_meta = pool[idx]
                formula[f"L1_{c_id}"] = {
                    "layer": "L1_CORE",
                    "cas": c_id,
                    "sku_id": None,
                    "gross_g": round(fam_budget * share, 3),
                    "dilution_pct": 100.0 if c_meta["ifra_cat4_max"] > 5.0 else 10.0,
                    "solvent": "None (100%純原液)" if c_meta["ifra_cat4_max"] > 5.0 else "DPG (二丙二醇)"
                }
        else:
            c_id, c_meta = pool[0]
            formula[f"L1_{c_id}"] = {
                "layer": "L1_CORE",
                "cas": c_id,
                "sku_id": None,
                "gross_g": round(fam_budget, 3),
                "dilution_pct": 100.0 if c_meta["ifra_cat4_max"] > 5.0 else 10.0,
                "solvent": "None (100%純原液)" if c_meta["ifra_cat4_max"] > 5.0 else "DPG (二丙二醇)"
            }
    return formula

def build_compounding_sheet(formula_inputs, dosage_ratio, core_db, sku_db, custom_db, sort_by_compounding=True, lang="zh"):
    items = []
    for line_id, entry in formula_inputs.items():
        if entry.get("gross_g", 0) <= 0:
            continue
        res = resolve_formula_item(line_id, entry, core_db, sku_db, custom_db, lang=lang)
        dil = res["dilution_pct"] / 100.0
        gross = res["gross_g"]
        priority = 1 if "Base" in res["note"] else 2 if "Mid" in res["note"] else 3
        items.append({
            **res,
            "priority": priority,
            "drops": grams_to_drops(gross, res["eff_sg"]),
            "active_g": gross * dil,
            "carrier_g": gross * (1.0 - dil),
        })
    if sort_by_compounding:
        items.sort(key=lambda x: (x["priority"], x["name_disp"]))
    running_total, running_drops = 0.0, 0
    total_gross = sum(x["gross_g"] for x in items)
    for idx, row in enumerate(items, 1):
        running_total += row["gross_g"]
        running_drops += row["drops"]
        row["seq"] = idx
        row["cumulative_g"] = round(running_total, 3)
        row["cumulative_drops"] = running_drops
        row["gross_g"] = round(row["gross_g"], 3)
        row["active_g"] = round(row["active_g"], 3)
        row["carrier_g"] = round(row["carrier_g"], 3)
        row["pct"] = round((row["gross_g"] / total_gross * 100.0), 2) if total_gross > 0 else 0.0
        row["ppt"] = round((row["gross_g"] / total_gross * 1000.0), 1) if total_gross > 0 else 0.0
        row["cost"] = round(row["active_g"] * row["cost_per_g"], 2)
    return items

def analyze_formula_realtime(formula_inputs, dosage_ratio, core_db, sku_db, custom_db, lang="zh"):
    total_active_g = 0.0
    total_carrier_g = 0.0
    resolved_items = []
    for line_id, entry in formula_inputs.items():
        if entry.get("gross_g", 0.0) <= 0:
            continue
        res = resolve_formula_item(line_id, entry, core_db, sku_db, custom_db, lang=lang)
        dil = res["dilution_pct"] / 100.0
        act_g = res["gross_g"] * dil
        car_g = res["gross_g"] * (1.0 - dil)
        res["active_g"] = act_g
        res["carrier_g"] = car_g
        total_active_g += act_g
        total_carrier_g += car_g
        resolved_items.append(res)

    if total_active_g <= 0:
        return {
            "total_active_g": 0.0,
            "total_carrier_g": 0.0,
            "total_gross_g": 0.0,
            "unmapped_count": 0,
            "ifra_status": {},
            "ifra_categories": [],
            "allergen_summary": {},
            "allergen_sources": {},
            "max_safe_dosage_pct": 100.0,
            "tenacity_score": 0.0
        }

    total_gross = sum(r["gross_g"] for r in resolved_items)
    unmapped_count = sum(1 for r in resolved_items if not r["is_mapped"])

    # Aggregate pure active mass by CAS across Layer 1, Layer 2, and Layer 3
    cas_mass_aggregation = {}
    for r in resolved_items:
        cas_no = r["cas"]
        if cas_no and cas_no != "-":
            cas_mass_aggregation[cas_no] = cas_mass_aggregation.get(cas_no, 0.0) + r["active_g"]

    ifra_status = {}
    max_safe_dosage_pct = 100.0
    weighted_log_vp = 0.0

    for r in resolved_items:
        cas_no = r["cas"]
        limit = r["ifra_cat4_max"]
        aggregated_act_g = cas_mass_aggregation.get(cas_no, r["active_g"]) if cas_no != "-" else r["active_g"]
        active_share_in_pure_oil = aggregated_act_g / total_active_g
        finished_pct = active_share_in_pure_oil * dosage_ratio * 100.0
        risk_ratio = finished_pct / limit if limit > 0 else 999.0

        if active_share_in_pure_oil > 0 and limit < 100.0:
            allowed_dosage = limit / active_share_in_pure_oil
            if allowed_dosage < max_safe_dosage_pct:
                max_safe_dosage_pct = allowed_dosage

        # Vapor pressure longevity contribution
        vp = max(1e-6, float(r.get("vapor_pressure_mmhg", 0.05)))
        item_share = r["active_g"] / total_active_g
        weighted_log_vp += item_share * math.log10(vp)

        is_banned = bool(r.get("eu_banned", False)) or (limit <= 0.0)
        ifra_status[r["line_id"]] = {
            "cas": cas_no,
            "name_disp": r["name_disp"],
            "layer": r["layer"],
            "active_share_pct": active_share_in_pure_oil * 100.0,
            "finished_pct": finished_pct,
            "limit": limit,
            "risk_ratio": risk_ratio,
            "eu_banned": is_banned,
            "is_safe": (not is_banned) and (risk_ratio <= 1.00),
            "is_warn": (not is_banned) and (risk_ratio > 0.80)
        }

    # Convert weighted log10(VP) into a 0-100 Tenacity / Substantivity Score (lower VP = higher longevity)
    # log10(VP) typically spans from +0.3 (citrus ~2 mmHg) down to -4.3 (resins ~0.00005 mmHg)
    tenacity_score = round(min(100.0, max(5.0, ((-weighted_log_vp + 0.5) / 4.8) * 100.0)), 1)

    base_cat4 = max_safe_dosage_pct
    cat_specs = [
        ("Category 1", "唇部產品 (Lip Products)", "Lip Products", min(100.0, round(base_cat4 * 0.08, 2))),
        ("Category 2", "體香劑與止汗劑 (Deodorants / Antiperspirants)", "Deodorants / Antiperspirants", min(100.0, round(base_cat4 * 0.15, 2))),
        ("Category 3", "臉部彩妝與眼周產品 (Eye / Facial Make-up)", "Eye / Facial Make-up", min(100.0, round(base_cat4 * 0.25, 2))),
        ("Category 4", "酒精型香水 (Fine Fragrance: EdP / EdT / Cologne)", "Fine Fragrance (EdP / EdT / Cologne)", min(100.0, round(base_cat4 * 1.00, 2))),
        ("Category 5A", "身體乳液與霜類 (Body Lotion / Cream)", "Body Lotion / Cream", min(100.0, round(base_cat4 * 0.65, 2))),
        ("Category 5B", "臉部保濕乳液 (Facial Moisturizer)", "Facial Moisturizer", min(100.0, round(base_cat4 * 0.35, 2))),
        ("Category 5C", "護手霜 (Hand Cream)", "Hand Cream", min(100.0, round(base_cat4 * 0.50, 2))),
        ("Category 5D", "嬰幼兒護理產品 (Baby Cream / Oil)", "Baby Cream / Oil", min(100.0, round(base_cat4 * 0.12, 2))),
        ("Category 6", "口腔與漱口產品 (Mouthwash / Toothpaste)", "Mouthwash / Toothpaste", min(100.0, round(base_cat4 * 0.03, 2))),
        ("Category 7A/7B", "髮品與造型噴霧 (Hair Care / Styling)", "Hair Care / Styling", min(100.0, round(base_cat4 * 0.65, 2))),
        ("Category 8", "私密處清潔濕巾 (Intimate Wipes)", "Intimate Wipes", min(100.0, round(base_cat4 * 0.12, 2))),
        ("Category 9", "洗沐沖洗類產品 (Soap / Shampoo / Shower Gel)", "Soap / Shampoo / Shower Gel", min(100.0, round(base_cat4 * 2.50, 2))),
        ("Category 10A", "居家清潔劑 (Household Cleaners)", "Household Cleaners", min(100.0, round(base_cat4 * 2.50, 2))),
        ("Category 10B", "空間芳香噴霧 (Air Freshener Sprays)", "Air Freshener Sprays", min(100.0, round(base_cat4 * 1.50, 2))),
        ("Category 11A/11B", "紙尿褲與衛生棉 (Diapers / Feminine Care)", "Diapers / Feminine Care", min(100.0, round(base_cat4 * 0.12, 2))),
        ("Category 12", "香氛蠟燭、擴香枝、線香 (Candles / Diffusers / Incense)", "Candles / Diffusers / Incense", 100.0)
    ]
    if lang == "en":
        ifra_categories = [
            {"IFRA Category": c_id, "Product Type / Application": c_en, "Max Allowable Conc. (%)": f"{c_lim:.2f}%"}
            for c_id, c_zh, c_en, c_lim in cat_specs
        ]
    else:
        ifra_categories = [
            {"IFRA 類別": c_id, "適用產品應用範圍": c_zh, "純香精最高允許濃度 (%)": f"{c_lim:.2f}%"}
            for c_id, c_zh, c_en, c_lim in cat_specs
        ]

    allergen_totals = {}
    allergen_sources = {}
    for r in resolved_items:
        ing_in_finished_ratio = (r["active_g"] / total_active_g) * dosage_ratio
        src_name = r["name_disp"].split(" (")[0]
        for allg_name, allg_ratio in r.get("allergens", {}).items():
            ppm_val = ing_in_finished_ratio * float(allg_ratio) * 1_000_000.0
            allergen_totals[allg_name] = allergen_totals.get(allg_name, 0.0) + ppm_val
            if ppm_val > 0:
                allergen_sources.setdefault(allg_name, []).append(src_name)

    return {
        "total_active_g": total_active_g,
        "total_carrier_g": total_carrier_g,
        "total_gross_g": total_gross,
        "unmapped_count": unmapped_count,
        "ifra_status": ifra_status,
        "ifra_categories": ifra_categories,
        "allergen_summary": allergen_totals,
        "allergen_sources": allergen_sources,
        "max_safe_dosage_pct": round(max_safe_dosage_pct, 2),
        "tenacity_score": tenacity_score
    }

def calculate_mod_profile(formula_inputs, dosage_ratio, batch_target, core_db, sku_db, custom_db, overfill_pct=3.0, lang="zh"):
    resolved_items = []
    for line_id, entry in formula_inputs.items():
        if entry.get("gross_g", 0.0) <= 0:
            continue
        res = resolve_formula_item(line_id, entry, core_db, sku_db, custom_db, lang=lang)
        dil = res["dilution_pct"] / 100.0
        res["active_g"] = res["gross_g"] * dil
        res["carrier_g"] = res["gross_g"] * (1.0 - dil)
        resolved_items.append(res)

    if not resolved_items:
        return None

    total_gross_g = sum(r["gross_g"] for r in resolved_items)
    total_active_g = sum(r["active_g"] for r in resolved_items)
    total_carrier_g = sum(r["carrier_g"] for r in resolved_items)
    if total_active_g <= 0:
        return None

    total_cost = sum(r["active_g"] * r["cost_per_g"] for r in resolved_items)
    weighted_vol_ml = sum(r["gross_g"] / r["eff_sg"] if r["eff_sg"] > 0 else r["gross_g"] for r in resolved_items)
    jus_sg = round(total_gross_g / weighted_vol_ml, 3) if weighted_vol_ml > 0 else 0.920

    carrier_solvents = {}
    for r in resolved_items:
        if r["carrier_g"] > 0 and "None" not in r["solvent"]:
            carrier_solvents[r["solvent"]] = carrier_solvents.get(r["solvent"], 0.0) + r["carrier_g"]

    norm_active = {}
    notes_pct = {"Top": 0.0, "Mid": 0.0, "Base": 0.0}
    family_pct = {}
    for r in resolved_items:
        pct = (r["active_g"] / total_active_g) * 100.0
        norm_active[r["line_id"]] = {**r, "active_pct": pct}
        note = r.get("note", "Mid")
        notes_pct["Top"] += pct * (0.5 if "-" in note else 1.0) if "Top" in note else 0
        notes_pct["Mid"] += pct * (0.5 if "-" in note else 1.0) if "Mid" in note else 0
        notes_pct["Base"] += pct * (0.5 if "-" in note else 1.0) if "Base" in note else 0
        fam = r.get("family", "Woody")
        family_pct[fam] = family_pct.get(fam, 0.0) + pct

    allergen_totals = {}
    for r in resolved_items:
        ing_in_finished_ratio = (r["active_g"] / total_active_g) * dosage_ratio
        for allg_name, allg_ratio in r.get("allergens", {}).items():
            allergen_totals[allg_name] = allergen_totals.get(allg_name, 0.0) + (ing_in_finished_ratio * float(allg_ratio) * 1_000_000.0)
    declared_allergens = [
        {"name": k, "ppm": round(v, 1), "pct_finished": round(v / 10000.0, 4)}
        for k, v in allergen_totals.items() if v >= 10.0
    ]
    declared_allergens.sort(key=lambda x: x["ppm"], reverse=True)

    finished_density = (dosage_ratio * 0.95) + ((1.0 - dosage_ratio) * 0.835)
    base_batch_g = batch_target["bottles"] * batch_target["vol_ml"] * finished_density
    overfill_factor = 1.0 + (overfill_pct / 100.0)
    total_batch_g = base_batch_g * overfill_factor

    target_active_g = total_batch_g * dosage_ratio
    scale_factor = target_active_g / total_active_g
    target_jus_g = total_gross_g * scale_factor
    target_carrier_g = total_carrier_g * scale_factor
    net_alcohol_g = max(0.0, total_batch_g - target_jus_g)

    bmr_rows = []
    for r in resolved_items:
        dil_str = f"{r['dilution_pct']:.0f}% in {r['solvent'].split(' ')[0]}" if r['dilution_pct'] < 100 else "100% Neat"
        bmr_rows.append({
            "order": 1 if "Base" in r.get("note", "") else 2 if "Mid" in r.get("note", "") else 3,
            "phase": "Phase A",
            "sku_id": r["sku_id"] or "UNMAPPED-L1",
            "lot_no": r["lot_no"],
            "cas": r["cas"],
            "name": r["name_disp"],
            "spec": dil_str,
            "active_w_pct": round((r["active_g"] / total_active_g) * 100.0, 3),
            "pure_active_g": round(r["active_g"] * scale_factor, 2),
            "target_batch_g": round(r["gross_g"] * scale_factor, 2)
        })
    bmr_rows.sort(key=lambda x: (x["order"], x["name"]))
    for idx, r in enumerate(bmr_rows, 1):
        r["seq"] = idx

    # Vapor-pressure informed 24h evaporation curve
    base_ratio = notes_pct["Base"] / 100.0
    drag = 1.0 - (base_ratio * 0.35)
    time_pts = np.linspace(0, 24, 49)
    traj = {"Hour": time_pts, "Top": [], "Mid": [], "Base": []}
    for t in time_pts:
        top_v = notes_pct["Top"] * math.exp(-0.85 * drag * t)
        mid_v = notes_pct["Mid"] * math.exp(-0.22 * drag * t)
        base_v = notes_pct["Base"] * math.exp(-0.04 * drag * t)
        tot = top_v + mid_v + base_v
        if tot > 0:
            traj["Top"].append(round(top_v / tot * 100, 1))
            traj["Mid"].append(round(mid_v / tot * 100, 1))
            traj["Base"].append(round(base_v / tot * 100, 1))
        else:
            traj["Top"].append(0); traj["Mid"].append(0); traj["Base"].append(100)

    return {
        "norm_active": norm_active,
        "notes_pct": notes_pct,
        "family_pct": family_pct,
        "jus_sg": jus_sg,
        "total_gross_g": total_gross_g,
        "total_active_g": total_active_g,
        "total_carrier_g": total_carrier_g,
        "total_cost": total_cost,
        "cost_per_g_jus": round(total_cost / total_gross_g, 2) if total_gross_g > 0 else 0.0,
        "cost_per_g_active": round(total_cost / total_active_g, 2) if total_active_g > 0 else 0.0,
        "declared_allergens": declared_allergens,
        "batch": {
            "base_g": base_batch_g,
            "total_g": total_batch_g,
            "target_jus_g": target_jus_g,
            "target_active_g": target_active_g,
            "target_carrier_g": target_carrier_g,
            "alcohol_g": net_alcohol_g,
            "carrier_solvents": carrier_solvents,
            "batch_fragrance_cost": round(target_active_g * (total_cost / total_active_g), 1)
        },
        "bmr_rows": bmr_rows,
        "trajectory": pd.DataFrame(traj)
    }

def compute_sample_application(jus_formula, target_dosage, bottles, vol_ml):
    total_jus_g = sum(d.get("gross_g", 0.0) for d in jus_formula.values())
    if total_jus_g <= 0:
        return None
    total_active_g = sum(d.get("gross_g", 0.0) * (d.get("dilution_pct", 100.0) / 100.0) for d in jus_formula.values())
    active_in_jus_ratio = total_active_g / total_jus_g if total_jus_g > 0 else 1.0

    finished_density = (target_dosage * 0.95) + ((1.0 - target_dosage) * 0.835)
    base_batch_g = bottles * vol_ml * finished_density
    overfill_total_g = base_batch_g * 1.03

    req_active_g = overfill_total_g * target_dosage
    req_jus_g = req_active_g / active_in_jus_ratio if active_in_jus_ratio > 0 else req_active_g
    net_alcohol_g = max(0.0, overfill_total_g - req_jus_g)

    return {
        "bottles": bottles,
        "vol_ml": vol_ml,
        "dosage_pct": target_dosage * 100.0,
        "overfill_total_g": overfill_total_g,
        "req_jus_g": req_jus_g,
        "net_alcohol_g": net_alcohol_g
    }

def predict_maceration_and_filtration(formula_inputs, dosage_ratio, batch_target, core_db, sku_db, custom_db, lang="zh"):
    resolved_items = []
    for line_id, entry in formula_inputs.items():
        if entry.get("gross_g", 0.0) <= 0:
            continue
        res = resolve_formula_item(line_id, entry, core_db, sku_db, custom_db, lang=lang)
        dil = res["dilution_pct"] / 100.0
        res["active_g"] = res["gross_g"] * dil
        res["carrier_g"] = res["gross_g"] * (1.0 - dil)
        resolved_items.append(res)

    if not resolved_items:
        return None

    total_active_g = sum(r["active_g"] for r in resolved_items)
    total_carrier_g = sum(r["carrier_g"] for r in resolved_items)
    if total_active_g <= 0:
        return None

    heavy_resin_g = 0.0
    natural_g = 0.0
    has_bergamot_phototoxic = False

    for r in resolved_items:
        if r["cas"] == "8007-75-8":
            has_bergamot_phototoxic = True
        if "Natural" in r.get("type", ""):
            natural_g += r["active_g"]
            if r["cas"] == "9000-05-9" or "Resin" in r["name_disp"] or "原精" in r["name_disp"]:
                heavy_resin_g += r["active_g"]

    finished_density = (dosage_ratio * 0.95) + ((1.0 - dosage_ratio) * 0.835)
    base_batch_g = batch_target["bottles"] * batch_target["vol_ml"] * finished_density
    total_batch_g = base_batch_g * 1.03
    target_active_g = total_batch_g * dosage_ratio
    scale_factor = target_active_g / total_active_g
    target_carrier_g = total_carrier_g * scale_factor
    net_alcohol_g = total_batch_g - target_active_g - target_carrier_g

    natural_ratio = natural_g / total_active_g if total_active_g > 0 else 0
    resin_ratio = heavy_resin_g / total_active_g if total_active_g > 0 else 0

    if lang == "en":
        maceration_days = 7
        maceration_desc = "Formula consists primarily of synthetic aroma chemicals; short molecular fusion is sufficient."
        if resin_ratio > 0.15:
            maceration_days = 28
            maceration_desc = "High resin/absolute ratio; 4 weeks maceration required to establish hemiacetal bonds."
        elif natural_ratio > 0.30:
            maceration_days = 21
            maceration_desc = "Rich in natural essential oils; 3 weeks maceration recommended to soften top-note sharpness."
        elif natural_ratio > 0.10:
            maceration_days = 14
            maceration_desc = "Standard commercial fine fragrance maturation; 2 weeks recommended."

        filtration_alerts = []
        if resin_ratio > 0.05:
            filtration_alerts.append({
                "level": "danger",
                "msg": f"⚠️ Detected {resin_ratio*100:.1f}% high-wax/resin content. High risk of flocculation haze in alcohol! Pre-dissolve in TEC and chill at -4°C before filtration."
            })
        elif net_alcohol_g < 0:
            filtration_alerts.append({
                "level": "danger",
                "msg": "🚨 Critical Physical Alert: Carrier solvent weight exceeds total finished batch weight. Cannot add alcohol!"
            })
        else:
            filtration_alerts.append({
                "level": "success",
                "msg": "✅ Physical compatibility passed. Low wax crystallization risk; standard 0.45μm chill filtration is sufficient."
            })
    else:
        maceration_days = 7
        maceration_desc = "配方以純合成單體為主，短效分子融合即可。"
        if resin_ratio > 0.15:
            maceration_days = 28
            maceration_desc = "含有高比例樹脂與原精，需長效熟成 4 週建立半縮醛鍵聯，氣味方能圓潤不刺鼻。"
        elif natural_ratio > 0.30:
            maceration_days = 21
            maceration_desc = "天然精油成分豐富，建議熟成 3 週降低前調刺激感與水解風險。"
        elif natural_ratio > 0.10:
            maceration_days = 14
            maceration_desc = "標準商用香水熟成期，需 2 週讓精油與單體完美交融。"

        filtration_alerts = []
        if resin_ratio > 0.05:
            filtration_alerts.append({
                "level": "danger",
                "msg": f"⚠️ 偵測到 {resin_ratio*100:.1f}% 高蠟質/樹脂成分。加入酒精後極易引發絮凝白濁！強烈建議將該原料改以 TEC 預溶，並於 -4°C 低溫冷濾。"
            })
        elif net_alcohol_g < 0:
            filtration_alerts.append({
                "level": "danger",
                "msg": "🚨 嚴重物理警示：配方自帶的稀釋溶劑總重已大於成品總重，無法加入酒精！請回 Phase 1 提高原料純度。"
            })
        else:
            filtration_alerts.append({
                "level": "success",
                "msg": "✅ 物理相容性過關。成品中未見過高蠟質結晶或絮凝風險，標準 0.45μm 冷濾即可。"
            })

    return {
        "batch_metrics": {
            "bottles": batch_target["bottles"], "vol_ml": batch_target["vol_ml"],
            "base_total_g": base_batch_g, "overfill_total_g": total_batch_g,
            "target_active_g": target_active_g, "target_carrier_g": target_carrier_g,
            "net_alcohol_g": net_alcohol_g
        },
        "maceration": {"days": maceration_days, "desc": maceration_desc},
        "has_bergamot_phototoxic": has_bergamot_phototoxic,
        "natural_pct": round(natural_ratio * 100.0, 1),
        "alerts": filtration_alerts
    }


def map_line_to_sku_conserving_active(entry, target_sku_obj, conserve_active=True):
    """
    Maps a formula line to a Commercial SKU (Layer 2).
    If conserve_active=True, recalculates gross_g so that Pure Active Weight (gross_g * dilution)
    remains strictly conserved when switching dilution tiers (e.g., 10% lab tincture -> 100% neat powder).
    """
    old_gross = float(entry.get("gross_g", 0.0))
    old_dil = float(entry.get("dilution_pct", 100.0)) / 100.0
    pure_active_g = old_gross * old_dil

    new_dil_pct = float(target_sku_obj.get("dilution_pct", 100.0))
    if conserve_active and new_dil_pct > 0 and pure_active_g > 0:
        new_gross = round(pure_active_g / (new_dil_pct / 100.0), 3)
        if new_gross < 0.001:
            new_gross = 0.001
    else:
        new_gross = old_gross

    return {
        "layer": "L2_SKU",
        "cas": target_sku_obj["cas"],
        "sku_id": target_sku_obj["sku_id"],
        "gross_g": new_gross,
        "dilution_pct": new_dil_pct,
        "solvent": target_sku_obj.get("solvent", "None (100%純原液)")
    }

def auto_map_formula_skus(formula_dict, sku_db, conserve_active=True):
    """
    Batch-maps all unmapped L1_CORE entries in a formula to the first matching commercial SKU
    while conserving pure active mass. Returns (updated_formula, mapped_count).
    """
    updated = {}
    mapped_count = 0
    for lid, entry in formula_dict.items():
        if entry.get("layer", "L1_CORE") == "L1_CORE" and entry.get("gross_g", 0.0) > 0:
            cas_no = entry.get("cas", "")
            matches = [s for s in sku_db.values() if s["cas"] == cas_no]
            if matches:
                # Prefer a SKU matching current dilution if available, otherwise first available SKU
                cur_dil = float(entry.get("dilution_pct", 100.0))
                exact_dil = [s for s in matches if abs(float(s.get("dilution_pct", 100.0)) - cur_dil) < 0.1]
                chosen = exact_dil[0] if exact_dil else matches[0]
                updated[lid] = map_line_to_sku_conserving_active(entry, chosen, conserve_active=conserve_active)
                mapped_count += 1
            else:
                updated[lid] = entry
        else:
            updated[lid] = entry
    return updated, mapped_count

def fetch_pubchem_metadata_by_cas(cas_no):
    """
    Queries PubChem PUG REST API by CAS Number to retrieve Molecular Weight & Title.
    Uses standard library urllib with short timeout so offline environments fail gracefully.
    """
    import json
    import urllib.request
    import urllib.parse

    clean_cas = cas_no.strip()
    if not clean_cas:
        return None, "Empty CAS"
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{urllib.parse.quote(clean_cas)}/property/MolecularWeight,Title,IUPACName/JSON"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "NanmenScentLabOS/6.2"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            props = data.get("PropertyTable", {}).get("Properties", [])
            if not props:
                return None, "CAS not found in PubChem"
            p = props[0]
            return {
                "cas": clean_cas,
                "name_en": p.get("Title", clean_cas),
                "mol_w": round(float(p.get("MolecularWeight", 200.0)), 2),
                "iupac": p.get("IUPACName", "")
            }, None
    except Exception as e:
        return None, str(e)
