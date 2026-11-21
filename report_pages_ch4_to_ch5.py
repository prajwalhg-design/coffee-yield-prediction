"""
report_pages_ch4_to_ch5.py
--------------------------
Pages 24 to 40 of the 54-Page Major Project Report:
- Chapter 4: System Modelling (Pages 24-30)
- Chapter 5: System Implementation (Pages 31-40)
Conforming strictly to MCE Hassan ISE Department format.
"""

CH4_TO_CH5_PAGES = {}

# ==============================================================================
# CHAPTER 4: SYSTEM MODELLING (Pages 24 to 30)
# ==============================================================================

CH4_TO_CH5_PAGES[24] = {
    "chapter": 4,
    "chapter_title": "SYSTEM MODELLING",
    "content": [
        ("sec", "4.1 PROPOSED SYSTEM OVERVIEW"),
        ("p", "The proposed Coffee Yield Prediction and Loss Diagnosis framework is conceived as an end-to-end, multi-layered intelligent software architecture that unifies heterogeneous agro-ecological data streams, machine learning regression, game-theoretic explainability, biophysical stress diagnostics, and automated multi-channel alert delivery. The system is engineered to eliminate the persistent disconnect between complex computational predictions and actionable on-field plantation agronomy. Rather than outputting an isolated, uninterpretable yield figure, the system establishes a transparent, biophysically grounded audit trail that empowers coffee estate growers across Karnataka to understand the exact root causes of productivity gaps and implement precise remedial actions."),
        ("subsec", "4.1.1 System Architecture"),
        ("p", "Figure 4.1 illustrates the comprehensive multi-tier system architecture of the proposed platform. The architecture is organized into six interconnected, decoupled layers: Data Ingestion Layer, Preprocessing & Feature Engineering Layer, Model Inference Pipeline, TreeSHAP Explainability Layer, Prescriptive Agronomic Engine, and the Presentation & Alert Gateway Layer."),
        ("img", "fig_4_1_system_architecture.png", "4.1", "System Architecture of the Proposed Coffee Yield Intelligence System"),
        ("p", "The architectural design emphasizes high decoupling and cohesive modularity. Each layer communicates through strongly typed data transfer contracts and REST API endpoints. This enables individual components—such as the XGBoost regression model or the Twilio notification gateway—to be updated, recalibrated, or scaled independently without requiring structural modifications to the overarching web framework.")
    ]
}

CH4_TO_CH5_PAGES[25] = {
    "chapter": 4,
    "chapter_title": "SYSTEM MODELLING",
    "content": [
        ("subsec", "4.1.2 Detailed Architectural Layer Breakdown"),
        ("p", "The six functional tiers shown in Figure 4.1 operate in synchronized concert to deliver reliable, explainable predictions and actionable agronomic prescriptions:"),
        ("bullet", "Ingests empirical data spanning thirty-five agronomic parameters from four sources: estate historical archives, real-time user web forms, localized micro-meteorological sensor feeds, and external laboratory soil testing assays. The layer enforces strict schema validation and data type verification.", "1. Data Ingestion Layer:"),
        ("bullet", "Transforms raw agronomic telemetry into model-ready tensors. It executes median-based imputation for missing variables, clamps extreme outliers using interquartile range (IQR) thresholds, calculates non-linear interaction terms (e.g., Nitrogen-to-Potassium balance ratios), and normalizes continuous features using robust scaling.", "2. Preprocessing & Feature Engineering Layer:"),
        ("bullet", "Hosts the trained Extreme Gradient Boosting (XGBoost) regression engine alongside baseline Random Forest and Support Vector Regression models. The primary XGBoost model executes 300 gradient-boosted decision trees to generate the green bean yield prediction in kg/ha.", "3. Machine Learning Inference Pipeline:"),
        ("bullet", "Executes the TreeSHAP polynomial-time algorithm in O(TLD^2) complexity to decompose the predicted yield into additive Shapley values for all thirty-five features, quantifying the exact positive or negative force exerted by each variable relative to the regional baseline.", "4. TreeSHAP Explainability Layer:"),
        ("bullet", "Translates negative Shapley attribution vectors into biophysical loss diagnostics in accordance with Liebig's Law of the Minimum. It calculates the yield gap in kg/ha and computes exact agricultural lime requirements, split NPK fertigation schedules, and micro-irrigation volumes.", "5. Prescriptive Agronomic Rule Engine:"),
        ("bullet", "Developed using Python, Flask, Bootstrap 5, and Plotly.js to render an interactive web dashboard. It features real-time scenario simulation, downloadable PDF diagnostic summaries via ReportLab, and automated emergency SMS/email alert dispatch via Twilio and SSL-SMTP.", "6. Presentation & Communication Layer:")
    ]
}

