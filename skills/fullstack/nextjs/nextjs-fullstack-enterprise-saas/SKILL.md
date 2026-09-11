---
name: nextjs-fullstack-enterprise-saas
description: Concevoir, développer, auditer ou faire évoluer une application Next.js fullstack professionnelle avec interface utilisateur, logique serveur, interfaces de programmation, données, intégrations, sécurité et déploiement. Utiliser ce skill lorsque Next.js porte à la fois le frontend et des responsabilités backend; utiliser un skill frontend lorsque le serveur reste entièrement externe.
metadata:
  title: Skill Next.js fullstack pour produit SaaS professionnel
  version: "1.0.0"
  language: fr
  status: stable
  intended_users:
    - coding-agents
    - human-developers
---

# Next.js fullstack pour produit SaaS professionnel

## Vocabulaire accessible

Dans ce skill :

- **fullstack** signifie que le même produit comprend l’interface utilisateur, les traitements serveur, les données et leur exploitation ;
- **SaaS** signifie un logiciel accessible comme un service et généralement partagé entre plusieurs organisations clientes isolées ;
- **frontend** désigne la partie visible et interactive utilisée dans le navigateur ;
- **backend** désigne les traitements exécutés sur le serveur ;
- **interface de programmation**, souvent abrégée API dans les standards externes, désigne un contrat permettant à un logiciel d’appeler une capacité ;
- **route du protocole web HTTP** désigne une adresse réseau associée à une méthode comme lecture, création, modification ou suppression ;
- **App Router** et **Pages Router** désignent les deux systèmes de routage proposés par différentes générations de Next.js ;
- **traitement serveur** désigne une fonction exécutée sur le serveur et appelée depuis l’application Next.js ;
- **gestionnaire de route** désigne le fichier Next.js qui reçoit une requête réseau sur une route ;
- **organisation cliente** désigne le périmètre métier isolé d’un client dans un produit partagé, souvent appelé tenant dans la documentation externe ;
- **transaction** désigne un ensemble de modifications qui doivent réussir ou être annulées ensemble ;
- **migration de données** désigne un changement versionné de la structure ou du contenu persistant ;
- **cache** désigne une copie temporaire destinée à accélérer une lecture ;
- **webhook** désigne un appel envoyé par un système externe pour signaler un événement ;
- **observabilité** désigne les journaux, mesures et traces permettant de comprendre le fonctionnement réel du système.

Employer ensuite les mots complets contrôlés par le projet. Un terme imposé par Next.js ou un protocole peut être conservé, mais sa responsabilité doit être expliquée à sa première utilisation.

## Statut normatif

- **DOIT** ou **TOUJOURS** : exigence obligatoire et vérifiable.
- **NE DOIT PAS** ou **INTERDIT** : comportement interdit.
- **DEVRAIT** : règle à suivre par défaut, sauf justification documentée.
- **PEUT** : possibilité autorisée lorsque le contexte la rend pertinente.

Une dérogation doit nommer la règle, expliquer la nécessité, évaluer le risque, identifier l’autorité qui l’accepte et prévoir son maintien ou sa correction.

## Portabilité entre agents de code

Les règles normatives résident dans `SKILL.md` et `references/`. Elles ne dépendent ni de Codex, ni d’un fournisseur de modèle, ni d’un service d’orchestration particulier.

Le fichier `agents/openai.yaml` est seulement un adaptateur facultatif de découverte. Un autre agent de code doit charger directement le dossier maître complet avec le mécanisme offert par son environnement.

## Navigation des ressources

Lire ce document complètement. Lire ensuite uniquement les références nécessaires à la tâche, sans remplacer leurs règles par le résumé présent ici :

- [Architecture fullstack et frontières](references/fullstack-architecture-and-boundaries.md) avant une décision de découpage, d’exécution ou d’extraction de service.
- [Organisation du dépôt et dépendances](references/repository-organization-and-dependencies.md) avant de créer, déplacer ou partager un dossier, un fichier, un module ou une fonctionnalité.
- [Nommage, types et code lisible](references/naming-types-and-readable-code.md) avant de créer ou renommer un symbole, un contrat, un fichier ou un dossier.
- [Interfaces backend et routes HTTP](references/backend-interfaces-and-http-routes.md) pour les gestionnaires de routes, contrats publics, versions, statuts, fichiers et requêtes externes.
- [Données, transactions et migrations](references/database-modeling-transactions-and-migrations.md) pour la persistance, les contraintes, la concurrence, les changements de schéma et les sauvegardes.
- [Authentification, permissions et isolation](references/authentication-permissions-and-organization-isolation.md) pour les sessions, rôles, politiques, ressources et organisations clientes.
- [Sécurité, validation et secrets](references/security-validation-and-secrets.md) pour toute entrée externe, donnée sensible, intégration, journal ou configuration.
- [Traitements serveur, formulaires et expérience utilisateur](references/server-actions-forms-and-user-experience.md) pour les mutations initiées par l’interface, les états, erreurs et retours d’action.
- [Cache, tâches différées et intégrations](references/cache-background-work-and-integrations.md) pour l’invalidation, les files de travail, événements, webhooks et services externes.
- [Rendu frontend, accessibilité et pages publiques](references/frontend-rendering-accessibility-and-public-pages.md) pour les composants serveur et navigateur, la navigation, les langues, les marques et les métadonnées.
- [Performance, observabilité, déploiement et montée en charge](references/performance-observability-deployment-and-scaling.md) pour les mesures, journaux, alertes, instances, déploiements et retours arrière.
- [Tests, livraison et évolution](references/testing-delivery-and-evolution.md) pour les preuves, migrations, compatibilité, audit et mise en production.
- [Installation et prompt obligatoire de démarrage](installation/installation.md) lors de l’installation et au début de chaque session.
- [Scénarios de validation](tests/scenarios.md) pour contrôler les décisions et l’évolution du skill.
- [Modèle de module fullstack](assets/templates/fullstack-module/template.md), [modèle de fonctionnalité fullstack](assets/templates/fullstack-feature/template.md), [modèle de route backend](assets/templates/backend-route/template.md), [modèle de changement de données](assets/templates/database-change/template.md), [modèle d’intégration externe](assets/templates/external-integration/template.md) et [modèle de rapport d’audit](assets/templates/audit-report.md) pour préparer des livrables vérifiables.

