# HasDigit Agent Skills

Ce dépôt contient des skills autonomes pour guider des agents d’intelligence artificielle dans des travaux d’ingénierie exigeants.

## Skills disponibles

- [Méthode d’orchestration](skills/orchestration/ai-orchestrator-methodology/SKILL.md) : cadrage, état, délégation, preuves, récupération et communication.
- [Frontend React et Vite Enterprise SaaS](skills/frontend/react/react-vite-enterprise-saas/SKILL.md) : architecture modulaire, permissions, sécurité, accessibilité, tests et livraison.
- [Frontend Next.js Enterprise SaaS](skills/frontend/nextjs/nextjs-enterprise-saas/SKILL.md) : architecture App Router, rendu serveur et client, cache, expérience produit, permissions, sécurité, pages publiques, accessibilité, performance, tests et déploiement lorsque le backend reste externe ou hors périmètre.
- [Next.js Fullstack Enterprise SaaS](skills/fullstack/nextjs/nextjs-fullstack-enterprise-saas/SKILL.md) : architecture de bout en bout, routes backend, contrats, données, transactions, migrations, tâches durables, intégrations, frontend, sécurité, exploitation et montée en charge.

Chaque skill conserve ses propres références, templates, scénarios et historique. Aucun template métier n’est centralisé à la racine.

## Utilisation

Lire [l’installation](docs/installation.md), puis [l’utilisation du dépôt](docs/repository-usage.md). Pour contribuer, appliquer [les règles de contribution](docs/contributing.md).

Chaque nouvelle session doit commencer par le prompt fourni avec le skill installé :

- [Démarrage du skill d’orchestration](skills/orchestration/ai-orchestrator-methodology/installation/installation.md)
- [Démarrage du skill frontend React et Vite](skills/frontend/react/react-vite-enterprise-saas/installation/installation.md)
- [Démarrage du skill frontend Next.js](skills/frontend/nextjs/nextjs-enterprise-saas/installation/installation.md)
- [Démarrage du skill Next.js fullstack](skills/fullstack/nextjs/nextjs-fullstack-enterprise-saas/installation/installation.md)

## Validation

Exécuter :

    python scripts/validate-all-skills.py

Le validateur contrôle la structure, les liens, les frontmatters et la reconstruction exacte des trois documents d’origine à partir de la nouvelle arborescence.

## Branche de travail

Les nouveaux travaux sont préparés et validés sur la branche `Draft` avant leur intégration dans `main`. La branche `skill-non-structurer` conserve l’état antérieur à la restructuration.
