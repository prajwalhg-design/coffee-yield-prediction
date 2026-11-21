"""
generate_full_50page_report.py
------------------------------
Generates a comprehensive, 50-page major project final report conforming to
the exact layout, chapter hierarchy, header/footer styling, and institutional
conventions of the Department of Information Science and Engineering (ISE),
Malnad College of Engineering (MCE), Hassan - 573201 (Academic Year 2025-26).
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def create_element(name):
    return OxmlElement(name)

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_header_footer(section):
    # Header: Project Name (Left) | Year 2025-26 (Right)
    header = section.header
    header_p = header.paragraphs[0]
    header_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    header_p.text = ""
    run_l = header_p.add_run("Coffee Yield Prediction and Loss Diagnosis Using Explainable AI")
    run_l.font.name = 'Times New Roman'
    run_l.font.size = Pt(9.5)
    run_l.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    
    # Tab to right
    run_tab = header_p.add_run("\t\t2025-26")
    run_tab.font.name = 'Times New Roman'
    run_tab.font.size = Pt(9.5)
    run_tab.font.bold = True
    
    # Add bottom border to header paragraph
    pPr = header_p._p.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="4" w:color="888888"/></w:pBdr>')
    pPr.append(pBdr)

    # Footer: Dept of ISE, MCE (Left) | Page Number (Right)
    footer = section.footer
    footer_p = footer.paragraphs[0]
    footer_p.text = ""
    run_dept = footer_p.add_run("Dept of ISE, MCE")
    run_dept.font.name = 'Times New Roman'
    run_dept.font.size = Pt(9.5)
    run_dept.font.bold = True
    
    # Tab to right for page number
    run_space = footer_p.add_run("\t\t")
    fld_simple = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
    footer_p._p.append(fld_simple)
    
    # Add top border to footer paragraph
    fpPr = footer_p._p.get_or_add_pPr()
    fpBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:top w:val="single" w:sz="6" w:space="4" w:color="888888"/></w:pBdr>')
    fpPr.append(fpBdr)

def format_heading1(doc, chapter_num, title):
    p_chap = doc.add_paragraph()
    p_chap.paragraph_format.space_before = Pt(18)
    p_chap.paragraph_format.space_after = Pt(6)
    p_chap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_c = p_chap.add_run(f"CHAPTER {chapter_num}\n")
    run_c.font.name = 'Times New Roman'
    run_c.font.size = Pt(14)
    run_c.font.bold = True
    
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(16)
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_t = p_title.add_run(title.upper())
    run_t.font.name = 'Times New Roman'
    run_t.font.size = Pt(14)
    run_t.font.bold = True
    return p_title

def format_heading2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = True
    return p

def format_heading3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.italic = True
    return p

def add_body_p(doc, text, indent=True):
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

def add_bullet_p(doc, text, bold_prefix=""):
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

def add_figure_box(doc, ascii_art, fig_num, caption):
    p_box = doc.add_paragraph()
    p_box.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_box.paragraph_format.space_before = Pt(10)
    p_box.paragraph_format.space_after = Pt(2)
    
    # Create framed box table
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.rows[0].cells[0]
    cell.width = Inches(6.5)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    p_cell = cell.paragraphs[0]
    p_cell.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_art = p_cell.add_run(ascii_art)
    run_art.font.name = 'Consolas'
    run_art.font.size = Pt(8.5)
    run_art.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    
    # Caption
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(4)
    p_cap.paragraph_format.space_after = Pt(12)
    run_cap = p_cap.add_run(f"Fig {fig_num} :{caption}")
    run_cap.font.name = 'Times New Roman'
    run_cap.font.size = Pt(10)
    run_cap.font.bold = False

print("Helper definitions initialized.")
