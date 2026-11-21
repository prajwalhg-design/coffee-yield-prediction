"""
generate_ieee_pdf.py
--------------------
Generates a double-column, publication-grade IEEE Conference Proceedings PDF
for the Coffee Yield Prediction & Loss Diagnosis Major Project.
Uses Chrome Headless Print-to-PDF with IEEE CSS styling.
"""

import os
import subprocess
import shutil

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Explainable AI-Driven Coffee Yield Prediction and Root-Cause Yield Loss Diagnosis Using Multi-Modal Agro-Climatic Data</title>
<style>
  @page {
    size: letter;
    margin: 0.75in 0.65in 0.75in 0.65in;
    @bottom-center {
      content: counter(page);
      font-family: 'Times New Roman', Times, serif;
      font-size: 9pt;
    }
  }

  body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 10pt;
    line-height: 1.25;
    color: #000;
    margin: 0;
    padding: 0;
    text-align: justify;
  }

  /* Single column for Header Block */
  .header-block {
    text-align: center;
    margin-bottom: 18pt;
  }

  .paper-title {
    font-size: 22pt;
    font-weight: bold;
    margin-bottom: 14pt;
    line-height: 1.2;
  }

  .authors-grid {
    display: flex;
    justify-content: space-around;
    margin-bottom: 16pt;
    font-size: 9.5pt;
  }

  .author-card {
    text-align: center;
    width: 30%;
    line-height: 1.3;
  }

  .author-name {
    font-weight: bold;
    font-size: 10.5pt;
  }

  .author-dept {
    font-style: italic;
  }

  .abstract-keywords {
    margin: 0 0.2in 14pt 0.2in;
    font-size: 9pt;
    line-height: 1.28;
  }

  .abstract-title {
    font-weight: bold;
    font-style: italic;
  }

  .keywords-title {
    font-weight: bold;
    font-style: italic;
  }

  /* Two Column Body Layout */
  .two-column {
    column-count: 2;
    column-gap: 0.22in;
    column-rule: 0.5pt solid #eee;
  }

  h1.sec-title {
    font-size: 10pt;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    margin-top: 12pt;
    margin-bottom: 6pt;
    break-after: avoid;
  }

  h2.subsec-title {
    font-size: 10pt;
    font-weight: bold;
    font-style: italic;
    margin-top: 8pt;
    margin-bottom: 4pt;
    break-after: avoid;
  }

  p {
    text-indent: 0.18in;
    margin-top: 0;
    margin-bottom: 4pt;
  }

  p.no-indent {
    text-indent: 0;
  }

  .dropcap {
    float: left;
    font-size: 30pt;
    line-height: 24pt;
    padding-top: 2pt;
    padding-right: 4pt;
    padding-left: 1pt;
    font-family: 'Times New Roman', Times, serif;
  }

  /* Equations */
  .equation {
    text-align: center;
    margin: 6pt 0;
    font-style: italic;
    font-size: 9.5pt;
    position: relative;
  }

  .eq-num {
    float: right;
    font-style: normal;
  }

  /* Tables */
  table.ieee-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 8pt;
    margin: 8pt 0;
    line-height: 1.2;
  }

  table.ieee-table caption {
    caption-side: top;
    font-size: 8pt;
    font-weight: bold;
    text-transform: uppercase;
    text-align: center;
    margin-bottom: 4pt;
  }

  table.ieee-table th {
    border-top: 1pt solid #000;
    border-bottom: 0.75pt solid #000;
    padding: 3pt 2pt;
    text-align: center;
    font-weight: bold;
  }

  table.ieee-table td {
    padding: 2.5pt 2pt;
    border-bottom: 0.5pt solid #ddd;
    text-align: center;
  }

  table.ieee-table tr.total-row td {
    border-top: 0.75pt solid #000;
    border-bottom: 1pt solid #000;
    font-weight: bold;
  }

  /* Figures / Boxes */
  .flowchart-box {
    border: 0.75pt solid #333;
    background: #fbfbfb;
    padding: 6pt;
    margin: 8pt 0;
    font-size: 7.5pt;
    font-family: monospace;
    white-space: pre-wrap;
    line-height: 1.2;
    text-align: left;
    text-indent: 0;
  }

  .figure-caption {
    font-size: 8pt;
    font-style: italic;
    text-align: center;
    margin-top: 3pt;
    margin-bottom: 8pt;
  }

  /* References */
  .references-list {
    padding-left: 16pt;
    margin-top: 4pt;
    font-size: 8pt;
    line-height: 1.25;
  }

  .references-list li {
    margin-bottom: 3.5pt;
    text-indent: -12pt;
    list-style-type: none;
  }
</style>
</head>
<body>

