# config.py

PERFUME_CONCENTRATION_PRESETS = {
    "EdC_5": {
        "ratio": 0.05,
        "zh": "Eau de Cologne (EdC) - 5%",
        "en": "Eau de Cologne (EdC) - 5%"
    },
    "EdT_10": {
        "ratio": 0.10,
        "zh": "Eau de Toilette (EdT) - 10%",
        "en": "Eau de Toilette (EdT) - 10%"
    },
    "EdP_15": {
        "ratio": 0.15,
        "zh": "Eau de Parfum (EdP) - 15% (商業主力推薦)",
        "en": "Eau de Parfum (EdP) - 15% (Commercial Standard)"
    },
    "EdP_18": {
        "ratio": 0.18,
        "zh": "Eau de Parfum Intense - 18%",
        "en": "Eau de Parfum Intense - 18%"
    },
    "Extrait_25": {
        "ratio": 0.25,
        "zh": "Extrait de Parfum - 25% (頂級沙龍高濃度)",
        "en": "Extrait de Parfum - 25% (High Concentration)"
    }
}

REGULATORY_REGIONS = {
    "EU": {
        "code": "EU",
        "name_zh": "EU (歐盟 EC 1223/2009 & IFRA 51st)",
        "name_en": "EU (EC 1223/2009 & IFRA 51st)",
        "allergen_ppm_threshold": 10.0,
        "desc_zh": "全球最嚴苛標準，駐留型產品致敏原超過 10 ppm (0.001%) 強制外盒標示，嚴格遵守 IFRA 51st 限量。",
        "desc_en": "Strictest global standard: leave-on products with allergens > 10 ppm (0.001%) require label declaration; strict IFRA 51st limits."
    },
    "TW": {
        "code": "TW",
        "name_zh": "TW (台灣衛福部 TFDA 化粧品法規)",
        "name_en": "TW (Taiwan TFDA Cosmetic Regulations)",
        "allergen_ppm_threshold": 10.0,
        "desc_zh": "依台灣衛福部化粧品成分標示規定，駐留型香精致敏原超過 10 ppm 須展開標示。",
        "desc_en": "Per Taiwan TFDA cosmetic labeling rules, leave-on fragrance allergens exceeding 10 ppm must be declared."
    },
    "US": {
        "code": "US",
        "name_zh": "US (美國 FDA MoCRA)",
        "name_en": "US (FDA MoCRA)",
        "allergen_ppm_threshold": 10.0,
        "desc_zh": "美國現代化粧品法案 (MoCRA)，要求致敏原全面揭露與產品安全佐證。",
        "desc_en": "US Modernization of Cosmetics Regulation Act (MoCRA), requiring fragrance allergen disclosure and safety substantiation."
    }
}

DILUTION_TIERS = [100.0, 50.0, 20.0, 10.0, 1.0]

SOLVENT_DATABASE = {
    "None (100%純原液)": {"cas": "-", "sg": 1.000, "inci": "", "zh": "None (100%純原液)", "en": "None (100% Neat)"},
    "DPG (二丙二醇)": {"cas": "25265-71-8", "sg": 1.023, "inci": "DIPROPYLENE GLYCOL", "zh": "DPG (二丙二醇)", "en": "DPG (Dipropylene Glycol)"},
    "TEC (檸檬酸三乙酯)": {"cas": "77-93-0", "sg": 1.137, "inci": "TRIETHYL CITRATE", "zh": "TEC (檸檬酸三乙酯)", "en": "TEC (Triethyl Citrate)"},
    "IPM (肉豆蔻酸異丙酯)": {"cas": "110-27-0", "sg": 0.853, "inci": "ISOPROPYL MYRISTATE", "zh": "IPM (肉豆蔻酸異丙酯)", "en": "IPM (Isopropyl Myristate)"},
    "Ethanol (95%變性酒精)": {"cas": "64-17-5", "sg": 0.812, "inci": "ALCOHOL DENAT.", "zh": "Ethanol (95%變性酒精)", "en": "Ethanol (95% Denat.)"},
    "Jojoba Oil (荷荷巴油)": {"cas": "61789-91-1", "sg": 0.865, "inci": "SIMMONDSIA CHINENSIS SEED OIL", "zh": "Jojoba Oil (荷荷巴油)", "en": "Jojoba Oil"},
    "Grapeseed Oil (葡萄籽油)": {"cas": "8024-22-4", "sg": 0.920, "inci": "VITIS VINIFERA SEED OIL", "zh": "Grapeseed Oil (葡萄籽油)", "en": "Grapeseed Oil"},
    "Sweet Almond Oil (甜杏仁油)": {"cas": "8007-69-0", "sg": 0.915, "inci": "PRUNUS AMYGDALUS DULCIS OIL", "zh": "Sweet Almond Oil (甜杏仁油)", "en": "Sweet Almond Oil"}
}
SOLVENT_CHOICES = list(SOLVENT_DATABASE.keys())

DROP_VOLUME_ML = 0.025

STANDARD_ALLERGENS = [
    "Limonene", "Linalool", "Citral", "Geraniol",
    "Benzyl Benzoate", "Cinnamal", "Coumarin", "Eugenol", "Citronellol"
]
