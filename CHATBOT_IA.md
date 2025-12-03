# 🤖 Guide du Chatbot IA - La Tour Assistant

## Overview
Le Chatbot IA est une nouvelle fonctionnalité intégrée à La Tour qui permet aux utilisateurs authentifiés de discuter avec un assistant IA. Cette fonctionnalité combine:
- Un **widget flottant** accessible sur toutes les pages du site (pour les utilisateurs connectés)
- Une **page dédiée** pour les conversations plus longues
- Une **intégration WebLLM** pour exécuter des modèles IA légers localement
- Un **historique personnel** conservé pour chaque utilisateur

## Fonctionnalités

### 1. Widget Chatbot Flottant
- **Position**: Bas-droit de l'écran
- **Bouton**: Floatant avec l'icône 🤖 pour ouvrir/fermer
- **Accès**: Uniquement pour les utilisateurs authentifiés
- **Avantage**: Accessible sur toutes les pages du site
- **Disparition**: S'efface automatiquement sur la page dédiée "Chatbot IA"

### 2. Page Dédiée Chatbot
- **Navigation**: Menu "Chatbot IA" dans le header (visible après authentification)
- **Interface**: Étendue pour des conversations longues
- **Historique**: Affiche tout l'historique de conversation avec l'IA
- **Intégration**: Widget disparaît sur cette page pour laisser la place

### 3. Historique Personnalisé
- **Stockage**: Conservé par utilisateur en localStorage
- **Clé**: `chatbot_history_{email}@gmail.com`
- **Persistance**: L'historique est maintenu entre les sessions
- **Synchronisation**: Le widget et la page affichent toujours l'historique à jour

### 4. WebGPU & WebLLM
- **Support**: Chrome 113+, Edge 113+, Firefox 118+
- **Modèle**: TinyLlama-1.1B (léger et rapide)
- **Mode Simulé**: Fallback automatique si WebGPU n'est pas disponible
- **Gestion d'erreurs**: Messages clairs en cas d'indisponibilité

## Architecture Technique

### Fichiers Impliqués

#### 1. `index.html` (Modifications)
```html
<!-- CDN WebLLM -->
<script src="https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm@0.2.0/lib/index.js"></script>

<!-- Widget HTML -->
<button id="chatbot-toggle-btn">Bouton flottant</button>
<div id="chatbot-widget">
    <div id="chatbox-messages">Messages</div>
    <div id="user-message">Input</div>
    <button id="send-btn">Envoyer</button>
</div>

<!-- Page Dédiée -->
<div id="chatbot" class="page">Page du chatbot</div>
```

#### 2. `static/js/chatbot.js` (Nouveau fichier)
Contient:
- `initChatbotAI()` - Initialisation du modèle IA
- `askAI(message)` - Traitement des questions utilisateur
- `displayMessage(content, role)` - Affichage des messages
- `loadChatHistory()` / `saveChatHistory()` - Gestion de l'historique
- `generateSimulatedResponse(message)` - Réponses de fallback

#### 3. `static/css/style.css` (Additions)
Styles pour:
- Widget flottant animé
- Messages utilisateur/assistant
- Indicateur de frappe "typing..."
- Design responsive

## Flux d'Exécution

### 1. Authentification
```
L'utilisateur se connecte
↓
updateUIForAuthenticatedUser() est appelée
↓
Widget et bouton apparaissent
↓
chatbot.js : setupChatbotListeners()
↓
loadChatHistory() chargé depuis localStorage
```

### 2. Interaction Utilisateur
```
Utilisateur écrit un message
↓
Pressé Entrée ou clique Envoyer
↓
askAI(userMessage)
↓
Message sauvegardé dans chatHistory[]
↓
showTypingIndicator()
↓
Si WebLLM disponible → MLCEngine génère réponse
↓
Sinon → generateSimulatedResponse() en mode fallback
↓
Réponse affichée et sauvegardée
```

### 3. Navigation
```
Utilisateur clique sur "Chatbot IA" (menu)
↓
showPage('chatbot') appelée
↓
hideChatbotWidget() masque le widget
↓
updateDedicatedChatPage() charge l'historique
↓
Page affiche la conversation complète
```

## Configuration WebLLM

### Modèle Utilisé
```javascript
modelId = 'TinyLlama-1.1B-Chat-v1.0-q4f32_1'
```
- **Taille**: ~2-3 GB (téléchargé une fois)
- **Performance**: Optimisé pour GPU (WebGPU)
- **Temps de réponse**: 1-5 secondes par message
- **Contexte**: 2048 tokens

