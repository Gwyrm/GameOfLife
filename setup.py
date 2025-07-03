#!/usr/bin/env python3
"""
Script universel de configuration de l'environnement virtuel Python
Détecte automatiquement le système d'exploitation et lance le script approprié
"""

import os
import sys
import platform
import subprocess

def detect_os():
    """Détecte le système d'exploitation"""
    system = platform.system().lower()
    return system

def run_setup_script():
    """Lance le script de configuration approprié selon l'OS"""
    os_type = detect_os()
    
    print("🔍 Détection du système d'exploitation...")
    print(f"✅ Système détecté: {platform.system()} {platform.release()}")
    print()
    
    if os_type in ['linux', 'darwin']:  # Linux ou macOS
        script_name = "setup_env.sh"
        print(f"🚀 Lancement du script Unix/Mac: {script_name}")
        
        # Rendre le script exécutable
        try:
            os.chmod(script_name, 0o755)
        except OSError:
            pass
        
        # Exécuter le script
        try:
            result = subprocess.run(['bash', script_name], check=True)
            return result.returncode == 0
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de l'exécution du script: {e}")
            return False
        except FileNotFoundError:
            print(f"❌ Script {script_name} non trouvé")
            return False
            
    elif os_type == 'windows':
        script_name = "setup_env.bat"
        print(f"🚀 Lancement du script Windows: {script_name}")
        
        # Exécuter le script batch
        try:
            result = subprocess.run([script_name], shell=True, check=True)
            return result.returncode == 0
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de l'exécution du script: {e}")
            return False
        except FileNotFoundError:
            print(f"❌ Script {script_name} non trouvé")
            return False
    else:
        print(f"❌ Système d'exploitation non supporté: {os_type}")
        print("💡 Systèmes supportés: Windows, macOS, Linux")
        return False

def main():
    """Fonction principale"""
    print("🎮 Configuration automatique de l'environnement - Jeu de la Vie de Conway")
    print("=" * 70)
    print()
    
    success = run_setup_script()
    
    print()
    if success:
        print("🎉 Configuration terminée avec succès!")
        print()
        print("📝 Prochaines étapes:")
        if detect_os() == 'windows':
            print("   1. Pour activer l'environnement: venv\\Scripts\\activate.bat")
        else:
            print("   1. Pour activer l'environnement: source venv/bin/activate")
        print("   2. Pour lancer le jeu: python main.py")
    else:
        print("❌ La configuration a échoué")
        print("💡 Vérifiez que Python est installé et accessible")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 