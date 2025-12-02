# 🧪 Scénarios de test complets

## Avant de commencer
1. Ouvrir `index.html` dans un navigateur moderne
2. Ouvrir DevTools (F12) → Console pour voir les erreurs éventuelles
3. Vérifier localStorage dans DevTools → Application → LocalStorage

---

## TEST 1: Chargement initial
```
ACTION:
1. Ouvrir index.html

RÉSULTAT ATTENDU:
✓ Page d'authentification s'affiche (fullscreen avec gradient bleu)
✓ Onglet "Se connecter" actif
✓ Formulaire avec champs Email et Mot de passe
✓ Onglet "Créer un compte" visible mais inactif
✓ Pas de menu de navigation visible
✓ localStorage['users'] contient l'utilisateur test
```

---

## TEST 2: Login avec l'utilisateur de test
```
ACTION:
1. Email: latour@laplateforme.io
2. Password: 1234
3. Cliquer "Se connecter"

RÉSULTAT ATTENDU:
✓ Page d'authentification disparaît
✓ Page d'accueil s'affiche
✓ Menu de navigation visible avec 4 boutons:
   - Accueil
   - Mentorat ▼
   - Mes rendez-vous
   - Chatbot IA
✓ Profil utilisateur en haut à droite:
   - Email: latour@laplateforme.io
   - Bouton "Déconnexion"
✓ localStorage['user'] = {email: "latour@laplateforme.io"}

NAVIGATION TEST:
1. Cliquer "Accueil" → Section héros s'affiche
2. Cliquer "Mentorat ▼" → Dropdown apparaît
   - 👥 Trouver un mentor
   - 🎓 Devenir mentor
3. Cliquer "Mes rendez-vous" → Page rendez-vous s'affiche
4. Cliquer "Chatbot IA" → Page chatbot s'affiche
5. Cliquer "La Tour" (logo) → Revenir à l'accueil
```

---

## TEST 3: Burger menu des spécialisations
```
ACTION:
1. Après login, localiser le burger menu (3 lignes horizontales)
2. Cliquer dessus

RÉSULTAT ATTENDU:
✓ Burger button se transforme en X (animation)
✓ Dropdown apparaît sous le burger avec 5 items:
   💻 Dev Web
   🤖 IA
   🔒 Cybersécurité
   🎮 Systèmes Immersifs
   ⚙️ Logiciels
✓ Chaque item a un hover effect (texte bleu + indent)
✓ Cliquer sur un item: 
   - Ferme le dropdown (optionnel pour cette version)
   - Item devient bleu temporairement

ACTION 2:
1. Cliquer ailleurs sur la page

RÉSULTAT ATTENDU:
✓ Dropdown se ferme
✓ Burger revient à l'état normal (3 lignes)
```

---

## TEST 4: Déconnexion
```
ACTION:
1. Après login, localiser le bouton "Déconnexion"
2. Cliquer dessus

RÉSULTAT ATTENDU:
✓ Page d'authentification réapparaît
✓ Menu de navigation disparaît
✓ Bouton "S'identifier" visible
✓ Onglets sont réinitialisés (login actif)
✓ localStorage['user'] est supprimé
✓ localStorage['users'] conserve les comptes
✓ Formulaires de login et register sont vides
```

---

## TEST 5: Bouton "S'identifier" depuis la page d'accueil (après logout)
```
ACTION:
1. Après déconnexion, attendre quelques secondes
2. Vérifier qu'on est bien sur la page d'authentification
3. Cliquer "S'identifier" (doit être visible)

RÉSULTAT ATTENDU:
✓ Page d'authentification reste visible
✓ Onglet "Se connecter" est actif
✓ Tous les champs sont vides
```

---

