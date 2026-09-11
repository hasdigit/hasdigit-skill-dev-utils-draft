# Routage, rendu et cache Next.js

Lire ce document pour toute modification touchant `app/`, `pages/`, une frontière serveur ou navigateur, une source de données, un traitement serveur, un gestionnaire de route, une métadonnée ou un cache.

## Décision fondée sur la version

Le comportement de rendu et de cache de Next.js évolue. Avant de décider :

1. relever la version installée ;
2. inspecter `next.config.*` et les options actives ;
3. déterminer si le projet utilise les composants de cache récents ou le modèle précédent ;
4. vérifier les capacités de l’hébergement ;
5. lire la documentation officielle de cette version.

Ne jamais écrire « Next.js met toujours en cache » ou « Next.js ne met jamais en cache » sans préciser la version, la configuration, l’API et la donnée concernées.

## Routage avec l’App Router

Dans l’App Router, les dossiers représentent des segments d’adresse et les fichiers spéciaux définissent leur comportement.

- `page.tsx` rend une page accessible ;
- `layout.tsx` partage une mise en page persistante ;
- `template.tsx` recrée une partie de l’arbre à chaque navigation ;
- `loading.tsx` fournit une interface de chargement liée à une frontière d’attente ;
- `error.tsx` capture les erreurs de son segment et s’exécute côté navigateur ;
- `global-error.tsx` traite les erreurs non capturées au niveau racine ;
- `not-found.tsx` fournit l’interface d’absence ;
- `default.tsx` fournit une solution de repli pour une route parallèle ;
- `route.ts` expose un point d’entrée réseau.

Un dossier n’est pas une route publique tant qu’il ne contient pas un fichier qui l’expose. Malgré cela, ne compter ni sur la profondeur du dossier ni sur l’absence d’un lien visible pour protéger une donnée.

## Paramètres et état dans l’adresse

Valider les paramètres de segments dynamiques et les paramètres de recherche avant usage. Ils proviennent d’une entrée externe.

Placer dans l’adresse les états qui doivent être partageables, rechargeables ou compatibles avec la navigation : page courante, filtre, tri, recherche et onglet significatif.

Ne pas placer dans l’adresse un secret, une donnée personnelle non nécessaire ou un état interne temporaire.

Les mises en page ne doivent pas être utilisées comme unique point d’autorisation. Des navigations partielles et d’autres points d’entrée peuvent contourner une hypothèse fondée uniquement sur l’affichage du parent.

## Composants serveur par défaut

Utiliser un composant serveur lorsque le composant :

- lit une donnée sur le serveur ;
- accède à un secret ou à une intégration privée ;
- ne dépend pas d’un événement du navigateur ;
- peut réduire le code envoyé au navigateur ;
- compose du contenu qui peut être rendu progressivement.

Un composant serveur peut appeler directement une fonction serveur autorisée. Éviter un aller-retour réseau vers un gestionnaire de route interne lorsque ce réseau n’apporte aucune frontière utile.

## Composants client limités

Utiliser un composant client seulement lorsqu’il a besoin :

- d’événements interactifs ;
- d’un état local ;
- d’un effet de cycle de vie ;
- d’une interface propre au navigateur ;
- d’une bibliothèque qui exige le navigateur.

La directive `use client` marque une frontière. Les modules importés sous cette frontière peuvent entrer dans le code livré au navigateur. Vérifier leurs dépendances, leur poids et leurs données.

Les valeurs transmises à un composant client doivent être sérialisables. Transmettre un objet limité à l’usage de l’interface, jamais une entité complète contenant des champs inutiles ou sensibles.

## Choisir une stratégie de rendu

La stratégie doit être décidée par route et par source de données :

- **rendu préparé à l’avance** pour un contenu identique entre visiteurs et suffisamment stable ;
- **rendu dynamique sur le serveur** pour un contenu dépendant de la requête, de la session ou de données fraîches ;
- **mise en cache avec revalidation** pour un contenu partageable qui accepte une fraîcheur définie ;
- **rendu dans le navigateur** pour une interaction qui ne peut pas être produite utilement sur le serveur ;
- **chargement progressif** pour afficher rapidement une structure utile pendant l’arrivée des parties lentes.

