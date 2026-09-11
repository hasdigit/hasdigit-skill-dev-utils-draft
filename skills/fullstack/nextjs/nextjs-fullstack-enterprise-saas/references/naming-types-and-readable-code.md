# Nommage, types et code lisible

Lire ce document avant de créer ou renommer un dossier, fichier, route, table, colonne, événement, fonction, variable ou déclaration TypeScript.

## Résultat attendu

Une personne qui ne connaît pas la base de code doit pouvoir comprendre la responsabilité générale d’un élément grâce à son nom et à son emplacement.

Un nom ne doit pas obliger à connaître une convention réservée aux spécialistes. Il doit préciser le domaine, l’action et la nature lorsque ces informations évitent une ambiguïté.

## Préfixes TypeScript complets

Pour les déclarations contrôlées par le projet :

- `Interface` pour une interface TypeScript ;
- `Type` pour un alias de type ;
- `Enumeration` pour une énumération ;
- `Schema` pour un schéma de validation ;
- `Result` pour un résultat d’opération ;
- `Error` pour une erreur structurée du domaine ;
- `Event` pour un événement métier ;
- `Command` pour une demande de modification ;
- `Query` pour une demande de lecture.

Exemple :

```ts
interface InterfaceCreateInvoiceInput {
  customerOrganizationIdentifier: string;
  invoiceLineItems: TypeInvoiceLineItem[];
}

type TypeCreateInvoiceResult =
  | { status: "created"; invoiceIdentifier: string }
  | { status: "invalid-input"; fieldErrors: Record<string, string[]> }
  | { status: "permission-denied" };

enum EnumerationInvoiceStatus {
  Draft = "draft",
  Issued = "issued",
  Paid = "paid",
}
```

Les préfixes isolés `I`, `T` et `E` sont interdits. Leur signification n’est pas déductible par une personne extérieure au projet.

## Mots complets

| Éviter | Préférer |
|---|---|
| `cfg` | `configuration` |
| `ctx` | `context` |
| `auth` | `authentication` ou `authorization` |
| `perm` | `permission` |
| `org` | `organization` |
| `usr` | `user` |
| `svc` | nom du service avec son domaine |
| `repo` | `repository` lorsque ce mot décrit réellement l’accès aux données |
| `util` | nom précis de l’opération |
| `dto` | `data-transfer-object` ou, mieux, nom du résultat transporté |
| `db` | `database` dans les noms contrôlés |
| `id` | `Identifier` ou `identifier` |
| `req` | `request` |
| `res` | `response` |
| `err` | `error` |

Les noms imposés par un standard externe peuvent rester abrégés à sa frontière : `HTTP`, `HTML`, `JSON`, `URL`, `SQL`, `OpenAPI`, `Next.js`. Expliquer le terme dans les documents destinés à un public non technique et convertir vers des noms internes complets lorsque possible.

## Dossiers

Un dossier décrit un domaine ou une responsabilité :

- `invoice-creation/` ;
- `organization-permission-policies/` ;
- `invoice-data-access/` ;
- `payment-provider-adapter/` ;
- `route-input-validation/` ;
- `database-migrations/` ;
- `background-job-processing/`.

Éviter `utils/`, `helpers/`, `lib/`, `common/`, `misc/`, `stuff/`, `core/` ou `services/` sans domaine et responsabilité complémentaires.

## Fichiers

Un nom de fichier indique sa fonction principale :

- `create-invoice-use-case.ts` ;
- `invoice-permission-policy.ts` ;
- `invoice-database-repository.ts` ;
- `create-invoice-route-input-schema.ts` ;
- `create-invoice-server-action.ts` ;
- `payment-provider-webhook-route-adapter.ts` ;
- `invoice-created-domain-event.ts` ;
- `invoice-database-migration-plan.md`.

Éviter `index.ts` pour la logique. Un point d’export peut utiliser ce nom seulement si la convention est maîtrisée et si l’interface reste limitée.

## Exceptions Next.js

Les fichiers spéciaux sont imposés par le framework :

- `page.tsx` ;
- `layout.tsx` ;
- `route.ts` ;
- `loading.tsx` ;
- `error.tsx` ;
- `global-error.tsx` ;
- `not-found.tsx` ;
- `template.tsx` ;
- `default.tsx` ;
- fichiers de métadonnées reconnus.