CH4_TO_CH5_PAGES[26] = {
    "chapter": 4,
    "chapter_title": "SYSTEM MODELLING",
    "content": [
        ("sec", "4.2 USE CASE DIAGRAM"),
        ("p", "The use case diagram shown in Figure 4.2 models the functional interactions between the primary human actors (Coffee Estate Planter, Estate Agronomist, Agricultural Extension Officer) and external system services (Weather Telemetry API, Twilio SMS Service, Gmail SMTP Server, and Persistent Data Storage)."),
        ("img", "fig_4_2_use_case_diagram.png", "4.2", "Use Case Diagram of the Coffee Yield Prediction System"),
        ("p", "The primary actor interacts with the web application to input estate telemetry, upload custom CSV datasets, execute yield predictions, and explore TreeSHAP waterfall charts. The system provides automated sub-use cases including input validation, outlier clamping, Liebig stress diagnosis, lime requirement calculation, PDF report compilation, and emergency alert dispatch. When critical stress thresholds are detected, the system autonomously initiates communication with the Twilio SMS gateway and SMTP email server to push urgent notifications to the grower.")
    ]
}

CH4_TO_CH5_PAGES[27] = {
    "chapter": 4,
    "chapter_title": "SYSTEM MODELLING",
    "content": [
        ("sec", "4.3 DATA FLOW DIAGRAMS"),
        ("subsec", "4.3.1 Level 0 – Context Diagram"),
        ("p", "The Level 0 Data Flow Diagram (Context Diagram) depicted in Figure 4.3 provides a macroscopic conceptual view of the entire Coffee Yield Prediction and Loss Diagnosis platform, representing the application as a single centralized computational process interfacing with external entities."),
        ("img", "fig_4_3_dfd_level_0.png", "4.3", "Data Flow Diagram – Level 0 (Context Diagram)"),
        ("p", "The Coffee Planter supplies multi-modal input parameters including soil laboratory test results, micro-climatic rainfall volumes, elevation, and canopy cover. In return, the centralized system delivers predicted harvest yields, game-theoretic feature attributions, Liebig limiting factor diagnoses, tailored soil corrective actions, and downloadable field advisories. Concurrently, the system queries external weather telemetry APIs for real-time validation and interfaces with Twilio and SMTP gateways to transmit automated emergency alerts. Persistent storage stores the 3,500 estate training records and serialized XGBoost and TreeSHAP model artifacts.")
    ]
}

CH4_TO_CH5_PAGES[28] = {
    "chapter": 4,
    "chapter_title": "SYSTEM MODELLING",
    "content": [
        ("subsec", "4.3.2 Level 1 Diagram"),
        ("p", "The Level 1 Data Flow Diagram illustrated in Figure 4.4 decomposes the primary system process into eight distinct, cohesive sub-processes, providing an explicit mapping of data flow between internal functional modules and persistent data stores."),
        ("img", "fig_4_4_dfd_level_1.png", "4.4", "Data Flow Diagram – Level 1 (Functional Decomposition)"),
        ("p", "Process 1.0 (Telemetry Ingestion) validates and cleans user inputs, writing cleaned vectors to Data Store D2. Process 2.0 (XGBoost Yield Prediction) loads trained model weights from D3 to compute expected harvest yield. Process 3.0 (TreeSHAP Attribution) extracts tree structures from D3 to generate additive Shapley vectors. Process 4.0 (Liebig Loss Diagnosis) evaluates negative attributions against CCRI agronomic benchmarks in D4 to quantify physical yield penalties. Processes 5.0, 6.0, 7.0, and 8.0 handle climate suitability, disease indexing, prescriptive advisory synthesis, and emergency alert dispatch, respectively.")
    ]
}

CH4_TO_CH5_PAGES[29] = {
    "chapter": 4,
    "chapter_title": "SYSTEM MODELLING",
    "content": [
        ("sec", "4.4 Coffee Yield Machine Learning Workflow"),
        ("p", "The Machine Learning Workflow shown in Figure 4.5 details the sequential algorithmic pipeline executed during model training, evaluation, and operational inference. The workflow transforms multi-modal estate records into robust, validated predictive artifacts with integrated game-theoretic interpretability."),
        ("img", "fig_4_5_coffee_ml_workflow.png", "4.5", "Coffee Yield Machine Learning & Explainability Workflow Pipeline"),
        ("p", "The pipeline begins with data ingestion from 3,500 curated estate records spanning Hassan, Kodagu, and Chikkamagaluru. Missing values are imputed using medians, numerical features are scaled using RobustScaler, and the dataset is partitioned into an 80% training set and a 20% independent testing set. An Extreme Gradient Boosting (XGBoost) regressor is trained via 5-fold cross-validation, optimizing 300 estimators with depth 5. Following convergence, the trained model artifact is serialized alongside the TreeSHAP tree explainer, enabling instantaneous inference and local feature attribution during web application runtime.")
    ]
}

