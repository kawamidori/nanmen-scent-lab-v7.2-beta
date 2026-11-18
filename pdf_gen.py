# pdf_gen.py
import io
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

import os
from reportlab.pdfbase.ttfonts import TTFont

# Register Chinese Font (TrueType preferred for Streamlit Cloud / Linux, fallback to CID MSung-Light)
CJK_FONT = "Helvetica"
try:
    # Try common Linux system font paths for Noto Sans CJK
    font_paths = [
        "/usr/share/fonts/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
    ]
    font_loaded = False
    for fp in font_paths:
        if os.path.exists(fp):
            pdfmetrics.registerFont(TTFont("NotoSansCJK", fp))
            CJK_FONT = "NotoSansCJK"
            font_loaded = True
            break
    
    if not font_loaded:
        # Fallback to CID font if TrueType is unavailable
        pdfmetrics.registerFont(UnicodeCIDFont("MSung-Light"))
        CJK_FONT = "MSung-Light"
except Exception as e:
    print(f"Font registration warning: {e}")
    CJK_FONT = "Helvetica"

def _escape_xml(text):
    if text is None:
        return ""
    s = str(text)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def _get_styles():
    return {
        "brand": ParagraphStyle("Brand", fontName="Helvetica-Bold", fontSize=14, textColor=colors.HexColor("#0F172A"), leading=18),
        "sub": ParagraphStyle("Sub", fontName=CJK_FONT, fontSize=8.5, textColor=colors.HexColor("#475569"), leading=12),
        "h1": ParagraphStyle("H1", fontName=CJK_FONT, fontSize=13, textColor=colors.HexColor("#0F172A"), leading=17, spaceBefore=6, spaceAfter=4),
        "h2": ParagraphStyle("H2", fontName=CJK_FONT, fontSize=10.5, textColor=colors.HexColor("#0369A1"), leading=14, spaceBefore=8, spaceAfter=4),
        "body": ParagraphStyle("Body", fontName=CJK_FONT, fontSize=9, textColor=colors.HexColor("#1E293B"), leading=13),
        "small": ParagraphStyle("Small", fontName=CJK_FONT, fontSize=8, textColor=colors.HexColor("#475569"), leading=11),
        "cell": ParagraphStyle("Cell", fontName=CJK_FONT, fontSize=8, textColor=colors.HexColor("#0F172A"), leading=10.5),
        "cell_hdr": ParagraphStyle("CellHdr", fontName=CJK_FONT, fontSize=8, textColor=colors.white, leading=10.5),
        "code": ParagraphStyle("Code", fontName="Helvetica", fontSize=8.5, textColor=colors.HexColor("#0F172A"), leading=12, backColor=colors.HexColor("#F1F5F9")),
        "nda_warn": ParagraphStyle("NdaWarn", fontName=CJK_FONT, fontSize=8.5, textColor=colors.HexColor("#92400E"), leading=12)
    }

def _header_banner(title_en, subtitle_zh, doc_code):
    st = _get_styles()
    tbl = Table(
        [[
            Paragraph(f"<b>NANMEN SCENT LAB OS</b><br/><font size='8' color='#94A3B8'>Enterprise Perfumery &amp; Regulatory Compliance System</font>", ParagraphStyle("BannerL", fontName="Helvetica", fontSize=12, textColor=colors.white, leading=15)),
            Paragraph(f"<b>{_escape_xml(doc_code)}</b><br/><font size='8' color='#38BDF8'>Date: {datetime.now().strftime('%Y-%m-%d')}</font>", ParagraphStyle("BannerR", fontName="Helvetica", fontSize=9.5, textColor=colors.white, leading=13, alignment=TA_RIGHT))
        ]],
        colWidths=[125 * mm, 55 * mm]
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#0F172A")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    elems = [
        tbl,
        Spacer(1, 6),
        Paragraph(f"<b>{_escape_xml(title_en)}</b>", st["h1"]),
        Paragraph(_escape_xml(subtitle_zh), st["sub"]),
        HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceBefore=4, spaceAfter=8)
    ]
    return elems