## TEST 6: Créer un nouveau compte
```
ACTION:
1. Sur la page d'authentification
2. Cliquer onglet "Créer un compte"
3. Email: testuser@example.com
4. Mot de passe: testpass123
5. Confirmer: testpass123
6. Cliquer "Créer un compte"

RÉSULTAT ATTENDU:
✓ Compte créé et utilisateur auto-connecté
✓ Page d'accueil s'affiche
✓ Profil affiche: testuser@example.com
✓ Menu de navigation visible
✓ localStorage['users'] contient 2 utilisateurs
✓ localStorage['user'] = {email: "testuser@example.com"}

VÉRIFICATION ADDITIONNELLE:
1. Déconnecter (Déconnexion)
2. Login avec testuser@example.com / testpass123
3. Doit fonctionner correctement
```

---

## TEST 7: Validation - Mot de passe incorrect
```
ACTION:
1. Page d'authentification (onglet "Se connecter")
2. Email: latour@laplateforme.io
3. Mot de passe: wrongpassword
4. Cliquer "Se connecter"

RÉSULTAT ATTENDU:
✓ Message d'erreur s'affiche:
   "Email ou mot de passe incorrect"
✓ Erreur est rouge et au-dessus du bouton
✓ Aucune redirection ne se produit
✓ localStorage['user'] ne change pas
✓ Utilisateur ne peut pas accéder à la page d'accueil
```

---

## TEST 8: Validation - Mdp < 4 caractères
```
ACTION:
1. Onglet "Créer un compte"
2. Email: test@test.com
3. Mot de passe: abc (3 caractères)
4. Confirmer: abc
5. Cliquer "Créer un compte"

RÉSULTAT ATTENDU:
✓ Message d'erreur:
   "Le mot de passe doit contenir au moins 4 caractères"
✓ Compte non créé
✓ Utilisateur reste sur la page de création
```

---

## TEST 9: Validation - Mots de passe non correspondants
```
ACTION:
1. Onglet "Créer un compte"
2. Email: test@test.com
3. Mot de passe: abcd1234
4. Confirmer: different5678
5. Cliquer "Créer un compte"

RÉSULTAT ATTENDU:
✓ Message d'erreur:
   "Les mots de passe ne correspondent pas"
✓ Compte non créé
```

---

## TEST 10: Validation - Email déjà utilisé
```
ACTION:
1. Onglet "Créer un compte"
2. Email: latour@laplateforme.io (existant)
3. Mot de passe: newpass123
4. Confirmer: newpass123
5. Cliquer "Créer un compte"

RÉSULTAT ATTENDU:
✓ Message d'erreur:
   "Cet email est déjà utilisé"
✓ Compte non créé
✓ Utilisateur reste sur la page de création
```

---

## TEST 11: Validation - Email invalide (optionnel)
```
ACTION:
1. Onglet "Se connecter"
2. Email: notanemail (sans @)
3. Mot de passe: 1234
4. Cliquer "Se connecter"

RÉSULTAT ATTENDU:
✓ HTML5 validation empêche la soumission
✓ Message natif du navigateur:
   "Veuillez inclure une adresse de messagerie"
```

---

## TEST 12: Persistance de session (localStorage)
```
ACTION:
1. Login: latour@laplateforme.io / 1234
2. Page d'accueil s'affiche
3. Rafraîchir la page (F5 ou Cmd+R)

RÉSULTAT ATTENDU:
✓ Utilisateur reste connecté
✓ Page d'accueil s'affiche directement
✓ Pas de page d'authentification
✓ Profil utilisateur conservé
✓ localStorage['user'] toujours présent

ACTION 2:
1. Fermer et rouvrir le navigateur
2. Aller sur index.html

RÉSULTAT ATTENDU:
✓ Utilisateur peut encore être connecté (selon localStorage)
✓ Si localStorage persiste, utilisateur connecté
```

---

## TEST 13: Tabs de navigation
```
ACTION:
1. Onglet "Se connecter" actif
2. Cliquer onglet "Créer un compte"

RÉSULTAT ATTENDU:
✓ Onglet "Se connecter" perd l'état actif (underline disparaît)
✓ Onglet "Créer un compte" devient actif (underline bleu)
✓ Formulaire de connexion disparaît
✓ Formulaire de création apparaît avec animation
✓ Les deux onglets changent de couleur au survol

ACTION 2:
1. Cliquer "Se connecter"

RÉSULTAT ATTENDU:
✓ Retour au formulaire de connexion
✓ Formulaire de création disparaît
✓ Styles des onglets changent
```

