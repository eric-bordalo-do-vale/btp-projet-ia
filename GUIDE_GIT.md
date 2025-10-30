# 🌿 Guide Git pour La Tour

Guide pour travailler en équipe avec Git sur le projet La Tour.

---

## 🚀 Setup initial (à faire une seule fois)

### 1. Configurer Git (si pas déjà fait)
```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
```

### 2. Vérifier le statut du repo
```bash
git status
```

### 3. Ajouter tous les fichiers
```bash
git add .
```

### 4. Premier commit
```bash
git commit -m "Initial commit: Setup du projet La Tour"
```

### 5. Pousser sur GitHub (si repository distant existe)
```bash
git remote add origin https://github.com/votre-username/btp-projet-ia.git
git branch -M main
git push -u origin main
```

---

## 📋 Workflow quotidien

### Avant de commencer à travailler
```bash
# 1. Vérifier sur quelle branche vous êtes
git branch

# 2. Se mettre sur main
git checkout main

# 3. Récupérer les dernières modifications
git pull

# 4. Créer une nouvelle branche pour votre feature
git checkout -b feature-nom-de-la-feature
```

### Pendant le travail
```bash
# Voir ce qui a changé
git status

# Voir les modifications en détail
git diff

# Ajouter des fichiers spécifiques
git add fichier1.py fichier2.html

# OU ajouter tous les fichiers modifiés
git add .

# Faire un commit
git commit -m "Description claire des changements"
```

### Quand la feature est terminée
```bash
# 1. S'assurer d'avoir tout committé
git status

# 2. Pousser la branche
git push origin feature-nom-de-la-feature

# 3. Créer une Pull Request sur GitHub
# (via l'interface web de GitHub)

# 4. Après merge, supprimer la branche locale
git checkout main
git pull
git branch -d feature-nom-de-la-feature
```

---

## 🌿 Stratégie de branches

### Branches principales

```
main (ou master)
└── Code stable, testé, prêt à déployer
```

### Branches de features

```
feature/authentification
feature/chatbot-ia
feature/messagerie
feature/notifications
fix/bug-rdv
```

### Convention de nommage

| Type | Exemple | Usage |
|------|---------|-------|
| `feature/` | `feature/login` | Nouvelle fonctionnalité |
| `fix/` | `fix/bug-rdv` | Correction de bug |
| `refactor/` | `refactor/database` | Refactoring code |
| `style/` | `style/navbar` | Changements CSS |
| `docs/` | `docs/readme` | Documentation |

---

## 💬 Messages de commit

### Structure d'un bon commit
```
Type: Description courte (50 caractères max)

Description détaillée si nécessaire (72 caractères par ligne max)
- Point 1
- Point 2

Refs #issue_number (si applicable)
```

### Types de commits

| Type | Exemple |
|------|---------|
| `feat:` | `feat: Ajout du système de login` |
| `fix:` | `fix: Correction du bug sur les RDV` |
| `style:` | `style: Amélioration du design de la navbar` |
| `refactor:` | `refactor: Restructuration du code de la BDD` |
| `docs:` | `docs: Mise à jour du README` |
| `test:` | `test: Ajout des tests unitaires` |
| `chore:` | `chore: Mise à jour des dépendances` |

### Exemples de bons commits
```bash
git commit -m "feat: Ajout de l'authentification utilisateur"
git commit -m "fix: Correction du filtre de mentors"
git commit -m "style: Amélioration du responsive mobile"
git commit -m "docs: Ajout du guide HTMX"
```

---

## 🔄 Résolution de conflits

### Quand un conflit survient
```bash
# 1. Git vous informe d'un conflit
git pull
# CONFLICT (content): Merge conflict in app.py

# 2. Ouvrir le fichier en conflit
# Vous verrez quelque chose comme :
<<<<<<< HEAD
# Votre code
=======
# Code de quelqu'un d'autre
>>>>>>> branch-name

# 3. Choisir quelle version garder ou fusionner manuellement

# 4. Marquer comme résolu
git add app.py

# 5. Terminer le merge
git commit -m "Merge: Résolution des conflits"
```

---

## 📦 Commandes utiles

### Voir l'historique
```bash
# Historique complet
git log

# Historique condensé
git log --oneline

# Historique avec graphique
git log --graph --oneline --all
```

### Annuler des changements
```bash
# Annuler les modifications d'un fichier (avant add)
git checkout -- fichier.py

# Retirer un fichier du staging (après add, avant commit)
git reset HEAD fichier.py

# Annuler le dernier commit (garder les modifications)
git reset --soft HEAD~1

# Annuler le dernier commit (perdre les modifications)
git reset --hard HEAD~1
```

