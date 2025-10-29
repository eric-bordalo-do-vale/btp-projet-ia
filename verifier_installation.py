"""
Script de vérification de l'installation de La Tour
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Vérifier la version de Python"""
    print("🐍 Vérification de Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✓ Python {version.major}.{version.minor}.{version.micro} détecté")
        return True
    else:
        print(f"   ✗ Python {version.major}.{version.minor} détecté (version 3.8+ requise)")
        return False

def check_files():
    """Vérifier que tous les fichiers nécessaires existent"""
    print("\n📁 Vérification des fichiers...")
    
    files_to_check = [
        'app.py',
        'requirements.txt',
        '.env.example',
        'templates/base.html',
        'templates/index.html',
        'templates/mentors.html',
        'templates/mentor_detail.html',
        'templates/demander_rdv.html',
        'templates/mes_rdv.html',
        'templates/chatbot.html',
        'static/css/style.css'
    ]
    
    all_ok = True
    for file in files_to_check:
        if os.path.exists(file):
            print(f"   ✓ {file}")
        else:
            print(f"   ✗ {file} manquant")
            all_ok = False
    
    return all_ok

def check_venv():
    """Vérifier si l'environnement virtuel existe"""
    print("\n🔧 Vérification de l'environnement virtuel...")
    
    if os.path.exists('venv') or os.path.exists('.venv'):
        print("   ✓ Environnement virtuel trouvé")
        return True
    else:
        print("   ⚠ Environnement virtuel non trouvé")
        print("   → Créez-le avec: python -m venv venv")
        return False

def check_packages():
    """Vérifier si les packages sont installés"""
    print("\n📦 Vérification des packages...")
    
    required_packages = ['flask', 'flask_sqlalchemy', 'dotenv']
    all_ok = True
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"   ✓ {package}")
        except ImportError:
            print(f"   ✗ {package} non installé")
            all_ok = False
    
    if not all_ok:
        print("   → Installez avec: pip install -r requirements.txt")
    
    return all_ok

def check_database():
    """Vérifier si la base de données existe"""
    print("\n💾 Vérification de la base de données...")
    
    if os.path.exists('latour.db') or os.path.exists('instance/latour.db'):
        print("   ✓ Base de données trouvée")
        return True
    else:
        print("   ⚠ Base de données non trouvée")
        print("   → Initialisez avec: flask init-db")
        return False

def check_env():
    """Vérifier si .env existe"""
    print("\n⚙️  Vérification de la configuration...")
    
    if os.path.exists('.env'):
        print("   ✓ Fichier .env trouvé")
        return True
    else:
        print("   ⚠ Fichier .env non trouvé")
        print("   → Créez-le avec: copy .env.example .env")
        return False

def main():
    print("=" * 50)
    print("🗼 LA TOUR - Vérification de l'installation")
    print("=" * 50)
    
    checks = {
        'Python': check_python_version(),
        'Fichiers': check_files(),
        'Environnement virtuel': check_venv(),
        'Packages': check_packages(),
        'Configuration': check_env(),
        'Base de données': check_database()
    }
    
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ")
    print("=" * 50)
    
    for name, status in checks.items():
        status_icon = "✅" if status else "❌"
        print(f"{status_icon} {name}")
    
    all_good = all(checks.values())
    
    print("\n" + "=" * 50)
    if all_good:
        print("✨ Tout est prêt ! Vous pouvez lancer l'application avec:")
        print("   python app.py")
        print("\nEnsuite, ouvrez votre navigateur sur:")
        print("   http://127.0.0.1:5000")
    else:
        print("⚠️  Il y a des problèmes à résoudre.")
        print("\n📘 Consultez le fichier DEMARRAGE.md pour plus d'aide")
        print("   ou exécutez setup.bat pour une installation automatique")
    print("=" * 50)

if __name__ == '__main__':
    main()
