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

# 6. Choix obligatoire du modèle de protection

Si le projet ne documente pas son modèle d’autorisation, l’agent doit demander ou faire valider le choix.

## 6.1 Modèles possibles

### A. Privilèges fins

- permission de route ;
- permission de composant ;
- permission d’action ;
- permission d’appel API ;
- permission de champ ;
- permission par ressource ;
- permission par périmètre.

### B. Rôles

- rôle simple ;
- rôle organisationnel ;
- groupe de rôles.

### C. Hybride recommandé

- rôles pour regrouper les responsabilités ;
- privilèges pour les actions fines ;
- scopes pour le tenant, l’organisation, le projet ou la ressource ;
- attributs pour les décisions contextuelles.

### D. ABAC

Décision fondée sur :

- attributs utilisateur ;
- attributs ressource ;
- tenant ;
- organisation ;
- contexte ;
- heure ;
- propriété ;
- statut.

## 6.2 Comportement par défaut

Si une décision temporaire est indispensable :

- appliquer le modèle hybride ;
- utiliser le principe du moindre privilège ;
- marquer l’hypothèse ;
- demander validation avant production.

## 6.3 Sécurité réelle

Le frontend :

- masque ;
- désactive ;
- explique ;
- oriente.

Le backend :

- autorise ;
- refuse ;
- contrôle le scope ;
- garantit l’isolation ;
- journalise.

Le frontend ne doit jamais être l’unique barrière de sécurité.

---

# 7. Stack de référence

La stack de référence est :

- React ;
- TypeScript ;
- Vite ;
- React Router ;
- React Hook Form ;
- Zod ;
- Tailwind CSS ou système CSS validé ;
- Axios ou Fetch encapsulé ;
- TanStack Query pour le server-state significatif ;
- Vitest ;
- React Testing Library ;
- MSW ;
- Playwright ;
- axe-core.

Les versions doivent être définies dans le projet, pas figées dans ce Skill.

L’agent doit :

- respecter les versions installées ;
- vérifier les migrations ;
- éviter les APIs dépréciées ;
- consulter la documentation officielle en cas d’incertitude ;
- ne pas mettre à jour une dépendance majeure sans analyse.

---

# 8. Architecture modulaire orientée domaines, features et permissions

## 8.1 Principe architectural obligatoire

Toute application doit être organisée selon la hiérarchie suivante :

```text
Application
└── Modules métier ou fonctionnels
    ├── Permissions propres au module
    ├── Features
    │   └── Permissions propres à chaque feature
    └── Shared propre au module
        ├── Shared features du module
        └── Primitives partagées du module
```

Même lorsqu’une application ne possède initialement qu’un seul grand domaine fonctionnel, elle doit disposer d’au moins **un module explicitement nommé**.

Le module est le parent architectural de la feature.

Une feature ne doit pas être placée directement à la racine de l’application.

Cette organisation doit permettre :

- d’ajouter de nouveaux modules sans restructuration globale ;
- de conserver des domaines métier isolés ;
- de rattacher clairement chaque permission à son propriétaire ;
- de distinguer les permissions globales d’un module de celles de ses features ;
- de charger, tester, activer ou désactiver les modules indépendamment ;
- de contrôler les dépendances ;
- d’améliorer la compréhension par les agents IA et les équipes ;
- de scaler en volume de code, en organisation et en fonctionnalités.

## 8.2 Définition d’un module

Un module est un grand domaine métier, fonctionnel ou produit disposant :

- d’un nom explicite ;
- d’une responsabilité délimitée ;
- de permissions d’accès ou d’administration propres au module ;
- de ses features ;
- de ses éléments partagés internes ;
- de ses routes ;
- de sa navigation ;
- de ses contrats publics ;
- de ses providers éventuels ;
- de ses traductions ;
- de ses tests ;
- de sa documentation ;
- de son manifeste ;
- de son API publique.

Exemples :

- `module-administration` ;
- `module-identity-access` ;
- `module-billing` ;
- `module-project-management` ;
- `module-customer-portal` ;
- `module-reporting`.

Un module doit représenter un bounded context ou un périmètre fonctionnel réel.

Sont interdits les noms imprécis :

- `module-main` ;
- `module-general` ;
- `module-misc` ;
- `module-other` ;
- `module-utils`.

## 8.3 Convention de nommage

### Module

```text
module-<nom-du-module>
```

Exemples :

```text
module-billing
module-identity-access
module-project-management
```

### Feature

```text
<nom-de-la-feature>
```

Exemples :

```text
invoices
payments
organization-users
api-key-management
```

### Permissions

```text
module-permissions/
feature-permissions/
```

Les noms doivent :

- être en minuscules ;
- utiliser des tirets ;
- refléter le domaine métier ;
- rester stables ;
- éviter le nom d’une technologie.

## 8.4 Structure globale recommandée

```text
src/
├── app/
│   ├── bootstrap/
│   ├── error-boundaries/
│   ├── layouts/
│   ├── module-registry/
│   ├── providers/
│   ├── router/
│   └── App.tsx
│
├── modules/
│   ├── module-administration/
│   │   ├── module-permissions/
│   │   ├── features/
│   │   ├── shared-module/
│   │   ├── config/
│   │   ├── contracts/
│   │   ├── i18n/
│   │   ├── navigation/
│   │   ├── providers/
│   │   ├── routes/
│   │   ├── tests/
│   │   ├── module.manifest.ts
│   │   ├── index.ts
│   │   └── README.md
│   │
│   └── module-billing/
│       ├── module-permissions/
│       ├── features/
│       ├── shared-module/
│       ├── config/
│       ├── contracts/
│       ├── i18n/
│       ├── navigation/
│       ├── providers/
│       ├── routes/
│       ├── tests/
│       ├── module.manifest.ts
│       ├── index.ts
│       └── README.md
│
├── shared/
│   ├── features/
│   ├── kernel/
│   ├── design-system/
│   ├── config/
│   ├── i18n/
│   ├── seo/
│   ├── types/
│   └── utils/
│
├── assets/
├── styles/
├── test/
├── main.tsx
└── vite-env.d.ts
```

## 8.5 Cas d’une application à module unique

Une application à module unique doit tout de même adopter la structure modulaire.

```text
src/
├── modules/
│   └── module-customer-portal/
│       ├── module-permissions/
│       ├── features/
│       ├── shared-module/
│       ├── module.manifest.ts
│       └── index.ts
└── shared/
```

Il est interdit de déplacer les features directement sous `src/features/` sous prétexte que l’application est encore petite.

## 8.6 Structure complète d’un module

```text
src/modules/module-<module-name>/
├── module-permissions/
│   ├── <module>.module-permissions.ts
│   ├── <module>.module-policies.ts
│   ├── <module>.module-permission-manifest.ts
│   └── index.ts
│
├── features/
│   ├── <feature-a>/
│   └── <feature-b>/
│
├── shared-module/
│   ├── features/
│   ├── components/
│   ├── hooks/
│   ├── schemas/
│   ├── services/
│   ├── state/
│   ├── types/
│   └── utils/
│
├── config/
├── contracts/
├── i18n/
├── navigation/
├── providers/
├── routes/
├── tests/
├── module.manifest.ts
├── index.ts
└── README.md
```

Créer uniquement les dossiers réellement nécessaires, à l’exception des dossiers structurants imposés par le projet.

## 8.7 Structure complète d’une feature

```text
src/modules/module-<module-name>/features/<feature-name>/
├── feature-permissions/
│   ├── routes/
│   │   └── <feature>.route-policies.ts
│   ├── components/
│   │   └── <feature>.component-policies.ts
│   ├── api-actions/
│   │   └── <feature>.api-policies.ts
│   ├── <feature>.permissions.ts
│   ├── <feature>.permission-manifest.ts
│   └── index.ts
│
├── api/
│   ├── <feature>.api.ts
│   ├── <feature>.queries.ts
│   └── <feature>.mutations.ts
├── components/
├── hooks/
├── pages/
├── routes/
├── schemas/
├── services/
├── state/
├── types/
├── utils/
├── tests/
├── index.ts
└── README.md
```

## 8.8 Les niveaux de partage

### Niveau 1 — Privé à une feature

Un élément utilisé uniquement par une feature reste dans cette feature.

```text
modules/module-billing/features/invoices/components/InvoiceLineEditor.tsx
```

### Niveau 2 — Shared feature du module

Une véritable capacité fonctionnelle réutilisée par plusieurs features du même module va dans :

```text
modules/module-billing/shared-module/features/
```

Exemples :

- `billing-account-selector` ;
- `payment-method-selector` ;
- `billing-period-management`.

Une shared feature peut posséder :

- API ;
- composants ;
- hooks ;
- permissions ;
- services ;
- types ;
- tests ;
- manifeste.

### Niveau 3 — Primitive partagée du module

Un élément simple, technique ou de faible portée commun au module reste directement dans :

```text
shared-module/components/
shared-module/hooks/
shared-module/types/
shared-module/utils/
```

Il ne faut pas transformer artificiellement chaque composant partagé en feature.

### Niveau 4 — Shared feature globale

Une véritable fonctionnalité réutilisée par plusieurs modules va dans :

```text
src/shared/features/
```

Exemples :

- notifications ;
- file management ;
- global search ;
- help center ;
- user preferences.

Chaque shared feature globale suit la même discipline qu’une feature métier et peut posséder son propre `feature-permissions/`.

### Niveau 5 — Kernel global

Les capacités techniques fondamentales vont dans :

```text
src/shared/kernel/
```

Structure recommandée :

```text
shared/kernel/
├── api/
├── auth/
├── errors/
├── observability/
├── permissions/
├── routing/
├── storage/
└── tenancy/
```

Le kernel ne contient pas de règles métier propres à un module.

### Niveau 6 — Design system global

Les primitives visuelles vont dans :

```text
src/shared/design-system/
```

Exemples :

- Button ;
- Modal ;
- Input ;
- Table ;
- Toast ;
- tokens ;
- thèmes ;
- providers visuels.

Le design system n’est pas une feature métier.

## 8.9 Règle de promotion

La promotion suit cet ordre :

```text
feature privée
→ shared-module primitive ou shared-module feature
→ shared feature globale
→ kernel global uniquement si la capacité est technique et universelle
```

Un élément ne doit jamais être placé immédiatement dans `shared/` sans analyse.

Une duplication temporaire limitée peut être préférable à une abstraction globale prématurée.

## 8.10 Matrice obligatoire des dépendances

| Source | Peut importer | Ne peut pas importer |
|---|---|---|
| `app/` | API publiques des modules, shared features, kernel, design system | détails internes des modules |
| `shared/kernel/` | autres éléments du kernel autorisés | modules, features métier |
| `shared/design-system/` | tokens, primitives techniques autorisées | modules, features métier |
| `shared/features/` | kernel, design system, autres API publiques explicitement autorisées | internes des modules |
| `module-permissions/` | kernel permissions, contrats du module, manifestes publics de features | composants internes des features |
| `shared-module/` | kernel, design system, contrats du module | internes des features, autres modules |
| feature | kernel, design system, shared-module, shared features, contrats publics autorisés | internes d’une autre feature ou d’un autre module |
| API publique d’un module | contrats et façades explicitement exportés | détails internes non exportés |

