---
name: frontend-react-vite-enterprise-saas-modular-permission-driven
title: Skill Frontend React + TypeScript + Vite — Enterprise SaaS modulaire et Permission-Driven
description: >
  Skill normatif pour tout agent IA chargé de concevoir, développer, auditer,
  corriger, tester, sécuriser, optimiser, documenter ou faire évoluer une
  application frontend React + TypeScript + Vite professionnelle, SaaS-ready,
  multi-tenant, white-label, modulaire, responsive, accessible, portable,
  observable, maintenable, scalable et déployable dans tout environnement.
version: 1.1.0
language: fr
status: stable
owners:
  - Frontend Architecture
  - Product Engineering
applies_to:
  - new-project
  - existing-project
  - refactoring
  - feature-development
  - module-development
  - code-review
  - technical-audit
  - bug-fix
  - performance-optimization
  - security-hardening
  - saas-white-label
---
<!-- preserved-source-part-start: frontend-preamble -->

# SKILL FRONTEND REACT + TYPESCRIPT + VITE  
## Architecture Enterprise modulaire, SaaS, Multi-tenant, White-label et Permission-Driven

---

## 0. Statut normatif du document

Ce document est une **spécification opérationnelle obligatoire** destinée à être comprise et exécutée par un agent IA, un sous-agent IA, un développeur humain ou un système d’orchestration de développement.

Les termes suivants ont une valeur normative :

- **DOIT / TOUJOURS** : exigence obligatoire ;
- **NE DOIT PAS / INTERDIT** : interdiction absolue ;
- **DEVRAIT** : recommandation forte, sauf justification documentée ;
- **PEUT** : option autorisée lorsque le contexte le justifie.

L’agent ne doit jamais considérer ce document comme une simple liste de bonnes pratiques facultatives. Il doit s’en servir comme :

- cadre de décision ;
- grille d’audit ;
- contrat de réalisation ;
- norme de revue de code ;
- Definition of Done ;
- mécanisme de prévention des régressions.

Toute dérogation doit être :

1. explicitement identifiée ;
2. justifiée techniquement ;
3. évaluée en termes de risques ;
4. validée par le responsable technique ;
5. documentée avec une stratégie de correction ou de maintien.

---

<!-- preserved-source-part-end: frontend-preamble -->

## Navigation des ressources

Lire ce fichier complètement avant de modifier une application. Charger ensuite les références directement concernées :

- [Installation et prompt obligatoire de démarrage](installation/installation.md) à utiliser lors de l’installation du skill et au début de chaque nouvelle session.
- [Architecture](references/architecture.md) pour les modules, routes, composants, thèmes, données, configuration, déploiement, performance et observabilité.
- [Nommage et types](references/naming-and-types.md) avant de créer ou renommer un dossier, fichier, symbole ou type TypeScript.
- [Permissions](references/permissions.md) pour les modèles de protection, catalogues, politiques, routes, composants et actions.
- [Sécurité](references/security.md) pour l’authentification, les attaques par injection de script, les secrets et les dépendances.
- [Accessibilité](references/accessibility.md) pour le responsive, le zoom, le reflow, la sémantique interactive et les exigences d’accessibilité.
- [Tests et livraison](references/testing-and-delivery.md) pour l’intégration continue, la création, la validation, la définition de terminé et les audits.
- [Scénarios de test](tests/scenarios.md) pour choisir les niveaux et parcours de test.
- [Template de module](assets/templates/frontend-module/template.md) pour créer un module.
- [Template de feature](assets/templates/frontend-feature/template.md) pour créer une feature.
- [Template de rapport d’audit](assets/templates/audit-report.md) pour rendre compte du travail.

Lire plusieurs références lorsque la tâche traverse plusieurs responsabilités. Ne jamais remplacer une règle détaillée par un résumé de navigation.

<!-- preserved-source-part-start: frontend-section-1 -->
# 1. Mission de l’agent

L’agent agit comme un **expert Frontend senior de niveau architecture enterprise**.

Il doit être capable de :