---

## TEST 14: Vérification localStorage
```
ACTION:
1. Ouvrir DevTools (F12)
2. Aller à Application → LocalStorage
3. Trouver "file://" ou votre URL

RÉSULTAT ATTENDU:
✓ 2 clés présentes:
   - "users" (liste de tous les utilisateurs)
   - "user" (utilisateur actuellement connecté)

EXEMPLE DE CONTENU:
users: [
  {"email":"latour@laplateforme.io","password":"1234"},
  {"email":"testuser@example.com","password":"testpass123"}
]

user: {"email":"latour@laplateforme.io"}
```

---

## TEST 15: Responsive design
```
ACTION 1 (Desktop):
1. Ouvrir dans navigateur normal
2. Largeur: ~1200px+

RÉSULTAT ATTENDU:
✓ Page d'authentification centrée
✓ Auth box: ~450px largeur max
✓ Burger menu visible à droite du menu
✓ Tous les éléments visibles et espacés

ACTION 2 (Tablet):
1. DevTools (F12) → Toggle device toolbar
2. iPad (768px)

RÉSULTAT ATTENDU:
✓ Auth box responsive
✓ Onglets affichés correctement
✓ Inputs prennent toute la largeur
✓ Burger menu toujours visible

ACTION 3 (Mobile):
1. DevTools → iPhone 12 (390px)

RÉSULTAT ATTENDU:
✓ Auth box responsive
✓ Padding réduit
✓ Fonts lisibles
✓ Inputs accessibles
✓ Burger menu toujours fonctionnel
```

---

## TEST 16: Animations et transitions
```
ACTION 1 (Auth page):
1. Ouvrir index.html
2. Observer la page d'authentification

RÉSULTAT ATTENDU:
✓ Auth box apparaît avec animation (scale)
✓ Transition fluide (<0.5s)

ACTION 2 (Burger menu):
1. Cliquer burger button
2. Observer l'animation

RÉSULTAT ATTENDU:
✓ Burger lignes se transforment en X (animation rotations)
✓ Dropdown apparaît avec fade-in
✓ Transformation fluide

ACTION 3 (Tab switching):
1. Cliquer onglets
2. Observer les transitions

RÉSULTAT ATTENDU:
✓ Formulaires apparaissent/disparaissent avec fade
✓ Pas de saccades
```

---

## Checklist de test complète

- [ ] Chargement initial → Auth page
- [ ] Login réussi → Page d'accueil
- [ ] Menu 4 boutons visible après login
- [ ] Profil utilisateur visible après login
- [ ] Bouton "S'identifier" visible avant login
- [ ] Déconnexion fonctionne
- [ ] Création de compte fonctionne
- [ ] Burger menu affiche spécialisations
- [ ] Burger menu animation X
- [ ] Validation mdp incorrect
- [ ] Validation mdp < 4 caractères
- [ ] Validation mdp non-correspondants
- [ ] Validation email doublon
- [ ] Persistance de session (F5 ne déconnecte pas)
- [ ] localStorage contient les bonnes données
- [ ] Responsive design (desktop, tablet, mobile)
- [ ] Animations fluides
- [ ] Pas d'erreurs dans console (F12)
- [ ] Toutes les transitions sont lisses
- [ ] Tous les boutons sont cliquables
- [ ] Tous les formulaires valident les inputs

---

## Dépannage rapide

| Problème | Solution |
|----------|----------|
| Page blanche | Vérifier console (F12) pour erreurs |
| Pas de localStorage | Navigateur en mode privé → désactiver |
| Boutons ne réagissent pas | Vérifier que les IDs correspondent |
| Animations hachées | Réduire les effets ou mettre à jour navigateur |
| Menu non visible | Vérifier la taille de l'écran (≥1025px pour burger) |
| Utilisateur pas connecté après F5 | localStorage peut-être supprimé → vérifier DevTools |

---

**Durée estimée des tests**: 30-45 minutes pour tout couvrir

Fin des scénarios de test.
