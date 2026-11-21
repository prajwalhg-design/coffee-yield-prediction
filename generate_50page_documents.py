"""
generate_50page_documents.py
----------------------------
Assembles the complete 50-page major project final report in both Microsoft Word (.docx)
and print-compiled PDF (.pdf) formats conforming strictly to the Department of
Information Science and Engineering (ISE), Malnad College of Engineering (MCE),
Hassan - 573201 (Academic Year 2025-26).
"""

import os
import re
import subprocess
import shutil
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

from report_data import PAGES

def sanitize_xml(s):
    if not isinstance(s, str):
        return s
    s = s.replace('\x0c', r'\f').replace('\x07', r'\a')
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', s)

BASE_DIR = r'C:\Users\prajw\.gemini\antigravity\scratch\coffee_yield_project'
IMG_DIR = os.path.join(BASE_DIR, 'report_images')
BRAIN_DIR = r'C:\Users\prajw\.gemini\antigravity\brain\8ddc1524-2d7e-4612-a363-58bd93735cf3'

DOCX_OUT = os.path.join(BASE_DIR, 'Coffee_Yield_Major_Project_Final_Report_50Pages.docx')
HTML_OUT = os.path.join(BASE_DIR, 'Coffee_Yield_Major_Project_Final_Report_50Pages.html')
PDF_OUT = os.path.join(BASE_DIR, 'Coffee_Yield_Major_Project_Final_Report_50Pages.pdf')

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def setup_word_header_footer(section):
    # Header
    header = section.header
    hp = header.paragraphs[0]
    hp.text = ""
    r1 = hp.add_run("Coffee Yield Prediction and Loss Diagnosis Using Explainable AI")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(9.5)
    r1.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    
    rtab = hp.add_run("\t\t2025-26")
    rtab.font.name = 'Times New Roman'
    rtab.font.size = Pt(9.5)
    rtab.font.bold = True
    
    pPr = hp._p.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="4" w:color="888888"/></w:pBdr>')
    pPr.append(pBdr)

    # Footer
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.text = ""
    rdept = fp.add_run("Dept of ISE, MCE")
    rdept.font.name = 'Times New Roman'
    rdept.font.size = Pt(9.5)
    rdept.font.bold = True
    
    fp.add_run("\t\t")
    fld = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
    fp._p.append(fld)
    
    fpPr = fp._p.get_or_add_pPr()
    fpBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:top w:val="single" w:sz="6" w:space="4" w:color="888888"/></w:pBdr>')
    fpPr.append(fpBdr)

