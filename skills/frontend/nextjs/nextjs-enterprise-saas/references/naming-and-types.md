# Nommage compréhensible et types TypeScript

Lire ce document avant de créer ou renommer un dossier, un fichier, un composant, une fonction, une constante, une route ou une déclaration TypeScript.

## Objectif

Une personne qui ne connaît pas l’architecture doit pouvoir comprendre la responsabilité générale d’un élément en lisant son nom et son emplacement.

Un nom clair ne remplace pas la documentation d’un mécanisme complexe. Il évite seulement de rendre cette documentation nécessaire pour découvrir le rôle élémentaire du code.

## TypeScript strict

Activer les contrôles stricts compatibles avec le projet et ne pas les contourner pour terminer plus vite.

Les données suivantes doivent être considérées inconnues jusqu’à validation :

- corps et paramètres de requête ;
- paramètres de route et de recherche ;
- cookies et en-têtes ;
- réponses de services externes ;
- variables d’environnement ;
- contenu de formulaires ;
- données persistées dont le schéma n’est pas garanti ;
- messages et événements externes.

Valider ces données à leur frontière, puis convertir le résultat vers un type métier sûr.

L’utilisation de `any` est interdite sauf contrainte externe démontrée, limitée et documentée. Préférer `unknown`, un type générique, un type union ou un schéma de validation.

## Préfixes de types écrits en toutes lettres

Pour les déclarations appartenant au projet, utiliser :

- `Interface` pour une interface TypeScript ;
- `Type` pour un alias de type ;
- `Enumeration` pour une énumération ;
- `Schema` pour un schéma de validation ;
- `Result` pour un résultat explicite ;
- `Error` pour une erreur structurée appartenant au domaine.

Exemples :

```ts
interface InterfaceInvoicePaymentFormProperties {
  invoiceIdentifier: string;
  onPaymentCompleted: (paymentIdentifier: string) => void;
}

type TypeInvoicePaymentState =
  | { status: "idle" }
  | { status: "submitting" }
  | { status: "completed"; paymentIdentifier: string }
  | { status: "failed"; userMessage: string };

enum EnumerationInvoicePaymentMethod {
  BankTransfer = "bank-transfer",
  PaymentCard = "payment-card",
}
```

Ne pas utiliser `I`, `T` ou `E` comme préfixes isolés. Une personne non spécialiste ne peut pas déduire leur signification de manière fiable.

## Noms complets

Interdire les abréviations contrôlées par le projet lorsqu’un mot complet reste raisonnable.

| À éviter | Préférer | Raison |
|---|---|---|
| `cfg` | `configuration` | La responsabilité devient immédiate. |
| `ctx` | `context` | Le mot complet évite une convention implicite. |
| `auth` | `authentication` ou `authorization` | Les deux concepts sont différents. |
| `perm` | `permission` | Le mot complet reste court. |
| `org` | `organization` | Le domaine est compréhensible sans glossaire. |
| `usr` | `user` | L’abréviation n’apporte rien. |
| `svc` | `service` avec un domaine | La nature et le domaine deviennent visibles. |
| `util` | un nom décrivant l’opération | Le nom révèle la responsabilité réelle. |
| `props` dans un type projet | `Properties` | La catégorie est écrite explicitement. |
| `id` dans un nom contrôlé | `Identifier` | La valeur est lisible sans convention. |

Les sigles imposés par un standard ou un produit restent autorisés à leur frontière : `HTML`, `CSS`, `URL`, `HTTP`, `GET`, `POST`, `SEO`, `JSON`, `GraphQL`, `OpenAPI`, `Next.js` et `TypeScript`. Expliquer leur signification dans un document destiné à une personne non spécialiste lors de leur première utilisation.

Ne pas propager une abréviation externe dans les noms internes. Par exemple, une propriété réseau `org_id` peut être convertie vers `organizationIdentifier` après validation.

## Noms propres aux frontières Next.js

Les fichiers spéciaux imposés par Next.js constituent des exceptions :

- `page.tsx` ;
- `layout.tsx` ;
- `loading.tsx` ;
- `error.tsx` ;
- `global-error.tsx` ;
- `not-found.tsx` ;
- `route.ts` ;
- `template.tsx` ;
- `default.tsx` ;
- les fichiers de métadonnées reconnus par le framework.

Leur dossier parent doit fournir le contexte métier. Un fichier `page.tsx` dans `invoice-payment/` est compréhensible; un fichier dans un segment vague comme `stuff/` ne l’est pas.

Pour les éléments non imposés, utiliser des catégories explicites :

