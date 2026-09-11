# Organisation du dépôt et dépendances

Lire ce document avant de créer, déplacer ou partager un dossier, un fichier, un module, une fonctionnalité ou un point d’entrée.

## Objectif de lisibilité

Une personne qui découvre le dépôt doit pouvoir répondre sans lire tout le code :

- où se trouve une capacité métier ;
- où entre une requête ;
- où se décide une règle ;
- où une donnée est lue ou modifiée ;
- quel module possède une table ou une permission ;
- quel code part dans le navigateur ;
- quel code dépend d’un fournisseur externe ;
- où se trouvent les tests et migrations.

L’arborescence doit décrire les responsabilités, pas seulement les technologies.

## Arborescence de référence

Adapter cette structure à l’existant sans déplacement général injustifié :

```text
src/
├── app/
│   ├── (public)/
│   ├── (authenticated)/
│   ├── api/
│   ├── layout.tsx
│   ├── loading.tsx
│   ├── error.tsx
│   └── not-found.tsx
├── modules/
│   └── billing/
│       ├── billing-module-manifest.ts
│       ├── public-interface/
│       ├── features/
│       ├── shared-module/
│       └── tests/
├── shared/
│   ├── design-system/
│   ├── server-infrastructure/
│   ├── browser-infrastructure/
│   └── cross-module-capabilities/
├── configuration/
└── instrumentation.ts
database/
├── migrations/
├── seeds/
└── documentation/
tests/
├── integration/
├── end-to-end/
└── support/
```

Le dossier `src/` est facultatif. Le projet choisit une convention et l’applique partout.

## Responsabilité de `app/`

Les fichiers spéciaux de Next.js doivent rester centrés sur :

- lecture et validation des paramètres ;
- résolution minimale du contexte de requête ;
- appel d’une interface publique de module ;
- composition de page et métadonnées ;
- conversion d’un résultat en réponse réseau ;
- frontière de chargement ou d’erreur.

Ils ne doivent pas posséder :

- requête de données complexe ;
- transaction métier ;
- règle de permission dupliquée ;
- appel fournisseur non adapté ;
- transformation métier réutilisable ;
- logique de cache dispersée.

## Structure d’un module

```text
modules/billing/
├── billing-module-manifest.ts
├── public-interface/
│   ├── billing-public-use-cases.ts
│   ├── billing-public-server-components.ts
│   └── billing-public-types.ts
├── features/
│   └── invoice-payment/
│       ├── presentation/
│       │   ├── components/
│       │   ├── server-actions/
│       │   └── route-adapters/
│       ├── application/
│       │   ├── use-cases/
│       │   ├── authorization-policies/
│       │   └── result-types/
│       ├── domain/
│       ├── data-access/
│       └── tests/
├── shared-module/
│   ├── application/
│   ├── domain/
│   ├── data-access/
│   └── integrations/
└── tests/
```

Créer uniquement les dossiers portant une responsabilité réelle. Un petit module n’a pas besoin de tous ces niveaux physiques si les frontières restent visibles.

## Fonctionnalités dans un module

Une fonctionnalité contient un parcours cohérent de bout en bout. Elle ne devient pas un module uniquement parce qu’elle possède une page ou une table.

Les responsabilités utilisées par une seule fonctionnalité restent dans son dossier. Les responsabilités réellement communes montent vers `shared-module/`. Une fonctionnalité transversale à plusieurs modules possède une responsabilité et un emplacement explicitement documentés ; elle ne devient pas un dossier général où déposer les exceptions.

## Manifeste du module

Le manifeste décrit en mots simples :

- responsabilité ;
- capacités publiques ;
- données possédées ;
- permissions ;
- routes et traitements serveur ;
- événements produits et consommés ;
- dépendances autorisées ;
- informations sensibles ;
- contrôles obligatoires.

Le manifeste est une carte, pas une seconde implémentation. Éviter les identifiants codés sans explication.

## Interface publique

Un autre module importe uniquement depuis `public-interface/`. Cette interface expose le minimum stable :

- cas d’usage autorisés ;
- types nécessaires ;
- composants explicitement partageables ;
- événements documentés.

Séparer les exports utilisables sur le serveur de ceux utilisables dans le navigateur. Ne jamais réexporter un client de base de données, un secret ou un adaptateur fournisseur.

Éviter un fichier `index.ts` général qui révèle tout le module. Un fichier d’exportation ciblé peut exister si son nom et sa portée restent explicites.

