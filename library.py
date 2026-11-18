# library.py

# ==============================================================================
# LAYER 1: 底層化學核心 (CHEMICAL CORE DATABASE - 180+ Curated Materials + EU Banned Radar)
# ==============================================================================
CHEMICAL_CORE_DB = {
    '54464-57-2': {
        "cas": '54464-57-2', "name_cn": '龍涎酮 (Iso E Super)', "name_en": 'Iso E Super',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 234.38, "vapor_pressure_mmhg": 0.00042, "sg_pure": 0.963,
        "ifra_cat4_max": 21.4, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '乾淨透明的雪松木質與天鵝絨般的偽體香，極佳的結構擴散劑。', "desc_en": 'Clean, transparent cedarwood with velvety skin-like aura; exceptional structural diffuser.'
    },
    '6790-58-5': {
        "cas": '6790-58-5', "name_cn": '降龍涎香醚 (Ambroxan)', "name_en": 'Ambroxan',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 236.39, "vapor_pressure_mmhg": 9e-05, "sg_pure": 0.98,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '乾燥礦物感與溫暖龍涎香交織，提供強大尾韻支撐力。', "desc_en": 'Dry mineral facets intertwined with warm ambergris, anchoring the dry-down.'
    },
    '3738-00-9': {
        "cas": '3738-00-9', "name_cn": '賽塔洛克斯 (Cetalox)', "name_en": 'Cetalox',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 236.39, "vapor_pressure_mmhg": 8e-05, "sg_pure": 0.98,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '比 Ambroxan 更潔淨清冷、帶有現代紙張與麝香感的龍涎香單體。', "desc_en": 'Cleaner, crisper ambergris note with modern papery-musk nuances.'
    },
    '70788-30-6': {
        "cas": '70788-30-6', "name_cn": '諾林巴醇 (Norlimbanol / Timberol)', "name_en": 'Norlimbanol',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 226.4, "vapor_pressure_mmhg": 0.00012, "sg_pure": 0.94,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '極度乾燥銳利的動物感木質與廣藿香骨架，穿透力極強。', "desc_en": 'Ultra-dry, animalic woody-patchouli backbone with immense tenacity.'
    },
    '198404-98-7': {
        "cas": '198404-98-7', "name_cn": '爪哇檀香醇 (Javanol)', "name_en": 'Javanol',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 222.37, "vapor_pressure_mmhg": 0.00018, "sg_pure": 0.942,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '極致濃郁且具現代金屬光澤的奶油檀香分子，微量即有驚人擴散。', "desc_en": 'Radiant, creamy sandalwood molecule with modern metallic clarity.'
    },
    '67801-20-1': {
        "cas": '67801-20-1', "name_cn": '伊巴醇 (Ebanol)', "name_en": 'Ebanol',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 208.34, "vapor_pressure_mmhg": 0.00065, "sg_pure": 0.935,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '濃郁滑順的邁索爾檀香木與微帶麝香的奶香木質。', "desc_en": 'Rich, smooth Mysore-type sandalwood with musky-creamy warmth.'
    },
    '65113-99-7': {
        "cas": '65113-99-7', "name_cn": '檀香醇 208 (Sandalore)', "name_en": 'Sandalore',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 210.36, "vapor_pressure_mmhg": 0.0005, "sg_pure": 0.916,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '溫暖圓潤的純淨檀香心材氣息，能柔化花香與木質過渡。', "desc_en": 'Warm, round pure sandalwood heartwood note that smooths floral transitions.'
    },
    '107898-54-4': {
        "cas": '107898-54-4', "name_cn": '多檀醇 (Polysantol)', "name_en": 'Polysantol',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 222.37, "vapor_pressure_mmhg": 0.00025, "sg_pure": 0.912,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '高強度天然感檀香分子，帶有細膩花香甜韻。', "desc_en": 'High-impact natural sandalwood molecule with subtle floral sweetness.'
    },
    '28219-61-6': {
        "cas": '28219-61-6', "name_cn": '巴克達醇 (Bacdanol)', "name_en": 'Bacdanol',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 208.34, "vapor_pressure_mmhg": 0.00058, "sg_pure": 0.918,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '明亮清甜的檀香木質，帶有一絲露水花瓣質感。', "desc_en": 'Bright, sweet sandalwood note with a dewy petal nuance.'
    },
    '19870-74-7': {
        "cas": '19870-74-7', "name_cn": '雪松琥珀醚 (Cedramber)', "name_en": 'Cedramber',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 236.4, "vapor_pressure_mmhg": 0.00035, "sg_pure": 0.955,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '乾燥雪松木屑與溫暖龍涎琥珀的經典橋樑單體。', "desc_en": 'Classic bridge between dry cedar shavings and warm ambergris.'
    },
    '32388-55-9': {
        "cas": '32388-55-9', "name_cn": '甲基柏木酮 (Vertofix Coeur)', "name_en": 'Vertofix Coeur',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 246.39, "vapor_pressure_mmhg": 0.0003, "sg_pure": 0.995,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '深沉厚實的雪松木、皮革與微帶麝香的定香核心。', "desc_en": 'Deep, rich cedarwood, leather, and musky fixative core.'
    },
    '36306-87-3': {
        "cas": '36306-87-3', "name_cn": '開菲利斯 (Kephalis)', "name_en": 'Kephalis',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 238.37, "vapor_pressure_mmhg": 0.0004, "sg_pure": 0.975,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '溫暖煙草、琥珀與絨面木質交織，賦予木質調豐富層次。', "desc_en": 'Warm tobacco, amber, and velvety woodiness adding rich depth.'
    },
    '33704-61-9': {
        "cas": '33704-61-9', "name_cn": '開司米酮 (Cashmeran)', "name_en": 'Cashmeran',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 206.32, "vapor_pressure_mmhg": 0.0011, "sg_pure": 0.962,
        "ifra_cat4_max": 3.8, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '絨毛般的麝香木質、微辛松針與礦物溫泉氣息（IFRA 限值 3.8%）。', "desc_en": 'Velvety musky wood, spicy pine needle, and mineral warmth (IFRA limit 3.8%).'
    },
    '476332-65-7': {
        "cas": '476332-65-7', "name_cn": '極致琥珀 (Amber Xtreme)', "name_en": 'Amber Xtreme',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 250.42, "vapor_pressure_mmhg": 5e-05, "sg_pure": 0.96,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '極高強度的乾燥龍涎琥珀木質，0.1% 即能撐起整支香水的擴散度。', "desc_en": 'Ultra-powerful dry amber-woody booster; 0.1% elevates full-formula projection.'
    },
    '8014-09-3': {
        "cas": '8014-09-3', "name_cn": '廣藿香 (Patchouli)', "name_en": 'Patchouli Oil',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 222.37, "vapor_pressure_mmhg": 0.0021, "sg_pure": 0.965,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '深邃陳香、微帶黑巧克力與雨後泥土的古老根系，西普調靈魂。', "desc_en": 'Deep, aged earthy roots with dark cacao nuances; quintessential chypre anchor.'
    },
    '1450625-49-6': {
        "cas": '1450625-49-6', "name_cn": '淨化廣藿香 (Clearwood)', "name_en": 'Clearwood',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 222.37, "vapor_pressure_mmhg": 0.0018, "sg_pure": 0.955,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '生物發酵製成的透明廣藿香，去除泥土霉味，留下純淨琥珀木質。', "desc_en": 'Biotech clear patchouli prism without damp earthiness; clean amber wood.'
    },
    '8016-96-4': {
        "cas": '8016-96-4', "name_cn": '海地岩蘭草 (Vetiver Haiti)', "name_en": 'Vetiver Oil Haiti',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 218.34, "vapor_pressure_mmhg": 0.0009, "sg_pure": 0.992,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Isoeugenol': 0.002},
        "desc_zh": '煙燻泥土、烘烤堅果與微帶葡萄柚皮清香的頂級根部精油。', "desc_en": 'Smoky earthy roots with roasted hazelnut and grapefruit peel facets.'
    },
    '117-98-6': {
        "cas": '117-98-6', "name_cn": '乙酸岩蘭草酯 (Vetiveryl Acetate)', "name_en": 'Vetiveryl Acetate',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 262.39, "vapor_pressure_mmhg": 0.00045, "sg_pure": 0.985,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '去除岩蘭草苦澀煙燻感，轉化為絲滑高雅的木質定香劑。', "desc_en": 'Refined, silky woody fixative stripping raw bitterness from vetiver.'
    },
    '8006-87-9': {
        "cas": '8006-87-9', "name_cn": '東印度檀香 (Sandalwood Mysore)', "name_en": 'Sandalwood Album Oil',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 220.35, "vapor_pressure_mmhg": 0.0004, "sg_pure": 0.974,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '溫潤如絲緞般的乳脂檀木香氣，定香與圓潤度無可取代。', "desc_en": 'Velvety, creamy, sacred sandalwood heartwood; incomparable natural fixative.'
    },
    '8024-35-9': {
        "cas": '8024-35-9', "name_cn": '澳洲檀香 (Australian Sandalwood)', "name_en": 'Sandalwood Spicatum Oil',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 220.35, "vapor_pressure_mmhg": 0.00055, "sg_pure": 0.965,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Farnesol': 0.015},
        "desc_zh": '帶有乾燥木屑與微辛樹脂前韻的永續來源檀香精油。', "desc_en": 'Sustainably harvested sandalwood with dry wood-shaving and resinous top facets.'
    },
    '8000-27-9': {
        "cas": '8000-27-9', "name_cn": '維吉尼亞雪松 (Cedarwood Virginia)', "name_en": 'Cedarwood Virginia Oil',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 222.37, "vapor_pressure_mmhg": 0.0048, "sg_pure": 0.92,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '乾燥削鉛筆木屑的經典冷冽木質，定香力極強。', "desc_en": 'Classic dry pencil-shaving cedarwood with tenacious fixative power.'
    },
    '8023-85-6': {
        "cas": '8023-85-6', "name_cn": '大西洋雪松 (Cedarwood Atlas)', "name_en": 'Cedarwood Atlas Oil',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 218.34, "vapor_pressure_mmhg": 0.0039, "sg_pure": 0.935,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '溫暖帶動物感與蜂蜜樹脂韻味的北非雪松木質。', "desc_en": 'Warm, slightly animalic North African cedarwood with honeyed resin nuances.'
    },
    '91770-58-0': {
        "cas": '91770-58-0', "name_cn": '台灣肖楠 (Taiwan Incense Cedar)', "name_en": 'Taiwan Incense Cedar Oil',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 220.35, "vapor_pressure_mmhg": 0.0032, "sg_pure": 0.94,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '台灣特有種，沉穩內斂的百年古剎冷冽木質與溫潤奶香。', "desc_en": 'Endemic Taiwanese wood oil; meditative, cool temple woodiness with creamy warmth.'
    },
    '91745-96-9': {
        "cas": '91745-96-9', "name_cn": '台灣紅檜 (Taiwan Red Hinoki)', "name_en": 'Taiwan Red Hinoki Oil',
        "note": 'Mid-Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 222.37, "vapor_pressure_mmhg": 0.0055, "sg_pure": 0.94,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '台灣高山霧林紅檜，檸檬清香與深邃檜木醇完美平衡。', "desc_en": 'Taiwanese alpine red cypress; lemon-zest clarity balanced with deep hinokitiol.'
    },
    '8016-23-7': {
        "cas": '8016-23-7', "name_cn": '癒創木 (Guaiacwood)', "name_en": 'Guaiacwood Oil',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 222.37, "vapor_pressure_mmhg": 0.0008, "sg_pure": 0.968,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '溫潤煙燻茶香、玫瑰木質與微甜香草氣息的半固態樹脂木油。', "desc_en": 'Warm smoky tea, rosy woodiness, and mild vanilla facets.'
    },
    '8016-36-2': {
        "cas": '8016-36-2', "name_cn": '乳香 (Olibanum / Frankincense)', "name_en": 'Olibanum Oil',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 0.018, "sg_pure": 0.875,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.14},
        "desc_zh": '神聖靜謐的古老樹脂煙燻感，前調帶有清亮檸檬松針氣息。', "desc_en": 'Sacred, tranquil ancient resin with bright lemon-pine top terpenes and balsamic depth.'
    },
    '8016-37-3': {
        "cas": '8016-37-3', "name_cn": '沒藥 (Myrrh)', "name_en": 'Myrrh Oil',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 218.34, "vapor_pressure_mmhg": 0.0025, "sg_pure": 0.995,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '苦甜交織、帶有蘑菇泥土與溫暖藥草樹脂感的古老香料。', "desc_en": 'Bittersweet, earthy-mushroom and warm balsamic ancient resin.'
    },
    '8001-61-4': {
        "cas": '8001-61-4', "name_cn": '古巴香脂 (Copaiba)', "name_en": 'Copaiba Balsam Oil',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 204.35, "vapor_pressure_mmhg": 0.0085, "sg_pure": 0.9,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '深沉溫和的木質樹脂底蘊，極佳的天然定香劑。', "desc_en": 'Gentle, woody-balsamic base note; superb natural fixative.'
    },
    '8013-86-3': {
        "cas": '8013-86-3', "name_cn": '絲柏 (Cypress)', "name_en": 'Cypress Oil',
        "note": 'Mid', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 0.54, "sg_pure": 0.87,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.04},
        "desc_zh": '冷冽乾燥的針葉柏木氣息，為木質調帶來垂直向上的森林骨架。', "desc_en": 'Cool, dry needle-woody heart that builds vertical forest structure.'
    },
    '8021-29-2': {
        "cas": '8021-29-2', "name_cn": '西伯利亞冷杉 (Siberian Fir)', "name_en": 'Siberian Fir Needle Oil',
        "note": 'Top', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 196.29, "vapor_pressure_mmhg": 0.68, "sg_pure": 0.9,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.15},
        "desc_zh": '高比例乙酸龍腦酯，清冷雪松針葉與微甜樹脂香。', "desc_en": 'High bornyl acetate content; crisp pine-needle freshness with sweet balsamic undertones.'
    },
    '8022-91-1': {
        "cas": '8022-91-1', "name_cn": '芳樟 (Ho Wood)', "name_en": 'Ho Wood Oil',
        "note": 'Mid', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 154.25, "vapor_pressure_mmhg": 0.16, "sg_pure": 0.865,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Linalool': 0.92},
        "desc_zh": '富含天然右旋沉香醇，比花梨木更細膩的溫暖花香木質。', "desc_en": 'Rich in natural linalool; smooth, floral-woody heart softer than rosewood.'
    },
    '499-44-5': {
        "cas": '499-44-5', "name_cn": '檜木醇 (Hinokitiol)', "name_en": 'Hinokitiol',
        "note": 'Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 164.2, "vapor_pressure_mmhg": 0.002, "sg_pure": 1.05,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '台灣紅檜特有的結晶單體，清冷抗菌森林木質核心。', "desc_en": 'Signature crystalline tropolone of Taiwanese Hinoki; crisp forest woodiness.'
    },
    '24851-98-7': {
        "cas": '24851-98-7', "name_cn": '二氫茉莉酮酸甲酯 (Hedione)', "name_en": 'Hedione',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 226.31, "vapor_pressure_mmhg": 0.0012, "sg_pure": 1.0,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '輕盈透明的水感茉莉微風，無形中提亮所有花香與柑橘輪廓。', "desc_en": 'Airy, transparent watery jasmine breeze that effortlessly lifts floral and citrus accords.'
    },
    '60-12-8': {
        "cas": '60-12-8', "name_cn": '苯乙醇 (PEA)', "name_en": 'Phenethyl Alcohol (PEA)',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 122.16, "vapor_pressure_mmhg": 0.086, "sg_pure": 1.02,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '新鮮露水玫瑰花瓣的核心骨架，溫潤柔和。', "desc_en": 'Core building block of dewy fresh rose petals; soft, honeyed, and warm.'
    },
    '106-22-9': {
        "cas": '106-22-9', "name_cn": '香茅醇 (Citronellol)', "name_en": 'Citronellol',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 156.27, "vapor_pressure_mmhg": 0.02, "sg_pure": 0.855,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Citronellol': 1.0},
        "desc_zh": '乾淨明亮的玫瑰與天竺葵花香，賦予花束真實的植物水潤感。', "desc_en": 'Clean, bright rose-geranium floralcy giving bouquets lifelike botanical hydration.'
    },
    '106-24-1': {
        "cas": '106-24-1', "name_cn": '牻牛兒醇 (Geraniol)', "name_en": 'Geraniol',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 154.25, "vapor_pressure_mmhg": 0.03, "sg_pure": 0.889,
        "ifra_cat4_max": 5.3, "eu_banned": False, "baseline_allergens": {'Geraniol': 1.0},
        "desc_zh": '甜美濃郁的玫瑰花瓣與微帶柑橘果香的核心單體（IFRA 限值 5.3%）。', "desc_en": 'Sweet, rich rose petal monomer with citrus-fruity nuances (IFRA limit 5.3%).'
    },
    '106-25-2': {
        "cas": '106-25-2', "name_cn": '橙花醇 (Nerol)', "name_en": 'Nerol',
        "note": 'Top-Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 154.25, "vapor_pressure_mmhg": 0.035, "sg_pure": 0.881,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Geraniol': 0.02},
        "desc_zh": '比牻牛兒醇更清新水潤、帶有檸檬橙花氣息的玫瑰單體。', "desc_en": 'Fresher, more watery and citrus-neroli faceted than geraniol.'
    },
    '78-70-6': {
        "cas": '78-70-6', "name_cn": '芳樟醇 (Linalool)', "name_en": 'Linalool',
        "note": 'Top-Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 154.25, "vapor_pressure_mmhg": 0.16, "sg_pure": 0.861,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Linalool': 1.0},
        "desc_zh": '薰衣草、佛手柑與花梨木的共通靈魂，帶來通透潔淨的花木前調。', "desc_en": 'Universal floral-woody bridge found in lavender and bergamot; airy top lift.'
    },
    '115-95-7': {
        "cas": '115-95-7', "name_cn": '乙酸芳樟酯 (Linalyl Acetate)', "name_en": 'Linalyl Acetate',
        "note": 'Top', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 196.29, "vapor_pressure_mmhg": 0.11, "sg_pure": 0.895,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Linalool': 0.01},
        "desc_zh": '佛手柑與真正薰衣草的果香酯類核心，優雅柔和。', "desc_en": 'Fruity-floral ester heart of bergamot and true lavender.'
    },
    '16409-43-1': {
        "cas": '16409-43-1', "name_cn": '玫瑰醚 (Rose Oxide)', "name_en": 'Rose Oxide',
        "note": 'Top-Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 154.25, "vapor_pressure_mmhg": 0.42, "sg_pure": 0.875,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '金屬感、荔枝與鮮綠玫瑰葉的強烈穿透前調，微量即有驚人立體感。', "desc_en": 'Metallic, lychee, and crushed green rose-leaf top note; immense lift at trace levels.'
    },
    '23696-85-7': {
        "cas": '23696-85-7', "name_cn": '大馬士革酮 (Damascenone)', "name_en": 'Beta-Damascenone',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 190.28, "vapor_pressure_mmhg": 0.015, "sg_pure": 0.942,
        "ifra_cat4_max": 0.02, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '極致濃郁的熟蘋果、李子果醬與大馬士革玫瑰靈魂（IFRA 嚴格限量 0.02%！）。', "desc_en": 'Opulent stewed apple, plum jam, and Damask rose soul (Strict IFRA limit 0.02%!).'
    },
    '24720-09-0': {
        "cas": '24720-09-0', "name_cn": 'α-大馬士革酮 (Alpha-Damascone)', "name_en": 'Alpha-Damascone',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 192.3, "vapor_pressure_mmhg": 0.019, "sg_pure": 0.934,
        "ifra_cat4_max": 0.02, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '帶有黑醋栗與茶香的鮮活玫瑰果香單體（IFRA 嚴格限量 0.02%）。', "desc_en": 'Vibrant rose-plum monomer with blackcurrant and tea facets (IFRA limit 0.02%).'
    },
    '23726-92-3': {
        "cas": '23726-92-3', "name_cn": 'β-大馬士革酮 (Beta-Damascone)', "name_en": 'Beta-Damascone',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 192.3, "vapor_pressure_mmhg": 0.018, "sg_pure": 0.938,
        "ifra_cat4_max": 0.02, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '深沉蜂蜜菸草與天鵝絨紅玫瑰花瓣香氣（IFRA 嚴格限量 0.02%）。', "desc_en": 'Deep honeyed tobacco and velvety red rose petal aroma (IFRA limit 0.02%).'
    },
    '57378-68-4': {
        "cas": '57378-68-4', "name_cn": 'δ-大馬士革酮 (Delta-Damascone)', "name_en": 'Delta-Damascone',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 192.3, "vapor_pressure_mmhg": 0.022, "sg_pure": 0.93,
        "ifra_cat4_max": 0.02, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '黑醋栗芽與酸甜紅莓玫瑰前中調單體（IFRA 嚴格限量 0.02%）。', "desc_en": 'Cassis bud and tart red-berry rose monomer (IFRA limit 0.02%).'
    },
    '105-87-3': {
        "cas": '105-87-3', "name_cn": '乙酸牻牛兒酯 (Geranyl Acetate)', "name_en": 'Geranyl Acetate',
        "note": 'Top-Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 196.29, "vapor_pressure_mmhg": 0.032, "sg_pure": 0.91,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Geraniol': 0.01},
        "desc_zh": '清甜梨子、薰衣草與玫瑰花瓣的明亮酯類。', "desc_en": 'Crisp pear, lavender, and rose petal ester.'
    },
    '150-84-5': {
        "cas": '150-84-5', "name_cn": '乙酸香茅酯 (Citronellyl Acetate)', "name_en": 'Citronellyl Acetate',
        "note": 'Top-Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 198.3, "vapor_pressure_mmhg": 0.038, "sg_pure": 0.89,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Citronellol': 0.01},
        "desc_zh": '果香清新、帶檸檬皮與天竺葵葉氣息的輕盈玫瑰酯。', "desc_en": 'Fruity-fresh rose ester with lemon zest and geranium leaf nuances.'
    },
    '103-45-7': {
        "cas": '103-45-7', "name_cn": '乙酸苯乙酯 (Phenethyl Acetate)', "name_en": 'Phenethyl Acetate',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 164.2, "vapor_pressure_mmhg": 0.055, "sg_pure": 1.032,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '蜂蜜、水蜜桃與粉紅玫瑰的甜美花果單體。', "desc_en": 'Honeyed peach and pink rose floral-fruity monomer.'
    },
    '140-11-4': {
        "cas": '140-11-4', "name_cn": '乙酸苄酯 (Benzyl Acetate)', "name_en": 'Benzyl Acetate',
        "note": 'Top-Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 150.17, "vapor_pressure_mmhg": 0.177, "sg_pure": 1.055,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '茉莉與依蘭的核心果香前調，帶有成熟香蕉與水梨甜潤。', "desc_en": 'Core fruity top note of jasmine and ylang with ripe pear/banana sweetness.'
    },
    '118-58-1': {
        "cas": '118-58-1', "name_cn": '水楊酸苄酯 (Benzyl Salicylate)', "name_en": 'Benzyl Salicylate',
        "note": 'Base', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 228.24, "vapor_pressure_mmhg": 0.0001, "sg_pure": 1.176,
        "ifra_cat4_max": 17.7, "eu_banned": False, "baseline_allergens": {'Benzyl Salicylate': 1.0},
        "desc_zh": '陽光曬暖肌膚般的溫暖花香定香劑，白花與防曬調靈魂（IFRA 限值 17.7%）。', "desc_en": 'Sun-warmed skin floral fixative; soul of solar white florals (IFRA limit 17.7%).'
    },
    '100-51-6': {
        "cas": '100-51-6', "name_cn": '苯甲醇 (Benzyl Alcohol)', "name_en": 'Benzyl Alcohol',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 108.14, "vapor_pressure_mmhg": 0.094, "sg_pure": 1.045,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Benzyl Alcohol': 1.0},
        "desc_zh": '溫和微甜的杏仁花香溶劑與茉莉伴侶。', "desc_en": 'Mildly sweet almond-floral solvent and natural jasmine companion.'
    },
    '134-20-3': {
        "cas": '134-20-3', "name_cn": '鄰氨基苯甲酸甲酯 (Methyl Anthranilate)', "name_en": 'Methyl Anthranilate',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 151.16, "vapor_pressure_mmhg": 0.025, "sg_pure": 1.168,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '橙花、晚香玉與康科德葡萄的濃郁甜美氮雜單體（易使香水變色）。', "desc_en": 'Rich orange blossom, tuberose, and Concord grape note (causes Schiff base browning).'
    },
    '89-43-0': {
        "cas": '89-43-0', "name_cn": '橙花素 (Aurantiol)', "name_en": 'Aurantiol',
        "note": 'Base', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 285.38, "vapor_pressure_mmhg": 4e-05, "sg_pure": 1.06,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Hydroxycitronellal': 0.45},
        "desc_zh": '橙花與鈴蘭的席夫鹼縮合物，金黃濃郁且定香力極強。', "desc_en": 'Golden, tenacious Schiff base of methyl anthranilate and hydroxycitronellal.'
    },
    '107-75-5': {
        "cas": '107-75-5', "name_cn": '羥基香茅醛 (Hydroxycitronellal)', "name_en": 'Hydroxycitronellal',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 172.26, "vapor_pressure_mmhg": 0.008, "sg_pure": 0.922,
        "ifra_cat4_max": 3.6, "eu_banned": False, "baseline_allergens": {'Hydroxycitronellal': 1.0},
        "desc_zh": '經典水潤鈴蘭與菩提花核心單體（IFRA 限值 3.6%）。', "desc_en": 'Classic dewy lily-of-the-valley (muguet) and linden blossom core (IFRA limit 3.6%).'
    },
    '125109-85-5': {
        "cas": '125109-85-5', "name_cn": '花青醛 (Florhydral)', "name_en": 'Florhydral',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 190.28, "vapor_pressure_mmhg": 0.012, "sg_pure": 0.945,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '現代水感鈴蘭與風信子綠意花香，擴散力極佳且無過敏原限制。', "desc_en": 'Modern watery muguet and hyacinth green floral; high diffusion without allergen restrictions.'
    },
    '103694-68-4': {
        "cas": '103694-68-4', "name_cn": '鈴蘭醇 (Majantol)', "name_en": 'Majantol',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 164.24, "vapor_pressure_mmhg": 0.014, "sg_pure": 0.94,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '純淨透明的鈴蘭花香醇類，常作為傳統鈴蘭醛的安全替代核心。', "desc_en": 'Clean, transparent muguet alcohol; safe modern replacement for restricted muguet aldehydes.'
    },
    '13828-37-0': {
        "cas": '13828-37-0', "name_cn": '五月醇 (Mayol)', "name_en": 'Mayol',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 156.27, "vapor_pressure_mmhg": 0.016, "sg_pure": 0.915,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '柔和細膩的鈴蘭與紫丁香花瓣單體。', "desc_en": 'Soft, delicate muguet and lilac petal monomer.'
    },
    '1205-17-0': {
        "cas": '1205-17-0', "name_cn": '新洋茉莉醛 (Helional)', "name_en": 'Helional',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 192.21, "vapor_pressure_mmhg": 0.0045, "sg_pure": 1.162,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '水感西瓜、仙客來與陽光臭氧花香，現代水生調核心。', "desc_en": 'Watery melon, cyclamen, and solar ozonic floral; core of modern aquatic accords.'
    },
    '103-95-7': {
        "cas": '103-95-7', "name_cn": '仙客來醛 (Cyclamen Aldehyde)', "name_en": 'Cyclamen Aldehyde',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 190.28, "vapor_pressure_mmhg": 0.011, "sg_pure": 0.95,
        "ifra_cat4_max": 0.95, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '清新露水仙客來與椴樹花香（IFRA 限值 0.95%）。', "desc_en": 'Fresh dewy cyclamen and linden blossom aldehyde (IFRA limit 0.95%).'
    },
    '101-86-0': {
        "cas": '101-86-0', "name_cn": '己基肉桂醛 (Hexyl Cinnamal)', "name_en": 'Alpha-Hexyl Cinnamaldehyde',
        "note": 'Mid-Base', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 216.32, "vapor_pressure_mmhg": 0.0007, "sg_pure": 0.95,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Hexyl Cinnamal': 1.0},
        "desc_zh": '溫暖油潤的茉莉花心定香單體。', "desc_en": 'Warm, oily jasmine heart fixative monomer.'
    },
    '127-51-5': {
        "cas": '127-51-5', "name_cn": 'α-異甲基紫羅蘭酮 (Alpha-Isomethyl Ionone)', "name_en": 'Alpha-Isomethyl Ionone',
        "note": 'Mid-Base', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 206.32, "vapor_pressure_mmhg": 0.0021, "sg_pure": 0.935,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Alpha-Isomethyl Ionone': 1.0},
        "desc_zh": '天鵝絨般的紫羅蘭與鳶尾根粉感木質花香。', "desc_en": 'Velvety violet and orris-root powdery woody-floral.'
    },
    '14901-07-6': {
        "cas": '14901-07-6', "name_cn": 'β-紫羅蘭酮 (Beta-Ionone)', "name_en": 'Beta-Ionone',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 192.3, "vapor_pressure_mmhg": 0.004, "sg_pure": 0.945,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '溫暖木質紫羅蘭與覆盆子果香，為花香與木質帶來絲絨感。', "desc_en": 'Warm woody violet and raspberry note lending velvety texture.'
    },
    '127-41-3': {
        "cas": '127-41-3', "name_cn": 'α-紫羅蘭酮 (Alpha-Ionone)', "name_en": 'Alpha-Ionone',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 192.3, "vapor_pressure_mmhg": 0.0052, "sg_pure": 0.931,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '比 β-紫羅蘭酮更清甜粉嫩的紫羅蘭花瓣香氣。', "desc_en": 'Sweeter, more powdery violet petal note than beta-ionone.'
    },
    '79-69-6': {
        "cas": '79-69-6', "name_cn": '鳶尾酮 (Alpha-Irone)', "name_en": 'Alpha-Irone',
        "note": 'Base', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 206.32, "vapor_pressure_mmhg": 0.0015, "sg_pure": 0.934,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '珍貴鳶尾根脂的冷冽粉質紫羅蘭與奶油木質靈魂。', "desc_en": 'Cool powdery violet and buttery woodiness of precious orris butter.'
    },
    '120-72-9': {
        "cas": '120-72-9', "name_cn": '吲哚 (Indole)', "name_en": 'Indole',
        "note": 'Mid-Base', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 117.15, "vapor_pressure_mmhg": 0.012, "sg_pure": 1.06,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '低濃度時呈現真實白花（茉莉、橙花）的豐潤肉感，高濃度具動物性。', "desc_en": 'Imparts lifelike narcotic fleshiness to jasmine and orange blossom at trace levels.'
    },
    '488-10-8': {
        "cas": '488-10-8', "name_cn": '順式茉莉酮 (Cis-Jasmone)', "name_en": 'Cis-Jasmone',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 164.24, "vapor_pressure_mmhg": 0.028, "sg_pure": 0.944,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '天然茉莉原精中不可或缺的辛香草本白花核心分子。', "desc_en": 'Essential spicy-herbaceous white floral molecule of natural jasmine absolute.'
    },
    '8007-01-0': {
        "cas": '8007-01-0', "name_cn": '大馬士革玫瑰精油 (Rose Otto)', "name_en": 'Rose Damascena Otto',
        "note": 'Mid', "family": 'Floral', "type": 'Natural Essential Oil',
        "mol_w": 154.25, "vapor_pressure_mmhg": 0.025, "sg_pure": 0.855,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Citronellol': 0.35, 'Geraniol': 0.22, 'Eugenol': 0.015},
        "desc_zh": '保加利亞水蒸氣蒸餾，清冽蜂蜜檸檬與露水玫瑰花瓣（低溫會凝結結晶）。', "desc_en": 'Bulgarian steam-distilled rose; crisp honey-lemon and dewy rose petals (crystallizes when cool).'
    },
    '84604-12-6': {
        "cas": '84604-12-6', "name_cn": '千葉玫瑰原精 (Rose Centifolia Abs.)', "name_en": 'Rose Centifolia Absolute',
        "note": 'Mid-Base', "family": 'Floral', "type": 'Natural Essential Oil',
        "mol_w": 122.16, "vapor_pressure_mmhg": 0.015, "sg_pure": 0.98,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Phenethyl Alcohol': 0.6, 'Citronellol': 0.12, 'Geraniol': 0.08},
        "desc_zh": '格拉斯溶劑萃取，深沉蜂蜜與辛香暖意的濃郁紅玫瑰。', "desc_en": 'Grasse solvent-extracted rose; deep honeyed, spicy, opulent red rose.'
    },
    '91770-14-8': {
        "cas": '91770-14-8', "name_cn": '小花茉莉原精 (Jasmine Sambac Abs.)', "name_en": 'Jasmine Sambac Absolute',
        "note": 'Mid', "family": 'Floral', "type": 'Natural Essential Oil',
        "mol_w": 150.17, "vapor_pressure_mmhg": 0.018, "sg_pure": 0.96,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Linalool': 0.06, 'Benzyl Alcohol': 0.03},
        "desc_zh": '帶有綠茶、橙花與熱帶果香的清甜奔放茉莉。', "desc_en": 'Vibrant, sweet jasmine with green tea, orange blossom, and tropical fruit nuances.'
    },
    '8022-96-6': {
        "cas": '8022-96-6', "name_cn": '大花茉莉原精 (Jasmine Grandiflorum Abs.)', "name_en": 'Jasmine Grandiflorum Absolute',
        "note": 'Mid-Base', "family": 'Floral', "type": 'Natural Essential Oil',
        "mol_w": 150.17, "vapor_pressure_mmhg": 0.014, "sg_pure": 0.955,
        "ifra_cat4_max": 0.7, "eu_banned": False, "baseline_allergens": {'Benzyl Benzoate': 0.15, 'Linalool': 0.05, 'Eugenol': 0.03},
        "desc_zh": '經典法式香水靈魂，深邃吲哚白花與成熟果香（IFRA 限值 0.7%）。', "desc_en": 'Classic French perfumery icon; deep indolic white floral with ripe fruit (IFRA limit 0.7%).'
    },
    '8016-38-4': {
        "cas": '8016-38-4', "name_cn": '突尼西亞橙花精油 (Neroli Bigarade)', "name_en": 'Neroli Oil',
        "note": 'Top-Mid', "family": 'Floral', "type": 'Natural Essential Oil',
        "mol_w": 154.25, "vapor_pressure_mmhg": 0.12, "sg_pure": 0.872,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Linalool': 0.35, 'Limonene': 0.15, 'Geraniol': 0.03},
        "desc_zh": '苦橙花瓣水蒸氣蒸餾，清冷高雅、微帶蜂蜜苦橙葉氣息。', "desc_en": 'Steam-distilled bitter orange blossoms; crisp, aristocratic, honeyed floralcy.'
    },
    '8006-81-3': {
        "cas": '8006-81-3', "name_cn": '完全伊蘭 (Ylang Complete)', "name_en": 'Ylang Ylang Complete Oil',
        "note": 'Mid', "family": 'Floral', "type": 'Natural Essential Oil',
        "mol_w": 180.24, "vapor_pressure_mmhg": 0.024, "sg_pure": 0.93,
        "ifra_cat4_max": 0.8, "eu_banned": False, "baseline_allergens": {'Benzyl Benzoate': 0.08, 'Linalool': 0.12, 'Geraniol': 0.02},
        "desc_zh": '濃郁異國感與奶油般醉人的熱帶白花香（IFRA 限值 0.8%）。', "desc_en": 'Opulent, creamy, narcotic tropical white floral (IFRA limit 0.8%).'
    },
    '8014-19-5': {
        "cas": '8014-19-5', "name_cn": '玫瑰草 (Palmarosa)', "name_en": 'Palmarosa Oil',
        "note": 'Mid', "family": 'Floral', "type": 'Natural Essential Oil',
        "mol_w": 154.25, "vapor_pressure_mmhg": 0.042, "sg_pure": 0.885,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Geraniol': 0.82, 'Linalool': 0.03},
        "desc_zh": '富含天然牻牛兒醇，帶有清新青草露水感的玫瑰花香。', "desc_en": 'Rich in natural geraniol; fresh, dewy, green-grassy rose heart.'
    },
    '8000-46-2': {
        "cas": '8000-46-2', "name_cn": '波旁天竺葵 (Geranium Bourbon)', "name_en": 'Geranium Bourbon Oil',
        "note": 'Mid', "family": 'Floral', "type": 'Natural Essential Oil',
        "mol_w": 156.27, "vapor_pressure_mmhg": 0.045, "sg_pure": 0.892,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Citronellol': 0.32, 'Geraniol': 0.18, 'Linalool': 0.08},
        "desc_zh": '留尼旺島蒸餾，兼具玫瑰花香、薄荷綠葉與荔枝果香的經典中調。', "desc_en": 'Distilled in Réunion; classic rose-mint green leaf floral heart.'
    },
    '8000-28-0': {
        "cas": '8000-28-0', "name_cn": '真正薰衣草 (Lavender Angustifolia)', "name_en": 'Lavender Angustifolia Oil',
        "note": 'Mid', "family": 'Floral', "type": 'Natural Essential Oil',
        "mol_w": 196.29, "vapor_pressure_mmhg": 0.11, "sg_pure": 0.88,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Linalool': 0.38, 'Limonene': 0.01, 'Coumarin': 0.005},
        "desc_zh": '酯類豐富，乾淨細緻且具安撫力的草本花香。', "desc_en": 'Ester-rich, serene herbaceous floral heart.'
    },
    'NCS-MALLOTUS-01': {
        "cas": 'NCS-MALLOTUS-01', "name_cn": '白楸花天然複方基劑 (Mallotus NCS)', "name_en": 'Mallotus Flower Natural Accord',
        "note": 'Mid', "family": 'Floral', "type": 'Natural Botanical Blend',
        "mol_w": 180.0, "vapor_pressure_mmhg": 0.05, "sg_pure": 0.91,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Linalool': 0.1, 'Limonene': 0.05},
        "desc_zh": '台灣野地白楸花原精結合尤加利與芳樟葉，清甜帶粉感的山野白花香。', "desc_en": 'Wild Taiwanese Mallotus flower absolute blended with eucalyptus and ho leaf; powdery meadow floral.'
    },
    '8007-75-8': {
        "cas": '8007-75-8', "name_cn": '佛手柑 (Bergamot Non-FCF)', "name_en": 'Bergamot Oil (Expressed)',
        "note": 'Top', "family": 'Citrus', "type": 'Natural Essential Oil',
        "mol_w": 196.29, "vapor_pressure_mmhg": 0.82, "sg_pure": 0.875,
        "ifra_cat4_max": 0.4, "eu_banned": False, "baseline_allergens": {'Limonene': 0.42, 'Linalool': 0.12, 'Citral': 0.01},
        "desc_zh": '精緻伯爵茶清香，兼顧檸檬活力與薰衣草花香（未去光敏 IFRA 限值 0.4%）。', "desc_en": 'Refined Earl Grey citrus-floral elegance (Non-FCF IFRA Cat.4 limit: 0.4%).'
    },
    '89957-91-5': {
        "cas": '89957-91-5', "name_cn": '無光敏佛手柑 (Bergamot FCF)', "name_en": 'Bergamot Oil FCF (Bergaptene-Free)',
        "note": 'Top', "family": 'Citrus', "type": 'Natural Essential Oil',
        "mol_w": 196.29, "vapor_pressure_mmhg": 0.85, "sg_pure": 0.872,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.44, 'Linalool': 0.13, 'Citral': 0.01},
        "desc_zh": '分子蒸餾去除佛手柑內酯（無光敏限制），可安全高比例用於日光香水。', "desc_en": 'Distilled bergaptene-free bergamot; safe for high-dosage daytime fine fragrances.'
    },
    '8028-48-6': {
        "cas": '8028-48-6', "name_cn": '甜橙 (Sweet Orange)', "name_en": 'Sweet Orange Oil',
        "note": 'Top', "family": 'Citrus', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 1.54, "sg_pure": 0.844,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.94, 'Linalool': 0.01},
        "desc_zh": '陽光多汁、純真溫暖的鮮榨果實甜香。', "desc_en": 'Radiant, juicy, sun-drenched sweet citrus burst.'
    },
    '8008-57-9': {
        "cas": '8008-57-9', "name_cn": '血橙 (Blood Orange)', "name_en": 'Blood Orange Oil',
        "note": 'Top', "family": 'Citrus', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 1.45, "sg_pure": 0.846,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.92, 'Linalool': 0.01},
        "desc_zh": '帶有紅莓果酸與微苦果皮層次的濃郁柑橘。', "desc_en": 'Rich citrus with red-berry tartness and bittersweet peel depth.'
    },
    '8008-31-9': {
        "cas": '8008-31-9', "name_cn": '紅橘 (Tangerine / Mandarin)', "name_en": 'Tangerine / Mandarin Oil',
        "note": 'Top', "family": 'Citrus', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 1.48, "sg_pure": 0.845,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.9, 'Linalool': 0.01},
        "desc_zh": '比甜橙更柔和微甜、帶有童趣與撫慰感的柑橘香氣。', "desc_en": 'Softer, sweeter, and more comforting than sweet orange.'
    },
    '8008-56-8': {
        "cas": '8008-56-8', "name_cn": '義大利檸檬 (Lemon Cold-Pressed)', "name_en": 'Lemon Oil (Cold-Pressed)',
        "note": 'Top', "family": 'Citrus', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 1.65, "sg_pure": 0.852,
        "ifra_cat4_max": 2.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.68, 'Citral': 0.03},
        "desc_zh": '清脆銳利的鮮榨黃檸檬皮香氣（冷壓版本 IFRA 限值 2.0%）。', "desc_en": 'Crisp, sparkling expressed yellow lemon peel (Cold-pressed IFRA limit 2.0%).'
    },
    '8008-26-2': {
        "cas": '8008-26-2', "name_cn": '蒸餾萊姆 (Lime Distilled)', "name_en": 'Lime Oil (Distilled)',
        "note": 'Top', "family": 'Citrus', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 1.72, "sg_pure": 0.86,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.5, 'Citral': 0.01},
        "desc_zh": '水蒸氣蒸餾萊姆，帶有可樂糖果與清涼松針的無光敏柑橘氣息。', "desc_en": 'Steam-distilled lime with cola-candy and crisp terpene freshness; non-phototoxic.'
    },
    '8016-20-4': {
        "cas": '8016-20-4', "name_cn": '粉紅葡萄柚 (Grapefruit Pink)', "name_en": 'Grapefruit Oil Pink',
        "note": 'Top', "family": 'Citrus', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 1.58, "sg_pure": 0.85,
        "ifra_cat4_max": 4.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.91},
        "desc_zh": '多汁微苦、帶有微量硫醇果香的明亮柑橘（IFRA 限值 4.0%）。', "desc_en": 'Juicy, bittersweet citrus with sparkling grapefruit mercaptan nuances (IFRA limit 4.0%).'
    },
    '233683-84-6': {
        "cas": '233683-84-6', "name_cn": '日本柚子 (Yuzu EO)', "name_en": 'Yuzu Essential Oil',
        "note": 'Top', "family": 'Citrus', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 1.4, "sg_pure": 0.854,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.78, 'Linalool': 0.03},
        "desc_zh": '融合葡萄柚、紅橘與青草木質的日式高雅柑橘。', "desc_en": 'Refined Japanese citrus blending grapefruit, mandarin, and herbal-woody zest.'
    },
    '8014-17-3': {
        "cas": '8014-17-3', "name_cn": '苦橙葉 (Petitgrain)', "name_en": 'Petitgrain Oil',
        "note": 'Top-Mid', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 196.29, "vapor_pressure_mmhg": 0.14, "sg_pure": 0.885,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Linalool': 0.25, 'Limonene': 0.08, 'Geraniol': 0.03},
        "desc_zh": '微苦青澀枝葉中透出細緻橙花氣息，高酯類強力放鬆。', "desc_en": 'Crisp, bittersweet green twigs and leaves revealing delicate neroli-like floralcy.'
    },
    '8023-89-0': {
        "cas": '8023-89-0', "name_cn": '欖香脂 (Elemi)', "name_en": 'Elemi Oil',
        "note": 'Top-Mid', "family": 'Citrus', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 0.76, "sg_pure": 0.88,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.52},
        "desc_zh": '帶有明亮檸檬與黑胡椒辛香的輕盈樹脂，銜接前調與後調的橋樑。', "desc_en": 'Luminous lemon-pepper resin bridging bright citrus tops with olibanum base notes.'
    },
    '5989-27-5': {
        "cas": '5989-27-5', "name_cn": '右旋檸檬烯 (D-Limonene)', "name_en": 'D-Limonene',
        "note": 'Top', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 136.24, "vapor_pressure_mmhg": 1.98, "sg_pure": 0.841,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 1.0},
        "desc_zh": '所有柑橘精油的主要單萜烯骨架，清甜橙皮爆發力（注意抗氧化）。', "desc_en": 'Primary monoterpene backbone of citrus oils; bright sweet orange peel burst.'
    },
    '5392-40-5': {
        "cas": '5392-40-5', "name_cn": '檸檬醛 (Citral)', "name_en": 'Citral',
        "note": 'Top', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 152.24, "vapor_pressure_mmhg": 0.091, "sg_pure": 0.888,
        "ifra_cat4_max": 0.6, "eu_banned": False, "baseline_allergens": {'Citral': 1.0},
        "desc_zh": '銳利清脆的檸檬皮汁液爆發感（IFRA 嚴格限量 0.6%）。', "desc_en": 'Sharp, zesty burst of freshly squeezed lemon peel (strict IFRA Cat.4 limit: 0.6%).'
    },
    '18479-58-8': {
        "cas": '18479-58-8', "name_cn": '二氫月桂烯醇 (Dihydromyrcenol)', "name_en": 'Dihydromyrcenol',
        "note": 'Top', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 156.27, "vapor_pressure_mmhg": 0.35, "sg_pure": 0.834,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '現代古龍水與男香標誌性的冷冽萊姆、薰衣草與金屬潔淨感。', "desc_en": 'Iconic crisp lime, lavender, and metallic freshness of modern colognes.'
    },
    '124-13-0': {
        "cas": '124-13-0', "name_cn": '辛醛 (Aldehyde C-8)', "name_en": 'Aldehyde C-8 (Octanal)',
        "note": 'Top', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 128.21, "vapor_pressure_mmhg": 1.18, "sg_pure": 0.821,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '蠟質鮮橙皮與氣泡香檳般的經典醛香前調。', "desc_en": 'Waxy sweet orange peel and sparkling champagne-like classic aldehyde.'
    },
    '124-19-6': {
        "cas": '124-19-6', "name_cn": '壬醛 (Aldehyde C-9)', "name_en": 'Aldehyde C-9 (Nonanal)',
        "note": 'Top', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 142.24, "vapor_pressure_mmhg": 0.37, "sg_pure": 0.827,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '帶有蠟質玫瑰花瓣與柑橘皮光澤的透明醛香。', "desc_en": 'Transparent waxy rose petal and citrus peel aldehyde.'
    },
    '112-31-2': {
        "cas": '112-31-2', "name_cn": '癸醛 (Aldehyde C-10)', "name_en": 'Aldehyde C-10 (Decanal)',
        "note": 'Top', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 156.27, "vapor_pressure_mmhg": 0.11, "sg_pure": 0.828,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '濃郁甜橙皮與皂感潔淨度的經典醛香支柱。', "desc_en": 'Rich sweet orange peel and soapy cleanliness aldehyde pillar.'
    },
    '112-45-8': {
        "cas": '112-45-8', "name_cn": '十一烯醛 (Aldehyde C-11 Undecylenic)', "name_en": 'Aldehyde C-11 Undecylenic',
        "note": 'Top-Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 168.28, "vapor_pressure_mmhg": 0.045, "sg_pure": 0.842,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": 'Chanel No.5 標誌性的冷冽白花蠟質與微金屬光芒。', "desc_en": 'Signature cold waxy white-floral metallic radiance of classic aldehydic florals.'
    },
    '112-54-9': {
        "cas": '112-54-9', "name_cn": '十二醛 (Aldehyde C-12 Lauric)', "name_en": 'Aldehyde C-12 Lauric',
        "note": 'Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 184.32, "vapor_pressure_mmhg": 0.015, "sg_pure": 0.831,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '溫暖松針、紫羅蘭與高級香皂的綿長粉蠟質感。', "desc_en": 'Warm pine, violet, and luxury soap waxy-powdery depth.'
    },
    '110-41-8': {
        "cas": '110-41-8', "name_cn": '甲基壬基乙醛 (Aldehyde C-12 MNA)', "name_en": 'Aldehyde C-12 MNA',
        "note": 'Top-Mid', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 184.32, "vapor_pressure_mmhg": 0.022, "sg_pure": 0.828,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '乾燥琥珀、冷杉針葉與銀色金屬光澤的現代高級醛香。', "desc_en": 'Dry amber, fir needle, and silver metallic radiance; ultra-chic modern aldehyde.'
    },
    '104-67-6': {
        "cas": '104-67-6', "name_cn": '十四醛 / 桃醛 (Aldehyde C-14 / Gamma-Undecalactone)', "name_en": 'Gamma-Undecalactone (Aldehyde C-14)',
        "note": 'Mid-Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 184.28, "vapor_pressure_mmhg": 0.0035, "sg_pure": 0.944,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '天鵝絨般的熟水蜜桃果皮與奶油白花香氣。', "desc_en": 'Velvety ripe peach skin and creamy white-floral lactone.'
    },
    '77-83-8': {
        "cas": '77-83-8', "name_cn": '十六醛 / 草莓醛 (Aldehyde C-16)', "name_en": 'Ethyl Methylphenylglycidate (C-16)',
        "note": 'Mid', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 206.24, "vapor_pressure_mmhg": 0.0028, "sg_pure": 1.095,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '甜美野生草莓果醬與蜂蜜花香縮水甘油酯。', "desc_en": 'Sweet wild strawberry jam and honeyed floral glycidate.'
    },
    '104-61-0': {
        "cas": '104-61-0', "name_cn": '十八醛 / 椰子醛 (Aldehyde C-18 / Gamma-Nonalactone)', "name_en": 'Gamma-Nonalactone (Aldehyde C-18)',
        "note": 'Mid-Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 156.22, "vapor_pressure_mmhg": 0.014, "sg_pure": 0.96,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '奶油椰子、無花果奶香與防曬乳般的溫暖內酯。', "desc_en": 'Creamy coconut, fig milk, and warm solar-lotion lactone.'
    },
    '928-96-1': {
        "cas": '928-96-1', "name_cn": '順式-3-己烯醇 / 葉醇 (Cis-3-Hexenol)', "name_en": 'Cis-3-Hexenol (Leaf Alcohol)',
        "note": 'Top', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 100.16, "vapor_pressure_mmhg": 1.04, "sg_pure": 0.848,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '剛修剪過的新鮮青草汁液與揉碎綠葉的強烈自然綠意。', "desc_en": 'Intense freshly cut grass and crushed green leaf naturalness.'
    },
    '3681-71-8': {
        "cas": '3681-71-8', "name_cn": '乙酸順式-3-己烯酯 (Cis-3-Hexenyl Acetate)', "name_en": 'Cis-3-Hexenyl Acetate',
        "note": 'Top', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 142.2, "vapor_pressure_mmhg": 0.72, "sg_pure": 0.897,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '帶有青香蕉、綠梨與清脆葉片氣息的果香綠意前調。', "desc_en": 'Fruity-green top note with green banana, crisp pear, and leaf facets.'
    },
    '68039-49-6': {
        "cas": '68039-49-6', "name_cn": '女貞醛 (Triplal / Ligustral)', "name_en": 'Triplal (Ligustral)',
        "note": 'Top', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 138.21, "vapor_pressure_mmhg": 0.48, "sg_pure": 0.935,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '極具穿透力的鮮綠無花果葉與柑橘草本前調。', "desc_en": 'High-impact crushed green fig leaf and zesty herbal top note.'
    },
    '8023-91-4': {
        "cas": '8023-91-4', "name_cn": '白松香精油 (Galbanum Oil)', "name_en": 'Galbanum Oil',
        "note": 'Top-Mid', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 0.62, "sg_pure": 0.88,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.12},
        "desc_zh": '冷冽苦澀的深綠植物汁液與泥土樹脂，法式綠西普調靈魂。', "desc_en": 'Cold, bitter, ultra-green plant sap and earthy resin; soul of French green chypres.'
    },
    '90147-36-7': {
        "cas": '90147-36-7', "name_cn": '紫羅蘭葉原精 (Violet Leaf Absolute)', "name_en": 'Violet Leaf Absolute',
        "note": 'Mid', "family": 'Floral', "type": 'Natural Essential Oil',
        "mol_w": 138.21, "vapor_pressure_mmhg": 0.08, "sg_pure": 0.93,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '黃瓜水感、濕潤泥土與深邃皮革綠葉的奢華天然原精。', "desc_en": 'Aqueous cucumber, damp earth, and deep leathery green leaf luxury absolute.'
    },
    '67634-00-8': {
        "cas": '67634-00-8', "name_cn": '戊基烯丙基乙醇酸酯 (Allyl Amyl Glycolate)', "name_en": 'Allyl Amyl Glycolate',
        "note": 'Top-Mid', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 186.25, "vapor_pressure_mmhg": 0.085, "sg_pure": 0.942,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '冷冽金屬鳳梨、白松香與海洋空氣感，現代馥奇調核心。', "desc_en": 'Cold metallic pineapple, galbanum, and marine air; modern fougère staple.'
    },
    '39255-32-8': {
        "cas": '39255-32-8', "name_cn": '曼札酯 (Manzanate)', "name_en": 'Manzanate',
        "note": 'Top', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 158.24, "vapor_pressure_mmhg": 0.65, "sg_pure": 0.87,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '清脆青蘋果、鳳梨與洋甘菊果香前調。', "desc_en": 'Crisp green apple, pineapple, and chamomile fruity top note.'
    },
    '88-41-5': {
        "cas": '88-41-5', "name_cn": '綠花酯 (Verdox)', "name_en": 'Verdox',
        "note": 'Top-Mid', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 198.3, "vapor_pressure_mmhg": 0.095, "sg_pure": 0.945,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '清脆青蘋果果皮與木質松針的明亮果香。', "desc_en": 'Crisp green apple skin and woody pine brightness.'
    },
    '34300-94-2': {
        "cas": '34300-94-2', "name_cn": '黑醋栗基劑分子 (Cassis Mercaptan)', "name_en": 'Cassis Mercaptan (8-Mercaptomenthone)',
        "note": 'Top-Mid', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 186.32, "vapor_pressure_mmhg": 0.04, "sg_pure": 0.985,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '鮮嫩黑醋栗芽、葡萄柚與無花果葉的寫實果酸爆發力。', "desc_en": 'Lifelike blackcurrant bud, grapefruit, and fig-leaf tangy burst.'
    },
    '1222-05-5': {
        "cas": '1222-05-5', "name_cn": '佳樂麝香 (Galaxolide)', "name_en": 'Galaxolide',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 258.4, "vapor_pressure_mmhg": 0.00015, "sg_pure": 1.005,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '潔淨蓬鬆的現代白麝香，賦予配方持久貼膚的皂感與圓潤度。', "desc_en": 'Clean, diffusive modern white musk imparting lasting skin-hugging soapy roundness.'
    },
    '111879-80-2': {
        "cas": '111879-80-2', "name_cn": '哈巴諾內酯 (Habanolide)', "name_en": 'Habanolide',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 238.37, "vapor_pressure_mmhg": 0.00018, "sg_pure": 0.962,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '帶有熱熨斗蒸氣與金屬光澤的優雅大環麝香，擴散力極佳。', "desc_en": 'Elegant macrocyclic musk with hot-iron steam and metallic radiance.'
    },
    '106-02-5': {
        "cas": '106-02-5', "name_cn": '環十五內酯 (Exaltolide)', "name_en": 'Exaltolide',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 240.38, "vapor_pressure_mmhg": 0.00011, "sg_pure": 0.955,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '細膩粉嫩、帶有漿果與肌膚體溫感的頂級大環麝香。', "desc_en": 'Delicate, powdery, berry-tinged macrocyclic skin musk.'
    },
    '28645-51-4': {
        "cas": '28645-51-4', "name_cn": '黃葵內酯 (Ambrettolide)', "name_en": 'Ambrettolide',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 252.39, "vapor_pressure_mmhg": 9e-05, "sg_pure": 0.958,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '源自黃葵籽的奢華大環麝香，帶有梨子酒香與柔和粉感。', "desc_en": 'Luxurious ambrette-derived macrocyclic musk with pear-liqueur warmth.'
    },
    '105-95-3': {
        "cas": '105-95-3', "name_cn": '巴西酸乙二酯 (Ethylene Brassylate)', "name_en": 'Ethylene Brassylate',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 270.36, "vapor_pressure_mmhg": 6e-05, "sg_pure": 1.042,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '溫暖香草粉感與甜美花香的大環麝香，性價比極高的定香劑。', "desc_en": 'Warm vanilla-powdery and sweet floral macrocyclic musk fixative.'
    },
    '541-91-3': {
        "cas": '541-91-3', "name_cn": '麝香酮 (L-Muscone)', "name_en": 'Muscone',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 238.41, "vapor_pressure_mmhg": 0.00022, "sg_pure": 0.922,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '天然靈貓與麝香鹿的核心大環酮分子，溫潤感性且極具穿透力。', "desc_en": 'Signature macrocyclic ketone of natural musk; warm, sensual, and diffusive.'
    },
    '82356-51-2': {
        "cas": '82356-51-2', "name_cn": '麝香烯酮 (Muscenone)', "name_en": 'Muscenone',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 236.39, "vapor_pressure_mmhg": 0.00025, "sg_pure": 0.935,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '強效現代感性大環麝香，兼顧粉感優雅與動物張力。', "desc_en": 'Potent modern sensual macrocyclic musk balancing powdery elegance and animalic lift.'
    },
    '141773-73-1': {
        "cas": '141773-73-1', "name_cn": '赫維托內酯 (Helvetolide)', "name_en": 'Helvetolide',
        "note": 'Mid-Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 284.43, "vapor_pressure_mmhg": 0.00038, "sg_pure": 0.925,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '帶有西洋梨果香與黃葵籽氣息的線性麝香，從前調就能聞到。', "desc_en": 'Linear alicyclic musk with pear-fruit and ambrette facets noticeable from the top.'
    },
    '236391-76-7': {
        "cas": '236391-76-7', "name_cn": '羅曼多內酯 (Romandolide)', "name_en": 'Romandolide',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 270.41, "vapor_pressure_mmhg": 0.00032, "sg_pure": 0.938,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '極致潔淨柔滑的白麝香，帶有微甜黑莓與乾淨棉布氣息。', "desc_en": 'Ultra-clean, smooth white musk with subtle blackberry and fresh cotton nuances.'
    },
    '1506-02-1': {
        "cas": '1506-02-1', "name_cn": '吐納麝香 (Tonalide)', "name_en": 'Tonalide',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 258.4, "vapor_pressure_mmhg": 0.00014, "sg_pure": 0.995,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '溫暖粉質與微帶琥珀樹脂感的多環麝香。', "desc_en": 'Warm, powdery, slightly ambery polycyclic musk.'
    },
    '13171-00-1': {
        "cas": '13171-00-1', "name_cn": '薩利麝香 (Celestolide)', "name_en": 'Celestolide',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 244.37, "vapor_pressure_mmhg": 0.0002, "sg_pure": 0.985,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '帶有莓果甜香與潔淨皂感的多環麝香。', "desc_en": 'Berry-sweet, clean soapy polycyclic musk.'
    },
    '542-46-1': {
        "cas": '542-46-1', "name_cn": '靈貓酮 (Civettone)', "name_en": 'Civettone',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 250.42, "vapor_pressure_mmhg": 7e-05, "sg_pure": 0.918,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '絲絨般的動物性暖意，能讓白花與玫瑰綻放出奢華古典光澤。', "desc_en": 'Velvety animalic warmth that gives white florals and roses opulent vintage depth.'
    },
    '106-44-5': {
        "cas": '106-44-5', "name_cn": '對甲酚 (Para-Cresol)', "name_en": 'Para-Cresol',
        "note": 'Mid-Base', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 108.14, "vapor_pressure_mmhg": 0.11, "sg_pure": 1.018,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '依蘭、水仙與皮革調中的關鍵動物性酚類（僅限極微量使用）。', "desc_en": 'Key animalic phenolic note in ylang, narcissus, and leather (use in extreme traces).'
    },
    '8015-62-1': {
        "cas": '8015-62-1', "name_cn": '黃葵籽精油 (Ambrette Seed Oil)', "name_en": 'Ambrette Seed Oil',
        "note": 'Base', "family": 'Sweet', "type": 'Natural Essential Oil',
        "mol_w": 252.39, "vapor_pressure_mmhg": 0.0008, "sg_pure": 0.905,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Farnesol': 0.05},
        "desc_zh": '植物界最珍貴的天然麝香替代品，兼顧白蘭地酒香、堅果與肌膚暖意。', "desc_en": "Botanical world's premier natural musk; cognac, nutty, and skin-warm."
    },
    '97-53-0': {
        "cas": '97-53-0', "name_cn": '丁香酚 (Eugenol)', "name_en": 'Eugenol',
        "note": 'Mid-Base', "family": 'Spicy', "type": 'Aroma Chemical',
        "mol_w": 164.2, "vapor_pressure_mmhg": 0.022, "sg_pure": 1.067,
        "ifra_cat4_max": 2.5, "eu_banned": False, "baseline_allergens": {'Eugenol': 1.0},
        "desc_zh": '溫暖辛辣的丁香花蕾與康乃馨花香核心（IFRA 限值 2.5%）。', "desc_en": 'Warm, spicy clove bud and carnation floral heart (IFRA limit 2.5%).'
    },
    '97-54-1': {
        "cas": '97-54-1', "name_cn": '異丁香酚 (Isoeugenol)', "name_en": 'Isoeugenol',
        "note": 'Mid-Base', "family": 'Spicy', "type": 'Aroma Chemical',
        "mol_w": 164.2, "vapor_pressure_mmhg": 0.012, "sg_pure": 1.08,
        "ifra_cat4_max": 0.11, "eu_banned": False, "baseline_allergens": {'Isoeugenol': 1.0},
        "desc_zh": '細膩粉質康乃馨與菸草辛香（IFRA 嚴格限量 0.11%！）。', "desc_en": 'Delicate powdery carnation and spicy tobacco note (Strict IFRA limit 0.11%!).'
    },
    '104-55-2': {
        "cas": '104-55-2', "name_cn": '肉桂醛 (Cinnamaldehyde)', "name_en": 'Cinnamal',
        "note": 'Mid', "family": 'Spicy', "type": 'Aroma Chemical',
        "mol_w": 132.16, "vapor_pressure_mmhg": 0.029, "sg_pure": 1.05,
        "ifra_cat4_max": 0.05, "eu_banned": False, "baseline_allergens": {'Cinnamal': 1.0},
        "desc_zh": '熾熱甜辣的肉桂皮核心單體（IFRA 嚴格限量 0.05%！）。', "desc_en": 'Fiery, sweet-spicy cinnamon bark monomer (Strict IFRA limit 0.05%!).'
    },
    '104-54-1': {
        "cas": '104-54-1', "name_cn": '肉桂醇 (Cinnamyl Alcohol)', "name_en": 'Cinnamyl Alcohol',
        "note": 'Mid-Base', "family": 'Spicy', "type": 'Aroma Chemical',
        "mol_w": 134.18, "vapor_pressure_mmhg": 0.006, "sg_pure": 1.044,
        "ifra_cat4_max": 0.8, "eu_banned": False, "baseline_allergens": {'Cinnamyl Alcohol': 1.0},
        "desc_zh": '溫潤微甜的風信子與肉桂樹脂花香（IFRA 限值 0.8%）。', "desc_en": 'Warm, mildly sweet hyacinth and cinnamon-balsamic floral (IFRA limit 0.8%).'
    },
    '8000-66-6': {
        "cas": '8000-66-6', "name_cn": '綠豆蔻精油 (Cardamom Oil)', "name_en": 'Cardamom Oil',
        "note": 'Top-Mid', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 196.29, "vapor_pressure_mmhg": 0.32, "sg_pure": 0.928,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.04, 'Linalool': 0.05},
        "desc_zh": '清涼桉油醇與溫暖辛香交織的頂級香料，賦予木質與茶香高級感。', "desc_en": 'Cooling cineole intertwined with warm spice; elevates woody and tea accords.'
    },
    '8006-82-4': {
        "cas": '8006-82-4', "name_cn": '黑胡椒 (Black Pepper)', "name_en": 'Black Pepper Oil',
        "note": 'Top', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 204.35, "vapor_pressure_mmhg": 0.45, "sg_pure": 0.875,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.18, 'Linalool': 0.01},
        "desc_zh": '乾燥微辛的木質胡椒粒氣息，給予前調躍動的立體能量。', "desc_en": 'Dry, sparkling woody-spicy peppercorn note that energizes top structures.'
    },
    '949495-68-5': {
        "cas": '949495-68-5', "name_cn": '粉紅胡椒 CO2 (Pink Pepper CO2)', "name_en": 'Pink Pepper CO2 Extract',
        "note": 'Top', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 0.78, "sg_pure": 0.862,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.25},
        "desc_zh": '清脆果香、微帶玫瑰與杜松子辛香的現代氣泡前調。', "desc_en": 'Crisp, fruity-rosy and juniper-spiced modern sparkling top note.'
    },
    '8008-45-5': {
        "cas": '8008-45-5', "name_cn": '肉豆蔻精油 (Nutmeg Oil)', "name_en": 'Nutmeg Oil',
        "note": 'Top-Mid', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 0.41, "sg_pure": 0.895,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.05, 'Isoeugenol': 0.005},
        "desc_zh": '溫暖粉質的木質香料氣息，兼具胡椒活力與甜美樹脂韻味。', "desc_en": 'Warm, powdery woody spice bridging peppery lift and sweet balsamic depth.'
    },
    '8000-34-8': {
        "cas": '8000-34-8', "name_cn": '丁香花苞精油 (Clove Bud Oil)', "name_en": 'Clove Bud Oil',
        "note": 'Mid-Base', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 164.2, "vapor_pressure_mmhg": 0.025, "sg_pure": 1.048,
        "ifra_cat4_max": 3.0, "eu_banned": False, "baseline_allergens": {'Eugenol': 0.82, 'Isoeugenol': 0.005},
        "desc_zh": '濃郁暖甜的丁香香料，賦予東方調與康乃馨花香厚實骨架。', "desc_en": 'Rich, warm-sweet clove spice anchoring oriental and carnation accords.'
    },
    '8015-91-6': {
        "cas": '8015-91-6', "name_cn": '錫蘭肉桂皮精油 (Cinnamon Bark Oil)', "name_en": 'Cinnamon Bark Oil',
        "note": 'Mid', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 132.16, "vapor_pressure_mmhg": 0.035, "sg_pure": 1.02,
        "ifra_cat4_max": 0.08, "eu_banned": False, "baseline_allergens": {'Cinnamal': 0.65, 'Eugenol': 0.05},
        "desc_zh": '高含量肉桂醛的熾熱木質辛香（IFRA 嚴格限量 0.08%）。', "desc_en": 'Fiery woody spice rich in cinnamaldehyde (Strict IFRA limit 0.08%).'
    },
    '8007-08-7': {
        "cas": '8007-08-7', "name_cn": '鮮薑 CO2 萃取 (Ginger CO2)', "name_en": 'Ginger Root CO2 Extract',
        "note": 'Top-Mid', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 204.35, "vapor_pressure_mmhg": 0.28, "sg_pure": 0.882,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Citral': 0.02, 'Limonene': 0.04},
        "desc_zh": '超臨界 CO2 萃取，完整保留鮮薑檸檬辛辣穿透力與溫暖根莖感。', "desc_en": 'Supercritical CO2 extract capturing zesty fresh ginger bite and warm root depth.'
    },
    '8008-52-4': {
        "cas": '8008-52-4', "name_cn": '芫荽籽精油 (Coriander Seed Oil)', "name_en": 'Coriander Seed Oil',
        "note": 'Top-Mid', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 154.25, "vapor_pressure_mmhg": 0.24, "sg_pure": 0.87,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Linalool': 0.72, 'Limonene': 0.03},
        "desc_zh": '富含天然沉香醇，帶有甜橙皮、胡椒與溫暖木質的香料前中調。', "desc_en": 'Rich in natural linalool; sweet orange peel, pepper, and warm woody spice.'
    },
    '8006-90-4': {
        "cas": '8006-90-4', "name_cn": '歐薄荷 (Peppermint)', "name_en": 'Peppermint Oil',
        "note": 'Top', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 156.27, "vapor_pressure_mmhg": 0.85, "sg_pure": 0.898,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.03, 'Linalool': 0.01},
        "desc_zh": '強烈清涼薄荷腦穿透力，瞬間醒腦提神。', "desc_en": 'Crisp, penetrating menthol freshness that awakens top notes.'
    },
    '8008-79-5': {
        "cas": '8008-79-5', "name_cn": '綠薄荷 (Spearmint Oil)', "name_en": 'Spearmint Oil',
        "note": 'Top', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 150.22, "vapor_pressure_mmhg": 0.62, "sg_pure": 0.925,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.15},
        "desc_zh": '富含香芹酮，比歐薄荷更清甜草本、帶有茶香與青綠葉片感。', "desc_en": 'Carvone-rich mint; sweeter, more herbaceous, and tea-like than peppermint.'
    },
    '2216-51-5': {
        "cas": '2216-51-5', "name_cn": '左旋薄荷腦 (L-Menthol)', "name_en": 'L-Menthol',
        "note": 'Top', "family": 'Spicy', "type": 'Aroma Chemical',
        "mol_w": 156.27, "vapor_pressure_mmhg": 0.064, "sg_pure": 0.89,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '純淨冰涼結晶分子，賦予皮膚真實清涼觸感與極致通透前調。', "desc_en": 'Pure cooling crystalline molecule imparting tactile skin chill and crisp lift.'
    },
    '470-82-6': {
        "cas": '470-82-6', "name_cn": '1,8-桉油醇 (Eucalyptol)', "name_en": 'Eucalyptol (1,8-Cineole)',
        "note": 'Top', "family": 'Spicy', "type": 'Aroma Chemical',
        "mol_w": 154.25, "vapor_pressure_mmhg": 1.9, "sg_pure": 0.922,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '尤加利、羅溫莎葉與迷迭香的清涼樟腦氧化物核心。', "desc_en": 'Crisp camphoraceous oxide core of eucalyptus, ravintsara, and rosemary.'
    },
    '8000-48-4': {
        "cas": '8000-48-4', "name_cn": '澳洲尤加利 (Eucalyptus Radiata)', "name_en": 'Eucalyptus Radiata Oil',
        "note": 'Top', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 154.25, "vapor_pressure_mmhg": 1.9, "sg_pure": 0.91,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.06, 'Citral': 0.01},
        "desc_zh": '清澈微甜的澳洲森林氣息，呼吸感極佳且不嗆鼻。', "desc_en": 'Crisp, slightly sweet Australian forest air; smooth and non-harsh.'
    },
    '92201-50-8': {
        "cas": '92201-50-8', "name_cn": '羅溫莎葉 (Ravintsara)', "name_en": 'Ravintsara Oil',
        "note": 'Top', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 154.25, "vapor_pressure_mmhg": 1.85, "sg_pure": 0.9,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.03, 'Linalool': 0.01},
        "desc_zh": '高含量 1,8-桉油醇，帶來通透潔淨的森林空氣感。', "desc_en": 'Rich in 1,8-cineole; crisp, breathable camphoraceous forest air.'
    },
    '8014-68-4': {
        "cas": '8014-68-4', "name_cn": '綠花白千層 (Niaouli)', "name_en": 'Niaouli Oil',
        "note": 'Top', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 154.25, "vapor_pressure_mmhg": 1.75, "sg_pure": 0.91,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.08, 'Linalool': 0.01},
        "desc_zh": '比茶樹溫和且帶有微甜花果尾韻的氧化物清新。', "desc_en": 'Softer than tea tree; clean 1,8-cineole freshness with a subtly sweet fruity-floral undertone.'
    },
    '68647-73-4': {
        "cas": '68647-73-4', "name_cn": '茶樹 (Tea Tree)', "name_en": 'Tea Tree Oil',
        "note": 'Top', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 154.25, "vapor_pressure_mmhg": 1.4, "sg_pure": 0.9,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.03, 'Linalool': 0.01},
        "desc_zh": '純淨潔癖般的草本藥草氣息，賦予現代潔淨調真實感。', "desc_en": 'Crisp, medicinal herbal clarity lending authentic cleanliness to modern accords.'
    },
    '8000-25-7': {
        "cas": '8000-25-7', "name_cn": '桉油醇迷迭香 (Rosemary Cineole)', "name_en": 'Rosemary Cineole Oil',
        "note": 'Top', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 154.25, "vapor_pressure_mmhg": 1.62, "sg_pure": 0.905,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.04, 'Linalool': 0.02},
        "desc_zh": '強烈草本清涼穿透力，提升專注力，馥奇調核心。', "desc_en": 'Penetrating, cooling herbal clarity; classic aromatic fougère top note.'
    },
    '8016-63-5': {
        "cas": '8016-63-5', "name_cn": '快樂鼠尾草 (Clary Sage)', "name_en": 'Clary Sage Oil',
        "note": 'Mid', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 196.29, "vapor_pressure_mmhg": 0.075, "sg_pure": 0.89,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Linalool': 0.22, 'Geraniol': 0.02},
        "desc_zh": '堅果草本、微醺茶香與琥珀龍涎氣息交織，深層鎮靜。', "desc_en": 'Nutty, tea-like herbaceous heart with ambery-musk undertones.'
    },
    '8007-46-3': {
        "cas": '8007-46-3', "name_cn": '白百里香精油 (Thyme White Oil)', "name_en": 'Thyme White Oil',
        "note": 'Top-Mid', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 150.22, "vapor_pressure_mmhg": 0.35, "sg_pure": 0.915,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Linalool': 0.05, 'Limonene': 0.03},
        "desc_zh": '溫暖乾燥的地中海藥草辛香，富含百里酚與傘花烴。', "desc_en": 'Warm, dry Mediterranean herbal spice rich in thymol and p-cymene.'
    },
    '8015-73-4': {
        "cas": '8015-73-4', "name_cn": '沉香醇羅勒 (Basil Linalool)', "name_en": 'Basil Linalool Oil',
        "note": 'Top-Mid', "family": 'Spicy', "type": 'Natural Essential Oil',
        "mol_w": 154.25, "vapor_pressure_mmhg": 0.22, "sg_pure": 0.89,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Linalool': 0.55, 'Eugenol': 0.02},
        "desc_zh": '清甜綠葉、八角茴香與花香沉香醇交織的草本精油。', "desc_en": 'Sweet green leaf, anise, and floral linalool herbaceous oil.'
    },
    '8002-68-4': {
        "cas": '8002-68-4', "name_cn": '杜松子 (Juniper Berry)', "name_en": 'Juniper Berry Oil',
        "note": 'Top-Mid', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 136.24, "vapor_pressure_mmhg": 0.92, "sg_pure": 0.865,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Limonene': 0.05},
        "desc_zh": '琴酒般清脆冷冽的松柏果實木質，帶來通透的空氣感。', "desc_en": 'Crisp, gin-like coniferous berry woodiness imparting clean vertical lift.'
    },
    '28940-11-6': {
        "cas": '28940-11-6', "name_cn": '西瓜酮 / 海洋酮 (Calone 1951)', "name_en": 'Calone 1951',
        "note": 'Mid', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 178.23, "vapor_pressure_mmhg": 0.015, "sg_pure": 1.08,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '90年代水生海洋調的傳奇分子，帶有海風鹽味與西瓜清甜。', "desc_en": 'Legendary 90s marine molecule with sea-breeze salinity and watery melon.'
    },
    '67634-15-5': {
        "cas": '67634-15-5', "name_cn": '花青臭氧醛 (Floralozone)', "name_en": 'Floralozone',
        "note": 'Top-Mid', "family": 'Floral', "type": 'Aroma Chemical',
        "mol_w": 190.28, "vapor_pressure_mmhg": 0.019, "sg_pure": 0.945,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '潔淨海風、臭氧空氣與水感白花的現代清新分子。', "desc_en": 'Clean ocean breeze, ozonic air, and watery white-floral modern molecule.'
    },
    '106-72-9': {
        "cas": '106-72-9', "name_cn": '甜瓜醛 (Melonal)', "name_en": 'Melonal',
        "note": 'Top', "family": 'Citrus', "type": 'Aroma Chemical',
        "mol_w": 140.22, "vapor_pressure_mmhg": 0.42, "sg_pure": 0.848,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '鮮切哈密瓜、小黃瓜與水感前調分子。', "desc_en": 'Freshly sliced cantaloupe, cucumber, and aqueous top-note molecule.'
    },
    '90028-68-5': {
        "cas": '90028-68-5', "name_cn": '低阿特蘭醇橡木苔 (Oakmoss Abs. Low-Atranol)', "name_en": 'Oakmoss Absolute (IFRA Compliant)',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 220.0, "vapor_pressure_mmhg": 0.0005, "sg_pure": 1.02,
        "ifra_cat4_max": 0.1, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '經分子處理去除致敏酚類的合規橡木苔，深邃森林苔蘚西普靈魂（IFRA 限值 0.1%）。', "desc_en": 'IFRA-compliant de-atranolized oakmoss; deep forest moss chypre soul (Limit 0.1%).'
    },
    '121-33-5': {
        "cas": '121-33-5', "name_cn": '香草醛 (Vanillin)', "name_en": 'Vanillin',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 152.15, "vapor_pressure_mmhg": 0.00012, "sg_pure": 1.056,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '天然香草莢的核心結晶分子，溫暖乳脂甜香與東方調支柱。', "desc_en": 'Signature crystalline molecule of vanilla pods; warm creamy sweetness.'
    },
    '121-32-4': {
        "cas": '121-32-4', "name_cn": '乙基香草醛 (Ethyl Vanillin)', "name_en": 'Ethyl Vanillin',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 166.17, "vapor_pressure_mmhg": 8e-05, "sg_pure": 1.045,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '強度為香草醛 3 倍的濃郁巧克力與卡士達香草結晶。', "desc_en": 'Three times stronger than vanillin; rich chocolate-custard vanilla warmth.'
    },
    '91-64-5': {
        "cas": '91-64-5', "name_cn": '香豆素 (Coumarin)', "name_en": 'Coumarin',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 146.14, "vapor_pressure_mmhg": 0.00098, "sg_pure": 0.935,
        "ifra_cat4_max": 1.6, "eu_banned": False, "baseline_allergens": {'Coumarin': 1.0},
        "desc_zh": '零陵香豆的核心結晶，剛曬乾的乾草、杏仁與香草粉感（IFRA 限值 1.6%）。', "desc_en": 'Signature crystalline lactone of tonka bean; sun-dried hay and almond powder (Limit 1.6%).'
    },
    '4940-11-8': {
        "cas": '4940-11-8', "name_cn": '乙基麥芽酚 (Ethyl Maltol)', "name_en": 'Ethyl Maltol',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 140.14, "vapor_pressure_mmhg": 0.0012, "sg_pure": 1.15,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '焦糖棉花糖與烤草莓果醬的現代美食調核心分子。', "desc_en": 'Caramelized cotton candy and spun-sugar modern gourmand cornerstone.'
    },
    '118-71-8': {
        "cas": '118-71-8', "name_cn": '麥芽酚 (Maltol)', "name_en": 'Maltol',
        "note": 'Mid-Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 126.11, "vapor_pressure_mmhg": 0.0025, "sg_pure": 1.18,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '剛出爐的焦糖餅乾與烘焙麵包甜香。', "desc_en": 'Freshly baked caramel biscuit and toasted sweetness.'
    },
    '9000-05-9': {
        "cas": '9000-05-9', "name_cn": '安息香原精 (Benzoin Resinoid)', "name_en": 'Benzoin Resinoid',
        "note": 'Base', "family": 'Sweet', "type": 'Natural Essential Oil',
        "mol_w": 212.24, "vapor_pressure_mmhg": 5e-05, "sg_pure": 1.15,
        "ifra_cat4_max": 2.0, "eu_banned": False, "baseline_allergens": {'Benzyl Benzoate': 0.15, 'Cinnamal': 0.01},
        "desc_zh": '濃稠溫潤的香草焦糖樹脂香（高蠟質，強烈建議以 TEC 預溶）。', "desc_en": 'Viscous, comforting vanilla-caramel resin (high wax; pre-dissolve in TEC).'
    },
    '120-51-4': {
        "cas": '120-51-4', "name_cn": '苯甲酸苄酯 (Benzyl Benzoate)', "name_en": 'Benzyl Benzoate',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 212.24, "vapor_pressure_mmhg": 0.00022, "sg_pure": 1.118,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Benzyl Benzoate': 1.0},
        "desc_zh": '微帶樹脂花香的無色定香溶劑，能有效延緩高揮發香料散逸。', "desc_en": 'Faintly balsamic fixative solvent that slows evaporation of volatile top notes.'
    },
    '8046-22-8': {
        "cas": '8046-22-8', "name_cn": '零陵香豆原精 (Tonka Bean Absolute)', "name_en": 'Tonka Bean Absolute',
        "note": 'Base', "family": 'Sweet', "type": 'Natural Essential Oil',
        "mol_w": 146.14, "vapor_pressure_mmhg": 0.0006, "sg_pure": 1.08,
        "ifra_cat4_max": 1.8, "eu_banned": False, "baseline_allergens": {'Coumarin': 0.45},
        "desc_zh": '富含天然香豆素，兼顧焦糖杏仁、菸草與溫暖木質的奢華底蘊。', "desc_en": 'Rich in natural coumarin; caramel almond, tobacco, and warm woody luxury.'
    },
    '8016-26-0': {
        "cas": '8016-26-0', "name_cn": '岩薔薇 / 勞丹脂原精 (Labdanum Absolute)', "name_en": 'Labdanum Absolute',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 222.37, "vapor_pressure_mmhg": 0.0003, "sg_pure": 1.04,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '琥珀調的天然靈魂，深沉皮革、蜂蜜樹脂與龍涎香般的動物暖意。', "desc_en": 'Natural soul of amber accords; deep leather, honeyed resin, and ambergris warmth.'
    },
    '8007-00-9': {
        "cas": '8007-00-9', "name_cn": '秘魯香脂精油 (Peru Balsam Oil)', "name_en": 'Peru Balsam Oil',
        "note": 'Base', "family": 'Sweet', "type": 'Natural Essential Oil',
        "mol_w": 212.24, "vapor_pressure_mmhg": 0.00015, "sg_pure": 1.11,
        "ifra_cat4_max": 0.4, "eu_banned": False, "baseline_allergens": {'Benzyl Benzoate': 0.55, 'Benzyl Cinnamate': 0.25, 'Cinnamal': 0.01},
        "desc_zh": '濃郁香草、肉桂與深色焦糖樹脂香（IFRA 嚴格限量 0.4%！）。', "desc_en": 'Rich vanilla, cinnamon, and dark caramel resin (Strict IFRA limit 0.4%!).'
    },
    '9000-64-0': {
        "cas": '9000-64-0', "name_cn": '吐魯香脂 (Tolu Balsam Resinoid)', "name_en": 'Tolu Balsam Resinoid',
        "note": 'Base', "family": 'Sweet', "type": 'Natural Essential Oil',
        "mol_w": 212.24, "vapor_pressure_mmhg": 0.00018, "sg_pure": 1.12,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {'Benzyl Benzoate': 0.12, 'Cinnamal': 0.02},
        "desc_zh": '帶有風信子花香與肉桂香草氣息的溫潤南美樹脂。', "desc_en": 'Warm South American resin with hyacinth floral and cinnamon-vanilla facets.'
    },
    '8046-19-3': {
        "cas": '8046-19-3', "name_cn": '蘇合香樹脂 (Styrax Resinoid)', "name_en": 'Styrax Resinoid',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 134.18, "vapor_pressure_mmhg": 0.0008, "sg_pure": 1.09,
        "ifra_cat4_max": 0.6, "eu_banned": False, "baseline_allergens": {'Cinnamyl Alcohol': 0.08},
        "desc_zh": '帶有皮革、肉桂花香與微煙燻感的古老定香樹脂（IFRA 限值 0.6%）。', "desc_en": 'Ancient leathery, cinnamic-floral, slightly smoky fixative resin (IFRA limit 0.6%).'
    },
    '5471-51-2': {
        "cas": '5471-51-2', "name_cn": '覆盆子酮 (Raspberry Ketone)', "name_en": 'Raspberry Ketone',
        "note": 'Mid-Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 164.2, "vapor_pressure_mmhg": 0.00035, "sg_pure": 1.05,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '成熟覆盆子果醬與粉感紫羅蘭的甜美結晶分子。', "desc_en": 'Ripe raspberry jam and powdery violet sweet crystalline molecule.'
    },
    '28664-35-9': {
        "cas": '28664-35-9', "name_cn": '葫蘆巴內酯 (Sotolon)', "name_en": 'Sotolon',
        "note": 'Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 128.13, "vapor_pressure_mmhg": 0.0018, "sg_pure": 1.12,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '極強力的楓糖漿、烤核桃與焦糖咖哩草本分子（僅限極微量使用）。', "desc_en": 'Ultra-potent maple syrup, roasted walnut, and fenugreek molecule (trace use only).'
    },
    '80-71-7': {
        "cas": '80-71-7', "name_cn": '甲基環戊烯醇酮 (Maple Lactone / Cyclotene)', "name_en": 'Methyl Cyclopentenolone',
        "note": 'Mid-Base', "family": 'Sweet', "type": 'Aroma Chemical',
        "mol_w": 112.13, "vapor_pressure_mmhg": 0.0042, "sg_pure": 1.14,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '焦糖咖啡、楓糖與烘焙堅果的美食調單體。', "desc_en": 'Caramel coffee, maple, and roasted hazelnut gourmand monomer.'
    },
    '65442-31-1': {
        "cas": '65442-31-1', "name_cn": '異丁基喹啉 (Isobutyl Quinoline)', "name_en": 'Isobutyl Quinoline',
        "note": 'Mid-Base', "family": 'Woody', "type": 'Aroma Chemical',
        "mol_w": 185.27, "vapor_pressure_mmhg": 0.0045, "sg_pure": 0.996,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '乾燥銳利的綠色皮革、岩蘭草根與橡木苔靈魂單體。', "desc_en": 'Dry, sharp green leather, vetiver root, and oakmoss signature molecule.'
    },
    '8001-88-5': {
        "cas": '8001-88-5', "name_cn": '精餾樺木焦油 (Birch Tar Rectified)', "name_en": 'Birch Tar Oil Rectified',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 150.22, "vapor_pressure_mmhg": 0.012, "sg_pure": 0.945,
        "ifra_cat4_max": 0.1, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '篝火煙燻、俄羅斯皮革與炭烤木質氣息（需精餾去除多環芳烴，限值 0.1%）。', "desc_en": 'Campfire smoke, Russian leather, and charred wood (PAH-rectified; IFRA limit 0.1%).'
    },
    '8013-10-3': {
        "cas": '8013-10-3', "name_cn": '精餾杜松焦油 (Cade Oil Rectified)', "name_en": 'Cade Oil Rectified',
        "note": 'Base', "family": 'Woody', "type": 'Natural Essential Oil',
        "mol_w": 204.35, "vapor_pressure_mmhg": 0.015, "sg_pure": 0.955,
        "ifra_cat4_max": 0.1, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '乾燥煙燻杜松木與煙草皮革氣息（IFRA 限值 0.1%）。', "desc_en": 'Dry smoky juniper wood and tobacco leather aroma (IFRA limit 0.1%).'
    },
    '116-26-7': {
        "cas": '116-26-7', "name_cn": '番紅花醛 (Safranal)', "name_en": 'Safranal',
        "note": 'Top-Mid', "family": 'Spicy', "type": 'Aroma Chemical',
        "mol_w": 150.22, "vapor_pressure_mmhg": 0.085, "sg_pure": 0.973,
        "ifra_cat4_max": 0.005, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '天然藏紅花的乾燥藥草、皮革與金屬辛香（IFRA 極嚴格限量 0.005%！）。', "desc_en": 'Dry medicinal, leathery, metallic saffron spice (Strict IFRA limit 0.005%!).'
    },
    '54440-17-4': {
        "cas": '54440-17-4', "name_cn": '藏紅花醚 (Safraleine)', "name_en": 'Safraleine',
        "note": 'Mid-Base', "family": 'Spicy', "type": 'Aroma Chemical',
        "mol_w": 186.25, "vapor_pressure_mmhg": 0.014, "sg_pure": 0.988,
        "ifra_cat4_max": 100.0, "eu_banned": False, "baseline_allergens": {},
        "desc_zh": '融合藏紅花、乾燥菸草與絨面皮革的現代安全替代分子。', "desc_en": 'Modern safe molecule blending saffron, dry tobacco, and suede leather.'
    },
    '80-54-6': {
        "cas": '80-54-6', "name_cn": '🚨 [EU禁用] 百合醛 (Lilial / BMHCA)', "name_en": '[EU BANNED] Lilial (BMHCA)',
        "note": 'Mid', "family": 'Floral', "type": 'EU Prohibited Substance',
        "mol_w": 204.31, "vapor_pressure_mmhg": 0.0042, "sg_pure": 0.946,
        "ifra_cat4_max": 0.0, "eu_banned": True, "baseline_allergens": {},
        "desc_zh": '⛔ 歐盟 EC 1223/2009 附錄二全面禁用物質（生殖毒性 CMR 1B），嚴禁於歐盟及多國市場販售！', "desc_en": '⛔ BANNED under EU Cosmetics Regulation Annex II (CMR 1B). Strictly prohibited in finished products!'
    },
    '31906-04-4': {
        "cas": '31906-04-4', "name_cn": '🚨 [EU禁用] 新鈴蘭醛 (Lyral / HICC)', "name_en": '[EU BANNED] Lyral (HICC)',
        "note": 'Mid', "family": 'Floral', "type": 'EU Prohibited Substance',
        "mol_w": 210.31, "vapor_pressure_mmhg": 0.0006, "sg_pure": 0.992,
        "ifra_cat4_max": 0.0, "eu_banned": True, "baseline_allergens": {},
        "desc_zh": '⛔ 歐盟 EC 1223/2009 全面禁用物質（極高接觸性致敏原），請改用 Majantol 或 Florhydral。', "desc_en": '⛔ BANNED under EU Cosmetics Regulation Annex II (potent contact allergen). Replace with Majantol.'
    },
    '526-37-4': {
        "cas": '526-37-4', "name_cn": '🚨 [EU禁用] 阿特蘭醇 (Atranol)', "name_en": '[EU BANNED] Atranol',
        "note": 'Base', "family": 'Woody', "type": 'EU Prohibited Substance',
        "mol_w": 152.15, "vapor_pressure_mmhg": 0.001, "sg_pure": 1.15,
        "ifra_cat4_max": 0.0, "eu_banned": True, "baseline_allergens": {},
        "desc_zh": '⛔ 橡木苔中的高致敏酚類單體，歐盟法規全面禁止檢出（0.0% 容許值）。', "desc_en": '⛔ Potent oakmoss sensitizer strictly BANNED under EU Cosmetics Regulation Annex II (0.0% limit).'
    },
    '57074-21-2': {
        "cas": '57074-21-2', "name_cn": '🚨 [EU禁用] 氯阿特蘭醇 (Chloroatranol)', "name_en": '[EU BANNED] Chloroatranol',
        "note": 'Base', "family": 'Woody', "type": 'EU Prohibited Substance',
        "mol_w": 186.59, "vapor_pressure_mmhg": 0.0008, "sg_pure": 1.22,
        "ifra_cat4_max": 0.0, "eu_banned": True, "baseline_allergens": {},
        "desc_zh": '⛔ 橡木苔中的氯化致敏酚類單體，歐盟法規全面禁止檢出（0.0% 容許值）。', "desc_en": '⛔ Chlorinated oakmoss sensitizer strictly BANNED under EU Cosmetics Regulation Annex II (0.0% limit).'
    },
    '83-66-9': {
        "cas": '83-66-9', "name_cn": '🚨 [EU/IFRA禁用] 葵子麝香 (Musk Ambrette)', "name_en": '[BANNED] Musk Ambrette',
        "note": 'Base', "family": 'Sweet', "type": 'EU Prohibited Substance',
        "mol_w": 268.27, "vapor_pressure_mmhg": 5e-05, "sg_pure": 1.18,
        "ifra_cat4_max": 0.0, "eu_banned": True, "baseline_allergens": {},
        "desc_zh": '⛔ 具備神經毒性與光毒性，已遭歐盟與 IFRA 全球全面禁止使用。', "desc_en": '⛔ Neurotoxic and phototoxic nitro-musk; globally BANNED by both EU Annex II and IFRA.'
    },
    '81-15-2': {
        "cas": '81-15-2', "name_cn": '🚨 [EU禁用] 二甲苯麝香 (Musk Xylol)', "name_en": '[EU BANNED] Musk Xylol',
        "note": 'Base', "family": 'Sweet', "type": 'EU Prohibited Substance',
        "mol_w": 297.26, "vapor_pressure_mmhg": 3e-05, "sg_pure": 1.21,
        "ifra_cat4_max": 0.0, "eu_banned": True, "baseline_allergens": {},
        "desc_zh": '⛔ 歐盟 REACH 高關注度持久性生物累積物質（vPvB），禁止於化粧品中使用。', "desc_en": '⛔ EU REACH SVHC (vPvB) nitro-musk; prohibited in EU cosmetic formulations.'
    },
    '94-59-7': {
        "cas": '94-59-7', "name_cn": '🚨 [EU/IFRA禁用] 黃樟素 (Safrole)', "name_en": '[BANNED] Safrole',
        "note": 'Mid', "family": 'Spicy', "type": 'EU Prohibited Substance',
        "mol_w": 162.19, "vapor_pressure_mmhg": 0.062, "sg_pure": 1.096,
        "ifra_cat4_max": 0.0, "eu_banned": True, "baseline_allergens": {},
        "desc_zh": '⛔ 具有致癌風險，歐盟法規與 IFRA 標準嚴格禁止作為香精原料添加。', "desc_en": '⛔ Carcinogenic phenylpropene strictly BANNED under EU Annex II and IFRA Standards.'
    },
    '8023-88-9': {
        "cas": '8023-88-9', "name_cn": '🚨 [EU/IFRA禁用] 木香根精油 (Costus Root Oil)', "name_en": '[BANNED] Costus Root Oil',
        "note": 'Base', "family": 'Woody', "type": 'EU Prohibited Substance',
        "mol_w": 232.32, "vapor_pressure_mmhg": 0.0012, "sg_pure": 0.995,
        "ifra_cat4_max": 0.0, "eu_banned": True, "baseline_allergens": {},
        "desc_zh": '⛔ 極強皮膚致敏原，歐盟法規與 IFRA 標準全面禁止使用。', "desc_en": '⛔ Severe dermal sensitizer strictly BANNED under EU Annex II and IFRA Standards.'
    },
    '8024-12-2': {
        "cas": '8024-12-2', "name_cn": '🚨 [EU/IFRA禁用] 天然馬鞭草精油 (Verbena Oil)', "name_en": '[BANNED] Verbena Essential Oil',
        "note": 'Top', "family": 'Citrus', "type": 'EU Prohibited Substance',
        "mol_w": 152.24, "vapor_pressure_mmhg": 0.45, "sg_pure": 0.895,
        "ifra_cat4_max": 0.0, "eu_banned": True, "baseline_allergens": {},
        "desc_zh": '⛔ 具備強烈光敏與致敏風險，歐盟法規禁止於駐留型香水中使用（僅限使用合規無光敏原精）。', "desc_en": '⛔ Potent phototoxic/sensitizing oil BANNED in leave-on fragrances under EU Annex II.'
    },
    '68916-52-9': {
        "cas": '68916-52-9', "name_cn": '🚨 [EU/IFRA禁用] 無花果葉原精 (Fig Leaf Absolute)', "name_en": '[BANNED] Fig Leaf Absolute',
        "note": 'Mid', "family": 'Citrus', "type": 'EU Prohibited Substance',
        "mol_w": 186.16, "vapor_pressure_mmhg": 0.015, "sg_pure": 0.96,
        "ifra_cat4_max": 0.0, "eu_banned": True, "baseline_allergens": {},
        "desc_zh": '⛔ 含有高濃度補骨脂素光毒成分，歐盟與 IFRA 全面禁止使用（請改用 Stemone 或 Triplal 調配無花果調）。', "desc_en": '⛔ High psoralen phototoxicity; BANNED by EU & IFRA. Reconstruct fig notes with Stemone/Triplal.'
    },
}