def build_docx():
    print("Building Word Document (.docx)...")
    doc = Document()

    # Configure Margins (A4)
    sec = doc.sections[0]
    sec.page_width = Inches(8.27)
    sec.page_height = Inches(11.69)
    sec.top_margin = Inches(0.85)
    sec.bottom_margin = Inches(0.85)
    sec.left_margin = Inches(0.95)
    sec.right_margin = Inches(0.80)
    setup_word_header_footer(sec)

    for page_num in range(1, 51):
        pdata = PAGES.get(page_num, {})
        
        # Check if new chapter starts on this page
        if pdata.get("chapter") and page_num in [1, 5, 12, 17, 24, 31, 44]:
            p_c = doc.add_paragraph()
            p_c.paragraph_format.space_before = Pt(16)
            p_c.paragraph_format.space_after = Pt(2)
            rc = p_c.add_run(f"CHAPTER {pdata['chapter']}\n")
            rc.font.name = 'Times New Roman'
            rc.font.size = Pt(13)
            rc.font.bold = True
            
            p_t = doc.add_paragraph()
            p_t.paragraph_format.space_before = Pt(0)
            p_t.paragraph_format.space_after = Pt(14)
            p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
            rt = p_t.add_run(pdata['chapter_title'])
            rt.font.name = 'Times New Roman'
            rt.font.size = Pt(13)
            rt.font.bold = True
        elif pdata.get("chapter_title") and page_num in [47, 48, 49, 50]:
            # Standalone headers for References, Certificates
            p_t = doc.add_paragraph()
            p_t.paragraph_format.space_before = Pt(16)
            p_t.paragraph_format.space_after = Pt(14)
            p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
            rt = p_t.add_run(pdata['chapter_title'])
            rt.font.name = 'Times New Roman'
            rt.font.size = Pt(13)
            rt.font.bold = True

        for item in pdata.get("content", []):
            itype = item[0]
            
            if itype == "sec":
                p = doc.add_paragraph()
                p.paragraph_format.space_before = Pt(12)
                p.paragraph_format.space_after = Pt(4)
                r = p.add_run(sanitize_xml(item[1]))
                r.font.name = 'Times New Roman'
                r.font.size = Pt(11.5)
                r.font.bold = True
                
            elif itype == "subsec":
                p = doc.add_paragraph()
                p.paragraph_format.space_before = Pt(8)
                p.paragraph_format.space_after = Pt(3)
                r = p.add_run(sanitize_xml(item[1]))
                r.font.name = 'Times New Roman'
                r.font.size = Pt(11)
                r.font.bold = True
                r.font.italic = True
                
            elif itype == "p":
                p = doc.add_paragraph()
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(5)
                p.paragraph_format.line_spacing = 1.15
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p.paragraph_format.first_line_indent = Inches(0.4)
                r = p.add_run(sanitize_xml(item[1]))
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10.5)
                
            elif itype == "bullet":
                p = doc.add_paragraph(style='List Bullet')
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(3)
                p.paragraph_format.line_spacing = 1.15
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                if len(item) > 2 and item[2]:
                    r_pre = p.add_run(sanitize_xml(item[2]))
                    r_pre.font.name = 'Times New Roman'
                    r_pre.font.size = Pt(10.5)
                    r_pre.font.bold = True
                r = p.add_run(sanitize_xml(item[1]))
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10.5)
                
            elif itype == "math":
                p = doc.add_paragraph()
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(4)
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(sanitize_xml(item[1]))
                r.font.name = 'Cambria Math'
                r.font.size = Pt(10.5)
                r.font.italic = True
                
            elif itype == "img":
                img_file, fnum, fcap = item[1], item[2], item[3]
                img_path = os.path.join(IMG_DIR, img_file)
                if os.path.exists(img_path):
                    p_img = doc.add_paragraph()
                    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_img.paragraph_format.space_before = Pt(6)
                    p_img.paragraph_format.space_after = Pt(2)
                    doc.add_picture(img_path, width=Inches(6.2))
                    
                    p_cap = doc.add_paragraph()
                    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_cap.paragraph_format.space_before = Pt(2)
                    p_cap.paragraph_format.space_after = Pt(8)
                    rcap = p_cap.add_run(f"Fig {fnum} : {sanitize_xml(fcap)}")
                    rcap.font.name = 'Times New Roman'
                    rcap.font.size = Pt(9.5)
                    rcap.font.bold = False
                    
            elif itype == "table":
                tcaption, rows = item[1], item[2]
                tbl = doc.add_table(rows=len(rows), cols=len(rows[0]))
                tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
                for r_idx, rdata in enumerate(rows):
                    row = tbl.rows[r_idx]
                    for c_idx, cell_value in enumerate(rdata):
                        c = row.cells[c_idx]
                        set_cell_margins(c, top=80, bottom=80, left=100, right=100)
                        cp = c.paragraphs[0]
                        cp.paragraph_format.space_before = Pt(0)
                        cp.paragraph_format.space_after = Pt(0)
                        cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        rcell = cp.add_run(sanitize_xml(cell_value))
                        rcell.font.name = 'Times New Roman'
                        rcell.font.size = Pt(9)
                        if r_idx == 0:
                            set_cell_background(c, "0F172A")
                            rcell.font.bold = True
                            rcell.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                        else:
                            bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
                            set_cell_background(c, bg)
                p_tcap = doc.add_paragraph()
                p_tcap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_tcap.paragraph_format.space_before = Pt(3)
                p_tcap.paragraph_format.space_after = Pt(6)
                rtcap = p_tcap.add_run(sanitize_xml(tcaption))
                rtcap.font.name = 'Times New Roman'
                rtcap.font.size = Pt(9.5)
                
            elif itype == "paper":
                # Paper review: [num], title, authors, desc, setup, metrics, result, limit
                p_p = doc.add_paragraph()
                p_p.paragraph_format.space_before = Pt(8)
                p_p.paragraph_format.space_after = Pt(3)
                rtit = p_p.add_run(f"[{item[1]}] TITLE: {sanitize_xml(item[2])}\n")
                rtit.font.name = 'Times New Roman'
                rtit.font.size = Pt(10.5)
                rtit.font.bold = True
                
                rauth = p_p.add_run(f"AUTHORS: {sanitize_xml(item[3])}\n")
                rauth.font.name = 'Times New Roman'
                rauth.font.size = Pt(10)
                rauth.font.bold = True
                
                full_desc = f"DESCRIPTION: {item[4]} The dataset used was: {item[5]} Setup: {item[5]} Metrics: {item[6]}. Result: {item[7]} Limitation: {item[8]}"
                rdesc = p_p.add_run(sanitize_xml(full_desc))
                rdesc.font.name = 'Times New Roman'
                rdesc.font.size = Pt(10)
                
            elif itype == "ref":
                p_ref = doc.add_paragraph()
                p_ref.paragraph_format.space_before = Pt(1)
                p_ref.paragraph_format.space_after = Pt(3)
                p_ref.paragraph_format.line_spacing = 1.15
                rnum = p_ref.add_run(f"[{item[1]}] ")
                rnum.font.name = 'Times New Roman'
                rnum.font.size = Pt(9.5)
                rnum.font.bold = True
                rtxt = p_ref.add_run(sanitize_xml(item[2]))
                rtxt.font.name = 'Times New Roman'
                rtxt.font.size = Pt(9.5)


        # Hard page break after each page except page 50
        if page_num < 50:
            doc.add_page_break()

    doc.save(DOCX_OUT)
    print("DOCX successfully generated:", DOCX_OUT)
    print("DOCX File Size:", os.path.getsize(DOCX_OUT) / 1024, "KB")

