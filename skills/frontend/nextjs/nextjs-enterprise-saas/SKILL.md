---
name: nextjs-enterprise-saas
description: Concevoir, développer, auditer ou faire évoluer un produit Next.js et TypeScript professionnel, modulaire, sécurisé, accessible, multi-organisation, personnalisable par marque et déployable sur plusieurs infrastructures. Utiliser ce skill pour une application Next.js existante ou nouvelle; ne pas l’utiliser pour une application React sans Next.js.
metadata:
  title: Skill Next.js et TypeScript pour produit SaaS professionnel
  version: "1.0.0"
  language: fr
  status: stable
  intended_users:
    - coding-agents
    - human-developers
---

# Next.js et TypeScript pour produit SaaS professionnel

## Statut normatif

Ce skill constitue une spécification opérationnelle destinée aux agents d’intelligence artificielle, aux développeurs et aux systèmes d’orchestration qui travaillent sur une application Next.js.

Les mots suivants indiquent le niveau d’obligation :

- **DOIT** ou **TOUJOURS** : exigence obligatoire et vérifiable ;
- **NE DOIT PAS** ou **INTERDIT** : comportement interdit ;
- **DEVRAIT** : règle à suivre par défaut, sauf justification documentée ;
- **PEUT** : possibilité autorisée lorsque le contexte la rend pertinente.

Une dérogation doit identifier la règle concernée, expliquer sa raison, évaluer son risque, indiquer qui l’a autorisée et prévoir son maintien ou sa correction.

## Portabilité entre agents de code

Les règles normatives se trouvent uniquement dans `SKILL.md` et `references/`. Elles ne dépendent ni de Codex, ni d’un fournisseur de modèle, ni d’un outil d’orchestration particulier.

Le fichier `agents/openai.yaml` est un adaptateur facultatif de découverte et d’affichage pour les environnements qui reconnaissent ce format. Il n’ajoute, ne remplace et ne limite aucune règle. Un autre agent de code doit utiliser directement le dossier maître complet selon son propre mécanisme de chargement.

L’absence d’une fonction propre à une plateforme ne dispense pas l’agent d’appliquer la règle. Il doit utiliser un contrôle équivalent disponible ou déclarer clairement l’impossibilité et le risque restant.

## Navigation des ressources

Lire ce fichier complètement avant toute modification. Lire ensuite les ressources qui correspondent réellement à la tâche :

- [Installation et prompt obligatoire de démarrage](installation/installation.md) au moment de l’installation et au début de chaque nouvelle session.
- [Architecture modulaire](references/architecture.md) avant de créer ou déplacer un module, une fonctionnalité, une route ou une responsabilité partagée.
- [Routage, rendu et cache](references/routing-rendering-and-cache.md) pour l’App Router, les composants serveur et client, les traitements serveur, les gestionnaires de routes, le chargement progressif et l’invalidation du cache.
- [Nommage compréhensible et types](references/naming-and-types.md) avant de créer ou renommer un dossier, un fichier, un symbole ou une déclaration TypeScript.
- [Permissions](references/permissions.md) pour l’authentification, l’autorisation, les organisations clientes, les routes, les traitements serveur et l’interface.
- [Sécurité](references/security.md) pour les secrets, les données sensibles, les entrées externes, les en-têtes, les journaux et les dépendances.
- [Interface produit et expérience utilisateur](references/product-interface-and-user-experience.md) pour les pages, composants, mises en page, navigations, listes, dialogues, retours d’action et aides intégrées.
- [Données, état, formulaires et erreurs](references/data-state-forms-and-errors.md) pour choisir l’autorité d’une information, gérer les lectures, soumissions, demandes concurrentes, erreurs et traitements différés.
- [Pages publiques, métadonnées et internationalisation](references/public-pages-metadata-and-internationalization.md) pour l’indexation, les domaines, les marques, les images de partage, les plans de site, les langues et le formatage local.
- [Accessibilité](references/accessibility.md) pour les tailles d’écran, le zoom, le clavier, la navigation, les titres et les annonces de changement de page.
- [Performance, observabilité et exploitation](references/performance-observability-and-operations.md) pour les mesures, le code navigateur, les images, les scripts, les journaux, la santé, la construction et les modes de déploiement.
- [Tests et livraison](references/testing-and-delivery.md) pour les contrôles automatisés, les audits, la construction de production et le déploiement.
- [Scénarios de validation](tests/scenarios.md) lors d’une évolution du skill ou pour vérifier une décision difficile.
- [Modèle de module](assets/templates/frontend-module/template.md), [modèle de fonctionnalité](assets/templates/frontend-feature/template.md) et [modèle de rapport d’audit](assets/templates/audit-report.md) pour produire des livrables cohérents.

Ne jamais remplacer une règle détaillée par le seul résumé présent dans ce fichier.

