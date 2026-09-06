# Permissions et modèles de protection

Cette référence définit la propriété des permissions et leur application cohérente aux modules, features, routes, composants et actions serveur.

<!-- preserved-source-part-start: frontend-section-6 -->
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

<!-- preserved-source-part-end: frontend-section-6 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-20 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-20 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-21 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-21 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-22 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-22 -->

<!-- preserved-source-part-start: frontend-section-8-subsection-8-23 -->
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

<!-- preserved-source-part-end: frontend-section-8-subsection-8-23 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-2 -->
## 27.2 Principe de propriété

Chaque permission appartient au domaine qui la définit :

- le module possède ses permissions globales ;
- la feature possède ses permissions métier ;
- une shared feature possède ses propres permissions ;
- le kernel fournit uniquement le moteur générique d’évaluation.

Le kernel ne doit pas contenir le catalogue métier de toutes les permissions.

<!-- preserved-source-part-end: frontend-section-27-subsection-27-2 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-3 -->
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

<!-- preserved-source-part-end: frontend-section-27-subsection-27-3 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-4 -->
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

<!-- preserved-source-part-end: frontend-section-27-subsection-27-4 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-5 -->
## 27.5 Interdiction des permissions dans `.env`

Le catalogue des permissions ne doit pas être stocké dans les variables d’environnement.

Les permissions métier :

- ne sont pas des secrets ;
- doivent être typées ;
- doivent être recherchables ;
- doivent rester cohérentes entre environnements ;
- doivent être versionnées avec le code ou générées depuis une source centrale.

Les variables d’environnement restent réservées aux configurations variables.

<!-- preserved-source-part-end: frontend-section-27-subsection-27-5 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-6 -->
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

<!-- preserved-source-part-end: frontend-section-27-subsection-27-6 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-7 -->
## 27.7 Politiques de route

Chaque route doit déclarer explicitement l’un des modes suivants :

- publique ;
- authentifiée ;
- protégée par permission ;
- protégée par scope ;
- désactivée.

Aucune route ne doit dépendre d’une convention implicite.

<!-- preserved-source-part-end: frontend-section-27-subsection-27-7 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-8 -->
## 27.8 Politiques de composant

Les composants sensibles doivent utiliser :

- `ComponentPermissionGuard` ;
- `ActionPermissionGuard` ;
- hook d’autorisation typé ;
- policy déclarative.

Le code de permission ne doit pas être recopié directement dans plusieurs composants.

Le masquage ou la désactivation doit être choisi selon le contexte UX.

<!-- preserved-source-part-end: frontend-section-27-subsection-27-8 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-9 -->
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

<!-- preserved-source-part-end: frontend-section-27-subsection-27-9 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-10 -->
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

<!-- preserved-source-part-end: frontend-section-27-subsection-27-10 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-11 -->
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

<!-- preserved-source-part-end: frontend-section-27-subsection-27-11 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-12 -->
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

<!-- preserved-source-part-end: frontend-section-27-subsection-27-12 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-13 -->
## 27.13 Refus et retour utilisateur

En cas de refus :

- ne pas afficher une erreur technique ;
- expliquer que l’utilisateur n’a pas l’autorisation ;
- préciser l’action refusée ;
- proposer une action possible si pertinente ;
- ne pas révéler une ressource sensible ;
- journaliser la décision.

<!-- preserved-source-part-end: frontend-section-27-subsection-27-13 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-14 -->
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

<!-- preserved-source-part-end: frontend-section-27-subsection-27-14 -->
