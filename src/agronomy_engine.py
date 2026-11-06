"""
agronomy_engine.py
------------------
Coffee Agronomic Knowledge Engine & Biological Response Models.
Based on research guidelines from Central Coffee Research Institute (CCRI),
International Coffee Organization (ICO), and FAO Coffee Soil Management.
"""

from typing import Dict, Any, Tuple

# Optimal and tolerance thresholds for Coffee Species
COFFEE_BENCHMARKS = {
    "Arabica": {
        "optimal_altitude": (1000, 1600),       # meters
        "altitude_range": (800, 2000),
        "optimal_temp_avg": (18.0, 23.0),       # Celsius
        "temp_avg_range": (15.0, 28.0),
        "max_temp_threshold": 30.0,
        "min_temp_threshold": 10.0,
        "optimal_rainfall": (1500, 2200),       # mm/year
        "rainfall_range": (1100, 3000),
        "optimal_blossom_rain": (25, 45),       # mm in March/April
        "optimal_ph": (5.8, 6.5),
        "ph_range": (4.5, 7.5),
        "optimal_n": (130, 180),                # kg/ha
        "optimal_p": (50, 90),                  # kg/ha
        "optimal_k": (130, 190),                # kg/ha
        "optimal_oc": (1.2, 2.5),               # % Organic Carbon
        "optimal_ec": (0.2, 1.0),               # dS/m Electrical Conductivity
        "potential_yield_kg_ha": 1400.0,        # Clean bean potential under ideal conditions
        "min_yield_kg_ha": 300.0
    },
    "Robusta": {
        "optimal_altitude": (400, 900),         # meters
        "altitude_range": (200, 1200),
        "optimal_temp_avg": (23.0, 28.0),       # Celsius
        "temp_avg_range": (19.0, 32.0),
        "max_temp_threshold": 34.0,
        "min_temp_threshold": 14.0,
        "optimal_rainfall": (1800, 2600),       # mm/year
        "rainfall_range": (1200, 3400),
        "optimal_blossom_rain": (30, 60),       # mm in Feb/March
        "optimal_ph": (5.5, 6.5),
        "ph_range": (4.5, 7.5),
        "optimal_n": (150, 220),                # kg/ha
        "optimal_p": (40, 80),                  # kg/ha
        "optimal_k": (150, 230),                # kg/ha
        "optimal_oc": (1.0, 2.2),               # % Organic Carbon
        "optimal_ec": (0.2, 1.2),               # dS/m
        "potential_yield_kg_ha": 2100.0,        # Clean bean potential under ideal conditions
        "min_yield_kg_ha": 450.0
    }
}

# Regional presets with typical environmental profiles
REGION_PRESETS = {
    "Kodagu (Coorg), Karnataka": {"species": "Robusta", "altitude": 850, "temp_avg": 22.5, "rainfall": 2100, "ph": 5.8},
    "Chikkamagaluru, Karnataka": {"species": "Arabica", "altitude": 1150, "temp_avg": 20.5, "rainfall": 1750, "ph": 6.1},
    "Hassan (Sakleshpur), Karnataka": {"species": "Robusta", "altitude": 950, "temp_avg": 23.0, "rainfall": 2300, "ph": 5.7},
    "Wayanad, Kerala": {"species": "Robusta", "altitude": 750, "temp_avg": 24.0, "rainfall": 2400, "ph": 5.6},
    "Idukki, Kerala": {"species": "Arabica", "altitude": 1200, "temp_avg": 19.5, "rainfall": 2600, "ph": 5.9},
    "Nilgiris, Tamil Nadu": {"species": "Arabica", "altitude": 1450, "temp_avg": 17.5, "rainfall": 1500, "ph": 6.2},
    "Shevaroys (Yercaud), Tamil Nadu": {"species": "Arabica", "altitude": 1300, "temp_avg": 19.0, "rainfall": 1400, "ph": 6.0},
    "Minas Gerais, Brazil": {"species": "Arabica", "altitude": 1100, "temp_avg": 21.0, "rainfall": 1600, "ph": 6.0},
    "Central Highlands, Vietnam": {"species": "Robusta", "altitude": 600, "temp_avg": 25.0, "rainfall": 2100, "ph": 5.8}
}

