# 🐛 Bugs Corrigés - La Tour

## Date: 28 octobre 2025

---

## ✅ Corrections apportées

### 1. **Bug de filtre des mentors** (app.py ligne 51)
**Avant:**
```python
query = User.query.filter(User.role.in_(['intervenant', 'etudiant']))
```

**Après:**
```python
query = User.query.filter(User.role == 'intervenant')
```

**Raison:** Les étudiants ne doivent pas apparaître dans la liste des mentors disponibles.

---

### 2. **Incohérence rôle/bio dans seed_db()** (app.py ligne 128)
**Avant:**
```python
User(nom='Leroy', prenom='Marie', email='marie.leroy@laplateforme.io',
     role='etudiant', specialisation='web', bio='Mentor bénévole en React', disponible=True)
```

**Après:**
```python
User(nom='Leroy', prenom='Marie', email='marie.leroy@laplateforme.io',
     role='intervenant', specialisation='web', bio='Mentor bénévole en React', disponible=True)
```

**Raison:** Le rôle 'etudiant' ne correspond pas à la bio "Mentor bénévole".

---

### 3. **ID hardcodé dans demander_rdv()** (app.py ligne 70)
**Avant:**
```python
etudiant_id = 1
nouveau_rdv = RendezVous(
    etudiant_id=etudiant_id,
    ...
)
```

**Après:**
```python
etudiant = User.query.filter_by(role='etudiant').first()
if not etudiant:
    flash('Erreur: Aucun étudiant trouvé...', 'error')
    return redirect(url_for('mentors'))

nouveau_rdv = RendezVous(
    etudiant_id=etudiant.id,
    ...
)
```

**Raison:** Évite les erreurs si l'utilisateur ID=1 n'existe pas.

**Améliorations supplémentaires:**
- ✅ Validation que le mentor existe et est un intervenant
- ✅ Vérification que le mentor est disponible
- ✅ Validation du format de date
- ✅ Vérification que la date est dans le futur
- ✅ Gestion des erreurs avec try/except
- ✅ Rollback de la transaction en cas d'erreur

---

### 4. **ID hardcodé dans mes_rdv()** (app.py ligne 92)
**Avant:**
```python
user_id = 1
rdv_demandes = RendezVous.query.filter_by(etudiant_id=user_id).all()
```

**Après:**
```python
user = User.query.filter_by(role='etudiant').first()
if not user:
    flash('Aucun utilisateur trouvé...', 'error')
    return redirect(url_for('index'))

rdv_demandes = RendezVous.query.filter_by(etudiant_id=user.id).all()
```

**Raison:** Dynamique et sécurisé, évite les erreurs si l'utilisateur n'existe pas.

---

### 5. **Faille XSS dans chat_api()** (app.py ligne 104)
**Avant:**
```python
message = request.json.get('message', '')
reponse = f"... '{message}' ..."
```

**Après:**
```python
from markupsafe import escape

message = request.json.get('message', '').strip()

# Validations
if not message:
    return {'erreur': 'Message vide'}, 400
if len(message) > 500:
    return {'erreur': 'Message trop long'}, 400

message_safe = escape(message)
reponse = f"... '{message_safe}' ..."
```

**Raison:** 
- Prévention XSS avec échappement HTML
- Validation de la présence du message
- Limitation de la taille pour éviter les abus

---

### 6. **Bug HTMX dans mentors.html** (ligne 9)
**Avant:**
```html
<form method="get" hx-get="..." hx-trigger="change">
    <select name="specialisation" id="specialisation">...</select>
    <button type="submit" class="btn">Filtrer</button>
</form>
```

**Après:**
```html
<form hx-get="..." hx-target="#mentors-list" hx-trigger="change from:#specialisation">
    <select name="specialisation" id="specialisation">...</select>
</form>
```

**Raison:** 
- Suppression du conflit entre `method="get"` et `hx-get`
- Utilisation pure de HTMX pour le rechargement partiel
- Suppression du bouton inutile (changement automatique)

---

### 7. **Protection contre les doublons dans seed_db()**
**Ajouté:**
```python
for user in users:
    existing = User.query.filter_by(email=user.email).first()
    if not existing:
        db.session.add(user)
```

**Raison:** Évite les erreurs de contrainte UNIQUE sur l'email lors de l'exécution répétée de `seed_db`.

---

## 📋 Résumé des améliorations

### Sécurité
- ✅ Protection XSS dans l'API chat
- ✅ Validation des entrées utilisateur
- ✅ Échappement HTML avec markupsafe

### Robustesse
- ✅ Gestion des erreurs avec try/except
- ✅ Validation des dates et formats
- ✅ Vérifications de l'existence des entités
- ✅ Messages d'erreur clairs pour l'utilisateur

### Logique métier
- ✅ Seuls les intervenants apparaissent comme mentors
- ✅ Vérification de la disponibilité des mentors
- ✅ Cohérence des données de test
- ✅ Protection contre les doublons

### UX/UI
- ✅ HTMX pur pour le filtrage dynamique
- ✅ Messages flash informatifs
- ✅ Redirection appropriée en cas d'erreur

---

## 🚀 Pour tester les corrections

```bash
# 1. Réinitialiser la base de données
flask init-db

# 2. Ajouter les données de test
flask seed-db

# 3. Lancer l'application
python app.py
```

## 📝 Notes importantes

⚠️ **Authentification:** Les fonctions utilisent toujours un système d'authentification simulé. Pour la production, il faudra implémenter:
- Flask-Login pour la gestion des sessions
- Hachage des mots de passe
- Système de rôles complet

⚠️ **MarkupSafe:** Déjà inclus avec Flask, pas besoin de l'installer séparément.