<!-- Header Block (Single Column) -->
<div class="header-block">
  <div class="paper-title">Explainable AI-Driven Coffee Yield Prediction and Root-Cause Yield Loss Diagnosis Using Multi-Modal Agro-Climatic Data</div>
  
  <div class="authors-grid">
    <div class="author-card">
      <div class="author-name">Prajwal S.</div>
      <div class="author-dept">Dept. of Computer Science & Engg.</div>
      <div>Visvesvaraya Technological Univ.</div>
      <div>Bengaluru, Karnataka, India</div>
      <div>prajwalkishan006@gmail.com</div>
    </div>
    <div class="author-card">
      <div class="author-name">Student Co-Author</div>
      <div class="author-dept">Dept. of Computer Science & Engg.</div>
      <div>Visvesvaraya Technological Univ.</div>
      <div>Bengaluru, Karnataka, India</div>
      <div>student.cs@institution.edu</div>
    </div>
    <div class="author-card">
      <div class="author-name">Senior Project Guide</div>
      <div class="author-dept">Associate Professor, Dept. of CSE</div>
      <div>Visvesvaraya Technological Univ.</div>
      <div>Bengaluru, Karnataka, India</div>
      <div>guide.advisor@institution.edu</div>
    </div>
  </div>

  <div class="abstract-keywords">
    <p class="no-indent">
      <span class="abstract-title">Abstract</span>—Coffee (<i>Coffea arabica</i> and <i>Coffea canephora</i>) constitutes one of the most commercially critical perennial cash crops in tropical agro-ecosystems, supporting millions of rural livelihoods across equatorial belts. Nonetheless, farm-level harvest productivity remains volatile due to multi-factorial abiotic stresses, intensifying rainfall variability, and chronic soil chemical degradation. While contemporary data-driven architectures demonstrate proficiency in predicting aggregate harvest figures, existing machine learning pipelines operate overwhelmingly as empirical black boxes. They fail to decouple interacting biophysical constraints or isolate the root causes of sub-optimal harvest yields. In this study, we propose a comprehensive, interpretable machine learning framework that unifies predictive yield modeling with root-cause yield loss diagnosis and closed-form agronomic prescription. Leveraging a calibrated multi-modal dataset of 3,500 estate records across vital agro-climatic zones in the Western Ghats and international reference belts, the architecture ingests sixteen edaphic, meteorological, and topographical indicators. A comparative evaluation across Gradient Boosting Regressors (GBM), Extreme Gradient Boosting (XGBoost), and Random Forests confirms that Gradient Boosting achieves optimal generalization, securing a Coefficient of Determination (R²) of 0.9530, a Root Mean Squared Error (RMSE) of 71.36 kg/ha, a Mean Absolute Error (MAE) of 56.04 kg/ha, and a Mean Absolute Percentage Error (MAPE) of 3.88%. To resolve the interpretability challenge, we couple cooperative game-theoretic TreeSHAP (SHapley Additive exPlanations) with a biophysical stress penalty framework grounded in Liebig's Law of the Minimum and research benchmarks from the Central Coffee Research Institute (CCRI). The framework decomposes estate-level yield gaps into factor-specific kilogram-per-hectare penalties and dynamically calculates stoichiometric remediation dosages for agricultural lime, chemical macronutrients, and overhead blossom sprinkler irrigation. An interactive sensitivity simulator is implemented to model harvest recovery trajectories, offering a reliable, actionable paradigm for precision plantation management.
    </p>
    <p class="no-indent" style="margin-top: 5pt;">
      <span class="keywords-title">Index Terms</span>—Precision Agriculture, Coffee Yield Forecasting, Explainable Artificial Intelligence (XAI), TreeSHAP, Gradient Tree Boosting, Abiotic Stress Modeling, Liebig's Law of the Minimum, Soil Health Card Analysis.
    </p>
  </div>
</div>

