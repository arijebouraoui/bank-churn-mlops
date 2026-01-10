# 🏦 Bank Churn Prediction - MLOps Complete Project

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![MLflow](https://img.shields.io/badge/MLflow-2.8-orange.svg)](https://mlflow.org/)
[![ZenML](https://img.shields.io/badge/ZenML-0.93-purple.svg)](https://zenml.io/)
[![DVC](https://img.shields.io/badge/DVC-3.66-red.svg)](https://dvc.org/)

**Complete MLOps pipeline for predicting bank customer churn using Random Forest, with automated training, deployment, versioning, and monitoring.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Data Versioning (DVC)](#data-versioning-dvc)
- [ML Pipeline (ZenML)](#ml-pipeline-zenml)
- [Hyperparameter Optimization (Optuna)](#hyperparameter-optimization-optuna)
- [Docker Deployment](#docker-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [API Documentation](#api-documentation)
- [Model Versioning](#model-versioning)
- [Monitoring](#monitoring)
- [Results](#results)
- [Contributing](#contributing)

---

## 🎯 Overview

This project implements a complete **MLOps workflow** for predicting bank customer churn. It demonstrates industry best practices including:

- **Data Versioning** with DVC
- **Experiment Tracking** with MLflow
- **Pipeline Orchestration** with ZenML
- **Hyperparameter Optimization** with Optuna
- **Containerization** with Docker & Docker Compose
- **CI/CD** with GitHub Actions
- **API Deployment** on Azure Container Apps
- **Monitoring** with Azure Application Insights
- **Model Versioning** with v1/v2 and rollback capabilities

---

## 🏗️ Architecture
```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   GitHub    │─────▶│GitHub Actions│─────▶│   Docker    │
│ Repository  │      │   CI/CD      │      │   Build     │
└─────────────┘      └──────────────┘      └─────────────┘
                              │                     │
                              ▼                     ▼
                     ┌─────────────────┐   ┌──────────────┐
                     │  Run Tests      │   │Push to Azure │
                     │  - pytest       │   │Container Reg.│
                     └─────────────────┘   └──────────────┘
                                                    │
                                                    ▼
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│     DVC     │      │    ZenML     │      │   Azure     │
│Data Version │◀────▶│  Pipelines   │─────▶│Container App│
└─────────────┘      └──────────────┘      └─────────────┘
       │                     │                     │
       ▼                     ▼                     ▼
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   MLflow    │      │   Optuna     │      │  FastAPI    │
│Experiments  │      │Optimization  │      │   Serving   │
└─────────────┘      └──────────────┘      └─────────────┘
                                                    │
                                                    ▼
                                           ┌─────────────┐
                                           │App Insights │
                                           │ Monitoring  │
                                           └─────────────┘
```

---

## ✨ Features

### 🤖 Machine Learning
- **Model**: Random Forest Classifier
- **Dataset**: Bank Churn (10,000 samples, 10 features)
- **Metrics**: Accuracy, F1 Score, Precision, Recall
- **Baseline**: 76.5% accuracy
- **Optimized**: 76.5% accuracy with improved F1 score (+11%)

### 🔄 MLOps Pipeline
- ✅ **DVC**: Data version control with remote storage
- ✅ **MLflow**: Experiment tracking and model registry
- ✅ **ZenML**: Pipeline orchestration (data → train → eval → export)
- ✅ **Optuna**: Automated hyperparameter tuning (10 trials)
- ✅ **Docker**: Containerized application
- ✅ **Docker Compose**: Multi-service orchestration
- ✅ **GitHub Actions**: Automated CI/CD
- ✅ **Azure Deployment**: Production-ready API
- ✅ **Monitoring**: Application Insights integration

### 🌐 API Features
- `/health` - Health check endpoint
- `/predict` - Single prediction
- `/predict/batch` - Batch predictions
- `/docs` - Interactive Swagger UI
- `/redoc` - ReDoc documentation

### 🎨 User Interface
- **Streamlit Dashboard**: Professional web interface with:
  - Interactive input forms
  - Real-time predictions
  - Risk visualization (gauge charts)
  - Recommendations based on risk level

---

## 📁 Project Structure
```
bank-churn-mlops/
├── .dvc/                      # DVC configuration
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions pipeline
├── .zen/                      # ZenML configuration
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI application
│   └── models.py             # Pydantic models
├── data/
│   ├── bank_churn.csv        # Dataset (tracked by DVC)
│   └── bank_churn.csv.dvc    # DVC tracking file
├── model/
│   ├── churn_model.pkl       # Trained model (v1)
│   ├── zenml_model.pkl       # ZenML pipeline model
│   ├── optuna_best_model.pkl # Optimized model (v2)
│   ├── zenml_metrics.json    # ZenML results
│   └── optuna_results.json   # Optuna results
├── mlruns/                    # MLflow tracking data
├── tests/
│   └── test_api.py           # API tests
├── .dockerignore
├── .dvcignore
├── .gitignore
├── app_streamlit.py          # Streamlit UI
├── docker-compose.yml        # Docker Compose configuration
├── Dockerfile                # Docker image definition
├── generate_data.py          # Dataset generation
├── train_model.py            # Model training script
├── zenml_pipeline.py         # ZenML pipeline
├── run_variations.py         # Run multiple pipeline variations
├── optuna_optimization.py    # Optuna hyperparameter tuning
├── deploy_versions.py        # Model version deployment demo
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## 📦 Requirements

### Software
- Python 3.11+
- Docker Desktop
- Git
- Azure CLI (for cloud deployment)

### Python Packages
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
scikit-learn==1.3.2
pandas==2.1.3
mlflow==2.8.1
zenml[local]==0.93.0
dvc==3.66.1
optuna==3.0+
streamlit==1.31.0
plotly==6.5.0
```

See `requirements.txt` for complete list.

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/arijebouraoui/bank-churn-mlops.git
cd bank-churn-mlops
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize DVC
```bash
# Initialize DVC
python -m dvc init

# Configure remote storage (local example)
mkdir C:\dvc-storage
python -m dvc remote add -d myremote C:\dvc-storage

# Pull data
python -m dvc pull
```

### 5. Initialize ZenML
```bash
# Initialize ZenML (use full path on Windows)
C:\Users\YOUR_USERNAME\AppData\Roaming\Python\Python311\Scripts\zenml.exe init
```

---

## ⚡ Quick Start

### Train Model
```bash
# Generate dataset
python generate_data.py

# Train baseline model
python train_model.py

# View MLflow UI
mlflow ui --port 5000
# Open http://localhost:5000
```

### Run ZenML Pipeline
```bash
# Single run
python zenml_pipeline.py

# Multiple variations
python run_variations.py

# View ZenML runs
C:\Users\YOUR_USERNAME\AppData\Roaming\Python\Python311\Scripts\zenml.exe pipeline runs list
```

### Optimize with Optuna
```bash
# Run hyperparameter optimization (10 trials)
python optuna_optimization.py

# View results
type model\optuna_results.json
```

### Local API Testing
```bash
# Start API
uvicorn app.main:app --reload --port 8000

# Test health
curl http://localhost:8000/health

# Test prediction
curl -X POST "http://localhost:8000/predict" ^
  -H "Content-Type: application/json" ^
  -d "{\"CreditScore\": 650, \"Age\": 35, \"Tenure\": 5, \"Balance\": 50000, \"NumOfProducts\": 2, \"HasCrCard\": 1, \"IsActiveMember\": 1, \"EstimatedSalary\": 75000, \"Geography_Germany\": 0, \"Geography_Spain\": 1}"
```

### Streamlit Dashboard
```bash
streamlit run app_streamlit.py
# Opens automatically at http://localhost:8501
```

---

## 💾 Data Versioning (DVC)

### Why DVC?
- Track large datasets without bloating Git
- Version control for data and models
- Reproduce experiments with exact data versions
- Share data efficiently across team

### DVC Workflow
```bash
# Track new data file
python -m dvc add data/new_dataset.csv

# Commit DVC file to Git
git add data/new_dataset.csv.dvc data/.gitignore
git commit -m "Add new dataset"

# Push data to remote
python -m dvc push

# Pull data on another machine
python -m dvc pull
```

### DVC Remote Storage

Currently configured with local storage at `C:\dvc-storage`. For production, configure cloud storage:
```bash
# AWS S3
python -m dvc remote add -d s3remote s3://mybucket/dvcstore

# Google Cloud Storage
python -m dvc remote add -d gsremote gs://mybucket/dvcstore

# Azure Blob Storage
python -m dvc remote add -d azureremote azure://mycontainer/dvcstore
```

### Demo: Data Reproducibility
```bash
# Delete local data
del data\bank_churn.csv

# Restore from DVC
python -m dvc pull

# Verify restoration
dir data
# ✅ bank_churn.csv is back!
```

---

## 🔄 ML Pipeline (ZenML)

### Pipeline Architecture
```python
@pipeline
def training_pipeline(n_estimators: int, max_depth: int):
    """
    Complete training pipeline with 4 steps:
    1. load_data: Load and split dataset
    2. train_model: Train Random Forest
    3. evaluate_model: Calculate metrics
    4. export_model: Save model and metrics
    """
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train, n_estimators, max_depth)
    metrics = evaluate_model(model, X_test, y_test)
    model_path = export_model(model, metrics)
```

### Run Pipeline Variations
```bash
# Baseline
python -c "from zenml_pipeline import training_pipeline; training_pipeline(n_estimators=100, max_depth=10)"

# More trees
python -c "from zenml_pipeline import training_pipeline; training_pipeline(n_estimators=200, max_depth=15)"

# Simpler model
python -c "from zenml_pipeline import training_pipeline; training_pipeline(n_estimators=50, max_depth=5)"
```

### View Pipeline Runs
```bash
# List all runs
C:\Users\YOUR_USERNAME\AppData\Roaming\Python\Python311\Scripts\zenml.exe pipeline runs list

# Expected output:
# ID    INDEX   RUN NAME                              PIPELINE              STATUS
# ────────────────────────────────────────────────────────────────────────────────
# xxx   1       training_pipeline-2026_01_09-...      training_pipeline     ✅
# xxx   2       training_pipeline-2026_01_09-...      training_pipeline     ✅
# xxx   3       training_pipeline-2026_01_09-...      training_pipeline     ✅
```

---

## 🎯 Hyperparameter Optimization (Optuna)

### Optimization Process

Optuna automatically searches for the best hyperparameters:
```python
# Parameters optimized:
- n_estimators: [50, 200]
- max_depth: [5, 20]
- min_samples_split: [2, 10]
- min_samples_leaf: [1, 5]

# Objective: Maximize F1 Score
```

### Run Optimization
```bash
python optuna_optimization.py
```

### Results
```json
{
  "best_params": {
    "n_estimators": 90,
    "max_depth": 14,
    "min_samples_split": 7,
    "min_samples_leaf": 1
  },
  "best_f1_score": 0.3661,
  "best_accuracy": 0.7645,
  "n_trials": 10
}
```

**Improvement**: +11% F1 Score (0.3290 → 0.3661)

---

## 🐳 Docker Deployment

### Docker Compose Stack
```yaml
services:
  api:                    # FastAPI application
    - Port: 8000
    - Model: /app/model/churn_model.pkl
    
  mlflow:                 # MLflow tracking server
    - Port: 5000
    - Storage: ./mlruns
```

### Start Services
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Test Deployed Services
```bash
# Test API
curl http://localhost:8000/health

# Open UIs
# API Docs: http://localhost:8000/docs
# MLflow: http://localhost:5000
```

### Build Individual Image
```bash
# Build image
docker build -t bank-churn-api:v1 .

# Run container
docker run -p 8000:8000 bank-churn-api:v1

# Push to registry
docker tag bank-churn-api:v1 your-registry/bank-churn-api:v1
docker push your-registry/bank-churn-api:v1
```

---

## 🔄 CI/CD Pipeline

### GitHub Actions Workflow

Automated pipeline triggered on every push to `main`:
```yaml
jobs:
  test:
    - Install dependencies
    - Run pytest tests
    - Check code coverage
    
  build-and-deploy:
    - Login to Azure
    - Build Docker image
    - Push to Azure Container Registry
    - Deploy to Azure Container Apps
    - Verify deployment
```

### Pipeline Stages

1. **Test** (2-3 min)
   - Unit tests
   - Integration tests
   - Code coverage report

2. **Build** (3-5 min)
   - Docker image build
   - Tag with commit SHA
   - Push to ACR

3. **Deploy** (2-3 min)
   - Update Container App
   - Health check verification
   - Rollback on failure

### View Pipeline Status
```
https://github.com/arijebouraoui/bank-churn-mlops/actions
```

---

## 📚 API Documentation

### Production URL
```
https://bank-churn.victoriousmoss-65485a03.francecentral.azurecontainerapps.io
```

### Endpoints

#### GET `/health`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

#### POST `/predict`
Single customer churn prediction

**Request:**
```json
{
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
```

**Response:**
```json
{
  "churn_probability": 0.0036,
  "prediction": 0,
  "risk_level": "Low"
}
```

#### POST `/predict/batch`
Batch predictions for multiple customers

**Request:**
```json
{
  "customers": [
    { /* customer 1 data */ },
    { /* customer 2 data */ }
  ]
}
```

#### GET `/docs`
Interactive Swagger UI documentation

#### GET `/redoc`
ReDoc API documentation

---

## 🔖 Model Versioning

### Version Tags

- **v1**: Baseline model (n_estimators=100, max_depth=10)
- **v2**: Optuna optimized (n_estimators=90, max_depth=14)

### Deployment Demo
```bash
# Run version deployment demo
python deploy_versions.py
```

**Demo Process:**
1. ✅ Test v1 (baseline)
2. ✅ Deploy v2 (optimized)
3. ✅ Test v2
4. ✅ Rollback to v1
5. ✅ Test rollback

**Expected Output:**
```
======================================================================
📊 SUMMARY
======================================================================

v1 (Baseline):  Churn Prob = 0.0036
v2 (Optimized): Churn Prob = 0.0038
v1 (Rollback):  Churn Prob = 0.0036

✅ Demonstration Complete!
======================================================================
```

### Manual Version Switch
```bash
# Deploy v2
copy model\optuna_best_model.pkl model\churn_model.pkl
docker-compose restart api

# Rollback to v1
copy model\churn_model_backup.pkl model\churn_model.pkl
docker-compose restart api
```

---

## 📊 Monitoring

### Azure Application Insights

**Connection String:** Configured via environment variable `APPLICATIONINSIGHTS_CONNECTION_STRING`

**Tracked Events:**
- API requests (latency, status codes)
- Predictions (probability, risk level)
- Errors and exceptions
- Custom metrics

### View Logs
```bash
# Via Azure Portal
1. Go to Application Insights resource
2. Click "Logs"
3. Run query:
   traces
   | where message contains "prediction"
   | project timestamp, message, customDimensions
   | order by timestamp desc
```

### Key Metrics

- **Request Rate**: Requests per minute
- **Response Time**: P50, P95, P99 latency
- **Error Rate**: Failed requests percentage
- **Churn Predictions**: Distribution of risk levels

---

## 📈 Results

### Model Performance

| Model | Accuracy | F1 Score | Parameters |
|-------|----------|----------|------------|
| Baseline (v1) | 76.55% | 0.3290 | n_estimators=100, max_depth=10 |
| Optimized (v2) | 76.45% | 0.3661 | n_estimators=90, max_depth=14 |
| **Improvement** | -0.1% | **+11.3%** | Optuna optimization |

### Pipeline Execution

| Step | Avg Time | Description |
|------|----------|-------------|
| load_data | ~33s | Load and split dataset |
| train_model | ~9s | Train Random Forest |
| evaluate_model | ~0.7s | Calculate metrics |
| export_model | ~3s | Save model and metrics |
| **Total** | **~46s** | Complete pipeline |

### Optuna Optimization

- **Trials**: 10
- **Best Trial**: #6
- **Search Space**: 4 hyperparameters
- **Execution Time**: ~3 minutes
- **Improvement**: +11% F1 Score

### CI/CD Performance

- **Average Pipeline Duration**: 8-10 minutes
- **Success Rate**: 95%+
- **Deployment Frequency**: On every push to main
- **Rollback Time**: <2 minutes

---

## 🛠️ Troubleshooting

### Common Issues

#### DVC Pull Fails
```bash
# Check remote configuration
python -m dvc remote list

# Reconfigure remote
python -m dvc remote add -d myremote C:\dvc-storage --force
```

#### ZenML Command Not Found
```bash
# Use full path
C:\Users\YOUR_USERNAME\AppData\Roaming\Python\Python311\Scripts\zenml.exe --help

# Or add to PATH
set PATH=%PATH%;C:\Users\YOUR_USERNAME\AppData\Roaming\Python\Python311\Scripts
```

#### Docker Container Won't Start
```bash
# Check logs
docker-compose logs api

# Rebuild image
docker-compose build --no-cache
docker-compose up -d
```

#### API Returns 503
```bash
# Check if model exists
dir model\churn_model.pkl

# Verify container is running
docker ps

# Restart container
docker-compose restart api
```

---

## 🤝 Contributing

### Development Setup
```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v --cov=app

# Lint code
flake8 app/
black app/

# Type checking
mypy app/
```

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/your-feature

# Make changes and commit
git add .
git commit -m "feat: add new feature"

# Push and create PR
git push origin feature/your-feature
```

### Coding Standards

- Follow PEP 8
- Add type hints
- Write docstrings
- Include tests for new features
- Update README for new functionality

---

## 📄 License

This project is licensed under the MIT License.

---

## 👥 Authors

- **Arije Bouraoui** - [GitHub](https://github.com/arijebouraoui)

---

## 🙏 Acknowledgments

- **Workshop MLOps avec Azure** - [nevermind78](https://nevermind78.github.io/mlops-workshop-docs/)
- **Bank Churn Dataset** - Synthetic dataset generated for educational purposes
- **MLOps Community** - For tools and best practices

---

## 📞 Contact

- **Email**: arije.bouraoui@polytechnicien.tn
- **GitHub**: [@arijebouraoui](https://github.com/arijebouraoui)
- **Project Link**: [bank-churn-mlops](https://github.com/arijebouraoui/bank-churn-mlops)

---

## 🎓 Project Context

This project was developed as part of the **MLOps Mini-Project** for the MLOps 2025-26 course at **Polytechnique Sousse** under the supervision of **Dr. Salah Gontara**.

**Objectives Achieved:**
- ✅ Complete MLOps workflow implementation
- ✅ Data versioning with DVC
- ✅ Experiment tracking with MLflow
- ✅ Pipeline orchestration with ZenML
- ✅ Hyperparameter optimization with Optuna
- ✅ Containerization with Docker
- ✅ CI/CD automation with GitHub Actions
- ✅ Production deployment on Azure
- ✅ Monitoring and observability
- ✅ Model versioning and rollback

---

**Made with ❤️ using MLOps best practices**