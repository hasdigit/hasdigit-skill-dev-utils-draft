# Installation

## Installer un skill

Un skill est l’ensemble du dossier terminal qui contient son fichier `SKILL.md`. Copier ce dossier complet dans le répertoire de skills de l’environnement cible. Ne pas copier uniquement `SKILL.md`, car les références, templates et métadonnées font partie de la compétence.

Exemples d’unités installables :

- `skills/orchestration/ai-orchestrator-methodology/`
- `skills/frontend/react/react-vite-enterprise-saas/`

Dans Codex, le répertoire utilisateur est généralement `$CODEX_HOME/skills`. Lorsque `CODEX_HOME` n’est pas défini, utiliser le répertoire de skills indiqué par l’installation locale.

## Vérifier avant installation

1. Exécuter `python scripts/validate-all-skills.py`.
2. Vérifier que le résultat ne contient aucune erreur.
3. Copier le dossier terminal complet.
4. Redémarrer ou recharger l’environnement si la plateforme l’exige.
5. Vérifier que le nom et la description du skill apparaissent correctement.
