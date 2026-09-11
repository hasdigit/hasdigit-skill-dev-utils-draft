# Architecture fullstack et frontières

Lire ce document avant de choisir une couche, un point d’entrée, une base de données, une intégration ou une extraction de service.

## Comprendre le système réel

Relever avant toute proposition :

- version exacte de Next.js, React et TypeScript ;
- App Router, Pages Router ou coexistence ;
- modes d’exécution serveur réellement disponibles ;
- système de données, outil de migration et contraintes ;
- cache local ou partagé ;
- hébergement sur une ou plusieurs instances ;
- files de travail et tâches planifiées ;
- consommateurs des routes HTTP ;
- frontières déjà établies et conventions du projet.

Une architecture cible ne justifie pas une réorganisation générale. Adapter la décision à l’existant et au périmètre demandé.

## Responsabilités fondamentales

### Présentation

Affiche les informations, recueille l’intention et rend les états compréhensibles. Elle ne décide pas seule d’une autorisation et ne contient pas les secrets.

### Transport

Convertit une requête ou un formulaire en entrée du système, puis convertit le résultat en réponse. Les gestionnaires de routes Next.js et les traitements serveur appartiennent à cette frontière.

### Application

Orchestre un cas d’usage complet : validation métier, autorisation, transaction, appel du domaine, persistance, événement et résultat. Cette couche exprime ce que le produit fait.

### Domaine

Contient les règles métier stables, les états autorisés, les valeurs et les décisions qui restent vraies indépendamment de Next.js ou de la base de données.

### Données

Traduit les besoins du domaine vers la persistance, applique les filtres d’organisation et gère les détails du moteur de données.

### Intégrations

Adapte un fournisseur de paiement, de messagerie, de stockage ou un autre service. Le fournisseur ne doit pas imposer son vocabulaire à tout le domaine.

### Exploitation

Assure configuration, secrets, journaux, mesures, santé, déploiement, sauvegarde et récupération.

## Direction des dépendances

Le domaine ne dépend pas :

- de Next.js ;
- de React ;
- d’un objet de requête réseau ;
- d’un client de base de données ;
- d’un fournisseur externe ;
- d’un outil de journalisation concret.

La couche application dépend du domaine et de contrats abstraits. Les adaptateurs de données et d’intégration mettent en œuvre ces contrats. Next.js appelle les cas d’usage ; les cas d’usage n’appellent pas Next.js.

Cette direction permet de tester les règles sans serveur web et de remplacer un adaptateur sans réécrire le métier.

## Module métier vertical

Un module possède une responsabilité métier stable, par exemple facturation, catalogue ou identité client. Il rassemble ses cas d’usage, domaine, interfaces publiques et adaptateurs privés.

Un module doit avoir :

- un nom complet ;
- une responsabilité et des limites ;
- une interface publique réduite ;
- une propriété claire des données ;
- des permissions définies ;
- des événements documentés ;
- des tests de frontières ;
- une politique de dépendance.

Ne pas créer un module pour chaque page, table ou méthode réseau. Ne pas fusionner des domaines différents dans un module vague appelé `core` ou `common`.

## Fonctionnalité verticale

Une fonctionnalité représente une capacité utilisateur ou métier cohérente appartenant à un seul module, par exemple créer une facture ou enregistrer un paiement.

Elle regroupe au niveau le plus local possible :

- présentation ;
- adaptateurs de route ou traitements serveur ;
- cas d’usage ;
- règles du domaine propres à cette capacité ;
- accès aux données spécifiques ;
- tests.

Une fonctionnalité ne dépend pas directement des détails privés d’une autre fonctionnalité. Elle passe par l’interface publique du module ou par un élément explicitement partagé dans ce module.

Promouvoir une responsabilité vers le partage du module seulement lorsqu’au moins deux fonctionnalités l’utilisent réellement ou lorsqu’un invariant du module doit être unique dès l’origine.

## Cas d’usage

Un cas d’usage représente une intention complète : créer une facture, enregistrer un paiement, inviter un membre ou publier un produit.

Il doit :

1. recevoir une entrée validée techniquement ;
2. résoudre l’acteur et l’organisation depuis une source fiable ;
3. vérifier la permission et la ressource ;
4. charger les données nécessaires ;
5. appliquer les règles métier ;
6. persister dans une transaction adaptée ;
7. enregistrer les événements ou tâches durables ;
8. retourner un résultat limité et compréhensible.

Éviter les services généraux contenant des dizaines de méthodes sans intention métier identifiable.

## Frontières Next.js

### Composant serveur

Utiliser pour charger et composer une interface sur le serveur. Il appelle directement une lecture ou un cas d’usage autorisé, sans passer par une route réseau interne.

