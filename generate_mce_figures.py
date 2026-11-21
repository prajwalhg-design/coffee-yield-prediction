"""
generate_mce_figures.py
-----------------------
Generates high-resolution architecture diagrams, workflow pipelines, and team identification
sheets conforming to the MCE Hassan reference style.
Team: POORVIK KR, PRAJWAL HG, VARUN KM, PRAJWAL D URS
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

img_dir = r'C:\Users\prajw\.gemini\antigravity\scratch\coffee_yield_project\report_images'
os.makedirs(img_dir, exist_ok=True)

# 1. Team Identification Sheet
def create_team_sheet():
    fig, ax = plt.subplots(figsize=(10, 8.5), dpi=200)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    # Border
    rect = patches.Rectangle((0.02, 0.02), 0.96, 0.96, fc='#FFFFFF', ec='#0F172A', lw=1.5)
    ax.add_patch(rect)

    # Header
    ax.text(0.5, 0.955, 'DEPARTMENT OF INFORMATION SCIENCE AND ENGINEERING', ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')
    ax.text(0.5, 0.925, 'MALNAD COLLEGE OF ENGINEERING, HASSAN – 573201', ha='center', va='center', fontsize=10.5, fontweight='bold', color='#0F172A')
    ax.text(0.5, 0.895, 'ACADEMIC YEAR 2026–27 | B.E. MAJOR PROJECT IDENTIFICATION SHEET', ha='center', va='center', fontsize=9, color='#475569')

    ax.text(0.5, 0.855, 'Coffee Yield Prediction and Loss Diagnosis Using Explainable AI', ha='center', va='center', fontsize=11.5, fontweight='bold', color='#1E3A8A')
    ax.text(0.5, 0.825, 'Guide: Mrs. Sindhu K S / Mrs. Divya H T, Assistant Professor', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#334155')

    # Table Header
    y_top = 0.77
    row_h = 0.14
    cols = [0.05, 0.11, 0.38, 0.58, 0.78, 0.95]
    
    # Header Row
    ax.fill_between([0.05, 0.95], y_top, y_top + 0.04, color='#0F172A')
    headers = ["SL NO", "STUDENT DETAILS", "CONTACT ADDRESS AT HASSAN", "PERMANENT ADDRESS", "PHOTO"]
    for i in range(len(headers)):
        cx = (cols[i] + cols[i+1]) / 2
        ax.text(cx, y_top + 0.02, headers[i], ha='center', va='center', fontsize=7.5, fontweight='bold', color='#FFFFFF')

    # Students data (4 team members)
    students = [
        ("1", "POORVIK KR\n4MC23IS075\nDOB: 14-06-2005\npoorvikkr@gmail.com", 
         "B T Kopplu\nHassan - 573201\nPh: +91 94812 55678", 
         "B T Kopplu\nHassan - 573201\nPh: +91 94812 55678", "#1E40AF", "P. KR"),
        ("2", "PRAJWAL HG\n4MC23IS070\nDOB: 28-02-2005\nprajwalkishan006@gmail.com", 
         "Kuvempunagar\nHassan - 573201\nPh: +91 91085 97495", 
         "Kuvempunagar\nHassan - 573201\nPh: +91 91085 97495", "#059669", "P. HG"),
        ("3", "VARUN KM\n4MC23IS085\nDOB: 19-09-2005\nvarunkm@gmail.com", 
         "Kuvempunagar\nHassan - 573201\nPh: +91 96328 53872", 
         "Kuvempunagar\nHassan - 573201\nPh: +91 96328 53872", "#D97706", "V. KM"),
        ("4", "PRAJWAL D URS\n4MC23IS072\nDOB: 11-11-2005\nprajwaldurs@gmail.com", 
         "M Hosakopplu\nHassan - 573201\nPh: +91 79758 73504", 
         "M Hosakopplu\nHassan - 573201\nPh: +91 79758 73504", "#7C3AED", "P. URS")
    ]

    for s_idx, (sl, details, contact, perm, col, init) in enumerate(students):
        y = y_top - (s_idx + 1) * row_h
        # Row outline
        r_box = patches.Rectangle((0.05, y), 0.90, row_h, fc='#FFFFFF', ec='#CBD5E1', lw=1)
        ax.add_patch(r_box)
        
        # Col dividers
        for cx in cols[1:-1]:
            ax.plot([cx, cx], [y, y + row_h], color='#CBD5E1', lw=1)

        # Content
        ax.text((cols[0] + cols[1])/2, y + row_h/2, sl, ha='center', va='center', fontsize=9, fontweight='bold')
        ax.text(cols[1] + 0.015, y + row_h/2, details, ha='left', va='center', fontsize=7.2, color='#0F172A')
        ax.text(cols[2] + 0.015, y + row_h/2, contact, ha='left', va='center', fontsize=7.2, color='#334155')
        ax.text(cols[3] + 0.015, y + row_h/2, perm, ha='left', va='center', fontsize=7.2, color='#334155')
        
        # Photo box
        p_card = patches.FancyBboxPatch((cols[4] + 0.02, y + 0.015), 0.13, row_h - 0.03, boxstyle="round,pad=0.01", fc=col, ec=col)
        ax.add_patch(p_card)
        ax.text(cols[4] + 0.085, y + row_h/2, f"STUDENT\n{init}\nPHOTO", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#FFFFFF')

    # Signatures
    y_sig = 0.08
    ax.text(0.18, y_sig, '_________________________\nSignature of Candidates\n(Poorvik, Prajwal HG, Varun, Urs)', ha='center', va='center', fontsize=7.5, fontweight='bold', color='#334155')
    ax.text(0.50, y_sig, '_________________________\nSignature of Guide\n(Mrs. Sindhu K S / Mrs. Divya H T)', ha='center', va='center', fontsize=7.5, fontweight='bold', color='#334155')
    ax.text(0.82, y_sig, '_________________________\nHead of the Department\nDept. of ISE, MCE Hassan', ha='center', va='center', fontsize=7.5, fontweight='bold', color='#334155')

    plt.tight_layout()
    path = os.path.join(img_dir, 'team_identification_sheet.png')
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

# 2. Publication Details Sheet
def create_publication_sheet():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=200)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    rect = patches.Rectangle((0.02, 0.02), 0.96, 0.96, fc='#FFFFFF', ec='#0F172A', lw=1.5)
    ax.add_patch(rect)

    ax.text(0.5, 0.92, 'DEPARTMENT OF INFORMATION SCIENCE AND ENGINEERING', ha='center', va='center', fontsize=11, fontweight='bold', color='#0F172A')
    ax.text(0.5, 0.86, 'MALNAD COLLEGE OF ENGINEERING, HASSAN – 573201', ha='center', va='center', fontsize=10.5, fontweight='bold', color='#0F172A')
    ax.text(0.5, 0.80, 'PROJECT PUBLICATION DETAILS, 2026–27', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#475569')

    # Table
    y_start = 0.73
    rows = [
        ("1", "Paper Title", "Coffee Yield Prediction and Loss Diagnosis Using Explainable AI"),
        ("2", "Authors", "1. Mrs. Sindhu K S / Mrs. Divya H T (Project Guide)\n2. Poorvik K R (4MC23IS075)\n3. Prajwal H G (4MC23IS070)\n4. Varun K M (4MC23IS085)\n5. Prajwal D Urs (4MC23IS072)"),
        ("3", "Conference Name", "ICDSIS-2027\n4th International Conference on Data Science and Information System"),
        ("4", "Name of Journal /\nConference / Proceedings", "4th International Conference on Data Science and Information System\n(ICDSIS-2027) / IEEE Conference Proceedings"),
        ("5", "Status of the Technical Paper", "Submitted / Under Review (Peer Review Track)")
    ]

    cur_y = y_start
    for sl, key, val in rows:
        h = 0.09 if sl in ["1", "5"] else 0.13
        r_box = patches.Rectangle((0.06, cur_y - h), 0.88, h, fc='#F8FAFC', ec='#CBD5E1', lw=1)
        ax.add_patch(r_box)
        ax.plot([0.12, 0.12], [cur_y - h, cur_y], color='#CBD5E1', lw=1)
        ax.plot([0.38, 0.38], [cur_y - h, cur_y], color='#CBD5E1', lw=1)
        
        ax.text(0.09, cur_y - h/2, sl, ha='center', va='center', fontsize=9, fontweight='bold')
        ax.text(0.14, cur_y - h/2, key, ha='left', va='center', fontsize=8.5, fontweight='bold', color='#1E293B')
        ax.text(0.40, cur_y - h/2, val, ha='left', va='center', fontsize=8.2, color='#0F172A')
        cur_y -= h

    plt.tight_layout()
    path = os.path.join(img_dir, 'publication_details_sheet.png')
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

# 3. Fig 4.5: Coffee Yield Prediction & Loss Diagnosis ML Workflow
def create_ml_workflow_fig():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    ax.text(0.5, 0.94, 'Coffee Yield Machine Learning & Explainability Workflow Pipeline', 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#0F172A')

    stages = [
        ("Multi-Modal Data\nIngestion", "3,500 Estate Records\n(Hassan, Kodagu,\nChikkamagaluru)", "#3B82F6"),
        ("Preprocessing &\nFeature Scaling", "Outlier Clamping,\nMedian Imputation,\n35 Agronomic Features", "#0D9488"),
        ("Tuned XGBoost\nRegression", "300 Trees, Depth 5,\nL1/L2 Regularization\nR²=0.9530, RMSE=71.36", "#16A34A"),
        ("TreeSHAP Local\nAttribution", "Exact Shapley Values,\nMarginal Feature Impact\nPolynomial-Time", "#9333EA"),
        ("Liebig Loss\nDiagnosis & Alerts", "Limiting Stress Bottleneck,\nSoil Acidity & Drought Triage,\nFlask API & Alerts", "#EA580C")
    ]

    for i, (title, desc, col) in enumerate(stages):
        x = 0.04 + i * 0.19
        p = patches.FancyBboxPatch((x, 0.28), 0.16, 0.54, boxstyle="round,pad=0.02", fc="#FFFFFF", ec=col, lw=1.8)
        ax.add_patch(p)
        hdr = patches.Rectangle((x, 0.64), 0.16, 0.18, fc=col, ec=col)
        ax.add_patch(hdr)
        ax.text(x + 0.08, 0.73, title, ha='center', va='center', fontsize=8, fontweight='bold', color='#FFFFFF')
        ax.text(x + 0.08, 0.46, desc, ha='center', va='center', fontsize=7.2, color='#1E293B')
        if i < 4:
            ax.annotate('', xy=(x + 0.19, 0.55), xytext=(x + 0.16, 0.55),
                        arrowprops=dict(arrowstyle="->", color="#64748B", lw=2))

    # Bottom summary box
    p_bot = patches.FancyBboxPatch((0.08, 0.06), 0.84, 0.14, boxstyle="round,pad=0.015", fc="#0F172A", ec="#0F172A")
    ax.add_patch(p_bot)
    ax.text(0.5, 0.13, 'Accurate, Data-Driven, and Explainable Coffee Yield Intelligence & Prescriptive Advisory', 
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#38BDF8')

    plt.tight_layout()
    path = os.path.join(img_dir, 'fig_4_5_coffee_ml_workflow.png')
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

# 4. Fig 4.6: Agronomic Suitability & Recommendation Workflow
def create_recommendation_workflow_fig():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')
    ax.axis('off')

    ax.text(0.5, 0.94, 'Soil-Climate Suitability & Agronomic Recommendation Workflow', 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#0F172A')

    boxes = [
        ("Soil & Climate Telemetry", "pH, N, P, K, Organic Carbon,\nBlossom Rain, Max/Min Temp", "#0284C7", 0.05, 0.45),
        ("Agronomic Threshold Engine", "CCRI Optimal Benchmarks\n& Liebig Deficiency Curves", "#0D9488", 0.37, 0.45),
        ("Prescriptive Calculus", "Lime Tonnes/ha = (5.8 - pH)*CEC*0.25\nSplit NPK Fertigation Schedules", "#16A34A", 0.69, 0.45),
        ("Foliar Disease Assessment", "Leaf Rust & White Stem Borer\nRisk Index Calculation", "#D97706", 0.21, 0.12),
        ("Automated Alerts & PDF", "Flask SMS/Email Alert Dispatch\n& Printable Field Advisory", "#E11D48", 0.53, 0.12)
    ]

    for title, desc, col, x, y in boxes:
        p = patches.FancyBboxPatch((x, y), 0.26, 0.32, boxstyle="round,pad=0.02", fc="#FFFFFF", ec=col, lw=1.8)
        ax.add_patch(p)
        hdr = patches.Rectangle((x, y + 0.20), 0.26, 0.12, fc=col, ec=col)
        ax.add_patch(hdr)
        ax.text(x + 0.13, y + 0.26, title, ha='center', va='center', fontsize=8, fontweight='bold', color='#FFFFFF')
        ax.text(x + 0.13, y + 0.10, desc, ha='center', va='center', fontsize=7.2, color='#1E293B')

    # Arrows
    ax.annotate('', xy=(0.37, 0.61), xytext=(0.31, 0.61), arrowprops=dict(arrowstyle="->", color="#475569", lw=1.5))
    ax.annotate('', xy=(0.69, 0.61), xytext=(0.63, 0.61), arrowprops=dict(arrowstyle="->", color="#475569", lw=1.5))
    ax.annotate('', xy=(0.34, 0.28), xytext=(0.34, 0.45), arrowprops=dict(arrowstyle="->", color="#475569", lw=1.5))
    ax.annotate('', xy=(0.53, 0.28), xytext=(0.47, 0.28), arrowprops=dict(arrowstyle="->", color="#475569", lw=1.5))

    plt.tight_layout()
    path = os.path.join(img_dir, 'fig_4_6_recommendation_workflow.png')
    plt.savefig(path, bbox_inches='tight')
    plt.close()
    print("Saved:", path)

if __name__ == '__main__':
    create_team_sheet()
    create_publication_sheet()
    create_ml_workflow_fig()
    create_recommendation_workflow_fig()
    print("All supplementary figures generated successfully!")
