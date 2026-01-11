\# Project Submission Checklist



\*\*Project:\*\* Bank Churn MLOps  

\*\*Student:\*\* Arije Bouraoui  

\*\*Date:\*\* January 11, 2026  

\*\*Repository:\*\* https://github.com/arijebouraoui/bank-churn-mlops.git



---



\## ✅ Deliverables Checklist



\### 1. Repository \& Code

\- \[x] GitHub repository: https://github.com/arijebouraoui/bank-churn-mlops.git

\- \[x] Clean structure with organized folders

\- \[x] README.md (22 KB) with complete documentation

\- \[x] All source code committed



\### 2. Git Management

\- \[x] Branches: main, dev

\- \[x] Tags: v1, v2

\- \[x] Clean commit history

\- \[x] .gitignore properly configured



\### 3. Docker \& Containerization

\- \[x] Dockerfile

\- \[x] docker-compose.yml (API + MLflow services)

\- \[x] Containers tested and running

\- \[x] Screenshots: docker-compose ps



\### 4. Data Versioning (DVC)

\- \[x] DVC v3.66.1 installed

\- \[x] data/bank\_churn.csv.dvc

\- \[x] Remote: myremote → C:\\dvc-storage

\- \[x] .dvc/config configured

\- \[x] DVC\_PROOF.md documentation

\- \[x] Screenshots: 5 captures in screenshots/dvc/



\### 5. Experiment Tracking (MLflow)

\- \[x] MLflow UI accessible (port 5000)

\- \[x] 2 experiments: bank-churn-prediction, bank-churn-retrain

\- \[x] Multiple runs logged (3+ runs)

\- \[x] Parameters, metrics, artifacts logged

\- \[x] Model versions: v1, v2

\- \[x] Screenshots: 7 captures in screenshots/mlflow/



\### 6. Pipeline (ZenML)

\- \[x] ZenML v0.93.0 installed

\- \[x] zenml\_pipeline.py implemented

\- \[x] Pipeline steps: load\_data → train → eval → export

\- \[x] .zen/config.yaml configured

\- \[x] Multiple executions (cached runs prove this)

\- \[x] ZENML\_PROOF.md documentation

\- \[x] Screenshots: 3 captures in screenshots/zenml/



\### 7. Hyperparameter Optimization (Optuna)

\- \[x] optuna\_optimization.py

\- \[x] 10 trials completed

\- \[x] Best F1 Score: 0.366

\- \[x] model/optuna\_results.json

\- \[x] model/optuna\_best\_model.pkl



\### 8. CI/CD

\- \[x] .gitlab-ci.yml (3,639 bytes)

\- \[x] .github/workflows/ci-cd.yml (2,795 bytes)

\- \[x] .github/workflows/continuous-training.yml (1,564 bytes)

\- \[x] Jobs: test, lint, build, push, CT



\### 9. Deployment

\- \[x] FastAPI application (app/main.py)

\- \[x] API running on port 8000

\- \[x] Swagger UI: /docs

\- \[x] Endpoints: /predict, /health

\- \[x] DEPLOYMENT\_DEMO.md

\- \[x] test\_deployment\_demo.bat

\- \[x] v1 → v2 → rollback demonstrated

\- \[x] Screenshots: 6+ captures in screenshots/deployment/

\- \[x] Screenshots: 4 captures in screenshots/api/



\### 10. Bonus Features

\- \[x] Monitoring: drift\_detect.py

\- \[x] Automated retrain: retrain\_scheduler.py

\- \[x] RETRAIN\_EXPLANATION.md



\### 11. Documentation

\- \[x] README.md - Project overview

\- \[x] DEPLOYMENT.md - Azure deployment guide

\- \[x] DEPLOYMENT\_DEMO.md - Version management demo

\- \[x] DVC\_PROOF.md - Data versioning proof

\- \[x] ZENML\_PROOF.md - Pipeline execution proof

