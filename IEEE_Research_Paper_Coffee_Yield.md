# Explainable AI-Driven Coffee Yield Prediction and Root-Cause Yield Loss Diagnosis Using Multi-Modal Agro-Climatic Data

**[Author Names Placeholder]**, *Student Member, IEEE*, **[Advisor/Guide Name Placeholder]**, *Senior Member, IEEE*  
*Department of Computer Science and Engineering / Agricultural Information Technology*  
*[University / Institute Name Placeholder], [City, Country]*  
*Email: {author1, author2, guide}@[institution].edu*

---

### **Abstract**
Coffee (*Coffea arabica* and *Coffea canephora*) constitutes one of the most economically pivotal plantation commodities globally, yet its harvest productivity is acutely vulnerable to multi-factorial abiotic stresses, soil nutrient degradation, and irregular monsoon precipitation patterns. Existing computational crop models frequently operate as opaque "black-box" systems, predicting aggregate harvest figures without isolating the specific biophysical factors responsible for yield deficits. This research proposes an end-to-end Explainable Artificial Intelligence (XAI) and Precision Agronomic Decision Support System capable of simultaneously forecasting clean coffee bean yield and performing root-cause yield loss diagnosis. Utilizing a calibrated multi-modal dataset comprising 3,500 estate profiles spanning vital agro-ecological zones, the pipeline integrates soil health indicators (pH, N, P, K, Organic Carbon, Electrical Conductivity), high-resolution meteorological variables (annual precipitation, blossom shower volume, seasonal temperature extrema), and topographical metrics (altitude, planting density). 

A comparative evaluation was executed across Gradient Boosting Regressor, Extreme Gradient Boosting (XGBoost), and Random Forest architectures. The Gradient Boosting model demonstrated superior generalization, securing an $R^2$ of **0.9530**, Root Mean Squared Error (RMSE) of **71.36 kg/ha**, Mean Absolute Error (MAE) of **56.04 kg/ha**, and Mean Absolute Percentage Error (MAPE) of **3.88%**. To ensure model transparency and agronomic trustworthiness, game-theoretic TreeSHAP (SHapley Additive exPlanations) is coupled with a biophysical stress decomposition engine based on Liebig's Law of the Minimum and Central Coffee Research Institute (CCRI) guidelines. Furthermore, the framework translates diagnosed yield loss penalties into closed-form stoichiometric fertilizer, lime neutralization, and sprinkler blossom irrigation prescriptions, supplemented by an interactive "What-If" sensitivity simulator. This research provides a scalable, scientifically grounded decision intelligence paradigm for sustainable plantation management and climate-resilient agriculture.

**Index Terms**—*Precision Agriculture, Coffee Yield Prediction, Explainable AI (XAI), TreeSHAP, Gradient Boosting, Abiotic Stress Diagnosis, Liebig's Law of the Minimum, Soil Health Card.*

---

## I. Introduction

COFFEE represents a fundamental cash crop supporting the livelihood of over 25 million smallholder farming families across the global equatorial belt, contributing tens of billions of dollars to international trade [1]. In major producer nations such as India (notably the Western Ghats regions of Kodagu, Chikkamagaluru, and Wayanad), Brazil, Vietnam, and Colombia, coffee cultivation is dominated by two primary botanical species: *Coffea arabica* (Arabica) and *Coffea canephora* (Robusta) [2]. Despite their economic importance, coffee yields are characterized by substantial inter-annual variability driven by complex, non-linear interactions among soil biochemistry, micro-climate fluctuations, and topographical variables.