def calculate_stress_factors(params: Dict[str, Any]) -> Dict[str, float]:
    """
    Computes biological stress indices (0.0 = no stress/loss, 1.0 = maximum loss)
    for each agronomic parameter based on deviation from species benchmark.
    """
    species = params.get("Coffee_Species", "Arabica")
    bm = COFFEE_BENCHMARKS.get(species, COFFEE_BENCHMARKS["Arabica"])

    stresses = {}

    # 1. Soil pH Stress (Bell-shaped curve around optimal)
    ph = params["Soil_pH"]
    opt_ph_min, opt_ph_max = bm["optimal_ph"]
    if opt_ph_min <= ph <= opt_ph_max:
        stresses["ph_stress"] = 0.0
    elif ph < opt_ph_min:
        # Acidity stress (aluminum/manganese toxicity, P-fixation)
        stresses["ph_stress"] = min(1.0, max(0.0, (opt_ph_min - ph) / 1.5))
    else:
        # Alkalinity stress (zinc, iron chlorosis)
        stresses["ph_stress"] = min(1.0, max(0.0, (ph - opt_ph_max) / 1.5))

    # 2. Nitrogen Stress (Liebig limitation)
    n = params["Nitrogen_N"]
    opt_n_min, opt_n_max = bm["optimal_n"]
    if n >= opt_n_min:
        stresses["n_stress"] = 0.0
    else:
        stresses["n_stress"] = min(1.0, max(0.0, (opt_n_min - n) / opt_n_min))

    # 3. Phosphorus Stress
    p = params["Phosphorus_P"]
    opt_p_min, opt_p_max = bm["optimal_p"]
    if p >= opt_p_min:
        stresses["p_stress"] = 0.0
    else:
        stresses["p_stress"] = min(1.0, max(0.0, (opt_p_min - p) / opt_p_min))

    # 4. Potassium Stress (crucial for berry expansion & drought resilience)
    k = params["Potassium_K"]
    opt_k_min, opt_k_max = bm["optimal_k"]
    if k >= opt_k_min:
        stresses["k_stress"] = 0.0
    else:
        stresses["k_stress"] = min(1.0, max(0.0, (opt_k_min - k) / opt_k_min))

    # 5. Organic Carbon Stress
    oc = params["Organic_Carbon_pct"]
    opt_oc_min = bm["optimal_oc"][0]
    if oc >= opt_oc_min:
        stresses["oc_stress"] = 0.0
    else:
        stresses["oc_stress"] = min(1.0, max(0.0, (opt_oc_min - oc) / opt_oc_min))

    # 6. Rainfall Stress (Deficit vs Flooding/Leaching)
    rain = params["Annual_Rainfall_mm"]
    opt_rain_min, opt_rain_max = bm["optimal_rainfall"]
    if opt_rain_min <= rain <= opt_rain_max:
        stresses["rainfall_stress"] = 0.0
    elif rain < opt_rain_min:
        # Drought stress
        stresses["rainfall_stress"] = min(1.0, max(0.0, (opt_rain_min - rain) / (opt_rain_min - 600)))
    else:
        # Excess moisture / fungal leaf rust / aeration loss
        stresses["rainfall_stress"] = min(0.7, max(0.0, (rain - opt_rain_max) / 1500))

    # 7. Blossom Shower Stress
    blossom_rain = params.get("Blossom_Rainfall_mm", 35.0)
    opt_blossom_min = bm["optimal_blossom_rain"][0]
    if blossom_rain >= opt_blossom_min:
        stresses["blossom_stress"] = 0.0
    else:
        # Blossom failure significantly impairs fruit set
        stresses["blossom_stress"] = min(1.0, max(0.0, (opt_blossom_min - blossom_rain) / opt_blossom_min))

    # 8. Temperature Stress
    temp = params["Avg_Temperature_C"]
    opt_temp_min, opt_temp_max = bm["optimal_temp_avg"]
    if opt_temp_min <= temp <= opt_temp_max:
        stresses["temp_stress"] = 0.0
    elif temp > opt_temp_max:
        # Heat stress (flower abortion, berry scorch)
        stresses["temp_stress"] = min(1.0, max(0.0, (temp - opt_temp_max) / 6.0))
    else:
        # Cold stress / slowed metabolism
        stresses["temp_stress"] = min(1.0, max(0.0, (opt_temp_min - temp) / 5.0))

    # 9. Altitude Mismatch Stress
    alt = params["Altitude_meters"]
    opt_alt_min, opt_alt_max = bm["optimal_altitude"]
    if opt_alt_min <= alt <= opt_alt_max:
        stresses["altitude_stress"] = 0.0
    elif alt < opt_alt_min:
        stresses["altitude_stress"] = min(0.8, max(0.0, (opt_alt_min - alt) / 500))
    else:
        stresses["altitude_stress"] = min(0.8, max(0.0, (alt - opt_alt_max) / 600))

    return stresses

def simulate_agronomic_yield(params: Dict[str, Any]) -> Tuple[float, float, Dict[str, float]]:
    """
    Simulates actual yield and factor-wise yield loss in kg/ha based on multi-factorial interaction.
    """
    species = params.get("Coffee_Species", "Arabica")
    bm = COFFEE_BENCHMARKS.get(species, COFFEE_BENCHMARKS["Arabica"])
    potential = bm["potential_yield_kg_ha"]
    min_yield = bm["min_yield_kg_ha"]

    stresses = calculate_stress_factors(params)

    # Weights of each stress factor in overall yield penalty (calibrated to coffee physiology)
    loss_weights = {
        "ph_stress": 0.22,
        "n_stress": 0.20,
        "k_stress": 0.18,
        "rainfall_stress": 0.20,
        "blossom_stress": 0.15,
        "p_stress": 0.12,
        "temp_stress": 0.14,
        "oc_stress": 0.08,
        "altitude_stress": 0.08
    }

    # Calculate absolute loss per factor
    max_loss_potential = potential - min_yield
    losses = {}
    for factor, stress_val in stresses.items():
        w = loss_weights.get(factor, 0.1)
        loss_kg = stress_val * w * max_loss_potential
        losses[factor] = round(loss_kg, 2)

    total_loss_kg = min(max_loss_potential, sum(losses.values()))
    actual_yield = max(min_yield, potential - total_loss_kg)

    return round(actual_yield, 2), round(potential, 2), losses
