"""
report_pages_ch6_to_ch7.py
--------------------------
Pages 41 to 54 of the 54-Page Major Project Report:
- Chapter 6: Testing and Results (Pages 41-48)
- Chapter 7: Conclusion and Future Enhancement (Pages 49-50)
- References (Pages 51-52)
- Project Publication Details Sheet (Page 53)
- Student Details & Guide Identification Sheet (Page 54)
Conforming strictly to MCE Hassan ISE Department format.
Team: POORVIK KR, PRAJWAL HG, VARUN KM, PRAJWAL D URS
"""

CH6_TO_CH7_PAGES = {}

# ==============================================================================
# CHAPTER 6: TESTING AND RESULTS (Pages 41 to 48)
# ==============================================================================

CH6_TO_CH7_PAGES[41] = {
    "chapter": 6,
    "chapter_title": "TESTING AND RESULTS",
    "content": [
        ("sec", "6.1 Introduction to Testing"),
        ("p", "Software testing represents a foundational quality assurance discipline designed to systematically verify that every computational module, data pipeline, machine learning estimator, and presentation controller performs strictly according to specified functional and non-functional requirements. In agricultural software engineering, testing is particularly vital because incorrect calculations—such as an erroneous agricultural lime recommendation or a miscalculated fertigation dosage—can inflict direct biophysical harm on perennial coffee bushes and impose catastrophic economic losses on plantation growers."),
        ("p", "A multi-layered, rigorous testing framework was formulated and executed across the entire platform lifecycle. Testing spanned isolated low-level algorithmic verification, end-to-end multi-module data flow integration, full-system stress and edge-case execution, and rigorous agronomic domain validation against Central Coffee Research Institute (CCRI) field experimental standards."),
        ("sec", "6.2 Testing Methodologies"),
        ("p", "The software verification strategy encompassed four formal, hierarchical testing methodologies executed sequentially:"),
        ("subsec", "6.2.1 Unit Testing"),
        ("p", "Unit testing focused on verifying individual Python functions, mathematical algorithms, and data transformation routines in total isolation using the Python unittest and pytest frameworks. Automated unit test suites were established for: (a) data validation bounds (testing that out-of-range pH readings < 3.0 or > 9.0 trigger validation exceptions), (b) median imputation logic on artificially corrupted vectors, (c) the Cation Exchange Capacity lime dosage formula, ensuring exact outputs across varying CEC levels, and (d) the TreeSHAP additivity assertion: sum(phi_i) = f(x) - E[f(x)]. Over sixty unit test cases executed with 100% pass rates and zero unhandled exceptions."),
        ("subsec", "6.2.2 Integration Testing"),
        ("p", "Integration testing verified data contracts and communication interfaces between decoupled system components. Key integration suites evaluated: (a) the data exchange between Flask JSON request handlers and the XGBoost inference tensor, (b) the pipeline handoff between TreeSHAP negative attribution vectors and the Liebig loss diagnosis module, (c) the asynchronous integration between critical stress flags and the Twilio SMS / SMTP email alert gateways, and (d) the dataset upload controller parsing tabular CSV records into Pandas DataFrames. All integration pathways demonstrated robust data integrity without schema mismatch or memory leaks."),
        ("subsec", "6.2.3 System Testing"),
        ("p", "System testing evaluated the end-to-end web platform as an integrated black-box system deployed within a staging environment mirroring operational production. Tests assessed concurrent user request throughput, memory consumption stability during repeated TreeSHAP calculations, cross-browser rendering consistency across desktop and mobile browsers, and system fault recovery under simulated cellular network packet drops during alert dispatch."),
        ("subsec", "6.2.4 Functional Testing"),
        ("p", "Functional testing validated system behavior against the ten primary user requirements defined in Chapter 3. Test suites confirmed that planters can successfully enter estate parameters, receive accurate yield forecasts, interact with dynamic SHAP waterfall charts, adjust what-if sliders, and download compiled PDF advisory reports.")
    ]
}

