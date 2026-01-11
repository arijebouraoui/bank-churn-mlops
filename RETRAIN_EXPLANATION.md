\# Automated Retrain System - Explanation



\## System Overview



The automated retrain system (`retrain\_scheduler.py`) monitors model performance and triggers retraining when needed.



\## Retrain Triggers



Retraining occurs when:

\- \*\*Accuracy < 0.70\*\* (70%)

\- \*\*F1 Score < 0.25\*\*

\- \*\*Model age > 30 days\*\*

\- \*\*Data drift detected\*\*



\## Current Status

```bash

$ python retrain\_scheduler.py

✅ No retrain needed

Current model is performing well and is recent enough

Current metrics:

&nbsp; Accuracy: 0.7655

&nbsp; F1 Score: 0.3290

&nbsp; Last trained: 2026-01-10

```



\*\*Decision:\*\* No retrain required (model performs above thresholds)



\## MLflow Tracking



All retrain attempts (successful or failed) are logged in MLflow experiment "bank-churn-retrain".



\## Production Behavior



In production, this would:

1\. Run on a schedule (e.g., daily cron job)

2\. Send alerts if retrain fails

3\. Automatically deploy new model if performance improves