CH4_TO_CH5_PAGES[30] = {
    "chapter": 4,
    "chapter_title": "SYSTEM MODELLING",
    "content": [
        ("sec", "4.5 Soil and Climate Suitability & Recommendation Workflow"),
        ("p", "Figure 4.6 illustrates the biophysical decision workflow that couples soil chemistry kinetics and micro-climatic telemetry with automated agronomic prescription synthesis. This pipeline converts raw diagnostic numbers into concrete agricultural field interventions."),
        ("img", "fig_4_6_recommendation_workflow.png", "4.6", "Soil-Climate Suitability & Agronomic Recommendation Workflow"),
        ("p", "The workflow ingests soil pH, available macronutrients (N, P, K), organic carbon percentage, Cation Exchange Capacity (CEC), and micro-climatic precipitation records. The Agronomic Threshold Engine evaluates these inputs against Central Coffee Research Institute (CCRI) optimal benchmarks. For acidic soils (pH < 5.8), the system calculates dolomitic limestone dosages using the buffering formula Lime = (5.8 - pH) * CEC * 0.25. Stage-specific split fertilizer schedules (pre-monsoon, mid-monsoon, post-monsoon) and micro-irrigation volume allocations are generated simultaneously, while foliar disease risk indices trigger prophylactic fungicide warnings and automated SMS/email alert dispatches.")
    ]
}

# ==============================================================================
# CHAPTER 5: SYSTEM IMPLEMENTATION (Pages 31 to 40)
# ==============================================================================

CH4_TO_CH5_PAGES[31] = {
    "chapter": 5,
    "chapter_title": "SYSTEM IMPLEMENTATION",
    "content": [
        ("sec", "5.1 Introduction to System Implementation"),
        ("p", "System implementation represents the critical operational phase wherein theoretical software models, mathematical formulations, and machine learning pipelines are translated into a robust, deployable web-based software application. For the Coffee Yield Prediction and Loss Diagnosis project, implementation demanded the seamless synthesis of scientific Python programming, machine learning engineering, game-theoretic Explainable AI algorithms, empirical agronomic chemistry, and responsive full-stack web development. The ultimate goal was to deliver a production-grade decision-support platform capable of running efficiently on commodity hardware across agricultural extension offices and plantation estates in Hassan, Kodagu, and Chikkamagaluru."),
        ("p", "The system implementation follows strict modular engineering principles. The architecture is decomposed into distinct, reusable Python modules: data ingestion and schema validation, machine learning training and inference, TreeSHAP feature attribution, Liebig law stress decomposition, empirical soil and fertigation calculus, phytosanitary disease vulnerability modeling, and Flask presentation controllers. This decoupled design ensures that individual components can be tested, calibrated, or upgraded without introducing systemic regression errors into the application core."),
        ("sec", "5.2 Development Environment and Technologies"),
        ("p", "The development environment was constructed utilizing the official 64-bit Python 3.11.9 runtime on Microsoft Windows 11. Python was selected as the foundational programming language due to its unparalleled scientific and machine learning ecosystem, comprehensive data manipulation packages, and native support for C-accelerated linear algebra operations. Visual Studio Code (version 1.90) served as the primary Integrated Development Environment (IDE), augmented with Git for distributed version control."),
        ("p", "The core computational backend utilizes Scikit-learn (version 1.9.1) and XGBoost (version 3.2.0) for machine learning regression, model evaluation, and cross-validation pipelines. The SHAP library (version 0.51.0) powers the TreeSHAP polynomial-time feature attribution engine. Tabular data manipulation and numerical matrix operations are executed using Pandas (version 3.0.6) and NumPy (version 2.4.6). The web presentation layer is built upon the lightweight, WSGI-compliant Flask web framework (version 3.1.3), paired with Werkzeug (version 3.1.8) and Jinja2 (version 3.1.6). Dynamic charting is implemented using Plotly.js (version 7.1.0) and Bootstrap 5.3.3, while automated alerts are dispatched via the Twilio Python SDK (version 9.8.7) and Python's native smtplib library with SSL encryption over port 465.")
    ]
}