def build_html():
    print("Building Print-Ready HTML...")
    html_lines = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "<meta charset='UTF-8'>",
        "<title>Coffee Yield Prediction and Loss Diagnosis Using Explainable AI - Major Project Report</title>",
        "<style>",
        "@page { size: A4; margin: 14mm 16mm 14mm 16mm; }",
        "body { font-family: 'Times New Roman', Times, serif; font-size: 10pt; line-height: 1.20; color: #000; margin: 0; padding: 0; }",
        ".page { page-break-after: always; break-after: page; width: 100%; height: 268mm; max-height: 268mm; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; overflow: hidden; }",
        ".page-header { display: flex; justify-content: space-between; border-bottom: 1px solid #777; padding-bottom: 3px; font-size: 9pt; color: #333; margin-bottom: 8pt; }",
        ".page-footer { display: flex; justify-content: space-between; border-top: 1px solid #777; padding-top: 3px; font-size: 9pt; margin-top: 8pt; }",
        ".page-content { flex-grow: 1; }",
        ".chap-num { font-size: 13pt; font-weight: bold; margin-top: 6pt; margin-bottom: 2pt; text-align: left; }",
        ".chap-title { font-size: 13pt; font-weight: bold; margin-top: 0; margin-bottom: 10pt; text-align: center; }",
        ".sec-title { font-size: 11pt; font-weight: bold; margin-top: 8pt; margin-bottom: 3pt; }",
        ".subsec-title { font-size: 10.5pt; font-weight: bold; font-style: italic; margin-top: 6pt; margin-bottom: 2pt; }",
        "p.body-text { text-align: justify; text-indent: 0.35in; margin-top: 0; margin-bottom: 4pt; }",
        "p.bullet-text { text-align: justify; margin-top: 0; margin-bottom: 2.5pt; padding-left: 0.2in; }",
        ".math-block { text-align: center; font-style: italic; margin: 4pt 0; font-size: 10pt; font-family: 'Cambria Math', serif; }",
        ".figure-container { text-align: center; margin: 4pt 0 2pt 0; }",
        ".figure-container img { max-width: 92%; max-height: 85mm; height: auto; border: 1px solid #CBD5E1; border-radius: 3px; }",
        ".figure-caption { text-align: center; font-size: 9pt; margin-top: 2pt; margin-bottom: 4pt; }",
        "table.data-table { width: 100%; border-collapse: collapse; margin: 4pt 0; font-size: 8.5pt; }",
        "table.data-table th, table.data-table td { border: 1px solid #CBD5E1; padding: 3pt 5pt; text-align: left; }",
        "table.data-table th { background-color: #0F172A; color: #FFFFFF; font-weight: bold; }",
        "table.data-table tr:nth-child(even) { background-color: #F8FAFC; }",
        ".table-caption { text-align: center; font-size: 8.5pt; margin-top: 2pt; margin-bottom: 4pt; font-weight: bold; }",
        ".paper-block { margin-top: 4pt; margin-bottom: 4pt; text-align: justify; }",
        ".paper-title { font-weight: bold; font-size: 10pt; }",
        ".paper-meta { font-weight: bold; font-size: 9.5pt; }",
        ".ref-line { font-size: 9pt; margin-bottom: 2.5pt; text-align: justify; }",
        "</style>",
        "</head>",
        "<body>"
    ]

    for page_num in range(1, 51):
        pdata = PAGES.get(page_num, {})
        html_lines.append(f"<div class='page' id='page-{page_num}'>")
        
        # Running Header
        html_lines.append("<div class='page-header'>")
        html_lines.append("<span>Coffee Yield Prediction and Loss Diagnosis Using Explainable AI</span>")
        html_lines.append("<span><b>2025-26</b></span>")
        html_lines.append("</div>")

        html_lines.append("<div class='page-content'>")
        if pdata.get("chapter") and page_num in [1, 5, 12, 17, 24, 31, 44]:
            html_lines.append(f"<div class='chap-num'>CHAPTER {pdata['chapter']}</div>")
            html_lines.append(f"<div class='chap-title'>{pdata['chapter_title']}</div>")
        elif pdata.get("chapter_title") and page_num in [47, 48, 49, 50]:
            html_lines.append(f"<div class='chap-title' style='margin-top:8pt;'>{pdata['chapter_title']}</div>")

        for item in pdata.get("content", []):
            itype = item[0]
            if itype == "sec":
                html_lines.append(f"<div class='sec-title'>{item[1]}</div>")
            elif itype == "subsec":
                html_lines.append(f"<div class='subsec-title'>{item[1]}</div>")
            elif itype == "p":
                html_lines.append(f"<p class='body-text'>{item[1]}</p>")
            elif itype == "bullet":
                pre = f"<b>{item[2]}</b> " if len(item) > 2 and item[2] else "• "
                html_lines.append(f"<p class='bullet-text'>{pre}{item[1]}</p>")
            elif itype == "math":
                html_lines.append(f"<div class='math-block'>{item[1]}</div>")
            elif itype == "img":
                img_file, fnum, fcap = item[1], item[2], item[3]
                img_path = os.path.join(IMG_DIR, img_file)
                html_lines.append("<div class='figure-container'>")
                html_lines.append(f"<img src='{img_path}' alt='{fcap}'>")
                html_lines.append(f"<div class='figure-caption'>Fig {fnum} : {fcap}</div>")
                html_lines.append("</div>")
            elif itype == "table":
                tcaption, rows = item[1], item[2]
                html_lines.append("<table class='data-table'>")
                html_lines.append("<thead><tr>")
                for c in rows[0]:
                    html_lines.append(f"<th>{c}</th>")
                html_lines.append("</tr></thead><tbody>")
                for row in rows[1:]:
                    html_lines.append("<tr>")
                    for c in row:
                        html_lines.append(f"<td>{c}</td>")
                    html_lines.append("</tr>")
                html_lines.append("</tbody></table>")
                html_lines.append(f"<div class='table-caption'>{tcaption}</div>")
            elif itype == "paper":
                html_lines.append("<div class='paper-block'>")
                html_lines.append(f"<div class='paper-title'>[{item[1]}] TITLE: {item[2]}</div>")
                html_lines.append(f"<div class='paper-meta'>AUTHORS: {item[3]}</div>")
                html_lines.append(f"<div><b>DESCRIPTION:</b> {item[4]} <b>The dataset used was:</b> {item[5]} <b>Setup:</b> {item[5]} <b>Metrics:</b> {item[6]}. <b>Result:</b> {item[7]} <b>Limitation:</b> {item[8]}</div>")
                html_lines.append("</div>")
            elif itype == "ref":
                html_lines.append(f"<div class='ref-line'><b>[{item[1]}]</b> {item[2]}</div>")

        html_lines.append("</div>") # End .page-content

        # Running Footer
        html_lines.append("<div class='page-footer'>")
        html_lines.append("<span><b>Dept of ISE, MCE</b></span>")
        html_lines.append(f"<span><b>{page_num}</b></span>")
        html_lines.append("</div>")

        html_lines.append("</div>") # End .page

    html_lines.append("</body></html>")

    with open(HTML_OUT, 'w', encoding='utf-8') as f:
        f.write("\n".join(html_lines))
    print("HTML successfully generated:", HTML_OUT)

def compile_pdf():
    print("Compiling PDF via Chrome Headless...")
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    
    cmd = [
        chrome_path,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        f'--print-to-pdf={PDF_OUT}',
        '--print-to-pdf-no-header',
        HTML_OUT
    ]

    subprocess.run(cmd, check=True)
    print("PDF successfully compiled:", PDF_OUT)
    print("PDF File Size:", os.path.getsize(PDF_OUT) / 1024, "KB")


def sync_artifacts():
    print("Syncing documents to brain artifact directory...")
    brain_docx = os.path.join(BRAIN_DIR, 'Coffee_Yield_Major_Project_Final_Report_50Pages.docx')
    brain_pdf = os.path.join(BRAIN_DIR, 'Coffee_Yield_Major_Project_Final_Report_50Pages.pdf')
    
    shutil.copy2(DOCX_OUT, brain_docx)
    shutil.copy2(PDF_OUT, brain_pdf)
    print("Synced to:", brain_docx)
    print("Synced to:", brain_pdf)

if __name__ == '__main__':
    build_docx()
    build_html()
    compile_pdf()
    sync_artifacts()
    print("All tasks completed successfully!")
