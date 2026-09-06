# Nommage compréhensible et types TypeScript

Lire cette référence avant toute création ou modification de nom. Les mots complets, les préfixes explicites et l’absence d’abréviations contrôlées sont obligatoires.

<!-- preserved-source-part-start: frontend-section-10 -->
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

<!-- preserved-source-part-end: frontend-section-10 -->

<!-- preserved-source-part-start: frontend-section-11 -->
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

<!-- preserved-source-part-end: frontend-section-11 -->