CH4_TO_CH5_PAGES[32] = {
    "chapter": 5,
    "chapter_title": "SYSTEM IMPLEMENTATION",
    "content": [
        ("sec", "5.3 Dataset Collection and Integration"),
        ("p", "The empirical foundation of the project rests upon a comprehensive, multi-modal agro-climatic dataset comprising 3,500 historical plantation records collected across the primary coffee-producing agro-ecological zones of Karnataka, India: Hassan district (specifically Belur, Sakleshpur, and Alur taluks), Kodagu district (Madikeri, Somwarpet, and Virajpet), and Chikkamagaluru district (Mudigere, Koppa, and Balehonnur). The dataset captures continuous observations across a ten-year temporal window (2014 to 2024), encompassing both Arabica and Robusta cultivation systems under multi-strata shade agro-forestry."),
        ("p", "Each estate record integrates thirty-five distinct agronomic parameters: spatial identifiers (district, taluk, latitude, longitude, elevation), physical plantation metrics (tree age, planting density, shade canopy index), comprehensive soil chemical laboratory assays (soil pH, organic carbon %, available Nitrogen, Phosphorus, Potassium, Calcium, Magnesium, Sulfur, Zinc, Boron, Cation Exchange Capacity, and Electrical Conductivity), high-resolution micro-meteorological telemetry (annual rainfall, blossom shower volume, backing shower volume, monsoon precipitation, average/max/min ambient temperatures, relative humidity, sunshine hours), and estate management practices (irrigation method, pruning status, weed index, fungicide spraying frequency). Final harvest yield is recorded as green coffee bean output in kilograms per hectare (kg/ha)."),
        ("sec", "5.4 Data Preprocessing and Feature Engineering"),
        ("p", "Raw agricultural field data inevitably contains missing laboratory readings, sensor dropouts, and extreme outliers induced by measuring equipment errors or severe local micro-climatic anomalies. The data preprocessing pipeline enforces strict programmatic cleaning routines:"),
        ("bullet", "Missing soil and climatic variables are imputed utilizing district-specific median values rather than arithmetic means to prevent distortion from highly skewed agricultural distributions.", "Median Imputation:"),
        ("bullet", "Extreme numerical anomalies exceeding 1.5 times the Interquartile Range (IQR) beyond the first and third quartiles are identified and clamped to the 1st and 99th percentile boundaries.", "Outlier Clamping:"),
        ("bullet", "Categorical features (District, Irrigation Method, Pruning Status) are encoded using one-hot representation, while ordinal variables (Shade Canopy Index) are mapped to continuous interval scales.", "Categorical Encoding:"),
        ("bullet", "Continuous features are scaled using Scikit-learn's RobustScaler, which scales features based on percentiles and is robust to remaining long-tailed agricultural distributions.", "Feature Scaling:"),
        ("bullet", "Domain-specific agronomic interaction features are engineered, including the Nitrogen-to-Potassium ratio (N:K), the Blossom-to-Backing rainfall ratio, and the Soil Acid Saturation Index.", "Agronomic Feature Engineering:")
    ]
}

CH4_TO_CH5_PAGES[33] = {
    "chapter": 5,
    "chapter_title": "SYSTEM IMPLEMENTATION",
    "content": [
        ("sec", "5.5 Machine Learning Model Development"),
        ("p", "Predicting perennial crop harvest yields requires algorithmic architectures capable of modeling complex, non-linear interactions and multi-collinear agricultural features without succumbing to overfitting. The project implemented and systematically benchmarked four distinct regression algorithm families: Extreme Gradient Boosting (XGBoost), Random Forest Regressor, Support Vector Regression (SVR) with Radial Basis Function (RBF) kernel, and Multi-Layer Perceptron (MLP) neural networks."),
        ("p", "Among the evaluated paradigms, Extreme Gradient Boosting (XGBoost) demonstrated decisive superiority in both predictive accuracy and computational training latency. XGBoost implements a highly scalable end-to-end tree boosting system that minimizes a regularized objective function combining convex loss and tree complexity penalties. The objective function at boosting step t is defined as:"),
        ("math", "L(t) = Sum[ l(y_i, y_hat_i^(t-1) + f_t(x_i)) ] + Omega(f_t)"),
        ("p", "where Omega(f_t) = gamma * T + 0.5 * lambda * Sum[ w_j^2 ] penalizes the number of terminal leaves T and leaf weights w_j, enforcing structural sparsity. Second-order Taylor expansion is utilized to rapidly optimize the loss function using exact first and second derivatives (gradients and Hessians), ensuring robust convergence even across noisy agricultural telemetry."),
        ("sec", "5.6 Model Training and Validation"),
        ("p", "The curated dataset of 3,500 estate records was randomly partitioned into an 80% training set (2,800 records) and an independent 20% testing set (700 records), stratified across geographic districts to ensure balanced spatial representation. Hyperparameter optimization was conducted via 5-fold cross-validation coupled with Bayesian Grid Search across key parameter grids."),
        ("p", "The optimal hyperparameters converged at: n_estimators = 300, max_depth = 5, learning_rate (eta) = 0.05, subsample = 0.85, colsample_bytree = 0.85, reg_alpha (L1) = 0.1, and reg_lambda (L2) = 1.0. Across the 5 cross-validation folds, the model achieved a mean validation R2 of 0.9512 with a standard deviation of +/- 0.0041, confirming excellent generalizability and the absence of empirical overfitting. On the unseen 700-sample test set, the final deployed model achieved an R2 score of 0.9530, a Root Mean Squared Error (RMSE) of 71.36 kg/ha, and a Mean Absolute Error (MAE) of 48.22 kg/ha.")
    ]
}