- concevoir une architecture React hiérarchisée en application, modules et features ;
- développer des fonctionnalités robustes ;
- auditer une base de code ;
- détecter les anti-patterns ;
- sécuriser les flux frontend ;
- concevoir un design system ;
- implémenter un fonctionnement SaaS et white-label ;
- garantir la compatibilité multi-tenant ;
- assurer la portabilité multi-environnement ;
- optimiser les performances ;
- assurer une gestion exhaustive des erreurs ;
- garantir la qualité UX ;
- garantir le responsive et le reflow ;
- assurer l’accessibilité ;
- gérer le SEO des pages publiques ;
- créer une stratégie de tests ;
- documenter les décisions ;
- produire un compte rendu honnête et vérifiable.

L’objectif n’est jamais de produire uniquement une interface visuellement convaincante.

Une application n’est considérée comme professionnelle que si elle est :

- fonctionnelle ;
- claire ;
- cohérente ;
- structurée ;
- harmonisée ;
- maintenable ;
- testable ;
- portable ;
- configurable ;
- sécurisée ;
- accessible ;
- responsive ;
- observable ;
- évolutive ;
- scalable ;
- résiliente ;
- exploitable dans plusieurs environnements ;
- prête pour un usage SaaS.

---

<!-- preserved-source-part-end: frontend-section-1 -->

<!-- preserved-source-part-start: frontend-section-2 -->
# 2. Philosophie générale

## 2.1 Concevoir SaaS-ready dès l’origine

Toute application frontend doit être codée **comme si elle devait devenir un SaaS**, même si elle commence comme une application mono-client.

Cela signifie que l’application doit pouvoir évoluer vers :

- plusieurs tenants ;
- plusieurs organisations ;
- plusieurs domaines ;
- plusieurs marques ;
- plusieurs thèmes ;
- plusieurs logos ;
- plusieurs langues ;
- plusieurs fuseaux horaires ;
- plusieurs devises ;
- plusieurs plans ou licences ;
- plusieurs ensembles de fonctionnalités ;
- plusieurs modes de sécurité ;
- plusieurs environnements ;
- plusieurs configurations de déploiement.

L’ajout futur d’un backend multi-tenant ne doit pas exiger une réécriture complète du frontend.

## 2.2 Éviter la surconfiguration inutile

« Tout rendre paramétrable » ne signifie pas transformer chaque constante interne en paramètre administrable.

Doivent obligatoirement être configurables :

- les données dépendantes de l’environnement ;
- les données dépendantes du tenant ;
- les données de branding ;
- les fonctionnalités activables ;
- les paramètres métier variables ;
- les textes légaux ;
- les coordonnées de support ;
- les paramètres SEO publics ;
- les URLs externes ;
- les limites fonctionnelles susceptibles de varier.

Peuvent rester des constantes internes :

- les invariants techniques stables ;
- les identifiants internes du design system ;
- les valeurs nécessaires au fonctionnement du code et non destinées à varier par tenant ;
- les décisions architecturales validées.

L’agent doit distinguer **configuration utile** et **complexité artificielle**.

---

<!-- preserved-source-part-end: frontend-section-2 -->

<!-- preserved-source-part-start: frontend-section-3 -->
# 3. Ordre de priorité

En cas de conflit, appliquer cet ordre :

1. sécurité ;
2. protection des données ;
3. isolation des tenants ;
4. intégrité des données ;
5. correction fonctionnelle ;
6. accessibilité ;
7. gestion explicite des erreurs ;
8. compréhension utilisateur ;
9. cohérence architecturale ;
10. portabilité ;
11. maintenabilité ;
12. performance ;
13. harmonie UX/UI ;
14. rapidité de livraison.

Exemples :

- ne jamais sacrifier une permission backend pour simplifier l’interface ;
- ne jamais désactiver le zoom pour préserver une mise en page ;
- ne jamais masquer une erreur pour donner l’impression que l’action a réussi ;
- ne jamais stocker un secret dans le bundle pour faciliter le déploiement ;
- ne jamais introduire une dépendance lourde pour gagner quelques lignes.

---

<!-- preserved-source-part-end: frontend-section-3 -->

<!-- preserved-source-part-start: frontend-section-4 -->
# 4. Règles absolues

## 4.1 L’agent DOIT toujours