- `InvoicePaymentPageContent` pour le contenu métier d’une page ;
- `InvoicePaymentServerQuery` pour une lecture serveur ;
- `InvoicePaymentServerAction` pour un traitement serveur ;
- `InvoicePaymentRouteHandler` pour une frontière réseau ;
- `InvoicePaymentPermissionPolicy` pour une règle d’autorisation ;
- `InvoicePaymentDataAccess` pour un accès aux données ;
- `InvoicePaymentClientForm` pour un formulaire interactif livré au navigateur ;
- `InvoicePaymentLoadingState` pour un état de chargement ;
- `InvoicePaymentErrorState` pour un état d’erreur.

Ne pas ajouter `Server` ou `Client` partout. Utiliser ces mots seulement lorsqu’ils préviennent réellement une confusion de frontière.

## Dossiers

Un dossier doit décrire un domaine, une capacité ou une responsabilité :

- `invoice-payment/` ;
- `customer-organization-selection/` ;
- `billing-authorization/` ;
- `server-actions/` ;
- `server-queries/` ;
- `permission-policies/` ;
- `error-normalization/`.

Éviter `misc/`, `other/`, `common/`, `general/`, `helpers/`, `utils/` ou `lib/` sans domaine et sans responsabilité explicites.

Un dossier partagé doit indiquer ce qui est partagé et pourquoi. `shared/kernel/` peut désigner l’infrastructure générique si le projet documente le mot `kernel`; pour un public large, préférer un nom fonctionnel plus direct lorsque possible.

## Fichiers

Utiliser un nom qui indique la responsabilité principale :

- `invoice-payment-server-action.ts` ;
- `invoice-payment-permission-policy.ts` ;
- `invoice-payment-input-schema.ts` ;
- `invoice-payment-client-form.tsx` ;
- `invoice-payment-error-normalization.ts` ;
- `customer-organization-branding-resolution.ts`.

Éviter `index.ts` comme emplacement de logique. Un fichier d’exportation peut utiliser ce nom uniquement lorsque la convention du projet l’exige et que les exports restent limités.

## Fonctions et variables

Une fonction commence par un verbe précis :

- `loadAuthorizedInvoicePayment` ;
- `validateInvoicePaymentInput` ;
- `resolveCustomerOrganizationContext` ;
- `invalidateInvoicePaymentCache` ;
- `formatInvoicePaymentUserMessage`.

Éviter `handleData`, `processItem`, `doAction`, `manageState` ou `getInfo`.

Un booléen doit former une affirmation lisible :

- `isPaymentAuthorized` ;
- `hasActiveCustomerOrganization` ;
- `canRetryInvoicePayment` ;
- `shouldRevalidateInvoicePayment`.

## États discriminés

Préférer un état discriminé à plusieurs booléens contradictoires :

```ts
type TypeInvoiceLoadingState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "loaded"; invoice: InterfaceInvoiceSummary }
  | { status: "empty" }
  | { status: "failed"; userMessage: string };
```

Les chaînes d’état sont des valeurs techniques. Le document ou le type doit expliquer leur effet lorsqu’il n’est pas évident.

## Importations

- Utiliser les alias configurés et documentés.
- Éviter les chemins relatifs profonds.
- Importer un autre module par son interface publique.
- Séparer les points d’entrée serveur et navigateur.
- Utiliser `import type` lorsque seule l’information de type est nécessaire.
- Éviter les réexportations générales qui cachent l’origine ou livrent accidentellement du code serveur au navigateur.

## Exceptions contrôlées

Une abréviation ou un nom imposé est accepté uniquement lorsqu’il provient :

- du langage ;
- d’une convention obligatoire de Next.js ;
- d’un protocole ou standard externe ;
- d’une bibliothèque ;
- d’un contrat de données externe ;
- d’un fichier généré.

Limiter l’exception à cette frontière, expliquer sa signification et convertir vers des noms internes complets lorsque le projet contrôle la suite.

Ne pas renommer automatiquement les fichiers existants hors du périmètre demandé. Un renommage doit préserver les importations, les routes, les contrats externes et l’historique utile.

## Contrôle avant livraison

Vérifier :

- les préfixes `Interface`, `Type` et `Enumeration` ;
- l’absence de nouveaux noms vagues ou abrégés ;
- les noms des routes et dossiers métier ;
- la différence claire entre authentification et autorisation ;
- la distinction des frontières serveur et navigateur ;
- la compatibilité des renommages avec les importations et contrats ;
- la compréhension des nouveaux noms par une personne ne connaissant pas le code.
