# ⚡ Guide HTMX pour La Tour

HTMX est déjà intégré dans votre projet ! Ce guide vous montre comment l'utiliser efficacement.

---

## 📚 Bases de HTMX

HTMX permet de créer des interfaces dynamiques directement dans le HTML, sans écrire de JavaScript.

### Attributs principaux

| Attribut | Rôle | Exemple |
|----------|------|---------|
| `hx-get` | Requête GET | `<div hx-get="/api/data">` |
| `hx-post` | Requête POST | `<form hx-post="/submit">` |
| `hx-target` | Où afficher le résultat | `hx-target="#results"` |
| `hx-swap` | Comment remplacer | `hx-swap="innerHTML"` |
| `hx-trigger` | Quand déclencher | `hx-trigger="click"` |

---

## 🎯 Exemples pratiques pour La Tour

### 1. Filtrer les mentors sans rechargement

**templates/mentors.html** (déjà implémenté)
```html
<form hx-get="/mentors" 
      hx-target="#mentors-list" 
      hx-trigger="change">
    <select name="specialisation">
        <option value="">Toutes les spécialisations</option>
        <option value="web">Web</option>
        <option value="data">Data</option>
    </select>
</form>

<div id="mentors-list">
    <!-- Les résultats s'afficheront ici -->
</div>
```

**Comment ça marche ?**
- `hx-get="/mentors"` : Envoie une requête GET à /mentors
- `hx-target="#mentors-list"` : Met le résultat dans la div #mentors-list
- `hx-trigger="change"` : Se déclenche quand on change la sélection

---

### 2. Chatbot avec envoi de message

**templates/chatbot.html** (déjà implémenté)
```html
<div id="chat-messages">
    <!-- Messages ici -->
</div>

<form hx-post="/api/chat"
      hx-target="#chat-messages"
      hx-swap="beforeend"
      hx-on::after-request="this.reset()">
    <input type="text" name="message" placeholder="Votre question...">
    <button type="submit">Envoyer</button>
</form>
```

**Backend (app.py)**
```python
@app.route('/api/chat', methods=['POST'])
def chat_api():
    message = request.form.get('message')
    reponse = "Réponse du bot..."
    
    # Retourner du HTML qui sera ajouté au chat
    return f'''
        <div class="message user-message">
            <strong>Vous :</strong>
            <p>{message}</p>
        </div>
        <div class="message bot-message">
            <strong>Bot :</strong>
            <p>{reponse}</p>
        </div>
    '''
```

---

### 3. Notifications en temps réel

**Ajouter dans base.html**
```html
<div id="notifications" 
     hx-get="/api/notifications"
     hx-trigger="every 10s"
     hx-swap="innerHTML">
    <!-- Notifications ici -->
</div>
```

**Backend**
```python
@app.route('/api/notifications')
@login_required
def notifications():
    rdv_attente = RendezVous.query.filter_by(
        mentor_id=current_user.id,
        statut='en_attente'
    ).count()
    
    if rdv_attente > 0:
        return f'''
            <div class="notification warning">
                📅 {rdv_attente} demande(s) de RDV en attente
            </div>
        '''
    return ''
```

---

### 4. Accepter/Refuser un RDV

**templates/mes_rdv.html**
```html
<div class="rdv-card" id="rdv-{{ rdv.id }}">
    <h3>{{ rdv.sujet }}</h3>
    
    {% if rdv.statut == 'en_attente' %}
    <div class="actions">
        <button hx-post="/rdv/accepter/{{ rdv.id }}"
                hx-target="#rdv-{{ rdv.id }}"
                hx-swap="outerHTML"
                class="btn btn-success">
            ✓ Accepter
        </button>
        
        <button hx-post="/rdv/refuser/{{ rdv.id }}"
                hx-target="#rdv-{{ rdv.id }}"
                hx-swap="outerHTML"
                class="btn btn-danger">
            ✗ Refuser
        </button>
    </div>
    {% endif %}
</div>
```

**Backend**
```python
@app.route('/rdv/accepter/<int:id>', methods=['POST'])
@login_required
def accepter_rdv(id):
    rdv = RendezVous.query.get_or_404(id)
    rdv.statut = 'accepte'
    db.session.commit()
    
    # Retourner la carte mise à jour
    return render_template('partials/rdv_card.html', rdv=rdv)

@app.route('/rdv/refuser/<int:id>', methods=['POST'])
@login_required
def refuser_rdv(id):
    rdv = RendezVous.query.get_or_404(id)
    rdv.statut = 'refuse'
    db.session.commit()
    
    return render_template('partials/rdv_card.html', rdv=rdv)
```

**templates/partials/rdv_card.html**
```html
<div class="rdv-card status-{{ rdv.statut }}" id="rdv-{{ rdv.id }}">
    <h3>{{ rdv.sujet }}</h3>
    <span class="badge">{{ rdv.statut }}</span>
    <p>Date : {{ rdv.date_rdv.strftime('%d/%m/%Y à %H:%M') }}</p>
</div>
```

---

### 5. Recherche en direct

**templates/mentors.html**
```html
<input type="text" 
       name="search"
       placeholder="Rechercher un mentor..."
       hx-get="/api/search-mentors"
       hx-trigger="keyup changed delay:500ms"
       hx-target="#search-results">

<div id="search-results">
    <!-- Résultats de recherche -->
</div>
```

