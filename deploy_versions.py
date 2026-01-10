# deploy_versions.py
import shutil
import os
import time
import requests
import json

print("="*70)
print("🚀 DEMONSTRATION: Model Versioning (v1 → v2 → Rollback)")
print("="*70)

# Backup current model
print("\n📦 Step 1: Backup current model...")
if os.path.exists("model/churn_model.pkl"):
    shutil.copy("model/churn_model.pkl", "model/churn_model_backup.pkl")
    print("✅ Backup created: churn_model_backup.pkl")

# Test data
test_customer = {
    "CreditScore": 650,
    "Age": 35,
    "Tenure": 5,
    "Balance": 50000,
    "NumOfProducts": 2,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 75000,
    "Geography_Germany": 0,
    "Geography_Spain": 1
}

def test_prediction(version):
    """Test API prediction"""
    print(f"\n🧪 Testing {version}...")
    try:
        response = requests.post(
            "http://localhost:8000/predict",
            json=test_customer,
            timeout=5
        )
        result = response.json()
        print(f"   Churn Probability: {result['churn_probability']}")
        print(f"   Prediction: {result['prediction']}")
        print(f"   Risk Level: {result['risk_level']}")
        return result
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None

# Test v1 (baseline model)
print("\n" + "="*70)
print("📌 CURRENT VERSION: v1 (Baseline Model)")
print("   n_estimators=100, max_depth=10")
print("="*70)
v1_result = test_prediction("v1")

# Deploy v2 (Optuna optimized)
print("\n" + "="*70)
print("🔄 DEPLOYING v2: Optuna Optimized Model")
print("   n_estimators=90, max_depth=14")
print("="*70)

if os.path.exists("model/optuna_best_model.pkl"):
    print("\n📦 Step 2: Deploying v2 model...")
    shutil.copy("model/optuna_best_model.pkl", "model/churn_model.pkl")
    print("✅ v2 deployed!")
    
    # Need to restart container to load new model
    print("\n⏳ Restarting API container...")
    os.system("docker-compose restart api")
    time.sleep(10)  # Wait for restart
    
    print("\n" + "="*70)
    print("📌 NEW VERSION: v2 (Optimized Model)")
    print("="*70)
    v2_result = test_prediction("v2")
else:
    print("❌ Optuna model not found! Skipping v2 deployment.")
    v2_result = None

# Rollback to v1
print("\n" + "="*70)
print("⏪ ROLLBACK: Reverting to v1")
print("="*70)

print("\n📦 Step 3: Rolling back to v1...")
if os.path.exists("model/churn_model_backup.pkl"):
    shutil.copy("model/churn_model_backup.pkl", "model/churn_model.pkl")
    print("✅ Rollback completed!")
    
    print("\n⏳ Restarting API container...")
    os.system("docker-compose restart api")
    time.sleep(10)  # Wait for restart
    
    print("\n" + "="*70)
    print("📌 ROLLED BACK TO: v1 (Baseline Model)")
    print("="*70)
    v1_rollback = test_prediction("v1 (after rollback)")
else:
    print("❌ Backup not found!")

# Summary
print("\n" + "="*70)
print("📊 SUMMARY")
print("="*70)
if v1_result:
    print(f"\nv1 (Baseline):  Churn Prob = {v1_result['churn_probability']}")
if v2_result:
    print(f"v2 (Optimized): Churn Prob = {v2_result['churn_probability']}")
if v1_rollback:
    print(f"v1 (Rollback):  Churn Prob = {v1_rollback['churn_probability']}")

print("\n✅ Demonstration Complete!")
print("="*70)