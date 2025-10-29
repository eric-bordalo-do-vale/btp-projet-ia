# 🎉 BIENVENUE SUR LA TOUR !

## ⚡ Commencer en 3 étapes

### 1️⃣ Créer les fichiers (si pas déjà fait)
```bash
python create_files.py
```

### 2️⃣ Installer automatiquement (Windows)
```bash
setup.bat
```

**OU** Installer manuellement :
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
flask init-db
flask seed-db
```

### 3️⃣ Lancer l'application
```bash
python app.py
```

Puis ouvrez : **http://127.0.0.1:5000**

---

## 🧐 Vérifier l'installation

```bash
python verifier_installation.py
```

---

## 📚 Documentation

| Fichier | Description |
|---------|-------------|
| **README.md** | Vue d'ensemble du projet |
| **DEMARRAGE.md** | Guide de démarrage rapide |
| **ROADMAP.md** | Fonctionnalités et planning |
| **EXEMPLES_CODE.md** | Exemples pour futures features |
| **README_PROJET.md** | Documentation complète |

---

## 🗂️ Structure actuelle

```
btp-projet-ia/
│
├── 📄 Fichiers principaux
│   ├── app.py                    # ❤️ Cœur de l'application
│   ├── requirements.txt          # 📦 Dépendances
│   ├── .env.example              # ⚙️ Configuration
│   └── .gitignore               # 🚫 Fichiers à ignorer
│
├── 📁 templates/                 # 🎨 Pages HTML
│   ├── base.html                # Template de base
│   ├── index.html               # Page d'accueil
│   ├── mentors.html             # Liste des mentors
│   ├── mentor_detail.html       # Profil d'un mentor
│   ├── demander_rdv.html        # Formulaire RDV
│   ├── mes_rdv.html             # Mes rendez-vous
│   └── chatbot.html             # Interface chatbot
│
├── 📁 static/
│   └── css/
│       └── style.css            # 💅 Styles CSS
│
├── 📁 Scripts utiles
│   ├── setup.bat                # 🚀 Installation auto (Windows)
│   ├── create_files.py          # 🔧 Créer les fichiers
│   └── verifier_installation.py # ✅ Vérifier l'install
│
└── 📁 Documentation
    ├── README.md                # Vue d'ensemble
    ├── DEMARRAGE.md             # Guide rapide
    ├── ROADMAP.md               # Planning & idées
    ├── EXEMPLES_CODE.md         # Exemples de code
    └── README_PROJET.md         # Doc complète
```

---

## 🎯 Fonctionnalités actuelles

| Feature | Status | Description |
|---------|--------|-------------|
| 🏠 Page d'accueil | ✅ | Présentation du projet |
| 👥 Liste des mentors | ✅ | Avec filtre par spécialisation |
| 👤 Profil mentor | ✅ | Détails d'un mentor |
| 📅 Demander un RDV | ✅ | Formulaire de demande |
| 📋 Mes RDV | ✅ | Liste des rendez-vous |
| 🤖 Interface chatbot | ✅ | Prête pour IA |
| ⚡ HTMX | ✅ | Interactions dynamiques |
| 💾 Base de données | ✅ | SQLite avec SQLAlchemy |
| 📱 Responsive | ✅ | Mobile & desktop |

---

## 🚀 Prochaines étapes

### Jour 1-2 (Vous êtes ici ! 🎯)
- [x] Setup du projet
- [x] Structure de base
- [x] Pages principales
- [ ] **→ Tester l'application**
- [ ] **→ Faire des commits Git**

### Jour 3-4
- [ ] Système de connexion/inscription
- [ ] Gestion des sessions
- [ ] Édition de profil

### Jour 5-6
- [ ] Chatbot IA fonctionnel
- [ ] Acceptation/refus de RDV
- [ ] Notifications basiques

### Jour 7-8
- [ ] Messagerie interne
- [ ] Système de notation
- [ ] Statistiques

### Jour 9-10
- [ ] Tests finaux
- [ ] Optimisations
- [ ] Présentation

---

## 💻 Commandes utiles

### Gérer la base de données
```bash
flask init-db          # Créer les tables
flask seed-db          # Ajouter des données de test
flask shell            # Ouvrir le shell Flask
```

### Développement
```bash
python app.py          # Lancer l'application
python verifier_installation.py  # Vérifier l'install
```

### Git
```bash
git status             # Voir les modifications
git add .              # Ajouter tous les fichiers
git commit -m "message"  # Faire un commit
git push               # Envoyer sur GitHub
```

---

## 🎓 Données de test

Après `flask seed-db`, vous aurez accès à :

| Nom | Email | Rôle | Spécialisation |
|-----|-------|------|----------------|
| Jean Dupont | jean.dupont@laplateforme.io | Intervenant | Web |
| Sophie Martin | sophie.martin@laplateforme.io | Intervenante | Data |
| Pierre Durand | pierre.durand@laplateforme.io | Étudiant | Cyber |
| Marie Leroy | marie.leroy@laplateforme.io | Étudiante | Web |

---

## 🐛 Problèmes courants

### "Python n'est pas reconnu"
→ Installez Python depuis python.org

### "Module not found"
→ Activez l'environnement virtuel : `venv\Scripts\activate`
→ Installez les dépendances : `pip install -r requirements.txt`

### "No such table"
→ Initialisez la BDD : `flask init-db`

### "Port 5000 already in use"
→ Modifiez le port dans app.py : `app.run(port=5001)`

---

## 🤝 Travailler en équipe

### Répartition suggérée

**👤 Personne 1 : Backend & BDD**
- Gestion des modèles
- Routes Flask
- Base de données

**👤 Personne 2 : Frontend & Design**
- Templates HTML
- CSS/Styling
- HTMX

**👤 Personne 3 : Features**
- Authentification
- Chatbot IA
- Notifications

**👤 Personne 4 : Tests & Doc**
- Tests de l'appli
- Documentation
- Débogage

### Workflow Git
```bash
# Créer une branche pour chaque feature
git checkout -b feature-authentification

# Faire des commits réguliers
git commit -m "Ajout du système de login"

# Pousser la branche
git push origin feature-authentification

# Créer une Pull Request sur GitHub
```

---

## 📖 Ressources

### Documentation officielle
- **Flask** : https://flask.palletsprojects.com/
- **HTMX** : https://htmx.org/docs/
- **SQLAlchemy** : https://docs.sqlalchemy.org/
- **Python** : https://docs.python.org/3/

### Tutoriels
- Flask Mega-Tutorial : https://blog.miguelgrinberg.com/
- HTMX Examples : https://htmx.org/examples/
- Python pour débutants : https://python.org/about/gettingstarted/

### Outils
- **VS Code** : Éditeur de code
- **DB Browser for SQLite** : Visualiser la BDD
- **Postman** : Tester les API
- **Git** : Gestion de versions

---

## 🎉 Conseils pour réussir

1. **Testez souvent** : Après chaque modification
2. **Commitez régulièrement** : Petits commits fréquents
3. **Communiquez** : Parlez de ce que vous faites
4. **Documentez** : Commentez votre code
5. **Amusez-vous** : C'est un projet d'apprentissage !

---

## ✨ C'est parti !

Vous avez tout ce qu'il faut pour créer une super plateforme ! 🚀

**Questions ? Consultez la documentation ou créez une issue sur GitHub.**

**Bon développement ! 💪🗼**

---

Made with ❤️ by La Plateforme students
