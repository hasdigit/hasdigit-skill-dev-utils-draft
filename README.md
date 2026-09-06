# HasDigit Agent Skills

Ce dépôt contient des skills autonomes pour guider des agents d’intelligence artificielle dans des travaux d’ingénierie exigeants.

## Skills disponibles

- [Méthode d’orchestration](skills/orchestration/ai-orchestrator-methodology/SKILL.md) : cadrage, état, délégation, preuves, récupération et communication.
- [Frontend React et Vite Enterprise SaaS](skills/frontend/react/react-vite-enterprise-saas/SKILL.md) : architecture modulaire, permissions, sécurité, accessibilité, tests et livraison.

Chaque skill conserve ses propres références, templates, scénarios et historique. Aucun template métier n’est centralisé à la racine.

## Utilisation

Lire [l’installation](docs/installation.md), puis [l’utilisation du dépôt](docs/repository-usage.md). Pour contribuer, appliquer [les règles de contribution](docs/contributing.md).

## Validation

Exécuter :

    python scripts/validate-all-skills.py

Le validateur contrôle la structure, les liens, les frontmatters et la reconstruction exacte des trois documents d’origine à partir de la nouvelle arborescence.

## Branche de travail

La restructuration est développée sur la branche `Draft`. La branche `main` conserve l’état validé avant restructuration jusqu’à une nouvelle décision de fusion.
