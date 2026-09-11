# Performance, observabilité et exploitation

Lire ce document pour une optimisation, une intégration de suivi, une construction de production, un déploiement ou une modification d’infrastructure.

## Mesurer avant d’optimiser

Définir une situation de référence et un objectif observable :

- temps avant l’affichage du contenu principal ;
- stabilité visuelle ;
- délai entre une interaction et sa réponse visible ;
- quantité de code envoyée au navigateur ;
- durée des lectures serveur ;
- durée des traitements serveur ;
- taux d’erreur ;
- utilisation de mémoire et de processeur ;
- taux de réussite du cache.

Mesurer sur des appareils, réseaux, données et routes représentatifs. Une amélioration locale qui dégrade une autre route critique n’est pas une optimisation validée.

## Budget navigateur

Les composants serveur limitent le code envoyé au navigateur uniquement si les frontières `use client` restent étroites.

- Inspecter l’effet de chaque dépendance client importante.
- Charger tard une fonction rarement utilisée lorsque l’attente reste compréhensible.
- Éviter les bibliothèques générales pour une opération simple déjà disponible.
- Importer les fonctions précises lorsque la bibliothèque le permet.
- Ne pas envoyer au navigateur une donnée ou un composant uniquement nécessaire au serveur.
- Mesurer la construction avec l’outil d’analyse compatible avec la version.

Une division en fragments supplémentaires ne garantit pas un produit plus rapide. Vérifier le nombre de requêtes, la priorité et le moment d’usage réel.

## Images

Utiliser le composant d’image de Next.js lorsque ses garanties correspondent au déploiement.

- Fournir dimensions ou proportion stable pour éviter les déplacements visuels.
- Définir `sizes` selon la largeur réellement affichée.
- Charger prioritairement seulement l’image principale visible immédiatement.
- Limiter les domaines et chemins distants autorisés.
- Fournir un texte alternatif selon le sens de l’image.
- Choisir une qualité mesurée, pas maximale par défaut.
- Vérifier l’optimisation disponible sur la plateforme cible.

Une image protégée par authentification peut nécessiter une stratégie différente. Ne pas transmettre automatiquement des en-têtes privés à un service d’optimisation.

## Polices et scripts tiers

Préférer le module de polices de Next.js lorsqu’il convient afin de maîtriser l’hébergement et les déplacements de mise en page. Limiter familles, graisses et alphabets au besoin réel tout en couvrant les langues prises en charge.

Charger les scripts tiers avec une stratégie explicite selon leur importance. Un outil d’analyse, de discussion ou de publicité ne doit pas bloquer l’interface principale.

Avant d’ajouter un script tiers, évaluer :

- finalité et consentement ;
- données transmises ;
- coût de chargement et d’exécution ;
- politique de sécurité du contenu ;
- comportement en cas d’indisponibilité ;
- possibilité de retrait.

## Performance serveur

- Éviter les chaînes de lectures lorsque les opérations sont indépendantes.
- Sélectionner uniquement les champs nécessaires.
- Indexer les recherches à partir de mesures réelles.
- Grouper les appels externes lorsque leur contrat le permet.
- Définir des délais maximums et des limites de taille.
- Ne pas effectuer une tâche lourde plusieurs fois par rendu sans nécessité.
- Déplacer les traitements réellement longs vers un mécanisme différé fiable.

Le cache améliore certaines lectures, mais ajoute une responsabilité d’isolation et d’invalidation. Appliquer [Routage, rendu et cache](routing-rendering-and-cache.md) avant toute mise en cache métier.

## Observabilité

L’observabilité doit permettre de répondre à quatre questions : que s’est-il passé, pour quelle opération, dans quel environnement et avec quel effet utilisateur ?

Utiliser les points d’instrumentation supportés par la version de Next.js pour initialiser les outils côté serveur et côté navigateur. Ne pas multiplier des initialisations concurrentes dans les composants.

Prévoir :

- journaux structurés ;
- identifiants de corrélation ;
- suivi des erreurs serveur et navigateur ;
- mesures de latence et de volume ;
- traces entre services lorsque nécessaires ;
- mesures de qualité perçue dans le navigateur ;
- alertes liées à un effet réel ;
- tableaux de suivi par route et opération métier.

Une information d’observation ne doit contenir ni secret, ni jeton, ni contenu de formulaire, ni donnée personnelle non nécessaire. L’identifiant d’une organisation peut nécessiter une transformation ou une limitation d’accès.

## Événements métier et mesures produit

Distinguer les événements techniques des événements métier. Un clic n’est pas toujours une réussite métier.

Chaque événement important doit définir :

- nom complet et stable ;
- moment précis de production ;
- propriétés autorisées ;
- version du contrat ;
- propriétaire ;
- politique de conservation ;
- preuve empêchant les doublons lorsque nécessaire.

