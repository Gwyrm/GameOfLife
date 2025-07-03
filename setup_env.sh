#!/bin/bash

# Script de configuration de l'environnement virtuel Python
# Compatible Mac/Linux

echo "🚀 Configuration de l'environnement pour le Jeu de la Vie de Conway"
echo "================================================="

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 n'est pas installé. Veuillez l'installer avant de continuer."
    exit 1
fi

echo "✅ Python3 détecté: $(python3 --version)"

# Nom de l'environnement virtuel
VENV_NAME="venv"

# Créer l'environnement virtuel s'il n'existe pas
if [ ! -d "$VENV_NAME" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv $VENV_NAME
    echo "✅ Environnement virtuel créé avec succès"
else
    echo "📦 Environnement virtuel existant détecté"
fi

# Activer l'environnement virtuel
echo "🔄 Activation de l'environnement virtuel..."
source $VENV_NAME/bin/activate

# Vérifier que l'environnement est activé
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "✅ Environnement virtuel activé: $VIRTUAL_ENV"
else
    echo "❌ Erreur lors de l'activation de l'environnement virtuel"
    exit 1
fi

# Mettre à jour pip
echo "🔧 Mise à jour de pip..."
pip install --upgrade pip

# Installer les dépendances depuis requirements.txt
if [ -f "requirements.txt" ]; then
    echo "📚 Installation des dépendances..."
    pip install -r requirements.txt
    echo "✅ Dépendances installées avec succès"
else
    echo "⚠️  Aucun fichier requirements.txt trouvé"
fi

echo ""
echo "🎉 Configuration terminée avec succès!"
echo ""
echo "📝 Pour activer l'environnement à l'avenir, utilisez:"
echo "   source $VENV_NAME/bin/activate"
echo ""
echo "📝 Pour désactiver l'environnement, utilisez:"
echo "   deactivate"
echo ""
echo "🎮 Pour lancer le jeu, utilisez:"
echo "   python main.py" 