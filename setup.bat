@echo off
echo ========================================
echo Configuration de La Tour
echo ========================================
echo.

REM Créer les dossiers
echo Creation des dossiers...
if not exist "templates" mkdir templates
if not exist "static\css" mkdir static\css
echo [OK] Dossiers crees

REM Copier .env
echo.
echo Configuration de l'environnement...
if not exist ".env" (
    copy ".env.example" ".env"
    echo [OK] Fichier .env cree
) else (
    echo [INFO] Le fichier .env existe deja
)

REM Créer environnement virtuel
echo.
echo Creation de l'environnement virtuel Python...
if not exist "venv" (
    python -m venv venv
    echo [OK] Environnement virtuel cree
) else (
    echo [INFO] L'environnement virtuel existe deja
)

REM Activer l'environnement et installer les dépendances
echo.
echo Installation des dependances...
call venv\Scripts\activate.bat
pip install -r requirements.txt
echo [OK] Dependances installees

REM Initialiser la base de données
echo.
echo Initialisation de la base de donnees...
flask init-db
echo [OK] Base de donnees initialisee

REM Ajouter des données de test
echo.
echo Ajout des donnees de test...
flask seed-db
echo [OK] Donnees de test ajoutees

echo.
echo ========================================
echo Installation terminee avec succes!
echo ========================================
echo.
echo Pour lancer l'application :
echo 1. Activez l'environnement virtuel : venv\Scripts\activate
echo 2. Lancez l'application : python app.py
echo 3. Ouvrez votre navigateur sur : http://127.0.0.1:5000
echo.
pause
