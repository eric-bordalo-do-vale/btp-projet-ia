# 🗼 La Tour - Plateforme de Mentorat

Plateforme d'entraide et de mentorat pour les étudiants de La Plateforme (Marseille).

## 🚀 Installation

### 1. Créer un environnement virtuel Python

```bash
python -m venv venv
```

### 2. Activer l'environnement virtuel

**Windows :**
```bash
venv\Scripts\activate
```

**Linux/Mac :**
```bash
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

Copier `.env.example` vers `.env` et modifier si nécessaire :
```bash
copy .env.example .env
```

### 5. Initialiser la base de données

```bash
flask init-db
```

### 6. Ajouter des données de test

```bash
flask seed-db
```

### 7. Lancer l'application

```bash
python app.py
```

L'application sera accessible sur : http://127.0.0.1:5000

## 📁 Structure du projet

```
btp-projet-ia/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── .env                   # Variables d'environnement (à créer)
├── .env.example          # Exemple de configuration
├── templates/            # Templates HTML
│   ├── base.html
│   ├── index.html
│   ├── mentors.html
│   ├── mentor_detail.html
│   ├── demander_rdv.html
│   ├── mes_rdv.html
│   └── chatbot.html
└── static/
    └── css/
        └── style.css     # Styles CSS
```

## 🎯 Fonctionnalités implémentées

### ✅ Version 1 (Base)
- [x] Page d'accueil
- [x] Liste des mentors avec filtres par spécialisation
- [x] Profil détaillé d'un mentor
- [x] Formulaire de demande de rendez-vous
- [x] Page "Mes rendez-vous"
- [x] Interface chatbot (UI prête)
- [x] Base de données SQLite avec modèles User et RendezVous
- [x] Design responsive avec HTMX
- [x] Données de test

## 🔨 À développer (prochaines étapes)

### 📌 Priorité 1 (Jours 1-3)
- [ ] Système d'authentification (inscription/connexion)
- [ ] Gestion des sessions utilisateurs
- [ ] Édition de profil utilisateur
- [ ] Validation et acceptation/refus des rendez-vous

### 📌 Priorité 2 (Jours 4-6)
- [ ] Intégration d'une vraie IA pour le chatbot (OpenAI, Hugging Face, etc.)
- [ ] Système de notifications
- [ ] Recherche avancée de mentors
- [ ] Calendrier interactif pour les disponibilités

### 📌 Priorité 3 (Jours 7-9)
- [ ] Système de notation/avis
- [ ] Messagerie interne
- [ ] Statistiques et tableau de bord
- [ ] Export de données

### 📌 Finitions (Jour 10)
- [ ] Tests finaux
- [ ] Documentation utilisateur
- [ ] Optimisations de performance
- [ ] Préparation de la présentation

## 🛠️ Technologies utilisées

- **Backend** : Python 3.x + Flask
- **Base de données** : SQLite (SQLAlchemy ORM)
- **Frontend** : HTML5/CSS3 + HTMX
- **Design** : CSS personnalisé (responsive)

## 💡 Exemples d'utilisation de HTMX

HTMX est déjà intégré dans le projet. Voici des exemples :

### Filtrage de mentors sans rechargement
```html
<form hx-get="/mentors" hx-target="#mentors-list" hx-trigger="change">
    <select name="specialisation">...</select>
</form>
```

### Envoi de message chatbot
```html
<form hx-post="/api/chat" hx-target="#chat-messages" hx-swap="beforeend">
    <input type="text" name="message">
</form>
```

## 👥 Équipe

4 étudiants de La Plateforme - Marseille

## 📝 Notes pour le développement

### Bonnes pratiques
- Faire des commits réguliers avec des messages clairs
- Tester chaque fonctionnalité avant de passer à la suivante
- Commenter le code complexe
- Utiliser les branches Git pour les nouvelles fonctionnalités

### Conseils HTMX
- `hx-get` / `hx-post` : requêtes AJAX
- `hx-target` : où afficher la réponse
- `hx-swap` : comment remplacer le contenu
- `hx-trigger` : quand déclencher la requête

### Base de données
- Utilisez `flask shell` pour tester des requêtes
- Les migrations peuvent être ajoutées avec Flask-Migrate si nécessaire

## 🐛 Débogage

Si l'application ne démarre pas :
1. Vérifier que l'environnement virtuel est activé
2. Vérifier que toutes les dépendances sont installées
3. Vérifier que la base de données est initialisée
4. Consulter les logs d'erreur dans le terminal

## 📞 Support

En cas de problème, consultez :
- Documentation Flask : https://flask.palletsprojects.com/
- Documentation HTMX : https://htmx.org/docs/
- Documentation SQLAlchemy : https://docs.sqlalchemy.org/

Bon courage pour votre projet ! 🚀
