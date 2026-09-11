# Architecture modulaire Next.js

Lire ce document avant de créer, déplacer ou exposer un module, une fonctionnalité, une route, une source de données ou une responsabilité partagée.

## Reconnaître le projet réel

Avant de proposer une architecture, relever :

- la version exacte de Next.js et de React dans `package.json` et le fichier de verrouillage des dépendances ;
- la présence de `app/`, `pages/` ou des deux ;
- l’usage éventuel de `src/` ;
- le mode de sortie et les options actives de `next.config.*` ;
- les environnements d’exécution réellement ciblés ;
- l’hébergement sur une seule instance, plusieurs instances, une plateforme spécialisée ou une sortie statique ;
- les conventions déjà établies dans le projet.

Ne jamais appliquer une règle dépendante d’une version en se fondant uniquement sur la mémoire. Vérifier la documentation officielle correspondant à la version installée.

## Principe d’organisation

Next.js fournit le routage et les frontières d’exécution. Il ne doit pas devenir le découpage métier complet du produit.

L’architecture recommandée sépare :

1. **la couche de routage** : fichiers spéciaux de Next.js, composition de page, chargement, erreurs et métadonnées ;
2. **les modules métier** : grands domaines stables tels que facturation, comptes clients ou catalogue ;
3. **les fonctionnalités** : capacités utilisateur cohérentes appartenant à un module ;
4. **les responsabilités partagées** : système de design, fonctionnalités transversales et infrastructure générique ;
5. **les frontières serveur** : accès aux données, sessions, autorisations, traitements serveur et intégrations externes.

Une route peut exposer une fonctionnalité. Elle n’en devient pas automatiquement propriétaire.

## Structure de référence

Adapter cette structure à l’existant sans déplacer inutilement du code valide :

```text
src/
├── app/
│   ├── (public)/
│   ├── (authenticated)/
│   ├── api/
│   ├── layout.tsx
│   ├── loading.tsx
│   ├── error.tsx
│   ├── not-found.tsx
│   └── global-error.tsx
├── modules/
│   └── billing/
│       ├── billing-module-manifest.ts
│       ├── public/
│       ├── features/
│       ├── shared-module/
│       ├── server/
│       └── tests/
├── shared/
│   ├── design-system/
│   ├── features/
│   └── kernel/
└── configuration/
```

Le dossier `src/` est facultatif. Le projet doit choisir une seule convention et l’appliquer de façon cohérente.

Les groupes de routes entre parenthèses organisent les sections sans modifier l’adresse publique. Les dossiers privés commençant par un trait de soulignement peuvent signaler une implémentation non routable. Ces conventions ne remplacent pas les modules métier.

## Responsabilité de la couche `app/`

Les fichiers `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`, `template.tsx`, `default.tsx` et `route.ts` ont une signification imposée par Next.js.

Ils devraient rester limités à :

- lire et valider les paramètres de route ;
- résoudre le contexte de requête nécessaire ;
- appeler une capacité publique de module ;
- composer la page, la mise en page ou la réponse ;
- définir les métadonnées ;
- placer les frontières de chargement et d’erreur ;
- convertir une réponse métier en protocole réseau lorsqu’un gestionnaire de route est requis.

Ils ne devraient pas contenir :

- une politique d’autorisation dupliquée ;
- une requête de base de données complexe ;
- une transformation métier réutilisable ;
- une intégration externe non isolée ;
- un catalogue de permissions ;
- une logique de marque ou d’organisation cliente codée en dur.

## Définition d’un module

Un module représente une responsabilité métier stable, avec :

- un nom complet ;
- un manifeste décrivant sa responsabilité et ses dépendances ;
- une interface publique ;
- des fonctionnalités internes ;
- des règles de permissions ;
- des responsabilités serveur identifiables ;
- des tests de frontières.

Créer un module uniquement lorsque la responsabilité possède son propre vocabulaire métier, ses propres règles et une évolution raisonnablement indépendante. Ne pas créer un module pour chaque page ou chaque table de données.

### Structure de module

```text
modules/billing/
├── billing-module-manifest.ts
├── public/
│   ├── billing-public-components.ts
│   ├── billing-public-server-services.ts
│   └── billing-public-types.ts
├── features/
│   └── invoice-payment/
├── shared-module/
│   ├── components/
│   ├── server/
│   ├── validation/
│   └── types/
├── server/
│   ├── billing-data-access/
│   ├── billing-authorization/
│   └── billing-integrations/
└── tests/
```

