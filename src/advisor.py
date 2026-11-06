"""
advisor.py
----------
Prescriptive Agricultural Advisory Engine for Coffee Plantations.
Translates diagnosed yield-loss factors into concrete, actionable agronomic recommendations,
fertilizer dosage calculations, soil remediation, and irrigation schedules.
"""

from typing import Dict, Any, List
from src.agronomy_engine import COFFEE_BENCHMARKS

def generate_recommendations(input_params: Dict[str, Any], loss_report: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Generates tailored agronomic advice based on the loss diagnosis.
    Returns list of recommendations with:
    - category (Soil, Nutrition, Water, Canopy/Climate)
    - issue
    - urgency (High, Medium, Maintenance)
    - action
    - dosage_or_specification
    """
    species = input_params.get("Coffee_Species", "Arabica")
    bm = COFFEE_BENCHMARKS.get(species, COFFEE_BENCHMARKS["Arabica"])
    recommendations = []
    
    # 1. Soil pH / Acidity Remediation
    ph = input_params["Soil_pH"]
    opt_ph_min, opt_ph_max = bm["optimal_ph"]
    if ph < opt_ph_min:
        ph_deficit = opt_ph_min - ph
        # Standard lime requirement for laterite coffee soil: ~1.0 to 1.5 MT lime/ha per 0.5 pH deficit
        lime_kg_ha = int(round(ph_deficit * 2500))
        dolomite_kg_ha = int(round(lime_kg_ha * 0.6))
        agricultural_lime = int(round(lime_kg_ha * 0.4))
        recommendations.append({
            "category": "Soil Chemistry",
            "issue": f"Soil is Acidic (pH {ph:.2f} < optimal {opt_ph_min})",
            "urgency": "High" if ph < 5.2 else "Medium",
            "action": "Apply Agricultural Lime and Dolomite to neutralize soil acidity and unlock fixed nutrients.",
            "prescription": f"Broadcast {lime_kg_ha} kg/ha (or {round(lime_kg_ha*0.4047, 1)} kg/acre) of neutralizing agent. Recommended split: {agricultural_lime} kg/ha Agricultural Lime + {dolomite_kg_ha} kg/ha Dolomite (supplies essential Magnesium). Apply in October-November or April-May before onset of heavy showers."
        })
    elif ph > opt_ph_max:
        recommendations.append({
            "category": "Soil Chemistry",
            "issue": f"Soil pH is Alkaline for Coffee (pH {ph:.2f} > optimal {opt_ph_max})",
            "urgency": "Medium",
            "action": "Incorporate organic matter, elemental sulfur, or ammonium-based fertilizers to gently acidify soil.",
            "prescription": "Apply well-decomposed coffee pulp compost (5 MT/ha) and use Ammonium Sulphate instead of Urea as the nitrogen carrier."
        })

    # 2. Nitrogen (N) Advisory
    n_cur = input_params["Nitrogen_N"]
    n_opt_min, n_opt_max = bm["optimal_n"]
    if n_cur < n_opt_min:
        n_deficit = n_opt_min - n_cur
        # Urea has 46% N
        urea_kg_ha = int(round((n_deficit / 0.46)))
        recommendations.append({
            "category": "Crop Nutrition (N)",
            "issue": f"Nitrogen Deficit ({n_cur:.1f} kg/ha < target {n_opt_min} kg/ha)",
            "urgency": "High" if n_cur < 100 else "Medium",
            "action": "Apply balanced split doses of Nitrogen fertilizer to stimulate vegetative flush and berry cluster formation.",
            "prescription": f"Supplement with {urea_kg_ha} kg/ha Urea ({round(urea_kg_ha*0.4047, 1)} kg/acre). Split into 3 equal doses: Pre-monsoon (April/May), Post-monsoon (September/October), and Berry development (November). Apply in a wide drip-circle under tree canopy."
        })

    # 3. Phosphorus (P) Advisory
    p_cur = input_params["Phosphorus_P"]
    p_opt_min, p_opt_max = bm["optimal_p"]
    if p_cur < p_opt_min:
        p_deficit = p_opt_min - p_cur
        # Rock Phosphate (20-22% P2O5) or DAP (46% P2O5)
        dap_kg_ha = int(round((p_deficit / 0.46)))
        recommendations.append({
            "category": "Crop Nutrition (P)",
            "issue": f"Phosphorus Deficit ({p_cur:.1f} kg/ha < target {p_opt_min} kg/ha)",
            "urgency": "Medium",
            "action": "Apply phosphatic fertilizers to encourage feeder root proliferation and flowering.",
            "prescription": f"Incorporate {dap_kg_ha} kg/ha DAP or {int(p_deficit * 5.0)} kg/ha Mussoorie Rock Phosphate into soil trenches along with compost to prevent fixation."
        })

    # 4. Potassium (K) Advisory
    k_cur = input_params["Potassium_K"]
    k_opt_min, k_opt_max = bm["optimal_k"]
    if k_cur < k_opt_min:
        k_deficit = k_opt_min - k_cur
        # MOP (Muriate of Potash, 60% K2O)
        mop_kg_ha = int(round((k_deficit / 0.60)))
        recommendations.append({
            "category": "Crop Nutrition (K)",
            "issue": f"Potassium Deficit ({k_cur:.1f} kg/ha < target {k_opt_min} kg/ha)",
            "urgency": "High" if k_cur < 110 else "Medium",
            "action": "Apply Potash to prevent branch dieback, enhance bean weight, and improve moisture retention.",
            "prescription": f"Apply {mop_kg_ha} kg/ha MOP (Muriate of Potash) in 2 splits: August-September during berry expansion, and post-harvest in January."
        })

    # 5. Organic Carbon & Soil Structure
    oc_cur = input_params["Organic_Carbon_pct"]
    oc_opt_min = bm["optimal_oc"][0]
    if oc_cur < oc_opt_min:
        recommendations.append({
            "category": "Soil Health & Carbon",
            "issue": f"Low Soil Organic Carbon ({oc_cur:.2f}% < optimal {oc_opt_min}%)",
            "urgency": "Medium",
            "action": "Replenish organic matter to enhance moisture-holding capacity and beneficial microbial flora.",
            "prescription": "Mulch the plantation with fallen shade-tree leaves, prune shade trees (Dadaps/Silver Oak), and apply 5 to 8 tonnes/ha of well-aerated Farm Yard Manure (FYM) or enriched coffee pulp compost."
        })

    # 6. Water Management & Rainfall
    rain = input_params["Annual_Rainfall_mm"]
    blossom = input_params.get("Blossom_Rainfall_mm", 35.0)
    opt_rain_min, opt_rain_max = bm["optimal_rainfall"]
    opt_blossom_min = bm["optimal_blossom_rain"][0]
    
    if blossom < opt_blossom_min:
        recommendations.append({
            "category": "Water & Irrigation",
            "issue": f"Blossom Shower Inadequacy ({blossom:.1f} mm received vs {opt_blossom_min} mm required)",
            "urgency": "High",
            "action": "Immediate overhead sprinkler irrigation for floral anthesis and fruit setting.",
            "prescription": f"Deliver 25 mm equivalent overhead sprinkler irrigation (approx. 50,000 gallons/acre) within 7 days of dry spell break in February/March, followed by a 'backing shower' of 15 mm after 18-21 days."
        })
        
    if rain < opt_rain_min:
        recommendations.append({
            "category": "Water & Irrigation",
            "issue": f"Annual Rainfall Deficit ({rain:.1f} mm < optimal {opt_rain_min} mm)",
            "urgency": "High",
            "action": "Deploy micro-irrigation and soil moisture conservation barriers.",
            "prescription": "Install drip irrigation lines along tree rows delivering 4-6 liters/bush twice weekly during dry months (Dec-April). Maintain continuous green/dry leaf mulch around root zones."
        })
    elif rain > opt_rain_max:
        recommendations.append({
            "category": "Water & Drainage",
            "issue": f"Excess Rainfall / Waterlogging Risk ({rain:.1f} mm > optimal {opt_rain_max} mm)",
            "urgency": "Medium",
            "action": "Prevent root asphyxiation, collar rot, and fungal leaf rust epidemics.",
            "prescription": "Construct contour drainage trenches and cradle pits across hill slopes. Apply prophylactic 0.5% Bordeaux mixture spray to protect foliage against Coffee Leaf Rust (Hemileia vastatrix)."
        })

    # 7. Temperature & Micro-climate / Canopy Management
    temp_avg = input_params["Avg_Temperature_C"]
    opt_temp_min, opt_temp_max = bm["optimal_temp_avg"]
    if temp_avg > opt_temp_max:
        recommendations.append({
            "category": "Canopy & Shade Management",
            "issue": f"Thermal Heat Stress (Avg {temp_avg:.1f}°C > optimal {opt_temp_max}°C)",
            "urgency": "High",
            "action": "Establish two-tier shade canopy to buffer temperature and reduce solar irradiance.",
            "prescription": "Plant Erythrina lithosperma (Dadap) for lower quick shade and Grevillea robusta (Silver Oak) for high permanent shade. Target 50-60% filtered ambient sunlight to maintain plantation micro-climate below 28°C."
        })
        
    # If no issues found
    if not recommendations:
        recommendations.append({
            "category": "Maintenance",
            "issue": "All Parameters Within Optimal Agronomic Ranges",
            "urgency": "Maintenance",
            "action": "Maintain current standard operating practices.",
            "prescription": "Continue annual soil testing, biennial leaf tissue testing, and standard prophylactic Bordeaux spray cycles."
        })
        
    return recommendations