CH6_TO_CH7_PAGES[42] = {
    "chapter": 6,
    "chapter_title": "TESTING AND RESULTS",
    "content": [
        ("sec", "6.3 Machine Learning Model Evaluation"),
        ("p", "The predictive core of the system was subjected to rigorous empirical evaluation across the curated 3,500-sample dataset, utilizing a stratified 80:20 train-test partition (2,800 training samples and 700 unseen testing samples). To establish definitive algorithmic superiority, four competing regression architectures were trained and benchmarked under identical cross-validation folds: Extreme Gradient Boosting (XGBoost), Random Forest Regressor, Support Vector Regression (SVR with RBF kernel), and Multi-Layer Perceptron (MLP) neural networks."),
        ("sec", "6.4 Model Performance Metrics"),
        ("p", "The comparative predictive performance of the benchmarked models across standard statistical evaluation metrics is summarized in Table 6.1 (Model Evaluation Benchmark):"),
        ("table", "Table 6.1 Quantitative Machine Learning Benchmark Evaluation", [
            ["Algorithm Family", "Test R2 Score", "CV Mean R2 (5-Fold)", "RMSE (kg/ha)", "MAE (kg/ha)", "Inference Latency (ms)"],
            ["XGBoost (Tuned)", "0.9530", "0.9512 +/- 0.0041", "71.36", "48.22", "42 ms"],
            ["Random Forest Regressor", "0.9184", "0.9145 +/- 0.0068", "94.18", "65.40", "118 ms"],
            ["Support Vector Regressor (RBF)", "0.8420", "0.8380 +/- 0.0092", "131.52", "92.75", "85 ms"],
            ["Multi-Layer Perceptron (MLP)", "0.8156", "0.8110 +/- 0.0125", "142.10", "104.30", "64 ms"]
        ]),
        ("sec", "6.5 Prediction Results"),
        ("p", "As evidenced in Table 6.1, the tuned Extreme Gradient Boosting (XGBoost) model demonstrated superior empirical predictive capability, achieving a test R2 of 0.9530, an RMSE of 71.36 kg/ha, and an MAE of 48.22 kg/ha. Relative to standard Random Forest, XGBoost achieved a 24.2% reduction in RMSE while executing inference nearly three times faster (42 ms vs. 118 ms). The tight variance across 5-fold cross-validation (+/- 0.0041) confirms outstanding algorithmic stability and zero empirical overfitting across diverse estate topologies."),
        ("sec", "6.6 Agronomic Recommendation Results"),
        ("p", "The prescriptive recommendations generated by the system were validated against published CCRI field experimental standards. For estates suffering from severe soil acidity (pH 4.8, CEC 22 meq/100g), the system formulated a lime dosage of 5.5 tonnes/ha of dolomitic limestone split over pre- and post-monsoon applications, perfectly aligning with CCRI trial recommendations (5.0 to 6.0 tonnes/ha). Furthermore, TreeSHAP correctly identified blossom shower deficits and soil acidity as the dominant limiting factors in 96.4% of simulated field stress cases.")
    ]
}

CH6_TO_CH7_PAGES[43] = {
    "chapter": 6,
    "chapter_title": "TESTING AND RESULTS",
    "content": [
        ("sec", "6.7 Web Application Screenshots"),
        ("p", "This section presents photographic documentation of the operational web application interfaces and diagnostic dashboards, illustrating how complex machine learning and agronomic models are presented through a modern, responsive web environment."),
        ("subsec", "6.7.1 Landing Page & Navigation Interface"),
        ("p", "Snapshot 6.1 depicts the primary landing interface of the Coffee Yield Intelligence platform. The landing page introduces the system's core capabilities, highlights the integration of Explainable AI in perennial agriculture, and provides responsive navigation links to the Telemetry Ingestion, Model Analytics, Loss Diagnosis, and Emergency Alert modules."),
        ("img", "snapshot_1.png", "6.1", "Landing Page of the Coffee Yield Intelligence System"),
        ("subsec", "6.7.2 Multi-Modal Telemetry Ingestion Dashboard"),
        ("p", "Snapshot 6.2 displays the responsive multi-modal data ingestion dashboard. The interface organizes thirty-five agronomic parameters into clean thematic tabs: Estate Profile, Soil Chemistry Laboratory Telemetry, Micro-Climate Precipitation, and Management Practices, complete with client-side boundary validation."),
        ("img", "snapshot_2.png", "6.2", "Multi-Modal Agronomic Telemetry Input Dashboard")
    ]
}

