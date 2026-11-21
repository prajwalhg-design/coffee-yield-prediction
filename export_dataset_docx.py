"""
export_dataset_docx.py
----------------------
Generates a comprehensive, publication-grade Microsoft Word (.docx) document
for the Coffee Yield Prediction & Loss Diagnosis dataset.
Includes Dataset Metadata, Data Dictionary (all 35 attributes), Statistical Summary,
Representative Estate Observations, and Agronomic Benchmark Guidelines.
"""

import os
import pandas as pd
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def generate_word_document():
    base_dir = r'C:\Users\prajw\.gemini\antigravity\scratch\coffee_yield_project'
    brain_dir = r'C:\Users\prajw\.gemini\antigravity\brain\8ddc1524-2d7e-4612-a363-58bd93735cf3'
    csv_path = os.path.join(base_dir, 'data', 'coffee_dataset.csv')
    
    df = pd.read_csv(csv_path)
    doc = Document()
    
    # Page Margins (0.8 inches all around)
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)
        
    # Styles
    style_normal = doc.styles['Normal']
    font = style_normal.font
    font.name = 'Calibri'
    font.size = Pt(10.5)
    font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

    # -------------------------------------------------------------
    # DOCUMENT COVER HEADER
    # -------------------------------------------------------------
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(12)
    title_p.paragraph_format.space_after = Pt(4)
    run_title = title_p.add_run("Agro-Climatic Dataset & Codebook for Coffee Yield Prediction and Loss Diagnosis")
    run_title.font.size = Pt(22)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(0x0F, 0x20, 0x27)
    
    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(14)
    run_sub = sub_p.add_run("A Calibrated 3,500-Record Precision Agricultural Dataset for Machine Learning and Explainable AI (SHAP)")
    run_sub.font.size = Pt(13)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(0x05, 0x96, 0x69)

    meta_box = doc.add_paragraph()
    meta_box.paragraph_format.space_after = Pt(18)
    meta_box.add_run("Author: ").bold = True
    meta_box.add_run("Prajwal (prajwalhg-design)\n")
    meta_box.add_run("Email: ").bold = True
    meta_box.add_run("prajwalkishan006@gmail.com\n")
    meta_box.add_run("GitHub Repository: ").bold = True
    meta_box.add_run("https://github.com/prajwalhg-design/coffee-yield-prediction\n")
    meta_box.add_run("Benchmark Standards: ").bold = True
    meta_box.add_run("Central Coffee Research Institute (CCRI) & International Coffee Organization (ICO)")

    # -------------------------------------------------------------
    # SECTION 1: DATASET METADATA
    # -------------------------------------------------------------
    h1 = doc.add_heading("1. Dataset Overview & Scope", level=1)
    h1.style.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
    
    p1 = doc.add_paragraph(
        "This dataset comprises 3,500 comprehensive agro-climatic plantation profiles synthesized and calibrated against empirical field benchmarks from the Central Coffee Research Institute (CCRI) and regional agricultural directorates across Southern India (Kodagu/Coorg, Chikkamagaluru, Sakleshpur, Wayanad, Idukki, Nilgiris, Yercaud) and international reference zones (Minas Gerais, Brazil; Central Highlands, Vietnam). "
        "The dataset captures the multi-modal interaction between edaphic Soil Health Card test parameters, meteorological seasonal extremes, topographical elevation, and botanical variety (Coffea arabica vs. Coffea canephora). "
        "It includes both target harvest yields and granular ground-truth factor-wise loss breakdowns derived via Liebig's Law of the Minimum."
    )
    
    # Metadata Summary Table
    meta_table = doc.add_table(rows=6, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_rows = [
        ("Total Number of Observations (Rows)", f"{len(df):,} records"),
        ("Total Number of Attributes (Columns)", f"{df.shape[1]} features (Categorical + Numerical)"),
        ("Target Variable", "Yield_kg_per_Ha (Clean green coffee bean yield in kg/ha)"),
        ("Botanical Varieties", f"Arabica: {(df['Coffee_Species']=='Arabica').sum()} records | Robusta: {(df['Coffee_Species']=='Robusta').sum()} records"),
        ("Geographical Zones Covered", "9 distinct agro-ecological regions across Western Ghats and global belts"),
        ("Primary Machine Learning Task", "Non-linear multi-modal regression, feature attribution, and yield loss gap decomposition")
    ]
    for idx, (k, v) in enumerate(meta_rows):
        r = meta_table.rows[idx]
        c0, c1 = r.cells[0], r.cells[1]
        c0.text = k
        c0.paragraphs[0].runs[0].font.bold = True
        c1.text = v
        set_cell_background(c0, "F1F5F9" if idx % 2 == 0 else "FFFFFF")
        set_cell_background(c1, "F8FAFC" if idx % 2 == 0 else "FFFFFF")
        set_cell_margins(c0)
        set_cell_margins(c1)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # -------------------------------------------------------------
    # SECTION 2: COMPLETE DATA DICTIONARY (ALL 35 ATTRIBUTES)
    # -------------------------------------------------------------
    h2 = doc.add_heading("2. Complete Data Dictionary & Variable Schema", level=1)
    h2.style.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    doc.add_paragraph(
        "The table below details all 35 columns present in the dataset, including data types, measurement units, agronomic roles, and typical parameter distributions:"
    )

    columns_meta = [
        ("Coffee_Species", "String (Categorical)", "None", "Botanical coffee variety (Arabica or Robusta)."),
        ("Region", "String (Categorical)", "None", "Agro-ecological district / plantation zone."),
        ("Altitude_meters", "Float (Numeric)", "meters MSL", "Elevation above sea level; directly correlates with temperature lapse rates."),
        ("Avg_Temperature_C", "Float (Numeric)", "°C", "Mean annual ambient temperature (Arabica optimal: 18-23°C; Robusta: 23-28°C)."),
        ("Max_Temperature_C", "Float (Numeric)", "°C", "Summer peak temperature. Values >30°C induce floral abortion in Arabica."),
        ("Min_Temperature_C", "Float (Numeric)", "°C", "Winter minimum temperature. Values <10°C slow vegetative flush."),
        ("Annual_Rainfall_mm", "Float (Numeric)", "mm/year", "Cumulative annual precipitation (Optimal: 1500-2600 mm)."),
        ("Blossom_Rainfall_mm", "Float (Numeric)", "mm", "Pre-monsoon showers in Feb-April crucial for triggering floral anthesis."),
        ("Soil_pH", "Float (Numeric)", "pH scale (1:2.5)", "Active soil acidity. Values <5.0 induce aluminum toxicity and fix phosphorus."),
        ("Nitrogen_N", "Float (Numeric)", "kg/ha", "Available Nitrogen; essential for vegetative cropping wood and node formation."),
        ("Phosphorus_P", "Float (Numeric)", "kg/ha", "Available Phosphorus; stimulates feeder root development and blossom bud setting."),
        ("Potassium_K", "Float (Numeric)", "kg/ha", "Available Potassium; critical for berry expansion, bean weight, and drought resilience."),
        ("Organic_Carbon_pct", "Float (Numeric)", "%", "Soil organic matter percentage; governs cation exchange capacity and water holding."),
        ("Electrical_Conductivity_dS_m", "Float (Numeric)", "dS/m", "Measure of soluble salts and soil salinity index."),
        ("Relative_Humidity_pct", "Float (Numeric)", "%", "Mean relative atmospheric humidity."),
        ("Farm_Area_Hectares", "Float (Numeric)", "Hectares", "Total land area under coffee cultivation in hectares."),
        ("Farm_Area_Acres", "Float (Numeric)", "Acres", "Total land area converted to acres (1 ha = 2.47105 acres)."),
        ("Tree_Density_per_Ha", "Integer (Numeric)", "trees/ha", "Planting stand density (typically 1,000 to 2,500 bushes/ha)."),
        ("Yield_kg_per_Ha", "Float (Target)", "kg/ha", "Actual clean green coffee bean harvest yield per hectare (Main Prediction Target)."),
        ("Potential_Yield_kg_ha", "Float (Numeric)", "kg/ha", "Theoretical biological potential under ideal non-limiting conditions (1400/2100 kg/ha)."),
        ("Yield_Loss_kg_ha", "Float (Target)", "kg/ha", "Total yield gap below potential: (Potential_Yield - Actual_Yield)."),
        ("Yield_Efficiency_pct", "Float (Numeric)", "%", "Harvest realization rate: (Actual_Yield / Potential_Yield) * 100%."),
        ("Total_Yield_kg", "Float (Numeric)", "kg", "Total plantation harvest: (Yield_kg_per_Ha * Farm_Area_Hectares)."),
        ("Total_Yield_MT", "Float (Numeric)", "Metric Tonnes", "Total estate output in Metric Tonnes (Total_Yield_kg / 1,000)."),
        ("Primary_Loss_Factor", "String (Categorical)", "None", "The dominant environmental factor causing the highest yield penalty."),
        ("Secondary_Loss_Factor", "String (Categorical)", "None", "The second most limiting environmental factor."),
        ("Loss_pH_kg_ha", "Float (Numeric)", "kg/ha", "Attributed yield deduction caused by soil acidity / alkalinity stress."),
        ("Loss_Nitrogen_kg_ha", "Float (Numeric)", "kg/ha", "Attributed yield deduction caused by available Nitrogen deficit."),
        ("Loss_Phosphorus_kg_ha", "Float (Numeric)", "kg/ha", "Attributed yield deduction caused by available Phosphorus deficit."),
        ("Loss_Potassium_kg_ha", "Float (Numeric)", "kg/ha", "Attributed yield deduction caused by available Potassium deficit."),
        ("Loss_Rainfall_kg_ha", "Float (Numeric)", "kg/ha", "Attributed yield deduction caused by annual drought or excessive rain."),
        ("Loss_Blossom_kg_ha", "Float (Numeric)", "kg/ha", "Attributed yield deduction caused by blossom shower inadequacy."),
        ("Loss_Temperature_kg_ha", "Float (Numeric)", "kg/ha", "Attributed yield deduction caused by thermal heat or cold stress."),
        ("Loss_OrganicCarbon_kg_ha", "Float (Numeric)", "kg/ha", "Attributed yield deduction caused by depleted soil organic matter."),
        ("Loss_Altitude_kg_ha", "Float (Numeric)", "kg/ha", "Attributed yield deduction caused by elevation-species incompatibility.")
    ]

    dict_table = doc.add_table(rows=len(columns_meta) + 1, cols=4)
    dict_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Variable Name", "Data Type", "Unit", "Agronomic Role & Description"]
    
    # Format Header Row
    hdr_cells = dict_table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        hdr_cells[i].paragraphs[0].runs[0].font.bold = True
        set_cell_background(hdr_cells[i], "1E293B")
        hdr_cells[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_margins(hdr_cells[i])
        
    for idx, (col_name, dtype, unit, desc) in enumerate(columns_meta):
        row_cells = dict_table.rows[idx + 1].cells
        row_cells[0].text = col_name
        row_cells[0].paragraphs[0].runs[0].font.bold = True
        row_cells[1].text = dtype
        row_cells[2].text = unit
        row_cells[3].text = desc
        bg = "F8FAFC" if idx % 2 == 0 else "FFFFFF"
        for c in row_cells:
            set_cell_background(c, bg)
            set_cell_margins(c)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # -------------------------------------------------------------
    # SECTION 3: STATISTICAL SUMMARY
    # -------------------------------------------------------------
    h3 = doc.add_heading("3. Descriptive Statistical Summary", level=1)
    h3.style.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    doc.add_paragraph(
        "Parametric distribution metrics (Mean, Standard Deviation, Minimum, 25th percentile, Median, 75th percentile, Maximum) for key continuous variables across the 3,500 plantation records:"
    )

    numeric_cols = [
        "Altitude_meters", "Avg_Temperature_C", "Annual_Rainfall_mm", "Blossom_Rainfall_mm",
        "Soil_pH", "Nitrogen_N", "Phosphorus_P", "Potassium_K", "Organic_Carbon_pct",
        "Yield_kg_per_Ha", "Yield_Loss_kg_ha", "Yield_Efficiency_pct"
    ]
    
    stats_df = df[numeric_cols].describe().T[['mean', 'std', 'min', '25%', '50%', '75%', 'max']]
    stats_df = stats_df.round(2)

    stat_table = doc.add_table(rows=len(stats_df) + 1, cols=8)
    stat_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    s_headers = ["Attribute", "Mean", "Std Dev", "Min", "25%", "Median", "75%", "Max"]
    
    s_hdr_cells = stat_table.rows[0].cells
    for i, h in enumerate(s_headers):
        s_hdr_cells[i].text = h
        s_hdr_cells[i].paragraphs[0].runs[0].font.bold = True
        set_cell_background(s_hdr_cells[i], "0F766E")
        s_hdr_cells[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_margins(s_hdr_cells[i])

    for idx, (col_name, row_data) in enumerate(stats_df.iterrows()):
        cells = stat_table.rows[idx + 1].cells
        cells[0].text = col_name
        cells[0].paragraphs[0].runs[0].font.bold = True
        for c_idx, val in enumerate(row_data):
            cells[c_idx + 1].text = str(val)
        bg = "F0FDFA" if idx % 2 == 0 else "FFFFFF"
        for c in cells:
            set_cell_background(c, bg)
            set_cell_margins(c)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # -------------------------------------------------------------
    # SECTION 4: REPRESENTATIVE SAMPLE DATASET
    # -------------------------------------------------------------
    h4 = doc.add_heading("4. Representative Sample Observations", level=1)
    h4.style.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    doc.add_paragraph(
        "A selection of 6 representative plantation records illustrating distinct agro-ecological conditions (Optimal Arabica, Acidic Coorg Soil, Drought-stressed Sakleshpur, High-altitude Tamil Nadu, etc.):"
    )

    sample_cols = [
        "Coffee_Species", "Region", "Altitude_meters", "Avg_Temperature_C", "Annual_Rainfall_mm",
        "Soil_pH", "Potassium_K", "Yield_kg_per_Ha", "Yield_Loss_kg_ha", "Primary_Loss_Factor"
    ]
    sample_df = df[sample_cols].iloc[[0, 1, 15, 42, 108, 250]]

    samp_table = doc.add_table(rows=len(sample_df) + 1, cols=len(sample_cols))
    samp_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    s_cells = samp_table.rows[0].cells
    for i, col in enumerate(sample_cols):
        s_cells[i].text = col.replace("_", " ")
        s_cells[i].paragraphs[0].runs[0].font.bold = True
        s_cells[i].paragraphs[0].runs[0].font.size = Pt(8.5)
        set_cell_background(s_cells[i], "1E293B")
        s_cells[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_margins(s_cells[i])

    for r_idx, (_, row) in enumerate(sample_df.iterrows()):
        cells = samp_table.rows[r_idx + 1].cells
        for c_idx, val in enumerate(row):
            cells[c_idx].text = str(val)
            cells[c_idx].paragraphs[0].runs[0].font.size = Pt(8.5)
        bg = "F8FAFC" if r_idx % 2 == 0 else "FFFFFF"
        for c in cells:
            set_cell_background(c, bg)
            set_cell_margins(c)

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # -------------------------------------------------------------
    # SECTION 5: AGRONOMIC BENCHMARK GUIDE
    # -------------------------------------------------------------
    h5 = doc.add_heading("5. Agronomic Benchmark Reference Standards", level=1)
    h5.style.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    doc.add_paragraph(
        "Scientific thresholds utilized for biophysical transfer functions, stress curve calibration, and prescriptive advisory generation:"
    )

    bench_table = doc.add_table(rows=6, cols=3)
    bench_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    b_data = [
        ("Parameter", "Arabica (C. arabica)", "Robusta (C. canephora)"),
        ("Optimal Elevation", "1,000 to 1,600 meters MSL", "400 to 900 meters MSL"),
        ("Optimal Temperature Window", "18.0°C to 23.0°C (Critical Max: 30°C)", "23.0°C to 28.0°C (Critical Max: 34°C)"),
        ("Annual Precipitation", "1,500 to 2,200 mm/year", "1,800 to 2,600 mm/year"),
        ("Blossom Showers (Feb-Apr)", "25.0 to 45.0 mm required", "30.0 to 60.0 mm required"),
        ("Optimal Soil pH (1:2.5)", "5.80 to 6.50", "5.50 to 6.50")
    ]
    for idx, (p, a, r) in enumerate(b_data):
        cells = bench_table.rows[idx].cells
        cells[0].text = p
        cells[1].text = a
        cells[2].text = r
        if idx == 0:
            for c in cells:
                c.paragraphs[0].runs[0].font.bold = True
                set_cell_background(c, "0F766E")
                c.paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        else:
            cells[0].paragraphs[0].runs[0].font.bold = True
            bg = "F0FDFA" if idx % 2 == 0 else "FFFFFF"
            for c in cells:
                set_cell_background(c, bg)
        for c in cells:
            set_cell_margins(c)

    # Save to both project folder and brain artifacts
    docx_path = os.path.join(base_dir, 'Coffee_Yield_Agro_Climatic_Dataset.docx')
    brain_docx_path = os.path.join(brain_dir, 'Coffee_Yield_Agro_Climatic_Dataset.docx')
    
    doc.save(docx_path)
    doc.save(brain_docx_path)
    print(f"Word document successfully created at:\n{docx_path}\n{brain_docx_path}")
    print(f"File size: {os.path.getsize(docx_path) / 1024:.2f} KB")

if __name__ == '__main__':
    generate_word_document()
