\# Bank Churn Prediction API



\## Description

This project is a \*\*Bank Churn Prediction API\*\* built with \*\*FastAPI\*\*. It predicts the probability of a customer leaving a bank using a machine learning model (RandomForestClassifier). The project includes monitoring, drift detection, and caching for production readiness. The API is deployed on \*\*Azure Container Apps\*\* with \*\*Application Insights\*\* for monitoring and logging.



\## Project Structure

bank\_churn/

├── app/

│ ├── main.py # FastAPI application

│ ├── models.py # Pydantic models for requests/responses

│ └── drift\_detect.py # Script to detect data drift

├── data/

│ ├── bank\_churn.csv # Reference dataset

│ └── production\_data.csv # Production dataset (drift testing)

├── model/

│ └── churn\_model.pkl # Trained ML model

├── drift\_data\_gen.py # Script to generate data with drift

├── requirements.txt # Python dependencies

└── README.md







\## Features

1\. \*\*Prediction Endpoint\*\*  

&nbsp;  `POST /predict`  

&nbsp;  Accepts customer features as JSON and returns:  

&nbsp;  - `churn\_probability`  

&nbsp;  - `prediction` (0 = no churn, 1 = churn)  

&nbsp;  - `risk\_level` (Low, Medium, High)



2\. \*\*Health Check\*\*  

&nbsp;  `GET /health`  

&nbsp;  Checks if the model is loaded and the API is running.



3\. \*\*Data Drift Detection\*\*  

&nbsp;  `POST /drift/check`  

&nbsp;  Compares production data with reference data and reports which features have drifted.



4\. \*\*Caching\*\*  

&nbsp;  Predictions are cached to improve performance using `lru\_cache`.



5\. \*\*Monitoring \& Logging\*\*  

&nbsp;  Integrated with Azure Application Insights.



\## How to Access the API



The API is deployed on Azure Container Apps. Use the following \*\*base URL\*\* for all endpoints:  



https://bank-churn-api.victoriousmoss-65485a03.francecentral.azurecontainerapps.io



\*\*Important:\*\* Accessing the root URL will return `{"detail":"Not Found"}`. You must call one of the endpoints:



\- \*\*Health Check:\*\*  

&nbsp; ```bash

&nbsp; curl https://bank-churn-api.victoriousmoss-65485a03.francecentral.azurecontainerapps.io/health



Predict Churn:

curl -X POST https://bank-churn-api.victoriousmoss-65485a03.francecentral.azurecontainerapps.io/predict \\

-H "Content-Type: application/json" \\

-d '{"CreditScore":650,"Age":40,"Tenure":5,"Balance":60000,"NumOfProducts":2,"HasCrCard":1,"IsActiveMember":1,"EstimatedSalary":50000,"Geography\_Germany":0,"Geography\_Spain":1}'



Data Drift Check:



First, generate production data with drift:



python drift\_data\_gen.py





Then call the endpoint:



curl -X POST https://bank-churn-api.victoriousmoss-65485a03.francecentral.azurecontainerapps.io/drift/check



Setup Instructions (Local)



Install dependencies:



pip install -r requirements.txt





Run API locally:



uvicorn app.main:app --host 0.0.0.0 --port 8000





Test endpoints locally using the same commands as above, replacing the Azure URL with http://127.0.0.1:8000.



Author



Arij Bouraoui – Bank Churn Prediction Project for Déploiement de modèle IA Workshop