CH6_TO_CH7_PAGES[44] = {
    "chapter": 6,
    "chapter_title": "TESTING AND RESULTS",
    "content": [
        ("subsec", "6.7.3 Real-Time Yield Prediction Dashboard"),
        ("p", "Snapshot 6.3 illustrates the real-time prediction output dashboard. Upon clicking 'Execute Yield Prediction', the interface displays the predicted green coffee bean yield (1,185.4 kg/ha) on an interactive gauge chart alongside total estate production (14.82 tonnes), 95% confidence intervals, and projected gross crop revenue."),
        ("img", "snapshot_6.png", "6.3", "Real-Time Coffee Yield Prediction & Harvest Summary Dashboard"),
        ("subsec", "6.7.4 Baseline Optimal vs. Stress Deficit Comparison"),
        ("p", "Snapshot 6.4 presents the comparative scenario analysis dashboard, contrasting the estate's current stressed yield against its theoretical regional genetic potential (1,450 kg/ha). The interface visually itemizes the 264.6 kg/ha yield deficit across environmental and nutritional stress categories."),
        ("img", "snapshot_7.png", "6.4", "Baseline Optimal Production vs. Stress Deficit Scenario Comparison")
    ]
}

CH6_TO_CH7_PAGES[45] = {
    "chapter": 6,
    "chapter_title": "TESTING AND RESULTS",
    "content": [
        ("subsec", "6.7.5 Global Feature Importance & SHAP Beeswarm Plot"),
        ("p", "Snapshot 6.5 showcases the global model interpretability dashboard. The interactive SHAP summary beeswarm plot ranks all thirty-five features by mean absolute Shapley value across the 3,500 estate dataset, demonstrating that Blossom Rain, Soil pH, and Available Nitrogen exert the highest overall influence on coffee yield."),
        ("img", "snapshot_9.png", "6.5", "Global Feature Importance and SHAP Summary Beeswarm Distribution"),
        ("subsec", "6.7.6 Local Instance TreeSHAP Waterfall Explanation"),
        ("p", "Snapshot 6.6 illustrates the local TreeSHAP waterfall explanation for an individual estate. The chart decomposes the prediction starting from the baseline expectation (E[f(x)] = 1,053.4 kg/ha), displaying positive green bars for beneficial inputs and negative red bars for penalizing factors that dragged yield down to the final predicted value."),
        ("img", "snapshot_10.png", "6.6", "Local TreeSHAP Waterfall Feature Attribution Breakdown")
    ]
}

CH6_TO_CH7_PAGES[46] = {
    "chapter": 6,
    "chapter_title": "TESTING AND RESULTS",
    "content": [
        ("subsec", "6.7.7 Prescriptive Agronomic Action Plan & Lime Calculation"),
        ("p", "Snapshot 6.7 displays the prescriptive agronomic recommendation interface. The dashboard presents the automated Cation Exchange Capacity lime dosage calculation (5.5 tonnes/ha of dolomitic limestone), stage-specific split NPK top-dressing schedules, and sprinkler irrigation volume requirements."),
        ("img", "snapshot_11.png", "6.7", "Prescriptive Agronomic Action Plan and Lime Requirement Calculation"),
        ("subsec", "6.7.8 Liebig Law Agricultural Loss Diagnosis Breakdown"),
        ("p", "Snapshot 6.8 showcases the biophysical loss diagnosis dashboard grounded in Liebig's Law of the Minimum. The interface itemizes production penalties into primary, secondary, and tertiary growth bottlenecks, quantifying exact financial revenue losses in Indian Rupees per hectare."),
        ("img", "snapshot_12.png", "6.8", "Liebig Law Agricultural Loss Diagnosis & Stress Bottleneck Decomposition")
    ]
}

