# 🚀 Guide d'utilisation - Système d'Authentification La Tour

## Démarrage rapide

### Ouverture de l'application
1. Ouvrir `index.html` dans un navigateur web
2. La page d'authentification s'affiche automatiquement

### Scénarios de test

#### ✅ Test 1: Login avec utilisateur test
1. Page d'authentification apparaît avec onglet "Se connecter" actif
2. Remplir :
   - **Email** : `latour@laplateforme.io`
   - **Mot de passe** : `1234`
3. Cliquer "Se connecter"
4. **Résultat attendu** :
   - Page d'accueil s'affiche
   - Header affiche les 4 boutons (Accueil, Mentorat ▼, Mes rendez-vous, Chatbot IA)
   - Profil utilisateur visible avec email et "Déconnexion"
   - Burger menu des spécialisations visible

#### ✅ Test 2: Création de nouveau compte
1. Cliquer sur onglet "Créer un compte"
2. Remplir :
   - **Email** : `newtestuser@example.com`
   - **Mot de passe** : `testpass1234`
   - **Confirmer** : `testpass1234`
3. Cliquer "Créer un compte"
4. **Résultat attendu** :
   - Compte créé et utilisateur auto-connecté
   - Affichage de la page d'accueil
   - Profil affiche le nouvel email

#### ✅ Test 3: Validation des erreurs
1. **Cas 1 - Email ou mdp incorrect**
   - Login : `latour@laplateforme.io` / `wrongpassword`
   - Résultat : "Email ou mot de passe incorrect"

2. **Cas 2 - Mdp < 4 caractères**
   - Onglet "Créer un compte"
   - Email : `test@test.com`, Mdp : `123`
   - Résultat : "Le mot de passe doit contenir au moins 4 caractères"

3. **Cas 3 - Mdp non correspondants**
   - Onglet "Créer un compte"
   - Email : `test@test.com`, Mdp : `abcd`, Confirmer : `efgh`
   - Résultat : "Les mots de passe ne correspondent pas"

4. **Cas 4 - Email déjà utilisé**
   - Onglet "Créer un compte"
   - Email : `latour@laplateforme.io` (existant), Mdp : `newpass123`
   - Résultat : "Cet email est déjà utilisé"

#### ✅ Test 4: Déconnexion
1. Après connexion, localiser le bouton "Déconnexion" dans le header
2. Cliquer dessus
3. **Résultat attendu** :
   - Page d'authentification réapparaît
   - Les 4 boutons disparaissent
   - Bouton "S'identifier" visible
   - Toutes les données de session sont effacées

#### ✅ Test 5: Bouton "S'identifier" depuis page d'accueil
1. Après déconnexion et rechargement, cliquer "S'identifier"
2. **Résultat attendu** :
   - Page d'authentification réapparaît
   - Les 4 boutons disparaissent

#### ✅ Test 6: Burger menu des spécialisations
1. Page d'accueil (après login)
2. Localiser le burger menu (3 lignes) dans le header
3. Cliquer sur le burger
4. **Résultat attendu** :
   - Menu s'ouvre avec dropdown
   - Affiche les 5 spécialisations :
     - 💻 Dev Web
     - 🤖 IA
     - 🔒 Cybersécurité
     - 🎮 Systèmes Immersifs
     - ⚙️ Logiciels
   - Burger se transforme en X
5. Cliquer ailleurs → menu se ferme

#### ✅ Test 7: Persistance de session
1. Après login, rafraîchir la page (F5)
2. **Résultat attendu** :
   - Utilisateur reste connecté
   - Page d'accueil s'affiche directement
   - Profil utilisateur conservé

#### ✅ Test 8: Navigation complète
Après login :
1. Cliquer "Accueil" → section d'accueil
2. Cliquer "Mentorat" → affiche dropdown avec 2 options
3. Cliquer "Mes rendez-vous" → page de rendez-vous
4. Cliquer "Chatbot IA" → page chatbot

### Utilisation avancée

#### Créer plusieurs utilisateurs
1. Créer les comptes via "Créer un compte"
2. Test avec différents emails/passwords
3. Basculer entre comptes via déconnexion/reconnexion

#### Vérifier le stockage localStorage
1. Ouvrir DevTools (F12)
2. Application → LocalStorage
3. Observer :
   - **users** : Liste de tous les utilisateurs
   - **user** : Utilisateur actuellement connecté

#### Exemple de données stockées
```json
// Onglet "users" dans localStorage
[
  { "email": "latour@laplateforme.io", "password": "1234" },
  { "email": "john@example.com", "password": "pass123" }
]

// Onglet "user" dans localStorage (si connecté)
{ "email": "latour@laplateforme.io" }
```

#### Réinitialiser tout
1. DevTools → Application → LocalStorage
2. Supprimer les clés "users" et "user"
3. Rafraîchir la page
4. Utilisateur test se recréera automatiquement

### Dépannage

#### Problème : Page blanche au démarrage
- **Solution** : Vérifier la console (F12) pour les erreurs JavaScript
- **Cause probable** : Script error ou fichier CSS manquant

#### Problème : Impossible de se connecter
- **Solution 1** : Vérifier l'email/password exact
- **Solution 2** : Regarder localStorage pour voir les utilisateurs enregistrés
- **Solution 3** : Réinitialiser localStorage et recommencer

#### Problème : Burger menu ne fonctionne pas
- **Solution** : Assurez-vous d'être sur un écran ≥ 1025px ou légèrement réduire le zoom

#### Problème : Menu des 4 boutons manquant
- **Cause** : Utilisateur non authentifié (normal)
- **Solution** : Se connecter ou créer un compte

### Questions fréquentes

**Q: Où sont stockés les mots de passe?**
A: Actuellement dans localStorage du navigateur en clair. Ne pas utiliser en production. Il faudrait les hacher avec bcrypt ou similar.

**Q: La session persiste après fermeture du navigateur?**
A: Oui, car on utilise localStorage. Utiliser sessionStorage pour supprimer après fermeture du navigateur.

**Q: Peut-on modifier les données depuis DevTools?**
A: Oui, c'est un exemple. En production, utiliser une API backend avec authentification tokens.

**Q: Combien d'utilisateurs peuvent être créés?**
A: Illimité (limité par la taille disponible dans localStorage, généralement 5-10MB).

**Q: Comment supprimer un utilisateur?**
A: Actuellement impossible via l'UI. Modifier manuellement dans DevTools ou réinitialiser localStorage.

---

**Support** : Pour toute question, vérifier la console (F12) pour les erreurs ou consulter le fichier AUTHENTIFICATION.md