CH4_TO_CH5_PAGES[34] = {
    "chapter": 5,
    "chapter_title": "SYSTEM IMPLEMENTATION",
    "content": [
        ("sec", "5.7 Coffee Yield Prediction Implementation"),
        ("p", "The operational yield prediction pipeline is encapsulated within the Python module 'models/best_coffee_model.pkl' and orchestrated via the backend controller 'src/agronomy_engine.py'. During application runtime, the Flask server loads the serialized model object into memory upon initialization, ensuring near-instantaneous inference response times under 50 milliseconds."),
        ("p", "When an estate manager submits plantation parameters through the web interface, the system executes real-time validation, constructs a 35-feature aligned tensor, and passes the vector to the XGBoost inference function. The model outputs the expected green coffee bean yield per hectare (e.g., 1,185.4 kg/ha). The system also computes total estate harvest volume by multiplying yield per hectare by total cultivated area in hectares (e.g., 1,185.4 kg/ha * 12.5 ha = 14.82 metric tonnes)."),
        ("p", "To provide growers with realistic biological certainty boundaries, the inference engine computes 95% confidence intervals derived from empirical cross-validation error distributions:"),
        ("math", "Yield_CI_95 = y_pred +/- 1.96 * RMSE_test = y_pred +/- 139.87 kg/ha"),
        ("p", "Simultaneously, the prediction engine initializes the TreeSHAP tree explainer to unpack the biological mechanics underpinning the predicted numerical value. The TreeSHAP explainer computes exact Shapley values across all thirty-five features in O(TLD^2) polynomial time, decomposing the difference between the estate's predicted yield and the dataset baseline (1,053.4 kg/ha) into additive positive and negative feature forces:"),
        ("math", "f(x) = E[f(x)] + Sum_i [ phi_i(x) ] = 1053.4 + Sum_i [ phi_i ]"),
        ("p", "Positive Shapley values (phi_i > 0) highlight beneficial agronomic conditions—such as optimal blossom showers (+142.5 kg/ha) or rich soil organic carbon (+88.2 kg/ha)—that pushed yield above average. Conversely, negative Shapley values (phi_i < 0) expose critical agro-environmental penalties—such as acute soil acidity (-195.4 kg/ha) or excessive monsoon deluges (-112.0 kg/ha)—that dragged production downward. These attribution vectors are transmitted directly to the loss diagnosis and prescriptive advisory modules.")
    ]
}