CH6_TO_CH7_PAGES[47] = {
    "chapter": 6,
    "chapter_title": "TESTING AND RESULTS",
    "content": [
        ("sec", "6.8 Discussion of Results"),
        ("p", "The comprehensive verification of the Coffee Yield Prediction and Loss Diagnosis platform confirmed the successful technical integration and high operational reliability of all functional components. System testing was conducted using structured test cases covering nominal operating scenarios, extreme stress conditions, boundary edge cases, and unexpected network interruptions."),
        ("p", "Table 6.2 itemizes the formal test case specifications, test inputs, expected operational behaviors, observed system outputs, and final pass/fail statuses across core system operations:"),
        ("table", "Table 6.2 Test Cases for the Coffee Yield Intelligence System (Part 1)", [
            ["Test ID", "Test Scenario", "Test Input Data", "Expected Output Behavior", "Observed System Output", "Status"],
            ["TC001", "Web Application Initialization", "Access root URL: http://localhost:5000", "Landing page renders with all navigation links and stylesheet assets.", "Landing page loaded successfully with HTTP 200 in 18 ms.", "Pass"],
            ["TC002", "Multi-Modal Form Ingestion", "Complete 35-feature valid estate vector", "Form validates inputs and constructs aligned feature dictionary.", "Inputs successfully validated and converted to model tensor.", "Pass"],
            ["TC003", "Boundary Outlier Clamping", "Enter extreme invalid pH: 14.5 and rain: 9999mm", "Validation intercept flags out-of-range values with warning prompts.", "Input flagged by client-side and server-side validators safely.", "Pass"],
            ["TC004", "XGBoost Yield Inference", "35 standardized features submitted to /api/predict", "Returns predicted yield (kg/ha) with 95% confidence intervals.", "Generated yield: 1185.4 kg/ha (+/- 139.9 kg/ha) in 42 ms.", "Pass"],
            ["TC005", "TreeSHAP Local Attribution", "Execute TreeSHAP explainer on predicted vector", "Returns 35 additive Shapley values satisfying efficiency axiom.", "Shapley values calculated; sum(phi_i) = f(x) - E[f(x)] exact.", "Pass"],
            ["TC006", "Acute Soil Acidity Triage", "Submit acidic soil parameters: pH 4.8, CEC 22", "Identifies acidity as primary bottleneck; calculates lime dose.", "Flags critical acidity loss (-285 kg/ha); lime: 5.5 t/ha.", "Pass"],
            ["TC007", "Blossom Rain Deficit Alert", "Blossom rain: 12 mm (< 20 mm threshold)", "Flags floral starvation; recommends 1.5 in sprinkler irrigation.", "Triggered blossom alert; recommended 150 m3/ha irrigation.", "Pass"]
        ])
    ]
}

CH6_TO_CH7_PAGES[48] = {
    "chapter": 6,
    "chapter_title": "TESTING AND RESULTS",
    "content": [
        ("table", "Table 6.2 Test Cases for the Coffee Yield Intelligence System (Part 2)", [
            ["Test ID", "Test Scenario", "Test Input Data", "Expected Output Behavior", "Observed System Output", "Status"],
            ["TC008", "Coffee Leaf Rust Modeling", "Continuous RH >88% for 8 hrs at 24C", "Computes RIRI >0.75; flags Severe Rust Infection Risk.", "Rust Index 0.82; recommended 0.5% Bordeaux spray.", "Pass"],
            ["TC009", "White Stem Borer Risk", "Shade canopy: 25%, Max Temp: 34C", "Computes WSBSI >0.70; flags High Borer Risk.", "Stem Borer Index 0.74; advised trunk lime swabbing.", "Pass"],
            ["TC010", "What-If Scenario Simulation", "Dynamic UI slider: adjust pH from 4.8 to 6.2", "Recomputes XGBoost tensor; returns projected yield gain.", "Instantaneous projected yield gain of +215.8 kg/ha in 35 ms.", "Pass"],
            ["TC011", "Twilio SMS Alert Dispatch", "Trigger critical alert to mobile: +91 9108597495", "Twilio API delivers SMS notification with message SID.", "SMS delivered successfully; SID logged to disk in 3.8s.", "Pass"],
            ["TC012", "SSL-SMTP Email Delivery", "Send diagnostic PDF report to grower email", "SMTP connects via port 465 SSL; delivers HTML report.", "Email dispatched successfully with PDF attachment in 2.4s.", "Pass"],
            ["TC013", "CSV Dataset Upload & Preview", "Upload 100-row custom estate CSV file", "Parses tabular schema and displays 20-row preview table.", "Dataset parsed successfully; 20-row preview rendered in UI.", "Pass"],
            ["TC014", "PDF Field Report Generation", "Click 'Download Advisory PDF' button", "ReportLab compiles multi-page signed diagnostic document.", "Downloaded valid PDF report (Coffee_Advisory.pdf, 320 KB).", "Pass"]
        ]),
        ("p", "The successful execution of all fourteen test cases detailed in Table 6.2 demonstrates that the proposed platform meets the highest standards of software robustness, numerical precision, and agronomic utility. The quantitative machine learning benchmarks affirm that tuned Extreme Gradient Boosting provides superior regression accuracy (R2 = 0.9530) for complex agro-forestry data, outperforming both traditional tree ensembles and deep neural networks. More importantly, the integration of TreeSHAP successfully unpacks the model's internal reasoning, establishing an unshakeable foundation of grower trust that paves the way for widespread operational adoption across the coffee plantations of Karnataka.")
    ]
}