## Niveaux de partage

Promouvoir un élément seulement au niveau nécessaire :

1. privé à une capacité ;
2. partagé dans le même module ;
3. capacité transversale entre modules ;
4. infrastructure serveur ou navigateur ;
5. système de design.

Deux codes qui se ressemblent ne forment pas automatiquement une abstraction commune. Leur sens, rythme d’évolution et dépendances doivent aussi être communs.

## Matrice de dépendances

| Source | Peut dépendre de |
|---|---|
| `app/` | Interfaces publiques, configuration et adaptateurs de présentation |
| Présentation d’une fonctionnalité | Application de la même fonctionnalité, partage du module, système de design |
| Application d’une fonctionnalité | Domaine de la même fonctionnalité, partage du module, contrats de données et intégrations |
| Domaine | Langage et bibliothèques sans dépendance d’infrastructure approuvées |
| Accès aux données | Domaine, contrats d’application, client de données |
| Intégration | Contrats d’application, client du fournisseur, configuration serveur |
| Infrastructure partagée | Mécanismes génériques, jamais une règle métier concrète |
| Système de design | Primitives visuelles et accessibilité, jamais accès aux données |

Interdire les importations circulaires. Contrôler automatiquement les frontières lorsque la taille du projet le justifie.

## Fichiers serveur et navigateur

Les responsabilités exclusivement serveur doivent être visibles dans leur chemin et protégées contre une importation navigateur. Utiliser la protection `server-only` lorsque compatible.

Ne pas créer un fichier mélangeant :

- une fonction utilisant un secret ;
- un type partagé ;
- un composant navigateur.

Séparer les contrats sans effet d’exécution des implémentations serveur.

## Routes et capacités

Le chemin public d’une route n’impose pas l’emplacement complet du métier. Une route située dans `app/api/billing/invoices/route.ts` appelle une capacité de `modules/billing/`; elle ne possède pas le domaine de facturation.

Une fonctionnalité visible sur plusieurs routes reste une seule capacité métier. Ne pas dupliquer son service et ses permissions par page.

## Données et migrations

Chaque table ou collection a un module propriétaire. Placer les migrations dans l’emplacement reconnu par l’outil, puis documenter leur propriété lorsque l’outil centralise tous les fichiers.

Les données de démonstration, de test et de production doivent être séparées. Un fichier de remplissage initial ne doit contenir aucun secret ni donnée personnelle réelle.

## Tests

- Tests unitaires près du domaine ou du cas d’usage lorsqu’ils facilitent la maintenance.
- Tests d’intégration dans le module ou l’espace d’intégration selon les outils.
- Tests de bout en bout à un emplacement global, organisés par parcours métier.
- Outils et données de test dans un dossier explicitement nommé.

Éviter un dossier global contenant des centaines de tests sans relation visible avec leur responsabilité.

## Croissance du dépôt

Lorsque le dépôt grandit :

- ajouter des contrôles de dépendance avant d’ajouter des couches ;
- mesurer les temps de construction et de test ;
- diviser par domaine lorsque les propriétaires et cycles diffèrent ;
- maintenir une commande commune de validation ;
- rendre les changements transversaux visibles ;
- documenter les contrats entre espaces déployables.

Un dépôt unique peut contenir plusieurs applications si le partage réel et les outils le justifient. Ne pas adopter un gestionnaire de dépôt multiple uniquement pour suivre une mode.

## Interdictions de nommage structurel

Éviter sans responsabilité complémentaire :

- `lib/` ;
- `utils/` ;
- `helpers/` ;
- `services/` ;
- `common/` ;
- `misc/` ;
- `core/` ;
- `data/`.

Préférer `invoice-total-calculation/`, `organization-permission-policy/`, `payment-provider-adapter/` ou `invoice-data-access/`.

## Contrôle avant livraison

- responsabilité de chaque nouveau dossier compréhensible ;
- chaque fonctionnalité rattachée à un seul module ;
- responsabilités locales conservées dans leur fonctionnalité ;
- route mince et rattachée à un module ;
- cas d’usage et domaine séparés de Next.js ;
- accès aux données et intégrations privés ;
- exports serveur et navigateur séparés ;
- dépendances conformes à la matrice ;
- absence de cycle ;
- migrations rattachées à un propriétaire ;
- tests découvrables par capacité ;
- aucun déplacement hors périmètre sans raison.

## Source officielle

- [Structure de projet Next.js](https://nextjs.org/docs/app/getting-started/project-structure)