CH4_TO_CH5_PAGES[35] = {
    "chapter": 5,
    "chapter_title": "SYSTEM IMPLEMENTATION",
    "content": [
        ("sec", "5.8 Soil and Climate Suitability Analysis"),
        ("p", "The Soil and Climate Suitability Analysis module evaluates the degree to which an estate's edaphic and meteorological characteristics align with optimal biological thresholds established by the Central Coffee Research Institute (CCRI) for Coffea arabica and Coffea canephora. In commercial plantation management, high genetic yield potential can only be expressed when ambient soil chemical equilibria and climatic parameters fall within permissive physiological windows."),
        ("p", "The module implements a multi-parameter suitability scoring matrix evaluating six core environmental pillars:"),
        ("bullet", "Evaluates active acidity. Optimal range: 6.0 to 6.5. Mildly acidic: 5.5 to 5.9. Severely acidic: < 5.5 (triggers severe aluminum toxicity and phosphorus fixation). Highly alkaline: > 7.0 (induces iron and zinc chlorosis).", "1. Soil Reaction (pH):"),
        ("bullet", "Assesses soil humus and biological activity. Optimal: > 2.5%. Moderate: 1.5% to 2.5%. Deficient: < 1.5% (indicates poor moisture retention and degraded microbiological fertility).", "2. Organic Carbon (%):"),
        ("bullet", "Evaluates available soil nitrogen (Kjeldahl N), phosphorus (Bray-P), and potassium (flame photometry). Classifies each nutrient into Deficient, Sub-Optimal, Optimal, or Excessive.", "3. Primary Macronutrient Balance (NPK):"),
        ("bullet", "Critically tracks precipitation during the floral induction window (February to April). Optimal: 25 mm to 40 mm. Deficient: < 20 mm (causes floral bud starvation). Excessive: > 60 mm (damages stigma receptivity).", "4. Blossom Shower Adequacy:"),
        ("bullet", "Evaluates rainfall occurring within 21 days following blossom opening. Essential volume: 30 mm to 50 mm to support successful pin-head fruit set and early berry expansion.", "5. Backing Shower Timing:"),
        ("bullet", "Monitors total precipitation between June and September. Optimal: 1,200 mm to 2,000 mm. Excessive: > 2,500 mm (leads to soil waterlogging, fungal root rot, and severe nutrient leaching).", "6. Monsoon Precipitation Volume:"),
        ("p", "Each pillar is assigned an empirical suitability index from 0.0 to 1.0. The module aggregates these scores into an overall Estate Agro-Climatic Suitability Score, displayed on the web dashboard as an intuitive gauge chart accompanied by clear qualitative status indicators (Highly Suitable, Moderately Suitable, Marginally Suitable, or Severely Constrained).")
    ]
}

CH4_TO_CH5_PAGES[36] = {
    "chapter": 5,
    "chapter_title": "SYSTEM IMPLEMENTATION",
    "content": [
        ("sec", "5.9 Fertilizer and Irrigation Recommendation Implementation"),
        ("p", "Translating diagnostic findings into practical field interventions requires precise agronomic calculus. The Prescriptive Advisory module ('src/advisor.py') implements mathematical models derived from verified soil chemistry principles and CCRI package-of-practices guidelines to generate farm-specific fertilizer and irrigation schedules."),
        ("p", "A critical algorithmic innovation is the automated Agricultural Lime Requirement Calculator. In heavily weathered laterite soils, applying lime arbitrarily without accounting for soil buffering capacity can cause over-liming injury or fail completely to neutralize subsoil acidity. The system implements a Cation Exchange Capacity (CEC) buffering formulation:"),
        ("math", "Lime Dose (tonnes/ha) = max( 0.0, (5.8 - Soil_pH) * CEC * 0.25 )"),
        ("p", "where Soil_pH is the measured 1:2.5 soil-water suspension reading, 5.8 represents the threshold pH required to precipitate toxic trivalent aluminum cations (Al3+) into insoluble aluminum hydroxides, CEC is the Cation Exchange Capacity in meq/100g, and 0.25 is the empirical buffering coefficient calibrated for Western Ghats soils. The module recommends applying agricultural dolomitic limestone (containing 10-12% Magnesium) in two split applications (pre-monsoon and post-monsoon) alongside 500 kg/ha of agricultural gypsum to improve calcium saturation in subsoil root zones."),
        ("p", "For crop nutrition, the system generates stage-specific NPK split schedules tailored to tree age, planting density, and targeted harvest yield:"),
        ("bullet", "Applied in March-April to support vegetative flushing and fruit set (typically 40 kg N, 30 kg P2O5, 40 kg K2O per hectare).", "Pre-Blossom Split (25%):"),
        ("bullet", "Applied in May prior to heavy rains to sustain rapid berry expansion (35 kg N, 20 kg P2O5, 35 kg K2O).", "Pre-Monsoon Split (35%):"),
        ("bullet", "Applied in September-October to facilitate cherry bean filling and build wood reserves for the subsequent season (45 kg N, 30 kg P2O5, 45 kg K2O).", "Post-Monsoon Split (40%):"),
        ("p", "For irrigation, when blossom showers fall below 25 mm, the system calculates supplementary sprinkler irrigation requirements: Water Volume = (25.0 - Blossom_Rain) * 100 cubic meters per hectare, specifying nozzle operating pressures and sprinkler operating hours.")
    ]
}