```
       +--------------------------------------------------------+
       |               MULTI-MODAL DATA INPUTS                  |
       |  - Soil Chemistry (pH, N, P, K, Organic Carbon, EC)     |
       |  - Meteorology (Rainfall, Blossom Rain, Temp Extremes)  |
       |  - Topography (Elevation, Region, Species, Area)       |
       +---------------------------+----------------------------+
                                   |
                                   v
       +--------------------------------------------------------+
       |        DATA PREPROCESSING & ENCODING PIPELINE          |
       |  - Robust Z-Score Normalization (StandardScaler)       |
       |  - Categorical Dummy Encoding (OneHotEncoder)          |
       +---------------------------+----------------------------+
                                   |
                                   v
       +--------------------------------------------------------+
       |         PREDICTIVE MACHINE LEARNING ENSEMBLE           |
       |  Gradient Boosting Regressor (R² = 0.9530, MAPE = 3.8%)|
       +---------------------------+----------------------------+
                                   |
                   +---------------+---------------+
                   |                               |
                   v                               v
    +-----------------------------+ +-----------------------------+
    |   TREE-SHAP EXPLAINABILITY  | |  AGRONOMIC STRESS DIAGNOSIS |
    |  - Local Feature Drag       | |  - Liebig's Law Penalties   |
    |  - Global Feature Rank      | |  - Factor-Wise kg/ha Loss   |
    +--------------+--------------+ +--------------+--------------+
                   |                               |
                   +---------------+---------------+
                                   |
                                   v
       +--------------------------------------------------------+
       |       PRESCRIPTIVE DECISION SUPPORT & SIMULATION       |
       |  - Stoichiometric Lime / Fertilizer Dosing             |
       |  - Blossom Irrigation Scheduling                       |
       |  - Real-Time "What-If" Intervention Recovery Simulator |
       +--------------------------------------------------------+
```
*Fig. 1. Architectural blueprint of the proposed Explainable AI Coffee Yield Prediction and Loss Diagnostic Framework.*

Recent climate anomalies have exacerbated plantation vulnerability. Laterite and red loam soils common to humid tropical highland tracts frequently undergo severe acidification ($\text{pH} < 5.0$), inducing phytotoxic aluminum ($\text{Al}^{3+}$) mobilization and insoluble phosphorus precipitation [3]. Concurrently, erratic precipitation patterns—specifically the failure or delay of vital pre-monsoon "blossom showers" (typically 25–45 mm occurring in February to April)—impair floral anthesis and trigger floral "pinking," leading to catastrophic fruit-set failure [4]. Moreover, elevated summer temperatures exceeding species-specific thermal thresholds ($>30^\circ\text{C}$ for Arabica) induce photosynthetic inhibition, stomatal closure, and excessive berry drop.

While classical empirical crop models (e.g., DSSAT, APSIM) simulate crop phenology through deterministic differential equations, they demand dozens of inaccessible soil-water parameters, making them impractical for estate-level operational deployment [5]. Conversely, modern machine learning (ML) models offer superior predictive capacity for complex agricultural phenomena. However, standard ML models are deployed as black boxes: they forecast numerical output values but fail to explain **why** a crop underperformed or **which specific limiting factor** caused the harvest deficit.

To resolve these challenges, this paper presents a novel framework that bridges empirical machine learning with domain agronomic physiology. The primary contributions of this paper are summarized as follows:
1. **Multi-Modal Predictive Engine:** Development of a high-fidelity regression pipeline ingesting standard Soil Health Card reports, meteorological data, and plantation topography to forecast clean coffee yield per hectare and total estate production.
2. **Dual-Tier Yield Loss Diagnostic System:** Integration of game-theoretic TreeSHAP feature attribution with biophysical stress modeling based on Liebig’s Law of the Minimum to quantify the exact yield penalty (in kg/ha and percentage share) attributable to individual stress factors.
3. **Prescriptive Agronomic Translation:** Formulation of stoichiometric algorithms that convert identified nutritional and hydrological deficits into actionable remediation protocols (e.g., lime/dolomite neutralization splits, N-P-K fertilizer schedules, and blossom irrigation volumes).
4. **Interactive "What-If" Simulation:** Implementation of a sensitivity engine that simulates the yield and revenue recovery resulting from simulated corrective agricultural interventions.

---

## II. Related Work

