# 🧠 Guide WebLLM - Intégration Avancée

## Vue d'Ensemble WebLLM

WebLLM est une bibliothèque qui permet d'exécuter des modèles LLM directement dans le navigateur en utilisant WebGPU pour l'accélération GPU.

### Avantages
✅ Pas de serveur requis  
✅ Confidentialité totale (données locales)  
✅ Latence faible (pas d'aller-retour réseau)  
✅ Fonctionne hors ligne après téléchargement  
✅ Gratuit (open-source)  

### Limitations
⚠️ Dépend de WebGPU (navigateurs récents)  
⚠️ Modèles téléchargés (3-7 GB)  
⚠️ Première initialisation lente (30-60s)  
⚠️ Dépend des ressources locales (CPU/GPU/RAM)  

## Configuration Actuelle

### CDN Import
```html
<script src="https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm@0.2.0/lib/index.js"></script>
```

### Modèle Utilisé
```javascript
const modelId = 'TinyLlama-1.1B-Chat-v1.0-q4f32_1';
```

**Caractéristiques**:
- Taille: ~2.5 GB
- Paramètres: 1.1B
- Quantization: q4 (4-bit)
- Format: FP32
- Contexte: 2048 tokens
- Temps/token: ~0.5-2s (selon GPU)

### Initialisation
```javascript
// Dans chatbot.js
chatEngine = new window.MLCEngine();
await chatEngine.reload(modelId, {
    temperature: 0.7,
    top_p: 0.9,
    context_window_size: 2048,
    gpu_memory_utilization: 0.8
});
```

## Modèles Disponibles

### Légers (< 3 GB)
```javascript
// Recommandé pour La Tour
'TinyLlama-1.1B-Chat-v1.0-q4f32_1'

// Autres options
'Mistral-7B-Instruct-v0.1-q4f32_1'     // 7 GB (plus puissant)
'Phi-2-q4f32_1'                         // 2.7 GB (léger)
'RedPajama-INCITE-3B-Chat-v1-q4f32_1'  // 3.5 GB
```

### Moyens (5-10 GB)
```javascript
'Llama-2-7B-Chat-hf-q4f32_1'           // 7.5 GB
'NeuralMonkey-7B-q4f32_1'              // 7.5 GB
'Orca-2-7B-q4f32_1'                    // 7.5 GB
```

### Puissants (15+ GB)
```javascript
'Llama-2-13B-Chat-hf-q4f32_1'          // 15 GB (lent)
'Mistral-7B-Instruct-v0.2-q4f32_1'     // 7 GB (meilleur qualité)
```

## Modifier le Modèle

### Changer le Modèle par Défaut

**Fichier**: `static/js/chatbot.js` ligne ~57

```javascript
// Actuel:
const modelId = 'TinyLlama-1.1B-Chat-v1.0-q4f32_1';

// Changer à:
const modelId = 'Mistral-7B-Instruct-v0.1-q4f32_1';
```

### Permettre aux Utilisateurs de Choisir

```javascript
// Ajouter dans l'interface
const modelSelect = document.createElement('select');
modelSelect.id = 'model-select';
modelSelect.innerHTML = `
    <option value="TinyLlama-1.1B">TinyLlama (Rapide)</option>
    <option value="Mistral-7B">Mistral (Puissant)</option>
    <option value="Phi-2">Phi-2 (Équilibré)</option>
`;

// Dans chatbot.js
async function initChatbotAI(selectedModel) {
    const modelId = `${selectedModel}-q4f32_1`;
    // ... reste du code
}
```

## Paramètres Avancés

### Temperature
```javascript
temperature: 0.0   // Déterministe (toujours même réponse)
temperature: 0.5   // Balanc équilibré
temperature: 0.7   // Recommandé (créatif mais cohérent)
temperature: 1.0   // Très créatif (risque d'incohérence)
```

### Top-P (Nucleus Sampling)
```javascript
top_p: 0.5    // Très restrictif (réponses prévisibles)
top_p: 0.9    // Recommandé (bonne diversité)
top_p: 1.0    // Accepte toutes les probabilités
```

### Max Tokens
```javascript
max_tokens: 256   // Court (questions/réponses rapides)
max_tokens: 512   // Recommandé (équilibre)
max_tokens: 1024  // Long (explications détaillées)
max_tokens: 2048  // Très long (contexte complet)
```

### Context Window
```javascript
context_window_size: 512    // Petite mémoire
context_window_size: 2048   // Recommandé (défaut)
context_window_size: 4096   // Longs contextes
```

## Optimisations

### 1. Cache du Modèle
```javascript
// WebLLM cache automatiquement après premier chargement
// IndexedDB stocke les weights compressés
// Visites suivantes: instantané ✓
```

### 2. Quantization
```javascript
// Modèles q4 (4-bit) recommandés
// 75% plus petits que fp32 (32-bit)
// Sacrifice minimal en qualité

'TinyLlama-1.1B-Chat-v1.0-q4f32_1'   // 2.5 GB
// vs
'TinyLlama-1.1B-Chat-v1.0-fp32'      // 10 GB (non recommandé)
```

### 3. Batch Processing
```javascript
// ❌ Ne pas faire:
for (let msg of messages) {
    const response = await chatEngine.chat.completions.create({...});
}

// ✅ Faire:
const response = await chatEngine.chat.completions.create({
    messages: messages,  // Tout en une requête
    max_tokens: 512
});
```

### 4. Compression de l'Historique
```javascript
// Si historique > 10k tokens:
const recentMessages = chatHistory.slice(-20);  // Garder les 20 derniers
const response = await chatEngine.chat.completions.create({
    messages: recentMessages,  // Plus léger
    max_tokens: 512
});
```

## Cas d'Usage Avancés

### 1. Fine-Tuning pour La Tour
```javascript
// Créer un système prompt spécifique
const systemPrompt = `
Tu es l'assistant IA de La Tour, une plateforme de mentorat.
Tu aides les étudiants en:
- Programmation (Web, Python, JavaScript)
- Cybersécurité
- Data Science
- Développement logiciel

Sois bienveillant, clair, et concis.
Propose des ressources La Tour quand approprié.
`;

// Utiliser dans chaque conversation
messages = [
    { role: "system", content: systemPrompt },
    { role: "user", content: userMessage }
];
```

### 2. Streaming (Réponses au fur et à mesure)
```javascript
// Future implémentation
async function* streamResponse(messages) {
    const stream = await chatEngine.chat.completions.create({
        messages: messages,
        stream: true,  // Streaming mode
        max_tokens: 512
    });
    
    for await (const chunk of stream) {
        yield chunk.choices[0].delta.content;
    }
}

// Usage:
for await (const text of streamResponse(messages)) {
    displayMessage(text, 'assistant');  // Afficher incrémentalement
}
```

### 3. Contrôle du Modèle
```javascript
// Charger/décharger dynamiquement
async function switchModel(newModelId) {
    if (chatEngine) {
        await chatEngine.unload();  // Libérer mémoire
    }
    chatEngine = new window.MLCEngine();
    await chatEngine.reload(newModelId, config);
}
```

### 4. Monitoring & Logs
```javascript
// Tracker performance
const metrics = {
    modelLoadTime: null,
    firstResponseTime: null,
    averageResponseTime: [],
    totalTokensProcessed: 0,
};

// Tracer:
console.log(`Model loaded in ${metrics.modelLoadTime}ms`);
console.log(`Average response: ${avg(metrics.averageResponseTime)}ms`);
console.log(`Total tokens: ${metrics.totalTokensProcessed}`);
```

## Dépannage WebLLM

### WebGPU Non Détecté
```javascript
// Check:
if (!navigator.gpu) {
    console.warn('WebGPU not supported');
    // Fallback à mode simulé
}

// Vérifier dans Chrome:
// chrome://gpu/ → WebGPU Status
```

### Modèle Ne Charge Pas
```javascript
// Check les logs:
console.log('Starting model load...');
try {
    await chatEngine.reload(modelId, config);
    console.log('Model loaded successfully');
} catch (error) {
    console.error('Model load failed:', error.message);
    console.error('Stack:', error.stack);
}
```

### Mémoire Insuffisante
```javascript
// Réduire context:
context_window_size: 1024,  // au lieu de 2048

// Ou réduire max_tokens:
max_tokens: 256,  // au lieu de 512
```

### Latence Élevée
```javascript
// Check GPU:
console.log('GPU:', navigator.gpu?.availableAdapters?.());

// Réduire parallelism:
gpu_memory_utilization: 0.5,  // Moins d'agressif
```

## Migration Future

### Option 1: Backend Serveur
```javascript
// Au lieu d'appeler chatEngine localement:
const response = await fetch('/api/chat', {
    method: 'POST',
    body: JSON.stringify({ message: userMessage })
});
```

### Option 2: Multiple Modèles
```javascript
// Choisir le meilleur selon la question:
if (questionLength > 500) {
    modelId = 'Mistral-7B';  // Plus puissant
} else {
    modelId = 'TinyLlama-1.1B';  // Plus rapide
}
```

### Option 3: Quantization Personnalisé
```javascript
// Compiler des modèles custom pour La Tour
// Nécessite: MLC Machine Learning Compiler
```

## Ressources

### Documentation Officielle
- [WebLLM GitHub](https://github.com/mlc-ai/web-llm)
- [Modèles Disponibles](https://mlc.ai/web-llm)
- [API Reference](https://mlc.ai/web-llm/docs/guide/get_started)

### Modèles
- [Hugging Face](https://huggingface.co/models?task=text-generation)
- [Ollama Models](https://ollama.ai/library)
- [MLC Models](https://github.com/mlc-ai/web-llm/tree/main/src/config)

### Communauté
- [Discord MLC](https://discord.gg/9Xpy2HGBj7)
- [Issues GitHub](https://github.com/mlc-ai/web-llm/issues)
- [Discussions](https://github.com/mlc-ai/web-llm/discussions)

## Performance Benchmarks

### Modèle: TinyLlama-1.1B
| Métrique | Valeur |
|----------|--------|
| Taille | 2.5 GB |
| Load Time | 30-60s (1ère fois) |
| Load Time | <1s (après) |
| Token/sec | 0.5-2 (selon GPU) |
| Qualité Réponse | Moyenne |
| Recommandé Pour | Chatbot général |

### Modèle: Mistral-7B
| Métrique | Valeur |
|----------|--------|
| Taille | 7.5 GB |
| Load Time | 60-120s |
| Token/sec | 0.2-1 |
| Qualité Réponse | Haute |
| Recommandé Pour | Conversations complexes |

---

**Version**: 1.0  
**Dernière mise à jour**: Décembre 2025

Pour plus d'infos, consultez `CHATBOT_IA.md`