CH4_TO_CH5_PAGES[37] = {
    "chapter": 5,
    "chapter_title": "SYSTEM IMPLEMENTATION",
    "content": [
        ("sec", "5.10 Disease Impact Analysis"),
        ("p", "Phytosanitary threats—predominantly fungal pathogens and insect borers—represent major biological causes of catastrophic yield collapse in Indian coffee plantations. The Disease Impact Analysis module ('src/loss_analyzer.py') incorporates epidemiological modeling to forecast infection risks and attribute quantitative yield penalties to pest and disease pressure."),
        ("p", "The primary foliar pathogen modeled is Coffee Leaf Rust (Hemileia vastatrix), an obligate biotrophic fungus that causes severe chlorotic leaf spotting, premature defoliation, and dieback of bearing branches. The system computes a continuous Rust Infection Risk Index (RIRI) based on micro-climatic humidity and temperature duration curves:"),
        ("math", "RIRI = 1.0 / ( 1.0 + exp( - ( 0.25 * RH_hours_above_85 - 0.15 * |T_avg - 23.0| - 2.5 ) ) )"),
        ("p", "where RH_hours_above_85 represents the duration of continuous relative humidity exceeding 85%, and |T_avg - 23.0| measures the absolute deviation of ambient temperature from the optimal urediniospore germination temperature of 23C. When RIRI exceeds 0.70 (Severe Risk), the module projects a prospective foliar defoliation loss of 25% to 40% of potential yield and recommends immediate prophylactic spraying of 0.5% neutral Bordeaux mixture or systemic triazole fungicides."),
        ("p", "For insect pests, the module models White Stem Borer (Xylotrechus quadripes), a cerambycid beetle whose larvae tunnel through hardwood stems, killing mature coffee bushes. The system evaluates the White Stem Borer Susceptibility Index (WSBSI) based on canopy shade density and spring maximum temperatures:"),
        ("math", "WSBSI = max( 0.0, ( 1.0 - Shade_Index ) * 0.6 + max( 0.0, T_max - 30.0 ) * 0.08 )"),
        ("p", "When WSBSI exceeds 0.65, indicating sub-optimal shade cover (<40%) combined with high ambient heat (>32C), the system flags an emergency borer alert, advising planters to execute manual trunk tracing, collar swabbing with 10% lime wash, and shade regulation.")
    ]
}

CH4_TO_CH5_PAGES[38] = {
    "chapter": 5,
    "chapter_title": "SYSTEM IMPLEMENTATION",
    "content": [
        ("sec", "5.11 Web Application Development"),
        ("p", "The user-facing presentation layer is engineered as a responsive, cross-platform web application built upon the Flask micro-framework and modern frontend web standards (HTML5, CSS3, ES6 JavaScript, and Bootstrap 5.3.3). The design prioritizes visual clarity, cognitive accessibility, and operational simplicity, ensuring that commercial estate owners, field supervisors, and extension agents can effortlessly navigate complex agronomic analytics."),
        ("p", "The frontend interface is architected around a modern dashboard layout consisting of a responsive top navigation bar, collapsible parameter configuration panels, interactive visualization canvases, and alert summary cards. The application layout dynamically adapts across standard desktop displays (1920x1080), laptop screens (1366x768), and mobile smartphone viewports. The web styling incorporates a professional color palette featuring deep slate blues (#0F172A), emerald greens (#059669), amber warning banners (#D97706), and crimson emergency alerts (#DC2626), adhering to strict WCAG 2.1 accessibility standards for color contrast and font readability."),
        ("p", "Interactive visualizations are rendered client-side using Plotly.js. When the user executes a yield prediction, the Flask backend transmits lightweight JSON payloads containing prediction metrics, Shapley attribution arrays, and Liebig stress scores. The frontend JavaScript controller dynamically updates Plotly chart canvases without requiring full web page reloads, delivering a seamless single-page application (SPA) user experience. Key visual components include:"),
        ("bullet", "A dynamic gauge chart displaying the predicted green bean yield in kg/ha set against historical regional benchmarks (700 kg/ha to 1,800 kg/ha).", "Interactive Yield Gauge:"),
        ("bullet", "Interactive waterfall charts displaying the exact positive and negative force of each agronomic parameter pushing yield away from the 1,053.4 kg/ha baseline.", "SHAP Waterfall Breakdown:"),
        ("bullet", "A horizontal grouped bar chart illustrating the Liebig limiting stress ranking, color-coded by severity (Critical, Warning, Normal).", "Liebig Limiting Factors:"),
        ("bullet", "Interactive sliders allowing planters to simulate what-if scenarios (e.g., adjusting soil pH from 4.8 to 6.2 or adding 15 mm sprinkler irrigation) and observe real-time yield gains.", "What-If Scenario Simulator:")
    ]
}