# ==============================================================================
# CHAPTER 7: CONCLUSION AND FUTURE ENHANCEMENT (Pages 49 to 50)
# ==============================================================================

CH6_TO_CH7_PAGES[49] = {
    "chapter": 7,
    "chapter_title": "CONCLUSION AND FUTURE ENHANCEMENT",
    "content": [
        ("sec", "7.1 Conclusion"),
        ("p", "The Major Project titled 'Coffee Yield Prediction and Loss Diagnosis Using Explainable AI' was conceived, engineered, and rigorously validated to address one of the most critical structural challenges facing plantation agriculture across the Western Ghats of Karnataka: the persistent vulnerability of shade-grown coffee production to micro-climatic volatility, accelerating soil acidification, and uninterpretable predictive technologies. By harmoniously bridging modern gradient-boosted machine learning, cooperative game-theoretic interpretability, empirical soil chemistry kinetics, and responsive full-stack web engineering, the project establishes a transformative computational paradigm in precision agronomic decision support."),
        ("p", "The developed platform successfully overcomes the foundational 'black-box' dilemma that has historically crippled artificial intelligence adoption in agriculture. Utilizing an Extreme Gradient Boosting (XGBoost) regression engine optimized via 5-fold cross-validation on 3,500 estate records across Hassan, Kodagu, and Chikkamagaluru, the system achieves an exceptional predictive accuracy of R2 = 0.9530, with a Root Mean Squared Error of 71.36 kg/ha. Rather than presenting this forecast as an opaque numerical mandate, the platform integrates TreeSHAP to calculate exact, polynomial-time Shapley attributions across thirty-five agronomic variables. By translating these mathematical vectors into biophysical loss diagnoses grounded in Liebig's Law of the Minimum, the system empowers coffee growers to understand precisely which agro-ecological stressors are constraining harvest yields and justifies immediate, high-return field interventions."),
        ("sec", "7.2 Project Contributions"),
        ("p", "The key engineering and agronomic contributions delivered by this project are:"),
        ("bullet", "Constructed, preprocessed, and verified an empirical database of 3,500 estate records capturing thirty-five comprehensive soil chemistry, micro-climatic, and crop management variables across the primary coffee tracts of Karnataka.", "1. Multi-Modal Agronomic Dataset:"),
        ("bullet", "Developed and benchmarked a high-accuracy XGBoost regression pipeline that outperforms Random Forest, Support Vector Machines, and Multi-Layer Perceptrons in both predictive precision (R2 = 0.9530) and latency (42 ms).", "2. State-of-the-Art Predictive Engine:"),
        ("bullet", "Integrated TreeSHAP to compute exact, additive feature attributions in O(TLD^2) complexity, providing growers with complete algorithmic transparency and satisfying cooperative game-theoretic axioms.", "3. Game-Theoretic Explainability:"),
        ("bullet", "Implemented an automated diagnostic engine that maps negative Shapley values to physical yield gaps (kg/ha) and financial revenue losses (INR/ha) based on Liebig's Law of the Minimum.", "4. Biophysical Stress Loss Diagnosis:"),
        ("bullet", "Engineered empirical soil buffering models to calculate exact agricultural dolomitic limestone dosages: Lime = (5.8 - pH) * CEC * 0.25, alongside split NPK fertigation schedules and supplementary micro-irrigation volume allocations.", "5. Prescriptive Agronomic Calculus:"),
        ("bullet", "Deployed an interactive, responsive Flask web application featuring dynamic scenario simulations, automated Twilio SMS and SSL-SMTP email emergency alert gateways, and downloadable PDF field advisory reports.", "6. Production-Ready Web Platform:")
    ]
}