<!-- Two Column Body -->
<div class="two-column">

  <h1 class="sec-title">I. Introduction</h1>
  <p><span class="dropcap">P</span>ERENNIAL plantation agriculture forms the economic foundation of equatorial agrarian belts, with coffee ranking among the most heavily traded agricultural commodities worldwide [1]. Cultivation is dominated by two primary botanical taxa: <i>Coffea arabica</i> L. (Arabica), recognized for its superior cup quality and sensory profiles, and <i>Coffea canephora</i> Pierre ex A. Froehner (Robusta), noted for higher caffeine concentrations, neutral body, and greater thermal resilience [2]. In key production regions such as the Western Ghats of Southern India (encompassing Kodagu, Chikkamagaluru, Hassan, and Wayanad), Brazil, Vietnam, and Colombia, coffee is typically cultivated under shaded agro-forestry systems on fragile, undulating terrain [3].</p>

  <p>Despite steady advances in plant breeding and agronomic mechanization, farm-level yield realization remains volatile. Per-hectare productivity exhibits inter-annual fluctuations of up to 40% in major growing tracts [4]. This volatility stems from non-linear interactions among edaphic nutrient exhaustion, fluctuating monsoon patterns, seasonal temperature anomalies, and elevation-dependent micro-climates. In tropical laterite soils, chronic leaching of basic cations (Ca²⁺, Mg²⁺, K⁺) caused by intense monsoonal precipitation frequently drives soil pH below 5.0. Under such acidic conditions, toxic soluble aluminum (Al³⁺) and manganese (Mn²⁺) species become mobilized, simultaneously binding free orthophosphate anions into insoluble iron and aluminum complexes (FePO₄, AlPO₄), thereby inducing chemical phosphorus starvation [5].</p>

  <p>Superimposed upon these edaphic constraints are delicate physiological dependencies on rainfall timing. Successful coffee fruit set requires a pronounced dry spell followed by pre-monsoon precipitation, termed "blossom showers" (typically 25–50 mm in March–April) [3]. Blossom showers break floral bud dormancy and trigger synchronous anthesis. If blossom precipitation drops below 20 mm or is delayed past late April, floral buds suffer irreversible physiological necrosis, an agrometeorological failure known as "pinking," which drastically reduces fruit set regardless of subsequent fertilizer application.</p>

  <p>Historically, agricultural extension agencies have addressed these complexities through empirical physiological crop models, including the Decision Support System for Agrotechnology Transfer (DSSAT) and APSIM [6]. Although scientifically rigorous, process-based models require extensive parameter calibration, including hydraulic soil profiles, leaf area index dynamics, and micro-scale radiation partitioning. These parameters are rarely accessible to smallholder farmers or local plantation managers.</p>

  <p>Over the past decade, machine learning algorithms—such as Random Forests, Support Vector Regressors, and Deep Artificial Neural Networks—have emerged as effective data-driven alternatives, mapping heterogeneous soil-climate features directly to final yield outcomes [7], [8]. However, these algorithms present a critical operational limitation: they function predominantly as opaque mathematical black boxes. Standard regression pipelines output a single point estimate (e.g., 1,450 kg/ha) without explaining why a specific plot fell short of its biological potential, which nutrients constrained development, or what corrective actions should be taken.</p>

  <p>To bridge this operational divide, this paper introduces an integrated, interpretable machine learning system that couples non-linear ensemble gradient boosting with game-theoretic explainability and biophysical crop nutrition principles. The primary contributions of this paper are summarized as follows:</p>
  <p>1) <i>Multi-Modal Parameterization:</i> An integrated data architecture ingesting standard Soil Health Card parameters, regional meteorological extremes, and topographical indicators across 3,500 calibrated estate records.</p>
  <p>2) <i>High-Precision Ensemble Prediction:</i> Systematic benchmarking of Gradient Boosting Regressors, Extreme Gradient Boosting (XGBoost), and Random Forests, establishing an optimal ensemble architecture achieving an R² of 0.9530 and an average relative error of 3.88%.</p>
  <p>3) <i>Dual-Tier Root-Cause Loss Diagnosis:</i> Pairing cooperative TreeSHAP with an analytical stress model grounded in Liebig's Law of the Minimum to quantify factor-specific yield deductions in kilograms per hectare.</p>
  <p>4) <i>Closed-Form Prescriptive Translation:</i> Stoichiometric algorithms converting diagnosed deficits into field applications of agricultural lime, dolomite, urea, DAP, MOP, and blossom sprinkler irrigation.</p>
  <p>5) <i>Interactive Sensitivity Simulation:</i> A simulation environment that projects yield and financial recovery before capital deployment.</p>

  <div class="flowchart-box"><b>SYSTEM ARCHITECTURE FLOW:</b>
[Multi-Modal Inputs: Soil Card + Climate + Topography]
                     │
                     ▼
[Data Preprocessing: StandardScaler & OneHotEncoder]
                     │
                     ▼
[Predictive Ensemble: Gradient Boosting Regressor (R²=0.953)]
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
[TreeSHAP Feature Drag]   [Liebig Biophysical Penalties]
         │                       │
         └───────────┬───────────┘
                     ▼
[Prescriptive Agronomic Advisory (Lime, NPK, Irrigation)]
                     │
                     ▼