Le dossier parent fournit leur contexte. La logique appelée doit porter un nom complet hors du fichier spécial.

## Fonctions

Commencer par un verbe décrivant l’effet :

- `createAuthorizedInvoice` ;
- `loadInvoiceForOrganization` ;
- `validateCreateInvoiceInput` ;
- `resolveCustomerOrganizationContext` ;
- `recordInvoiceCreatedEvent` ;
- `mapPaymentProviderResponse` ;
- `invalidateInvoiceReadModels`.

Éviter `handleData`, `processItem`, `manageRequest`, `doAction`, `getInfo` ou `execute` sans objet métier.

Une fonction qui lit ne modifie pas silencieusement une donnée. Une fonction qui modifie doit rendre son effet visible dans son nom ou son contrat.

## Booléens et états

Un booléen forme une affirmation :

- `isInvoicePaymentAuthorized` ;
- `hasActiveOrganizationMembership` ;
- `canRetryPaymentRequest` ;
- `shouldInvalidateInvoiceCache`.

Éviter plusieurs booléens permettant des états contradictoires. Utiliser une union discriminée avec des noms d’état compréhensibles.

## Identifiants

Préciser la nature :

- `invoiceIdentifier` ;
- `customerOrganizationIdentifier` ;
- `externalPaymentIdentifier` ;
- `correlationIdentifier` ;
- `idempotencyIdentifier`.

Ne pas mélanger un identifiant interne, public et fournisseur dans un même type de chaîne sans distinction.

## Routes HTTP

Les segments publics doivent utiliser des noms stables et compréhensibles. La méthode réseau décrit l’opération ; éviter les verbes répétés inutilement dans l’adresse.

Exemples :

```text
GET    /api/v1/invoices/{invoiceIdentifier}
POST   /api/v1/invoices
PATCH  /api/v1/invoices/{invoiceIdentifier}
POST   /api/v1/invoices/{invoiceIdentifier}/payments
```

Une adresse publique déjà utilisée est un contrat. Ne pas la renommer pour harmoniser l’interne sans migration des consommateurs.

## Tables et colonnes

Employer le vocabulaire métier et la convention du moteur de données. Les noms doivent distinguer :

- identifiant interne et identifiant externe ;
- instant de création et instant métier ;
- état courant et historique ;
- organisation propriétaire ;
- suppression logique et suppression réelle.

Éviter une colonne `data`, `value`, `status` ou `type` sans contexte suffisant. Une donnée structurée générale ne doit pas devenir un emplacement où toute évolution est cachée.

## Événements et tâches

Nommer au passé un fait accompli :

- `InvoiceCreated` ;
- `PaymentConfirmed` ;
- `OrganizationMemberInvited`.

Nommer à l’impératif une demande :

- `GenerateInvoiceDocument` ;
- `SendOrganizationInvitation`.

Un événement ne doit pas porter un nom général comme `Updated` sans préciser l’objet et le sens.

## Codes et références

Un code stable peut être nécessaire pour les machines. Toute communication destinée à une personne doit l’accompagner d’une explication :

```text
INVOICE_PAYMENT_ALREADY_COMPLETED (le paiement de cette facture a déjà été confirmé)
```

Ne pas renvoyer seulement `A12`, `ERR_4` ou un numéro de section. Ajouter un intitulé humain permettant de comprendre sans consulter un autre document.

## Commentaires

Un commentaire explique une contrainte, une décision ou un risque non évident. Il ne répète pas la ligne suivante.

Préférer un nom plus clair à un commentaire compensant un nom vague. Ajouter une référence externe seulement avec une explication locale de ce qu’elle prouve.

## Contrôle avant livraison

- préfixes `Interface`, `Type` et `Enumeration` ;
- mots complets dans les noms contrôlés ;
- domaine et responsabilité visibles dans les chemins ;
- fonctions nommées par effet ;
- identifiants non confondus ;
- routes publiques stables ;
- tables et événements compréhensibles ;
- codes accompagnés d’explications humaines ;
- exceptions limitées aux frontières imposées ;
- renommages compatibles avec les contrats et migrations.