Règle fondamentale :

> Une couche de niveau inférieur ne doit jamais dépendre d’une couche métier de niveau supérieur.

## 8.11 Communications entre features du même module

Une feature ne doit pas importer directement les fichiers internes d’une autre feature.

Options autorisées :

1. utiliser l’API publique de la feature ;
2. promouvoir l’élément vers `shared-module/` ;
3. utiliser un service d’orchestration du module ;
4. utiliser un contrat ou événement interne documenté.

## 8.12 Communications entre modules

Un module ne doit jamais importer les détails internes d’un autre module.

Mécanismes autorisés :

- API publique du module ;
- contrat TypeScript stable ;
- événement applicatif typé ;
- route documentée ;
- orchestration dans `app/` ;
- backend comme point de synchronisation.

## 8.13 API publique d’un module

Chaque module expose uniquement ce qui est nécessaire via son `index.ts`.

```ts
export { billingModuleManifest } from './module.manifest';
export { BILLING_MODULE_PERMISSIONS } from './module-permissions';
export { InvoiceSelector } from './features/invoices';
export type { InvoiceReference } from './contracts/invoice-reference';
```

Il est interdit de réexporter automatiquement tout le contenu du module.

## 8.14 Manifeste de module

```ts
export interface InterfaceApplicationModuleManifest {
  id: string;
  name: string;
  version: string;
  description: string;
  routes: readonly ModuleRouteDefinition[];
  navigation: readonly ModuleNavigationItem[];
  permissionManifest: ModulePermissionManifest;
  featureFlags?: readonly string[];
  dependencies?: readonly string[];
  defaultEnabled: boolean;
}
```

Le manifeste centralise :

- identité ;
- routes ;
- navigation ;
- permission manifest ;
- dépendances ;
- feature flags ;
- activation ;
- version ;
- providers éventuels.

## 8.15 Registre des modules

Le registre central doit :

- charger les manifestes ;
- vérifier les identifiants uniques ;
- vérifier les manifestes de permissions ;
- détecter les dépendances absentes ;
- détecter les cycles ;
- filtrer selon tenant, licence et feature flags ;
- assembler routes et navigation ;
- initialiser les providers ;
- permettre le lazy loading ;
- fournir un fallback.

## 8.16 Activation et désactivation

Un module peut être activé selon :

- tenant ;
- plan ;
- licence ;
- environnement ;
- feature flag ;
- permission de module ;
- configuration runtime.

Désactiver un module doit :

- retirer ses routes ;
- retirer sa navigation ;
- éviter son chargement ;
- empêcher ses points d’entrée ;
- gérer explicitement les anciennes URLs.

L’activation frontend ne remplace jamais l’autorisation backend.

## 8.17 Lazy loading et code splitting par module

Les modules significatifs doivent pouvoir être chargés paresseusement.

L’agent doit éviter :

- le chargement statique d’un module désactivable ;
- les imports qui annulent le code splitting ;
- la fragmentation excessive en micro-chunks.

## 8.18 Providers et état de module

Un état propre à un module doit rester dans ce module.

Les providers doivent :

- être montés au plus près des routes ;
- ne pas conserver l’état d’un tenant précédent ;
- être nettoyés au changement de tenant ;
- ne devenir globaux qu’en cas de nécessité réelle.

## 8.19 Routes et navigation

Flux obligatoire :

```text
feature route policies
→ feature routes
→ module routes
→ module manifest
→ module registry
→ application router
```

Les routes doivent être protégées à partir des politiques déclarées par leur feature ou leur module.

## 8.20 Propriété et hiérarchie des permissions

Les permissions sont possédées par le niveau métier concerné.

### Permissions de module

Elles décrivent des capacités globales au module :

```text
billing:access
billing:admin
billing:configure
billing:audit:read
```

Elles résident dans :

```text
module-billing/module-permissions/
```

### Permissions de feature

Elles décrivent les capacités métier propres à une feature :

```text
billing:invoice:read
billing:invoice:create
billing:invoice:update
billing:invoice:delete
billing:invoice:validate
billing:invoice:export
```

Elles résident dans :

```text
module-billing/features/invoices/feature-permissions/
```

Le droit d’accéder au module n’implique jamais automatiquement le droit d’exécuter toutes les actions des features.

## 8.21 Une permission métier, plusieurs surfaces d’application

Route, composant et appel API sont des **surfaces d’application**, pas nécessairement trois permissions différentes.

Correct :

```text
billing:invoice:create
├── route de création
├── bouton de création
└── action API de création
```

À éviter :

```text
billing:invoice:route:create
billing:invoice:component:create-button
billing:invoice:api:create
```

Une permission doit décrire une capacité métier stable, pas un détail d’implémentation React.

## 8.22 Manifeste de permissions d’une feature

```ts
export const INVOICE_PERMISSIONS = {
  READ: 'billing:invoice:read',
  CREATE: 'billing:invoice:create',
  UPDATE: 'billing:invoice:update',
  DELETE: 'billing:invoice:delete',
  VALIDATE: 'billing:invoice:validate',
  EXPORT: 'billing:invoice:export',
} as const;
```

```ts
export const invoicePermissionManifest = {
  featureId: 'billing.invoices',
  permissions: INVOICE_PERMISSIONS,
  enforcement: {
    routes: invoiceRoutePolicies,
    components: invoiceComponentPolicies,
    apiActions: invoiceApiPolicies,
  },
} as const;
```

Le manifeste du module agrège les manifestes des features sans devenir propriétaire de leurs détails internes.

## 8.23 Documentation obligatoire d’un module

Le `README.md` du module doit préciser :

- objectif ;
- périmètre ;
- features ;
- permissions de module ;
- manifestes de permissions des features ;
- API publique ;
- routes ;
- dépendances ;
- événements ;
- configuration ;
- feature flags ;
- état partagé ;
- stratégie de tests ;
- contraintes tenant ;
- limites connues.

## 8.24 Tests des frontières

La CI devrait vérifier :

- absence d’imports internes inter-modules ;
- absence d’import du kernel vers un module ;
- absence d’import de `shared-module/` vers une feature ;
- absence de cycle ;
- cohérence des manifestes ;
- unicité des modules ;
- unicité des codes de permission ;
- absence de permission technique dupliquant une capacité métier ;
- présence d’une politique pour chaque route protégée ;
- présence d’une politique pour chaque action API protégée.

## 8.25 Dépendances circulaires

Les dépendances circulaires sont interdites :

- entre modules ;
- entre features ;
- entre module et shared global ;
- entre manifestes ;
- entre providers.

## 8.26 Micro-frontends

L’architecture modulaire ne signifie pas automatiquement micro-frontends.

Par défaut, préférer un monolithe frontend modulaire.

Les micro-frontends exigent une justification basée sur :

- équipes autonomes ;
- déploiements indépendants ;
- domaines fortement séparés ;
- contraintes organisationnelles réelles.

## 8.27 Critères de création d’un nouveau module

Créer un module lorsque plusieurs critères sont réunis :

- domaine métier distinct ;
- cycle de vie propre ;
- navigation propre ;
- permissions propres ;
- ownership distinct ;
- données et workflows distincts ;
- activation par licence ou tenant ;
- volume de code significatif ;
- évolution indépendante.

Ne pas créer un module uniquement pour une page, un composant ou une petite opération CRUD.
# 9. Routage scalable

## 9.1 Routes hiérarchisées par feature et par module

Éviter un `App.tsx` contenant toutes les routes.

Les routes doivent être assemblées selon la hiérarchie :

```text
feature routes
→ module routes
→ module registry
→ application router
```

Exemple :

```text
modules/module-identity-access/features/users/routes/users.routes.tsx
modules/module-identity-access/features/organizations/routes/organizations.routes.tsx
modules/module-identity-access/routes/identity-access.routes.tsx
app/module-registry/application-modules.ts
app/router/app-router.tsx
```

Chaque niveau ne doit connaître que l’API publique du niveau inférieur.

## 9.2 Capacités obligatoires

Le routeur doit pouvoir gérer :

- routes publiques ;
- routes privées ;
- authentification ;
- permissions ;
- scopes ;
- tenant actif ;
- feature flags ;
- lazy loading ;
- layouts imbriqués ;
- paramètres validés ;
- query params ;
- base path ;
- 403 ;
- 404 ;
- 410 ;
- erreurs de chargement ;
- redirections contrôlées ;
- conservation des filtres ;
- restauration de la navigation.

## 9.3 Validation des paramètres

Tout paramètre d’URL est non fiable.

Le valider avant usage.

## 9.4 État dans l’URL

Stocker dans l’URL les états qui doivent être :

- partageables ;
- bookmarkables ;
- restaurables ;
- compatibles avec retour arrière.

Exemples :

- pagination ;
- tri ;
- filtres ;
- recherche ;
- onglet ;
- vue.

---

# 10. TypeScript strict

## 10.1 Configuration recommandée

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "noFallthroughCasesInSwitch": true,
    "useUnknownInCatchVariables": true
  }
}
```

## 10.2 Données externes

Considérer comme `unknown` :

- réponses API ;
- runtime config ;
- storage ;
- URL ;
- fichiers ;
- messages WebSocket ;
- événements externes ;
- postMessage ;
- imports utilisateurs.

Valider avec Zod ou équivalent.

## 10.3 `any`

Interdit par défaut.

Une exception doit contenir un commentaire expliquant :

- pourquoi ;
- le périmètre ;
- la stratégie de suppression.

## 10.4 États discriminés

Préférer :

```ts
type TypeAsynchronousState<TypeResultData> =
  | { status: 'idle' }
  | { status: 'pending' }
  | { status: 'success'; data: TypeResultData }
  | { status: 'error'; error: InterfaceApplicationError };