Documenter la raison, la fraîcheur attendue, la portée du cache, la stratégie d’erreur et la preuve de comportement.

Ne pas forcer une page entière en rendu dynamique parce qu’une petite partie dépend de la requête. Isoler la partie dynamique lorsque le framework et la version le permettent sans complexité disproportionnée.

## Chargement des données

- Charger les données au plus près de la responsabilité qui les utilise.
- Exécuter en parallèle les lectures indépendantes.
- Éviter les chaînes de requêtes séquentielles non nécessaires.
- Dédupliquer ou mémoriser une lecture répétée dans une même requête lorsque la solution est compatible avec la version.
- Limiter les champs retournés au navigateur.
- Annuler ou rendre obsolètes les demandes client dépassées.
- Afficher une interface de chargement proportionnée plutôt qu’un écran vide.

Une lecture serveur doit appliquer l’autorisation au niveau de la donnée. Un composant qui ne rend pas un champ ne protège pas ce champ si celui-ci a déjà été envoyé au navigateur.

## Politique de cache obligatoire

Pour chaque donnée métier, documenter :

- si elle peut être mise en cache ;
- si elle est publique, propre à une organisation ou propre à un utilisateur ;
- la clé d’isolation ;
- la durée ou condition de fraîcheur ;
- le mécanisme d’invalidation ;
- le comportement en cas d’échec d’invalidation ;
- la coordination nécessaire entre plusieurs instances.

### Données publiques

Une donnée publique et identique pour tous peut être partagée si sa fraîcheur est définie et testée.

### Données d’organisation cliente

La clé doit inclure l’identité serveur vérifiée de l’organisation et tous les paramètres qui changent le résultat. Ne pas utiliser un identifiant fourni par le navigateur sans autorisation.

### Données d’utilisateur ou de session

Ne pas placer une réponse personnalisée dans un cache global. Préférer une lecture dynamique ou une portée de cache dont l’isolation est démontrée par des tests.

## Invalidation après modification

Après une modification :

1. confirmer la réussite métier ;
2. invalider la donnée concernée avec le mécanisme le plus précis disponible ;
3. choisir entre visibilité immédiate et actualisation en arrière-plan selon le besoin utilisateur ;
4. éviter l’invalidation générale de routes ou de données non concernées ;
5. vérifier l’effet sur les autres organisations clientes ;
6. tester la lecture qui suit la modification.

Les fonctions de revalidation par étiquette ou par chemin ne sont pas interchangeables. Utiliser les fonctions supportées par la version et vérifier leurs restrictions d’appel.

## Traitements serveur

Un traitement serveur, souvent appelé Server Action dans la documentation Next.js, constitue une frontière réseau même lorsque son appel apparaît directement dans un formulaire ou un composant.

Chaque traitement doit :

- valider les entrées côté serveur ;
- vérifier la session ;
- vérifier l’autorisation sur la ressource et l’organisation ;
- limiter les données retournées ;
- gérer les erreurs attendues ;
- protéger les modifications répétées lorsque nécessaire ;
- invalider les caches concernés ;
- journaliser sans secret ni donnée personnelle inutile.

La fermeture d’une fonction sur une variable serveur ne remplace aucune validation. Ne jamais considérer l’identifiant technique généré pour un traitement comme une autorisation.

Pour les chargements de fichier, contrôler explicitement la taille, le type réel, le nom, le stockage et l’analyse de sécurité. Modifier une limite par défaut uniquement après évaluation du risque de consommation de ressources.

## Gestionnaires de routes

Utiliser `route.ts` lorsque le produit a besoin d’une véritable frontière HTTP : intégration externe, webhook, téléchargement, API consommée hors de l’application ou protocole particulier.

Chaque méthode exportée doit :

