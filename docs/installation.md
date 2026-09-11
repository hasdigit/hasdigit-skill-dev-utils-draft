# Installation

## Installer un skill

Un skill est l’ensemble du dossier terminal qui contient son fichier `SKILL.md`. Copier ce dossier complet dans le répertoire de skills de l’environnement cible. Ne pas copier uniquement `SKILL.md`, car les références, templates et métadonnées font partie de la compétence.

Exemples d’unités installables :

- `skills/orchestration/ai-orchestrator-methodology/`
- `skills/frontend/react/react-vite-enterprise-saas/`
- `skills/frontend/nextjs/nextjs-enterprise-saas/`
- `skills/fullstack/nextjs/nextjs-fullstack-enterprise-saas/`

Dans Codex, le répertoire utilisateur est généralement `$CODEX_HOME/skills`. Lorsque `CODEX_HOME` n’est pas défini, utiliser le répertoire de skills indiqué par l’installation locale.

## Vérifier avant installation

1. Exécuter `python scripts/validate-all-skills.py`.
2. Vérifier que le résultat ne contient aucune erreur.
3. Copier le dossier terminal complet.
4. Redémarrer ou recharger l’environnement si la plateforme l’exige.
5. Vérifier que le nom et la description du skill apparaissent correctement.

## Initialiser chaque nouvelle session

L’installation technique ne suffit pas à garantir l’application des règles. Au début de chaque nouvelle session, l’utilisateur doit envoyer le prompt de démarrage fourni dans le dossier du skill concerné :

- [Prompt de démarrage du skill d’orchestration](../skills/orchestration/ai-orchestrator-methodology/installation/installation.md)
- [Prompt de démarrage du skill frontend React et Vite](../skills/frontend/react/react-vite-enterprise-saas/installation/installation.md)
- [Prompt de démarrage du skill frontend Next.js](../skills/frontend/nextjs/nextjs-enterprise-saas/installation/installation.md)
- [Prompt de démarrage du skill Next.js fullstack](../skills/fullstack/nextjs/nextjs-fullstack-enterprise-saas/installation/installation.md)

Chaque prompt demande à la session de :

1. lire et inventorier le dossier maître complet du skill ;
2. examiner les garde-fous déjà présents dans le projet ;
3. comparer ces garde-fous avec les exigences actuelles du skill ;
4. mettre à jour les contrôles devenus incomplets après une évolution du skill ;
5. créer un espace partagé entre sessions lorsqu’aucun emplacement équivalent n’existe ;
6. vérifier continuellement les changements contre le skill et produire des preuves avant de déclarer le travail terminé.

Le prompt correspondant au skill doit être utilisé à chaque nouvelle session, même si le projet possède déjà des garde-fous. Dans ce cas, la session doit les contrôler et les actualiser, sans les recréer aveuglément ni détruire les conventions existantes.