```

Éviter les combinaisons contradictoires de booléens.

---

# 11. Conventions de nommage

## Lisibilité immédiate, vocabulaire accessible et préfixes de typage

### Objectif obligatoire

Tout nom créé ou modifié doit permettre de comprendre immédiatement :

- le domaine métier concerné ;
- la catégorie de l’élément ;
- sa responsabilité principale ;
- son niveau de portée lorsque celui-ci n’est pas déjà évident par son emplacement.

Cette règle s’applique aux dossiers, fichiers, modules, features, routes, pages, composants, hooks, services, schémas, types, fonctions, variables et constantes.

Une personne qui ne développe pas doit pouvoir parcourir l’arborescence et identifier la finalité générale des éléments sans ouvrir chaque fichier ni lire une documentation volumineuse. Cette exigence concerne l’identification, l’orientation et la compréhension de la responsabilité. Elle ne prétend pas remplacer l’explication du comportement technique détaillé.

La documentation complète un nom clair ; elle ne doit jamais servir à compenser un nom vague, raccourci ou trompeur.

### Mots complets et compréhensibles

L’agent DOIT :

- écrire les mots en entier dans tous les noms contrôlés par le projet ;
- utiliser un préfixe ou un suffixe composé d’un mot complet lorsque la catégorie de l’élément doit être indiquée ;
- privilégier des mots métier simples, précis et connus dans le produit ;
- utiliser le nom le plus court qui reste immédiatement compréhensible et non ambigu ;
- nommer d’abord la finalité réelle, puis le mécanisme technique lorsque celui-ci apporte une information nécessaire ;
- conserver une seule langue de nommage cohérente dans le projet ;
- remplacer les acronymes et les sigles par leur signification complète dans les noms appartenant au projet ;
- qualifier tout terme générique par son domaine et son action réelle ;
- employer un terme technique uniquement lorsqu’il est indispensable et qu’aucun mot courant aussi exact n’existe ;
- entourer tout terme technique imposé par un nom métier suffisamment clair pour que la responsabilité reste identifiable.

L’agent NE DOIT PAS :

- utiliser une lettre isolée comme préfixe de catégorie ;
- inventer ou conserver une abréviation uniquement pour raccourcir un nom ;
- supposer qu’un acronyme est compréhensible parce qu’il est courant dans une équipe technique ;
- utiliser seul un terme fourre-tout comme `data`, `thing`, `stuff`, `misc`, `other`, `general`, `manager`, `helper` ou `utils` ;
- choisir un terme très spécialisé lorsqu’un terme courant et exact suffit ;
- mélanger plusieurs langues dans une même convention ;
- produire un nom artificiellement long en répétant des informations déjà garanties par le dossier parent.

Exemples généraux :

| À éviter | Préférer | Raison |
|---|---|---|
| `data.ts` | `invoice-payment-summary.types.ts` | Le contenu et le domaine sont identifiables. |
| `Manager.ts` | `OrganizationAccessPolicyService.ts` | La responsabilité n’est plus implicite. |
| `utils.ts` | `format-invoice-due-date.ts` | L’action réelle remplace le terme fourre-tout. |
| `Dashboard.tsx` | `BillingOverviewPage.tsx` | La page et son domaine sont reconnaissables. |
| `useData.ts` | `useOrganizationInvoices.ts` | La donnée réellement chargée est visible. |
| `Config` | `TenantBrandingConfiguration` | Le mot et le périmètre sont écrits complètement. |
| `userId` | `userIdentifier` | `Identifier` ne demande pas de connaître l’abréviation `Id`. |
| `invoicePageProps` | `invoicePageProperties` | `Properties` remplace l’abréviation `Props`. |

### Préfixes complets obligatoires pour les types TypeScript

Toute déclaration de type nommée appartenant au projet DOIT commencer par le mot complet qui indique sa catégorie.

| Catégorie | Préfixe obligatoire | Exemple |
|---|---|---|
| Interface | `Interface` | `InterfaceOrganizationUser`, `InterfaceInvoicePageProperties` |
| Alias, union, intersection ou type dérivé | `Type` | `TypeInvoiceStatus`, `TypeCreateInvoiceRequest` |
| Énumération TypeScript | `Enumeration` | `EnumerationPaymentMethod`, `EnumerationInvoiceLifecycleStatus` |
| Paramètre générique | `Type` suivi de son rôle complet | `TypeInvoiceItem`, `TypeServerResponse` |

Les préfixes à une seule lettre `I`, `T` et `E` sont interdits. Ils obligent le lecteur à connaître une convention implicite et contredisent l’objectif de compréhension immédiate.

Le préfixe complet ne remplace jamais le nom métier. `TypeData`, `InterfaceThing`, `EnumerationType` et `TypeItem` restent interdits lorsqu’une responsabilité plus précise peut être nommée.

Les suffixes décrivant un rôle doivent eux aussi être écrits complètement. Utiliser notamment :

- `Properties` et non `Props` ;
- `Identifier` et non `Id` ;
- `Configuration` et non `Config` ou `Cfg` ;
- `Request` et non `Req` ;
- `Response` et non `Res` ;
- `Context` et non `Ctx` ;
- `Service` et non `Svc`.

Exemples :

```ts
interface InterfaceOrganizationUser {
  userIdentifier: string;
  displayName: string;
}

type TypeInvoiceStatus = 'draft' | 'issued' | 'paid';

enum EnumerationPaymentMethod {
  BankTransfer = 'bank-transfer',
  Card = 'card',
}

interface InterfaceInvoicePageProperties {
  organizationIdentifier: string;
}

type TypeCreateInvoiceRequest = {
  organizationIdentifier: string;
  customerIdentifier: string;
};

function groupInvoiceItems<TypeInvoiceItem>(
  items: TypeInvoiceItem[],
): TypeInvoiceItem[][] {
  return [items];
}
```

### Noms des dossiers, fichiers et éléments fonctionnels

Les noms structurels doivent également annoncer clairement leur catégorie et leur finalité lorsque le chemin parent ne suffit pas.

Exemples :

- `module-billing` identifie explicitement un module de facturation ;
- `BillingOverviewPage.tsx` identifie une page de synthèse de facturation ;
- `InvoicePaymentForm.tsx` identifie un formulaire de paiement de facture ;
- `invoice-payment.validation-schema.ts` identifie les règles de validation du paiement ;
- `useOrganizationInvoices.ts` identifie l’accès aux factures d’une organisation.

Un préfixe ou un suffixe ne doit pas être ajouté mécaniquement si le dossier parent fournit déjà la même information sans ambiguïté. La clarté est obligatoire ; la répétition inutile ne l’est pas.

### Exceptions contrôlées

Les abréviations ou noms imposés sont tolérés uniquement lorsqu’ils proviennent d’une contrainte que le projet ne contrôle pas :

- mot-clé obligatoire du langage ou du framework ;
- type provenant d’une dépendance externe ;
- type généré par OpenAPI, GraphQL ou un autre générateur ;
- nom défini par un contrat public existant ;
- protocole, format ou nom officiel qui ne peut pas être renommé localement.

L’agent ne doit pas propager automatiquement cette exception aux noms internes. Il adapte si nécessaire un élément externe vers un nom interne explicite à la frontière du projet.

L’agent ne doit jamais lancer un renommage massif hors périmètre pour imposer cette convention. Dans un fichier déjà modifié pour la tâche en cours, il aligne uniquement les noms touchés lorsque cela reste sûr, local et compatible avec les contrats existants.

### Contrôle avant livraison

Avant de terminer une tâche, l’agent vérifie chaque nom ajouté ou modifié :

1. Une personne non développeuse peut-elle identifier sa finalité générale sans ouvrir son implémentation ?
2. La catégorie de l’élément est-elle explicite lorsqu’elle ne peut pas être déduite du chemin ?
3. Le domaine métier est-il visible ou fourni sans ambiguïté par le dossier parent ?
4. Tous les mots contrôlés par le projet sont-ils écrits complètement ?
5. Les lettres isolées, abréviations, acronymes et termes fourre-tout ont-ils été supprimés ?
6. Chaque type appartenant au projet porte-t-il le préfixe complet correspondant à sa catégorie ?
7. Le nom reste-t-il lisible, recherchable et dépourvu de répétitions inutiles ?
8. La modification reste-t-elle strictement dans le périmètre demandé ?

En cas de conflit avec une convention existante explicitement imposée par le projet, l’agent ne décide pas silencieusement : il signale le conflit et applique la convention validée pour le périmètre concerné.

## Fichiers

- `PascalCase.tsx` pour les composants ;
- `PascalCasePage.tsx` pour les pages ;
- `useSomething.ts` pour les hooks ;
- `something.api.ts` pour l’API ;
- `something.queries.ts` pour les queries ;
- `something.mutations.ts` pour les mutations ;
- `something.service.ts` pour les services ;
- `something.schema.ts` pour les schémas ;
- `something.types.ts` pour les types ;
- `Something.test.tsx` pour les tests composants ;
- `something.spec.ts` pour les E2E.

## Code

- composants : PascalCase ;
- variables et fonctions : camelCase ;
- constantes : UPPER_SNAKE_CASE ;
- types : PascalCase avec le préfixe complet `Interface`, `Type` ou `Enumeration` ;
- permissions : `resource:action`;
- événements : convention centralisée.

## Imports

- utiliser un alias stable tel que `@/`;
- éviter les chemins relatifs profonds ;
- utiliser `import type`;
- éviter les barrels trop larges ;
- éviter les imports internes inter-features.

---

# 12. Composants épurés

## 12.1 Responsabilité unique

Un composant doit avoir une responsabilité principale.

Il ne doit pas simultanément gérer :

- une grosse logique API ;
- plusieurs formulaires ;
- plusieurs modales ;
- la navigation ;
- les permissions ;
- un état global ;
- un tableau complexe.

Découper lorsque nécessaire.

## 12.2 Séparation

Séparer :

- présentation ;
- orchestration ;
- logique métier ;
- accès données ;
- navigation ;
- validation ;
- transformation.

## 12.3 Props

Les props doivent être :

- explicites ;
- typées ;
- limitées ;
- cohérentes.

Éviter une accumulation de booléens.

Préférer :

- variantes ;
- composition ;
- sous-composants ;
- slots contrôlés.

## 12.4 État des composants

Prévoir selon le cas :

- default ;
- hover ;
- focus ;
- active ;
- disabled ;
- pending ;
- success ;
- warning ;
- error ;
- empty.

---

# 13. Design system et harmonisation

## 13.1 Principe

L’application doit disposer d’un système visuel unique.

Les mêmes concepts doivent avoir :

- la même apparence ;
- le même comportement ;
- les mêmes messages ;
- les mêmes espacements ;
- les mêmes états.

## 13.2 Primitives recommandées

- Button ;
- IconButton ;
- Link ;
- Input ;
- Textarea ;
- Select ;
- Checkbox ;
- Radio ;
- Switch ;
- FormField ;
- Dialog ;
- Modal ;
- Drawer ;
- Popover ;
- Tooltip ;
- Toast ;
- Alert ;
- Badge ;
- Card ;
- Tabs ;
- Table ;
- Pagination ;
- Skeleton ;
- Spinner ;
- Progress ;
- EmptyState ;
- ErrorState ;
- ConfirmDialog ;
- PageHeader ;
- Breadcrumb ;
- SearchField ;
- FilterBar.

## 13.3 Standardisation

Standardiser :

- hauteur des champs ;
- tailles des boutons ;
- espaces ;
- couleurs sémantiques ;
- rayons ;
- ombres ;
- typographie ;
- focus ;
- disabled ;
- loaders ;
- erreurs ;
- confirmations ;
- modales ;
- tables ;
- pagination.

---

# 14. Architecture SaaS, thèmes et white-label

Cette section est obligatoire pour toute application.

## 14.1 Principe fondamental

Aucune marque ne doit être figée dans les composants.

Les composants ne doivent pas connaître :

- le nom commercial ;
- le logo ;
- la couleur principale ;
- la couleur secondaire ;
- le favicon ;
- l’adresse du support ;
- les mentions légales ;
- les réseaux sociaux ;
- l’image sociale ;
- la police de marque ;
- le domaine public.

Ils doivent consommer une configuration de branding.

## 14.2 Architecture de tokens en couches

Organiser les tokens en quatre couches.

### Couche 1 — Tokens fondamentaux

Exemples :

- échelle de gris ;
- échelle d’espacement ;
- rayons ;
- typographie ;
- ombres ;
- durées ;
- z-index.

### Couche 2 — Tokens sémantiques

Exemples :

- `surface-page`;
- `surface-card`;
- `text-primary`;
- `text-secondary`;
- `border-default`;
- `action-primary`;
- `feedback-success`;
- `feedback-warning`;
- `feedback-error`.

### Couche 3 — Tokens de mode

Packages ou presets :

- mode clair ;
- mode sombre ;
- mode système ;
- mode contraste élevé ;
- variantes de marque autorisées.

### Couche 4 — Tokens composants

Exemples :

- bouton primary ;
- sidebar ;
- header ;
- modal ;
- champ ;
- tableau.

Les composants doivent utiliser les tokens sémantiques ou composants, jamais les couleurs brutes de la marque.

## 14.3 Packages de thèmes

Prévoir une organisation telle que :

```text
src/shared/design-system/themes/
├── base.tokens.ts
├── light.theme.ts
├── dark.theme.ts
├── high-contrast.theme.ts
├── theme.schema.ts
├── theme.resolver.ts
└── theme.provider.tsx
```

Un package de thème doit pouvoir définir :

- couleurs ;
- surfaces ;
- textes ;
- bordures ;
- états ;
- ombres ;
- typographie ;
- rayons ;
- densité ;
- illustrations ;
- composants.

## 14.4 Modes supportés

Le système doit au minimum pouvoir supporter :

- `light`;
- `dark`;
- `system`.

Il devrait pouvoir supporter :

- `high-contrast`;
- `brand-light`;
- `brand-dark`;
- thèmes personnalisés autorisés.

## 14.5 Configuration de branding

Exemple de contrat :

```ts
export interface InterfaceBrandAssets {
  logoLightUrl: string;
  logoDarkUrl: string;
  logoCompactUrl?: string;
  faviconUrl?: string;
  socialImageUrl?: string;
}

