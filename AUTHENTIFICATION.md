# Système d'Authentification - La Tour

## Résumé des changements

### 1. **Header modifié**
- **Logo animé supprimé** : L'image "La Tour" a été retirée du header
- **Burger menu des spécialisations** : Remplace le logo, affiche au clic les 5 spécialisations :
  - 💻 Dev Web
  - 🤖 IA
  - 🔒 Cybersécurité
  - 🎮 Systèmes Immersifs
  - ⚙️ Logiciels
- **Menu des 4 boutons caché** : Ne s'affiche que si l'utilisateur est authentifié
- **Bouton "S'identifier"** : Remplace les 4 boutons pour les utilisateurs non authentifiés
- **Profil utilisateur** : Affiche l'email et un bouton "Déconnexion" après authentification

### 2. **Système d'authentification**

#### Page de Login/Register
- **Interface avec 2 onglets** :
  1. **Se connecter** : Formulaire email + mot de passe
  2. **Créer un compte** : Formulaire email + mot de passe + confirmation

#### Fonctionnement
- **Stockage local** : Utilise `localStorage` du navigateur pour persister les données
- **Session utilisateur** : Maintient l'utilisateur connecté jusqu'à la déconnexion
- **Auto-création du compte** : La création d'un compte enregistre automatiquement l'utilisateur
- **Validation** :
  - Min 4 caractères pour le mot de passe
  - Les mots de passe doivent correspondre
  - Pas d'email doublon

#### Flux d'authentification
1. À l'ouverture : Page de login s'affiche
2. Login réussi → Page d'accueil avec menu + profil utilisateur
3. Click "S'identifier" → Page de login s'affiche de nouveau
4. Click "Déconnexion" → Retour à la page de login

### 3. **Utilisateur de test**
- **Email** : `latour@laplateforme.io`
- **Mot de passe** : `1234`
- Créé automatiquement au premier chargement

### 4. **Burger menu des spécialisations**
- **Visible sur tous les écrans** (≥ 1025px)
- **Position** : À côté du menu principal
- **Animation** : Icône en X au clic
- **Dropdown** : Affiche les 5 spécialisations

### 5. **Stockage des données**
```javascript
// Format dans localStorage
localStorage['users'] = [
  { email: 'user@example.com', password: '1234' },
  { email: 'latour@laplateforme.io', password: '1234' }
]

localStorage['user'] = { email: 'user@example.com' } // Utilisateur courant
```

## Fichiers modifiés

### `index.html`
- Suppression du logo animé du header
- Ajout du burger menu des spécialisations
- Ajout de l'interface d'authentification (Login/Register)
- Modification du header avec bouton "S'identifier" / profil utilisateur
- Ajout du JavaScript pour la gestion d'authentification

### `static/css/style.css`
- Styles pour la page d'authentification
- Styles pour le burger menu des spécialisations
- Styles pour la section auth (bouton et profil utilisateur)
- Responsive design pour mobile
- Animations de transition

## Tests recommandés

1. **Chargement initial** : Affiche page de login
2. **Création de compte** :
   - Remplir email et mot de passe
   - Vérifier que l'utilisateur est connecté
   - Vérifier que le menu s'affiche
3. **Login avec compte existant**:
   - Email : `latour@laplateforme.io`
   - Mot de passe : `1234`
   - Doit arriver sur la page d'accueil
4. **Déconnexion** : Bouton "Déconnexion" → Retour login
5. **Burger menu** : Clic → Affiche spécialisations
6. **Validation** :
   - Mots de passe non correspondants
   - Email déjà existant
   - Mot de passe < 4 caractères

## Prochaines étapes possibles

- Intégrer avec la base de données backend (remplacer localStorage)
- Ajouter hachage des mots de passe (bcrypt)
- Ajouter système de sessions côté serveur
- Ajouter réinitialisation de mot de passe
- Ajouter email de confirmation