Le nom `server/` indique que le contenu ne doit pas entrer dans le graphe de dépendances livré au navigateur. Ajouter une protection telle que le paquet `server-only` lorsque le projet l’utilise.

## Définition d’une fonctionnalité

Une fonctionnalité correspond à une capacité utilisateur ou métier cohérente. Elle appartient à un seul module.

```text
features/invoice-payment/
├── components/
├── server-actions/
├── server-queries/
├── validation/
├── permissions/
├── types/
├── tests/
└── invoice-payment-feature-manifest.ts
```

Tous ces dossiers ne sont pas obligatoires. Créer uniquement ceux qui portent une responsabilité réelle.

Une fonctionnalité ne doit pas importer directement les détails internes d’une autre fonctionnalité. Elle passe par l’interface publique du module concerné ou par une capacité partagée explicitement promue.

## Niveaux de partage

Utiliser le niveau le plus restreint qui répond au besoin :

1. **privé à la fonctionnalité** : utilisé par une seule fonctionnalité ;
2. **partagé dans le module** : utilisé par plusieurs fonctionnalités du même module ;
3. **fonctionnalité transversale** : capacité métier ou utilisateur utilisée par plusieurs modules ;
4. **infrastructure partagée** : mécanisme générique sans règle métier ;
5. **système de design** : primitives visuelles et règles d’interface.

Ne promouvoir un élément qu’après avoir identifié au moins deux consommateurs réels ou une frontière architecturale qui exige immédiatement ce partage. Une ressemblance de code ne suffit pas.

## Matrice de dépendances

| Source | Dépendance autorisée |
|---|---|
| Couche de routage | Interfaces publiques des modules, configuration et responsabilités partagées autorisées |
| Fonctionnalité | Éléments internes de la même fonctionnalité, partage du même module, interface publique d’un autre module |
| Partage du module | Infrastructure du même module et responsabilités globales autorisées |
| Fonctionnalité transversale | Interfaces publiques des modules selon un contrat documenté |
| Infrastructure partagée | Bibliothèques génériques et configuration, jamais une règle métier concrète |
| Système de design | Primitives visuelles, tokens, accessibilité et dépendances visuelles approuvées |

Les importations circulaires sont interdites. Les chemins d’importation doivent être contrôlés par les règles de code ou un outil d’analyse de dépendances lorsque la taille du projet le justifie.

## Interface publique d’un module

L’interface publique expose uniquement les composants, services serveur, types et événements nécessaires aux consommateurs autorisés.

Éviter les fichiers d’exportation qui réexportent l’intégralité d’un module. Une interface publique trop large supprime la frontière qu’elle prétend créer.

Séparer clairement :

- les exports utilisables côté serveur ;
- les exports utilisables côté navigateur ;
- les types sans effet d’exécution ;
- les contrats réellement stables.

Ne pas réexporter un module exclusivement serveur depuis un point d’entrée susceptible d’être importé par un composant client.

## Frontières serveur et navigateur

Les composants serveur sont le choix par défaut. Les composants client sont réservés aux besoins réels : événements, état local interactif, effets de cycle de vie et interfaces du navigateur.

Placer la frontière `use client` au niveau le plus bas raisonnable. Un composant serveur peut composer un petit composant client. Une bibliothèque nécessitant le navigateur doit être isolée derrière une frontière explicite.

Les propriétés transmises du serveur vers le navigateur doivent être sérialisables, minimisées et dépourvues de secret. Ne pas transmettre un objet de base de données complet lorsqu’un objet de transfert limité suffit.

Lire [Routage, rendu et cache](routing-rendering-and-cache.md) pour les règles détaillées.

## Produit multi-organisation et personnalisable

L’organisation cliente active doit être déterminée à partir d’une source serveur vérifiée : session, domaine validé, association utilisateur ou paramètre signé et autorisé.

Chaque accès aux données doit inclure la portée de l’organisation lorsque le modèle métier l’exige. Le simple fait que l’interface affiche la bonne organisation n’est pas une preuve d’isolation.

Les éléments suivants doivent pouvoir varier sans modification du code métier lorsqu’ils sont concernés :