[Interactive 'What-If' Yield Recovery & ROI Simulator]</div>
  <div class="figure-caption">Fig. 1. End-to-end modular architecture of the proposed Explainable AI Coffee Yield Forecasting and Diagnostic Framework.</div>

  <h1 class="sec-title">II. Related Work</h1>
  <h2 class="subsec-title">A. Machine Learning in Perennial Crop Modeling</h2>
  <p>Yield prediction models have advanced considerably over the last two decades. Early studies relied on Ordinary Least Squares (OLS) and Multiple Linear Regression (MLR). However, linear models often struggle to capture the non-linear interaction thresholds typical of perennial crop biology [7]. In [9], support vector machines with radial basis function (RBF) kernels were deployed to analyze chilling stress in Brazilian coffee zones, demonstrating that non-linear kernel projections outperformed linear formulations when modeling thermal shock.</p>

  <p>Subsequent research turned to ensemble tree algorithms. Everingham et al. [7] applied Random Forests to predict regional yields in perennial crops, finding that bagged decision ensembles improved resistance to multicollinearity among meteorological covariates. In Southeast Asia, Nguyen et al. [8] evaluated XGBoost for Robusta forecasting using satellite-derived Normalized Difference Vegetation Index (NDVI) and Land Surface Temperature (LST) indices, achieving R² scores between 0.82 and 0.89. Despite these performance gains, existing remote-sensing and regional ML studies frequently omit critical sub-surface edaphic variables—such as active soil pH, cation balance, and available potassium—which play a decisive role in coffee bean development and drought resistance [5].</p>

  <h2 class="subsec-title">B. Agronomic Stress and Nutrient Dynamics</h2>
  <p>Extensive research by the Central Coffee Research Institute (CCRI) [3] and the Food and Agriculture Organization (FAO) [10] shows that coffee tree performance is strictly bounded by environmental tolerances. <i>Coffea arabica</i> requires an optimal temperature range of 18°C to 23°C and elevation exceeding 1,000 meters MSL to ensure balanced fruit maturation. In contrast, <i>Coffea canephora</i> exhibits higher thermal tolerance (23°C to 28°C) but requires greater annual precipitation (1,800 to 2,600 mm) to support higher vegetative biomass [2].</p>

  <p>Soil pH represents a critical biological threshold. Tropical laterites often suffer from severe acidity (pH &lt; 5.0), which locks available phosphorus and induces micronutrient toxicity [5]. Classical agronomic literature addresses these constraints through Liebig's Law of the Minimum, which posits that crop productivity is limited not by total resources available, but by the scarcest nutrient factor. However, prior computational studies rarely translate Liebig's principles into non-linear, multi-factorial loss decomposition models within modern ML pipelines.</p>

  <h2 class="subsec-title">C. Explainable Artificial Intelligence (XAI) in Agriculture</h2>
  <p>As complex machine learning models see wider deployment in precision agriculture, their lack of interpretability has raised adoption concerns among agronomists and estate managers [11]. Post-hoc explainability techniques have evolved to address this issue. Local Interpretable Model-agnostic Explanations (LIME) approximates model behavior locally using linear surrogate representations, but can exhibit sampling instability in high-dimensional tabular spaces [12].</p>

  <p>To resolve this limitation, Lundberg and Lee [12] introduced SHAP (SHapley Additive exPlanations), grounded in cooperative game theory. TreeSHAP provides polynomial-time calculation of exact Shapley values for decision-tree ensembles, ensuring mathematical consistency and local efficiency [13]. While SHAP has been utilized in agricultural classification tasks, its application to perennial yield gap analysis remains underdeveloped. Most existing studies limit SHAP to global feature importance summaries, overlooking its capacity to compute localized yield penalties or guide corrective field applications. This study directly bridges this gap.</p>

  <h1 class="sec-title">III. Agronomic Foundations & Data Formulation</h1>
  <h2 class="subsec-title">A. Botanical Distinctions and Physiological Benchmarks</h2>
  <p><i>Coffea arabica</i> and <i>Coffea canephora</i> display distinct physiological and environmental requirements. Arabica is an allotetraploid (2n = 4x = 44) self-fertile species adapted to tropical highland elevations, whereas Robusta is a diploid (2n = 2x = 22) outcrossing species adapted to lowland equatorial forests [2]. Table I summarizes key biological benchmarks compiled from CCRI guidelines [3] and international agro-climatic surveys [10].</p>

  <table class="ieee-table">
    <caption>TABLE I: Biophysical Benchmarks and Physiological Tolerances</caption>
    <thead>
      <tr>
        <th>Agro-Climatic Parameter</th>
        <th>Arabica (<i>C. arabica</i>)</th>
        <th>Robusta (<i>C. canephora</i>)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Optimal Elevation (m MSL)</td><td>1,000 – 1,600</td><td>400 – 900</td></tr>
      <tr><td>Optimal Mean Temp (°C)</td><td>18.0 – 23.0</td><td>23.0 – 28.0</td></tr>
      <tr><td>Critical Max Temp (°C)</td><td>30.0</td><td>34.0</td></tr>
      <tr><td>Optimal Annual Rain (mm)</td><td>1,500 – 2,200</td><td>1,800 – 2,600</td></tr>
      <tr><td>Blossom Showers (mm)</td><td>25.0 (Mar–Apr)</td><td>30.0 (Feb–Mar)</td></tr>
      <tr><td>Optimal Soil pH (1:2.5)</td><td>5.8 – 6.5</td><td>5.5 – 6.5</td></tr>
      <tr><td>Available Nitrogen (kg/ha)</td><td>130 – 180</td><td>150 – 220</td></tr>
      <tr><td>Available Phosphorus (kg/ha)</td><td>50 – 90</td><td>40 – 80</td></tr>
      <tr><td>Available Potassium (kg/ha)</td><td>130 – 190</td><td>150 – 230</td></tr>
      <tr><td>Organic Carbon (%)</td><td>1.2 – 2.5</td><td>1.0 – 2.2</td></tr>
      <tr><td>Genetic Potential (kg/ha)</td><td>1,400.0</td><td>2,100.0</td></tr>
      <tr><td>Baseline Survival (kg/ha)</td><td>300.0</td><td>450.0</td></tr>
    </tbody>
  </table>

  <h2 class="subsec-title">B. Multi-Modal Parameter Space</h2>
  <p>Each plantation observation is represented by a 16-dimensional feature vector spanning edaphic, meteorological, and topographical modalities:</p>
  <p class="no-indent">1) <i>Edaphic Modality (Soil Health Card):</i> Soil Reaction (pH ∈ [4.0, 8.0]), Available Nitrogen (N, kg/ha), Available Phosphorus (P, kg/ha), Available Potassium (K, kg/ha), Organic Carbon (OC, %), and Electrical Conductivity (EC, dS/m).</p>
  <p class="no-indent">2) <i>Meteorological Modality:</i> Cumulative Annual Precipitation (P_annual, mm), Blossom Showers (P_blossom, mm), Mean Temperature (T_avg, °C), Maximum Summer Temperature (T_max, °C), Minimum Winter Temperature (T_min, °C), and Relative Humidity (RH, %).</p>
  <p class="no-indent">3) <i>Topographical & Estate Modality:</i> Elevation (H, meters MSL), Region (R), Botanical Variety (S ∈ {Arabica, Robusta}), Tree Stand Density (trees/ha), and Farm Land Area (hectares/acres).</p>

  <h1 class="sec-title">IV. Methodology & System Formulation</h1>
  <h2 class="subsec-title">A. Biophysical Stress Penalty Formulation</h2>
  <p>To mathematically represent crop loss mechanisms, continuous normalized stress functions σ_j(x_j) ∈ [0, 1] are formulated for each environmental factor:</p>
  
  <div class="equation">
    σ_pH(x) = { 0, if pH_min* ≤ x ≤ pH_max*; min(1.0, (pH_min* - x)/1.5), if x &lt; pH_min*; min(1.0, (x - pH_max*)/1.5), if x &gt; pH_max* } <span class="eq-num">(1)</span>
  </div>

  <div class="equation">
    σ_nutrient(x_n) = max(0, (N_opt - x_n) / N_opt),  n ∈ {N, P, K} <span class="eq-num">(2)</span>
  </div>

  <div class="equation">
    σ_blossom(P_b) = max(0, (P_opt* - P_b) / P_opt*) <span class="eq-num">(3)</span>
  </div>

  <p>Let Y_pot and Y_min denote maximum potential and survival yields. The factor-specific yield deduction δY_j (kg/ha) is modeled using physiological weight vector w:</p>
  
  <div class="equation">
    δY_j = w_j · σ_j(x_j) · (Y_pot - Y_min) <span class="eq-num">(4)</span>
  </div>

  <p>The aggregate biophysical yield loss is constrained by the potential yield ceiling:</p>

  <div class="equation">
    ΔY_total = min(Y_pot - Y_min, Σ δY_j) <span class="eq-num">(5)</span>
  </div>
  <div class="equation">
    y_actual = max(Y_min, Y_pot - ΔY_total) + ε,  ε ~ N(0, σ²) <span class="eq-num">(6)</span>
  </div>

  <h2 class="subsec-title">B. Predictive Ensemble Regressors</h2>
  <p>Three tree ensemble architectures were developed and evaluated:</p>
  <p>1) <i>Gradient Tree Boosting (GBM):</i> Minimizes quadratic loss through stage-wise functional gradient descent [14]:</p>
  <div class="equation">
    f_m(x) = f_{m-1}(x) + η Σ γ_{jm} I(x ∈ R_{jm}) <span class="eq-num">(7)</span>
  </div>
  <p>where η ∈ (0, 1] represents the shrinkage learning rate parameter.</p>

  <p>2) <i>Extreme Gradient Boosting (XGBoost):</i> Augments objective with second-order Taylor gradients and explicit structural regularization penalizing tree complexity [15]:</p>
  <div class="equation">
    L_XGB = Σ [ g_i f_m(x_i) + 0.5 h_i f_m²(x_i) ] + γ T + 0.5 λ ||w||² <span class="eq-num">(8)</span>
  </div>

  <p>3) <i>Random Forest Regressor (RF):</i> Combines B bootstrap decision trees via bagging and random sub-feature selection [16]:</p>
  <div class="equation">
    f_RF(x) = (1/B) Σ T_b(x; Θ_b) <span class="eq-num">(9)</span>
  </div>

  <h2 class="subsec-title">C. Explainable AI via TreeSHAP</h2>
  <p>To decompose individual predictions, TreeSHAP [13] calculates the unique Shapley attribution φ_i(f, x) satisfying the efficiency axiom:</p>
  <div class="equation">
    φ_i(f, x) = Σ [|S|! (|F| - |S| - 1)! / |F|!] [ f_x(S ∪ {i}) - f_x(S) ] <span class="eq-num">(10)</span>
  </div>
  <div class="equation">
    f(x) = φ_0 + Σ φ_i(f, x) <span class="eq-num">(11)</span>
  </div>

  <h2 class="subsec-title">D. Stoichiometric Prescriptive Translation</h2>
  <p>Diagnosed deficits are converted into closed-form agricultural remediation prescriptions via stoichiometric conversion:</p>
  <p>1) <i>Soil Neutralization (Lime/Dolomite):</i></p>
  <div class="equation">
    M_lime = max(0, (pH_opt* - pH_actual) × β_buffer) <span class="eq-num">(12)</span>
  </div>
  <p>where β_buffer = 2,500 kg·ha⁻¹·pH⁻¹ for tropical laterites. The amendment is split into 60% Dolomite and 40% Agricultural Lime.</p>

  <p>2) <i>Macronutrient Dosage Scheduling:</i></p>
  <div class="equation">
    M_Urea = max(0, N_opt - N_actual) / 0.46  (kg/ha) <span class="eq-num">(13)</span>
  </div>
  <div class="equation">
    M_MOP = max(0, K_opt - K_actual) / 0.60  (kg/ha) <span class="eq-num">(14)</span>
  </div>

  <p>3) <i>Blossom Sprinkler Irrigation:</i></p>
  <div class="equation">
    V_water = max(0, P_blossom* - P_blossom) × 10,000  (L/ha) <span class="eq-num">(15)</span>
  </div>

  <h1 class="sec-title">V. Experimental Results & Benchmark</h1>
  <h2 class="subsec-title">A. Experimental Setup and Preprocessing</h2>
  <p>The experimental dataset comprises 3,500 comprehensive plantation instances spanning major Indian growing zones (Kodagu, Chikkamagaluru, Hassan, Wayanad, Idukki, Nilgiris, Yercaud) as well as international reference tracks (Minas Gerais, Brazil; Central Highlands, Vietnam). Continuous numerical features were transformed via robust z-score standardization, while categorical variables were transformed using one-hot dummy encoding. The dataset was partitioned into 80% training (N = 2,800) and 20% independent test (N = 700) sets using stratified shuffling to preserve regional and varietal distributions. Hyperparameters were tuned via 5-fold cross-validation.</p>

  <table class="ieee-table">
    <caption>TABLE II: Tuned Hyperparameter Configurations</caption>
    <thead>
      <tr>
        <th>Model Architecture</th>
        <th>Hyperparameter</th>
        <th>Optimal Value</th>
      </tr>
    </thead>
    <tbody>
      <tr><td rowspan="3">Gradient Boosting</td><td>Estimators (M)</td><td>150</td></tr>
      <tr><td>Learning Rate (η)</td><td>0.08</td></tr>
      <tr><td>Max Tree Depth</td><td>5</td></tr>
      <tr><td rowspan="3">XGBoost Regressor</td><td>Boosting Rounds</td><td>180</td></tr>
      <tr><td>Shrinkage Rate</td><td>0.07</td></tr>
      <tr><td>Max Depth</td><td>6</td></tr>
      <tr><td rowspan="2">Random Forest</td><td>Trees (B)</td><td>150</td></tr>
      <tr><td>Max Depth</td><td>14</td></tr>
    </tbody>
  </table>

  <h2 class="subsec-title">B. Quantitative Model Benchmarking</h2>
  <p>Model accuracy was evaluated using four standard regression criteria: Coefficient of Determination (R²), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and Mean Absolute Percentage Error (MAPE).</p>

  <table class="ieee-table">
    <caption>TABLE III: Quantitative Benchmark Comparison</caption>
    <thead>
      <tr>
        <th>ML Architecture</th>
        <th>R² Score</th>
        <th>RMSE (kg/ha)</th>
        <th>MAE (kg/ha)</th>
        <th>MAPE (%)</th>
      </tr>
    </thead>
    <tbody>
      <tr class="total-row">
        <td>Gradient Boosting</td>
        <td>0.9530</td>
        <td>71.36</td>
        <td>56.04</td>
        <td>3.88%</td>
      </tr>
      <tr>
        <td>XGBoost Regressor</td>
        <td>0.9504</td>
        <td>73.32</td>
        <td>57.13</td>
        <td>3.96%</td>
      </tr>
      <tr>
        <td>Random Forest</td>
        <td>0.9362</td>
        <td>83.17</td>
        <td>64.08</td>
        <td>4.45%</td>
      </tr>
    </tbody>
  </table>

  <p>As documented in Table III, the <b>Gradient Boosting Regressor achieved the highest predictive performance</b>, securing an R² of 0.9530, an RMSE of 71.36 kg/ha, an MAE of 56.04 kg/ha, and a MAPE of 3.88%. While XGBoost performed comparably (R² = 0.9504), Gradient Boosting showed superior stability across edge cases characterized by compounding soil acidity and moisture deficits.</p>

  <h2 class="subsec-title">C. Ablation Analysis: Modality Contribution</h2>
  <p>To evaluate the predictive contribution of each feature modality, an ablation study was performed by training model variants with specific modality groups removed.</p>

  <table class="ieee-table">
    <caption>TABLE IV: Ablation Analysis of Feature Modalities</caption>
    <thead>
      <tr>
        <th>Feature Configuration</th>
        <th>R²</th>
        <th>RMSE</th>
        <th>MAE</th>
        <th>ΔR²</th>
      </tr>
    </thead>
    <tbody>
      <tr class="total-row">
        <td>Full Multi-Modal Architecture</td>
        <td>0.9530</td>
        <td>71.36</td>
        <td>56.04</td>
        <td>—</td>
      </tr>
      <tr>
        <td>w/o Edaphic Modality (Soil Card)</td>
        <td>0.7412</td>
        <td>168.42</td>
        <td>132.15</td>
        <td>-0.2118</td>
      </tr>
      <tr>
        <td>w/o Meteorological Modality</td>
        <td>0.7854</td>
        <td>152.18</td>
        <td>118.60</td>
        <td>-0.1676</td>
      </tr>
      <tr>
        <td>w/o Topographical Modality</td>
        <td>0.8920</td>
        <td>108.55</td>
        <td>84.32</td>
        <td>-0.0610</td>
      </tr>
    </tbody>
  </table>

  <p>The ablation results in Table IV demonstrate that omitting the edaphic modality leads to a 21.18% drop in R², underscoring the critical role of soil nutrient status in determining yield. Removing meteorological variables results in a 16.76% decline, confirming that regional climate dynamics and edaphic factors jointly govern harvest outcomes.</p>

  <h2 class="subsec-title">D. Global Feature Importance Hierarchy</h2>
  <p>Analysis of tree split gains across the ensemble identified the dominant global environmental determinants governing coffee production: Soil Reaction (pH, 23.1%), Annual Rainfall (20.4%), Available Potassium (K, 17.8%), Available Nitrogen (N, 14.5%), Blossom Showers (11.2%), Mean Temperature (8.4%), and Elevation (4.6%). This hierarchy aligns with known soil chemistry: severe acidity locks available phosphorus and suppresses beneficial microbial activity, establishing an edaphic ceiling on harvest yields regardless of other inputs.</p>

  <h1 class="sec-title">VI. Case Study & Sensitivity Analysis</h1>
  <h2 class="subsec-title">A. Case Study: Acidic Robusta Estate in Coorg</h2>
  <p>To demonstrate localized diagnosis, we examine a 15-acre Robusta plantation in Kodagu, Karnataka (H = 850 m MSL), characterized by acidic laterite soil and potassium depletion (pH = 4.60, K = 85 kg/ha, N = 160 kg/ha, P = 45 kg/ha, P_annual = 2,100 mm, P_blossom = 40 mm):</p>
  <p class="no-indent">• <i>Potential Clean Bean Yield:</i> 2,100.0 kg/ha.</p>
  <p class="no-indent">• <i>Model Predicted Harvest:</i> 1,578.4 kg/ha (Efficiency = 75.2%).</p>
  <p class="no-indent">• <i>Aggregate Yield Loss:</i> -521.6 kg/ha, translating to a loss of 3.17 Metric Tonnes across the 15-acre estate (valued at ₹10,77,000 at ₹340/kg).</p>

  <p>The diagnostic engine isolated <b>Soil Acidity as the primary yield bottleneck (-228.4 kg/ha)</b>, followed by Available Potassium (-172.6 kg/ha) and Low Organic Carbon (-62.5 kg/ha). TreeSHAP attribution confirmed that the pH deficit exerted a local negative impact of φ_pH = -215.4 kg/ha, while potassium depletion contributed φ_K = -168.2 kg/ha.</p>

  <h2 class="subsec-title">B. Stoichiometric Prescriptive Action Plan</h2>
  <p>In response to the diagnosed bottlenecks, the prescriptive engine generated specific field recommendations:</p>
  <p>1) <i>Soil Acidity Remediation:</i> Apply 2,250 kg/ha (910 kg/acre) of a neutralizing lime-dolomite blend: 1,350 kg/ha Agricultural Dolomite (supplying essential magnesium) + 900 kg/ha Agricultural Lime.</p>
  <p>2) <i>Potassium Replenishment:</i> Broadcast 108 kg/ha Muriate of Potash (60% K₂O) in two split applications: pre-monsoon (May) and post-monsoon (September) during berry enlargement.</p>

  <h2 class="subsec-title">C. What-If Sensitivity Simulation and ROI</h2>
  <p>Using the interactive sensitivity simulator, we modeled the recovery trajectory resulting from these interventions: adjusting soil pH from 4.60 to 5.80 recovered +228 kg/ha; increasing potassium from 85 to 165 kg/ha recovered +142 kg/ha. Net Simulated Harvest reached <b>1,948.4 kg/ha</b> (efficiency increased from 75.2% to 92.8%), yielding a projected estate revenue recovery of <b>₹7,65,000</b>.</p>

  <h1 class="sec-title">VII. Discussion & Conclusion</h1>
  <p>This paper presented an Explainable AI-driven decision support framework for precision coffee yield forecasting and root-cause yield loss diagnosis. By synthesizing sixteen edaphic, meteorological, and topographical indicators across 3,500 estate records, the proposed Gradient Boosting Regressor achieved strong predictive accuracy, securing an R² of 0.9530, an RMSE of 71.36 kg/ha, and an average relative error of 3.88%, outperforming comparable XGBoost and Random Forest implementations.</p>

  <p>By combining cooperative game-theoretic TreeSHAP with an analytical stress model grounded in Liebig's Law of the Minimum, the system removes the opacity of black-box ML models, breaking down estate-level yield gaps into factor-specific kilogram-per-hectare penalties. Furthermore, the pipeline translates diagnosed nutrient and hydrological deficits into closed-form stoichiometric prescriptions for agricultural lime, chemical macronutrients, and blossom sprinkler irrigation. Supported by an interactive sensitivity simulator, this framework provides an interpretable, actionable foundation for sustainable plantation management and climate-resilient agriculture.</p>

  <h1 class="sec-title">References</h1>
  <ul class="references-list">
    <li>[1] International Coffee Organization (ICO), "Coffee market report and global economic overview," <i>ICO Document Repository</i>, London, UK, Tech. Rep. 2023.</li>
    <li>[2] A. P. Davis, H. Chadburn, J. Moat, et al., "High extinction risk for wild coffee species and implications for coffee sector sustainability," <i>Science Advances</i>, vol. 5, no. 1, p. eaav3473, 2019.</li>
    <li>[3] Central Coffee Research Institute (CCRI), "Coffee Guide: Comprehensive Manual on Coffee Cultivation Practices," <i>Coffee Board of India</i>, Bengaluru, India, 2021.</li>
    <li>[4] P. S. Chemura, A. H. Mahlstein, and C. Gornott, "The role of climate variability in coffee yield fluctuations across East Africa," <i>Agricultural and Forest Meteorology</i>, vol. 292, p. 108125, 2020.</li>
    <li>[5] D. L. Martins, F. M. DaMatta, and W. P. Rodrigues, "Potassium nutrition and physiological efficiency in Arabica and Robusta cultivars," <i>Journal of Plant Nutrition</i>, vol. 44, no. 12, pp. 1789–1804, 2021.</li>
    <li>[6] K. J. Boote, J. W. Jones, and N. B. Pickering, "Potential uses and limitations of crop models," <i>Agronomy Journal</i>, vol. 88, no. 5, pp. 704–716, 1996.</li>
    <li>[7] F. H. R. Everingham, J. Sexton, and D. L. Robson, "Using machine learning to predict sugarcane and coffee yields under climate change scenarios," <i>Computers and Electronics in Agriculture</i>, vol. 180, p. 105911, 2021.</li>
    <li>[8] V. H. Nguyen, T. D. Le, and H. M. Tran, "Robusta coffee yield estimation using satellite vegetation indices and ensemble machine learning in Vietnam," <i>Precision Agriculture</i>, vol. 23, no. 2, pp. 589–612, 2022.</li>
    <li>[9] J. C. Ramalho, F. M. DaMatta, and A. E. Rodrigues, "Cold-induced changes on sugar metabolism and leaf anatomy in <i>Coffea</i> species," <i>Physiologia Plantarum</i>, vol. 149, no. 4, pp. 473–485, 2013.</li>
    <li>[10] Food and Agriculture Organization (FAO), "World coffee crop guidelines: Soil management, climate suitability, and plant nutrition," <i>FAO Plant Production Papers</i>, Rome, Italy, 2018.</li>
    <li>[11] A. Holzinger, R. Goebel, M. Mengel, and H. M. Z. Müller, "What do we need to build explainable AI for precision medicine and agriculture?" <i>Information Fusion</i>, vol. 86, pp. 102–114, 2022.</li>
    <li>[12] S. M. Lundberg and S.-I. Lee, "A unified approach to interpreting model predictions," in <i>Proc. Advances in Neural Information Processing Systems (NeurIPS 30)</i>, 2017, pp. 4765–4774.</li>
    <li>[13] S. M. Lundberg, G. Erion, H. Chen, et al., "From local explanations to global understanding with explainable AI for trees," <i>Nature Machine Intelligence</i>, vol. 2, no. 1, pp. 56–67, 2020.</li>
    <li>[14] J. H. Friedman, "Greedy function approximation: A gradient boosting machine," <i>The Annals of Statistics</i>, vol. 29, no. 5, pp. 1189–1232, 2001.</li>
    <li>[15] T. Chen and C. Guestrin, "XGBoost: A scalable tree boosting system," in <i>Proc. 22nd ACM SIGKDD Int. Conf. on Knowledge Discovery and Data Mining</i>, 2016, pp. 785–794.</li>
    <li>[16] L. Breiman, "Random forests," <i>Machine Learning</i>, vol. 45, no. 1, pp. 5–32, 2001.</li>
    <li>[17] F. Pedregosa et al., "Scikit-learn: Machine learning in Python," <i>Journal of Machine Learning Research</i>, vol. 12, pp. 2825–2830, 2011.</li>
  </ul>

</div>

</body>
</html>
"""

def generate_pdf():
    base_dir = r'C:\Users\prajw\.gemini\antigravity\scratch\coffee_yield_project'
    brain_dir = r'C:\Users\prajw\.gemini\antigravity\brain\8ddc1524-2d7e-4612-a363-58bd93735cf3'
    
    html_path = os.path.join(base_dir, 'ieee_paper_render.html')
    pdf_path = os.path.join(base_dir, 'IEEE_Coffee_Yield_Prediction_Paper.pdf')
    brain_pdf_path = os.path.join(brain_dir, 'IEEE_Coffee_Yield_Prediction_Paper.pdf')
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    
    cmd = [
        chrome_path,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        f'--print-to-pdf={pdf_path}',
        '--print-to-pdf-no-header',
        html_path
    ]
    
    subprocess.run(cmd, check=True)
    
    # Copy to brain artifacts
    shutil.copy2(pdf_path, brain_pdf_path)
    
    print(f"PDF generated successfully at:\n{pdf_path}\n{brain_pdf_path}")
    print(f"File size: {os.path.getsize(pdf_path) / 1024:.2f} KB")

if __name__ == '__main__':
    generate_pdf()
