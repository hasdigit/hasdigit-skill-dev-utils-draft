# Permissions et isolation des organisations clientes

Lire ce document pour toute route, page privée, donnée sensible, traitement serveur, gestionnaire de route, action utilisateur ou fonctionnalité conditionnelle.

## Concepts distincts

- **Authentification** : vérifier l’identité de la personne.
- **Session** : conserver de manière sûre l’état de connexion entre les requêtes.
- **Autorisation** : décider ce que cette personne peut lire ou modifier.
- **Organisation cliente** : périmètre métier auquel appartiennent les données et les droits; la documentation Next.js et de nombreux produits utilisent le mot tenant.

Ne pas réduire ces concepts au mot abrégé `auth`. Un contrôle d’identité ne prouve pas une autorisation, et une autorisation globale ne prouve pas l’accès à une ressource particulière.

## Autorité serveur obligatoire

L’interface peut masquer, désactiver ou expliquer une action. La décision de sécurité reste sur le serveur.

Chaque accès sensible doit vérifier au plus près de la donnée ou de la modification :

1. la session ;
2. l’utilisateur ;
3. l’organisation cliente active ;
4. la permission ou politique ;
5. l’appartenance de la ressource à cette organisation ;
6. les contraintes métier complémentaires.

Une vérification dans `layout.tsx`, dans un composant parent ou dans un fichier d’interception de requêtes ne remplace pas ces contrôles.

## Choisir le modèle de permission

### Permissions fines

Utiliser des capacités métier explicites lorsque le produit exige un contrôle détaillé :

```text
billing.invoice.read
billing.invoice.payment.create
billing.invoice.payment.cancel
```

### Rôles

Un rôle regroupe plusieurs permissions pour faciliter l’administration. Le code métier ne devrait pas dupliquer des conditions de rôle partout; il devrait demander la capacité nécessaire à une politique centrale.

### Attributs et contexte

Une politique peut aussi utiliser la propriété de la ressource, l’organisation, le plan, l’état du document ou une relation métier. Documenter ces attributs et les charger depuis des sources fiables.

### Modèle recommandé

Pour un produit professionnel, utiliser généralement :

- des permissions métier stables ;
- des rôles configurables qui regroupent ces permissions ;
- des règles contextuelles pour la ressource et l’organisation ;
- une décision serveur centralisée et testable.

## Propriété des permissions

Une permission appartient au module ou à la fonctionnalité qui définit la capacité métier.

- Une permission couvrant tout un domaine appartient au module.
- Une permission propre à une capacité appartient à la fonctionnalité.
- Une permission partagée entre plusieurs interfaces conserve une seule identité métier.

Ne pas créer une permission pour la page, une autre pour le bouton et une troisième pour le traitement serveur lorsqu’elles représentent la même capacité. Ces surfaces appliquent la même permission.

## Catalogue et manifestes

Le catalogue de permissions doit être une source versionnée et vérifiable, généralement TypeScript strict. Un fichier de données structurées peut servir de source de génération si le projet contrôle les doublons et la cohérence.

Les variables d’environnement ne doivent jamais contenir le catalogue métier. Elles peuvent sélectionner une source ou activer un mécanisme, pas définir les droits du produit.

Chaque fonctionnalité protégée devrait déclarer :

- ses permissions ;
- les routes concernées ;
- les composants concernés ;
- les traitements serveur concernés ;
- les gestionnaires de routes concernés ;
- les preuves de test attendues.

## Couche d’accès aux données

Centraliser les vérifications sécurisées dans une couche d’accès aux données ou un service serveur clairement nommé.

Cette couche :

- vérifie la session ;
- résout l’organisation cliente depuis une source serveur ;
- applique la politique ;
- filtre la requête par organisation ;
- retourne uniquement les champs nécessaires ;
- n’est jamais importée par un composant client.

Utiliser des objets de transfert limités plutôt que des entités complètes. Une donnée non envoyée au navigateur ne peut pas y être exposée accidentellement.

## Composants serveur

Un composant serveur peut effectuer un contrôle rapide pour choisir l’interface, mais la fonction qui charge la donnée doit aussi appliquer l’autorisation sécurisée.

Ne pas se fier uniquement à une mise en page protégée. Les composants imbriqués, traitements serveur et gestionnaires de routes possèdent leurs propres points d’entrée.

