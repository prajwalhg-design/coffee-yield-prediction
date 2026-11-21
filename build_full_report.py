"""
build_full_report.py
--------------------
Generates the complete 50-page major project final report for:
"Coffee Yield Prediction and Loss Diagnosis Using Explainable AI"
Conforming strictly to the Department of Information Science and Engineering (ISE),
Malnad College of Engineering (MCE), Hassan - 573201 (Academic Year 2025-26).
Produces:
1. Coffee_Yield_Major_Project_Final_Report_50Pages.docx (Word Document with native headers/footers)
2. Coffee_Yield_Major_Project_Final_Report_50Pages.html (Print-ready HTML with CSS paged media)
3. Coffee_Yield_Major_Project_Final_Report_50Pages.pdf (Compiled PDF via Chrome Headless)
"""

import os
import subprocess
import shutil
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

BASE_DIR = r'C:\Users\prajw\.gemini\antigravity\scratch\coffee_yield_project'
IMG_DIR = os.path.join(BASE_DIR, 'report_images')
BRAIN_DIR = r'C:\Users\prajw\.gemini\antigravity\brain\8ddc1524-2d7e-4612-a363-58bd93735cf3'

print("Initializing 50-page thesis builder...")
