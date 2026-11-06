"""
generate_coffee_data.py
-----------------------
Generates a realistic, research-grade synthetic dataset of coffee farms
combining soil nutrient reports, meteorological data, and geographical factors.
Includes biological interaction noise and ground-truth yield loss decomposition.
"""

import os
import sys
import numpy as np
import pandas as pd

# Add src to path for importing agronomy_engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.agronomy_engine import REGION_PRESETS, COFFEE_BENCHMARKS, simulate_agronomic_yield

def generate_dataset(n_samples: int = 3500, random_state: int = 42) -> pd.DataFrame:
    np.random.seed(random_state)
    regions = list(REGION_PRESETS.keys())
    
    data = []
    
    for i in range(n_samples):
        # Sample region
        region = np.random.choice(regions)
        preset = REGION_PRESETS[region]
        
        # 80% follow regional typical species, 20% mixed (for model generalizability)
        if np.random.rand() < 0.85:
            species = preset["species"]
        else:
            species = "Arabica" if preset["species"] == "Robusta" else "Robusta"
            
        bm = COFFEE_BENCHMARKS[species]
        
        # Altitude variation around region typical
        altitude = float(np.clip(
            np.random.normal(preset["altitude"], 150),
            250, 2000
        ))
        
        # Temperature (inversely correlated with altitude: ~0.65C drop per 100m)
        alt_delta = (altitude - preset["altitude"]) / 100.0
        avg_temp = float(np.clip(
            np.random.normal(preset["temp_avg"] - (alt_delta * 0.65), 1.8),
            14.0, 33.0
        ))
        max_temp = float(np.clip(avg_temp + np.random.uniform(5.0, 9.0), 22.0, 39.0))
        min_temp = float(np.clip(avg_temp - np.random.uniform(5.0, 8.5), 6.0, 24.0))
        
        # Rainfall around regional baseline with natural drought / excess rain tails
        rainfall = float(np.clip(
            np.random.normal(preset["rainfall"], 350) * np.random.choice([0.7, 1.0, 1.0, 1.0, 1.25], p=[0.15, 0.7, 0.05, 0.05, 0.05]),
            750, 3600
        ))
        
        # Blossom shower in March/April
        blossom_rain = float(np.clip(
            np.random.gamma(shape=3.5, scale=10.0),
            5.0, 80.0
        ))
        
        # Soil test report variables
        # pH (centered around regional tendency with realistic deviations)
        soil_ph = float(np.clip(
            np.random.normal(preset["ph"], 0.55),
            4.2, 7.8
        ))
        
        # N, P, K values
        n_val = float(np.clip(np.random.normal(150, 40), 40, 260))
        p_val = float(np.clip(np.random.normal(60, 22), 15, 130))
        k_val = float(np.clip(np.random.normal(160, 45), 45, 290))
        
        # Organic Carbon (%)
        oc_pct = float(np.clip(np.random.normal(1.4, 0.45), 0.4, 3.2))
        
        # Electrical conductivity (dS/m)
        ec_val = float(np.clip(np.random.normal(0.6, 0.3), 0.1, 2.5))
        
        # Relative humidity (%)
        humidity = float(np.clip(np.random.normal(75, 10), 45, 96))
        
        # Farm land size & planting density
        farm_area_ha = float(np.clip(np.random.exponential(scale=3.5) + 0.5, 0.5, 45.0))
        farm_area_acres = farm_area_ha * 2.47105
        tree_density = int(np.clip(np.random.normal(1600, 250), 1000, 2500))
        
        # Construct parameter dict
        farm_params = {
            "Coffee_Species": species,
            "Region": region,
            "Altitude_meters": round(altitude, 1),
            "Avg_Temperature_C": round(avg_temp, 1),
            "Max_Temperature_C": round(max_temp, 1),
            "Min_Temperature_C": round(min_temp, 1),
            "Annual_Rainfall_mm": round(rainfall, 1),
            "Blossom_Rainfall_mm": round(blossom_rain, 1),
            "Soil_pH": round(soil_ph, 2),
            "Nitrogen_N": round(n_val, 1),
            "Phosphorus_P": round(p_val, 1),
            "Potassium_K": round(k_val, 1),
            "Organic_Carbon_pct": round(oc_pct, 2),
            "Electrical_Conductivity_dS_m": round(ec_val, 2),
            "Relative_Humidity_pct": round(humidity, 1),
            "Farm_Area_Hectares": round(farm_area_ha, 2),
            "Farm_Area_Acres": round(farm_area_acres, 2),
            "Tree_Density_per_Ha": tree_density
        }
        
        # Simulate agronomic yield and factor losses
        sim_yield, pot_yield, losses = simulate_agronomic_yield(farm_params)
        
        # Add realistic micro-climate stochastic noise (+/- 4%)
        noise = np.random.normal(0, pot_yield * 0.035)
        actual_yield = float(np.clip(sim_yield + noise, bm["min_yield_kg_ha"], pot_yield * 1.05))
        actual_yield = round(actual_yield, 2)
        
        total_loss = round(max(0.0, pot_yield - actual_yield), 2)
        
        # Identify top primary and secondary loss factors
        sorted_losses = sorted(losses.items(), key=lambda x: x[1], reverse=True)
        primary_loss = sorted_losses[0][0].replace("_stress", "").title() if sorted_losses[0][1] > 25.0 else "None (Optimal)"
        secondary_loss = sorted_losses[1][0].replace("_stress", "").title() if sorted_losses[1][1] > 25.0 else "None"
        
        # Factor name cleaning
        name_map = {
            "Ph": "Soil Acidity / pH Stress",
            "N": "Nitrogen Deficiency",
            "P": "Phosphorus Deficiency",
            "K": "Potassium Deficiency",
            "Rainfall": "Rainfall Imbalance (Drought/Excess)",
            "Blossom": "Blossom Shower Deficit",
            "Temp": "Temperature Stress (Heat/Cold)",
            "Oc": "Organic Carbon Deficiency",
            "Altitude": "Altitude Mismatch"
        }
        primary_loss_clean = name_map.get(primary_loss, primary_loss)
        secondary_loss_clean = name_map.get(secondary_loss, secondary_loss)
        
        total_yield_kg = round(actual_yield * farm_area_ha, 2)
        total_yield_mt = round(total_yield_kg / 1000.0, 3)
        
        row = {
            **farm_params,
            "Yield_kg_per_Ha": actual_yield,
            "Potential_Yield_kg_ha": pot_yield,
            "Yield_Loss_kg_ha": total_loss,
            "Yield_Efficiency_pct": round((actual_yield / pot_yield) * 100.0, 1),
            "Total_Yield_kg": total_yield_kg,
            "Total_Yield_MT": total_yield_mt,
            "Primary_Loss_Factor": primary_loss_clean,
            "Secondary_Loss_Factor": secondary_loss_clean,
            # Explicit factor-wise loss columns
            "Loss_pH_kg_ha": losses.get("ph_stress", 0.0),
            "Loss_Nitrogen_kg_ha": losses.get("n_stress", 0.0),
            "Loss_Phosphorus_kg_ha": losses.get("p_stress", 0.0),
            "Loss_Potassium_kg_ha": losses.get("k_stress", 0.0),
            "Loss_Rainfall_kg_ha": losses.get("rainfall_stress", 0.0),
            "Loss_Blossom_kg_ha": losses.get("blossom_stress", 0.0),
            "Loss_Temperature_kg_ha": losses.get("temp_stress", 0.0),
            "Loss_OrganicCarbon_kg_ha": losses.get("oc_stress", 0.0),
            "Loss_Altitude_kg_ha": losses.get("altitude_stress", 0.0)
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    os.makedirs(out_dir, exist_ok=True)
    out_csv = os.path.join(out_dir, "coffee_dataset.csv")
    
    print(f"Generating synthetic coffee agronomic dataset...")
    df = generate_dataset(n_samples=3500)
    df.to_csv(out_csv, index=False)
    print(f"Successfully generated {len(df)} records and saved to {out_csv}")
    print("\nSummary Statistics of Target (Yield_kg_per_Ha):")
    print(df.groupby("Coffee_Species")["Yield_kg_per_Ha"].describe())
