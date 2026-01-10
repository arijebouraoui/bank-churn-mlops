# optuna_optimization.py
import optuna
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import joblib
import json

# Load data
print("📂 Loading data...")
df = pd.read_csv("data/bank_churn.csv")
X = df.drop('Exited', axis=1)
y = df['Exited']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"✅ Data loaded: {len(X_train)} train samples\n")

def objective(trial):
    """Optuna objective function"""
    
    # Suggest hyperparameters
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 200),
        'max_depth': trial.suggest_int('max_depth', 5, 20),
        'min_samples_split': trial.suggest_int('min_samples_split', 2, 10),
        'min_samples_leaf': trial.suggest_int('min_samples_leaf', 1, 5),
        'random_state': 42
    }
    
    # Train model
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f"  Trial {trial.number}: Accuracy={accuracy:.4f}, F1={f1:.4f}, params={params}")
    
    return f1

# Run Optuna study
print("="*70)
print("🔍 Starting Optuna Hyperparameter Optimization")
print("   Running 10 trials to find best parameters...")
print("="*70 + "\n")

study = optuna.create_study(
    direction='maximize',
    study_name='bank-churn-optimization'
)

study.optimize(objective, n_trials=10, show_progress_bar=True)

# Results
print("\n" + "="*70)
print("✅ OPTIMIZATION COMPLETE!")
print("="*70)
print(f"\n🏆 Best F1 Score: {study.best_value:.4f}")
print(f"\n📊 Best Parameters:")
for key, value in study.best_params.items():
    print(f"   {key}: {value}")

# Train final model with best params
print("\n🤖 Training final model with best parameters...")
best_model = RandomForestClassifier(**study.best_params, random_state=42)
best_model.fit(X_train, y_train)

# Evaluate best model
y_pred_best = best_model.predict(X_test)
best_accuracy = accuracy_score(y_test, y_pred_best)
best_f1 = f1_score(y_test, y_pred_best)

print(f"✅ Best Model Performance:")
print(f"   Accuracy: {best_accuracy:.4f}")
print(f"   F1 Score: {best_f1:.4f}")

# Save best model
joblib.dump(best_model, "model/optuna_best_model.pkl")
print("\n💾 Best model saved to: model/optuna_best_model.pkl")

# Save results
results = {
    "best_params": study.best_params,
    "best_f1_score": study.best_value,
    "best_accuracy": best_accuracy,
    "n_trials": len(study.trials)
}

with open("model/optuna_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("📊 Results saved to: model/optuna_results.json")
print("\n" + "="*70)
print("🎉 Optimization Complete!")
print("="*70)