Mesurer la confirmation serveur d’une action critique plutôt que seulement l’intention dans le navigateur.

## Santé et disponibilité

Une vérification de vie confirme que le processus répond. Une vérification de capacité confirme qu’il peut recevoir du trafic. Ne pas les confondre.

Une vérification de capacité doit contrôler uniquement les dépendances indispensables et répondre rapidement. Elle ne doit pas modifier de donnée ni déclencher un traitement coûteux.

Prévoir :

- démarrage et arrêt progressifs ;
- délai maximum des requêtes ;
- comportement des requêtes en cours ;
- reprise après indisponibilité d’une dépendance ;
- saturation des connexions ;
- espace disque lorsque le déploiement en dépend réellement.

## Modes de déploiement

Choisir à partir des capacités utilisées, pas d’une préférence générale.

### Serveur Next.js

Convient aux composants serveur, traitements serveur, gestionnaires de routes, rendu dynamique et revalidation. Vérifier la version de l’environnement JavaScript, les variables, le système de fichiers et l’arrêt progressif.

### Sortie statique

Convient uniquement lorsque chaque route peut être produite sans capacité serveur incompatible. Vérifier les formulaires, routes dynamiques, images, interceptions de requêtes et fonctions de revalidation avant ce choix.

### Plateforme avec adaptateur

Vérifier la matrice réelle des fonctions supportées, la version de l’adaptateur, la stratégie de cache, les limites d’exécution et la manière dont les erreurs sont observées.

## Auto-hébergement et plusieurs instances

Pour plusieurs instances :

- déployer le même artefact immuable ;
- partager ou coordonner le cache et les invalidations ;
- utiliser une clé de chiffrement commune pour les traitements serveur lorsque la version l’exige ;
- configurer un identifiant de déploiement compatible avec les versions simultanées ;
- coordonner les traitements planifiés ou différés ;
- ne pas dépendre d’un disque local éphémère ;
- vérifier la diffusion progressive derrière le serveur mandataire ;
- tester une modification sur une instance et une lecture sur une autre.

Le réseau de diffusion de contenu et le serveur mandataire doivent respecter les cookies, les en-têtes variables et le caractère privé des réponses. Une règle externe trop générale peut mettre en cache une réponse que Next.js considérait personnelle.

## Construction reproductible

- Utiliser un seul gestionnaire de paquets et son fichier de verrouillage.
- Installer les dépendances avec une commande reproductible.
- Séparer les variables nécessaires à la construction de celles nécessaires à l’exécution.
- Ne pas intégrer de secret durable dans l’artefact.
- Produire une construction de production avant livraison.
- Démarrer l’artefact dans une configuration proche de la cible lorsque possible.
- Identifier la révision et la version déployées.

Une image de conteneur doit utiliser une base maintenue, un utilisateur non privilégié, une liste de fichiers minimale et une procédure d’arrêt correcte.

## Déploiement progressif et retour

Avant publication :

1. vérifier les migrations de données et leur compatibilité avec deux versions simultanées ;
2. définir les signaux d’arrêt du déploiement ;
3. conserver un artefact précédent utilisable ;
4. vérifier la compatibilité des caches et des traitements serveur ;
5. documenter la procédure de retour ;
6. effectuer un contrôle après déploiement sur les parcours critiques.

Un retour de code ne retire pas automatiquement une migration de données. La stratégie doit préserver les données avant tout.

## Dépendances

Avant toute dépendance :

- besoin démontré ;
- activité de maintenance ;
- sécurité ;
- licence ;
- compatibilité serveur et navigateur ;
- compatibilité avec le mode d’exécution ;
- poids et coût d’exécution ;
- solution de retrait.

Examiner les alertes selon leur usage réel. Une mise à jour de sécurité urgente doit rester testée ; une alerte sans chemin exploitable doit être documentée, pas ignorée silencieusement.

## Contrôles obligatoires

- mesure avant et après sur les routes concernées ;
- quantité de code navigateur et dépendances importantes ;
- images, polices et scripts tiers ;
- temps serveur, erreurs et saturation ;
- absence de donnée sensible dans les journaux et événements ;
- construction reproductible ;
- démarrage, santé, capacité et arrêt ;
- cache et invalidation entre deux instances ;
- déploiement progressif et procédure de retour ;
- contrôle réel après déploiement.

## Sources officielles

- [Liste de contrôle de production Next.js](https://nextjs.org/docs/app/guides/production-checklist)
- [Composant d’image Next.js](https://nextjs.org/docs/app/api-reference/components/image)
- [Analyse et mesures de performance Next.js](https://nextjs.org/docs/app/guides/analytics)
- [Instrumentation Next.js](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation)
- [Auto-hébergement de Next.js](https://nextjs.org/docs/app/guides/self-hosting)