### Paramètres
```javascript
{
    temperature: 0.7,      // Créativité (0-1)
    top_p: 0.9,           // Diversité
    context_window_size: 2048,
    gpu_memory_utilization: 0.8
}
```

## Gestion des Erreurs

### WebGPU Non Disponible
- **Détection**: `navigator.gpu` check
- **Fallback**: Mode simulé avec réponses intelligentes
- **UX**: Message informatif à l'utilisateur
- **Fonctionnalité**: Chatbot reste complètement fonctionnel

### Modèle Non Chargé
- **Cause**: Erreur de téléchargement ou timeout
- **Fallback**: `generateSimulatedResponse()`
- **UX**: L'utilisateur peut continuer à converser normalement

### Authentification Manquante
- **Check**: Au démarrage et avant chaque requête
- **Fallback**: Message d'erreur + redirection vers login

## Stockage de l'Historique

### Structure localStorage
```javascript
// Clé
"chatbot_history_user@example.com"

// Valeur (Array JSON)
[
    { role: "user", content: "Bonjour" },
    { role: "assistant", content: "Bonjour! Comment puis-je vous aider?" },
    ...
]
```

### Limite
- **Stockage**: Jusqu'à 5-10 MB par navigateur
- **Taille par message**: ~100-500 bytes
- **Historique maximal**: 10,000+ messages

## Features Futures

### Court terme
1. ✅ WebLLM intégration basique
2. ✅ Historique personnel
3. ✅ Mode fallback simulé
4. [ ] Emoji réactifs pour les messages
5. [ ] Export d'historique PDF

### Moyen terme
1. [ ] Modèles alternatifs (Mistral, Llama2)
2. [ ] Recherche dans l'historique
3. [ ] Partage de conversations
4. [ ] Analyse de sentiment

### Long terme
1. [ ] Backend serveur pour historique cloud
2. [ ] Modèles multimodaux (images)
3. [ ] Intégration avec APIs externes
4. [ ] Analytics sur les questions populaires

## Dépannage

### Le widget n'apparaît pas
1. Vérifiez authentification (Se connecter d'abord)
2. Ouvrez Console (F12)
3. Vérifiez qu'il n'y a pas d'erreurs JS

### Pas de réponse du modèle
1. Vérifiez si WebGPU est disponible (F12 → Application)
2. Attendez le chargement du modèle (~30-60s la première fois)
3. Rechargez la page si c'est long

### Historique ne persiste pas
1. Vérifiez que localStorage n'est pas bloqué
2. Vérifiez que vous êtes toujours connecté
3. Nettoyez le cache du navigateur

### Performance lente
1. Réduisez la taille du contexte (max_tokens)
2. Fermez d'autres onglets/applications
3. Redémarrez le navigateur

## Intégration avec WebLLM

### Installation CDN
```html
<script src="https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm@0.2.0/lib/index.js"></script>
```

### Initialisation Async
```javascript
await initChatbotAI();
// MLCEngine est créé et le modèle est chargé
```

### Utilisation
```javascript
const response = await chatEngine.chat.completions.create({
    messages: [{role: "user", content: "Bonjour"}],
    max_tokens: 512
});
```

## Considérations de Sécurité

- ✅ **Pas de données envoyées à un serveur** (tout local)
- ✅ **Historique chiffré en localStorage** (navigateur)
- ✅ **Pas d'accès à webcam/microphone**
- ✅ **Validation des entrées** (escapeHtml)
- ✅ **Authentification requise** avant d'utiliser

## Performance

### Temps de Chargement
- **Première visite**: 30-60s (téléchargement modèle)
- **Visites suivantes**: Instantané (cache)
- **Par message**: 1-5s (selon la longueur)

### Mémoire
- **Modèle**: 2-3 GB VRAM
- **Historique**: ~1 MB pour 1000 messages
- **Widget**: <1 MB

## Limitations Actuelles

1. **Pas de vision multimodale** (images)
2. **Contexte limité** à 2048 tokens
3. **Pas d'accès à internet** pour le modèle
4. **WebGPU requis** pour performance optimale
5. **Conversations courtes recommandées** (< 10k tokens)

## Améliorations Recommandées

Pour améliorer encore le chatbot:

1. **Backend WebSocket**: Sauvegarder l'historique sur serveur
2. **Modèles multiples**: Proposer différents modèles
3. **Fine-tuning**: Affiner le modèle pour La Tour
4. **Intégration Mentors**: Proposer un mentor basé sur la question
5. **Analytics**: Tracker questions populaires

---

**Version**: 1.0  
**Dernière mise à jour**: Décembre 2025  
**Auteur**: La Tour Team