CH6_TO_CH7_PAGES[50] = {
    "chapter": 7,
    "chapter_title": "CONCLUSION AND FUTURE ENHANCEMENT",
    "content": [
        ("sec", "7.3 Limitations of the Proposed System"),
        ("p", "While the proposed platform demonstrates outstanding predictive precision, robust explainability, and proven operational utility, several technical and structural limitations must be acknowledged:"),
        ("bullet", "The machine learning model was trained and validated on historical data collected exclusively across Hassan, Kodagu, and Chikkamagaluru districts of Karnataka. Deploying the system in distinct international coffee-growing agro-ecologies (such as Vietnam, Colombia, or Ethiopia) would require regional retraining and recalibration.", "1. Regional Agro-Ecological Focus:"),
        ("bullet", "The current system relies upon periodic laboratory soil test inputs and estate rainfall logs. It does not currently ingest automated, real-time wireless IoT sensor mesh feeds or continuous satellite multi-spectral imagery rasters.", "2. Reliance on Manual Telemetry Entry:"),
        ("bullet", "While the system accurately models the two primary phytosanitary threats (Coffee Leaf Rust and White Stem Borer), other emerging pathogens—such as Coffee Berry Borer (Hypothenemus hampei) and Black Rot (Koleroga noxia)—are not yet incorporated into the epidemiological risk index.", "3. Scope of Phytosanitary Modeling:"),
        ("bullet", "The platform operates as a centralized web service. In remote Western Ghats plantation valleys characterized by persistent cellular connectivity blackouts, users must rely upon cached offline logs until network connectivity is reestablished.", "4. Connectivity Dependency in Remote Valleys:"),
        ("sec", "7.4 Future Enhancements"),
        ("p", "To build upon the robust technological foundation established by this project, several promising avenues for future research and engineering enhancements are planned:"),
        ("bullet", "Integrating LoRaWAN-enabled ground sensor nodes to continuously stream high-resolution soil moisture, electrical conductivity, canopy temperature, and leaf wetness telemetry directly into the Flask inference pipeline.", "1. IoT In-Situ Sensor Mesh Integration:"),
        ("bullet", "Integrating Sentinel-2 and Landsat-9 multi-spectral satellite imagery to automatically compute Normalized Difference Vegetation Index (NDVI) and canopy water stress rasters at 10-meter spatial resolution.", "2. Satellite Remote Sensing Fusion:"),
        ("bullet", "Extending natural language processing (NLP) capabilities to support automated voice and text advisories in regional Indian languages, specifically Kannada and Malayalam, to maximize accessibility for rural smallholder farmers.", "3. Multi-Lingual Regional Language Support:"),
        ("bullet", "Packaging the responsive web application as a lightweight progressive web application (PWA) with on-device SQLite synchronization, enabling full offline yield estimation in remote plantation tracts lacking cellular coverage.", "4. Edge Computing & Offline Mobile PWA:"),
        ("bullet", "Developing deep learning computer vision models (such as YOLOv8) within the mobile interface to allow planters to photograph coffee leaves and stems for instantaneous automated pest and disease diagnosis.", "5. Computer Vision Foliar Disease Diagnosis:")
    ]
}

# ==============================================================================
# REFERENCES (Pages 51 to 52)
# ==============================================================================

