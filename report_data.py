"""
report_data.py
--------------
Master compilation file containing all 54 pages of the Major Project Report:
"Coffee Yield Prediction and Loss Diagnosis Using Explainable AI"
Department of Information Science and Engineering
Malnad College of Engineering, Hassan – 573201
Academic Year 2026–27
Team: POORVIK KR, PRAJWAL HG, VARUN KM, PRAJWAL D URS
"""

import report_pages_ch1_to_ch3
import report_pages_ch4_to_ch5
import report_pages_ch6_to_ch7

PAGES = {}
PAGES.update(report_pages_ch1_to_ch3.CH1_TO_CH3_PAGES)
PAGES.update(report_pages_ch4_to_ch5.CH4_TO_CH5_PAGES)
PAGES.update(report_pages_ch6_to_ch7.CH6_TO_CH7_PAGES)

print(f"Loaded all {len(PAGES)} pages into report_data.py successfully!")