def build_formula_sheet_pdf(mod_name, perfumer_name, region_code, dosage_pct, notes, total_jus_g, total_active_g, total_carrier_g, print_rows):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm, topMargin=14*mm, bottomMargin=14*mm)
    st = _get_styles()
    elems = _header_banner(
        f"FORMULATION RECORD SHEET — {mod_name}",
        f"調香師 / Perfumer: {perfumer_name} ｜ 法規基準 / Reg: {region_code} ｜ 目標賦香率 / Dosage: {dosage_pct:.1f}%",
        f"DOC-{mod_name.replace(' ', '')}"
    )

    meta_tbl = Table(
        [
            [Paragraph(f"<b>Total Jus Weight (配方總重):</b> {total_jus_g:.3f} g", st["body"]),
             Paragraph(f"<b>Pure Active Oil (純香精淨重):</b> {total_active_g:.3f} g", st["body"]),
             Paragraph(f"<b>Carrier Solvent (載體溶劑):</b> {total_carrier_g:.3f} g", st["body"])],
            [Paragraph(f"<b>Perfumer Notes (調香筆記):</b> {_escape_xml(notes or 'N/A')}", st["body"]), "", ""]
        ],
        colWidths=[60*mm, 60*mm, 60*mm]
    )
    meta_tbl.setStyle(TableStyle([
        ("SPAN", (0, 1), (2, 1)),
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#CBD5E1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#E2E8F0")),
        ("PADDING", (0, 0), (-1, -1), 6),
    ]))
    elems.append(meta_tbl)
    elems.append(Spacer(1, 10))

    headers = ["#", "Note", "CAS No.", "Material Name (原料名稱)", "Dilution Spec", "Gross (g)", "Active (g)", "Share (%)", "PPT (‰)"]
    table_data = [[Paragraph(f"<b>{h}</b>", st["cell_hdr"]) for h in headers]]
    for r in print_rows:
        spec_s = f"{r['dilution_pct']:.0f}% in {r['solvent'].split(' ')[0]}" if r["dilution_pct"] < 100 else "100% Neat"
        table_data.append([
            Paragraph(str(r["seq"]), st["cell"]),
            Paragraph(_escape_xml(r["note"]), st["cell"]),
            Paragraph(_escape_xml(r["cas"]), st["cell"]),
            Paragraph(_escape_xml(r["name_disp"]), st["cell"]),
            Paragraph(_escape_xml(spec_s), st["cell"]),
            Paragraph(f"{r['gross_g']:.3f}", st["cell"]),
            Paragraph(f"{r['active_g']:.3f}", st["cell"]),
            Paragraph(f"{r['pct']:.2f}%", st["cell"]),
            Paragraph(f"{r['ppt']:.1f}", st["cell"]),
        ])

    col_w = [8*mm, 14*mm, 24*mm, 54*mm, 24*mm, 15*mm, 15*mm, 14*mm, 12*mm]
    t = Table(table_data, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0F172A")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CBD5E1")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    elems.append(t)
    doc.build(elems)
    return buf.getvalue()

def build_ifra_certificate_pdf(cert_no, mod_name, perfumer_name, dosage_pct, all_ifra_pass, has_banned, max_safe_dosage_pct, ifra_categories):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm, topMargin=14*mm, bottomMargin=14*mm)
    st = _get_styles()
    elems = _header_banner(
        "CERTIFICATE OF CONFORMITY WITH IFRA STANDARDS (51st Amendment)",
        f"IFRA 第 51 版跨品類符合性聲明書 ｜ Certificate No.: {cert_no}",
        cert_no
    )

    if has_banned:
        status_text = "PROHIBITED / FAIL — EU BANNED SUBSTANCE DETECTED (0.0% TOLERANCE)"
        status_bg = colors.HexColor("#FEE2E2")
        status_fg = "#B91C1C"
    elif all_ifra_pass:
        status_text = f"CONFORMING (PASS) — Safe up to {max_safe_dosage_pct:.2f}% in Category 4 (Fine Fragrance)"
        status_bg = colors.HexColor("#DCFCE7")
        status_fg = "#15803D"
    else:
        status_text = f"NON-CONFORMING (FAIL) — Exceeds IFRA Cat.4 Limit at {dosage_pct:.1f}% (Max Safe: {max_safe_dosage_pct:.2f}%)"
        status_bg = colors.HexColor("#FEE2E2")
        status_fg = "#B91C1C"

    badge_tbl = Table(
        [[Paragraph(f"<b><font color='{status_fg}'>{status_text}</font></b>", st["body"])]],
        colWidths=[180*mm]
    )
    badge_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), status_bg),
        ("BOX", (0, 0), (-1, -1), 1.0, colors.HexColor(status_fg)),
        ("PADDING", (0, 0), (-1, -1), 7),
    ]))
    elems.append(badge_tbl)
    elems.append(Spacer(1, 8))

    attest_txt = (
        f"We hereby certify that the fragrance compound <b>{_escape_xml(mod_name)}</b>, formulated by "
        f"<b>{_escape_xml(perfumer_name)}</b>, has been evaluated against the Standards of the International "
        f"Fragrance Association (IFRA 51st Amendment) and EU Cosmetics Regulation (EC) No. 1223/2009. "
        f"The maximum allowable concentrations of pure fragrance concentrate in finished consumer products across "
        f"IFRA Categories 1 through 12 are specified below:"
    )
    elems.append(Paragraph(attest_txt, st["body"]))
    elems.append(Spacer(1, 8))

    headers = ["IFRA Category", "Product Type / Application Scope (適用產品類別)", "Max Allowable Conc. (%)"]
    t_data = [[Paragraph(f"<b>{h}</b>", st["cell_hdr"]) for h in headers]]
    for c in ifra_categories:
        vals = list(c.values())
        t_data.append([
            Paragraph(f"<b>{_escape_xml(vals[0])}</b>", st["cell"]),
            Paragraph(_escape_xml(vals[1]), st["cell"]),
            Paragraph(f"<b>{_escape_xml(vals[2])}</b>", st["cell"]),
        ])

    cat_tbl = Table(t_data, colWidths=[32*mm, 113*mm, 35*mm], repeatRows=1)
    cat_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0F172A")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CBD5E1")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("PADDING", (0, 0), (-1, -1), 4.5),
    ]))
    elems.append(cat_tbl)
    elems.append(Spacer(1, 14))

    sig_tbl = Table(
        [[
            Paragraph(f"<b>Issued By (簽發單位):</b><br/>{_escape_xml(perfumer_name)} / Nanmen Scent Lab OS", st["small"]),
            Paragraph(f"<b>Authorized Signature (簽章確認):</b><br/>_______________________________<br/>Date: {datetime.now().strftime('%Y-%m-%d')}", st["small"])
        ]],
        colWidths=[90*mm, 90*mm]
    )
    sig_tbl.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#CBD5E1")),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))
    elems.append(sig_tbl)
    doc.build(elems)
    return buf.getvalue()