### Stash (mettre de côté)
```bash
# Mettre de côté les modifications
git stash

# Voir la liste des stash
git stash list

# Récupérer le dernier stash
git stash pop

# Récupérer un stash spécifique
git stash apply stash@{0}
```

### Branches
```bash
# Lister toutes les branches
git branch -a

# Créer une branche
git branch nom-branche

# Changer de branche
git checkout nom-branche

# Créer et changer de branche
git checkout -b nom-branche

# Supprimer une branche
git branch -d nom-branche

# Renommer la branche actuelle
git branch -m nouveau-nom
```

---

## 👥 Workflow en équipe

### Répartition des branches

```
main
├── feature/authentification (Personne 1)
├── feature/chatbot (Personne 2)
├── feature/design (Personne 3)
└── feature/tests (Personne 4)
```

### Règles de l'équipe

1. **Jamais de push direct sur main**
   - Toujours passer par une Pull Request

2. **Commits fréquents**
   - Au moins 1 commit par fonctionnalité complétée

3. **Pull avant push**
   - Toujours `git pull` avant de `git push`

4. **Code review**
   - Au moins 1 personne doit valider la PR

5. **Tests avant merge**
   - Tester localement avant de merger

---

## 🔍 Pull Requests (PR)

### Créer une PR sur GitHub

1. Aller sur le repository GitHub
2. Cliquer sur "Pull Requests"
3. Cliquer sur "New Pull Request"
4. Sélectionner votre branche
5. Remplir le titre et la description
6. Assigner des reviewers
7. Créer la PR

### Template de PR
```markdown
## 🎯 Description
Brève description de ce qui a été fait

## 🔄 Changements
- Ajout de X
- Modification de Y
- Suppression de Z

## ✅ Tests effectués
- [ ] Testé sur Firefox
- [ ] Testé sur Chrome
- [ ] Testé sur mobile

## 📸 Screenshots (si UI)
[Ajouter des captures d'écran]

## 📝 Notes
Informations supplémentaires pour les reviewers
```

---

## 🚨 Situations d'urgence

### J'ai committé sur la mauvaise branche
```bash
# 1. Noter le hash du commit
git log --oneline

# 2. Changer de branche
git checkout bonne-branche

# 3. Cherry-pick le commit
git cherry-pick <hash-du-commit>

# 4. Retourner sur la mauvaise branche
git checkout mauvaise-branche

# 5. Annuler le commit
git reset --hard HEAD~1
```

### J'ai committé des fichiers sensibles (.env)
```bash
# 1. Supprimer du dernier commit
git rm --cached .env

# 2. Ajouter au .gitignore
echo ".env" >> .gitignore

# 3. Commit
git commit -m "Remove .env from tracking"

# 4. Si déjà pushé, utiliser git-filter-branch ou BFG
```

### Je veux tout recommencer
```bash
# ⚠️ ATTENTION: Perd toutes les modifications locales
git reset --hard HEAD
git clean -fd
```

---

## 📚 Ressources

### Documentation
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

### Outils visuels
- **GitKraken** - Interface graphique Git
- **GitHub Desktop** - Client Git officiel
- **VS Code** - Intégration Git native

### Tutoriels
- [Learn Git Branching](https://learngitbranching.js.org/)
- [Git Immersion](http://gitimmersion.com/)

---

## 🎓 Best Practices

### DO ✅
- Commits fréquents et petits
- Messages de commit clairs
- Pull avant de push
- Créer des branches pour chaque feature
- Code review avant merge
- Tester avant de commit

### DON'T ❌
- Ne pas commit de fichiers sensibles (.env)
- Ne pas commit de fichiers générés (node_modules, venv)
- Ne pas faire de gros commits fourre-tout
- Ne pas travailler directement sur main
- Ne pas force push sur main
- Ne pas commit du code non testé

---

## 🎯 Workflow résumé

```
1. git checkout main
2. git pull
3. git checkout -b feature/ma-feature
4. [Travailler sur le code]
5. git add .
6. git commit -m "feat: Ma feature"
7. git push origin feature/ma-feature
8. [Créer une PR sur GitHub]
9. [Code review]
10. [Merge la PR]
11. git checkout main
12. git pull
13. git branch -d feature/ma-feature
```

---

Avec ce workflow, votre équipe travaillera efficacement et sans conflits ! 🚀

**Questions ? Consultez la doc Git ou demandez à l'équipe !**