## Composants client

Un composant client peut :

- cacher une action impossible ;
- désactiver un contrôle avec une raison ;
- afficher un message de refus ;
- éviter une requête inutile.

Il ne peut pas :

- décider seul d’une autorisation ;
- contenir le catalogue complet si celui-ci révèle des informations non nécessaires ;
- stocker un secret ;
- accepter la réussite avant la réponse serveur.

Le serveur doit toujours pouvoir refuser une demande fabriquée en dehors de l’interface.

## Traitements serveur

Chaque traitement serveur doit être considéré comme un point d’entrée public par le réseau.

Avant toute lecture sensible ou modification :

1. valider l’entrée ;
2. vérifier la session ;
3. résoudre l’organisation ;
4. vérifier la permission ;
5. charger la ressource dans la même portée ;
6. appliquer la règle métier ;
7. modifier de manière sûre ;
8. invalider les caches concernés ;
9. retourner un résultat limité et compréhensible.

Ne pas faire confiance à une valeur cachée de formulaire, une propriété de composant, une fermeture de fonction ou un identifiant généré par le framework.

## Gestionnaires de routes

Chaque méthode de `route.ts` applique les mêmes contrôles qu’une interface de programmation publique : authentification, autorisation, validation, limitation des données et journalisation sûre.

Une méthode de lecture et une méthode de modification peuvent exiger des permissions différentes. Les déclarer séparément.

Pour les intégrations externes, distinguer :

- session utilisateur ;
- clé de service ;
- signature de webhook ;
- jeton à portée limitée.

Chaque mécanisme possède sa propre politique et ne doit pas être confondu avec les autres.

## Fichier d’interception de requêtes

Le fichier `proxy.ts` ou, pour les versions qui l’utilisent encore, `middleware.ts`, peut effectuer un contrôle optimiste et rediriger rapidement.

Il ne doit pas :

- charger toute la politique métier ;
- être l’unique protection ;
- supposer qu’une route cachée est inaccessible ;
- exposer des détails de permission dans une redirection.

## Isolation des organisations clientes

L’organisation active doit provenir d’une association vérifiée entre l’utilisateur, la session, le domaine ou une autre source serveur autorisée.

Interdire :

- une requête filtrée uniquement par un identifiant reçu du navigateur ;
- un cache partagé sans clé d’organisation ;
- une invalidation qui mélange plusieurs organisations ;
- un journal contenant des données d’une autre organisation ;
- une métadonnée ou une image de partage provenant d’une organisation précédente ;
- un traitement différé sans contexte d’organisation signé ou revalidé.

Les tests doivent tenter explicitement un accès croisé entre deux organisations.

## Cache des permissions

Une permission peut être mise en cache seulement si :

- la clé inclut l’utilisateur, l’organisation et la version de politique nécessaires ;
- la durée de validité est définie ;
- les changements de rôle ou d’appartenance invalident le cache ;
- un refus sûr est possible lorsque le cache est absent ou incohérent ;
- les instances de production partagent ou coordonnent le cache lorsque nécessaire.

Ne jamais mettre en cache globalement une décision personnalisée.

## États de refus

Distinguer :

- utilisateur non connecté ;
- utilisateur connecté mais non autorisé ;
- ressource absente ;
- ressource appartenant à une autre organisation ;
- fonctionnalité indisponible dans le plan ;
- autorisation temporairement impossible à vérifier.

Le message utilisateur doit être utile sans révéler l’existence d’une ressource sensible. Le journal technique peut conserver un code de diagnostic expurgé.

## Tests obligatoires

Pour toute capacité protégée :

- accès autorisé ;
- session absente ;
- permission absente ;
- rôle modifié ;
- ressource absente ;
- identifiant falsifié ;
- tentative d’accès à une autre organisation ;
- appel direct du traitement serveur ;
- appel direct du gestionnaire de route ;
- interface masquée mais requête fabriquée ;
- cache de permission expiré ou invalidé ;
- modification répétée.

## Sources officielles

- [Guide d’authentification et d’autorisation Next.js](https://nextjs.org/docs/app/guides/authentication)
- [Directive serveur et considérations de sécurité](https://nextjs.org/docs/app/api-reference/directives/use-server)
