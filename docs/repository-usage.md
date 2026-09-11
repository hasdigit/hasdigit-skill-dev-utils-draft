# Utilisation et organisation du dépôt

## Principe de propriété

Tout ce qui appartient à une compétence reste dans son dossier. Une référence, un template ou un scénario n’est placé dans un espace partagé que lorsqu’il est réellement commun à plusieurs skills et possède une responsabilité clairement définie.

## Lecture progressive

Le fichier `SKILL.md` contient le cadre essentiel et indique précisément quelle référence lire selon la tâche. Les fichiers de `references/` contiennent les règles détaillées. Les fichiers de `assets/templates/` sont destinés à être copiés ou adaptés dans un livrable. Les fichiers de `tests/` contrôlent le comportement et la conservation du contenu.

## Skills actuellement disponibles

| Domaine | Unité autonome |
|---|---|
| Orchestration d’agents d’intelligence artificielle | `skills/orchestration/ai-orchestrator-methodology/` |
| Frontend React et Vite | `skills/frontend/react/react-vite-enterprise-saas/` |
| Frontend d’une application Next.js | `skills/frontend/nextjs/nextjs-enterprise-saas/` |
| Application Next.js fullstack avec backend | `skills/fullstack/nextjs/nextjs-fullstack-enterprise-saas/` |

## Correspondance avec les anciens documents

| Ancien document | Nouvelle unité |
|---|---|
| Méthode de travail de l’agent orchestrateur | `skills/orchestration/ai-orchestrator-methodology/` |
| Skill frontend React, TypeScript et Vite | `skills/frontend/react/react-vite-enterprise-saas/` |
| Instructions générales du README | Ce document et le nouveau `README.md` |

Les manifestes `tests/content-preservation.json` décrivent où chaque partie d’origine a été déplacée. Le validateur reconstruit les documents dans leur ordre initial et compare leurs empreintes Git.

## Contenu historique du README original

Le bloc suivant conserve exactement le README antérieur pour garantir qu’aucune information source ne disparaît. Les instructions actuelles se trouvent dans les sections précédentes.

<!-- preserved-source-part-start: repository-original-readme -->
# skill-dev-utils-draft
is the skill Draft to formalise and save to use


Un **Skill** est un ensemble de règles, de standards et de méthodologies de travail prédéfinis qui permettent d’orienter un agent IA.

L’objectif est d’éviter que l’agent travaille uniquement selon sa propre logique ou ses habitudes par défaut. Il doit au contraire respecter la méthodologie, les conventions techniques, les règles d’architecture et les bonnes pratiques que nous avons définies pour le projet.

### Mise en place

Dans la codebase du projet, créez un dossier dédié :

```text
SKILL-DEV-AGENT/
```

Puis placez à l’intérieur le fichier Skill :

```text
SKILL-DEV-AGENT/
└── SKILL_FRONTEND_REACT_VITE_ENTERPRISE_SAAS_V1.1.md
```

Ce fichier contient l’ensemble des règles et de la méthodologie que l’agent IA doit appliquer pendant le développement du frontend React/Vite de notre application SaaS Enterprise.

### Utilisation

À chaque fois que vous démarrez une **nouvelle session avec l’agent IA**, la première instruction doit lui demander de lire et charger entièrement le Skill avant de commencer le travail.

Il faut également lui préciser que ce Skill constitue la référence méthodologique principale de la session et qu’il doit continuer à l’appliquer pendant toute la durée du travail.

### Exemple de prompt de démarrage de session

```text
Avant de commencer toute tâche sur ce projet, lis intégralement le fichier suivant :

SKILL-DEV-AGENT/SKILL_FRONTEND_REACT_VITE_ENTERPRISE_SAAS_V1.1.md

Charge et assimile l’ensemble des règles, standards, conventions, principes d’architecture et méthodologies qui y sont définis.

À partir de maintenant, considère ce Skill comme la référence principale pour toutes les tâches de développement frontend réalisées dans cette session.

Pour chaque analyse, proposition d’architecture, création de composant, modification de code, refactoring ou revue de code :

1. respecte les règles définies dans ce Skill ;
2. vérifie que ta proposition est cohérente avec son architecture et ses conventions ;
3. ne contourne pas une règle du Skill sans le signaler explicitement ;
4. si une demande entre en contradiction avec le Skill, indique clairement la contradiction avant de proposer une solution ;
5. privilégie systématiquement les standards du Skill par rapport à tes habitudes ou choix par défaut ;
6. conserve ces instructions comme contexte de travail pendant toute la session.

Avant de commencer la première tâche, confirme simplement que tu as lu et compris le Skill, puis applique-le à toutes les tâches suivantes.
```

Ainsi, l’agent ne travaille pas simplement « comme il veut » : il travaille à l’intérieur du cadre d’ingénierie que nous avons défini pour le projet.

<!-- preserved-source-part-end: repository-original-readme -->
