from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import joblib
import numpy as np
import logging
import os

from opencensus.ext.azure.log_exporter import AzureLogHandler
from app.models import CustomerFeatures, PredictionResponse, HealthResponse

# ============================================================
# LOGGING & APPLICATION INSIGHTS
# ============================================================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bank-churn-api")

APPINSIGHTS_CONN = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")
if APPINSIGHTS_CONN:
    handler = AzureLogHandler(connection_string=APPINSIGHTS_CONN)
    logger.addHandler(handler)
    logger.info("app_startup", extra={
        "custom_dimensions": {
            "event_type": "startup",
            "status": "application_insights_connected"
        }
    })
else:
    logger.warning("app_startup", extra={
        "custom_dimensions": {
            "event_type": "startup",
            "status": "application_insights_not_configured"
        }
    })

# ============================================================
# FASTAPI INIT
# ============================================================
app = FastAPI(
    title="Bank Churn Prediction API",
    description="API de prédiction et monitoring du churn client",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = os.getenv("MODEL_PATH", "model/churn_model.pkl")
model = None

@app.on_event("startup")
async def load_model():
    global model
    try:
        model = joblib.load(MODEL_PATH)
        logger.info("model_loaded", extra={
            "custom_dimensions": {
                "event_type": "model_load",
                "model_path": MODEL_PATH,
                "status": "success"
            }
        })
    except Exception as e:
        logger.error("model_load_failed", extra={
            "custom_dimensions": {
                "event_type": "model_load",
                "error": str(e)
            }
        })
        model = None

# ============================================================
# GENERAL ENDPOINTS
# ============================================================
@app.get("/", tags=["General"])
def root():
    return {
        "message": "Bank Churn Prediction API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }

@app.get("/health", response_model=HealthResponse)
def health():
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "healthy", "model_loaded": True}

# ============================================================
# PREDICTION ENDPOINTS
# ============================================================
@app.post("/predict", response_model=PredictionResponse)
def predict(features: CustomerFeatures):
    if model is None:
        raise HTTPException(status_code=503, detail="Model unavailable")

    try:
        input_data = np.array([[  
            features.CreditScore,
            features.Age,
            features.Tenure,
            features.Balance,
            features.NumOfProducts,
            features.HasCrCard,
            features.IsActiveMember,
            features.EstimatedSalary,
            features.Geography_Germany,
            features.Geography_Spain
        ]])

        proba = float(model.predict_proba(input_data)[0][1])
        prediction = int(proba > 0.5)
        risk = "Low" if proba < 0.3 else "Medium" if proba < 0.7 else "High"

        logger.info("prediction", extra={
            "custom_dimensions": {
                "event_type": "prediction",
                "endpoint": "/predict",
                "probability": proba,
                "prediction": prediction,
                "risk_level": risk
            }
        })

        return {
            "churn_probability": round(proba, 4),
            "prediction": prediction,
            "risk_level": risk
        }

    except Exception as e:
        logger.error("prediction_error", extra={
            "custom_dimensions": {
                "event_type": "prediction_error",
                "error": str(e)
            }
        })
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/batch")
def predict_batch(features_list: List[CustomerFeatures]):
    if model is None:
        raise HTTPException(status_code=503, detail="Model unavailable")

    try:
        predictions = []
        for features in features_list:
            input_data = np.array([[  
                features.CreditScore,
                features.Age,
                features.Tenure,
                features.Balance,
                features.NumOfProducts,
                features.HasCrCard,
                features.IsActiveMember,
                features.EstimatedSalary,
                features.Geography_Germany,
                features.Geography_Spain
            ]])

            proba = float(model.predict_proba(input_data)[0][1])
            prediction = int(proba > 0.5)

            predictions.append({
                "churn_probability": round(proba, 4),
                "prediction": prediction
            })

        logger.info("batch_prediction", extra={
            "custom_dimensions": {
                "event_type": "batch_prediction",
                "count": len(predictions)
            }
        })

        return {
            "predictions": predictions,
            "count": len(predictions)
        }

    except Exception as e:
        logger.error("batch_prediction_error", extra={
            "custom_dimensions": {
                "event_type": "batch_prediction_error",
                "error": str(e)
            }
        })
        raise HTTPException(status_code=500, detail=str(e))