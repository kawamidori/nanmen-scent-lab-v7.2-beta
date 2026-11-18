# file_export.py
import io
import pandas as pd
from datetime import datetime

def build_tfda_pif_16_excel(mod_name, perfumer_name, dosage_pct, pif_rows, over_10ppm_list):
    """
    Generates a pre-formatted Excel file mapping formula data into 
    Taiwan TFDA PIF (Product Information File) Item 16 structure.
    """
    buf = io.BytesIO()
    
    # 1. 產品基本資訊表 (Product Basic Info)
    info_data = [
        ["產品名稱 (Product Name)", f"{mod_name} ({dosage_pct:.1f}%)"],
        ["建立日期 (Date)", datetime.now().strftime("%Y-%m-%d")],
        ["建檔人員 (Prepared By)", perfumer_name],
        ["文件類型 (Doc Type)", "TFDA 化粧品產品資訊檔案 (PIF) - 第16項：產品安全資料"]
    ]
    df_info = pd.DataFrame(info_data, columns=["欄位 (Field)", "內容 (Content)"])
    
    # 2. 全成分與暴露量計算表 (Full Quantitative Composition & Exposure)
    # TFDA PIF 16 requires exact ingredient percentages in the finished product
    comp_data = []
    for r in pif_rows:
        # Find the dynamic key for Finished %
        fin_key = [k for k in r.keys() if k.startswith("% in Finished")][0]
        comp_data.append({
            "INCI Name / 原料名稱": r["Material Name"],
            "CAS No.": r["CAS No."],
            "Supplier / 供應商": r.get("Supplier", "-"),
            "配方佔比 (Formula % in Pure Oil)": f"{r['% in Pure Oil']:.3f}%",
            "成品最終濃度 (Finished Product % / 暴露量)": f"{r[fin_key]:.4f}%"
        })
    df_comp = pd.DataFrame(comp_data)
    
    # 3. 法定致敏原清單表 (Regulated Allergens)
    allg_data = []
    if over_10ppm_list:
        for a in over_10ppm_list:
            allg_data.append({
                "致敏原 INCI Name": a["name"].upper(),
                "成品中濃度 (ppm)": a["ppm"],
                "成品中濃度 (%)": f"{a['pct_finished']:.4f}%",
                "TFDA 標示要求": "超過 10 ppm，駐留型產品需強制標示於外盒"
            })
    else:
        allg_data.append({
            "致敏原 INCI Name": "無 (None detected)",
            "成品中濃度 (ppm)": 0,
            "成品中濃度 (%)": "0%",
            "TFDA 標示要求": "低於 10 ppm 免標示"
        })
    df_allg = pd.DataFrame(allg_data)
    
    # Write to Excel with multiple sheets
    with pd.ExcelWriter(buf, engine="xlsxwriter") as writer:
        df_info.to_excel(writer, sheet_name="01_基本資訊", index=False)
        df_comp.to_excel(writer, sheet_name="02_全成分暴露量", index=False)
        df_allg.to_excel(writer, sheet_name="03_法定致敏原清單", index=False)
        
        # Auto-adjust column widths
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]
            worksheet.set_column('A:B', 35)
            if sheet_name == "02_全成分暴露量":
                worksheet.set_column('C:E', 25)
            elif sheet_name == "03_法定致敏原清單":
                worksheet.set_column('C:D', 40)
                
    return buf.getvalue()