## Mission

L’agent doit produire un système cohérent de bout en bout, pas une juxtaposition de pages et de routes. Il doit :

- comprendre le besoin métier et le parcours complet avant de choisir une technologie ;
- organiser le code par domaines et capacités compréhensibles ;
- rendre visibles les frontières entre interface, transport réseau, cas d’usage, règles métier, données et intégrations ;
- maintenir les fichiers spéciaux de Next.js comme adaptateurs minces ;
- traiter chaque route HTTP et traitement serveur comme un point d’entrée potentiellement hostile ;
- appliquer les permissions et l’isolation au plus près des données ;
- préserver la cohérence par des contraintes de base de données et des transactions adaptées ;
- choisir explicitement la fraîcheur, le cache et l’invalidation ;
- distinguer un travail court après réponse d’une tâche durable ;
- concevoir les erreurs, chargements et résultats pour l’utilisateur et l’exploitation ;
- rendre le système testable, observable, déployable et capable d’évoluer sans réécriture générale ;
- communiquer les preuves réelles et les limites restantes.

## Priorités

En cas de conflit, appliquer cet ordre :

1. protection des données et des secrets ;
2. isolation des organisations clientes ;
3. autorisation et intégrité des opérations ;
4. absence de perte ou corruption de données ;
5. correction fonctionnelle ;
6. accessibilité et compréhension utilisateur ;
7. contrats compatibles et erreurs explicites ;
8. architecture et dépendances maîtrisées ;
9. capacité d’exploitation et de récupération ;
10. maintenabilité et évolutivité ;
11. performance mesurée ;
12. rapidité de livraison.

## Préparation obligatoire

Avant toute modification, l’agent doit :

1. lire les instructions applicables et vérifier l’état réel du dépôt ;
2. relever les versions de Next.js, React, TypeScript, de l’environnement JavaScript et du gestionnaire de paquets ;
3. identifier le système de routage, les modes d’exécution, la base de données, les outils de migration, les files de travail, les caches et les services externes ;
4. cartographier les routes, traitements serveur, modules métier, tables, permissions, organisations clientes et flux de données concernés ;
5. distinguer les contrats internes, les routes publiques et les intégrations entrantes ou sortantes ;
6. inspecter les garde-fous, tests, journaux, alertes, constructions et déploiements existants ;
7. identifier les changements présents qui n’appartiennent pas à la tâche ;
8. définir les résultats, erreurs, effets de bord, contraintes de concurrence, stratégie de retour et preuves attendues ;
9. vérifier la documentation correspondant aux versions réellement installées ;
10. choisir la plus petite modification cohérente avec l’architecture existante.

Ne pas migrer le routage, remplacer la base de données, introduire une file de travail, changer le mode d’hébergement ou extraire un service sans besoin démontré et plan de transition.

## Architecture obligatoire

Le chemin logique d’une opération doit rester lisible :

```text
Interface utilisateur ou consommateur externe
  -> adaptateur Next.js ou route HTTP
  -> cas d’usage de l’application
  -> règle du domaine
  -> accès aux données ou intégration externe
```

Les dépendances vont vers le domaine, jamais depuis le domaine vers Next.js, une base de données précise ou un fournisseur externe. Les adaptateurs convertissent les formats ; ils ne possèdent pas la politique métier.

### Choisir le bon point d’entrée

| Besoin | Choix par défaut |
|---|---|
| Lire une donnée pendant le rendu serveur | Appeler directement un cas d’usage serveur autorisé |
| Modifier une donnée depuis un formulaire de l’application | Traitement serveur protégé et limité à ce parcours |
| Exposer un contrat à une application externe | Gestionnaire de route HTTP documenté et versionné si nécessaire |
| Recevoir un événement externe | Gestionnaire de route vérifiant signature, répétition et schéma |
| Exécuter une opération longue ou devant survivre à un redémarrage | File de travail ou service de tâches durable |
| Partager le backend avec plusieurs produits indépendants | Évaluer un service backend séparé avec contrat explicite |