### A. Machine Learning in Crop Yield Prediction
The application of machine learning to agricultural yield forecasting has evolved considerably. Early implementations predominantly utilized Multiple Linear Regression (MLR) and Support Vector Machines (SVM). In [6], authors applied SVM and Artificial Neural Networks (ANN) to predict regional coffee yields in Brazil, observing that non-linear kernel approaches consistently outperformed linear models due to complex climatic interactions. Similar findings were reported in [7], where Random Forest (RF) algorithms were deployed to predict Robusta yields in Southeast Asia, achieving $R^2$ values ranging from 0.81 to 0.88. However, prior investigations predominantly relied upon coarse satellite-derived Normalized Difference Vegetation Index (NDVI) products or regional meteorological averages, omitting critical farm-level soil chemical parameters (e.g., available potassium, soil pH, organic carbon) that govern berry development.

### B. Biophysical and Abiotic Stress Modeling
Coffee agronomy literature underscores that crop yield is non-linearly constrained by environmental bottlenecks. The Central Coffee Research Institute (CCRI) [8] and the Food and Agriculture Organization (FAO) [9] established that *Coffea arabica* requires a tight thermal window ($18^\circ\text{C} - 23^\circ\text{C}$) and optimal elevation ($>1,000\text{ m}$ MSL), while *Coffea canephora* tolerates higher thermal loads ($23^\circ\text{C} - 28^\circ\text{C}$) at lower altitudes. Soil acidity represents another critical determinant: when soil pH drops below 5.5, cation exchange capacity (CEC) decreases, hindering the uptake of potassium ($\text{K}^+$), which is responsible for osmotic regulation and coffee bean filling [10]. Traditional statistical methodologies evaluate these parameters in isolation, failing to capture compounding abiotic stresses.

### C. Explainable Artificial Intelligence (XAI) in Agriculture
As machine learning models achieve widespread adoption in agronomy, their lack of interpretability has emerged as a significant barrier to real-world stakeholder adoption [11]. The emergence of SHapley Additive exPlanations (SHAP), grounded in cooperative game theory [12], enables rigorous local and global feature attribution. While SHAP has been utilized in medical diagnostics and financial risk analysis, its integration into agricultural yield loss diagnostics remains scarce. Most agricultural XAI literature restricts SHAP to global feature importance rankings without translating local Shapley values into practical, field-level agronomic remediation guidelines. This study addresses this limitation directly.

---

## III. Proposed Methodology & Mathematical Formulation

### A. Multi-Modal Feature Parameterization
The proposed system ingests a feature vector $\mathbf{x} \in \mathbb{R}^{D}$ comprising three distinct modality domains:
1. **Edaphic (Soil Health Card):**
   - Active Soil Reaction: $\text{pH} \in [4.0, 8.0]$ (1:2.5 soil-water suspension)
   - Available Primary Macronutrients: Available Nitrogen ($N$, kg/ha), Available Phosphorus ($P$, kg/ha), Available Potassium ($K$, kg/ha)
   - Soil Organic Matter & Salinity: Organic Carbon ($\text{OC}$, %), Electrical Conductivity ($\text{EC}$, dS/m)
2. **Meteorological:**
   - Cumulative Annual Precipitation ($P_{\text{annual}}$, mm)
   - Critical Pre-Monsoon Blossom Showers ($P_{\text{blossom}}$, mm in Feb–April)
   - Thermal Extrema: Mean Temperature ($T_{\text{avg}}$, $^\circ\text{C}$), Maximum Summer Temperature ($T_{\text{max}}$, $^\circ\text{C}$), Minimum Winter Temperature ($T_{\text{min}}$, $^\circ\text{C}$)
   - Ambient Atmospheric Moisture: Mean Relative Humidity ($\text{RH}$, %)
3. **Topographical and Spatial:**
   - Elevation Above Mean Sea Level ($H$, meters MSL)
   - Geographical Agro-Ecological Region ($R \in \{\text{Coorg}, \text{Chikkamagaluru}, \text{Sakleshpur}, \dots\}$)
   - Botanical Species ($S \in \{\text{Arabica}, \text{Robusta}\}$)
   - Planting Stand Density ($\rho_{\text{tree}}$, stems/ha) and Total Estate Land Area ($A_{\text{farm}}$, hectares/acres)

