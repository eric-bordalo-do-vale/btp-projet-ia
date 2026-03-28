# 🚀 Guide de Déploiement - Chatbot IA

## Étapes d'Installation

### 1. Vérifier les Fichiers

```bash
# Vérifier que les fichiers suivants existent:
✓ index.html (modifié)
✓ static/css/style.css (modifié)
✓ static/js/chatbot.js (nouveau)
✓ CHATBOT_IA.md (nouveau)
✓ TESTING_CHATBOT.md (nouveau)
✓ MODIFICATIONS_CHATBOT.md (nouveau)
```

### 2. Vérifier les Modifications HTML

Dans `index.html`, rechercher:

```html
<!-- CDN WebLLM présent -->
<script src="https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm@0.2.0/lib/index.js"></script>

<!-- Widget HTML présent -->
<button id="chatbot-toggle-btn" aria-label="Ouvrir le chatbot"></button>
<div id="chatbot-widget">

<!-- Import chatbot.js -->
<script src="static/js/chatbot.js"></script>
```

### 3. Vérifier les Modifications CSS

Dans `static/css/style.css`, vérifier que les styles du chatbot sont à la fin:

```css
/* Chatbot Widget Styles */
#chatbot-widget {
    position: fixed;
    bottom: 20px;
    right: 20px;
    ...
}
```

### 4. Tester Localement

```bash
# Démarrer un serveur local
python -m http.server 8000

# Ou avec Node.js
npx http-server

# Accéder à: http://localhost:8000
```

### 5. Tests Pré-Déploiement

- [ ] Se connecter
- [ ] Vérifier que le bouton 🤖 apparaît
- [ ] Ouvrir le widget
- [ ] Envoyer un message
- [ ] Recharger la page
- [ ] Vérifier l'historique persiste
- [ ] Accéder à "Chatbot IA" menu
- [ ] Vérifier que le widget disparaît
- [ ] Tester sur mobile
- [ ] Vérifier aucune erreur en console (F12)

## Configuration Server

### Pour Production

#### Option 1: Serveur Node.js
```javascript
// server.js
const express = require('express');
const app = express();

app.use(express.static('./'));
app.listen(3000, () => {
  console.log('Serveur sur http://localhost:3000');
});
```

```bash
npm install express
node server.js
```

#### Option 2: Serveur Python
```bash
# Python 3.x
python -m http.server 8000

# Python 2.x
python -m SimpleHTTPServer 8000
```

#### Option 3: Nginx
```nginx
server {
    listen 80;
    server_name example.com;
    
    location / {
        root /var/www/btp-projet-ia;
        index index.html;
    }
    
    # Cache assets
    location ~* \.(js|css|png|jpg)$ {
        expires 30d;
    }
}
```

### CORS (si API externe future)
```nginx
# Si backend séparé
add_header 'Access-Control-Allow-Origin' '*';
add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
```

## Variables d'Environnement

Aucune configuration requise pour la version initiale (tout local).

Futures améliorations peuvent nécessiter:
```bash
# .env
API_URL=https://api.example.com
ENABLE_BACKEND=false
MODEL_CACHE_PATH=/var/cache/models
```

## Monitoring

### Logs à Vérifier

1. **Console du navigateur (F12)**
   - Pas d'erreurs JavaScript
   - Logs d'initialisation du chatbot

2. **localStorage** (DevTools → Application)
   - Clé: `user` (données utilisateur)
   - Clé: `chatbot_history_*` (historique)

3. **Network** (DevTools → Network)
   - Script WebLLM charge
   - Pas de 404 pour chatbot.js

### Métriques de Performance

```javascript
// Dans Console:
performance.measure('chatbot-init', ...)
console.time('askAI-response')
```

## Troubleshooting

### Le widget n'apparaît pas
```javascript
// Console check:
console.log(document.getElementById('chatbot-widget'));
console.log(document.getElementById('chatbot-toggle-btn'));
```
**Solution**: Vérifier que les utilisateurs sont authentifiés

### Erreur WebLLM CDN
```
Error: Cannot find module '@mlc-ai/web-llm'
```
**Solution**: Vérifier la version CDN (0.2.0+)

### localStorage plein
```
QuotaExceededError: DOM Exception 22
```
**Solution**: Nettoyer l'historique ou augmenter la taille localStorage

### Performance lente
```
First response takes 30+ seconds
```
**Solution**: Normal la première fois (téléchargement modèle). Cache après.

## Rollback

Si problème détecté:

```bash
# Revenir à version sans chatbot
git revert <commit-hash>

# Ou supprimer les fichiers
rm static/js/chatbot.js
# Supprimer les lignes du HTML/CSS
```

## Checklist Final

- [ ] Tous les fichiers présents
- [ ] Pas d'erreurs en console
- [ ] Widget fonctionne
- [ ] Authentification requise
- [ ] Historique persiste
- [ ] Navigation inchangée
- [ ] Tests réussis (voir TESTING_CHATBOT.md)
- [ ] Documentation lisible
- [ ] Performance acceptable
- [ ] Compatible navigateurs (voir CHATBOT_IA.md)

## Support & Maintenance

### Maintenance Hebdomadaire
- [ ] Vérifier logs d'erreurs
- [ ] Tester widget sur différents navigateurs
- [ ] Vérifier performance

### Maintenance Mensuelle
- [ ] Analyser utilisation du chatbot
- [ ] Collecter feedback utilisateurs
- [ ] Planifier améliorations

### Maintenance Annuelle
- [ ] Mettre à jour WebLLM
- [ ] Tester nouveaux modèles
- [ ] Archiver anciennes conversations

## Contacts & Support

Pour questions sur le Chatbot IA:
1. Lire la documentation (CHATBOT_IA.md)
2. Consulter les tests (TESTING_CHATBOT.md)
3. Vérifier les modifications (MODIFICATIONS_CHATBOT.md)
4. Ouvrir une issue si bug trouvé

## Version & Historique

**Version**: 1.0.0  
**Date**: 2025-12-03  
**Status**: Production Ready  

### Roadmap Future
- [ ] 1.1.0: Backend synchronisation
- [ ] 1.2.0: Modèles supplémentaires
- [ ] 1.3.0: Fine-tuning La Tour
- [ ] 2.0.0: Multimodal (images, audio)

---

**Déploiement réussi** ✅

Le Chatbot IA est maintenant disponible pour tous les utilisateurs authentifiés!