**Backend**
```python
@app.route('/api/search-mentors')
def search_mentors():
    query = request.args.get('search', '')
    
    mentors = User.query.filter(
        User.role.in_(['intervenant', 'partenaire']),
        db.or_(
            User.nom.ilike(f'%{query}%'),
            User.prenom.ilike(f'%{query}%'),
            User.specialisation.ilike(f'%{query}%')
        )
    ).all()
    
    return render_template('partials/mentors_list.html', mentors=mentors)
```

---

### 6. Loading states

**Afficher un spinner pendant le chargement**
```html
<button hx-post="/submit"
        hx-indicator="#spinner">
    Envoyer
</button>

<div id="spinner" class="htmx-indicator">
    ⏳ Chargement...
</div>
```

**CSS**
```css
.htmx-indicator {
    display: none;
}

.htmx-request .htmx-indicator {
    display: inline;
}

.htmx-request.htmx-indicator {
    display: inline;
}
```

---

### 7. Confirmation avant action

**Supprimer avec confirmation**
```html
<button hx-delete="/rdv/{{ rdv.id }}"
        hx-confirm="Êtes-vous sûr de vouloir annuler ce rendez-vous ?"
        hx-target="#rdv-{{ rdv.id }}"
        hx-swap="outerHTML swap:1s">
    🗑️ Annuler
</button>
```

---

### 8. Pagination infinie

**Charger plus de résultats**
```html
<div id="mentors-list">
    {% for mentor in mentors %}
        <!-- Carte mentor -->
    {% endfor %}
</div>

{% if has_more %}
<div hx-get="/mentors?page={{ next_page }}"
     hx-trigger="revealed"
     hx-swap="afterend">
    <p>Chargement...</p>
</div>
{% endif %}
```

---

## 🎨 Options de hx-swap

| Valeur | Effet |
|--------|-------|
| `innerHTML` | Remplace le contenu (défaut) |
| `outerHTML` | Remplace l'élément entier |
| `beforebegin` | Insère avant l'élément |
| `afterbegin` | Insère au début du contenu |
| `beforeend` | Insère à la fin du contenu |
| `afterend` | Insère après l'élément |
| `delete` | Supprime l'élément |
| `none` | Ne change rien |

---

## 🎯 Triggers utiles

| Trigger | Quand ça se déclenche |
|---------|----------------------|
| `click` | Au clic (défaut pour button) |
| `change` | Au changement (input, select) |
| `keyup` | À chaque touche relâchée |
| `load` | Au chargement de la page |
| `revealed` | Quand l'élément devient visible |
| `every 5s` | Toutes les 5 secondes |
| `mouseenter` | Survol de la souris |

**Combinaisons**
```html
<!-- Déclencher après 1s de pause -->
hx-trigger="keyup changed delay:1s"

<!-- Déclencher une seule fois -->
hx-trigger="click once"

<!-- Déclencher avec condition -->
hx-trigger="keyup[target.value.length > 3]"
```

---

## 🚀 Fonctionnalités avancées

### Polling (mise à jour automatique)
```html
<!-- Rafraîchir toutes les 30 secondes -->
<div hx-get="/api/status"
     hx-trigger="every 30s"
     hx-target="this">
    Status: En ligne
</div>
```

### WebSockets (temps réel)
```html
<div hx-ws="connect:/ws">
    <form hx-ws="send">
        <input name="message">
    </form>
</div>
```

### Headers personnalisés
```html
<button hx-post="/api/submit"
        hx-headers='{"X-Custom-Header": "value"}'>
    Submit
</button>
```

---

## 🐛 Debugging HTMX

### Activer les logs
```javascript
htmx.logAll();
```

### Chrome DevTools
- Onglet **Network** : voir les requêtes HTMX
- Rechercher "hx-" dans le HTML pour trouver les éléments HTMX

### Extension Chrome
- [HTMX DevTools](https://chrome.google.com/webstore) (si disponible)

---

## 💡 Bonnes pratiques

### 1. Utiliser des partials pour les réponses
```
templates/
├── mentors.html
└── partials/
    ├── mentor_card.html
    └── rdv_card.html
```

### 2. Gérer les erreurs
```python
@app.errorhandler(404)
def not_found(error):
    if request.headers.get('HX-Request'):
        return '<div class="error">Page non trouvée</div>', 404
    return render_template('404.html'), 404
```

### 3. Indicateurs de chargement
```html
<button hx-post="/submit">
    <span class="htmx-indicator">⏳</span>
    Envoyer
</button>
```

### 4. Progressive Enhancement
Toujours avoir un fallback sans HTMX :
```html
<form action="/submit" method="post" hx-post="/submit">
    <!-- Fonctionne avec et sans HTMX -->
</form>
```

---

## 📚 Ressources

- **Documentation** : https://htmx.org/docs/
- **Exemples** : https://htmx.org/examples/
- **Essays** : https://htmx.org/essays/
- **Discord** : Communauté HTMX active

---

## 🎓 Exercices pratiques

### Exercice 1 : Auto-sauvegarde
Créez un formulaire qui sauvegarde automatiquement toutes les 5 secondes.

### Exercice 2 : Recherche live
Ajoutez une recherche qui filtre les mentors en temps réel.

### Exercice 3 : Like/Unlike
Créez un bouton "J'aime" qui change d'état sans rechargement.

---

Avec HTMX, votre application sera rapide et moderne sans JavaScript complexe ! 🚀