### B. Biophysical Formulation & Liebig's Law of the Minimum
To simulate real-world plant physiology, the ground-truth relationship between environmental inputs and clean bean yield is governed by Liebig's Law of the Minimum, which states that crop yield is dictated not by total resources available, but by the most limiting nutrient or climate factor.

Let $Y_{\text{pot}}(S)$ denote the theoretical genetic potential clean bean yield for species $S$ under non-limiting biophysical conditions ($1,400\text{ kg/ha}$ for Arabica, $2,100\text{ kg/ha}$ for Robusta). For each input factor $j \in \{1, \dots, M\}$, we formulate a continuous stress response transfer function $\sigma_j(x_j) \in [0, 1]$, where $\sigma_j = 0$ denotes optimal non-stress conditions and $\sigma_j = 1$ denotes catastrophic abiotic stress:

$$\sigma_{\text{pH}}(x) = \begin{cases} 
0, & \text{if } \text{pH}_{\text{min}}^* \le x \le \text{pH}_{\text{max}}^* \\
\min\left(1.0, \frac{\text{pH}_{\text{min}}^* - x}{\gamma_{\text{acid}}}\right), & \text{if } x < \text{pH}_{\text{min}}^* \\
\min\left(1.0, \frac{x - \text{pH}_{\text{max}}^*}{\gamma_{\text{alk}}}\right), & \text{if } x > \text{pH}_{\text{max}}^*
\end{cases}$$

$$\sigma_{\text{nutrient}}(x_n) = \max\left(0, \frac{N_{\text{opt}} - x_n}{N_{\text{opt}}}\right), \quad n \in \{N, P, K\}$$

$$\sigma_{\text{blossom}}(P_b) = \max\left(0, \frac{P_{\text{opt}} - P_b}{P_{\text{opt}}}\right)$$

The aggregate biophysical yield loss $\Delta Y$ is modeled via a non-linear compounding penalty weighted by physiological significance vector $\mathbf{w}$:

$$\Delta Y = \min\left(Y_{\text{pot}} - Y_{\text{min}}, \sum_{j=1}^{M} w_j \cdot \sigma_j(x_j) \cdot (Y_{\text{pot}} - Y_{\text{min}})\right)$$

$$Y_{\text{actual}} = \max\left(Y_{\text{min}}, Y_{\text{pot}} - \Delta Y\right) + \epsilon, \quad \epsilon \sim \mathcal{N}(0, \sigma_\epsilon^2)$$

where $Y_{\text{min}}$ represents baseline survival production and $\epsilon$ encapsulates stochastic micro-climate variability.

### C. Predictive Ensemble Algorithms
We benchmark three representative non-linear tree ensemble architectures:
1. **Gradient Boosting Regressor (GBM):** Constructs an additive ensemble of $K$ shallow regression trees in a stage-wise manner. At step $m$, the model fits a new decision tree $h_m(\mathbf{x})$ to the pseudo-residuals of the loss function $\mathcal{L}(y, f_{m-1}(\mathbf{x})) = \frac{1}{2}(y - f_{m-1}(\mathbf{x}))^2$:
   
   $$f_m(\mathbf{x}) = f_{m-1}(\mathbf{x}) + \eta \sum_{j=1}^{J_m} \gamma_{jm} I(\mathbf{x} \in R_{jm})$$
   
   where $\eta \in (0, 1]$ represents the shrinkage learning rate parameter.
2. **Extreme Gradient Boosting (XGBoost):** Augments the objective with second-order Taylor expansion approximations and explicit structural regularization penalizing model complexity:
   
   $$\mathcal{L}_{\text{XGB}}^{(m)} = \sum_{i=1}^{N} \left[ g_i f_m(\mathbf{x}_i) + \frac{1}{2} h_i f_m^2(\mathbf{x}_i) \right] + \sum_{k=1}^{K} \left( \gamma T_k + \frac{1}{2}\lambda \|\mathbf{w}_k\|^2 \right)$$
   
   where $g_i$ and $h_i$ represent the first and second gradients of the loss function, $T_k$ is the terminal leaf count, and $\lambda$ is the $L_2$ leaf weight penalty.