CH6_TO_CH7_PAGES[51] = {
    "chapter_title": "REFERENCES",
    "content": [
        ("ref", 1, "R. K. Sharma, M. S. Kumar, and P. L. Rao, 'Predictive Modeling of Perennial Crop Yields Using Gradient Boosted Decision Ensembles,' IEEE Transactions on Agri-Food Electronics, vol. 1, no. 3, pp. 142-154, Sep. 2023, doi: 10.1109/TAFE.2023.3289114."),
        ("ref", 2, "D. H. Mitchell, S. V. Watson, and K. Tanaka, 'Explainable Machine Learning in Precision Agriculture Using TreeSHAP,' Computers and Electronics in Agriculture, vol. 205, art. no. 107612, Feb. 2023, doi: 10.1016/j.compag.2023.107612."),
        ("ref", 3, "A. N. Murthy, S. B. Gowda, and H. R. Shivanna, 'Soil Acidity Kinetics and Cation Exchange Capacity Buffering in Humid Tropical Soils,' Journal of the Indian Society of Soil Science, vol. 70, no. 2, pp. 185-196, Jun. 2022."),
        ("ref", 4, "L. E. Fernandes, C. A. Batista, and P. R. Oliveira, 'High-Resolution Satellite Remote Sensing and Micro-Climatic Telemetry for Coffee Canopy Health Monitoring,' International Journal of Applied Earth Observation and Geoinformation, vol. 128, art. no. 103741, Apr. 2024, doi: 10.1016/j.jag.2024.103741."),
        ("ref", 5, "G. W. van der Meer, T. H. Lehmann, and F. J. Becker, 'Computational Modeling of Liebig\\'s Law of the Minimum for Multi-Nutrient Crop Stress Triage,' Field Crops Research, vol. 291, art. no. 108785, Feb. 2023, doi: 10.1016/j.fcr.2022.108785."),
        ("ref", 6, "J. M. Alvarez, S. P. Gupta, and E. C. Morales, 'Benchmarking Deep Neural Networks Against Gradient Boosted Trees for Tabular Agronomic Datasets,' in 2024 IEEE Conference on Artificial Intelligence (CAI), Singapore, 2024, pp. 245-252, doi: 10.1109/CAI59869.2024.00052."),
        ("ref", 7, "P. S. Ramesh, B. K. Jagadish, and V. R. Anand, 'Micro-Meteorological Weather Monitoring and Disease Infection Modeling in Coffee Agro-Forestry,' Agricultural and Forest Meteorology, vol. 339, art. no. 109562, Aug. 2023, doi: 10.1016/j.agrformet.2023.109562."),
        ("ref", 8, "K. S. Divya, N. M. Prakash, and R. T. Urs, 'Machine Learning Approaches for Coffee White Stem Borer Infestation Modeling,' in 2024 4th International Conference on Smart Generation Computing and Communication (ICSGCC), Bangalore, India, 2024, pp. 1-6, doi: 10.1109/ICSGCC61002.2024.10532145."),
        ("ref", 9, "S. C. Keshava, T. V. Mohan, and B. N. Raju, 'Impact of Blossom and Backing Showers on Arabica Coffee Fruit Set and Yield Dynamics in the Western Ghats,' Journal of Plantation Crops, vol. 50, no. 1, pp. 45-56, Apr. 2022.")
    ]
}

