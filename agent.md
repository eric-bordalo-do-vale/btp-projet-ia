# 🤖 Guide des Agents IA - BTP Projet IA

## Vue d'Ensemble

Ce document décrit l'architecture conceptuelle des agents IA dans le prototype **BTP Projet IA**. Ces agents sont conçus pour assister les utilisateurs (étudiants, enseignants, partenaires) dans la résolution de problèmes techniques et conceptuels.

## Principes de Conception

### 1. Spécialisation Multi-Domaines
Chaque agent est optimisé pour un domaine spécifique avec des prompts adaptés :
- **Agent Debugging** : Analyse de code et résolution de bugs
- **Agent Concepts** : Explication de théories et principes
- **Agent Architecture** : Aide à la conception système
- **Agent Ressources** : Recommandation de matériels d'apprentissage

### 2. Ingénierie des Prompts
- Prompts contextuels adaptés à l'utilisateur
- Escalade progressive de la complexité
- Feedback iteratif pour l'amélioration

### 3. Gestion du Contexte
- Historique des interactions
- Niveau de compétence détecté
- Domaine d'expertise en focus

## Architecture des Agents

### Agent Debugging (Débogage)

**Objectif** : Aider à identifier et résoudre les bugs de code

**Spécialités** :
- Analyse de code source
- Trace d'exécution et logs
- Suggestions de solutions
- Prévention des erreurs courantes

**Prompt Strategy** :
```
Tu es un expert en débogage. Analyze le code, identifie le bug,
et fournis une explication progressive du problème et de la solution.
```

**Entrées** :
- Code problématique
- Message d'erreur
- Contexte d'exécution

**Sorties** :
- Identification du bug
- Explication causale
- Solution corrigée
- Ressources d'apprentissage

---

### Agent Concepts (Apprentissage)

**Objectif** : Expliquer des concepts complexes de manière progressive

**Spécialités** :
- Cryptographie, réseaux, systèmes
- Paradigmes de programmation
- Architecture logicielle

**Prompt Strategy** :
```
Tu es un pédagogue IA. Explique ce concept à un étudiant,
en partant du simple et en progressant vers le complexe.
Utilise des analogies et des exemples concrets.
```

**Entrées** :
- Concept à expliquer
- Niveau de l'utilisateur
- Domaine contexte

**Sorties** :
- Explication progressive
- Exemples pratiques
- Analogies
- Ressources complémentaires

---

### Agent Architecture (Design Système)

**Objectif** : Conseiller sur l'architecture et la conception

**Spécialités** :
- Patterns de conception
- Scalabilité et performance
- Sécurité système
- Infrastructure

**Prompt Strategy** :
```
Tu es un architecte système senior. Aide à concevoir une solution
scalable et sécurisée. Considère les trade-offs et les bonnes pratiques.
```

**Entrées** :
- Description du problème
- Contraintes
- Outils/technos disponibles

**Sorties** :
- Recommandations architecturales
- Diagrammes conceptuels
- Trade-offs analysis
- Étapes d'implémentation

---

### Agent Ressources (Apprentissage Continu)

**Objectif** : Recommander des ressources d'apprentissage pertinentes

**Spécialités** :
- Recommandation curatée
- Sources fiables
- Contenu progressif

**Prompt Strategy** :
```
Tu es un curateur de ressources. Recommande des matériels d'apprentissage
de qualité, du niveau approprié, pour progresser dans ce domaine.
```

**Entrées** :
- Domaine d'intérêt
- Niveau actuel
- Objectifs

**Sorties** :
- Ressources recommandées (docs, tutoriels, cours)
- Parcours d'apprentissage
- Points de contrôle

---

## Orchestration Multi-Agents

### Flux d'Interaction Typique

```
Utilisateur
    ↓
[Analyse du contexte]
    ↓
Dispatch vers agent(s) approprié(s)
    ↓
Agent(s) traite(nt) la requête
    ↓
Formatage et synthèse de la réponse
    ↓
Retour utilisateur avec ressources
```

### Coordination Inter-Agents

- **Agent Debugging** → recommande **Agent Concepts** pour expliquer l'erreur
- **Agent Concepts** → suggère **Agent Ressources** pour approfondir
- **Agent Architecture** → consulte **Agent Debugging** pour validation
- **Agent Ressources** → adapte basé sur feedback des autres agents

## Système de Prompts

### Structure de Prompt Standard

```
[Rôle]:
Tu es un [spécialiste IA] dans [domaine]

[Contexte]:
L'utilisateur est un [profil] avec niveau [niveau]

[Objectif]:
Tu dois [accomplir cette tâche] de manière [approche]

[Contraintes]:
- [Constraint 1]
- [Constraint 2]

[Format de réponse]:
[Specify output format]
```

### Exemple: Agent Debugging

```
Rôle:
Tu es un expert en débogage de code et résolution de problèmes techniques.

Contexte:
L'utilisateur est un étudiant en cybersécurité apprenant la programmation.

Objectif:
Aide à identifier et résoudre le bug de manière pédagogique.
Explique POURQUOI c'est un bug, pas juste comment le corriger.

Contraintes:
- Sois progressif: commence simple, complexifie si besoin
- Fournis toujours une explication et pas juste du code
- Suggère des bonnes pratiques de prévention

Format de réponse:
1. Identification du bug
2. Explication causale
3. Solution proposée
4. Leçon à retenir
5. Ressources pour approfondir
```

## Gestion des Niveaux d'Utilisateurs

### Classification

- **Débutant** : Premiers pas, concepts de base
- **Intermédiaire** : Principes appliqués, problèmes modérés
- **Avancé** : Architectures complexes, optimisations

### Adaptation par Agent

Les agents adaptent :
- La profondeur techniquement
- Les termes utilisés
- Les exemples fournis
- Le pas à pas des explications

## Métriques de Performance

### Pour les Agents
- Résolution de problème (bug fixé ?)
- Compréhension utilisateur (feedback)
- Temps de réponse
- Pertinence des recommandations

### Pour le Système
- Taux de satisfaction utilisateur
- Nombre d'escalades réussies
- Efficacité des collaborations inter-agents
- Analyse des feedback

## Évolution Future

### Améliorations Envisagées
- [ ] Mémoire persistante des utilisateurs
- [ ] Fine-tuning des modèles LLM
- [ ] Agents spécialisés supplémentaires (Sécurité, DevOps, etc.)
- [ ] Apprentissage par reinforcement feedback utilisateur
- [ ] Intégration avec outils externes (GitHub, Stack Overflow, etc.)

### Recherche
- Optimisation des prompts via A/B testing
- Études sur l'efficacité pédagogique
- Analyse des patterns d'utilisation
- Co-apprentissage humain-IA

---

## Notes pour les Développeurs

### Implémentation
Chaque agent devrait :
1. Implémenter une interface commune
2. Maintenir un historique du contexte
3. Supporter les escalades vers d'autres agents
4. Générer du feedback structuré

### Testing
- Tests unitaires par agent
- Intégration multi-agents
- Tests pédagogiques avec utilisateurs réels
- Validation des prompts

### Documentation
- Prompts explicits et documentés
- Exemples d'entrée/sortie
- Trade-offs et limitations connus
- Roadmap d'amélioration

---

**Développé par le Projet BTP IA - Équipe Cybersécurité Marseille**
