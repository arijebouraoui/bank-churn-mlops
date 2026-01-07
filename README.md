# Bank Churn Prediction API

## Description
This project is a **Bank Churn Prediction API** built with **FastAPI**. It predicts the probability of a customer leaving a bank using a machine learning model (RandomForestClassifier). The project includes monitoring, drift detection, caching, and a Streamlit interface for testing.

The API is deployed on **Azure Container Apps** with **Application Insights** for monitoring and logging.


## Project Structure

bank_churn/
├── app/
│ ├── main.py # FastAPI application
│ ├── models.py # Pydantic models for requests/responses
│ └── drift_detect.py # Script to detect data drift
├── data/
│ ├── bank_churn.csv # Reference dataset
│ └── production_data.csv # Production dataset (drift testing)
├── model/
│ └── churn_model.pkl # Trained ML model
├── drift_data_gen.py # Script to generate data with drift
├── app_streamlit.py # Streamlit interface for testing the API
├── requirements.txt # Python dependencies
└── README.md

## Features

1. **Prediction Endpoint**  
   `POST /predict`  
   Accepts customer features as JSON and returns:
   - `churn_probability`
   - `prediction` (0 = no churn, 1 = churn)
   - `risk_level` (Low, Medium, High)

2. **Health Check**  
   `GET /health`  
   Checks if the model is loaded and the API is running.

3. **Data Drift Detection**  
   `POST /drift/check`  
   Compares production data with reference data and reports which features have drifted.

4. **Caching**  
   Predictions are cached to improve performance using `lru_cache`.

5. **Monitoring & Logging**  
   Integrated with Azure Application Insights.

6. **Streamlit Interface**  
   `app_streamlit.py` allows testing the API via a friendly UI.

## Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
pip install streamlit requests

2. Run API locally
uvicorn app.main:app --host 0.0.0.0 --port 8000

3. Test Endpoints

Health:
curl http://127.0.0.1:8000/health

Predict:
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{"CreditScore":650,"Age":40,"Tenure":5,"Balance":60000,"NumOfProducts":2,"HasCrCard":1,"IsActiveMember":1,"EstimatedSalary":50000,"Geography_Germany":0,"Geography_Spain":1}'

Drift Check:
python drift_data_gen.py
curl -X POST http://127.0.0.1:8000/drift/check

4. Streamlit Interface
Run the Streamlit UI to test the API:
streamlit run app_streamlit.py

Fill in the customer features.

Click Predict Churn to get results.

The interface will call the public API at:
https://bank-churn-api.victoriousmoss-65485a03.francecentral.azurecontainerapps.io/predict

Deployment

The API is deployed on Azure Container Apps.

Docker is used for containerization.

Application Insights is used for monitoring.

Drift detection ensures production data is tracked.

Predictions are cached for faster responses.









Author
Arij Bouraoui – Bank Churn Prediction Project for Déploiement de modèle IA Workshop