DEFAULT_COMMERCIAL_SKUS = {
    "SKU-CHEM-54464-50": {
        "sku_id": "SKU-CHEM-54464-50", "cas": "54464-57-2",
        "trade_name_cn": "龍涎酮 50% in DPG (實驗室預溶)", "trade_name_en": "Iso E Super 50% in DPG (Lab Pre-diluted)",
        "supplier_zh": "單體庫 / IFF 規格", "supplier_en": "Aroma Chem Lab (IFF Spec)",
        "lot_no": "LOT-IES-2601", "exp_date": "2029/12/31",
        "dilution_pct": 50.0, "solvent": "DPG (二丙二醇)", "sg": 0.993, "cost_per_g": 3.5,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {}
    },
    "SKU-CHEM-24851-50": {
        "sku_id": "SKU-CHEM-24851-50", "cas": "24851-98-7",
        "trade_name_cn": "Hedione 50% in DPG (Firmenich 規格)", "trade_name_en": "Hedione 50% in DPG (Firmenich Spec)",
        "supplier_zh": "單體庫 / Firmenich 規格", "supplier_en": "Aroma Chem Lab (Firmenich Spec)",
        "lot_no": "LOT-HED-2602", "exp_date": "2029/12/31",
        "dilution_pct": 50.0, "solvent": "DPG (二丙二醇)", "sg": 1.012, "cost_per_g": 4.2,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {}
    },
    "SKU-GIV-6790-100": {
        "sku_id": "SKU-GIV-6790-100", "cas": "6790-58-5",
        "trade_name_cn": "Givaudan Ambroxan 100% 純結晶粉末", "trade_name_en": "Givaudan Ambroxan 100% Crystalline Powder",
        "supplier_zh": "Givaudan 奇華頓", "supplier_en": "Givaudan",
        "lot_no": "GIV-AMB-9921", "exp_date": "2030/06/30",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.980, "cost_per_g": 18.0,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {}
    },
    "SKU-LAB-6790-10": {
        "sku_id": "SKU-LAB-6790-10", "cas": "6790-58-5",
        "trade_name_cn": "Ambroxan 10% in DPG (調香室預溶液)", "trade_name_en": "Ambroxan 10% in DPG (Lab Tincture)",
        "supplier_zh": "單體庫 (預溶規格)", "supplier_en": "Aroma Chem Lab (Pre-dissolved)",
        "lot_no": "LAB-AMB-10A", "exp_date": "2028/12/31",
        "dilution_pct": 10.0, "solvent": "DPG (二丙二醇)", "sg": 1.019, "cost_per_g": 18.0,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {}
    },
    "SKU-CHEM-1222-50": {
        "sku_id": "SKU-CHEM-1222-50", "cas": "1222-05-5",
        "trade_name_cn": "Galaxolide 50% in IPM", "trade_name_en": "Galaxolide 50% in IPM",
        "supplier_zh": "單體庫 / IFF 規格", "supplier_en": "Aroma Chem Lab (IFF Spec)",
        "lot_no": "LOT-GLX-50", "exp_date": "2029/10/01",
        "dilution_pct": 50.0, "solvent": "IPM (肉豆蔻酸異丙酯)", "sg": 0.929, "cost_per_g": 3.0,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {}
    },
    "SKU-CHEM-60128-50": {
        "sku_id": "SKU-CHEM-60128-50", "cas": "60-12-8",
        "trade_name_cn": "苯乙醇 PEA 50% in DPG", "trade_name_en": "Phenethyl Alcohol 50% in DPG",
        "supplier_zh": "單體庫", "supplier_en": "Aroma Chem Lab",
        "lot_no": "LOT-PEA-01", "exp_date": "2029/08/15",
        "dilution_pct": 50.0, "solvent": "DPG (二丙二醇)", "sg": 1.022, "cost_per_g": 2.5,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {}
    },
    "SKU-CHEM-5392-10": {
        "sku_id": "SKU-CHEM-5392-10", "cas": "5392-40-5",
        "trade_name_cn": "檸檬醛 Citral 10% in DPG", "trade_name_en": "Citral 10% in DPG",
        "supplier_zh": "單體庫", "supplier_en": "Aroma Chem Lab",
        "lot_no": "LOT-CIT-10", "exp_date": "2028/05/01",
        "dilution_pct": 10.0, "solvent": "DPG (二丙二醇)", "sg": 1.010, "cost_per_g": 1.5,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Citral": 1.0}
    },
    # --- 中興化工採購批次 ---
    "SKU-ZX-8006904": {
        "sku_id": "SKU-ZX-8006904", "cas": "8006-90-4",
        "trade_name_cn": "中興化工 法國歐薄荷精油 (100% 純油)", "trade_name_en": "Chunghsing French Peppermint EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260526-PEP", "exp_date": "2028/09/14",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.898, "cost_per_g": 22.3,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.03, "Linalool": 0.01}
    },
    "SKU-ZX-8022911": {
        "sku_id": "SKU-ZX-8022911", "cas": "8022-91-1",
        "trade_name_cn": "中興化工 中國芳樟葉精油 (100% 純油)", "trade_name_en": "Chunghsing Ho Wood EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260526-HO", "exp_date": "2028/02/12",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.865, "cost_per_g": 23.1,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Linalool": 0.92}
    },
    "SKU-ZX-8001614": {
        "sku_id": "SKU-ZX-8001614", "cas": "8001-61-4",
        "trade_name_cn": "中興化工 古巴香脂精油 (100% 純油)", "trade_name_en": "Chunghsing Copaiba Balsam EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260526-COP", "exp_date": "2027/02/27",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.900, "cost_per_g": 27.8,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {}
    },
    "SKU-ZX-8006813": {
        "sku_id": "SKU-ZX-8006813", "cas": "8006-81-3",
        "trade_name_cn": "中興化工 馬達加斯加完全伊蘭 (10% in DPG)", "trade_name_en": "Chunghsing Madagascar Ylang Complete (10% in DPG)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260530-YLA", "exp_date": "2029/03/01",
        "dilution_pct": 10.0, "solvent": "DPG (二丙二醇)", "sg": 1.014, "cost_per_g": 40.9,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Benzyl Benzoate": 0.08, "Linalool": 0.12, "Geraniol": 0.02}
    },
    "SKU-ZX-8028486": {
        "sku_id": "SKU-ZX-8028486", "cas": "8028-48-6",
        "trade_name_cn": "中興化工 義大利冷壓甜橙精油 (100% 純油)", "trade_name_en": "Chunghsing Italian Sweet Orange EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260603-ORG", "exp_date": "2028/09/07",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.844, "cost_per_g": 12.0,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.94, "Linalool": 0.01}
    },
    "SKU-ZX-8000280": {
        "sku_id": "SKU-ZX-8000280", "cas": "8000-28-0",
        "trade_name_cn": "中興化工 法國高山薰衣草精油 (100% 純油)", "trade_name_en": "Chunghsing French Lavender Pop. EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260603-LAV", "exp_date": "2029/02/09",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.880, "cost_per_g": 39.8,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Linalool": 0.38, "Limonene": 0.01, "Coumarin": 0.005}
    },
    "SKU-ZX-92201508": {
        "sku_id": "SKU-ZX-92201508", "cas": "92201-50-8",
        "trade_name_cn": "中興化工 馬達加斯加羅溫莎葉 (100% 純油)", "trade_name_en": "Chunghsing Madagascar Ravintsara EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260603-RAV", "exp_date": "2028/08/11",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.900, "cost_per_g": 38.9,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.03, "Linalool": 0.01}
    },
    "SKU-ZX-8016362": {
        "sku_id": "SKU-ZX-8016362", "cas": "8016-36-2",
        "trade_name_cn": "中興化工 索馬利亞乳香精油 (100% 純油)", "trade_name_en": "Chunghsing Somalia Olibanum EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260603-OLI", "exp_date": "2028/12/01",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.875, "cost_per_g": 80.0,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.14}
    },
    "SKU-ZX-8008319": {
        "sku_id": "SKU-ZX-8008319", "cas": "8008-31-9",
        "trade_name_cn": "中興化工 義大利紅橘精油 (100% 純油)", "trade_name_en": "Chunghsing Italian Tangerine EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260603-TAN", "exp_date": "2028/06/05",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.845, "cost_per_g": 23.7,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.90, "Linalool": 0.01}
    },
    "SKU-ZX-8014173": {
        "sku_id": "SKU-ZX-8014173", "cas": "8014-17-3",
        "trade_name_cn": "中興化工 南美苦橙葉精油 (100% 純油)", "trade_name_en": "Chunghsing South America Petitgrain EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260626-PET", "exp_date": "2028/12/01",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.885, "cost_per_g": 28.3,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Linalool": 0.25, "Limonene": 0.08, "Geraniol": 0.03}
    },
    "SKU-ZX-8016635": {
        "sku_id": "SKU-ZX-8016635", "cas": "8016-63-5",
        "trade_name_cn": "中興化工 法國快樂鼠尾草精油 (100% 純油)", "trade_name_en": "Chunghsing French Clary Sage EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260626-CLA", "exp_date": "2029/01/15",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.890, "cost_per_g": 33.7,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Linalool": 0.22, "Geraniol": 0.02}
    },
    "SKU-ZX-91770580": {
        "sku_id": "SKU-ZX-91770580", "cas": "91770-58-0",
        "trade_name_cn": "中興化工 台灣肖楠木精油 (100% 純油)", "trade_name_en": "Chunghsing Taiwan Incense Cedar EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260727-CED", "exp_date": "2029/04/22",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.940, "cost_per_g": 74.5,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {}
    },
    "SKU-ZX-9000059": {
        "sku_id": "SKU-ZX-9000059", "cas": "9000-05-9",
        "trade_name_cn": "中興化工 蘇門答臘安息香 (50% in TEC 預溶)", "trade_name_en": "Chunghsing Sumatra Benzoin (50% in TEC)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260811-BEN", "exp_date": "2029/08/11",
        "dilution_pct": 50.0, "solvent": "TEC (檸檬酸三乙酯)", "sg": 1.144, "cost_per_g": 17.4,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Benzyl Benzoate": 0.15, "Cinnamal": 0.01}
    },
    "SKU-ZX-8002684": {
        "sku_id": "SKU-ZX-8002684", "cas": "8002-68-4",
        "trade_name_cn": "中興化工 杜松子精油 (100% 純油)", "trade_name_en": "Chunghsing Juniper Berry EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260927-JUN", "exp_date": "2029/09/27",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.865, "cost_per_g": 28.9,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.05}
    },
    "SKU-ZX-8006824": {
        "sku_id": "SKU-ZX-8006824", "cas": "8006-82-4",
        "trade_name_cn": "中興化工 黑胡椒精油 (100% 純油)", "trade_name_en": "Chunghsing Black Pepper EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-260927-PEP", "exp_date": "2029/09/27",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.875, "cost_per_g": 34.3,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.18, "Linalool": 0.01}
    },
    "SKU-ZX-91745969": {
        "sku_id": "SKU-ZX-91745969", "cas": "91745-96-9",
        "trade_name_cn": "中興化工 台灣紅檜樹心精油 (100% 純油)", "trade_name_en": "Chunghsing Taiwan Red Hinoki EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-261030-HIN", "exp_date": "2029/10/30",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.940, "cost_per_g": 37.2,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {}
    },
    "SKU-ZX-8021292": {
        "sku_id": "SKU-ZX-8021292", "cas": "8021-29-2",
        "trade_name_cn": "中興化工 西伯利亞冷杉精油 (100% 純油)", "trade_name_en": "Chunghsing Siberian Fir EO (100% Neat)",
        "supplier_zh": "中興化工", "supplier_en": "Chunghsing Chem",
        "lot_no": "ZX-261030-FIR", "exp_date": "2029/10/30",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.900, "cost_per_g": 22.2,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.15}
    },
    # --- 精油好事多 & 沐禾芳療 & 樸草園 ---
    "SKU-OH-8014195": {
        "sku_id": "SKU-OH-8014195", "cas": "8014-19-5",
        "trade_name_cn": "精油好事多 印度玫瑰草精油 (100% 純油)", "trade_name_en": "Oilhausco Indian Palmarosa EO (100% Neat)",
        "supplier_zh": "精油好事多", "supplier_en": "Oilhausco",
        "lot_no": "OH-260510-PAL", "exp_date": "2027/08/31",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.885, "cost_per_g": 24.2,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Geraniol": 0.82, "Linalool": 0.03}
    },
    "SKU-OH-8000257": {
        "sku_id": "SKU-OH-8000257", "cas": "8000-25-7",
        "trade_name_cn": "精油好事多 桉油醇迷迭香 (100% 純油)", "trade_name_en": "Oilhausco Rosemary Cineole EO (100% Neat)",
        "supplier_zh": "精油好事多", "supplier_en": "Oilhausco",
        "lot_no": "OH-260510-ROS", "exp_date": "2030/06/30",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.905, "cost_per_g": 26.0,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.04, "Linalool": 0.02}
    },
    "SKU-MH-8007758": {
        "sku_id": "SKU-MH-8007758", "cas": "8007-75-8",
        "trade_name_cn": "沐禾芳療 義大利佛手柑精油 (100% 純油)", "trade_name_en": "AromaHarvest Italian Bergamot EO (100% Neat)",
        "supplier_zh": "沐禾芳療", "supplier_en": "AromaHarvest",
        "lot_no": "MH-260429-BER", "exp_date": "2028/04/29",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.875, "cost_per_g": 68.6,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.42, "Linalool": 0.12, "Citral": 0.01}
    },
    "SKU-MH-8014684": {
        "sku_id": "SKU-MH-8014684", "cas": "8014-68-4",
        "trade_name_cn": "沐禾芳療 綠花白千層精油 (100% 純油)", "trade_name_en": "AromaHarvest Niaouli EO (100% Neat)",
        "supplier_zh": "沐禾芳療", "supplier_en": "AromaHarvest",
        "lot_no": "MH-260519-NIA", "exp_date": "2030/06/30",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.910, "cost_per_g": 24.7,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.08, "Linalool": 0.01}
    },
    "SKU-MH-8000484": {
        "sku_id": "SKU-MH-8000484", "cas": "8000-48-4",
        "trade_name_cn": "沐禾芳療 澳洲尤加利精油 (100% 純油)", "trade_name_en": "AromaHarvest Eucalyptus Radiata EO (100% Neat)",
        "supplier_zh": "沐禾芳療", "supplier_en": "AromaHarvest",
        "lot_no": "MH-260519-EUC", "exp_date": "2030/11/30",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.910, "cost_per_g": 26.4,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.06, "Citral": 0.01}
    },
    "SKU-MH-8013863": {
        "sku_id": "SKU-MH-8013863", "cas": "8013-86-3",
        "trade_name_cn": "沐禾芳療 法國絲柏精油 (100% 純油)", "trade_name_en": "AromaHarvest French Cypress EO (100% Neat)",
        "supplier_zh": "沐禾芳療", "supplier_en": "AromaHarvest",
        "lot_no": "MH-260519-CYP", "exp_date": "2030/11/30",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.870, "cost_per_g": 33.9,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.04}
    },
    "SKU-MH-8014093": {
        "sku_id": "SKU-MH-8014093", "cas": "8014-09-3",
        "trade_name_cn": "沐禾芳療 印尼廣藿香精油 (100% 純油)", "trade_name_en": "AromaHarvest Indonesian Patchouli EO (100% Neat)",
        "supplier_zh": "沐禾芳療", "supplier_en": "AromaHarvest",
        "lot_no": "MH-260609-PAT", "exp_date": "2031/01/31",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.965, "cost_per_g": 38.9,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {}
    },
    "SKU-MH-8000279": {
        "sku_id": "SKU-MH-8000279", "cas": "8000-27-9",
        "trade_name_cn": "沐禾芳療 維吉尼亞雪松精油 (100% 純油)", "trade_name_en": "AromaHarvest Cedarwood Virginia EO (100% Neat)",
        "supplier_zh": "沐禾芳療", "supplier_en": "AromaHarvest",
        "lot_no": "MH-260609-CED", "exp_date": "2030/01/31",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.920, "cost_per_g": 28.3,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {}
    },
    "SKU-MH-8023890": {
        "sku_id": "SKU-MH-8023890", "cas": "8023-89-0",
        "trade_name_cn": "沐禾芳療 欖香脂精油 (100% 純油)", "trade_name_en": "AromaHarvest Elemi EO (100% Neat)",
        "supplier_zh": "沐禾芳療", "supplier_en": "AromaHarvest",
        "lot_no": "MH-260609-ELE", "exp_date": "2029/07/31",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.880, "cost_per_g": 31.3,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.52}
    },
    "SKU-MH-68647734": {
        "sku_id": "SKU-MH-68647734", "cas": "68647-73-4",
        "trade_name_cn": "沐禾芳療 澳洲茶樹精油 (100% 純油)", "trade_name_en": "AromaHarvest Australian Tea Tree EO (100% Neat)",
        "supplier_zh": "沐禾芳療", "supplier_en": "AromaHarvest",
        "lot_no": "MH-260609-TEA", "exp_date": "2031/04/30",
        "dilution_pct": 100.0, "solvent": "None (100%純原液)", "sg": 0.900, "cost_per_g": 28.3,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Limonene": 0.03, "Linalool": 0.01}
    },
    "SKU-PCY-MALLOTUS": {
        "sku_id": "SKU-PCY-MALLOTUS", "cas": "NCS-MALLOTUS-01",
        "trade_name_cn": "樸草園 清輕白楸花複方 (50% in Solketal/DPG)", "trade_name_en": "PuCaoYuan Mallotus Flower Accord (50% Diluted)",
        "supplier_zh": "樸草園", "supplier_en": "PuCaoYuan",
        "lot_no": "PCY-260415-MAL", "exp_date": "2028/04/15",
        "dilution_pct": 50.0, "solvent": "DPG (二丙二醇)", "sg": 0.966, "cost_per_g": 54.9,
        "docs": {"COA": True, "SDS": True, "IFRA": True},
        "allergens": {"Linalool": 0.10, "Limonene": 0.05}
    }
}
