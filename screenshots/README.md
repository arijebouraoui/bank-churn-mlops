\# Project Screenshots and Evidence



This directory contains visual evidence and screenshots demonstrating all aspects of the MLOps project.



\## Directory Structure

```

screenshots/

├── mlflow/          # MLflow UI screenshots

├── zenml/           # ZenML pipeline execution

├── api/             # API and Swagger documentation

├── deployment/      # Deployment demonstration (v1→v2→rollback)

├── dvc/             # DVC commands and results

├── git/             # Git branches, tags, commits

└── README.md        # This file

```



---



\## Required Screenshots



\### 1. MLflow (screenshots/mlflow/)



\*\*Files needed:\*\*

\- `01\_experiments\_list.png` - List of experiments

\- `02\_runs\_comparison.png` - Comparison of multiple runs

\- `03\_run\_details.png` - Detailed view of a single run

\- `04\_metrics\_plots.png` - Metrics visualization

\- `05\_artifacts.png` - Logged artifacts (confusion matrix, feature importance)

\- `06\_model\_registry.png` - Model registry (bank-churn-classifier v1, v2)



\*\*How to capture:\*\*

1\. Open http://localhost:5000

2\. Navigate through experiments

3\. Click on "bank-churn-prediction" experiment

4\. Compare multiple runs

5\. View artifacts and metrics



---



\### 2. ZenML (screenshots/zenml/)



\*\*Files needed:\*\*

\- `01\_pipeline\_execution.png` - Terminal output of pipeline run

\- `02\_pipeline\_steps.png` - Pipeline steps (load\_data, train\_model, evaluate, export)

\- `03\_config.png` - .zen/config.yaml contents



\*\*How to capture:\*\*

```bash

\# Run pipeline

python zenml\_pipeline.py



\# Capture the output

```



---



\### 3. API (screenshots/api/)



\*\*Files needed:\*\*

\- `01\_swagger\_ui.png` - Swagger documentation at http://localhost:8000/docs

\- `02\_predict\_endpoint.png` - /predict endpoint details

\- `03\_health\_endpoint.png` - /health endpoint

\- `04\_prediction\_example.png` - Example prediction request/response



\*\*How to capture:\*\*

1\. Open http://localhost:8000/docs

2\. Test /predict endpoint with sample data

3\. Capture request and response



\*\*Sample request:\*\*

```json

{

&nbsp; "CreditScore": 650,

&nbsp; "Age": 35,

&nbsp; "Tenure": 5,

&nbsp; "Balance": 50000,

&nbsp; "NumOfProducts": 2,

&nbsp; "HasCrCard": 1,

&nbsp; "IsActiveMember": 1,

&nbsp; "EstimatedSalary": 60000

}

```



---



\### 4. Deployment (screenshots/deployment/)



\*\*Files needed:\*\*

\- `01\_v1\_prediction.png` - Prediction with baseline model (v1)

\- `02\_v2\_deployment.png` - Deployment of optimized model (v2)

\- `03\_v2\_prediction.png` - Prediction with optimized model

\- `04\_rollback.png` - Rollback to v1

\- `05\_rollback\_prediction.png` - Prediction after rollback

\- `06\_comparison\_summary.png` - All three predictions compared



\*\*How to capture:\*\*

```bash

\# Run automated script

test\_deployment\_demo.bat



\# Capture output at each step

```



---



\### 5. DVC (screenshots/dvc/)



\*\*Files needed:\*\*

\- `01\_dvc\_version.png` - `dvc version` output

\- `02\_dvc\_remote.png` - `dvc remote list` output

\- `03\_dvc\_status.png` - `dvc status` output

\- `04\_dvc\_file.png` - Contents of data/bank\_churn.csv.dvc

\- `05\_dvc\_cache.png` - DVC cache structure



\*\*Commands to capture:\*\*

```bash

dvc version

dvc remote list

dvc status

type data\\bank\_churn.csv.dvc

dir .dvc\\cache\\files\\md5\\00

```



---



\### 6. Git (screenshots/git/)



\*\*Files needed:\*\*

\- `01\_branches.png` - `git branch -a` output

\- `02\_tags.png` - `git tag -l` output

\- `03\_commit\_history.png` - Recent commits

\- `04\_github\_repo.png` - GitHub repository overview



\*\*Commands to capture:\*\*

```bash

git branch -a

git tag -l

git log --oneline -10

```



---



\## Screenshot Guidelines



\### Quality Standards

\- ✅ High resolution (at least 1920x1080)

\- ✅ Clear, readable text

\- ✅ Entire relevant window visible

\- ✅ No sensitive information (API keys, passwords)

\- ✅ Consistent naming convention



\### Naming Convention

```

<category>/<number>\_<description>.png



Examples:

mlflow/01\_experiments\_list.png

api/02\_predict\_endpoint.png

deployment/03\_v2\_prediction.png

```



\### Tools

\- Windows: Snipping Tool, Win+Shift+S

\- Third-party: Greenshot, ShareX

\- Browser: Built-in screenshot tools



---



\## Verification Checklist



Before submitting, ensure you have:



\- \[ ] At least 6 MLflow screenshots

\- \[ ] At least 3 ZenML screenshots

\- \[ ] At least 4 API screenshots

\- \[ ] At least 6 deployment screenshots

\- \[ ] At least 5 DVC screenshots

\- \[ ] At least 4 Git screenshots



\*\*Total minimum: 28 screenshots\*\*



---



\## Submission



These screenshots serve as visual proof of:

1\. ✅ Working MLflow experiment tracking

2\. ✅ Functional ZenML pipeline

3\. ✅ Operational API

4\. ✅ Successful deployment workflow

5\. ✅ DVC data versioning

6\. ✅ Proper Git usage



All screenshots should be committed to the repository:

```bash

git add screenshots/

git commit -m "Add project screenshots and visual evidence"

git push origin main

```



---



\*\*Last Updated:\*\* January 10, 2026  

\*\*Project:\*\* Bank Churn MLOps