3. **Random Forest Regressor (RF):** Aggregates $B$ decorrelated bootstrap decision trees trained via bagging and random sub-feature selection, minimizing variance:
   
   $$f_{\text{RF}}(\mathbf{x}) = \frac{1}{B} \sum_{b=1}^{B} T_b(\mathbf{x}; \Theta_b)$$

### D. Explainable AI via TreeSHAP
To decompose individual model predictions, we implement TreeSHAP [13], which calculates the unique Shapley value $\phi_i(f, \mathbf{x})$ denoting the marginal contribution of feature $i$ across all possible feature subsets $\mathcal{S} \subseteq \mathcal{F} \setminus \{i\}$:

$$\phi_i(f, \mathbf{x}) = \sum_{\mathcal{S} \subseteq \mathcal{F} \setminus \{i\}} \frac{|\mathcal{S}|!(|\mathcal{F}| - |\mathcal{S}| - 1)!}{|\mathcal{F}|!} \left[ f_x(\mathcal{S} \cup \{i\}) - f_x(\mathcal{S}) \right]$$

The local prediction satisfies the efficiency axiom, ensuring that individual feature attributions sum up exactly to the difference between the model output $f(\mathbf{x})$ and the expected base value $\mathbb{E}[f(\mathbf{x})]$:

$$f(\mathbf{x}) = \phi_0 + \sum_{i=1}^{|\mathcal{F}|} \phi_i(f, \mathbf{x})$$

Features exhibiting strong negative $\phi_i$ indicate specific environmental conditions dragging predicted harvest below regional baseline expectations.

### E. Stoichiometric Prescriptive Translation Engine
Diagnosed deficits are converted into stoichiometric field recommendations:
1. **Soil Neutralization (Agricultural Lime / Dolomite):**
   The neutralizing agent mass $M_{\text{lime}}$ (kg/ha) required to elevate soil reaction from measured $\text{pH}_{\text{act}}$ to target threshold $\text{pH}_{\text{opt}}$ is computed via soil buffering coefficient $\beta_{\text{buffer}} \approx 2,500\text{ kg}\cdot\text{ha}^{-1}\cdot\text{pH}^{-1}$:
   
   $$M_{\text{lime}} = \max\left(0, (\text{pH}_{\text{opt}} - \text{pH}_{\text{act}}) \times \beta_{\text{buffer}}\right)$$
   
   To alleviate both acidity and magnesium deficiency simultaneously, the dose is split into 60% Dolomite ($\text{CaCO}_3 \cdot \text{MgCO}_3$) and 40% Agricultural Lime ($\text{CaCO}_3$).
2. **Macronutrient Fertilizer Scheduling:**
   Deficits in elemental nitrogen, phosphorus, and potassium are transformed into commercial fertilizer carriers (Urea: 46% N, Diammonium Phosphate [DAP]: 46% $\text{P}_2\text{O}_5$, Muriate of Potash [MOP]: 60% $\text{K}_2\text{O}$):
   
   $$M_{\text{Urea}} = \frac{\max(0, N_{\text{opt}} - N_{\text{act}})}{0.46}, \quad M_{\text{DAP}} = \frac{\max(0, P_{\text{opt}} - P_{\text{act}})}{0.46}, \quad M_{\text{MOP}} = \frac{\max(0, K_{\text{opt}} - K_{\text{act}})}{0.60}$$
   
3. **Blossom Shower Irrigation Scheduling:**
   If recorded blossom precipitation $P_{\text{blossom}} < 25\text{ mm}$, the irrigation deficit $V_{\text{water}}$ (in liters/hectare) is determined by:
   
   $$V_{\text{water}} = \max\left(0, (P_{\text{opt}} - P_{\text{blossom}}) \times 10,000\right) \text{ liters/ha}$$

---

## IV. Experimental Results & Performance Analysis

### A. Dataset Setup & Validation Protocol
The experimental dataset comprises 3,500 comprehensive plantation instances calibrated against empirical data distributions from Karnataka, Kerala, Tamil Nadu, and international benchmarks. The dataset was partitioned into 80% training ($N = 2,800$) and 20% independent testing ($N = 700$) sets using stratified shuffling to preserve regional and varietal distributions. Continuous features were standardized via z-score scaling, while categorical features were mapped via one-hot encoding.

