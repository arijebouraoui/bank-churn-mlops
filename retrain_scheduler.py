# retrain_scheduler.py
"""
Script de retrain automatique basé sur des conditions.
Peut être déclenché:
1. Sur un schedule (cron job)
2. Quand la performance baisse
3. Quand les données driftent
"""

import os
import json
import joblib
import pandas as pd
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import mlflow

# Configuration
MODEL_PATH = "model/churn_model.pkl"
METRICS_PATH = "model/current_metrics.json"
MIN_ACCURACY_THRESHOLD = 0.70
MIN_F1_THRESHOLD = 0.25
RETRAIN_INTERVAL_DAYS = 7

def should_retrain():
    """
    Détermine si le modèle doit être réentraîné.
    
    Conditions de retrain:
    1. Modèle trop vieux (> 7 jours)
    2. Performance en baisse
    3. Pas de modèle existant
    """
    reasons = []
    
    # Condition 1: Vérifier si le modèle existe
    if not os.path.exists(MODEL_PATH):
        reasons.append("No model found")
        return True, reasons
    
    # Condition 2: Vérifier l'âge du modèle
    model_age = datetime.now() - datetime.fromtimestamp(
        os.path.getmtime(MODEL_PATH)
    )
    if model_age.days >= RETRAIN_INTERVAL_DAYS:
        reasons.append(f"Model is {model_age.days} days old (threshold: {RETRAIN_INTERVAL_DAYS})")
        return True, reasons
    
    # Condition 3: Vérifier les métriques
    if os.path.exists(METRICS_PATH):
        with open(METRICS_PATH, 'r') as f:
            metrics = json.load(f)
        
        if metrics.get('accuracy', 1.0) < MIN_ACCURACY_THRESHOLD:
            reasons.append(f"Accuracy below threshold: {metrics['accuracy']:.4f} < {MIN_ACCURACY_THRESHOLD}")
            return True, reasons
        
        if metrics.get('f1_score', 1.0) < MIN_F1_THRESHOLD:
            reasons.append(f"F1 Score below threshold: {metrics['f1_score']:.4f} < {MIN_F1_THRESHOLD}")
            return True, reasons
    
    return False, reasons

def retrain_model():
    """Réentraîner le modèle"""
    print("="*70)
    print("🔄 RETRAINING MODEL")
    print("="*70)
    
    # Load data
    print("\n📂 Loading data...")
    df = pd.read_csv("data/bank_churn.csv")
    X = df.drop('Exited', axis=1)
    y = df['Exited']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"✅ Data loaded: {len(X_train)} train, {len(X_test)} test samples")
    
    # Train model
    print("\n🤖 Training model...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        random_state=42
    )
    model.fit(X_train, y_train)
    print("✅ Model trained")
    
    # Evaluate
    print("\n📊 Evaluating model...")
    y_pred = model.predict(X_test)
    
    metrics = {
    "accuracy": float(accuracy_score(y_test, y_pred)),
    "f1_score": float(f1_score(y_test, y_pred)),
    "timestamp": datetime.now().isoformat(),
    "samples_trained": len(X_train)
    }

    # Séparer les métriques MLflow (seulement des nombres)
    mlflow_metrics = {
    "accuracy": metrics["accuracy"],
    "f1_score": metrics["f1_score"],
    "samples_trained": metrics["samples_trained"]
    }
    
    print(f"   Accuracy: {metrics['accuracy']:.4f}")
    print(f"   F1 Score: {metrics['f1_score']:.4f}")
    
    # Save model
    print("\n💾 Saving model...")
    
    # Backup old model
    if os.path.exists(MODEL_PATH):
        backup_path = MODEL_PATH.replace('.pkl', f'_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pkl')
        os.rename(MODEL_PATH, backup_path)
        print(f"   Old model backed up: {backup_path}")
    
    # Save new model
    joblib.dump(model, MODEL_PATH)
    print(f"✅ Model saved: {MODEL_PATH}")
    
    # Save metrics
    with open(METRICS_PATH, 'w') as f:
        json.dump(metrics, f, indent=2)
    print(f"✅ Metrics saved: {METRICS_PATH}")
    
    # Log to MLflow
    mlflow.set_tracking_uri("./mlruns")
    mlflow.set_experiment("bank-churn-retrain")
    
    with mlflow.start_run(run_name=f"retrain_{datetime.now().strftime('%Y%m%d_%H%M%S')}"):
        mlflow.log_params({
            "n_estimators": 100,
            "max_depth": 10,
            "retrain_trigger": "scheduled"
        })
        mlflow.log_metrics(mlflow_metrics)
        mlflow.sklearn.log_model(model, "model")
    
    print("\n✅ Model logged to MLflow")
    
    return metrics

def main():
    """Main retrain scheduler"""
    print("="*70)
    print("🔍 RETRAIN SCHEDULER - Checking if retrain needed")
    print("="*70)
    
    needs_retrain, reasons = should_retrain()
    
    if needs_retrain:
        print("\⚠️ RETRAIN REQUIRED!")
        print("Reasons:")
        for reason in reasons:
            print(f"  - {reason}")
        
        print("\n🚀 Starting retrain process...")
        metrics = retrain_model()
        
        print("\n" + "="*70)
        print("✅ RETRAIN COMPLETE!")
        print("="*70)
        print(f"New model metrics:")
        print(f"  Accuracy: {metrics['accuracy']:.4f}")
        print(f"  F1 Score: {metrics['f1_score']:.4f}")
        print(f"  Timestamp: {metrics['timestamp']}")
        
    else:
        print("\n✅ No retrain needed")
        print("Current model is performing well and is recent enough")
        
        if os.path.exists(METRICS_PATH):
            with open(METRICS_PATH, 'r') as f:
                metrics = json.load(f)
            print(f"\nCurrent metrics:")
            print(f"  Accuracy: {metrics.get('accuracy', 'N/A')}")
            print(f"  F1 Score: {metrics.get('f1_score', 'N/A')}")
            print(f"  Last trained: {metrics.get('timestamp', 'Unknown')}")

if __name__ == "__main__":
    main()