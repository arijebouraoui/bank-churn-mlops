\# Azure Deployment - Production Ready



\*\*Date:\*\* January 11, 2026  

\*\*Status:\*\* ✅ DEPLOYED AND OPERATIONAL



\## Production URL



\*\*API Endpoint:\*\* https://bank-churn.victoriousmoss-65485a03.francecentral.azurecontainerapps.io



\## Verification



\### Health Check

```bash

curl https://bank-churn.victoriousmoss-65485a03.francecentral.azurecontainerapps.io/health

```



\*\*Response:\*\*

```json

{"status":"healthy","model\_loaded":true}

```



✅ \*\*Status:\*\* Operational  

✅ \*\*Model:\*\* Loaded  

✅ \*\*Region:\*\* France Central  

✅ \*\*Service:\*\* Azure Container Apps



\## Endpoints



\- \*\*Swagger UI:\*\* /docs

\- \*\*Health Check:\*\* /health

\- \*\*Prediction:\*\* /predict



\## Azure Configuration



\- \*\*Service:\*\* Azure Container Apps

\- \*\*Region:\*\* France Central

\- \*\*Container:\*\* bank-churn-api

\- \*\*Auto-scaling:\*\* Enabled



\## CI/CD Integration



GitHub Actions automatically deploys to Azure on push to main branch.



---



\*\*This deployment exceeds the cahier des charges requirements!\*\*