- analyser l’existant avant de modifier ;
- comprendre le besoin métier ;
- identifier les utilisateurs concernés ;
- identifier les permissions ;
- identifier le tenant ou périmètre actif ;
- identifier les états fonctionnels ;
- identifier les cas d’erreur ;
- utiliser TypeScript strict ;
- appliquer les préfixes de typage définis en section 11 à toute nouvelle déclaration de type appartenant au projet ;
- choisir pour les dossiers, fichiers et symboles des noms qui rendent immédiatement compréhensibles leur domaine et leur responsabilité ;
- organiser le code par modules puis par features ;
- rattacher toute feature à un module parent ;
- attribuer les permissions au niveau qui en est propriétaire : module ou feature ;
- appliquer les permissions métier aux routes, composants et actions API concernés ;
- respecter les frontières des modules ;
- utiliser le niveau de partage approprié : feature, `shared-module/` ou `shared/` global ;
- utiliser les composants partagés existants ;
- gérer tous les états asynchrones ;
- catcher toutes les erreurs aux frontières pertinentes ;
- normaliser les erreurs ;
- afficher des messages explicites ;
- journaliser les erreurs techniquement ;
- empêcher les doubles soumissions ;
- empêcher les boucles de requêtes ;
- annuler les requêtes obsolètes ;
- rendre l’interface responsive ;
- tester le zoom et le reflow ;
- utiliser des tokens de design ;
- externaliser la configuration ;
- garantir l’absence de hardcoding critique ;
- documenter les variables ;
- protéger routes, composants et actions ;
- considérer le backend comme autorité de sécurité ;
- écrire ou adapter les tests ;
- exécuter les contrôles disponibles ;
- déclarer honnêtement ce qui n’a pas été vérifié.

## 4.2 L’agent NE DOIT JAMAIS

- laisser un `catch` vide ;
- ignorer une Promise rejetée ;
- utiliser `console.log` comme unique gestion d’erreur ;
- afficher directement une stack trace ;
- afficher une erreur Axios brute ;
- afficher un message SQL, Java, Node ou infrastructure ;
- exposer un token ;
- exposer une clé ;
- exposer une donnée sensible ;
- considérer une variable `VITE_*` comme secrète ;
- coder en dur une URL d’API ;
- coder en dur un domaine de production ;
- coder en dur un tenant ;
- coder en dur un logo de marque dans les composants ;
- coder en dur des couleurs métier dans les composants ;
- dupliquer les codes de permission ;
- créer trois permissions techniques différentes pour une seule capacité métier ;
- stocker le catalogue des permissions métier dans `.env` ;
- laisser un appel API protégé sans politique d’autorisation déclarée ;
- déclencher une requête dans le rendu React ;
- placer une feature métier directement à la racine hors module ;
- importer les détails internes d’un autre module ;
- déplacer prématurément un élément métier dans le `shared/` global ;
- créer une boucle de `useEffect`;
- désactiver arbitrairement `react-hooks/exhaustive-deps`;
- utiliser `any` sans justification ;
- utiliser une abréviation, un acronyme, un sigle ou un préfixe réduit dans un nom contrôlé par le projet ;
- utiliser un nom vague ou générique qui empêche de comprendre directement le rôle métier ou technique de l’élément ;
- renommer ou réorganiser du code existant hors du périmètre demandé sous le seul prétexte d’appliquer une convention de nommage ;
- simuler un bouton avec un `div`;
- rendre un texte statique éditable ;
- appliquer `cursor: text` globalement ;
- désactiver le zoom ;
- utiliser `user-scalable=no`;
- utiliser `maximum-scale=1`;
- cacher un défaut de layout avec `overflow-x: hidden`;
- déclarer terminé un travail dont le build échoue ;
- déclarer terminé un travail sans gestion des erreurs ;
- déclarer terminé un écran non responsive ;
- protéger une action uniquement par masquage frontend ;
- introduire une bibliothèque sans évaluation ;
- créer un nouveau module sans responsabilité métier réelle ;
- transformer automatiquement chaque module en micro-frontend ;
- inventer l’exécution d’un test.

---

<!-- preserved-source-part-end: frontend-section-4 -->

<!-- preserved-source-part-start: frontend-section-5 -->
# 5. Processus obligatoire avant tout développement

## 5.1 Comprendre le besoin

L’agent doit identifier :

- l’objectif utilisateur ;
- la valeur métier ;
- les acteurs ;
- le module métier propriétaire ;
- les features concernées ;
- les droits ;
- les données ;
- les parcours ;
- les volumes ;
- les contraintes responsive ;
- les contraintes SEO ;
- les contraintes légales ;
- les contraintes de performance ;
- les environnements ;
- les dépendances externes.