def build_pif_dossier_pdf(
    nda_ref_no, perfumer_name, brand_name, sa_name, mod_name,
    tier_label, dosage_pct, region_label, cert_no, all_ifra_pass,
    has_banned, max_safe_dosage_pct, jus_sg, maceration_days,
    pure_share_pct, carrier_share_pct, pif_rows, ifra_categories,
    over_10ppm_list, inci_final_str
):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm, topMargin=14*mm, bottomMargin=14*mm)
    st = _get_styles()
    elems = _header_banner(
        "CONFIDENTIAL PRODUCT INFORMATION FILE (PIF) TECHNICAL DOSSIER",
        f"三方保密協議直傳安全評估人員 (SA) 完整技術文件包 ｜ NDA Ref: {nda_ref_no}",
        nda_ref_no
    )

    # Confidentiality & Tri-Party NDA Box
    nda_tbl = Table(
        [
            [Paragraph("<b>STRICTLY CONFIDENTIAL — TRI-PARTY NDA ISOLATION PROTOCOL</b><br/>Disclosed exclusively to the designated Safety Assessor (SA) for Cosmetic Product Safety Report (CPSR / PIF) evaluation under EU EC 1223/2009 &amp; Taiwan TFDA regulations.", st["nda_warn"]), ""],
            [Paragraph(f"<b>① Disclosing Party (Perfumer):</b> {_escape_xml(perfumer_name)}", st["cell"]),
             Paragraph(f"<b>② Commissioning Party (Brand):</b> {_escape_xml(brand_name or '[Pending Brand Owner]')}", st["cell"])],
            [Paragraph(f"<b>③ Receiving Party (Safety Assessor / SA):</b> {_escape_xml(sa_name or '[Pending SA Name]')}", st["cell"]),
             Paragraph(f"<b>④ Product Application:</b> {_escape_xml(tier_label)} ({dosage_pct:.1f}%)", st["cell"])]
        ],
        colWidths=[90*mm, 90*mm]
    )
    nda_tbl.setStyle(TableStyle([
        ("SPAN", (0, 0), (1, 0)),
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFFBEB")),
        ("BOX", (0, 0), (-1, -1), 1.0, colors.HexColor("#D97706")),
        ("INNERGRID", (0, 1), (-1, -1), 0.4, colors.HexColor("#FDE68A")),
        ("PADDING", (0, 0), (-1, -1), 6),
    ]))
    elems.append(nda_tbl)
    elems.append(Spacer(1, 8))

    # PART 1: 100% Quantitative Composition
    elems.append(Paragraph(
        f"<b>PART 1: 100% FULL QUANTITATIVE FRAGRANCE COMPOSITION (Pure Oil: {pure_share_pct:.2f}% | Carrier: {carrier_share_pct:.2f}%)</b>",
        st["h2"]
    ))
    p1_headers = ["CAS No.", "Material Name (原料名稱)", "Dilution Spec", "% in Pure Oil", f"% Finished ({dosage_pct:.0f}%)"]
    p1_data = [[Paragraph(f"<b>{h}</b>", st["cell_hdr"]) for h in p1_headers]]
    for r in pif_rows:
        fin_key = [k for k in r.keys() if k.startswith("% in Finished")][0]
        p1_data.append([
            Paragraph(_escape_xml(r["CAS No."]), st["cell"]),
            Paragraph(_escape_xml(r["Material Name"]), st["cell"]),
            Paragraph(_escape_xml(r["Dilution"]), st["cell"]),
            Paragraph(f"{r['% in Pure Oil']:.3f}%", st["cell"]),
            Paragraph(f"{r[fin_key]:.4f}%", st["cell"]),
        ])
    t1 = Table(p1_data, colWidths=[28*mm, 72*mm, 30*mm, 24*mm, 26*mm], repeatRows=1)
    t1.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0F172A")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CBD5E1")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    elems.append(t1)
    elems.append(Spacer(1, 8))

    # PART 2: Regulated Allergens & Official INCI String
    elems.append(Paragraph("<b>PART 2: REGULATED ALLERGEN DECLARATION (&gt;10 PPM) &amp; OFFICIAL INCI LABEL</b>", st["h2"]))
    if over_10ppm_list:
        a_headers = ["Allergen (INCI Name)", "PPM in Finished Product", "% in Finished Product", "Regulatory Action"]
        a_data = [[Paragraph(f"<b>{h}</b>", st["cell_hdr"]) for h in a_headers]]
        for a in over_10ppm_list:
            a_data.append([
                Paragraph(f"<b>{_escape_xml(a['name'].upper())}</b>", st["cell"]),
                Paragraph(f"{a['ppm']:.1f} ppm", st["cell"]),
                Paragraph(f"{a['pct_finished']:.4f}%", st["cell"]),
                Paragraph("Mandatory Box Label (&gt;10 ppm)", st["cell"]),
            ])
        ta = Table(a_data, colWidths=[55*mm, 40*mm, 40*mm, 45*mm], repeatRows=1)
        ta.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0369A1")),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CBD5E1")),
            ("PADDING", (0, 0), (-1, -1), 4),
        ]))
        elems.append(ta)
    else:
        elems.append(Paragraph("No regulated fragrance allergens exceed the 10 ppm leave-on declaration threshold.", st["body"]))

    elems.append(Spacer(1, 5))
    elems.append(Paragraph(f"<b>Official Packaging INCI String:</b><br/>{_escape_xml(inci_final_str)}", st["code"]))
    elems.append(Spacer(1, 8))

    # PART 3: MSDS / GHS & IFRA Summary
    elems.append(Paragraph(f"<b>PART 3: MSDS / GHS SUMMARY &amp; IFRA 51st STATUS ({cert_no})</b>", st["h2"]))
    ifra_verdict = "PROHIBITED / FAIL (EU BANNED)" if has_banned else ("CONFORMING (PASS)" if all_ifra_pass else "EXCEEDS LIMIT (FAIL)")
    msds_tbl = Table(
        [
            [Paragraph(f"<b>IFRA 51st Verdict:</b> {ifra_verdict}", st["cell"]),
             Paragraph(f"<b>Cat.4 Max Safe Dosage:</b> {max_safe_dosage_pct:.2f}%", st["cell"])],
            [Paragraph(f"<b>Relative Density (20°C):</b> {jus_sg} g/cm³", st["cell"]),
             Paragraph(f"<b>Flash Point:</b> ~68°C (Jus) / ~14°C (Finished)", st["cell"])],
            [Paragraph("<b>GHS Hazards:</b> H225 Flam. Liq. 2, H317 Skin Sens. 1, H411 Aquatic Chronic 2", st["cell"]),
             Paragraph(f"<b>Maturation &amp; Filtration:</b> {maceration_days} days; -4°C / 0.45μm", st["cell"])]
        ],
        colWidths=[90*mm, 90*mm]
    )
    msds_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#CBD5E1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#E2E8F0")),
        ("PADDING", (0, 0), (-1, -1), 5),
    ]))
    elems.append(msds_tbl)

    doc.build(elems)
    return buf.getvalue()