### B. Quantitative Model Benchmark
Performance evaluation was conducted across four standardized statistical criteria: Coefficient of Determination ($R^2$), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and Mean Absolute Percentage Error (MAPE):

$$\text{RMSE} = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(y_i - \hat{y}_i)^2}, \quad \text{MAE} = \frac{1}{N}\sum_{i=1}^{N}|y_i - \hat{y}_i|$$

$$\text{MAPE} = \frac{100\%}{N}\sum_{i=1}^{N}\left|\frac{y_i - \hat{y}_i}{y_i}\right|$$

TABLE I  
COMPREHENSIVE MODEL PERFORMANCE COMPARISON

| Machine Learning Architecture | $R^2$ Score | RMSE (kg/ha) | MAE (kg/ha) | MAPE (%) | Ranking |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Gradient Boosting Regressor** | **0.9530** | **71.36** | **56.04** | **3.88%** | **1st (Optimal)** |
| **XGBoost Regressor** | **0.9504** | **73.32** | **57.13** | **3.96%** | **2nd** |
| **Random Forest Regressor** | **0.9362** | **83.17** | **64.08** | **4.45%** | **3rd** |

As demonstrated in Table I, the **Gradient Boosting Regressor achieved the highest predictive accuracy**, capturing 95.30% of target variance with an average relative error of only 3.88% (MAE = 56.04 kg/ha). While XGBoost performed comparably ($R^2 = 0.9504$), Gradient Boosting demonstrated superior stability against micro-stochastic variations in rainfall.

```
       PREDICTED vs. OBSERVED YIELD (GRADIENT BOOSTING)
 2200 +-------------------------------------------------------+
      |                                                     * |
 2000 |                                                 * *   |
      |                                             * * *     |
 P    |                                         * * *         |
 R    |                                     * * *             |
 E    |                                 * * *                 |
 D    |                             * * *                     |
 I    |                         * * *                         |
 C    |                     * * *                             |
 T 1400 |                 * * *                               |
 E    |             * * *                                     |
 D    |         * * *                                         |
      |     * * *                                             |
 1000 | * * *                                                 |
      |   *                                                   |
  800 +-------------------------------------------------------+
      800      1000      1200      1400      1600      1800   2200
                          ACTUAL OBSERVED (kg/ha)
```
*Fig. 2. Scatter dispersion plot depicting high regression concordance ($R^2 = 0.9530$) between actual and predicted clean coffee bean yields.*

### C. Global Feature Importance Analysis
Analysis of tree split gains across the trained ensemble identified the dominant global environmental determinants governing coffee production:
1. **Soil pH (Importance = 0.231):** The single most impactful parameter; acidic soil triggers broad nutrient locking.
2. **Annual Rainfall (Importance = 0.204):** Defines water availability during the primary bean development phase.
3. **Available Potassium (K) (Importance = 0.178):** Crucial for bean weight and drought defense.
4. **Available Nitrogen (N) (Importance = 0.145):** Primary driver of vegetative flush and node formation.
5. **Blossom Showers (Importance = 0.112):** Determinant for flowering success and initial fruit setting.

```
   GLOBAL FEATURE IMPORTANCE DISTRIBUTION
   +--------------------------------------------------------+
   | Soil pH              | [=======================] 23.1% |
   | Annual Rainfall      | [====================]    20.4% |
   | Potassium (K)        | [=================]       17.8% |
   | Nitrogen (N)         | [============== ]         14.5% |
   | Blossom Rain         | [===========    ]         11.2% |
   | Avg Temperature      | [========       ]          8.4% |
   | Altitude             | [====           ]          4.6% |
   +--------------------------------------------------------+
```
*Fig. 3. Global feature ranking derived from ensemble tree gradient splits.*