- marque, logo, couleurs et typographie ;
- domaine public et adresses canoniques ;
- langue, fuseau horaire et devise ;
- fonctionnalités disponibles et limites de plan ;
- textes légaux et coordonnées de support ;
- métadonnées des pages publiques.

Résoudre le thème et les métadonnées assez tôt pour éviter l’affichage d’une mauvaise marque ou l’indexation d’informations appartenant à une autre organisation.

## Système de design

Les composants ne doivent pas coder directement des couleurs de marque ou des espacements arbitraires. Utiliser :

- des tokens fondamentaux pour les valeurs brutes ;
- des tokens sémantiques pour l’intention ;
- des tokens de composant lorsque la primitive l’exige ;
- des thèmes de marque résolus depuis une configuration validée.

Les thèmes clair, sombre, système et contraste élevé sont des capacités à évaluer selon le produit. Ils ne doivent pas être simulés par quelques remplacements de couleurs incomplets.

Les fournisseurs de contexte destinés au navigateur doivent être placés aussi profondément que possible pour limiter le code client.

## Configuration

Séparer :

- la configuration disponible au moment de la construction ;
- la configuration résolue au démarrage du serveur ;
- la configuration déterminée pour chaque requête ;
- la configuration publique pouvant être envoyée au navigateur ;
- les secrets exclusivement serveur.

Toute variable exposée au navigateur doit être considérée publique. Les variables utilisant le préfixe public imposé par Next.js ne doivent contenir aucun secret.

Valider la configuration avec un schéma au point d’entrée approprié. Une configuration obligatoire absente doit provoquer une erreur compréhensible avant qu’elle ne produise un comportement partiel ou dangereux.

## Pages publiques, métadonnées et internationalisation

Pour une page publique indexable :

- choisir une adresse stable et canonique ;
- produire un titre et une description propres à la page ;
- générer les métadonnées sur le serveur ;
- fournir les variantes de langue lorsqu’elles existent ;
- produire un plan de site et des règles d’indexation cohérents ;
- tester le contenu HTML initial et les images de partage ;
- éviter toute fuite de marque ou d’organisation dans le cache de métadonnées.

Pour une page privée, empêcher l’indexation et ne pas exposer de donnée sensible dans les métadonnées.

## Pages Router existant

Le Pages Router reste une réalité dans de nombreux projets. Lorsqu’il est présent :

- appliquer ses conventions réelles plutôt que celles de l’App Router ;
- ne pas utiliser des traitements serveur de l’App Router dans une zone qui ne les supporte pas ;
- isoler les nouvelles responsabilités pour faciliter une migration future sans la rendre obligatoire ;
- documenter les différences de chargement de données, d’erreur et de mise en page ;
- tester les navigations entre les deux systèmes lorsqu’ils coexistent.

Une migration doit disposer de critères d’acceptation, d’un plan de retour et de preuves d’équivalence fonctionnelle.

## Dépendances et fonctions expérimentales

Avant d’ajouter une dépendance ou d’activer une fonction expérimentale :

1. confirmer le besoin non couvert ;
2. vérifier la compatibilité avec les versions installées et le mode d’exécution ;
3. évaluer le poids envoyé au navigateur et le coût serveur ;
4. vérifier la sécurité, la maintenance et la licence ;
5. prévoir les tests et la stratégie de retrait ;
6. documenter la décision.

Ne pas remplacer une fonction stable du framework par une bibliothèque sans bénéfice démontré.

## Contrôle architectural

Avant livraison, vérifier :

- que chaque route appelle une capacité dont la responsabilité est claire ;
- que chaque fonctionnalité appartient à un module ;
- que les fichiers spéciaux du framework restent minces ;
- que les frontières serveur et client sont minimales et explicites ;
- que les importations respectent la matrice ;
- que les données et caches sont isolés par organisation et utilisateur lorsque nécessaire ;
- que les thèmes, métadonnées et configurations ne sont pas codés en dur ;
- que les anciennes conventions du projet n’ont pas été remplacées sans justification ;
- que les tests de frontières couvrent les chemins critiques.

## Sources officielles à vérifier selon la version

- [Structure de projet Next.js](https://nextjs.org/docs/app/getting-started/project-structure)
- [Composants serveur et composants client](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Guide d’authentification Next.js](https://nextjs.org/docs/app/guides/authentication)