\- \[x] PROJECT\_VALIDATION.md - Complete validation report

\- \[x] MLFLOW\_RUNS\_EXPLANATION.md - Failed runs explanation

\- \[x] RETRAIN\_EXPLANATION.md - Retrain system documentation



\### 12. Screenshots (Visual Evidence)

\- \[x] screenshots/mlflow/ - 7 captures

\- \[x] screenshots/api/ - 4 captures

\- \[x] screenshots/deployment/ - 6+ captures

\- \[x] screenshots/dvc/ - 5 captures

\- \[x] screenshots/git/ - 4 captures

\- \[x] screenshots/zenml/ - 3 captures

\- \[x] screenshots/README.md - Guide for screenshots



---



\## 📊 Completion Summary



| Section | Requirement | Status |

|---------|-------------|--------|

| 3.1 | Use Case, Data \& Model | ✅ 100% |

| 3.2 | Git Management | ✅ 100% |

| 3.3 | Containerization | ✅ 100% |

| 3.4 | Data Versioning (DVC) | ✅ 100% |

| 3.5 | Experiment Tracking (MLflow) | ✅ 100% |

| 3.6 | Pipeline (ZenML) | ✅ 100% |

| 3.7 | Optimization (Optuna) | ✅ 100% |

| 3.8 | CI/CD | ✅ 100% |

| 3.9 | Deployment | ✅ 100% |

| 4.0 | Bonus Features | ✅ 100% |



\*\*Overall Completion: 100%\*\* ✅



---



\## 🎯 Key Achievements



1\. ✅ Complete MLOps workflow from data versioning to deployment

2\. ✅ Reproducible experiments with MLflow tracking

3\. ✅ Automated CI/CD with GitHub Actions \& GitLab CI

4\. ✅ Hyperparameter optimization with Optuna

5\. ✅ Version management with v1 → v2 → rollback demonstration

6\. ✅ Monitoring and automated retraining system

7\. ✅ Comprehensive documentation with 29+ screenshots

8\. ✅ Production-ready containerized deployment



---



\## 📁 Repository Structure

```

bank-churn-mlops/

├── .dvc/                    # DVC configuration

├── .github/workflows/       # GitHub Actions CI/CD

├── .zen/                    # ZenML configuration

├── app/                     # FastAPI application

├── data/                    # Dataset (DVC tracked)

├── model/                   # Trained models

├── mlruns/                  # MLflow experiments

├── screenshots/             # Visual evidence (29+ captures)

│   ├── mlflow/             # 7 captures

│   ├── api/                # 4 captures

│   ├── deployment/         # 6+ captures

│   ├── dvc/                # 5 captures

│   ├── git/                # 4 captures

│   └── zenml/              # 3 captures

├── tests/                   # Unit tests

├── .gitlab-ci.yml          # GitLab CI/CD

├── docker-compose.yml       # Container orchestration

├── Dockerfile              # Container definition

├── PROJECT\_VALIDATION.md    # Complete validation report

└── README.md               # Project documentation

```



---



\## 🚀 Quick Start Commands



\### Clone and Setup

```bash

git clone https://github.com/arijebouraoui/bank-churn-mlops.git

cd bank-churn-mlops

pip install -r requirements.txt

dvc pull

```



\### Run Services

```bash

docker-compose up -d

```



\### Access

\- API: http://localhost:8000/docs

\- MLflow: http://localhost:5000



---



\## 📝 Notes for Reviewers



\- All mandatory requirements from cahier des charges are met

\- Optional CI/CD implemented (both GitLab CI and GitHub Actions)

\- Bonus features (monitoring, retrain) fully implemented

\- 29+ screenshots provide visual evidence of all features

\- Failed MLflow runs demonstrate realistic development process

\- Model Registry visible in runs (v1, v2 tags in Models column)

\- Complete documentation with 8+ markdown files



---



\## ✅ Ready for Submission



All deliverables are present, tested, and documented with visual evidence.



---



