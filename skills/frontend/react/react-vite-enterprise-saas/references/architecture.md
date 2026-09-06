# Architecture frontend

Cette référence regroupe l’architecture modulaire, le routage, les composants, le système visuel, le fonctionnement SaaS, les échanges de données, les erreurs, la configuration, le déploiement, le référencement, la performance et l’observabilité.

<!-- preserved-source-part-start: frontend-section-7 -->
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

<!-- preserved-source-part-end: frontend-section-7 -->

<!-- preserved-source-part-start: frontend-section-8-heading -->
# 8. Architecture modulaire orientée domaines, features et permissions

<!-- preserved-source-part-end: frontend-section-8-heading -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-1 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-1 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-2 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-2 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-3 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-3 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-4 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-4 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-5 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-5 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-6 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-6 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-7 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-7 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-8 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-8 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-9 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-9 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-10 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-10 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-11 -->
## 8.11 Communications entre features du même module

Une feature ne doit pas importer directement les fichiers internes d’une autre feature.

Options autorisées :

1. utiliser l’API publique de la feature ;
2. promouvoir l’élément vers `shared-module/` ;
3. utiliser un service d’orchestration du module ;
4. utiliser un contrat ou événement interne documenté.

<!-- preserved-source-part-end: frontend-section-8-subsection-8-11 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-12 -->
## 8.12 Communications entre modules

Un module ne doit jamais importer les détails internes d’un autre module.

Mécanismes autorisés :

- API publique du module ;
- contrat TypeScript stable ;
- événement applicatif typé ;
- route documentée ;
- orchestration dans `app/` ;
- backend comme point de synchronisation.

<!-- preserved-source-part-end: frontend-section-8-subsection-8-12 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-13 -->
## 8.13 API publique d’un module

Chaque module expose uniquement ce qui est nécessaire via son `index.ts`.

```ts
export { billingModuleManifest } from './module.manifest';
export { BILLING_MODULE_PERMISSIONS } from './module-permissions';
export { InvoiceSelector } from './features/invoices';
export type { InvoiceReference } from './contracts/invoice-reference';
```

Il est interdit de réexporter automatiquement tout le contenu du module.

<!-- preserved-source-part-end: frontend-section-8-subsection-8-13 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-14 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-14 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-15 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-15 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-16 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-16 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-17 -->
## 8.17 Lazy loading et code splitting par module

Les modules significatifs doivent pouvoir être chargés paresseusement.

L’agent doit éviter :

- le chargement statique d’un module désactivable ;
- les imports qui annulent le code splitting ;
- la fragmentation excessive en micro-chunks.

<!-- preserved-source-part-end: frontend-section-8-subsection-8-17 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-18 -->
## 8.18 Providers et état de module

Un état propre à un module doit rester dans ce module.

Les providers doivent :

- être montés au plus près des routes ;
- ne pas conserver l’état d’un tenant précédent ;
- être nettoyés au changement de tenant ;
- ne devenir globaux qu’en cas de nécessité réelle.

<!-- preserved-source-part-end: frontend-section-8-subsection-8-18 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-19 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-19 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-24 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-24 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-25 -->
## 8.25 Dépendances circulaires

Les dépendances circulaires sont interdites :

- entre modules ;
- entre features ;
- entre module et shared global ;
- entre manifestes ;
- entre providers.

<!-- preserved-source-part-end: frontend-section-8-subsection-8-25 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-26 -->
## 8.26 Micro-frontends

L’architecture modulaire ne signifie pas automatiquement micro-frontends.

Par défaut, préférer un monolithe frontend modulaire.

Les micro-frontends exigent une justification basée sur :

- équipes autonomes ;
- déploiements indépendants ;
- domaines fortement séparés ;
- contraintes organisationnelles réelles.

<!-- preserved-source-part-end: frontend-section-8-subsection-8-26 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-27 -->
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
<!-- preserved-source-part-end: frontend-section-8-subsection-8-27 -->

<!-- preserved-source-part-start: frontend-section-9 -->
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

<!-- preserved-source-part-end: frontend-section-9 -->

<!-- preserved-source-part-start: frontend-section-12 -->
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

<!-- preserved-source-part-end: frontend-section-12 -->

<!-- preserved-source-part-start: frontend-section-13 -->
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

<!-- preserved-source-part-end: frontend-section-13 -->

<!-- preserved-source-part-start: frontend-section-14 -->
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

<!-- preserved-source-part-end: frontend-section-14 -->

<!-- preserved-source-part-start: frontend-section-15 -->
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

<!-- preserved-source-part-end: frontend-section-15 -->

<!-- preserved-source-part-start: frontend-section-19 -->
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

<!-- preserved-source-part-end: frontend-section-19 -->

<!-- preserved-source-part-start: frontend-section-20 -->
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

<!-- preserved-source-part-end: frontend-section-20 -->

<!-- preserved-source-part-start: frontend-section-21 -->
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

<!-- preserved-source-part-end: frontend-section-21 -->

<!-- preserved-source-part-start: frontend-section-22 -->
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

<!-- preserved-source-part-end: frontend-section-22 -->

<!-- preserved-source-part-start: frontend-section-23 -->
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

<!-- preserved-source-part-end: frontend-section-23 -->

<!-- preserved-source-part-start: frontend-section-24 -->
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

<!-- preserved-source-part-end: frontend-section-24 -->

<!-- preserved-source-part-start: frontend-section-25 -->
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

<!-- preserved-source-part-end: frontend-section-25 -->

<!-- preserved-source-part-start: frontend-section-26 -->
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

<!-- preserved-source-part-end: frontend-section-26 -->

<!-- preserved-source-part-start: frontend-section-28 -->
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

<!-- preserved-source-part-end: frontend-section-28 -->

<!-- preserved-source-part-start: frontend-section-29 -->
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

<!-- preserved-source-part-end: frontend-section-29 -->

<!-- preserved-source-part-start: frontend-section-30 -->
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

<!-- preserved-source-part-end: frontend-section-30 -->

<!-- preserved-source-part-start: frontend-section-32 -->
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

<!-- preserved-source-part-end: frontend-section-32 -->

<!-- preserved-source-part-start: frontend-section-33 -->
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

<!-- preserved-source-part-end: frontend-section-33 -->

<!-- preserved-source-part-start: frontend-section-34 -->
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

<!-- preserved-source-part-end: frontend-section-34 -->

<!-- preserved-source-part-start: frontend-section-35 -->
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

<!-- preserved-source-part-end: frontend-section-35 -->

<!-- preserved-source-part-start: frontend-section-38 -->
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

<!-- preserved-source-part-end: frontend-section-38 -->

<!-- preserved-source-part-start: frontend-section-46 -->
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

<!-- preserved-source-part-end: frontend-section-46 -->
