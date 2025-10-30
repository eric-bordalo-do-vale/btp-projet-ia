# ⚡ COMMANDES RAPIDES - La Tour

Aide-mémoire des commandes les plus utiles pour le projet.

---

## 🚀 Installation (première fois)

```bash
# 1. Créer les fichiers templates et CSS
python create_files.py

# 2. Installation automatique
setup.bat

# OU installation manuelle :
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
flask init-db
flask seed-db
```

---

## 💻 Commandes quotidiennes

### Lancer l'application
```bash
# Activer l'environnement virtuel
venv\Scripts\activate

# Lancer Flask
python app.py

# Ouvrir : http://127.0.0.1:5000
```

### Arrêter l'application
```
Ctrl + C dans le terminal
```

---

## 💾 Base de données

```bash
# Initialiser la base de données (première fois)
flask init-db

# Ajouter des données de test
flask seed-db

# Ouvrir le shell Flask (pour tester des requêtes)
flask shell

# Dans le shell :
>>> from app import db, User, RendezVous
>>> User.query.all()
>>> exit()
```

### Réinitialiser complètement la BDD
```bash
# Windows
del latour.db
flask init-db
flask seed-db

# Linux/Mac
rm latour.db
flask init-db
flask seed-db
```

---

## 🐍 Python

### Environnement virtuel
```bash
# Créer
python -m venv venv

# Activer (Windows)
venv\Scripts\activate

# Activer (Linux/Mac)
source venv/bin/activate

# Désactiver
deactivate
```

### Packages
```bash
# Installer les dépendances
pip install -r requirements.txt

# Installer un package
pip install nom-du-package

# Mettre à jour requirements.txt
pip freeze > requirements.txt

# Voir les packages installés
pip list
```

---

## 🌿 Git

### Setup initial
```bash
# Initialiser Git (si pas déjà fait)
git init

# Premier commit
git add .
git commit -m "Initial commit: Setup La Tour"

# Lier au repository distant
git remote add origin https://github.com/username/btp-projet-ia.git
git push -u origin main
```

### Workflow quotidien
```bash
# Voir l'état
git status

# Créer une branche
git checkout -b feature/nom-feature

# Ajouter des fichiers
git add .

# Commit
git commit -m "feat: Description du changement"

# Pousser
git push origin feature/nom-feature

# Mettre à jour depuis main
git checkout main
git pull
git checkout feature/nom-feature
git merge main
```

### Commandes utiles
```bash
# Voir l'historique
git log --oneline

# Voir les différences
git diff

# Annuler des modifications
git checkout -- fichier.py

# Voir les branches
git branch -a

# Supprimer une branche
git branch -d nom-branche
```

---

## 🧪 Tests & Vérification

```bash
# Vérifier l'installation
python verifier_installation.py

# Tester l'import de l'app
python -c "from app import app; print('OK')"

# Vérifier la syntaxe Python
python -m py_compile app.py
```

---

## 📂 Fichiers

### Voir la structure
```bash
# Windows
tree /F

# Linux/Mac
tree
```

### Créer des dossiers
```bash
# Windows
mkdir nom_dossier

# Créer plusieurs niveaux
mkdir templates\partials
```

---

## 🔍 Recherche

### Trouver du texte dans les fichiers
```bash
# Windows (PowerShell)
Select-String -Path *.py -Pattern "def"

# Linux/Mac
grep -r "def" *.py
```

---

## 📝 Édition

### Ouvrir dans VS Code
```bash
# Ouvrir le projet
code .

# Ouvrir un fichier
code app.py
```

---

## 🔥 Raccourcis utiles

### Terminal
- `Ctrl + C` - Arrêter un processus
- `Ctrl + L` - Effacer l'écran (ou `clear`)
- `↑` / `↓` - Naviguer dans l'historique
- `Tab` - Auto-complétion

### VS Code
- `Ctrl + `` ` - Ouvrir/fermer le terminal
- `Ctrl + P` - Rechercher un fichier
- `Ctrl + Shift + F` - Rechercher dans tous les fichiers
- `Ctrl + /` - Commenter/décommenter
- `Alt + ↑/↓` - Déplacer une ligne

---

## 🐛 Dépannage

### "Python n'est pas reconnu"
```bash
# Ajouter Python au PATH ou utiliser le chemin complet
C:\Python39\python.exe app.py
```

### "Module not found"
```bash
# Activer l'environnement virtuel
venv\Scripts\activate

# Réinstaller les dépendances
pip install -r requirements.txt
```

### "Port already in use"
```bash
# Trouver le processus sur le port 5000 (Windows)
netstat -ano | findstr :5000

# Tuer le processus (remplacer PID par le numéro)
taskkill /PID <PID> /F

# OU changer le port dans app.py
app.run(port=5001)
```

### "No such table"
```bash
# Réinitialiser la BDD
flask init-db
flask seed-db
```

---

## 📊 Infos système

```bash
# Version Python
python --version

# Version pip
pip --version

# Infos Git
git --version

# Variables d'environnement (Windows)
set

# Variables d'environnement (Linux/Mac)
env
```

---

## 🎯 Commandes pour chaque rôle

### Frontend Developer
```bash
# Voir les templates
dir templates

# Éditer le CSS
code static\css\style.css

# Tester une page
# Lancer app.py et ouvrir http://127.0.0.1:5000/mentors
```

### Backend Developer
```bash
# Éditer l'app
code app.py

# Tester dans le shell Flask
flask shell

# Voir les logs
# Lancer app.py et observer le terminal
```

### QA/Documentation
```bash
# Vérifier l'installation
python verifier_installation.py

# Voir les TODO
code TODO.md

# Voir le statut Git
git status
```

---

## 💡 Tips

### Créer un alias (raccourci)
```bash
# Windows (PowerShell)
Set-Alias run python app.py

# Linux/Mac (dans .bashrc ou .zshrc)
alias run="python app.py"
```

### Vérification rapide
```bash
# Tout vérifier en une commande
python verifier_installation.py && python app.py
```

---

## 📚 Aide

```bash
# Aide Flask
flask --help

# Aide pip
pip --help

# Aide Git
git --help
```

---

**Gardez ce fichier sous la main pendant le développement ! 📌**

*Pour plus de détails, consultez [INDEX.md](INDEX.md)*
