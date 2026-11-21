"""
build_complete_major_report.py
------------------------------
Generates the comprehensive 45-50 page major project report for:
"Coffee Yield Prediction and Loss Diagnosis Using Explainable AI"
Department of Information Science and Engineering (ISE),
Malnad College of Engineering (MCE), Hassan - 573201 (2025-26).
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def setup_header_footer(section):
    header = section.header
    header_p = header.paragraphs[0]
    header_p.text = ""
    run_l = header_p.add_run("Coffee Yield Prediction and Loss Diagnosis Using Explainable AI")
    run_l.font.name = 'Times New Roman'
    run_l.font.size = Pt(9.5)
    run_l.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    
    run_tab = header_p.add_run("\t\t2025-26")
    run_tab.font.name = 'Times New Roman'
    run_tab.font.size = Pt(9.5)
    run_tab.font.bold = True
    
    pPr = header_p._p.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="4" w:color="888888"/></w:pBdr>')
    pPr.append(pBdr)

    footer = section.footer
    footer_p = footer.paragraphs[0]
    footer_p.text = ""
    run_dept = footer_p.add_run("Dept of ISE, MCE")
    run_dept.font.name = 'Times New Roman'
    run_dept.font.size = Pt(9.5)
    run_dept.font.bold = True
    
    footer_p.add_run("\t\t")
    fld_simple = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
    footer_p._p.append(fld_simple)
    
    fpPr = footer_p._p.get_or_add_pPr()
    fpBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:top w:val="single" w:sz="6" w:space="4" w:color="888888"/></w:pBdr>')
    fpPr.append(fpBdr)

def add_chap_heading(doc, chap_num, title):
    p_chap = doc.add_paragraph()
    p_chap.paragraph_format.space_before = Pt(20)
    p_chap.paragraph_format.space_after = Pt(4)
    run_c = p_chap.add_run(f"CHAPTER {chap_num}\n")
    run_c.font.name = 'Times New Roman'
    run_c.font.size = Pt(14)
    run_c.font.bold = True
    
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(18)
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_t = p_title.add_run(title.upper())
    run_t.font.name = 'Times New Roman'
    run_t.font.size = Pt(14)
    run_t.font.bold = True

def add_sec_heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = True

def add_subsec_heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.italic = True

def add_body(doc, text, indent=True):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.4)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)
    return p

def add_bullet(doc, text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)
    return p

def add_diagram(doc, ascii_content, fig_num, caption):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.rows[0].cells[0]
    cell.width = Inches(6.5)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(ascii_content)
    r.font.name = 'Consolas'
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(4)
    p_cap.paragraph_format.space_after = Pt(12)
    r_cap = p_cap.add_run(f"Fig {fig_num} :{caption}")
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(10)

def add_image_snapshot(doc, img_num, title, description, fig_ref):
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(4)
    r_t = p_title.add_run(f"Image {img_num} – {title}")
    r_t.font.name = 'Times New Roman'
    r_t.font.size = Pt(11)
    r_t.font.bold = True
    
    add_body(doc, description, indent=False)
    
    # Graphic box placeholder
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = tbl.rows[0].cells[0]
    c.width = Inches(6.5)
    set_cell_background(c, "0F172A")
    set_cell_margins(c, top=200, bottom=200, left=200, right=200)
    p_box = c.paragraphs[0]
    p_box.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_box = p_box.add_run(f"[ SCREENSHOT: {title.upper()} ]\nInteractive Clinical & Agronomic Viewport Rendered in Streamlit")
    r_box.font.name = 'Consolas'
    r_box.font.size = Pt(9.5)
    r_box.font.color.rgb = RGBColor(0x38, 0xBD, 0xF8)
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(4)
    p_cap.paragraph_format.space_after = Pt(14)
    r_cap = p_cap.add_run(f"Figure {fig_ref} {title}")
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(10)

print("Base layout helpers ready.")
