# 🧪 Guide de Test - Chatbot IA

## Scénarios de Test

### 1. ✅ Authentification & Affichage du Widget

**Étapes**:
1. Ouvrir le site sans être connecté
2. Vérifier que le bouton flottant `🤖` n'est PAS visible
3. Vérifier que l'option menu "Chatbot IA" n'est PAS visible

**Résultat attendu**: ✅ Widget caché, menu caché

---

**Étapes**:
1. Se connecter avec: `latour@laplateforme.io` / `1234`
2. Observer l'apparition du bouton flottant bas-droit
3. Vérifier que le menu "Chatbot IA" est maintenant visible

**Résultat attendu**: ✅ Widget visible, menu visible, animations fluides

---

### 2. ✅ Interaction Widget Flottant

**Étapes**:
1. Cliquer sur le bouton `🤖` flottant
2. Vérifier que le widget s'ouvre avec animation
3. Observer le contenu: Header + Messages + Input

**Résultat attendu**: ✅ Widget s'ouvre avec animation smooth

---

**Étapes**:
1. Widget ouvert
2. Taper un message: "Bonjour"
3. Presser Entrée
4. Observer le message s'ajouter à droite (style utilisateur)
5. Observer l'indicateur "typing..." (3 points)
6. Après 1-2 secondes, une réponse apparaît à gauche

**Résultat attendu**: ✅ Conversation fluide, styles différents user/assistant

---

**Étapes**:
1. Widget ouvert avec un message
2. Cliquer le bouton X en haut-droit du widget
3. Observer que le widget se ferme

**Résultat attendu**: ✅ Widget se ferme normalement

---

### 3. ✅ Page Dédiée Chatbot

**Étapes**:
1. Être connecté
2. Cliquer sur "Chatbot IA" dans le menu principal
3. Observer la page dédiée

**Résultat attendu**: ✅ Page charge, widget flottant disparaît

---

**Étapes**:
1. Sur la page Chatbot
2. Envoyer un message via l'input "Posez votre question..."
3. Observer que le message s'ajoute à la zone de chat
4. Observer une réponse après quelques secondes

**Résultat attendu**: ✅ Conversation fonctionne sur page dédiée

---

**Étapes**:
1. Sur page Chatbot avec plusieurs messages
2. Naviguer vers une autre page (ex: "Trouver un mentor")
3. Le widget doit réapparaître
4. Observer que les messages antérieurs sont toujours là

**Résultat attendu**: ✅ Widget réapparaît, historique conservé

---

### 4. ✅ Historique Persistant

**Étapes**:
1. Envoyer 3 messages via le widget
2. Recharger la page (F5)
3. Observer les messages dans le widget

**Résultat attendu**: ✅ Les 3 messages antérieurs sont visibles

---

**Étapes**:
1. Sur page Chatbot avec historique
2. Cliquer "Mes RDV" ou autre page
3. Revenir à "Chatbot IA"
4. Observer les messages antérieurs

**Résultat attendu**: ✅ Historique complète visible

---

**Étapes**:
1. Se déconnecter
2. Se reconnecter avec le MÊME compte
3. Ouvrir le widget
4. Vérifier les messages de l'ancienne session

**Résultat attendu**: ✅ Historique par utilisateur conservé

---

**Étapes**:
1. Être connecté en tant que user1@exemple.com
2. Envoyer 3 messages
3. Se déconnecter et reconnecter avec user2@exemple.com
4. Vérifier l'historique (devrait être vide pour user2)

**Résultat attendu**: ✅ Chaque utilisateur a son historique isolé

---

### 5. ✅ Gestion des Erreurs

**Étapes**:
1. Ouvrir une page Chatbot sur navigateur sans WebGPU (ex: Safari)
2. Observer le message d'avertissement
3. Essayer d'envoyer un message

**Résultat attendu**: ✅ Message d'avertissement, mode simulé fonctionne

---

**Étapes**:
1. Vérifier Console (F12) pour les erreurs
2. Envoyer plusieurs messages rapidement
3. Observer pas de crash

**Résultat attendu**: ✅ Pas d'erreurs non gérées en console

---

### 6. ✅ Responsive Design

**Étapes**:
1. Ouvrir sur téléphone (ou DevTools mode mobile)
2. Widget devrait occuper 90% de largeur
3. Les messages doivent être lisibles
4. L'input doit être accessible

**Résultat attendu**: ✅ Widget adapté au mobile

---

**Étapes**:
1. Orientation Portrait → Paysage sur mobile
2. Observer que le widget s'adapte
3. Conversation toujours lisible