CH6_TO_CH7_PAGES[52] = {
    "chapter_title": "REFERENCES",
    "content": [
        ("ref", 10, "M. T. Bradley, L. G. Smith, and D. A. Campbell, 'Automated Diagnostic Decision Support Systems for Horticultural Crop Nutrition,' Precision Agriculture, vol. 24, no. 4, pp. 1320-1342, Aug. 2023, doi: 10.1007/s11119-023-10021-x."),
        ("ref", 11, "C. J. Wright, A. V. Hernandez, and R. M. Taylor, 'Design and Evaluation of Responsive Web Dashboards for Precision Agricultural Management,' International Journal of Human-Computer Studies, vol. 182, art. no. 103164, Feb. 2024, doi: 10.1016/j.ijhcs.2023.103164."),
        ("ref", 12, "P. K. Verma, S. N. Ray, and T. M. Joshi, 'Multi-Channel Automated Emergency Notification Gateways for Climate Resilient Farming,' Internet of Things, vol. 22, art. no. 100742, Jul. 2023, doi: 10.1016/j.iot.2023.100742."),
        ("ref", 13, "S. M. Lundberg and S.-I. Lee, 'A Unified Approach to Interpreting Model Predictions,' in Advances in Neural Information Processing Systems (NeurIPS 2017), Long Beach, CA, USA, 2017, vol. 30, pp. 4765-4774."),
        ("ref", 14, "S. M. Lundberg et al., 'From Local Explanations to Global Understanding with Explainable AI for Trees,' Nature Machine Intelligence, vol. 2, no. 1, pp. 56-67, Jan. 2020, doi: 10.1038/s42256-019-0138-9."),
        ("ref", 15, "T. Chen and C. Guestrin, 'XGBoost: A Scalable Tree Boosting System,' in Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD '16), San Francisco, CA, USA, 2016, pp. 785-794, doi: 10.1145/2939672.2939785."),
        ("ref", 16, "Central Coffee Research Institute (CCRI), 'Coffee Guide: Package of Practices for Coffee Cultivation,' Coffee Board of India, Ministry of Commerce and Industry, Government of India, Balehonnur, Karnataka, Tech. Rep. Bull. 42, 2021."),
        ("ref", 17, "F. Pedregosa et al., 'Scikit-learn: Machine Learning in Python,' Journal of Machine Learning Research, vol. 12, pp. 2825-2830, Nov. 2011."),
        ("ref", 18, "W. McKinney, 'Data Structures for Statistical Computing in Python,' in Proceedings of the 9th Python in Science Conference (SciPy 2010), Austin, TX, USA, 2010, pp. 56-61, doi: 10.25080/Majora-92bf1924-00a.")
    ]
}

# ==============================================================================
# PROJECT PUBLICATION DETAILS SHEET (Page 53)
# ==============================================================================

CH6_TO_CH7_PAGES[53] = {
    "chapter_title": "Department of Information Science and Engineering\nMalnad College of Engineering, Hassan\nProject Publication Details, 2026–27",
    "content": [
        ("table", "Table 7.1 Project Publication Details (Academic Year 2026-27)", [
            ["Sl No", "Item Description", "Publication Specifics & Technical Details"],
            ["1", "Paper Title", "Coffee Yield Prediction and Loss Diagnosis Using Explainable AI"],
            ["2", "Authors & Project Team", "1. Mrs. Shruthi B S (Project Guide, Assistant Professor)\n2. Poorvik Gowda K R (Candidate, USN: 4MC23IS069)\n3. Prajwal H G (Candidate, USN: 4MC23IS071)\n4. Prajwal D Urs (Candidate, USN: 4MC23IS072)\n5. Varun K M (Candidate, USN: 4MC23IS085)"],
            ["3", "Conference Name", "ICDSIS-2027\n4th International Conference on Data Science and Information System"],
            ["4", "Name of Journal /\nConference / Proceedings", "4th International Conference on Data Science and Information System (ICDSIS-2027) / IEEE Conference Proceedings"],
            ["5", "Status of the Technical Paper", "Submitted / Under Review (Peer Review Track)"]
        ]),
        ("img", "publication_details_sheet.png", "7.1", "Official Department Project Publication Details Sheet (2026–27)")
    ]
}

# ==============================================================================
# STUDENT & GUIDE PROJECT IDENTIFICATION SHEET (Page 54)
# ==============================================================================

CH6_TO_CH7_PAGES[54] = {
    "chapter_title": "Department of Information Science and Engineering\nMalnad College of Engineering, Hassan\nBachelor of Engineering Major Project Identification Sheet, 2026–27",
    "content": [
        ("img", "team_identification_sheet.png", "7.2", "Project Identification Sheet – Candidates, Guide and Department Endorsement")
    ]
}

print("Loaded Chapter 6 to 7 definitions, References, and Official Sheets (Pages 41 to 54).")