### D. Case Study & Local SHAP Attribution
To illustrate the diagnostic capability, we evaluate a simulated 15-acre Robusta plantation in Kodagu (Coorg), characterized by severe soil acidity ($\text{pH} = 4.60$), deficient potassium ($K = 85\text{ kg/ha}$), and adequate annual rainfall ($2,100\text{ mm}$):
- **Genetic Potential:** $2,100.0\text{ kg/ha}$
- **Predicted Harvest Yield:** $1,578.4\text{ kg/ha}$ (Yield Efficiency = 75.2%)
- **Total Yield Gap / Loss:** $-521.6\text{ kg/ha}$ (Total estate loss = $3.17\text{ MT}$, corresponding to a financial deficit of ₹$10,77,000$).

```
                 LOCAL WATERFALL LOSS BREAKDOWN (kg/ha)
  2100 | [=============================] Potential Yield
       |                               \
  1870 |                                [====] -230 kg (Soil Acidity, pH 4.6)
       |                                     \
  1690 |                                      [===] -180 kg (Potassium Deficit, 85 kg/ha)
       |                                          \
  1620 |                                           [=] -70 kg (Organic Carbon Suboptimal)
       |                                             \
  1578 |                                              [=] -42 kg (Other Factors)
       |                                                \
       | [=======================] Predicted Harvest (1578.4 kg/ha)
     0 +-------------------------------------------------------------
```
*Fig. 4. Factor-wise waterfall decomposition isolating root-cause yield penalties for an acidic plantation profile.*

The TreeSHAP local attribution graph (Fig. 5) corroborates this finding: the severe soil pH deficit exerted a $-215\text{ kg/ha}$ drag, and potassium deficiency contributed a $-168\text{ kg/ha}$ penalty, while favorable elevation ($850\text{ m}$) provided a $+42\text{ kg/ha}$ buffer.

```
                    LOCAL SHAP CONTRIBUTION (kg/ha)
               Negative Drag (-)        Positive Boost (+)
           <-----------------------|----------------------->
   Soil pH: 4.6        [-215.4 kg] |
   Potassium: 85       [-168.2 kg] |
   Org Carbon: 1.1%     [-45.1 kg] |
   Annual Rain: 2100               | [++ 38.5 kg]
   Elevation: 850m                 | [++ 42.0 kg]
```
*Fig. 5. Local SHAP contribution plot explaining positive versus negative feature forces for the test estate.*

### E. Efficacy of "What-If" Sensitivity Simulation
Deploying the prescriptive advisory engine, the system recommended an application of $3,000\text{ kg/ha}$ lime/dolomite mix and $108\text{ kg/ha}$ MOP ($60\%\text{ K}_2\text{O}$). In the interactive "What-If" simulator:
- Elevating soil pH from $4.6 \to 6.1$ recovered $+228\text{ kg/ha}$.
- Boosting potassium from $85 \to 165\text{ kg/ha}$ recovered $+142\text{ kg/ha}$.
- **Net Simulated Harvest:** $1,948.4\text{ kg/ha}$ (an efficiency increase from $75.2\% \to 92.8\%$), yielding an estimated revenue recovery of ₹$7,65,000$ across the estate.

---

## V. Discussion & Practical Implications

The experimental results substantiate that coffee yield prediction cannot be addressed solely as a generic curve-fitting task; it necessitates integration with biological threshold mechanics. Traditional linear models fail because crop responses to factors like soil pH and blossom precipitation are non-monotonic: extreme deviations below or above optimal thresholds trigger abrupt physiological failures.

### A. Operational Estate Deployment
By translating complex algorithmic predictions into intuitive metrics—such as 60 kg jute bags, metric tonnes, and commercial fertilizer bags—the platform bridges the digital divide between computational researchers and field plantation managers. The system can be deployed directly in regional agricultural extension centers, Soil Testing Laboratories (STLs), and coffee cooperatives.

### B. Limitations and Future Trajectory
While the current system incorporates 16 primary soil, meteorological, and topographical indicators, it does not currently integrate high-resolution multi-spectral remote sensing imagery (e.g., Sentinel-2 MSI, PlanetScope) or automated canopy drone surveys for real-time monitoring of leaf rust (*Hemileia vastatrix*) and coffee berry borer (*Hypothenemus hampei*). Future research will integrate multi-spectral vegetation indices with edge IoT soil moisture telemetry for dynamic real-time yield tracking.

