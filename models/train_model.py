"""
train_model.py
--------------
Trains, validates, and compares Machine Learning algorithms for Coffee Yield Prediction.
Evaluates Random Forest, XGBoost, and Gradient Boosting Regressor.
Generates SHAP explainability models and exports the best-performing pipeline.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import xgboost as xgb
import shap

def run_training():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_path = os.path.join(base_dir, "data", "coffee_dataset.csv")
    models_dir = os.path.join(base_dir, "models")
    os.makedirs(models_dir, exist_ok=True)

    print(f"Loading dataset from: {data_path}")
    df = pd.read_csv(data_path)
    
    # Feature sets
    categorical_features = ["Coffee_Species", "Region"]
    numeric_features = [
        "Altitude_meters",
        "Avg_Temperature_C",
        "Max_Temperature_C",
        "Min_Temperature_C",
        "Annual_Rainfall_mm",
        "Blossom_Rainfall_mm",
        "Soil_pH",
        "Nitrogen_N",
        "Phosphorus_P",
        "Potassium_K",
        "Organic_Carbon_pct",
        "Electrical_Conductivity_dS_m",
        "Relative_Humidity_pct",
        "Tree_Density_per_Ha"
    ]
    
    all_feature_names = categorical_features + numeric_features
    target = "Yield_kg_per_Ha"
    
    X = df[all_feature_names]
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=True
    )
    
    print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")
    
    # Preprocessing Pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features)
        ],
        remainder="drop"
    )
    
    # Candidate models
    candidate_models = {
        "Random_Forest": RandomForestRegressor(
            n_estimators=150, max_depth=14, min_samples_split=4, random_state=42, n_jobs=-1
        ),
        "XGBoost": xgb.XGBRegressor(
            n_estimators=180, learning_rate=0.07, max_depth=6, subsample=0.85,
            colsample_bytree=0.85, random_state=42, n_jobs=-1
        ),
        "Gradient_Boosting": GradientBoostingRegressor(
            n_estimators=150, learning_rate=0.08, max_depth=5, random_state=42
        )
    }
    
    results = {}
    fitted_pipelines = {}
    
    print("\n" + "="*50)
    print("MODEL TRAINING & COMPARATIVE BENCHMARKING")
    print("="*50)
    
    for name, model in candidate_models.items():
        pipe = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("regressor", model)
        ])
        
        pipe.fit(X_train, y_train)
        y_pred = pipe.predict(X_test)
        
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        mape = mean_absolute_percentage_error(y_test, y_pred) * 100.0
        
        results[name] = {
            "R2_Score": round(float(r2), 4),
            "RMSE": round(float(rmse), 2),
            "MAE": round(float(mae), 2),
            "MAPE_pct": round(float(mape), 2)
        }
        fitted_pipelines[name] = pipe
        
        print(f"[{name}]")
        print(f"  R2 Score : {r2:.4f}")
        print(f"  RMSE     : {rmse:.2f} kg/ha")
        print(f"  MAE      : {mae:.2f} kg/ha")
        print(f"  MAPE     : {mape:.2f} %\n")
        
    # Best model selection by R2
    best_model_name = max(results, key=lambda k: results[k]["R2_Score"])
    best_pipeline = fitted_pipelines[best_model_name]
    print(f"--> Best Performing Model: {best_model_name} (R2 = {results[best_model_name]['R2_Score']})")
    
    # Save the best model pipeline
    best_model_path = os.path.join(models_dir, "best_coffee_model.pkl")
    joblib.dump(best_pipeline, best_model_path)
    print(f"Saved best model pipeline to: {best_model_path}")
    
    # Preprocessed feature names
    encoder = best_pipeline.named_steps["preprocessor"].named_transformers_["cat"]
    cat_cols_encoded = list(encoder.get_feature_names_out(categorical_features))
    transformed_feature_names = numeric_features + cat_cols_encoded
    
    # Extract Global Feature Importances
    regressor = best_pipeline.named_steps["regressor"]
    if hasattr(regressor, "feature_importances_"):
        raw_importances = regressor.feature_importances_
        importance_dict = {
            feat: round(float(imp), 5)
            for feat, imp in sorted(zip(transformed_feature_names, raw_importances), key=lambda x: x[1], reverse=True)
        }
    else:
        importance_dict = {}
        
    # Fit SHAP Explainer
    print("Fitting SHAP TreeExplainer for Explainable AI...")
    X_train_trans = best_pipeline.named_steps["preprocessor"].transform(X_train)
    
    # Sample background for SHAP
    bg_sample = X_train_trans[:200]
    explainer = shap.TreeExplainer(regressor, data=bg_sample)
    
    explainer_path = os.path.join(models_dir, "shap_explainer.pkl")
    joblib.dump({
        "explainer": explainer,
        "feature_names": transformed_feature_names,
        "numeric_features": numeric_features,
        "categorical_features": categorical_features
    }, explainer_path)
    print(f"Saved SHAP explainer to: {explainer_path}")
    
    # Save metadata JSON
    metadata = {
        "best_model_name": best_model_name,
        "metrics": results,
        "transformed_feature_names": transformed_feature_names,
        "numeric_features": numeric_features,
        "categorical_features": categorical_features,
        "feature_importances": importance_dict,
        "training_samples_count": len(X_train),
        "test_samples_count": len(X_test)
    }
    
    meta_path = os.path.join(models_dir, "model_metadata.json")
    with open(meta_path, "w") as f:
        json.dump(metadata, f, indent=2)
    print(f"Saved model metadata and comparative benchmarks to: {meta_path}")

if __name__ == "__main__":
    run_training()
