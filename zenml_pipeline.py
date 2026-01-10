# zenml_pipeline.py
from zenml import pipeline, step
from typing import Tuple, Annotated
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import joblib
import json

@step
def load_data() -> Tuple[
    Annotated[pd.DataFrame, "X_train"],
    Annotated[pd.DataFrame, "X_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"]
]:
    """Load bank churn dataset"""
    print("📂 Loading data...")
    df = pd.read_csv("data/bank_churn.csv")
    
    X = df.drop('Exited', axis=1)
    y = df['Exited']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"✅ Data loaded: {len(X_train)} train, {len(X_test)} test samples")
    return X_train, X_test, y_train, y_test

@step
def train_model(
    X_train: pd.DataFrame, 
    y_train: pd.Series, 
    n_estimators: int = 100, 
    max_depth: int = 10
) -> Annotated[RandomForestClassifier, "model"]:
    """Train Random Forest model"""
    print(f"🤖 Training model with n_estimators={n_estimators}, max_depth={max_depth}...")
    
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=5,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    print(" Model trained successfully")
    return model

@step
def evaluate_model(
    model: RandomForestClassifier, 
    X_test: pd.DataFrame, 
    y_test: pd.Series
) -> Annotated[dict, "metrics"]:
    """Evaluate model performance"""
    print(" Evaluating model...")
    
    y_pred = model.predict(X_test)
    
    metrics = {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "f1_score": float(f1_score(y_test, y_pred))
    }
    
    print(f" Accuracy: {metrics['accuracy']:.4f}")
    print(f" F1 Score: {metrics['f1_score']:.4f}")
    
    return metrics

@step
def export_model(
    model: RandomForestClassifier, 
    metrics: dict
) -> Annotated[str, "model_path"]:
    """Export trained model"""
    print(" Exporting model...")
    
    model_path = "model/zenml_model.pkl"
    joblib.dump(model, model_path)
    
    # Save metrics
    with open("model/zenml_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
    
    print(f" Model exported to {model_path}")
    return model_path

@pipeline
def training_pipeline(n_estimators: int = 100, max_depth: int = 10):
    """Complete training pipeline"""
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train, n_estimators, max_depth)
    metrics = evaluate_model(model, X_test, y_test)
    model_path = export_model(model, metrics)

if __name__ == "__main__":
    # Run baseline pipeline
    print("="*50)
    print(" Running ZenML Pipeline - Baseline")
    print("="*50)
    training_pipeline()