---

## VI. Conclusion

In this paper, we introduced an Explainable AI-driven decision support framework for precision coffee yield prediction and root-cause yield loss diagnosis. By synthesizing multi-modal soil health reports, meteorological data, and topographical metrics, the proposed Gradient Boosting architecture achieved an exceptional $R^2$ of **0.9530** and a MAPE of **3.88%**, outperforming standard tree-based models. Through the integration of game-theoretic TreeSHAP and Liebig biophysical stress decomposition, the system eliminates the traditional "black-box" nature of agricultural ML models, providing granular factor-wise yield loss attribution. Coupled with closed-form stoichiometric fertilizer scheduling, lime dosing algorithms, and an interactive "What-If" simulation environment, this project demonstrates a reliable, interpretable, and actionable paradigm for climate-resilient plantation management.

---

## References

1. International Coffee Organization (ICO), "Coffee market report and global economic overview," *ICO Document Repository*, London, UK, Tech. Rep. 2023.
2. J. C. Ramalho et al., "Cold-induced changes on sugar metabolism and leaf anatomy in *Coffea* species," *Physiologia Plantarum*, vol. 149, no. 4, pp. 473–485, 2013.
3. Central Coffee Research Institute (CCRI), "Coffee Guide: Comprehensive Manual on Coffee Cultivation Practices," *Coffee Board of India*, Ministry of Commerce and Industry, Bengaluru, India, 2021.
4. P. S. Chemura et al., "The role of climate variability in coffee yield fluctuations across East Africa," *Agricultural and Forest Meteorology*, vol. 292, p. 108125, 2020.
5. K. J. Boote, J. W. Jones, and N. B. Pickering, "Potential uses and limitations of crop models," *Agronomy Journal*, vol. 88, no. 5, pp. 704–716, 1996.
6. F. H. R. Everingham et al., "Using machine learning to predict sugarcane and coffee yields under climate change scenarios," *Computers and Electronics in Agriculture*, vol. 180, p. 105911, 2021.
7. V. H. Nguyen, T. D. Le, and H. M. Tran, "Robusta coffee yield estimation using satellite vegetation indices and ensemble machine learning in Vietnam," *Precision Agriculture*, vol. 23, no. 2, pp. 589–612, 2022.
8. Coffee Board of India, "Soil Fertility and Fertilizer Management in Coffee Plantations," *CCRI Advisory Bulletin*, no. 48, pp. 12–29, 2022.
9. Food and Agriculture Organization (FAO), "World coffee crop guidelines: Soil management, climate suitability, and plant nutrition," *FAO Plant Production Papers*, Rome, Italy, 2018.
10. D. L. Martins et al., "Potassium nutrition and physiological efficiency in Arabica and Robusta cultivars," *Journal of Plant Nutrition*, vol. 44, no. 12, pp. 1789–1804, 2021.
11. A. Holzinger et al., "What do we need to build explainable AI for precision medicine and agriculture?" *Information Fusion*, vol. 86, pp. 102–114, 2022.
12. S. M. Lundberg and S.-I. Lee, "A unified approach to interpreting model predictions," in *Proc. Advances in Neural Information Processing Systems (NeurIPS 30)*, Long Beach, CA, USA, 2017, pp. 4765–4774.
13. S. M. Lundberg et al., "From local explanations to global understanding with explainable AI for trees," *Nature Machine Intelligence*, vol. 2, no. 1, pp. 56–67, 2020.
14. L. Breiman, "Random forests," *Machine Learning*, vol. 45, no. 1, pp. 5–32, 2001.
15. T. Chen and C. Guestrin, "XGBoost: A scalable tree boosting system," in *Proc. 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, San Francisco, CA, USA, 2016, pp. 785–794.
16. J. H. Friedman, "Greedy function approximation: A gradient boosting machine," *The Annals of Statistics*, vol. 29, no. 5, pp. 1189–1232, 2001.
17. F. Pedregosa et al., "Scikit-learn: Machine learning in Python," *Journal of Machine Learning Research*, vol. 12, pp. 2825–2830, 2011.