## Mission de l’agent

L’agent doit concevoir ou maintenir un produit durable, et non une démonstration visuelle. Il doit notamment :

- comprendre le besoin métier avant de choisir l’architecture ;
- identifier l’organisation cliente active, les utilisateurs, les permissions et les données sensibles ;
- distinguer clairement ce qui s’exécute sur le serveur de ce qui s’exécute dans le navigateur ;
- organiser le métier en modules et fonctionnalités aux responsabilités compréhensibles ;
- garder les fichiers spéciaux de Next.js concentrés sur le routage, la composition et les frontières du framework ;
- traiter chaque traitement serveur et chaque gestionnaire de route comme une entrée accessible par le réseau ;
- empêcher toute fuite de secret ou de donnée privée vers le code envoyé au navigateur ;
- choisir explicitement la stratégie de rendu, de cache et d’invalidation ;
- concevoir les parcours, formulaires, listes et retours d’action à partir du travail réel de l’utilisateur ;
- définir une seule autorité pour chaque information et traiter séparément les erreurs attendues et inattendues ;
- produire des pages publiques correctement indexables, localisées et isolées par marque lorsque le produit l’exige ;
- produire une interface accessible, adaptable aux tailles d’écran et utilisable au clavier ;
- mesurer la performance et rendre les erreurs de production observables sans exposer de donnée sensible ;
- tester les parcours, les permissions, les erreurs, le rendu et le déploiement réel ;
- rendre compte honnêtement des contrôles exécutés et de ceux qui ne l’ont pas été.

## Ordre de priorité

En cas de conflit, appliquer cet ordre :

1. sécurité et protection des données ;
2. isolation des organisations clientes ;
3. intégrité des données et autorisations serveur ;
4. correction fonctionnelle ;
5. accessibilité et compréhension utilisateur ;
6. gestion explicite des erreurs ;
7. cohérence architecturale ;
8. portabilité et capacité de déploiement ;
9. maintenabilité ;
10. performance mesurée ;
11. harmonie de l’expérience utilisateur ;
12. rapidité de livraison.

Ne jamais sacrifier une autorisation serveur, une protection de donnée, le zoom, une preuve de test ou une erreur visible pour simplifier l’implémentation.

## Préparation obligatoire

Avant toute modification, l’agent doit :

1. lire les instructions applicables au projet et vérifier l’état réel du dépôt ;
2. relever la version installée de Next.js, de React, de TypeScript et du gestionnaire de paquets ;
3. déterminer si le projet utilise l’App Router, le Pages Router ou une coexistence temporaire des deux ;
4. inspecter `next.config.*`, `package.json`, `tsconfig.json`, les règles de contrôle de code, les variables d’environnement documentées, les tests et le déploiement ;
5. cartographier les routes, modules, fonctionnalités, frontières serveur et client, sources de données, permissions et caches concernés ;
6. identifier les modifications existantes qui n’appartiennent pas à la tâche ;
7. définir les résultats attendus, les erreurs, les états de chargement, les autorisations, les tailles d’écran, les exigences d’indexation et les preuves ;
8. lire les documents officiels correspondant à la version installée avant d’utiliser une fonction dont le comportement dépend de la version ;
9. choisir une modification limitée au périmètre demandé ;
10. annoncer ce qui sera vérifié avant de commencer.

Ne pas migrer automatiquement un Pages Router existant vers l’App Router, activer une fonction expérimentale, modifier le mode de rendu ou changer la stratégie de déploiement sans besoin démontré.

## Règles absolues

### L’agent DOIT toujours

- employer TypeScript strict et valider les données externes au moment où elles entrent dans le système ;
- utiliser des noms complets qui indiquent le domaine et la responsabilité ;
- appliquer `Interface`, `Type` et `Enumeration` comme préfixes écrits en toutes lettres pour les déclarations contrôlées par le projet ;
- rattacher chaque fonctionnalité à un module métier propriétaire ;
- exposer les capacités d’un module par une interface publique limitée ;
- utiliser les composants serveur de React par défaut et justifier chaque frontière `use client` ;
- maintenir les secrets, accès directs aux données et règles d’autorisation dans des modules exclusivement serveur ;
- vérifier l’authentification et l’autorisation dans chaque traitement serveur, gestionnaire de route ou accès sensible concerné ;
- dériver l’organisation cliente depuis une source serveur vérifiée et contrôler son accès ;
- choisir et documenter la politique de cache de toute donnée métier ;
- invalider précisément les données après une modification ;
- fournir des interfaces de chargement, d’absence, d’erreur, de refus et de succès ;
- rendre chaque action observable, préserver les saisies après une erreur récupérable et traiter les demandes concurrentes ;
- utiliser les fichiers spéciaux de Next.js selon leur responsabilité officielle ;
- produire des métadonnées descriptives pour les pages publiques et des titres distincts pour la navigation accessible ;
- isoler les pages, métadonnées, traductions et images de partage selon la langue, le domaine et la marque ;
- empêcher les doubles soumissions et rendre les traitements répétés sûrs lorsque le risque le justifie ;
- utiliser les composants, styles et conventions déjà présents avant d’en créer de nouveaux ;
- exécuter les contrôles pertinents et communiquer leurs résultats réels.

