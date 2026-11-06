"""
app.py
------
Coffee Yield Prediction & Yield Loss Diagnostic Decision Support System.
A premium, modern agricultural intelligence dashboard built with Streamlit,
Scikit-Learn, Gradient Boosting, SHAP Explainability, and Precision Agronomy Advisory.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

from src.agronomy_engine import COFFEE_BENCHMARKS, REGION_PRESETS
from src.loss_analyzer import analyze_yield_loss
from src.advisor import generate_recommendations

# Page Configuration
st.set_page_config(
    page_title="CoffeeYield AI | Precision Yield & Loss Intelligence",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Styling (Google Fonts + Glassmorphism + Modern Gradients)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif;
    }

    /* Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        border-radius: 20px;
        padding: 35px 40px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px -10px rgba(15, 32, 39, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .hero-badge {
        display: inline-block;
        background: rgba(16, 185, 129, 0.2);
        border: 1px solid rgba(16, 185, 129, 0.6);
        color: #34D399;
        padding: 6px 14px;
        border-radius: 30px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0;
        background: linear-gradient(90deg, #FFFFFF 0%, #E2E8F0 60%, #A7F3D0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #CBD5E1;
        max-width: 820px;
        margin-top: 10px;
        line-height: 1.6;
    }

    .hero-stats {
        display: flex;
        gap: 30px;
        margin-top: 25px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.12);
    }

    .hero-stat-item {
        display: flex;
        flex-direction: column;
    }

    .hero-stat-value {
        font-size: 1.4rem;
        font-weight: 700;
        color: #6EE7B7;
    }

    .hero-stat-label {
        font-size: 0.78rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* KPI Cards */
    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 18px;
        margin-bottom: 25px;
    }

    .kpi-card-v2 {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 22px 24px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 8px 20px -6px rgba(0, 0, 0, 0.06);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .kpi-card-v2:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 28px -8px rgba(0, 0, 0, 0.12);
        border-color: #CBD5E1;
    }

    .kpi-card-v2::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
    }

    .kpi-card-blue::before { background: linear-gradient(90deg, #3B82F6, #60A5FA); }
    .kpi-card-green::before { background: linear-gradient(90deg, #10B981, #34D399); }
    .kpi-card-red::before { background: linear-gradient(90deg, #EF4444, #F87171); }
    .kpi-card-purple::before { background: linear-gradient(90deg, #8B5CF6, #A78BFA); }

    .kpi-header-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .kpi-tag {
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        color: #64748B;
    }

    .kpi-icon-pill {
        width: 38px;
        height: 38px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
    }

    .kpi-num {
        font-size: 2.1rem;
        font-weight: 800;
        color: #0F172A;
        margin-top: 8px;
        font-family: 'Outfit', sans-serif;
    }

    .kpi-unit {
        font-size: 0.95rem;
        font-weight: 600;
        color: #64748B;
    }

    .kpi-footnote {
        font-size: 0.84rem;
        color: #475569;
        margin-top: 6px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Diagnosis Alert Pill */
    .diagnosis-pill {
        background: linear-gradient(135deg, #FFF1F2 0%, #FFE4E6 100%);
        border: 1px solid #FECDD3;
        border-left: 6px solid #E11D48;
        border-radius: 14px;
        padding: 16px 22px;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        gap: 16px;
    }

    .diagnosis-pill-optimal {
        background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%);
        border: 1px solid #BBF7D0;
        border-left: 6px solid #16A34A;
        border-radius: 14px;
        padding: 16px 22px;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        gap: 16px;
    }

    /* Form Card Container */
    .form-glass-card {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 24px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }

    /* Advisory Card */
    .rx-card {
        background: #FFFFFF;
        border-radius: 14px;
        padding: 20px 24px;
        margin-bottom: 16px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
        transition: all 0.2s ease-in-out;
    }

    .rx-card:hover {
        border-color: #CBD5E1;
        box-shadow: 0 8px 18px rgba(0,0,0,0.06);
    }

    .rx-badge-high {
        background: #FEE2E2;
        color: #991B1B;
        font-weight: 700;
        font-size: 0.78rem;
        padding: 4px 12px;
        border-radius: 20px;
    }

    .rx-badge-medium {
        background: #FEF3C7;
        color: #92400E;
        font-weight: 700;
        font-size: 0.78rem;
        padding: 4px 12px;
        border-radius: 20px;
    }

    .rx-badge-optimal {
        background: #DCFCE7;
        color: #166534;
        font-weight: 700;
        font-size: 0.78rem;
        padding: 4px 12px;
        border-radius: 20px;
    }

    .rx-dosage-box {
        background: #F8FAFC;
        border-left: 3px solid #3B82F6;
        padding: 12px 16px;
        border-radius: 0 8px 8px 0;
        font-size: 0.92rem;
        color: #1E293B;
        margin-top: 10px;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #F8FAFC;
        border-right: 1px solid #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)

# Cache Model and Explainer
@st.cache_resource
def load_artifacts():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "models", "best_coffee_model.pkl")
    shap_path = os.path.join(base_dir, "models", "shap_explainer.pkl")
    meta_path = os.path.join(base_dir, "models", "model_metadata.json")
    
    model = joblib.load(model_path)
    shap_data = joblib.load(shap_path)
    with open(meta_path, "r") as f:
        metadata = json.load(f)
        
    return model, shap_data, metadata

model, shap_data, metadata = load_artifacts()

# Sidebar: Presets and Quick Controls
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 10px 0 15px 0;">
        <span style="font-size: 2.5rem;">☕</span>
        <h3 style="margin: 5px 0 0 0; color: #0F172A; font-weight: 800;">CoffeeYield AI</h3>
        <p style="font-size: 0.8rem; color: #64748B; margin-top: 2px;">Precision Agro-Intelligence System</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### ⚡ Quick Farm Scenarios")
    PRESET_OPTIONS = {
        "Manual Custom Input": None,
        "🟢 High Yield Arabica (Chikkamagaluru - Optimal)": {
            "Coffee_Species": "Arabica",
            "Region": "Chikkamagaluru, Karnataka",
            "Altitude_meters": 1250,
            "Avg_Temperature_C": 20.5,
            "Max_Temperature_C": 27.5,
            "Min_Temperature_C": 14.5,
            "Annual_Rainfall_mm": 1850.0,
            "Blossom_Rainfall_mm": 38.0,
            "Soil_pH": 6.2,
            "Nitrogen_N": 165.0,
            "Phosphorus_P": 75.0,
            "Potassium_K": 170.0,
            "Organic_Carbon_pct": 1.8,
            "Electrical_Conductivity_dS_m": 0.5,
            "Relative_Humidity_pct": 78.0,
            "Farm_Area_Acres": 10.0,
            "Tree_Density_per_Ha": 1650
        },
        "🔴 Acidic Soil & Potash Deficit (Coorg)": {
            "Coffee_Species": "Robusta",
            "Region": "Kodagu (Coorg), Karnataka",
            "Altitude_meters": 850,
            "Avg_Temperature_C": 23.0,
            "Max_Temperature_C": 31.0,
            "Min_Temperature_C": 16.0,
            "Annual_Rainfall_mm": 2100.0,
            "Blossom_Rainfall_mm": 40.0,
            "Soil_pH": 4.6,  # Very acidic
            "Nitrogen_N": 160.0,
            "Phosphorus_P": 45.0,
            "Potassium_K": 85.0,  # Severe K deficit
            "Organic_Carbon_pct": 1.1,
            "Electrical_Conductivity_dS_m": 0.4,
            "Relative_Humidity_pct": 82.0,
            "Farm_Area_Acres": 15.0,
            "Tree_Density_per_Ha": 1500
        },
        "💧 Severe Drought & Nitrogen Starved (Sakleshpur)": {
            "Coffee_Species": "Robusta",
            "Region": "Hassan (Sakleshpur), Karnataka",
            "Altitude_meters": 950,
            "Avg_Temperature_C": 24.5,
            "Max_Temperature_C": 33.0,
            "Min_Temperature_C": 17.5,
            "Annual_Rainfall_mm": 1150.0,
            "Blossom_Rainfall_mm": 12.0,
            "Soil_pH": 5.8,
            "Nitrogen_N": 80.0,
            "Phosphorus_P": 55.0,
            "Potassium_K": 160.0,
            "Organic_Carbon_pct": 0.8,
            "Electrical_Conductivity_dS_m": 0.6,
            "Relative_Humidity_pct": 62.0,
            "Farm_Area_Acres": 8.0,
            "Tree_Density_per_Ha": 1600
        },
        "🔥 Thermal Heat & Low Elevation Arabica (Wayanad)": {
            "Coffee_Species": "Arabica",
            "Region": "Wayanad, Kerala",
            "Altitude_meters": 650,
            "Avg_Temperature_C": 26.5,
            "Max_Temperature_C": 34.5,
            "Min_Temperature_C": 20.0,
            "Annual_Rainfall_mm": 2300.0,
            "Blossom_Rainfall_mm": 35.0,
            "Soil_pH": 5.9,
            "Nitrogen_N": 140.0,
            "Phosphorus_P": 50.0,
            "Potassium_K": 130.0,
            "Organic_Carbon_pct": 1.2,
            "Electrical_Conductivity_dS_m": 0.5,
            "Relative_Humidity_pct": 80.0,
            "Farm_Area_Acres": 12.0,
            "Tree_Density_per_Ha": 1700
        }
    }

    preset_choice = st.selectbox("Choose Preset:", list(PRESET_OPTIONS.keys()), label_visibility="collapsed")
    preset_data = PRESET_OPTIONS[preset_choice]

    st.markdown("---")
    st.markdown("#### ⚙️ Configuration")
    area_unit = st.radio("Land Area Unit:", ["Acres", "Hectares"], horizontal=True)
    coffee_price_per_kg = st.number_input("Clean Coffee Market Price (₹ / kg):", min_value=100.0, max_value=800.0, value=340.0, step=10.0)

    st.markdown("""
    <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:12px; padding:14px; margin-top:20px;">
        <span style="font-size:0.75rem; font-weight:700; color:#64748B; text-transform:uppercase;">Model In Service</span>
        <div style="font-size:0.95rem; font-weight:700; color:#0F172A; margin-top:2px;">Gradient Boosting Regressor</div>
        <div style="font-size:0.8rem; color:#10B981; font-weight:600; margin-top:3px;">● R² = 0.9530 | MAPE = 3.88%</div>
    </div>
    """, unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">🌿 AI DECISION SUPPORT SYSTEM • MAJOR PROJECT</div>
    <div class="hero-title">Coffee Yield Prediction & Loss Diagnosis</div>
    <div class="hero-subtitle">
        An Explainable AI platform combining <b>Soil Health Card parameters</b>, <b>Meteorological dynamics</b>, and <b>Topographical elevation</b> to accurately project harvest yield, isolate root-cause yield-loss factors, and prescribe precision agronomic remedies.
    </div>
    <div class="hero-stats">
        <div class="hero-stat-item">
            <span class="hero-stat-value">95.3%</span>
            <span class="hero-stat-label">Model Accuracy (R²)</span>
        </div>
        <div class="hero-stat-item">
            <span class="hero-stat-value">3,500</span>
            <span class="hero-stat-label">Estates Calibrated</span>
        </div>
        <div class="hero-stat-item">
            <span class="hero-stat-value">SHAP XAI</span>
            <span class="hero-stat-label">Biophysical Transparency</span>
        </div>
        <div class="hero-stat-item">
            <span class="hero-stat-value">CCRI Certified</span>
            <span class="hero-stat-label">Agronomic Benchmark</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Input Parameters Card
with st.expander("🛠️ CONFIGURE FARM SOIL, WEATHER & LOCATION PARAMETERS", expanded=True):
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("#### 📍 Location & Species")
        region_list = list(REGION_PRESETS.keys())
        default_region_idx = region_list.index(preset_data["Region"]) if preset_data else 1
        region = st.selectbox("Estate Place / Region:", region_list, index=default_region_idx)
        
        species_options = ["Arabica", "Robusta"]
        default_species_idx = species_options.index(preset_data["Coffee_Species"]) if preset_data else 0
        species = st.selectbox("Coffee Species:", species_options, index=default_species_idx)
        
        default_alt = preset_data["Altitude_meters"] if preset_data else REGION_PRESETS[region]["altitude"]
        altitude = st.number_input("Elevation / Altitude (meters MSL):", min_value=150, max_value=2500, value=int(default_alt), step=25)
        
        if area_unit == "Acres":
            default_area = preset_data["Farm_Area_Acres"] if preset_data else 10.0
            area_val = st.number_input("Total Land Area (Acres):", min_value=0.5, max_value=500.0, value=float(default_area), step=1.0)
            farm_area_ha = area_val * 0.404686
            farm_area_acres = area_val
        else:
            default_ha = (preset_data["Farm_Area_Acres"] * 0.404686) if preset_data else 4.0
            area_val = st.number_input("Total Land Area (Hectares):", min_value=0.2, max_value=200.0, value=float(default_ha), step=0.5)
            farm_area_ha = area_val
            farm_area_acres = area_val * 2.47105
            
        tree_density = st.slider("Planting Density (Trees / Hectare):", min_value=900, max_value=2600, value=preset_data["Tree_Density_per_Ha"] if preset_data else 1600, step=50)

    with col2:
        st.markdown("#### 🧪 Soil Health Card Report")
        default_ph = preset_data["Soil_pH"] if preset_data else 5.8
        soil_ph = st.slider("Soil pH (1:2.5 Water):", min_value=4.0, max_value=8.0, value=float(default_ph), step=0.05,
                            help="Optimal: Arabica 5.8-6.5 | Robusta 5.5-6.5. Acidic soils (< 5.0) fix phosphorus and induce aluminum toxicity.")
        
        default_n = preset_data["Nitrogen_N"] if preset_data else 145.0
        nitrogen = st.slider("Available Nitrogen - N (kg/ha):", min_value=30.0, max_value=300.0, value=float(default_n), step=5.0)
        
        default_p = preset_data["Phosphorus_P"] if preset_data else 55.0
        phosphorus = st.slider("Available Phosphorus - P (kg/ha):", min_value=10.0, max_value=140.0, value=float(default_p), step=2.0)
        
        default_k = preset_data["Potassium_K"] if preset_data else 150.0
        potassium = st.slider("Available Potassium - K (kg/ha):", min_value=30.0, max_value=320.0, value=float(default_k), step=5.0,
                              help="Potassium governs bean size, weight, and berry moisture resilience.")
        
        default_oc = preset_data["Organic_Carbon_pct"] if preset_data else 1.4
        organic_carbon = st.slider("Organic Carbon (%):", min_value=0.2, max_value=3.5, value=float(default_oc), step=0.1)
        
        default_ec = preset_data["Electrical_Conductivity_dS_m"] if preset_data else 0.5
        ec_val = st.number_input("Electrical Conductivity - EC (dS/m):", min_value=0.05, max_value=3.0, value=float(default_ec), step=0.05)

    with col3:
        st.markdown("#### 🌦️ Meteorology & Climate")
        default_rain = preset_data["Annual_Rainfall_mm"] if preset_data else float(REGION_PRESETS[region]["rainfall"])
        annual_rain = st.number_input("Annual Rainfall (mm):", min_value=500.0, max_value=4500.0, value=float(default_rain), step=50.0)
        
        default_blossom = preset_data["Blossom_Rainfall_mm"] if preset_data else 35.0
        blossom_rain = st.slider("Blossom Showers in Feb/March (mm):", min_value=0.0, max_value=90.0, value=float(default_blossom), step=1.0,
                                 help="Crucial rain event triggering blossom anthesis. Lack of blossom rain leads to crop failure.")
        
        default_avg_temp = preset_data["Avg_Temperature_C"] if preset_data else float(REGION_PRESETS[region]["temp_avg"])
        avg_temp = st.slider("Average Annual Temperature (°C):", min_value=14.0, max_value=34.0, value=float(default_avg_temp), step=0.5)
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            max_temp = st.number_input("Max Summer Temp (°C):", min_value=18.0, max_value=42.0, value=float(preset_data["Max_Temperature_C"] if preset_data else avg_temp + 7.5), step=0.5)
        with col_t2:
            min_temp = st.number_input("Min Winter Temp (°C):", min_value=4.0, max_value=26.0, value=float(preset_data["Min_Temperature_C"] if preset_data else avg_temp - 6.5), step=0.5)
            
        humidity = st.slider("Relative Humidity (%):", min_value=35.0, max_value=98.0, value=float(preset_data["Relative_Humidity_pct"] if preset_data else 76.0), step=1.0)

# Build Input Dataframe
input_dict = {
    "Coffee_Species": species,
    "Region": region,
    "Altitude_meters": altitude,
    "Avg_Temperature_C": avg_temp,
    "Max_Temperature_C": max_temp,
    "Min_Temperature_C": min_temp,
    "Annual_Rainfall_mm": annual_rain,
    "Blossom_Rainfall_mm": blossom_rain,
    "Soil_pH": soil_ph,
    "Nitrogen_N": nitrogen,
    "Phosphorus_P": phosphorus,
    "Potassium_K": potassium,
    "Organic_Carbon_pct": organic_carbon,
    "Electrical_Conductivity_dS_m": ec_val,
    "Relative_Humidity_pct": humidity,
    "Tree_Density_per_Ha": tree_density,
    "Farm_Area_Hectares": farm_area_ha,
    "Farm_Area_Acres": farm_area_acres
}

input_df = pd.DataFrame([input_dict])
pred_features = metadata["categorical_features"] + metadata["numeric_features"]
X_single = input_df[pred_features]

# Predict
predicted_yield_ha = float(model.predict(X_single)[0])
predicted_yield_ha = round(max(250.0, predicted_yield_ha), 1)

# Conversions
predicted_yield_acre = round(predicted_yield_ha * 0.404686, 1)
total_farm_yield_kg = round(predicted_yield_ha * farm_area_ha, 1)
total_farm_yield_mt = round(total_farm_yield_kg / 1000.0, 2)
bags_60kg = int(round(total_farm_yield_kg / 60.0))
estimated_revenue = round(total_farm_yield_kg * coffee_price_per_kg, 0)

# Loss Diagnosis
loss_report = analyze_yield_loss(input_dict, predicted_yield_ha)
potential_yield_ha = loss_report["potential_yield_kg_ha"]
total_loss_ha = loss_report["total_loss_kg_ha"]
efficiency_pct = loss_report["yield_efficiency_pct"]
total_farm_loss_kg = round(total_loss_ha * farm_area_ha, 1)
total_farm_loss_mt = round(total_farm_loss_kg / 1000.0, 2)
revenue_loss = round(total_farm_loss_kg * coffee_price_per_kg, 0)

# SHAP Feature Explanations
try:
    X_trans = model.named_steps["preprocessor"].transform(X_single)
    explainer = shap_data["explainer"]
    shap_vals = explainer(X_trans)
    shap_contributions = dict(zip(shap_data["feature_names"], shap_vals.values[0]))
except Exception:
    shap_contributions = {}

# Advisory
advisories = generate_recommendations(input_dict, loss_report)

# ========================================================
# KPI PRESENTATION ROW (STUNNING MODERN GLASS CARDS)
# ========================================================
st.markdown("<br>", unsafe_allow_html=True)
col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)

with col_kpi1:
    st.markdown(f"""
    <div class="kpi-card-v2 kpi-card-blue">
        <div class="kpi-header-row">
            <span class="kpi-tag">PREDICTED YIELD</span>
            <div class="kpi-icon-pill" style="background:#EFF6FF; color:#3B82F6;">🎯</div>
        </div>
        <div class="kpi-num">{predicted_yield_ha:,} <span class="kpi-unit">kg/ha</span></div>
        <div class="kpi-footnote">
            <span style="color:#059669; font-weight:700;">≈ {predicted_yield_acre:,} kg / acre</span> (Clean Bean)
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_kpi2:
    st.markdown(f"""
    <div class="kpi-card-v2 kpi-card-green">
        <div class="kpi-header-row">
            <span class="kpi-tag">ESTATE PRODUCTION</span>
            <div class="kpi-icon-pill" style="background:#ECFDF5; color:#10B981;">📦</div>
        </div>
        <div class="kpi-num">{total_farm_yield_mt:,} <span class="kpi-unit">MT</span></div>
        <div class="kpi-footnote">
            <b>{bags_60kg:,} bags</b> (60kg) • Est: ₹{estimated_revenue/100000:,.2f} Lakhs
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_kpi3:
    loss_color = "#EF4444" if total_loss_ha > 300 else "#F59E0B"
    bg_loss = "#FEF2F2" if total_loss_ha > 300 else "#FFFBEB"
    st.markdown(f"""
    <div class="kpi-card-v2 kpi-card-red">
        <div class="kpi-header-row">
            <span class="kpi-tag">YIELD GAP / LOSS</span>
            <div class="kpi-icon-pill" style="background:{bg_loss}; color:{loss_color};">⚠️</div>
        </div>
        <div class="kpi-num" style="color:{loss_color};">-{total_loss_ha:,} <span class="kpi-unit">kg/ha</span></div>
        <div class="kpi-footnote">
            Lost Revenue: <b style="color:{loss_color};">₹{revenue_loss/100000:,.2f} Lakhs</b> ({total_farm_loss_mt} MT)
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_kpi4:
    st.markdown(f"""
    <div class="kpi-card-v2 kpi-card-purple">
        <div class="kpi-header-row">
            <span class="kpi-tag">HARVEST EFFICIENCY</span>
            <div class="kpi-icon-pill" style="background:#F5F3FF; color:#8B5CF6;">⚡</div>
        </div>
        <div class="kpi-num">{efficiency_pct:.1f}<span class="kpi-unit">%</span></div>
        <div class="kpi-footnote">
            Genetic Potential: <b>{potential_yield_ha:.0f} kg/ha</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

# DIAGNOSTIC STATUS BANNER
st.markdown("<br>", unsafe_allow_html=True)
if total_loss_ha > 40.0:
    st.markdown(f"""
    <div class="diagnosis-pill">
        <span style="font-size: 2rem;">🚨</span>
        <div>
            <div style="font-size: 1.1rem; font-weight: 800; color: #9F1239;">
                PRIMARY BOTTLENECK IDENTIFIED: {loss_report['primary_bottleneck'].upper()}
            </div>
            <div style="font-size: 0.92rem; color: #BE123C; margin-top: 2px;">
                Secondary Contributing Factor: <b>{loss_report['secondary_bottleneck']}</b> • Yield performance is currently operating at {efficiency_pct:.1f}% of regional biological potential.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div class="diagnosis-pill-optimal">
        <span style="font-size: 2rem;">🌿</span>
        <div>
            <div style="font-size: 1.1rem; font-weight: 800; color: #166534;">
                OPTIMAL AGRO-CLIMATIC BALANCE ACHIEVED
            </div>
            <div style="font-size: 0.92rem; color: #15803D; margin-top: 2px;">
                Soil parameters and micro-climate match the physiological ideals for {species}. Yield efficiency is at <b>{efficiency_pct:.1f}%</b>.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ========================================================
# DETAILED TABBED NAVIGATION (ADVANCED INTERACTIVE SUITE)
# ========================================================
tab_loss, tab_shap, tab_rx, tab_sim, tab_eval = st.tabs([
    "📉 Factor-Wise Yield Loss Breakdown",
    "🧠 Explainable AI (SHAP Insights)",
    "💊 Precision Agronomic Advisory (Rx)",
    "🎛️ Interactive 'What-If' Yield Recovery Lab",
    "🏆 Model Evaluation & Viva Defense"
])

# TAB 1: YIELD LOSS BREAKDOWN
with tab_loss:
    st.markdown("### 📊 Root-Cause Yield Loss Decomposition")
    st.markdown("Biophysical deduction analysis matching the farm's soil card and climate indicators against Central Coffee Research Institute (CCRI) ideal thresholds.")
    
    col_wfall, col_gauge = st.columns([1.5, 1.0])
    
    with col_wfall:
        breakdown_items = loss_report["breakdown"]
        
        # Build Waterfall Data
        measure = ["absolute"]
        x_names = ["Genetic Potential"]
        y_vals = [potential_yield_ha]
        text_vals = [f"{potential_yield_ha:.0f}"]
        
        for item in breakdown_items:
            if item["loss_kg_ha"] > 1.0:
                measure.append("relative")
                x_names.append(item["display_name"].replace(" Deficiency", "").replace(" Stress", ""))
                y_vals.append(-item["loss_kg_ha"])
                text_vals.append(f"-{item['loss_kg_ha']:.0f} kg")
                
        measure.append("total")
        x_names.append("Actual Harvest")
        y_vals.append(predicted_yield_ha)
        text_vals.append(f"{predicted_yield_ha:.0f}")
        
        fig_waterfall = go.Figure(go.Waterfall(
            name="Yield Dynamics",
            orientation="v",
            measure=measure,
            x=x_names,
            textposition="outside",
            text=text_vals,
            y=y_vals,
            connector={"line": {"color": "#94A3B8", "width": 1.5, "dash": "dot"}},
            decreasing={"marker": {"color": "#EF4444"}},
            increasing={"marker": {"color": "#10B981"}},
            totals={"marker": {"color": "#3B82F6"}}
        ))
        
        fig_waterfall.update_layout(
            title="<b>Waterfall Impact on Yield (kg/ha)</b>",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=460,
            margin=dict(l=10, r=10, t=40, b=90),
            font=dict(family="Plus Jakarta Sans", size=12),
            xaxis_tickangle=-25
        )
        st.plotly_chart(fig_waterfall, use_container_width=True)

    with col_gauge:
        # Radial Gauge for Yield Efficiency
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=efficiency_pct,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "<b>Yield Realization Rate</b>", 'font': {'size': 18, 'family': 'Outfit'}},
            number={'suffix': "%", 'font': {'size': 42, 'color': '#0F172A', 'family': 'Outfit'}},
            gauge={
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#94A3B8"},
                'bar': {'color': "#3B82F6", 'thickness': 0.28},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "#E2E8F0",
                'steps': [
                    {'range': [0, 50], 'color': '#FEE2E2'},
                    {'range': [50, 75], 'color': '#FEF3C7'},
                    {'range': [75, 100], 'color': '#DCFCE7'}
                ],
                'threshold': {
                    'line': {'color': "#10B981", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        fig_gauge.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=320,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        st.markdown(f"""
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:12px; padding:12px 16px; font-size:0.85rem; color:#475569;">
            💡 <b>Financial Impact:</b> Recovering lost production can add up to <b>₹{revenue_loss/100000:,.2f} Lakhs</b> in revenue to this {farm_area_acres:.1f}-acre estate.
        </div>
        """, unsafe_allow_html=True)

    # Detailed Audit Breakdown Table
    st.markdown("#### 📋 Detailed Loss Factor Diagnostic Ledger")
    breakdown_df = pd.DataFrame([
        {
            "Stress Indicator": item["display_name"],
            "Tested Input": f"{input_dict.get(item['input_feature'].replace(' ', '_'), 'N/A')}",
            "Yield Loss (kg/ha)": f"-{item['loss_kg_ha']:.1f} kg/ha",
            "% Share of Gap": f"{item['loss_percentage']:.1f}%",
            "Severity Assessment": item["severity"]
        }
        for item in loss_report["breakdown"]
    ])
    st.dataframe(breakdown_df, hide_index=True, use_container_width=True)

# TAB 2: EXPLAINABLE AI (SHAP)
with tab_shap:
    st.markdown("### 🧠 Explainable AI: SHAP Attribution")
    st.markdown("Using game-theoretic **TreeSHAP** to explain the model's exact decision path. Features pushing yield **upward** appear in green (+), while adverse environmental penalties appear in red (-).")

    col_s1, col_s2 = st.columns([1.2, 1.0])
    
    with col_s1:
        if shap_contributions:
            sorted_shap = sorted(shap_contributions.items(), key=lambda x: abs(x[1]), reverse=True)[:9]
            shap_df = pd.DataFrame(sorted_shap, columns=["Feature", "SHAP Impact (kg/ha)"])
            shap_df["Impact Type"] = np.where(shap_df["SHAP Impact (kg/ha)"] > 0, "Yield Booster (+)", "Yield Penalty (-)")
            
            fig_shap = px.bar(
                shap_df,
                x="SHAP Impact (kg/ha)",
                y="Feature",
                orientation="h",
                color="Impact Type",
                color_discrete_map={"Yield Booster (+)": "#10B981", "Yield Penalty (-)": "#EF4444"},
                title="<b>Local SHAP Contribution for this Plantation</b>"
            )
            fig_shap.update_layout(
                yaxis=dict(autorange="reversed"),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                height=420,
                font=dict(family="Plus Jakarta Sans")
            )
            st.plotly_chart(fig_shap, use_container_width=True)
            
    with col_s2:
        st.markdown("#### 🌐 Global Feature Importance Across 3,500 Estates")
        feat_imp = metadata.get("feature_importances", {})
        top_imp = list(feat_imp.items())[:8]
        imp_df = pd.DataFrame(top_imp, columns=["Driver Feature", "Importance Score"])
        
        fig_imp = px.bar(
            imp_df,
            x="Importance Score",
            y="Driver Feature",
            orientation="h",
            color_discrete_sequence=["#3B82F6"],
            title="<b>Global Model Importance</b>"
        )
        fig_imp.update_layout(
            yaxis=dict(autorange="reversed"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=420,
            font=dict(family="Plus Jakarta Sans")
        )
        st.plotly_chart(fig_imp, use_container_width=True)

# TAB 3: AGRONOMIC ADVISORY (RX)
with tab_rx:
    st.markdown("### 💊 Precision Agronomic Prescription (Rx)")
    st.markdown("Tailored corrective measures to reverse diagnosed yield penalties. All dosages are stoichiometric calculations based on CCRI recommendations.")

    for adv in advisories:
        urgency = adv["urgency"]
        badge_class = {
            "High": "rx-badge-high",
            "Medium": "rx-badge-medium",
            "Maintenance": "rx-badge-optimal"
        }.get(urgency, "rx-badge-medium")
        
        border_color = {
            "High": "#EF4444",
            "Medium": "#F59E0B",
            "Maintenance": "#10B981"
        }.get(urgency, "#3B82F6")

        st.markdown(f"""
        <div class="rx-card" style="border-left: 5px solid {border_color};">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:1.1rem; font-weight:700; color:#0F172A;">🌱 {adv['category']}: {adv['issue']}</span>
                <span class="{badge_class}">PRIORITY: {urgency.upper()}</span>
            </div>
            <div style="margin-top:10px; font-weight:600; color:#334155; font-size:0.95rem;">
                <b>Required Intervention:</b> {adv['action']}
            </div>
            <div class="rx-dosage-box">
                <b>📌 Application Protocol & Dosages:</b><br/>{adv['prescription']}
            </div>
        </div>
        """, unsafe_allow_html=True)

# TAB 4: INTERACTIVE 'WHAT-IF' SIMULATOR
with tab_sim:
    st.markdown("### 🎛️ Interactive 'What-If' Simulation & Yield Recovery")
    st.markdown("Simulate precision corrective interventions (e.g. applying agricultural lime to neutralize soil acidity, boosting potash, or providing sprinkler blossom irrigation) to see real-time recovery!")

    col_sim1, col_sim2 = st.columns([1.2, 1.0])
    
    with col_sim1:
        st.markdown("#### Adjust Corrective Interventions:")
        sim_ph = st.slider("Simulated Soil pH (after Lime/Dolomite):", min_value=4.2, max_value=7.5, value=float(soil_ph), step=0.1)
        sim_n = st.slider("Simulated Nitrogen N (after Urea application):", min_value=40.0, max_value=250.0, value=float(nitrogen), step=5.0)
        sim_k = st.slider("Simulated Potassium K (after MOP application):", min_value=40.0, max_value=250.0, value=float(potassium), step=5.0)
        sim_blossom = st.slider("Simulated Blossom Rain (after Sprinkler Irrigation):", min_value=0.0, max_value=70.0, value=float(blossom_rain), step=2.0)
        
    with col_sim2:
        # Run simulation
        sim_dict = input_dict.copy()
        sim_dict["Soil_pH"] = sim_ph
        sim_dict["Nitrogen_N"] = sim_n
        sim_dict["Potassium_K"] = sim_k
        sim_dict["Blossom_Rainfall_mm"] = sim_blossom
        
        sim_df = pd.DataFrame([sim_dict])[pred_features]
        sim_pred_yield = float(model.predict(sim_df)[0])
        sim_pred_yield = round(max(250.0, sim_pred_yield), 1)
        
        yield_delta = round(sim_pred_yield - predicted_yield_ha, 1)
        revenue_delta = round(yield_delta * farm_area_ha * coffee_price_per_kg, 0)
        
        delta_color = "#10B981" if yield_delta >= 0 else "#EF4444"
        delta_sign = "+" if yield_delta >= 0 else ""

        # Visual Comparison Bar Chart
        comp_df = pd.DataFrame([
            {"Scenario": "Current Baseline", "Yield (kg/ha)": predicted_yield_ha},
            {"Scenario": "Simulated Corrected", "Yield (kg/ha)": sim_pred_yield}
        ])
        fig_comp = px.bar(
            comp_df,
            x="Scenario",
            y="Yield (kg/ha)",
            color="Scenario",
            color_discrete_map={"Current Baseline": "#94A3B8", "Simulated Corrected": "#10B981"},
            text_auto=True
        )
        fig_comp.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=260,
            margin=dict(l=10, r=10, t=10, b=10),
            showlegend=False
        )
        st.plotly_chart(fig_comp, use_container_width=True)

        st.markdown(f"""
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:14px; padding:18px 22px; box-shadow:0 4px 12px rgba(0,0,0,0.04);">
            <div style="font-size:0.8rem; font-weight:700; color:#64748B; text-transform:uppercase;">PROJECTED HARVEST RECOVERY</div>
            <div style="font-size:2rem; font-weight:800; color:{delta_color}; margin-top:4px;">
                {delta_sign}{yield_delta:,} <span style="font-size:1rem; font-weight:600;">kg/ha</span>
            </div>
            <div style="font-size:1.05rem; font-weight:700; color:#0F172A; margin-top:6px;">
                Estimated Estate Revenue Gain: <span style="color:{delta_color};">{delta_sign}₹{revenue_delta:,.0f}</span>
            </div>
            <div style="font-size:0.8rem; color:#64748B; margin-top:4px;">
                Calculated across {farm_area_acres:.1f} acres at ₹{coffee_price_per_kg}/kg clean bean.
            </div>
        </div>
        """, unsafe_allow_html=True)

# TAB 5: MODEL EVALUATION & VIVA DEFENSE
with tab_eval:
    st.markdown("### 🏆 Major Project Comparative Evaluation")
    st.markdown("Evaluation metrics from 3,500 training plantation profiles comparing three ensemble machine learning architectures:")

    metrics = metadata.get("metrics", {})
    metrics_table = []
    for m_name, m_vals in metrics.items():
        metrics_table.append({
            "Machine Learning Algorithm": m_name.replace("_", " "),
            "R² Score (Accuracy)": f"{m_vals['R2_Score']:.4f}",
            "RMSE (Error)": f"{m_vals['RMSE']} kg/ha",
            "MAE (Avg Dev)": f"{m_vals['MAE']} kg/ha",
            "MAPE (%)": f"{m_vals['MAPE_pct']} %"
        })
    st.dataframe(pd.DataFrame(metrics_table), hide_index=True, use_container_width=True)

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.markdown("""
        #### 🎓 Key Viva Presentation Arguments:
        1. **Why Tree Ensembles over Linear Regression?**
           Coffee yield exhibits biological threshold gates (e.g. blossom showers below 25mm trigger floral pinking, and pH < 5.0 fixes phosphorus). Linear models fail to capture these non-linear thresholds; Gradient Boosting captures them with 95.3% $R^2$.
        2. **How does SHAP eliminate the 'Black-Box' problem?**
           TreeSHAP computes exact Shapley values from cooperative game theory, ensuring that every prediction has an exact audit trail of which features contributed positively or negatively.
        """)
    with col_v2:
        st.markdown("""
        #### 🧪 Agronomic Grounding:
        - **Liebig's Law of the Minimum:** Crop yield is governed not by total resources available, but by the scarcest nutrient (limiting factor).
        - **Soil Buffering Formulation:** Neutralizing doses use regional soil buffering constants to convert pH deficits into practical bags of agricultural lime and dolomite.
        """)

# Report Export
st.markdown("---")
report_text = f"""=====================================================
COFFEE YIELD PREDICTION & LOSS DIAGNOSTIC AUDIT
Generated for: {region} | Species: {species}
=====================================================
LAND & TOPOGRAPHY:
- Farm Area: {farm_area_acres:.2f} Acres ({farm_area_ha:.2f} Hectares)
- Elevation: {altitude} meters MSL
- Planting Density: {tree_density} trees/ha

SOIL HEALTH REPORT:
- Soil pH: {soil_ph}
- Nitrogen (N): {nitrogen} kg/ha
- Phosphorus (P): {phosphorus} kg/ha
- Potassium (K): {potassium} kg/ha
- Organic Carbon: {organic_carbon} %
- Electrical Conductivity: {ec_val} dS/m

METEOROLOGICAL PROFILE:
- Annual Rainfall: {annual_rain} mm
- Blossom Rainfall: {blossom_rain} mm
- Average Temperature: {avg_temp} °C
- Relative Humidity: {humidity} %

AI PREDICTION & LOSS DECOMPOSITION:
- Predicted Yield: {predicted_yield_ha} kg/ha ({predicted_yield_acre} kg/acre)
- Total Estate Output: {total_farm_yield_mt} Metric Tonnes ({bags_60kg} bags of 60kg)
- Potential Biological Yield: {potential_yield_ha} kg/ha
- Total Lost Yield: {total_loss_ha} kg/ha ({total_farm_loss_mt} MT across estate)
- Yield Efficiency: {efficiency_pct:.1f} %
- Primary Bottleneck: {loss_report['primary_bottleneck']}
- Secondary Bottleneck: {loss_report['secondary_bottleneck']}
- Estimated Revenue Gap: ₹{revenue_loss:,.0f} (at ₹{coffee_price_per_kg}/kg)

AGRONOMIC ACTION PLAN:
"""
for idx, adv in enumerate(advisories, 1):
    report_text += f"{idx}. [{adv['category']}] {adv['issue']} (Priority: {adv['urgency']})\n"
    report_text += f"   Action: {adv['action']}\n"
    report_text += f"   Prescription: {adv['prescription']}\n\n"

st.download_button(
    label="📄 Download Diagnostic & Advisory Report (.txt)",
    data=report_text,
    file_name=f"Coffee_Yield_Audit_{region.split(',')[0].strip().replace(' ', '_')}.txt",
    mime="text/plain"
)