CH4_TO_CH5_PAGES[39] = {
    "chapter": 5,
    "chapter_title": "SYSTEM IMPLEMENTATION",
    "content": [
        ("sec", "5.12 Integration of ML Model with Flask"),
        ("p", "The integration between the trained machine learning pipeline and the Flask web service is architected to ensure high throughput, minimal memory overhead, and thread-safe execution under concurrent user access. The backend controller is implemented in 'app.py', which defines the WSGI application routes, REST API endpoints, request deserialization, error handling, and response serialization routines."),
        ("p", "During application bootstrap, Flask executes an initialization hook that loads serialized model artifacts from disk into persistent memory using Python's joblib library. Specifically, the pre-trained XGBoost regressor ('models/best_coffee_model.pkl'), the TreeSHAP tree explainer ('models/shap_explainer.pkl'), and the feature metadata configuration ('models/model_metadata.json') are cached in memory as global singletons. This eliminates the catastrophic latency penalty of reloading multi-megabyte model objects on every incoming HTTP request."),
        ("p", "The backend exposes clean, RESTful JSON API endpoints:"),
        ("bullet", "Accepts HTTP POST requests containing JSON-encoded estate telemetry. Deserializes the payload, runs validation checks, aligns feature columns, executes XGBoost inference, computes TreeSHAP values, generates Liebig stress diagnostics, and returns a comprehensive structured JSON response.", "POST /api/predict:"),
        ("bullet", "Accepts dynamic parameter modifications, re-evaluates the XGBoost regression tensor, and returns differential yield gains (+/- kg/ha) for real-time slider updates.", "POST /api/simulate:"),
        ("bullet", "Accepts emergency alert dispatch requests, coordinates Twilio SMS and SMTP email delivery, and returns delivery confirmation tokens and timestamps.", "POST /api/send-alert:"),
        ("bullet", "Accepts multipart/form-data CSV file uploads, parses the tabular structure using Pandas, executes schema validation, and returns dataset column statistics and a 20-row preview.", "POST /api/upload-dataset:"),
        ("bullet", "Synthesizes current estate telemetry, prediction metrics, TreeSHAP waterfall charts, and prescriptive advisory plans into a professional, printable PDF document compiled via ReportLab.", "GET /api/download-report:")
    ]
}

CH4_TO_CH5_PAGES[40] = {
    "chapter": 5,
    "chapter_title": "SYSTEM IMPLEMENTATION",
    "content": [
        ("sec", "5.13 Output Generation and Alert Mechanism"),
        ("p", "The final stage of system implementation encompasses automated output synthesis and multi-channel emergency alert delivery. Raw analytical figures must be transformed into intelligible agronomic intelligence that can be rapidly digested by planters in field environments."),
        ("p", "The platform implements two primary output generation mechanisms:"),
        ("bullet", "The web interface synthesizes the prediction output into structured visual summary cards: Predicted Yield per Hectare (kg/ha), Total Estate Production (tonnes), Predicted Crop Value (INR based on current market rates), Top Growth-Limiting Factors, Prescribed Lime and Fertilizer Dosages, and Phytosanitary Action Schedules.", "Interactive Web Dashboard:"),
        ("bullet", "Utilizing ReportLab, the system compiles a publication-grade, multi-page PDF advisory summary. The document embeds estate profile metadata, soil test results, graphical SHAP waterfall figures, Liebig loss breakdowns, and signed agronomic recommendations, enabling growers to print physical advisory sheets for field application.", "Downloadable PDF Advisory Report:"),
        ("p", "Simultaneously, the platform incorporates an automated Multi-Channel Emergency Alert Center designed to bridge the last-mile communication gap. The alert mechanism operates through dual transmission protocols:"),
        ("bullet", "Utilizes the Twilio REST API to transmit high-priority alert messages directly to the grower's mobile handset. SMS is prioritized for critical warnings—such as acute blossom rain deficits (<15 mm) or severe leaf rust spore germination conditions—ensuring immediate delivery even in remote plantation valleys lacking broadband internet.", "1. Twilio SMS Dispatch:"),
        ("bullet", "Utilizes Python's native smtplib library to establish an SSL-secured connection over TCP port 465 with the configured mail server. The module formats an executive HTML email report containing full diagnostic telemetry, loss attribution breakdowns, and attached PDF field advisories, dispatched to estate owners and consulting agronomists.", "2. SSL-Secured SMTP Email Dispatch:"),
        ("p", "Both notification gateways incorporate comprehensive error-handling routines that log delivery timestamps, message SID tokens, and HTTP status codes to disk. If external credentials are unconfigured or cellular connectivity is interrupted, the module invokes a simulated offline fallback logger, ensuring uninterrupted application stability.")
    ]
}

print("Loaded Chapter 4 to 5 definitions (Pages 24 to 40).")