**Résultat attendu**: ✅ Adaptation responsive

---

### 7. ✅ Navigation Existante Non-Rompue

**Étapes**:
1. Page d'accueil: Vérifier sections visibles
2. Cliquer "Trouver un mentor": Charge normalement
3. Cliquer "Mes RDV": Charge normalement
4. Page valeurs: Peuvent toujours être accessibles
5. "Devenir mentor": Formulaire fonctionne

**Résultat attendu**: ✅ Toutes les pages existantes fonctionnent

---

**Étapes**:
1. Sur "Trouver un mentor" avec widget ouvert
2. Filtrer par spécialisation
3. Cliquer sur un mentor
4. Observer que la navigation fonctionne
5. Widget reste accessible

**Résultat attendu**: ✅ Navigation fluide, widget ne perturbe pas

---

### 8. ✅ Formulaires Existants

**Étapes**:
1. Aller sur "Devenir mentor"
2. Remplir et soumettre le formulaire
3. Observer pas d'erreurs

**Résultat attendu**: ✅ Formulaires fonctionnent normalement

---

**Étapes**:
1. Demander un RDV avec un mentor
2. Remplir les détails
3. Confirmer le RDV

**Résultat attendu**: ✅ RDV créé sans problème

---

### 9. ✅ Performance

**Étapes**:
1. Ouvrir le site pour la PREMIÈRE fois
2. Mesurer le temps avant que le widget soit utilisable
3. Vérifier la console pour les logs

**Résultat attendu**: ⚠️ 30-60 secondes (téléchargement modèle normal la 1ère fois)

---

**Étapes**:
1. Widget déjà chargé une fois
2. Recharger la page
3. Mesurer le temps de chargement

**Résultat attendu**: ✅ Instantané (< 2 secondes)

---

**Étapes**:
1. Envoyer 10 messages rapidement
2. Observer l'application reste fluide
3. Pas de lag ou freeze

**Résultat attendu**: ✅ Pas de ralentissement

---

### 10. ✅ Messages Spéciaux

**Tester les réponses automatiques**:
- Message: "Bonjour" → Réponse personnalisée
- Message: "aide" → Réponse sur l'aide
- Message: "javascript" → Info JavaScript
- Message: "python" → Info Python
- Message: "web" → Info dev web
- Message: "mentor" → Info mentors
- Message: "rdv" → Info RDV

**Résultat attendu**: ✅ Réponses intelligentes par keyword

---

**Tester un message random**:
- Message: "xyzabc123random"

**Résultat attendu**: ✅ Réponse par défaut raisonnable

---

### 11. ✅ Accès Authentification

**Étapes**:
1. Sans être connecté, accéder /index.html#chatbot
2. Widget ne devrait pas être présent

**Résultat attendu**: ✅ Pas d'accès au widget sans auth

---

**Étapes**:
1. Se connecter
2. Accéder /index.html#chatbot
3. Widget et page visibles

**Résultat attendu**: ✅ Accès à la page dédiée

---

### 12. ✅ Scrolling

**Étapes**:
1. Widget ouvert avec 5+ messages
2. Observer que le widget scroll automatiquement en bas
3. Ajouter un nouveau message
4. Observer que le scroll suit

**Résultat attendu**: ✅ Auto-scroll fonctionne

---

## Checklist de Déploiement

- [ ] Tous les fichiers créés (chatbot.js, CHATBOT_IA.md, etc.)
- [ ] CSS ajouté à style.css
- [ ] Widget HTML ajouté à index.html
- [ ] Script chatbot.js chargé
- [ ] CDN WebLLM inclus
- [ ] Pas d'erreurs console
- [ ] Widget caché quand non authentifié
- [ ] Widget visible quand authentifié
- [ ] Historique persiste
- [ ] Page dédiée fonctionne
- [ ] Navigation existante non rompue
- [ ] Tests mobiles réussis
- [ ] Tests WebGPU manquant réussis
- [ ] Performance acceptable

## Résultats

### Avant Déploiement
```
Total Tests: 12 scénarios
À Tester: Tous
```

### Après Test
```
Total Tests: 12 scénarios
✅ Passés: __/12
❌ Échoués: __/12
⚠️ À Vérifier: __/12
```

## Notes de Test

```
Date: _______________
Testeur: _______________
Navigateur: _______________
OS: _______________
WebGPU: Oui / Non

Observations:
________________________________
________________________________
________________________________

Bugs Trouvés:
1. ________________________________
2. ________________________________

Améliorations Suggérées:
1. ________________________________
2. ________________________________
```

---

**Version**: 1.0  
**Mise à jour**: Décembre 2025