### L’agent NE DOIT JAMAIS

- considérer le masquage d’un bouton ou une redirection d’interface comme une autorisation suffisante ;
- faire confiance à un identifiant d’organisation cliente reçu du navigateur sans vérification serveur ;
- exposer un secret dans une variable accessible au navigateur, une propriété de composant client, le code HTML, une réponse ou un journal ;
- supposer qu’un traitement serveur est privé parce qu’il n’est appelé que depuis un composant connu ;
- placer une logique métier importante directement dans `page.tsx`, `layout.tsx`, `route.ts` ou un fichier d’interception de requête ;
- ajouter `use client` à un grand sous-arbre pour contourner une difficulté de conception ;
- mettre en cache globalement une donnée dépendante de l’utilisateur, de la session ou de l’organisation sans clé d’isolation démontrée ;
- utiliser une invalidation générale lorsqu’une invalidation ciblée fiable est disponible ;
- appeler une interface de programmation interne par le réseau depuis un composant serveur lorsque la fonction serveur autorisée peut être appelée directement ;
- ignorer une promesse rejetée, laisser un traitement d’erreur vide ou afficher une erreur d’infrastructure brute ;
- dupliquer une même donnée comme autorité indépendante dans l’adresse, le serveur et plusieurs états du navigateur ;
- afficher une réussite définitive avant confirmation serveur lorsque l’échec présente un risque important ;
- utiliser un nom abrégé, un préfixe réduit ou un dossier générique comme `misc`, `helpers` ou `utils` sans domaine explicite ;
- désactiver le zoom, masquer un débordement pour cacher une mise en page cassée ou simuler un bouton avec un élément non interactif ;
- introduire une dépendance, une fonction expérimentale ou une configuration d’hébergement sans évaluation ;
- déclarer le travail terminé lorsque le contrôle TypeScript, les tests nécessaires ou la construction de production échouent ;
- inventer l’exécution d’un contrôle.

## Invariants propres à Next.js

- Les pages et mises en page de l’App Router sont des composants serveur par défaut.
- Une directive `use client` définit une frontière de code livré au navigateur; tout ce qui traverse cette frontière doit être sérialisable et non sensible.
- Un traitement serveur exporté et un gestionnaire de route doivent être protégés comme des points d’entrée réseau.
- Un contrôle effectué dans une mise en page ne remplace pas un contrôle d’autorisation au plus près de la donnée ou de la modification.
- Le comportement du cache dépend de la version et de la configuration; l’agent doit inspecter le projet au lieu de supposer un comportement par défaut.
- Une donnée personnalisée par utilisateur ou organisation cliente ne doit jamais être partagée entre plusieurs contextes par un cache mal isolé.
- Les métadonnées statiques ou générées appartiennent aux composants serveur et doivent respecter la marque, la langue et la route réellement actives.
- Un déploiement sur plusieurs instances doit coordonner les caches, les invalidations et les identifiants de version lorsque les fonctions utilisées l’exigent.

## Validation et clôture

Avant de déclarer la tâche terminée, l’agent doit :

1. inspecter les différences produites et confirmer le périmètre ;
2. exécuter le contrôle TypeScript, le contrôle de code, les tests pertinents et la construction de production disponibles ;
3. vérifier au moins un parcours réel pour tout changement de route, de rendu, de traitement serveur ou de permission ;
4. contrôler les états de chargement, d’erreur, d’absence et de refus concernés ;
5. vérifier l’absence de secret, de donnée sensible et de mélange entre organisations clientes ;
6. contrôler le clavier, le zoom et les tailles d’écran lorsqu’une interface est modifiée ;
7. vérifier les formulaires, demandes concurrentes, erreurs et retours d’action concernés ;
8. vérifier le contenu initial, les métadonnées, les langues et les marques lorsqu’une page publique change ;
9. mesurer l’effet sur le navigateur ou le serveur lorsqu’une dépendance, une frontière client ou une stratégie de chargement change ;
10. confirmer que les journaux et mesures nécessaires existent sans contenir de donnée sensible ;
11. déclarer les contrôles non exécutés et le risque restant.

La réponse finale doit indiquer les fichiers modifiés, les décisions importantes, les résultats de contrôle et les limites. Un résultat sans preuve ne doit pas être présenté comme validé.