export interface InterfaceBrandTheme {
  light: Record<string, string>;
  dark: Record<string, string>;
  highContrast?: Record<string, string>;
}

export interface InterfaceTenantBranding {
  tenantId: string;
  applicationName: string;
  shortName?: string;
  assets: InterfaceBrandAssets;
  theme: InterfaceBrandTheme;
  defaultThemeMode: 'light' | 'dark' | 'system';
  supportEmail?: string;
  legalNoticeUrl?: string;
  privacyPolicyUrl?: string;
}
```

Ce contrat doit être validé à l’exécution.

## 14.6 Application globale

Le `ThemeProvider` doit :

1. résoudre le tenant ;
2. charger le branding ;
3. valider les données ;
4. choisir le mode ;
5. appliquer les variables CSS à la racine ;
6. appliquer les assets ;
7. fournir la configuration au reste de l’application ;
8. gérer les changements ;
9. persister la préférence utilisateur si autorisée ;
10. appliquer un fallback sûr.

Modifier la configuration doit impacter toute la plateforme sans modifier chaque composant.

## 14.7 Ordre de résolution recommandé

L’ordre peut être :

1. configuration spécifique du domaine ;
2. configuration du tenant actif ;
3. configuration de l’organisation ;
4. préférence utilisateur ;
5. configuration par défaut de l’application ;
6. fallback sécurisé.

Cet ordre doit être documenté.

## 14.8 Chargement du branding

Le branding peut être obtenu par :

- configuration runtime ;
- endpoint public de configuration ;
- configuration injectée par le serveur ;
- fichier JSON versionné ;
- edge configuration.

Il ne doit pas exiger de rebuild si le besoin SaaS impose des changements dynamiques.

## 14.9 Validation des couleurs

Une couleur fournie par un tenant peut être invalide ou inaccessible.

Le système doit :

- valider le format ;
- contrôler le contraste ;
- contrôler les combinaisons ;
- refuser les valeurs dangereuses ;
- appliquer une valeur de secours ;
- journaliser l’erreur ;
- préserver la lisibilité.

## 14.10 Assets distants

Pour les logos et images :

- valider les URLs ;
- utiliser une allowlist de domaines si nécessaire ;
- prévoir des dimensions ;
- prévoir un alt ;
- prévoir un fallback ;
- éviter les changements de layout ;
- gérer le cache ;
- versionner les assets ;
- éviter les SVG non fiables non assainis.

## 14.11 Prévention du flash de mauvais thème

Éviter le FOUC ou flash clair/sombre incorrect.

Solutions possibles :

- script bootstrap minimal avant React ;
- configuration injectée dans le HTML ;
- lecture sûre de la préférence locale ;
- variables CSS par défaut ;
- préchargement de la configuration ;
- cache versionné.

Le script bootstrap ne doit contenir aucun secret.

## 14.12 Changement dynamique

Le système doit pouvoir gérer :

- changement de thème utilisateur ;
- changement de branding tenant ;
- changement de logo ;
- changement de mode clair/sombre ;
- changement de domaine ;
- changement de configuration sans déployer un nouveau bundle, lorsque requis.

## 14.13 Isolation multi-tenant

Le cache de branding doit inclure le tenant dans sa clé.

Interdit :

- réutiliser le branding du tenant A pour le tenant B ;
- partager une configuration tenant non isolée ;
- laisser une réponse précédente écraser le tenant actif ;
- afficher brièvement un autre logo après changement de tenant.

---

# 15. Branding dynamique et SEO

## 15.1 Principe critique

Le fait que les couleurs, logos et métadonnées soient dynamiques ne doit pas dégrader le SEO.

Les couleurs elles-mêmes ne déterminent pas l’indexation, mais peuvent dégrader :

- accessibilité ;
- performance ;
- stabilité visuelle ;
- rendu social ;
- cohérence de marque.

Le logo et les métadonnées peuvent affecter :

- résultats de recherche ;
- données structurées ;
- aperçus sociaux ;
- favicon ;
- identité de l’organisation.

## 15.2 Pages privées

Pour une console SaaS privée :

- utiliser `noindex`;
- ne pas mettre de contenu sensible dans les métadonnées ;
- ne pas dépendre du SEO ;
- protéger l’accès ;
- empêcher l’indexation lorsque possible.

## 15.3 Pages publiques indexables

Pour une page publique, les métadonnées spécifiques au tenant doivent être disponibles dans le HTML initial.

Ne pas dépendre uniquement d’un `useEffect` React pour définir :

- title ;
- description ;
- canonical ;
- Open Graph ;
- Twitter cards ;
- données structurées ;
- favicon important ;
- image sociale.

## 15.4 Stratégies recommandées

Pour les pages publiques critiques :

- SSR avec Vite ;
- SSG ;
- pré-rendu ;
- injection HTML côté serveur ;
- rendu edge ;
- frontend public séparé ;
- architecture hybride.

## 15.5 Résolution SEO par tenant

Le serveur, build ou edge doit pouvoir résoudre :

- domaine ;
- tenant ;
- marque ;
- langue ;
- canonical ;
- logo ;
- image sociale ;
- données structurées.

Exemple logique :

```text
requête domaine-a.com
→ résolution tenant A
→ métadonnées tenant A
→ HTML initial tenant A
→ hydration React tenant A
```

## 15.6 Stabilité des URLs

Le branding dynamique ne doit pas modifier arbitrairement :

- slug ;
- canonical ;
- structure URL ;
- identifiants de page.

Les changements de marque doivent conserver les URLs stables ou prévoir des redirections correctes.

## 15.7 Logo structuré

Pour une organisation publique :

- fournir un logo crawlable ;
- utiliser une URL stable ;
- fournir des dimensions ;
- utiliser des données structurées appropriées ;
- éviter une URL temporaire expirante ;
- prévoir un fallback.

## 15.8 Cache SEO

Le cache doit varier selon :

- host ;
- tenant ;
- locale ;
- route ;
- version de branding.

Éviter qu’un CDN serve le HTML du tenant A au tenant B.

## 15.9 Performance

Le branding dynamique ne doit pas ajouter une requête bloquante lente sur chaque page.

Utiliser :

- cache ;
- ETag ;
- version ;
- CDN ;
- configuration injectée ;
- stale-while-revalidate maîtrisé.

## 15.10 Tests SEO multi-tenant

Tester :

- title par tenant ;
- description ;
- canonical ;
- favicon ;
- Open Graph ;
- logo ;
- données structurées ;
- index/noindex ;
- cache par domaine ;
- absence de fuite inter-tenant.

---

# 16. Responsive et adaptatif

## 16.1 Exigence non négociable

Toutes les interfaces doivent fonctionner sur :

- très petit mobile ;
- mobile standard ;
- grand mobile ;
- tablette portrait ;
- tablette paysage ;
- petit ordinateur ;
- desktop moyen ;
- grand écran ;
- écran très large.

## 16.2 Mobile-first

Concevoir d’abord le comportement mobile.

## 16.3 Règles de layout

Utiliser :

- flexbox ;
- grid ;
- `minmax`;
- `clamp`;
- dimensions fluides ;
- containers ;
- `max-width`;
- breakpoints cohérents ;
- `min-width: 0` dans les flex/grid lorsque nécessaire.

Éviter :

- largeur fixe globale ;
- hauteur fixe sur contenu dynamique ;
- `100vw` lorsque cela déborde ;
- positionnement absolu structurel ;
- margin négative fragile ;
- scroll horizontal global.

## 16.4 Tables

Pour les petits écrans :

- scroll horizontal local ;
- colonnes prioritaires ;
- mode carte ;
- détail dépliable ;
- actions regroupées.

## 16.5 Navigation

La sidebar doit :

- être fixe ou persistante sur grand écran ;
- devenir drawer ou navigation mobile ;
- gérer overlay ;
- gérer focus ;
- gérer fermeture ;
- ne pas dépasser ;
- ne pas créer de double scroll.

## 16.6 Modales

Sur mobile :

- plein écran ou drawer si nécessaire ;
- bouton de fermeture visible ;
- contenu scrollable ;
- clavier virtuel géré ;
- focus géré ;
- actions accessibles.

---

# 17. Zoom, viewport et reflow

## 17.1 Viewport

Toujours :

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

Jamais :

```html
maximum-scale=1
user-scalable=no
```

## 17.2 Niveaux de test

Tester :

- 100 % ;
- 125 % ;
- 150 % ;
- 200 % ;
- taille de texte augmentée ;
- portrait ;
- paysage.

## 17.3 Causes fréquentes d’ouverture « déjà zoomée »

Vérifier :

- `min-width` globale ;
- image sans `max-width`;
- tableau hors conteneur ;
- `100vw`;
- transform sur root ;
- position absolue ;
- sidebar trop large ;
- modal fixe ;
- viewport incorrect ;
- police ou champ provoquant un zoom mobile ;
- input inférieur à une taille lisible sur certains navigateurs mobiles.

## 17.4 Correction

Corriger la cause.

Ne pas masquer le débordement globalement.

---

# 18. Curseur et sémantique interactive

## 18.1 Règles

- `cursor: text` uniquement pour l’éditable ;
- `cursor: pointer` pour actions et liens ;
- curseur par défaut pour texte ordinaire ;
- `button` pour action ;
- `a` pour navigation ;
- `contenteditable` uniquement avec justification.

## 18.2 Interdictions

- caret sur texte statique ;
- `div` cliquable non accessible ;
- `user-select: none` global ;
- `cursor-text` global ;
- gestionnaire de clic sans clavier ;
- faux bouton.

---

# 19. Listes, collections, pagination et scroll

## 19.1 Choisir une stratégie

Chaque collection doit utiliser explicitement :

- pagination serveur ;
- pagination curseur ;
- bouton charger plus ;
- scroll infini ;
- virtualisation ;
- scroll local.

## 19.2 Pagination serveur

Gérer :

- page ;
- taille ;
- total ;
- tri ;
- filtres ;
- recherche ;
- première page ;
- dernière page ;
- changement de taille ;
- page vide ;
- URL.

## 19.3 Pagination curseur

Gérer :

- next cursor ;
- previous cursor si possible ;
- ordre stable ;
- doublons ;
- fin de liste ;
- rafraîchissement.

## 19.4 Scroll infini

Autorisé uniquement lorsque pertinent.

Prévoir :

- alternative accessible ;
- chargement ;
- erreur ;
- retry ;
- fin ;
- restauration de position ;
- navigation arrière.

## 19.5 Virtualisation

Tester :

- clavier ;
- focus ;
- lecteurs d’écran ;
- sélection ;
- hauteur dynamique ;
- défilement.

## 19.6 États obligatoires

Toute liste doit gérer :

- loading initial ;
- fetching suivant ;
- données ;
- vide ;
- aucun résultat ;
- erreur ;
- rafraîchissement ;
- permission absente ;
- filtre invalide ;
- total inconnu.

---

# 20. Loaders et progression

## 20.1 Règle

Toute action asynchrone déclenchée par l’utilisateur doit avoir un feedback immédiat.

## 20.2 Bouton

Pendant une requête :

- spinner ou indicateur ;
- libellé clair ;
- disabled ;
- prévention double clic ;
- `aria-busy`;
- restauration dans `finally`.

## 20.3 Choix du loader

- Skeleton : chargement initial ;
- spinner local : action courte ;
- progress bar : upload/import ;
- overlay : blocage global justifié ;
- rafraîchissement discret : anciennes données visibles.

## 20.4 Chargement progressif

Utiliser :

- lazy routes ;
- code splitting ;
- images lazy ;
- sections progressives ;
- pagination ;
- cache ;
- prefetch mesuré ;
- skeleton stable.

## 20.5 Ne pas surcharger

Ne pas afficher un spinner global pour une petite action locale.

---

# 21. Prévention des boucles de requêtes

## 21.1 Interdictions

- requête dans le rendu ;
- effet avec dépendance recréée ;
- effet modifiant sa propre dépendance sans garde ;
- retry infini ;
- polling non borné ;
- double fetch involontaire ;
- query key instable.

## 21.2 Effets

- dépendances exhaustives ;
- primitives stables ;
- callbacks mémorisés si nécessaire ;
- aucune désactivation arbitraire ESLint ;
- cleanup.

## 21.3 Annulation

Utiliser `AbortController` ou capacité équivalente.

Cas :

- navigation ;
- démontage ;
- changement de filtre ;
- recherche ;
- requête remplacée.

## 21.4 Race conditions

Une réponse obsolète ne doit pas écraser la plus récente.

## 21.5 Debounce

Recherche :

- debounce ;
- annulation ;
- longueur minimale si utile ;
- feedback ;
- query key stable.

## 21.6 Retry

- limité ;
- backoff ;
- erreurs transitoires uniquement ;
- pas de retry validation ;
- prudence mutations ;
- idempotency key pour actions critiques si backend supporte.

---

# 22. Gestion d’état

Séparer :

## État local

- modal ;
- onglet ;
- sélection ;
- champ.

## État serveur

- liste ;
- détail ;
- cache ;
- mutation ;
- invalidation.

## État global

- session ;
- tenant ;
- branding ;
- thème ;
- locale ;
- permissions ;
- registre des modules ;
- modules activés ;
- flags.

Un état propre à un module doit rester dans le provider ou store du module. Il ne devient global que lorsqu’il est réellement nécessaire à plusieurs modules.

## État URL

- page ;
- tri ;
- filtres ;
- recherche ;
- onglet.

Pour le server-state complexe, préférer TanStack Query.

Ne pas utiliser Context comme gestionnaire universel.

Ne pas stocker un état dérivable.

---

# 23. Couche API

## 23.1 Centralisation

La couche API doit gérer :

- base URL ;
- timeout ;
- headers ;
- auth ;
- tenant ;
- organisation ;
- locale ;
- correlation ID ;
- sérialisation ;
- validation ;
- erreurs ;
- annulation ;
- observabilité.

Les composants ne doivent pas appeler directement Axios ou Fetch.

## 23.2 Contrats

Utiliser OpenAPI lorsque disponible.

Générer ou synchroniser :

- types ;
- clients ;
- schemas ;
- codes d’erreur.

## 23.3 Statuts

Gérer :

- réseau ;
- timeout ;
- annulation ;
- 400 ;
- 401 ;
- 403 ;
- 404 ;
- 409 ;
- 410 ;
- 412 ;
- 422 ;
- 429 ;
- 500 ;
- 502 ;
- 503 ;
- 504.

## 23.4 401

Éviter :

- boucle de refresh ;
- multiples refresh concurrents ;
- redirection répétée ;
- perte de route de retour.

## 23.5 Configuration tenant

Les headers ou scopes tenant doivent être résolus centralement.

Ne jamais laisser un composant construire librement un header tenant.

---

# 24. Gestion exhaustive des erreurs

## 24.1 Principe

Toutes les erreurs doivent être gérées.

« Tout catcher » signifie :

- catcher aux frontières asynchrones ;
- utiliser Error Boundaries pour le rendu ;
- capturer les erreurs globales pour observabilité ;
- ne jamais laisser un incident invisible ;
- ne jamais faire croire au succès.

Cela ne signifie pas entourer chaque ligne de `try/catch`.

## 24.2 Taxonomie

```ts
export type TypeApplicationErrorCategory =
  | 'network'
  | 'timeout'
  | 'cancelled'
  | 'authentication'
  | 'authorization'
  | 'validation'
  | 'business'
  | 'conflict'
  | 'not-found'
  | 'rate-limit'
  | 'unavailable'
  | 'render'
  | 'configuration'
  | 'tenant'
  | 'unknown';

