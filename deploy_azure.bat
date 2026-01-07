@echo off
chcp 65001 >nul
echo ================================================================
echo     DEPLOIEMENT SUR AZURE - BANK CHURN API
echo ================================================================
echo.

REM Variables
set RESOURCE_GROUP=rg-mlops-bank-churn
set LOCATION=swedencentral
set ACR_NAME=acrmlops%USERNAME%%RANDOM%
set CONTAINER_APP_NAME=bank-churn-api
set CONTAINERAPPS_ENV=env-mlops-workshop
set IMAGE_NAME=bank-churn-api
set IMAGE_TAG=v1
set TARGET_PORT=8000

echo [1/9] Verification du Resource Group...
az group create --name %RESOURCE_GROUP% --location %LOCATION%
echo Resource Group OK

echo.
echo [2/9] Installation de l'extension containerapp...
az extension add --name containerapp --upgrade -y

echo.
echo [3/9] Enregistrement des providers...
az provider register --namespace Microsoft.ContainerRegistry
az provider register --namespace Microsoft.App
az provider register --namespace Microsoft.OperationalInsights

echo.
echo [4/9] Creation du Container Registry (ACR)...
echo Nom ACR: %ACR_NAME%
az acr create --resource-group %RESOURCE_GROUP% --name %ACR_NAME% --sku Basic --admin-enabled true --location %LOCATION%

echo Attente de 10 secondes...
timeout /t 10 /nobreak

echo.
echo [5/9] Login au registry...
az acr login --name %ACR_NAME%

echo.
echo [6/9] Build et Push de l'image Docker...
for /f "tokens=*" %%i in ('az acr show --name %ACR_NAME% --query loginServer -o tsv') do set ACR_LOGIN_SERVER=%%i
echo ACR Login Server: %ACR_LOGIN_SERVER%

echo Building Docker image...
docker build -t %IMAGE_NAME%:%IMAGE_TAG% .

echo Tagging images...
docker tag %IMAGE_NAME%:%IMAGE_TAG% %ACR_LOGIN_SERVER%/%IMAGE_NAME%:%IMAGE_TAG%
docker tag %IMAGE_NAME%:%IMAGE_TAG% %ACR_LOGIN_SERVER%/%IMAGE_NAME%:latest

echo Pushing image v1...
docker push %ACR_LOGIN_SERVER%/%IMAGE_NAME%:%IMAGE_TAG%

echo Pushing image latest...
docker push %ACR_LOGIN_SERVER%/%IMAGE_NAME%:latest

echo.
echo [7/9] Creation du Log Analytics Workspace...
set LAW_NAME=law-mlops-%USERNAME%-%RANDOM%
az monitor log-analytics workspace create -g %RESOURCE_GROUP% -n %LAW_NAME% -l %LOCATION%

echo Attente de 15 secondes...
timeout /t 15 /nobreak

for /f "tokens=*" %%i in ('az monitor log-analytics workspace show --resource-group %RESOURCE_GROUP% --workspace-name %LAW_NAME% --query customerId -o tsv') do set LAW_ID=%%i
for /f "tokens=*" %%i in ('az monitor log-analytics workspace get-shared-keys --resource-group %RESOURCE_GROUP% --workspace-name %LAW_NAME% --query primarySharedKey -o tsv') do set LAW_KEY=%%i

echo Log Analytics ID: %LAW_ID%

echo.
echo [8/9] Creation du Container Apps Environment...
az containerapp env create -n %CONTAINERAPPS_ENV% -g %RESOURCE_GROUP% -l %LOCATION% --logs-workspace-id %LAW_ID% --logs-workspace-key %LAW_KEY%

echo.
echo [9/9] Deploiement du Container App...
for /f "tokens=*" %%i in ('az acr credential show -n %ACR_NAME% --query username -o tsv') do set ACR_USER=%%i
for /f "tokens=*" %%i in ('az acr credential show -n %ACR_NAME% --query "passwords[0].value" -o tsv') do set ACR_PASS=%%i

echo ACR Username: %ACR_USER%

az containerapp create -n %CONTAINER_APP_NAME% -g %RESOURCE_GROUP% --environment %CONTAINERAPPS_ENV% --image %ACR_LOGIN_SERVER%/%IMAGE_NAME%:%IMAGE_TAG% --ingress external --target-port %TARGET_PORT% --registry-server %ACR_LOGIN_SERVER% --registry-username %ACR_USER% --registry-password "%ACR_PASS%" --min-replicas 1 --max-replicas 1

echo.
echo ================================================================
echo           DEPLOIEMENT REUSSI!
echo ================================================================

for /f "tokens=*" %%i in ('az containerapp show -n %CONTAINER_APP_NAME% -g %RESOURCE_GROUP% --query properties.configuration.ingress.fqdn -o tsv') do set APP_URL=%%i

echo.
echo URLs de l'application:
echo   API:    https://%APP_URL%
echo   Health: https://%APP_URL%/health
echo   Docs:   https://%APP_URL%/docs
echo.
echo Pour supprimer: az group delete --name %RESOURCE_GROUP% --yes --no-wait
echo ================================================================
pause