- valider le corps, les paramètres et les en-têtes ;
- appliquer authentification et autorisation ;
- vérifier la portée de l’organisation ;
- retourner des statuts et formats cohérents ;
- limiter le débit et la taille lorsque le risque le justifie ;
- traiter les requêtes répétées de manière sûre ;
- définir une politique de cache explicite.

Un webhook doit vérifier la signature sur le contenu brut selon le contrat du fournisseur et se protéger contre la répétition d’un même événement.

## Interception de requêtes

Selon la version, Next.js utilise une convention telle que `proxy.ts` ou l’ancienne convention `middleware.ts` pour intercepter des requêtes.

Cette couche peut effectuer une redirection rapide ou un contrôle optimiste. Elle ne doit pas devenir l’unique protection d’une donnée ni contenir toute la logique d’autorisation.

Maintenir les vérifications sécurisées dans la couche d’accès aux données, les traitements serveur et les gestionnaires de routes.

## Chargement progressif et erreurs

Placer les frontières de chargement au niveau où l’utilisateur peut comprendre ce qui attend. Préférer un squelette stable ou un état local à un indicateur global qui masque tout le produit.

Une frontière d’erreur doit :

- afficher un message compréhensible ;
- offrir une nouvelle tentative seulement si elle est sûre ;
- produire un identifiant de corrélation lorsqu’il existe ;
- ne pas exposer la pile technique ;
- laisser les zones indépendantes continuer à fonctionner lorsque possible.

Les erreurs attendues de validation ou d’autorisation doivent suivre un résultat métier explicite. Les défaillances inattendues doivent remonter vers la frontière appropriée et être observables.

## Métadonnées et indexation

Utiliser l’objet de métadonnées statiques, la fonction de génération dynamique ou les fichiers de métadonnées fournis par Next.js selon le besoin.

Les métadonnées :

- appartiennent à un composant serveur ;
- utilisent une adresse de base et une adresse canonique validées ;
- respectent la marque et la langue actives ;
- ne contiennent aucune donnée privée ;
- disposent d’une stratégie de cache cohérente avec la page ;
- incluent un titre unique et descriptif, utile aussi aux technologies d’assistance ;
- sont testées dans le document HTML obtenu et pas uniquement dans le code source.

## Déploiement et cohérence entre instances

Un seul processus `next start` supporte les fonctions principales de Next.js, mais une production distribuée ajoute des responsabilités.

Pour plusieurs instances ou un déploiement progressif, vérifier :

- le partage et l’invalidation coordonnée du cache ;
- la cohérence de la clé de chiffrement des traitements serveur lorsque la version l’exige ;
- un identifiant de déploiement cohérent ;
- la compatibilité des réponses diffusées progressivement ;
- le comportement du réseau de diffusion et du serveur mandataire ;
- la persistance ou non du système de fichiers ;
- les tâches qui ne doivent pas être exécutées plusieurs fois.

Une sortie entièrement statique ne supporte pas toutes les capacités serveur. Vérifier les besoins avant de choisir ce mode.

## Contrôles obligatoires

Pour toute modification de cette zone, vérifier au minimum :

- navigation directe et navigation côté client ;
- paramètres valides et invalides ;
- utilisateur absent, autorisé et refusé ;
- organisation correcte et tentative d’accès à une autre organisation ;
- chargement, absence, erreur et nouvelle tentative ;
- lecture immédiatement après modification ;
- cache froid, cache chaud et invalidation ;
- métadonnées du document initial pour une page publique ;
- comportement après une construction de production ;
- comportement multi-instance lorsqu’il fait partie du déploiement.

## Sources officielles à vérifier selon la version

- [App Router](https://nextjs.org/docs/app)
- [Composants serveur et client](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Revalidation avec les composants de cache](https://nextjs.org/docs/app/getting-started/revalidating)
- [Modèle de cache précédent](https://nextjs.org/docs/app/guides/caching-without-cache-components)
- [Traitements serveur et configuration](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions)
- [Gestionnaires de routes](https://nextjs.org/docs/app/api-reference/file-conventions/route)
- [Métadonnées et images de partage](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)
- [Auto-hébergement](https://nextjs.org/docs/app/guides/self-hosting)