export interface InterfaceApplicationError {
  code: string;
  category: TypeApplicationErrorCategory;
  userMessage: string;
  technicalMessage?: string;
  fieldErrors?: Record<string, string>;
  status?: number;
  correlationId?: string;
  retryable: boolean;
  cause?: unknown;
}
```

## 24.3 Normalisation centrale

Créer :

```ts
export function normalizeError(error: unknown): InterfaceApplicationError {
  // classification, extraction sûre et fallback
}
```

## 24.4 Message utilisateur

Le message doit expliquer :

- ce qui a échoué ;
- la conséquence ;
- la cause si elle est connue et utile ;
- l’action possible ;
- si les données ont été enregistrées ;
- si une nouvelle tentative est possible.

Correct :

> L’utilisateur n’a pas été ajouté à l’équipe, car il en est déjà membre. Aucune modification n’a été enregistrée.

Incorrect :

> Error 409.

## 24.5 Canaux UX

- inline : champ ;
- résumé formulaire : formulaire ;
- toast : feedback non bloquant ;
- modal : décision ou échec critique ;
- bannière : incident persistant ;
- état local : widget ;
- page erreur : route ;
- écran offline : perte réseau globale.

Ne pas dupliquer le même message sur plusieurs canaux.

## 24.6 Error Boundaries

Prévoir :

- global ;
- par route ;
- par zone critique.

Fallback :

- message clair ;
- retry ;
- retour ;
- référence support ;
- aucune stack visible.

## 24.7 Erreurs globales

Capturer :

- `window.error`;
- `unhandledrejection`.

Envoyer vers observabilité.

Ne pas les utiliser comme remplacement de la gestion locale.

## 24.8 Annulation

Une annulation attendue n’est pas une erreur utilisateur.

## 24.9 Optimistic update

En cas d’échec :

- rollback ;
- message ;
- invalidation ;
- réconciliation ;
- aucune conservation d’un faux état.

## 24.10 Logs

Inclure :

- code ;
- catégorie ;
- route ;
- feature ;
- action ;
- tenant pseudonymisé ;
- statut ;
- correlation ID ;
- version ;
- environnement ;
- durée.

Exclure :

- mot de passe ;
- token ;
- secret ;
- contenu sensible ;
- donnée personnelle inutile.

---

# 25. Retour utilisateur après toute action

## 25.1 Cycle obligatoire

1. prise en compte visuelle ;
2. état pending ;
3. blocage des répétitions ;
4. résultat ;
5. mise à jour UI ;
6. focus ou annonce si nécessaire.

## 25.2 Actions

### Création

- pending ;
- succès ;
- ajout visible ;
- erreur claire.

### Modification

- pending ;
- confirmation ;
- conservation des données ;
- gestion conflit.

### Suppression

- confirmation ;
- nom de ressource ;
- conséquences ;
- pending ;
- résultat ;
- possibilité de récupération si disponible.

### Upload

- progression ;
- taille ;
- annulation ;
- succès ;
- erreur.

### Export

- préparation ;
- téléchargement ;
- erreur ;
- expiration éventuelle.

### Traitement différé

- confirmation d’acceptation ;
- identifiant de suivi ;
- emplacement du suivi ;
- statut.

---

# 26. Formulaires

Chaque formulaire doit gérer :

- valeurs initiales ;
- validation client ;
- validation serveur ;
- erreurs par champ ;
- erreur globale ;
- pending ;
- double soumission ;
- succès ;
- données non sauvegardées ;
- reset ;
- création ;
- modification ;
- accessibilité ;
- clavier ;
- mobile ;
- formats ;
- fichiers.

Après une erreur serveur, conserver les données saisies.

Associer chaque erreur au champ.

Déplacer le focus vers la première erreur lorsque pertinent.

---

# 27. Sécurité frontend et gouvernance des permissions

## 27.1 Authentification

Préférer :

- cookie HttpOnly ;
- Secure ;
- SameSite ;
- BFF ;
- OAuth2/OIDC ;
- PKCE ;
- rotation ;
- expiration courte.

Éviter les tokens sensibles dans localStorage.

## 27.2 Principe de propriété

Chaque permission appartient au domaine qui la définit :

- le module possède ses permissions globales ;
- la feature possède ses permissions métier ;
- une shared feature possède ses propres permissions ;
- le kernel fournit uniquement le moteur générique d’évaluation.

Le kernel ne doit pas contenir le catalogue métier de toutes les permissions.

## 27.3 Catalogue TypeScript par défaut

Le catalogue doit être typé et colocalisé.

```ts
export const INVOICE_PERMISSIONS = {
  READ: 'billing:invoice:read',
  CREATE: 'billing:invoice:create',
  UPDATE: 'billing:invoice:update',
  DELETE: 'billing:invoice:delete',
} as const;

