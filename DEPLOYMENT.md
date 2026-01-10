\# 🚀 Deployment \& Scheduling Guide



\## Continuous Training Setup



\### Option 1: GitHub Actions (Automatique)



Le workflow `continuous-training.yml` s'exécute automatiquement:

\- \*\*Schedule\*\*: Chaque dimanche à 2h du matin (UTC)

\- \*\*Manuel\*\*: Peut être déclenché via "Actions" → "Continuous Training" → "Run workflow"



\### Option 2: Cron Job Local/Server



Pour exécuter le retrain sur un serveur:



\#### Linux/Mac:

```bash

\# Ouvrir crontab

crontab -e



\# Ajouter cette ligne (exécute chaque dimanche à 2h)

0 2 \* \* 0 cd /path/to/bank\_churn \&\& /path/to/python retrain\_scheduler.py >> /var/log/retrain.log 2>\&1

```



\#### Windows (Task Scheduler):

1\. Ouvrir "Task Scheduler"

2\. Créer une tâche basique

3\. Déclencheur: Hebdomadaire, dimanche 2h

4\. Action: Lancer `python C:\\path\\to\\bank\_churn\\retrain\_scheduler.py`



\### Option 3: Docker avec Cron



Créer un container avec cron:

```dockerfile

\# Dockerfile.retrain

FROM python:3.11-slim



WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt



COPY . .



\# Install cron

RUN apt-get update \&\& apt-get install -y cron



\# Add cron job

RUN echo "0 2 \* \* 0 cd /app \&\& python retrain\_scheduler.py >> /var/log/cron.log 2>\&1" > /etc/cron.d/retrain-cron

RUN chmod 0644 /etc/cron.d/retrain-cron

RUN crontab /etc/cron.d/retrain-cron



CMD \["cron", "-f"]

```



\## Retrain Conditions



Le script `retrain\_scheduler.py` vérifie automatiquement:



1\. ✅ \*\*Age du modèle\*\*: > 7 jours → retrain

2\. ✅ \*\*Performance\*\*: Accuracy < 70% → retrain

3\. ✅ \*\*F1 Score\*\*: < 0.25 → retrain

4\. ✅ \*\*Modèle manquant\*\*: → retrain



\## Test Retrain Manually

```bash

\# Test si retrain est nécessaire

python retrain\_scheduler.py



\# Forcer un retrain (supprimer le modèle)

del model\\churn\_model.pkl

python retrain\_scheduler.py

```



\## Monitoring



Les logs de retrain sont disponibles:

\- \*\*GitHub Actions\*\*: Dans l'onglet "Actions"

\- \*\*MLflow\*\*: Experiment "bank-churn-retrain"

\- \*\*Fichiers\*\*: `model/current\_metrics.json`