Ne pas appeler une route interne par le réseau depuis un composant serveur lorsque le cas d’usage peut être appelé directement. Ne pas utiliser un traitement serveur comme interface publique générale. Ne pas considérer la fonction `after` de Next.js comme une file de travail durable.

## Règles absolues

### L’agent DOIT toujours

- utiliser TypeScript strict et valider toute donnée externe à sa frontière ;
- appliquer les préfixes complets `Interface`, `Type` et `Enumeration` aux déclarations contrôlées par le projet ;
- utiliser des noms complets indiquant le domaine et la responsabilité ;
- rattacher chaque fonctionnalité et chaque route à un module métier propriétaire ;
- séparer le transport, les cas d’usage, le domaine, les données et les intégrations ;
- garder `page.tsx`, `layout.tsx`, `route.ts` et les traitements serveur minces ;
- vérifier authentification, autorisation, organisation et ressource côté serveur ;
- filtrer toute lecture et écriture par le périmètre d’organisation applicable ;
- retourner des objets limités aux champs nécessaires ;
- définir les contraintes et transactions qui protègent les invariants métier ;
- documenter chaque changement de schéma, compatibilité, retour et sauvegarde ;
- définir le contrat, les statuts, les limites et les erreurs de chaque route publique ;
- rendre les opérations répétées sûres lorsque le risque l’exige ;
- prévoir délai maximum, nouvelle tentative contrôlée et coupe-circuit pour une intégration fragile ;
- choisir la politique de cache et l’invalidation de chaque donnée mise en cache ;
- fournir chargement, absence, refus, erreur, succès et reprise ;
- mesurer la performance et rendre les opérations critiques observables ;
- exécuter les tests et constructions pertinents avant de conclure.

### L’agent NE DOIT JAMAIS

- placer toute l’application dans `app/`, `lib/`, `utils/`, `services/` ou un autre dossier générique ;
- importer Next.js, le client de base de données ou un fournisseur dans le domaine métier ;
- mettre la logique métier importante directement dans une route, une page ou un traitement serveur ;
- faire confiance à un identifiant d’utilisateur, d’organisation ou de ressource reçu du navigateur ;
- protéger une donnée uniquement en masquant l’interface ou en redirigeant dans une mise en page ;
- exposer une entité complète, un secret ou une erreur interne dans une réponse ;
- construire une requête de données non paramétrée depuis une entrée externe ;
- modifier plusieurs agrégats liés sans transaction ou stratégie de compensation démontrée ;
- exécuter une migration destructive sans sauvegarde, compatibilité et plan de retour ;
- mettre en cache une réponse privée dans une portée publique ou partagée ;
- effectuer silencieusement une tâche critique après la réponse sans garantie de livraison ;
- relancer automatiquement une opération non sûre ;
- accepter un webhook sans vérifier sa signature et sa répétition ;
- casser un contrat public sans version, migration des consommateurs et période de transition ;
- introduire une technologie parce qu’elle est populaire plutôt que nécessaire ;
- déclarer un contrôle exécuté sans preuve.

## Limite de Next.js comme backend

Next.js peut servir une couche backend proche de son frontend. L’agent doit toutefois évaluer un service séparé lorsque le système exige durablement :

- des connexions longues non supportées par l’hébergement ;
- des traitements lourds ou longs indépendants des requêtes ;
- une montée en charge très différente du frontend ;
- plusieurs consommateurs avec un cycle de version autonome ;
- une technologie serveur incompatible avec l’environnement choisi ;
- une disponibilité ou une isolation opérationnelle indépendante ;
- un grand domaine métier dont la responsabilité dépasse clairement l’application web.

Une extraction est une décision d’architecture, pas une amélioration automatique. Commencer par des frontières internes propres afin de rendre cette décision possible plus tard.

## Validation et clôture

Avant de déclarer la tâche terminée :

1. inspecter les différences et confirmer le périmètre ;
2. contrôler les dépendances entre couches et modules ;
3. exécuter TypeScript, règles de code, tests et construction de production ;
4. tester le parcours depuis l’entrée jusqu’à la donnée et le retour utilisateur ;
5. tester entrée invalide, session absente, permission refusée et accès croisé entre organisations ;
6. tester les contraintes, transactions, répétitions et migrations concernées ;
7. vérifier cache, invalidation, tâches différées et intégrations concernées ;
8. contrôler absence de secret et minimisation des réponses et journaux ;
9. vérifier accessibilité, pages publiques et performance lorsque concernées ;
10. confirmer la santé et le comportement du déploiement ciblé ;
11. déclarer les contrôles non exécutés et le risque restant.

La réponse finale doit nommer les fichiers modifiés, décisions, changements de contrat ou de données, preuves exécutées, limites et procédure de reprise utile.
