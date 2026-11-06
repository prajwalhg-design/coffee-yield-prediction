"""
loss_analyzer.py
----------------
Analyzes and decomposes coffee yield loss based on:
1. Explainable AI (SHAP TreeExplainer values from the ML model)
2. Agronomic Stress Factor Decomposition (Bio-physical penalties in kg/ha)
Identifies the primary bottlenecks causing yield reduction below potential.
"""

from typing import Dict, Any, List, Tuple
import numpy as np
import pandas as pd
from src.agronomy_engine import COFFEE_BENCHMARKS, calculate_stress_factors

FACTOR_DISPLAY_NAMES = {
    "ph_stress": ("Soil Acidity / pH Stress", "Soil pH"),
    "n_stress": ("Nitrogen Deficiency", "Nitrogen (N)"),
    "p_stress": ("Phosphorus Deficiency", "Phosphorus (P)"),
    "k_stress": ("Potassium Deficiency", "Potassium (K)"),
    "rainfall_stress": ("Rainfall Deficit / Excess", "Annual Rainfall"),
    "blossom_stress": ("Blossom Shower Inadequacy", "Blossom Rain"),
    "temp_stress": ("Thermal Stress (Heat/Cold)", "Avg Temperature"),
    "oc_stress": ("Low Organic Carbon", "Organic Carbon"),
    "altitude_stress": ("Suboptimal Altitude", "Altitude")
}

def analyze_yield_loss(
    input_params: Dict[str, Any],
    predicted_yield_kg_ha: float,
    shap_contributions: Dict[str, float] = None
) -> Dict[str, Any]:
    """
    Computes a comprehensive loss diagnosis report.
    Returns:
    - potential_yield_kg_ha
    - total_loss_kg_ha
    - yield_efficiency_pct
    - factor_loss_breakdown (list of dicts with name, kg_ha_lost, pct_contribution, severity)
    - shap_breakdown (if shap provided)
    - primary_bottleneck
    - secondary_bottleneck
    """
    species = input_params.get("Coffee_Species", "Arabica")
    bm = COFFEE_BENCHMARKS.get(species, COFFEE_BENCHMARKS["Arabica"])
    potential_yield = bm["potential_yield_kg_ha"]
    
    # Total loss relative to ideal potential
    total_loss_kg_ha = max(0.0, round(potential_yield - predicted_yield_kg_ha, 2))
    efficiency_pct = round((predicted_yield_kg_ha / potential_yield) * 100.0, 1) if potential_yield > 0 else 0.0

    # Calculate stress indicators
    stresses = calculate_stress_factors(input_params)
    
    # Agronomic weights
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
    
    # Compute raw loss per factor
    max_loss_potential = potential_yield - bm["min_yield_kg_ha"]
    factor_losses = {}
    for key, stress in stresses.items():
        w = loss_weights.get(key, 0.1)
        loss_kg = stress * w * max_loss_potential
        factor_losses[key] = loss_kg
        
    sum_losses = sum(factor_losses.values())
    
    # Re-normalize factor losses to match the actual ML predicted gap
    breakdown = []
    if sum_losses > 0 and total_loss_kg_ha > 0:
        scale = total_loss_kg_ha / sum_losses
        for key, raw_loss in factor_losses.items():
            adj_loss = raw_loss * scale
            pct = (adj_loss / total_loss_kg_ha) * 100.0 if total_loss_kg_ha > 0 else 0.0
            
            # Severity classification
            if pct >= 30.0:
                severity = "Critical"
            elif pct >= 15.0:
                severity = "Moderate"
            elif pct > 3.0:
                severity = "Minor"
            else:
                severity = "Negligible"
                
            display_name, input_feature = FACTOR_DISPLAY_NAMES.get(key, (key, key))
            
            breakdown.append({
                "factor_key": key,
                "display_name": display_name,
                "input_feature": input_feature,
                "loss_kg_ha": round(adj_loss, 2),
                "loss_percentage": round(pct, 1),
                "severity": severity,
                "stress_index": round(stresses[key], 2)
            })
    else:
        for key in stresses.keys():
            display_name, input_feature = FACTOR_DISPLAY_NAMES.get(key, (key, key))
            breakdown.append({
                "factor_key": key,
                "display_name": display_name,
                "input_feature": input_feature,
                "loss_kg_ha": 0.0,
                "loss_percentage": 0.0,
                "severity": "None (Optimal)",
                "stress_index": 0.0
            })
            
    # Sort by impact
    breakdown = sorted(breakdown, key=lambda x: x["loss_kg_ha"], reverse=True)
    
    primary = breakdown[0]["display_name"] if breakdown and breakdown[0]["loss_kg_ha"] > 15.0 else "None (Conditions Optimal)"
    secondary = breakdown[1]["display_name"] if len(breakdown) > 1 and breakdown[1]["loss_kg_ha"] > 15.0 else "None"

    return {
        "species": species,
        "potential_yield_kg_ha": potential_yield,
        "predicted_yield_kg_ha": predicted_yield_kg_ha,
        "total_loss_kg_ha": total_loss_kg_ha,
        "yield_efficiency_pct": efficiency_pct,
        "primary_bottleneck": primary,
        "secondary_bottleneck": secondary,
        "breakdown": breakdown,
        "shap_contributions": shap_contributions or {}
    }
