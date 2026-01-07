@echo off
chcp 65001 >nul
color 0A
echo.
echo ================================================================
echo         TEST DE PROGRESSION - WORKSHOP MLOPS
echo ================================================================
echo.

set /a total=0
set /a passed=0

echo ========================================
echo MODULE 1: ENTRAINEMENT DU MODELE
echo ========================================

set /a total+=6

if exist requirements.txt (
    echo [OK] requirements.txt existe
    set /a passed+=1
) else (
    echo [X] requirements.txt manque
)

if exist data\bank_churn.csv (
    echo [OK] data\bank_churn.csv existe
    set /a passed+=1
) else (
    echo [X] data\bank_churn.csv manque
)

if exist model\churn_model.pkl (
    echo [OK] model\churn_model.pkl existe
    set /a passed+=1
) else (
    echo [X] model\churn_model.pkl manque
)

if exist train_model.py (
    echo [OK] train_model.py existe
    set /a passed+=1
) else (
    echo [X] train_model.py manque
)

if exist generate_data.py (
    echo [OK] generate_data.py existe
    set /a passed+=1
) else (
    echo [X] generate_data.py manque
)

if exist mlruns (
    echo [OK] mlruns\ existe
    set /a passed+=1
) else (
    echo [X] mlruns\ manque
)

echo.
echo ========================================
echo MODULE 2: CREATION DE L'API FASTAPI
echo ========================================

set /a total+=5

if exist app\__init__.py (
    echo [OK] app\__init__.py existe
    set /a passed+=1
) else (
    echo [X] app\__init__.py manque
)

if exist app\main.py (
    echo [OK] app\main.py existe
    set /a passed+=1
) else (
    echo [X] app\main.py manque
)

if exist app\models.py (
    echo [OK] app\models.py existe
    set /a passed+=1
) else (
    echo [X] app\models.py manque
)

if exist tests\test_api.py (
    echo [OK] tests\test_api.py existe
    set /a passed+=1
) else (
    echo [X] tests\test_api.py manque
)

if exist tests\__init__.py (
    echo [OK] tests\__init__.py existe
    set /a passed+=1
) else (
    echo [X] tests\__init__.py manque
)

echo.
echo ========================================
echo MODULE 3: CONTENEURISATION DOCKER
echo ========================================

set /a total+=2

if exist Dockerfile (
    echo [OK] Dockerfile existe
    set /a passed+=1
) else (
    echo [X] Dockerfile manque
)

if exist .dockerignore (
    echo [OK] .dockerignore existe
    set /a passed+=1
) else (
    echo [X] .dockerignore manque
)

echo.
echo ========================================
echo MODULE 5: CI/CD GITHUB ACTIONS
echo ========================================

set /a total+=3

if exist .git (
    echo [OK] .git existe (Git initialise)
    set /a passed+=1
) else (
    echo [X] .git manque (Git non initialise)
)

if exist .gitignore (
    echo [OK] .gitignore existe
    set /a passed+=1
) else (
    echo [X] .gitignore manque
)

if exist .github\workflows\ci-cd.yml (
    echo [OK] .github\workflows\ci-cd.yml existe
    set /a passed+=1
) else (
    echo [X] .github\workflows\ci-cd.yml manque
)

echo.
echo ========================================
echo MODULE 6: MONITORING
echo ========================================

set /a total+=2

if exist app\drift_detect.py (
    echo [OK] app\drift_detect.py existe
    set /a passed+=1
) else (
    echo [X] app\drift_detect.py manque
)

if exist drift_data_gen.py (
    echo [OK] drift_data_gen.py existe
    set /a passed+=1
) else (
    echo [X] drift_data_gen.py manque
)

echo.
echo ================================================================
echo                         RESUME FINAL
echo ================================================================

set /a percent=passed*100/total

echo Total: %passed%/%total% checks passes (%percent%%%)
echo.

if %passed% geq 16 (
    echo [SUCCESS] Tous les modules principaux sont completes!
) else if %passed% geq 11 (
    echo [GOOD] La plupart des modules sont completes
) else if %passed% geq 6 (
    echo [PROGRESS] Quelques modules sont completes
) else (
    echo [START] Il reste beaucoup a faire
)

echo.
echo ================================================================
pause