## 5.2 Inspecter l’existant

Examiner au minimum :

- structure des dossiers ;
- modules existants ;
- manifestes et registre de modules ;
- frontières de dépendances ;
- configuration TypeScript ;
- configuration Vite ;
- package manager ;
- dépendances ;
- routes ;
- authentification ;
- permissions ;
- couche API ;
- design system ;
- composants ;
- thèmes ;
- configuration runtime ;
- tests ;
- CI ;
- documentation ;
- conventions de code.

## 5.3 Rechercher avant de recréer

Avant de créer un composant, hook, service ou utilitaire :

1. rechercher un équivalent ;
2. vérifier s’il est réutilisable ;
3. vérifier s’il peut être étendu ;
4. vérifier si l’extension ne crée pas une abstraction incorrecte ;
5. créer un nouvel élément uniquement lorsque nécessaire.

## 5.4 Définir les critères d’acceptation

Avant le code, définir :

- résultats attendus ;
- erreurs attendues ;
- permissions ;
- états de chargement ;
- comportement mobile ;
- comportement clavier ;
- comportement zoom ;
- contraintes SEO ;
- stratégie de tests.

---

<!-- preserved-source-part-end: frontend-section-5 -->

<!-- preserved-source-part-start: frontend-section-45 -->
# 45. Commande comportementale finale

Lorsqu’il utilise ce Skill, l’agent doit appliquer la règle suivante :

> Analyse d’abord le besoin et l’existant. Conçois toute interface en mode SaaS-ready, multi-tenant et white-label. Ne fige jamais le branding, les thèmes, les logos, les URLs ou les paramètres variables. Utilise des tokens sémantiques, des packages de thèmes clair, sombre, système et, si nécessaire, contraste élevé. Résous et valide la configuration du tenant de manière isolée. Préserve le SEO des pages publiques en fournissant les métadonnées tenant dans le HTML initial par SSR, SSG, pré-rendu, injection serveur ou edge lorsque l’indexation est importante. Respecte l’architecture application → modules → features, place les permissions globales dans `module-permissions/`, les permissions fonctionnelles dans `feature-permissions/`, et applique chaque permission métier aux routes, composants et actions API concernés. Utilise `shared-module/features/` pour les capacités partagées d’un module, `shared/features/` pour les fonctionnalités transversales et `shared/kernel/` pour l’infrastructure générique. Respecte les frontières de modules, les API publiques, TypeScript strict, le responsive, le zoom, l’accessibilité, la sécurité et la portabilité. Pour toute action asynchrone, affiche un loader adapté, empêche les doubles appels, annule les requêtes obsolètes, catche les erreurs aux frontières pertinentes, les normalise, les journalise sans données sensibles et affiche un message clair à l’utilisateur. N’ignore jamais une erreur. N’annonce jamais qu’une tâche est terminée sans contrôles et résultats vérifiables.

---

<!-- preserved-source-part-end: frontend-section-45 -->

<!-- preserved-source-part-start: frontend-section-48 -->
# 48. Conclusion normative

Le frontend doit être conçu comme un produit durable, pas comme une démonstration.

Le succès signifie que l’application :

- répond toujours à l’utilisateur ;
- explique toujours ses erreurs ;
- n’ignore aucun incident ;
- protège les actions ;
- respecte les tenants ;
- fonctionne sur tous les écrans ;
- ne force jamais le dézoom ;
- supporte les thèmes ;
- supporte le changement de marque ;
- change globalement à partir d’une configuration ;
- ne dépend pas d’un environnement ;
- ne contient aucun secret ;
- ne nécessite pas une réécriture pour devenir SaaS ;
- conserve un SEO correct pour les pages publiques ;
- peut être testée ;
- peut être observée ;
- peut être maintenue ;
- possède au moins un module métier explicite ;
- peut ajouter de nouveaux modules sans restructuration globale ;
- isole les features et les partages à leur niveau approprié ;
- rattache chaque permission à son module ou à sa feature propriétaire ;
- applique les mêmes capacités métier aux routes, composants et actions API correspondants ;
- distingue les shared features du kernel technique ;
- peut évoluer sans perdre sa cohérence.

**Toute implémentation contraire à ces principes doit être corrigée ou explicitement justifiée.**
<!-- preserved-source-part-end: frontend-section-48 -->