### Composant navigateur

Utiliser pour les interactions nécessitant événements, état local, effets ou fonctions du navigateur. La frontière `use client` doit rester petite et ne recevoir que des données sérialisables et non sensibles.

### Traitement serveur

Utiliser principalement pour une mutation initiée par l’interface Next.js. Il adapte le formulaire ou l’intention, applique les contrôles serveur et appelle un cas d’usage. Il ne constitue pas automatiquement un contrat stable pour des consommateurs externes.

### Gestionnaire de route

Utiliser pour une véritable frontière réseau : application externe, application mobile, webhook, fichier, intégration ou contrat public. Chaque méthode exportée est accessible indépendamment de l’interface.

### Interception de requête

Le fichier `proxy.ts`, ou `middleware.ts` dans les versions antérieures, peut rediriger ou appliquer un contrôle préliminaire. Il ne remplace pas les autorisations dans les cas d’usage et accès aux données.

## Choisir Next.js ou un service séparé

Conserver le backend dans Next.js lorsque :

- il sert principalement le même produit web ;
- les durées d’exécution sont compatibles avec l’hébergement ;
- les besoins de montée en charge restent proches ;
- les contrats externes sont limités et maîtrisés ;
- l’équipe bénéficie d’un déploiement cohérent ;
- les fonctions du framework couvrent réellement le besoin.

Évaluer un service séparé lorsque :

- plusieurs produits indépendants consomment le même domaine ;
- les versions du backend doivent évoluer séparément ;
- des connexions longues ou protocoles non supportés sont centraux ;
- des traitements lourds doivent survivre aux requêtes et redémarrages ;
- la charge, la disponibilité ou la sécurité exigent une isolation distincte ;
- une technologie spécialisée apporte un bénéfice démontré.

Ne pas extraire prématurément. Une architecture interne propre conserve l’option d’extraction sans en payer immédiatement le coût opérationnel.

## Frontière de transaction

La couche application définit l’unité métier qui doit réussir ou échouer ensemble. La couche de données réalise la transaction avec le moteur choisi.

Un appel externe ne participe généralement pas à la même transaction locale. Utiliser selon le risque :

- écriture d’un événement durable dans la même transaction ;
- traitement ultérieur avec répétition sûre ;
- état intermédiaire explicite ;
- opération de compensation documentée.

Ne pas maintenir une transaction de base de données ouverte pendant un appel réseau lent sans justification précise.

## Cohérence entre modules

Un module ne modifie pas directement les tables privées d’un autre module. Il utilise :

- l’interface publique du module dans le même processus ;
- un événement documenté ;
- un contrat réseau lorsqu’il s’agit d’un service séparé.

Chaque donnée possède un propriétaire. Une vue de lecture combinée peut agréger plusieurs sources sans transférer la propriété des écritures.

## Architecture multi-organisation

L’organisation active est résolue côté serveur à partir d’une relation vérifiée. Elle traverse explicitement les cas d’usage, politiques, accès aux données, caches, événements et journaux autorisés.

Éviter une variable globale contenant l’organisation courante. Dans un serveur concurrent, elle peut mélanger deux requêtes.

L’isolation doit être défendue à plusieurs niveaux adaptés :

- validation de session ;
- permission sur la ressource ;
- filtre de requête ;
- contrainte ou politique de base de données lorsque disponible ;
- clé de cache ;
- test croisé entre organisations.

## Architecture évolutive

Préparer l’évolution par :

- contrats internes limités ;
- noms métier stables ;
- dépendances dirigées ;
- migrations compatibles ;
- événements versionnés ;
- tests aux frontières ;
- mesures par cas d’usage ;
- décisions documentées avec conditions de révision.

Ne pas ajouter une couche abstraite uniquement parce qu’elle pourrait servir un jour. Une abstraction doit protéger une frontière réelle, réduire une duplication significative ou permettre un remplacement plausible.

## Contrôle architectural

- Chaque route et traitement serveur appelle un cas d’usage identifiable.
- Chaque cas d’usage appartient à un module.
- Le domaine reste indépendant des outils.
- Les accès aux données ne remontent pas vers l’interface.
- Les intégrations externes sont derrière des adaptateurs.
- Les transactions suivent les unités métier.
- Les événements durables sont enregistrés sans perte possible démontrée.
- Les organisations sont isolées dans lectures, écritures, caches et tâches.
- Le choix entre Next.js et service séparé est justifié par des contraintes réelles.

## Sources officielles

- [Next.js comme backend pour son frontend](https://nextjs.org/docs/app/guides/backend-for-frontend)
- [Composants serveur et composants navigateur](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Sécurité des données Next.js](https://nextjs.org/docs/app/guides/data-security)