export type TypeInvoicePermission =
  (typeof INVOICE_PERMISSIONS)[keyof typeof INVOICE_PERMISSIONS];
```

## 27.4 Catalogue YAML ou JSON optionnel

Un catalogue déclaratif YAML ou JSON est autorisé uniquement lorsqu’il devient la source de vérité commune pour :

- frontend ;
- backend ;
- IAM ;
- documentation ;
- audit ;
- génération de politiques.

Dans ce cas :

```text
catalogue central
├── types TypeScript générés
├── constantes frontend générées
├── contrats backend générés
├── configuration IAM générée
└── documentation générée
```

Il est interdit de maintenir manuellement plusieurs sources de vérité concurrentes.

## 27.5 Interdiction des permissions dans `.env`

Le catalogue des permissions ne doit pas être stocké dans les variables d’environnement.

Les permissions métier :

- ne sont pas des secrets ;
- doivent être typées ;
- doivent être recherchables ;
- doivent rester cohérentes entre environnements ;
- doivent être versionnées avec le code ou générées depuis une source centrale.

Les variables d’environnement restent réservées aux configurations variables.

## 27.6 Modèle de politique

Une politique doit pouvoir déclarer :

- permission requise ;
- logique `ALL` ou `ANY` ;
- scope ;
- tenant ;
- organisation ;
- ownership ;
- feature flag ;
- comportement de refus ;
- message utilisateur ;
- identifiant de politique.

Exemple :

```ts
export interface InterfaceAuthorizationPolicy {
  id: string;
  requiredPermissions?: readonly string[];
  permissionMode?: 'ALL' | 'ANY';
  requiresAuthentication: boolean;
  tenantScoped?: boolean;
  organizationScoped?: boolean;
  publicAccess?: boolean;
}
```

## 27.7 Politiques de route

Chaque route doit déclarer explicitement l’un des modes suivants :

- publique ;
- authentifiée ;
- protégée par permission ;
- protégée par scope ;
- désactivée.

Aucune route ne doit dépendre d’une convention implicite.

## 27.8 Politiques de composant

Les composants sensibles doivent utiliser :

- `ComponentPermissionGuard` ;
- `ActionPermissionGuard` ;
- hook d’autorisation typé ;
- policy déclarative.

Le code de permission ne doit pas être recopié directement dans plusieurs composants.

Le masquage ou la désactivation doit être choisi selon le contexte UX.

## 27.9 Politiques d’action API

Toute action API métier doit déclarer explicitement une politique :

```text
public
authenticated
permission-protected
system-internal
```

Les appels tels que login, configuration publique ou healthcheck peuvent être explicitement publics ou authentifiés sans permission métier.

Toute autre action métier protégée doit déclarer :

- la permission requise ;
- le scope ;
- le tenant ;
- le comportement en cas de refus ;
- les éventuelles conditions contextuelles.

## 27.10 Protection frontend et backend

Le frontend :

- masque ;
- désactive ;
- bloque la navigation ;
- évite un appel manifestement interdit ;
- explique le refus.

Le backend :

- vérifie réellement la permission ;
- vérifie le tenant ;
- vérifie l’organisation ;
- vérifie la ressource ;
- vérifie le scope ;
- refuse ;
- journalise.

Le backend reste l’autorité de sécurité.

## 27.11 Guards obligatoires

Le kernel peut fournir :

- `AuthGuard` ;
- `RoutePermissionGuard` ;
- `ComponentPermissionGuard` ;
- `ActionPermissionGuard` ;
- `FeatureFlagGuard` ;
- `TenantScopeGuard` ;
- `OrganizationScopeGuard` ;
- `ResourceOwnershipGuard`.

## 27.12 Cohérence des trois surfaces

Pour une capacité métier donnée, route, composant et action API doivent utiliser le même code de permission lorsque la même capacité est réellement protégée.

Exemple :

```text
billing:invoice:create
├── InvoiceCreateRoute
├── CreateInvoiceButton
└── createInvoice mutation
```

La CI devrait détecter :

- route autorisée mais action API non déclarée ;
- bouton visible sans politique ;
- action API déclarée avec une permission différente sans justification ;
- permission inutilisée ;
- permission inconnue.

## 27.13 Refus et retour utilisateur

En cas de refus :

- ne pas afficher une erreur technique ;
- expliquer que l’utilisateur n’a pas l’autorisation ;
- préciser l’action refusée ;
- proposer une action possible si pertinente ;
- ne pas révéler une ressource sensible ;
- journaliser la décision.

## 27.14 Cache des permissions

Le cache doit varier selon :

- utilisateur ;
- tenant ;
- organisation ;
- rôle ou groupe ;
- version de politique ;
- session.

Lors d’un changement de tenant ou de session :

- invalider le cache ;
- réévaluer la navigation ;
- réévaluer les routes ;
- réévaluer les composants ;
- éviter l’affichage transitoire d’actions non autorisées.

## 27.15 XSS

- éviter `dangerouslySetInnerHTML`;
- assainir le contenu riche ;
- utiliser une CSP ;
- valider les entrées ;
- encoder les sorties.

## 27.16 Secrets

Aucun secret dans :

- code ;
- variables Vite ;
- bundle ;
- storage ;
- source map publique ;
- log ;
- HTML.

## 27.17 Dépendances

Évaluer :

- sécurité ;
- licence ;
- maintenance ;
- taille ;
- réputation ;
- compatibilité.
# 28. Portabilité et configuration

## 28.1 Environnements

Le code doit fonctionner en :

- local ;
- dev ;
- test ;
- intégration ;
- preview ;
- recette ;
- staging ;
- préproduction ;
- production ;
- environnement client ;
- Docker ;
- Kubernetes ;
- cloud ;
- statique ;
- reverse proxy ;
- sous-chemin.

## 28.2 Aucun hardcoding critique

Externaliser :

- API URL ;
- auth URL ;
- domaine ;
- base path ;
- timeout ;
- tenant ;
- client ID public ;
- locale ;
- devise ;
- timezone ;
- pagination ;
- feature flags ;
- observabilité ;
- support ;
- branding ;
- légal ;
- SEO ;
- endpoints variables.

## 28.3 Build-time vs runtime

### Build-time

- optimisation ;
- code éliminé ;
- base technique ;
- instrumentation compilée.

### Runtime

- API ;
- auth ;
- tenant ;
- marque ;
- thèmes ;
- flags ;
- support ;
- SEO tenant ;
- limites variables.

### Secrets

Toujours côté serveur.

## 28.4 Variables Vite

Les variables `VITE_*` sont publiques.

## 28.5 Runtime config

Exemple :

```json
{
  "apiBaseUrl": "https://api.example.com",
  "authBaseUrl": "https://auth.example.com",
  "basePath": "/",
  "defaultLocale": "fr",
  "brandingEndpoint": "/public/branding",
  "features": {}
}
```

Valider avec un schéma.

## 28.6 Démarrage invalide

Si une configuration critique manque :

- ne pas utiliser localhost silencieusement ;
- afficher une page claire ;
- logger ;
- fournir une référence ;
- arrêter le bootstrap fonctionnel.

## 28.7 Reproductibilité

- lockfile ;
- version Node ;
- package manager ;
- commandes documentées ;
- CI identique ;
- aucun chemin absolu ;
- aucun comportement dépendant d’un OS.

---

# 29. Déploiement

## Vite

Configurer :

- base path ;
- alias ;
- chunks ;
- assets ;
- sourcemaps ;
- proxy local ;
- env ;
- tests.

## Docker

- multi-stage ;
- non-root ;
- image minimale ;
- cache ;
- runtime config ;
- serveur sécurisé ;
- healthcheck pertinent.

## Reverse proxy

- fallback SPA ;
- cache assets hashés ;
- no-cache runtime config ;
- compression ;
- headers ;
- HTTPS ;
- base path.

## Kubernetes

- ConfigMap ;
- secrets uniquement pour serveur ;
- readiness ;
- ingress ;
- version ;
- rollback ;
- isolation environnements.

## CDN

- assets hashés ;
- immutable ;
- cache ;
- compression ;
- variation par host pour HTML multi-tenant.

---

# 30. SEO complet

## 30.1 Classification

Chaque route doit être :

- publique indexable ;
- publique non indexable ;
- privée ;
- administrative.

## 30.2 Pages publiques

Gérer :

- title ;
- meta description ;
- canonical ;
- Open Graph ;
- social card ;
- favicon ;
- manifest ;
- robots ;
- sitemap ;
- hreflang ;
- données structurées ;
- URL lisible ;
- headings ;
- alt ;
- statut HTTP ;
- 404 réelle ;
- redirections ;
- performance.

## 30.3 SPA

Une SPA pure a des limites.

Pour SEO critique :

- SSR ;
- SSG ;
- pre-render ;
- edge rendering ;
- hybride.

## 30.4 Pages privées

- noindex ;
- pas de données sensibles dans metadata ;
- auth ;
- protection crawler si possible.

## 30.5 Tests

Tester :

- metadata ;
- canonical ;
- indexation ;
- locale ;
- tenant ;
- social preview ;
- schema ;
- erreurs ;
- cache.

---

# 31. Accessibilité

Cible minimale : WCAG 2.2 AA.

Toujours :

- HTML sémantique ;
- navigation clavier ;
- focus visible ;
- ordre logique ;
- labels ;
- descriptions ;
- aria-live ;
- contrastes ;
- information non dépendante de la couleur ;
- alt ;
- modales accessibles ;
- reduced motion ;
- touch targets ;
- zoom ;
- reflow ;
- langue ;
- tableaux structurés.

Ne pas utiliser ARIA pour remplacer un élément natif approprié.

---

# 32. Internationalisation

Prévoir :

- clés de traduction ;
- pluriels ;
- interpolation ;
- dates ;
- nombres ;
- devises ;
- fuseaux ;
- RTL ;
- fallback ;
- tenant locale ;
- préférence utilisateur.

Traduire les erreurs à partir de codes stables.

---

# 33. Aides et onboarding

Préparer le code pour :

- tooltips ;
- aide contextuelle ;
- step-by-step ;
- visite guidée ;
- checklist ;
- centre d’aide.

Utiliser des identifiants stables :

```tsx
data-tour-id="organization-create-button"
```

Le guide doit supporter :

- rôle ;
- permission ;
- tenant ;
- langue ;
- version ;
- progression ;
- responsive ;
- accessibilité.

---

# 34. Performance et scalabilité

## Mesurer

- bundle ;
- LCP ;
- CLS ;
- INP ;
- requêtes ;
- mémoire ;
- rendu ;
- listes.

## Optimiser

- code splitting ;
- lazy routes ;
- tree shaking ;
- cache ;
- images ;
- pagination ;
- virtualisation ;
- debounce ;
- memoization mesurée ;
- réduction rerenders ;
- bundle analysis.

Ne pas faire de micro-optimisation sans preuve.

---

# 35. Observabilité

Prévoir :

- error tracking ;
- performance monitoring ;
- correlation ID ;
- version ;
- environnement ;
- route ;
- feature ;
- action ;
- tenant pseudonymisé ;
- durée ;
- source maps privées.

Analytics :

- typés ;
- documentés ;
- consentis ;
- sans données inutiles ;
- sans doublon de rendu.

---

# 36. Tests

## 36.1 Niveaux

- unitaires ;
- composants ;
- intégration ;
- E2E ;
- visuels ;
- accessibilité ;
- contrat ;
- performance.

## 36.2 Scénarios obligatoires

Pour une action critique :

- succès ;
- validation ;
- erreur métier ;
- réseau ;
- timeout ;
- 401 ;
- 403 ;
- 404 ;
- 409 ;
- 422 ;
- 429 ;
- 500 ;
- réponse mal formée ;
- annulation ;
- double clic ;
- navigation ;
- retry ;
- permission absente ;
- mauvais tenant ;
- liste vide ;
- grand volume ;
- mobile ;
- zoom ;
- clavier.

## 36.3 Outils possibles

- Vitest ;
- React Testing Library ;
- MSW ;
- Playwright ;
- axe-core ;
- régression visuelle approuvée.

---

# 37. CI/CD

Minimum :

```text
install déterministe
lint
format-check
typecheck
tests
build
```

Selon criticité :

- E2E ;
- accessibilité ;
- audit sécurité ;
- licences ;
- scan secrets ;
- bundle budget ;
- SEO ;
- visual regression ;
- contrat API.

Le pipeline doit échouer en cas d’échec obligatoire.

---

# 38. Gestion des dépendances

Avant ajout :

- besoin ;
- alternative native ;
- taille ;
- sécurité ;
- licence ;
- maintenance ;
- compatibilité ;
- fréquence de release ;
- risque de lock-in.

Encapsuler les dépendances critiques.

---

# 39. Workflow de création d’un module ou d’une feature

## 39.1 Déterminer le bon niveau

Avant toute création, décider si le besoin correspond à :

- une modification d’une feature existante ;
- une nouvelle feature dans un module existant ;
- un élément partagé par les features d’un module ;
- un élément partagé globalement ;
- un nouveau module.

L’agent doit justifier la destination choisie.

## 39.2 Analyse

- besoin ;
- domaine métier ;
- module propriétaire ;
- features concernées ;
- acteurs ;
- permissions ;
- tenant ;
- licence ;
- données ;
- états ;
- erreurs ;
- volumes ;
- responsive ;
- accessibilité ;
- SEO ;
- environnement ;
- dépendances inter-modules.

## 39.3 Création d’un nouveau module

Lorsqu’un nouveau module est justifié :

1. choisir un nom métier stable ;
2. créer `modules/module-<nom>/` ;
3. créer son manifeste ;
4. définir son API publique ;
5. créer `features/` ;
6. créer `shared-module/` si nécessaire ;
7. définir routes et navigation ;
8. définir permissions ;
9. définir contrats et événements ;
10. définir providers et état ;
11. enregistrer le module dans le registre ;
12. configurer le lazy loading ;
13. documenter les dépendances ;
14. écrire les tests de frontières ;
15. mettre à jour la documentation.

## 39.4 Création d’une feature

Pour une nouvelle feature :

1. identifier son module parent ;
2. créer la structure dans `module-<nom>/features/<feature>/` ;
3. créer `feature-permissions/` avec catalogue, policies et manifeste ;
4. définir types et schémas ;
4. définir services, queries et mutations ;
5. créer composants et pages ;
6. définir routes de feature ;
7. intégrer les routes au module ;
8. définir permissions ;
9. gérer loaders et erreurs ;
10. écrire les tests ;
11. documenter l’API publique éventuelle.

## 39.5 Promotion vers un niveau partagé

Avant de déplacer un élément :

- vérifier qu’il est réellement réutilisé ;
- vérifier qu’il n’embarque pas une règle métier trop spécifique ;
- choisir `shared-module/` avant `shared/` global lorsque le partage reste interne ;
- stabiliser son contrat ;
- ajouter des tests ;
- mettre à jour les imports ;
- supprimer les duplications devenues inutiles.

## 39.6 Conception

- types ;
- schemas ;
- API ;
- routes ;
- composants ;
- état ;
- loaders ;
- messages ;
- permissions de module et de feature ;
- politiques de route, composant et action API ;
- contrats ;
- événements ;
- API publique ;
- tests ;
- observabilité.

## 39.7 Implémentation

- structure ;
- manifeste ;
- services ;
- queries ;
- mutations ;
- composants ;
- page ;
- routes ;
- navigation ;
- guards ;
- retours ;
- erreurs ;
- tests ;
- docs.

## 39.8 Validation

- lint ;
- format ;
- typecheck ;
- tests ;
- build ;
- frontières de modules ;
- cycles ;
- manifestes ;
- lazy loading ;
- activation/désactivation ;
- responsive ;
- zoom ;
- clavier ;
- permissions ;
- erreurs ;
- requêtes ;
- config ;
- secrets ;
- performance ;
- SEO.

---

# 40. Checklist module et feature

## Architecture modulaire

- [ ] module parent identifié ;
- [ ] module nommé `module-<nom-métier>` ;
- [ ] `module-permissions/` présent lorsque le module possède des permissions globales ;
- [ ] feature placée sous `modules/<module>/features/` ;
- [ ] `feature-permissions/` présent pour toute feature protégée ;
- [ ] shared feature interne placée dans `shared-module/features/` ;
- [ ] primitive interne placée directement dans `shared-module/` ;
- [ ] shared feature transversale placée dans `shared/features/` ;
- [ ] infrastructure générique placée dans `shared/kernel/` ;
- [ ] manifeste de module valide ;
- [ ] API publique limitée ;
- [ ] registre de modules mis à jour ;
- [ ] routes assemblées feature → module → application ;
- [ ] navigation et permissions déclarées ;
- [ ] activation et désactivation testées si applicables ;
- [ ] lazy loading respecté ;
- [ ] frontières respectées ;
- [ ] aucun import interne inter-module ;
- [ ] aucun cycle ;
- [ ] aucune duplication inutile.


## Permissions

- [ ] permission de module colocalisée dans `module-permissions/` ;
- [ ] permission de feature colocalisée dans `feature-permissions/` ;
- [ ] codes décrivant des capacités métier ;
- [ ] aucune permission liée au nom d’un bouton ou composant ;
- [ ] policies routes déclarées ;
- [ ] policies composants déclarées ;
- [ ] policies actions API déclarées ;
- [ ] appels publics explicitement marqués publics ;
- [ ] catalogue absent de `.env` ;
- [ ] manifeste de feature agrégé par le module ;
- [ ] backend identifié comme autorité finale ;
- [ ] cache invalidé au changement de tenant ou session ;


## SaaS

- [ ] aucun branding figé ;
- [ ] thème via tokens ;
- [ ] logo configurable ;
- [ ] tenant isolé ;
- [ ] cache tenant-safe ;
- [ ] fallback sûr.

## TypeScript

- [ ] strict ;
- [ ] aucun any injustifié ;
- [ ] validation runtime ;
- [ ] schémas.

## API

- [ ] client centralisé ;
- [ ] erreurs ;
- [ ] timeout ;
- [ ] annulation ;
- [ ] retry borné ;
- [ ] correlation ID.

## UX

- [ ] loader ;
- [ ] succès ;
- [ ] erreur ;
- [ ] vide ;
- [ ] confirmation ;
- [ ] double clic empêché.

## Responsive

- [ ] très petit écran ;
- [ ] mobile ;
- [ ] tablette ;
- [ ] desktop ;
- [ ] grand écran ;
- [ ] zoom 200 % ;
- [ ] aucun overflow global.

## Sécurité

- [ ] permission ;
- [ ] backend autoritaire ;
- [ ] tenant ;
- [ ] aucun secret ;
- [ ] XSS ;
- [ ] logs sûrs.

## Accessibilité

- [ ] clavier ;
- [ ] focus ;
- [ ] labels ;
- [ ] contraste ;
- [ ] aria-live ;
- [ ] modal.

## Tests

- [ ] succès ;
- [ ] erreurs ;
- [ ] permission ;
- [ ] tenant ;
- [ ] responsive ;
- [ ] accessibilité ;
- [ ] E2E critique.

---

# 41. Definition of Done

Une tâche n’est terminée que si les critères pertinents sont satisfaits.

## Fonctionnel

- [ ] besoin couvert ;
- [ ] cas nominaux ;
- [ ] erreurs ;
- [ ] aucun faux succès ;
- [ ] aucune action silencieuse.

## Architecture modulaire

- [ ] module parent explicite ;
- [ ] features correctement rattachées ;
- [ ] responsabilités séparées ;
- [ ] composants épurés ;
- [ ] `shared-module/features/` utilisé pour les capacités partagées du module ;
- [ ] primitives du module correctement colocalisées ;
- [ ] `shared/features/` utilisé pour les fonctionnalités transversales ;
- [ ] `shared/kernel/` réservé à l’infrastructure générique ;
- [ ] API publique minimale ;
- [ ] manifeste cohérent ;
- [ ] registre mis à jour ;
- [ ] frontières vérifiées ;
- [ ] aucun import interne inter-module ;
- [ ] aucun cycle ;
- [ ] cohérence.

## Permissions et politiques

- [ ] permissions de module dans `module-permissions/` ;
- [ ] permissions de feature dans `feature-permissions/` ;
- [ ] une permission métier réutilisée sur les surfaces correspondantes ;
- [ ] aucune duplication route/composant/API injustifiée ;
- [ ] chaque route possède un mode d’accès explicite ;
- [ ] chaque action API possède une politique explicite ;
- [ ] chaque composant sensible possède une politique ;
- [ ] catalogue typé ou généré depuis une source unique ;
- [ ] aucune permission métier dans `.env` ;
- [ ] contrôle backend confirmé ;
- [ ] tests de refus présents ;

## SaaS

- [ ] branding configurable ;
- [ ] thèmes configurables ;
- [ ] light/dark/system ;
- [ ] logo dynamique ;
- [ ] configuration validée ;
- [ ] absence de fuite tenant ;
- [ ] SEO tenant préservé.

## Erreurs

- [ ] toutes interceptées aux frontières ;
- [ ] normalisées ;
- [ ] messages clairs ;
- [ ] logs ;
- [ ] pas de données sensibles ;
- [ ] reprise proposée.

## Chargement

- [ ] loader adapté ;
- [ ] double clic empêché ;
- [ ] `finally`;
- [ ] progressif ;
- [ ] stabilité layout.

## Requêtes

- [ ] aucune boucle ;
- [ ] annulation ;
- [ ] race condition gérée ;
- [ ] retry contrôlé ;
- [ ] cache correct.

## Responsive

- [ ] mobile ;
- [ ] tablette ;
- [ ] desktop ;
- [ ] zoom ;
- [ ] reflow ;
- [ ] aucun scroll horizontal global.

## Portabilité

- [ ] pas de hardcoding critique ;
- [ ] variables documentées ;
- [ ] runtime config ;
- [ ] local ;
- [ ] production ;
- [ ] base path ;
- [ ] build reproductible.

## Sécurité

- [ ] auth ;
- [ ] permissions ;
- [ ] tenant ;
- [ ] secrets ;
- [ ] XSS ;
- [ ] logs.

## Accessibilité

- [ ] clavier ;
- [ ] focus ;
- [ ] labels ;
- [ ] contraste ;
- [ ] erreurs annoncées ;
- [ ] zoom ;
- [ ] reduced motion.

## Tests

- [ ] lint ;
- [ ] format ;
- [ ] typecheck ;
- [ ] tests ;
- [ ] build ;
- [ ] E2E si nécessaire ;
- [ ] accessibilité.

## Documentation

- [ ] décisions ;
- [ ] variables ;
- [ ] permissions ;
- [ ] limites ;
- [ ] migration ;
- [ ] tests exécutés.

---

# 42. Anti-patterns à détecter activement

- features placées directement à la racine hors module ;
- module sans responsabilité métier claire ;
- module nommé `main`, `general`, `misc` ou `utils` ;
- import direct des internes d’un autre module ;
- import de `shared/` global vers un module ;
- `shared-module/` important les détails internes d’une feature ;
- feature protégée sans `feature-permissions/` ;
- permission de feature stockée uniquement au niveau module ;
- permission nommée d’après un bouton, une page ou un appel Axios ;
- trois permissions techniques pour une seule capacité métier ;
- catalogue de permissions dans `.env` ;
- appel API métier sans politique déclarée ;
- route protégée et action API utilisant des permissions contradictoires ;
- moteur générique de permissions contenant tout le catalogue métier ;
- API publique réexportant tout un module ;
- registre de modules contenant de la logique métier ;
- dépendance circulaire inter-module ;
- module chargé statiquement alors qu’il est désactivable ;
- création d’un micro-frontend sans justification ;
- composant monolithique ;
- appels API dans JSX ;
- `useEffect` en boucle ;
- dépendance instable ;
- catch vide ;
- erreur console invisible ;
- message technique utilisateur ;
- token dans localStorage sans décision ;
- permission dispersée ;
- couleur en dur ;
- logo en dur ;
- URL en dur ;
- tenant non isolé ;
- thème appliqué composant par composant ;
- configuration non validée ;
- largeur fixe ;
- zoom désactivé ;
- overflow caché ;
- bouton sans loader ;
- double soumission ;
- liste sans stratégie ;
- table non responsive ;
- modal inaccessible ;
- div cliquable ;
- any ;
- duplication ;
- dépendance inutile ;
- Context énorme ;
- état dérivé ;
- aucune Error Boundary ;
- aucune page erreur ;
- console privée indexable ;
- metadata tenant uniquement côté client sur page publique ;
- cache CDN ne variant pas par tenant.

---

# 43. Grille de sévérité pour audit

## P0 — Bloquant critique

- fuite inter-tenant ;
- secret exposé ;
- contournement permission ;
- perte de données ;
- faux succès sur action critique ;
- XSS exploitable ;
- application inutilisable.

## P1 — Majeur

- violation des frontières inter-modules ;
- dépendance circulaire entre modules ;
- mauvais module activé pour un tenant ;
- erreurs non visibles ;
- boucle de requêtes ;
- absence de responsive ;
- mauvaise gestion auth ;
- branding tenant incorrect ;
- page publique SEO incorrecte ;
- double soumission destructive.

## P2 — Important

- dette architecturale ;
- composant monolithique ;
- accessibilité significativement dégradée ;
- performance importante ;
- duplication ;
- test critique absent.

## P3 — Amélioration

- cohérence visuelle mineure ;
- optimisation légère ;
- documentation secondaire ;
- refactoring non urgent.

L’agent doit traiter les P0 avant toute autre amélioration.

---

# 44. Format du compte rendu de l’agent

Après une réalisation, l’agent doit fournir :

## Résultat

Résumé factuel.

## Fichiers créés ou modifiés

Liste exacte.

## Architecture, modules et décisions

Module parent, features concernées, niveau de partage choisi, API publique, dépendances, permissions, politiques et raisons.

## SaaS et branding

Tenant, thèmes, logos, runtime config et SEO.

## Sécurité

Auth, permissions, secrets, isolation.

## UX et gestion des erreurs

Loaders, messages, erreurs et reprises.

## Responsive et accessibilité

Écrans et contrôles.

## Tests exécutés

Commandes et résultats exacts.

## Risques et limites

Ce qui reste à vérifier.

L’agent ne doit jamais inventer un résultat.

---

# 45. Commande comportementale finale

Lorsqu’il utilise ce Skill, l’agent doit appliquer la règle suivante :

> Analyse d’abord le besoin et l’existant. Conçois toute interface en mode SaaS-ready, multi-tenant et white-label. Ne fige jamais le branding, les thèmes, les logos, les URLs ou les paramètres variables. Utilise des tokens sémantiques, des packages de thèmes clair, sombre, système et, si nécessaire, contraste élevé. Résous et valide la configuration du tenant de manière isolée. Préserve le SEO des pages publiques en fournissant les métadonnées tenant dans le HTML initial par SSR, SSG, pré-rendu, injection serveur ou edge lorsque l’indexation est importante. Respecte l’architecture application → modules → features, place les permissions globales dans `module-permissions/`, les permissions fonctionnelles dans `feature-permissions/`, et applique chaque permission métier aux routes, composants et actions API concernés. Utilise `shared-module/features/` pour les capacités partagées d’un module, `shared/features/` pour les fonctionnalités transversales et `shared/kernel/` pour l’infrastructure générique. Respecte les frontières de modules, les API publiques, TypeScript strict, le responsive, le zoom, l’accessibilité, la sécurité et la portabilité. Pour toute action asynchrone, affiche un loader adapté, empêche les doubles appels, annule les requêtes obsolètes, catche les erreurs aux frontières pertinentes, les normalise, les journalise sans données sensibles et affiche un message clair à l’utilisateur. N’ignore jamais une erreur. N’annonce jamais qu’une tâche est terminée sans contrôles et résultats vérifiables.

---

# 46. Référence de démarrage pour une nouvelle application

Toute nouvelle application doit commencer avec au moins un module métier explicitement nommé.

```text
src/
├── app/
│   ├── bootstrap/
│   ├── error-boundaries/
│   ├── layouts/
│   ├── module-registry/
│   ├── providers/
│   └── router/
│
├── modules/
│   └── module-<premier-domaine-metier>/
│       ├── module-permissions/
│       │   ├── <module>.module-permissions.ts
│       │   ├── <module>.module-policies.ts
│       │   ├── <module>.module-permission-manifest.ts
│       │   └── index.ts
│       │
│       ├── features/
│       │   └── <premiere-feature>/
│       │       ├── feature-permissions/
│       │       │   ├── routes/
│       │       │   ├── components/
│       │       │   ├── api-actions/
│       │       │   ├── <feature>.permissions.ts
│       │       │   ├── <feature>.permission-manifest.ts
│       │       │   └── index.ts
│       │       ├── api/
│       │       ├── components/
│       │       ├── hooks/
│       │       ├── pages/
│       │       ├── routes/
│       │       ├── schemas/
│       │       ├── services/
│       │       ├── types/
│       │       └── index.ts
│       │
│       ├── shared-module/
│       │   ├── features/
│       │   ├── components/
│       │   ├── hooks/
│       │   ├── types/
│       │   └── utils/
│       │
│       ├── config/
│       ├── contracts/
│       ├── navigation/
│       ├── providers/
│       ├── routes/
│       ├── tests/
│       ├── module.manifest.ts
│       ├── index.ts
│       └── README.md
│
├── shared/
│   ├── features/
│   │   ├── notifications/
│   │   ├── file-management/
│   │   └── global-search/
│   ├── kernel/
│   │   ├── api/
│   │   ├── auth/
│   │   ├── errors/
│   │   ├── observability/
│   │   ├── permissions/
│   │   ├── routing/
│   │   ├── storage/
│   │   └── tenancy/
│   ├── design-system/
│   ├── config/
│   ├── i18n/
│   ├── seo/
│   ├── types/
│   └── utils/
│
├── test/
├── main.tsx
└── vite-env.d.ts
```

Fichiers attendus selon le besoin :

```text
.env.example
Dockerfile
README.md
runtime-config.schema.ts
runtime-config.example.json
application-module-manifest.types.ts
application-modules.registry.ts
authorization-policy.types.ts
permission-evaluator.ts
module.manifest.ts
module-permission-manifest.ts
feature-permission-manifest.ts
app-error.ts
error-normalizer.ts
theme.schema.ts
theme.provider.tsx
branding.provider.tsx
app-router.tsx
global-error-boundary.tsx
```

Règle de démarrage :

> Une petite application commence avec un seul module métier correctement nommé. Toute feature protégée possède son propre catalogue et manifeste de permissions. Les permissions du module restent séparées des permissions des features.

---

# 47. Historique de version

## Version 1.1.0

Évolution majeure de l’architecture des permissions et des espaces partagés :

- séparation de `module-permissions/` et `feature-permissions/` ;
- ajout des politiques `routes/`, `components/` et `api-actions/` ;
- adoption du principe « une permission métier, plusieurs surfaces d’application » ;
- ajout des manifestes de permissions par feature ;
- agrégation des manifestes au niveau module ;
- interdiction du catalogue de permissions dans `.env` ;
- TypeScript retenu par défaut ;
- YAML ou JSON autorisé uniquement comme source de vérité génératrice ;
- ajout de `shared/features/` pour les fonctionnalités transversales ;
- ajout de `shared/kernel/` pour l’infrastructure commune ;
- ajout de `shared-module/features/` pour les capacités partagées au sein d’un module ;
- distinction entre shared features et primitives techniques ;
- ajout des règles de cohérence entre route, composant et action API ;
- ajout des tests de politiques, de refus et d’unicité des permissions.

## Baseline modulaire précédente

La baseline précédente avait introduit :

- le niveau `modules/` ;
- l’obligation d’au moins un module ;
- `shared-module/` ;
- les manifestes et le registre des modules ;
- les frontières de dépendance ;
- le lazy loading ;
- l’activation par tenant, licence ou feature flag.

---

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
