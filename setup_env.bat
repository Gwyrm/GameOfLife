@echo off
chcp 65001 > nul

REM Script de configuration de l'environnement virtuel Python
REM Compatible Windows

echo 🚀 Configuration de l'environnement pour le Jeu de la Vie de Conway
echo =================================================

REM Vérifier si Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python n'est pas installé ou pas dans le PATH. Veuillez l'installer avant de continuer.
    pause
    exit /b 1
)

echo ✅ Python détecté
python --version

REM Nom de l'environnement virtuel
set VENV_NAME=venv

REM Créer l'environnement virtuel s'il n'existe pas
if not exist "%VENV_NAME%" (
    echo 📦 Création de l'environnement virtuel...
    python -m venv %VENV_NAME%
    echo ✅ Environnement virtuel créé avec succès
) else (
    echo 📦 Environnement virtuel existant détecté
)

REM Activer l'environnement virtuel
echo 🔄 Activation de l'environnement virtuel...
call %VENV_NAME%\Scripts\activate.bat

REM Mettre à jour pip
echo 🔧 Mise à jour de pip...
python -m pip install --upgrade pip

REM Installer les dépendances depuis requirements.txt
if exist "requirements.txt" (
    echo 📚 Installation des dépendances...
    pip install -r requirements.txt
    echo ✅ Dépendances installées avec succès
) else (
    echo ⚠️  Aucun fichier requirements.txt trouvé
)

echo.
echo 🎉 Configuration terminée avec succès!
echo.
echo 📝 Pour activer l'environnement à l'avenir, utilisez:
echo    %VENV_NAME%\Scripts\activate.bat
echo.
echo 📝 Pour désactiver l'environnement, utilisez:
echo    deactivate
echo.
echo 🎮 Pour lancer le jeu, utilisez:
echo    python main.py
echo.
pause 