# 🚀 GUIDE DE DÉMARRAGE RAPIDE - La Tour

## ⚡ Installation automatique (recommandé)

### Windows
1. Double-cliquez sur `setup.bat`
2. Attendez la fin de l'installation
3. Lancez l'application avec `python app.py`

### Alternative : Installation manuelle

```bash
# 1. Créer les dossiers et fichiers
python create_files.py

# 2. Créer l'environnement virtuel
python -m venv venv

# 3. Activer l'environnement virtuel
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Configurer l'environnement
copy .env.example .env

# 6. Initialiser la base de données
flask init-db

# 7. Ajouter des données de test
flask seed-db

# 8. Lancer l'application
python app.py
```

## 🌐 Accéder à l'application

Ouvrez votre navigateur sur : **http://127.0.0.1:5000**

## 📚 Structure des pages

- **/** - Page d'accueil
- **/mentors** - Liste des mentors
- **/mentor/[id]** - Profil d'un mentor
- **/rendez-vous/demander/[id]** - Demander un RDV
- **/mes-rendez-vous** - Voir tous mes RDV
- **/chatbot** - Assistant IA

## 🧪 Données de test

Après `flask seed-db`, vous aurez :
- **Jean Dupont** - Intervenant Web
- **Sophie Martin** - Intervenante Data
- **Pierre Durand** - Étudiant Cyber
- **Marie Leroy** - Étudiante Web (mentor)

## 🛠️ Commandes utiles

```bash
# Réinitialiser la base de données
flask init-db

# Ajouter des données de test
flask seed-db

# Lancer le serveur
python app.py

# Ouvrir le shell Flask (pour tests)
flask shell
```

## 📝 Prochaines étapes

1. **Authentification** : Ajouter un système de login
2. **Chatbot IA** : Intégrer une vraie IA (OpenAI, Hugging Face)
3. **Notifications** : Alertes pour les nouveaux RDV
4. **Recherche avancée** : Filtres multiples
5. **Messagerie** : Chat entre étudiants et mentors

## 🐛 Problèmes fréquents

### "Module not found"
```bash
pip install -r requirements.txt
```

### "No such table"
```bash
flask init-db
```

### "Port already in use"
Modifiez le port dans `app.py` :
```python
app.run(debug=True, port=5001)
```

## 💡 Conseils HTMX

HTMX est déjà intégré ! Exemples :

```html
<!-- Chargement sans reload -->
<div hx-get="/api/mentors" hx-target="#results"></div>

<!-- Formulaire AJAX -->
<form hx-post="/api/chat" hx-target="#messages"></form>

<!-- Auto-refresh -->
<div hx-get="/api/status" hx-trigger="every 5s"></div>
```

## 📖 Documentation

- Flask : https://flask.palletsprojects.com/
- HTMX : https://htmx.org/
- SQLAlchemy : https://docs.sqlalchemy.org/

## ✨ Bon développement !

N'oubliez pas :
- Commits réguliers
- Tests avant chaque feature
- Code propre et commenté
- Amusez-vous ! 🎉
