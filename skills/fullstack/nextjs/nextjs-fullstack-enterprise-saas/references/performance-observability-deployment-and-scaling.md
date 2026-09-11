# Performance, observabilité, déploiement et montée en charge

Lire ce document pour une optimisation, une nouvelle dépendance, une mesure, un journal, une alerte, une construction, un déploiement ou une évolution de capacité.

## Mesurer un parcours complet

Définir une référence et un objectif pour :

- affichage du contenu principal ;
- stabilité visuelle ;
- réponse à une interaction ;
- quantité de code navigateur ;
- durée d’un cas d’usage serveur ;
- durée et nombre de requêtes de données ;
- temps d’une intégration ;
- taux d’erreur ;
- utilisation de mémoire et de processeur ;
- saturation des connexions ;
- attente et durée des tâches ;
- taux de réussite du cache.

Mesurer avec des volumes, appareils, réseaux et routes représentatifs. Une optimisation n’est validée que si la mesure après modification démontre le bénéfice sans régression critique ailleurs.

## Performance du navigateur

- Limiter les frontières `use client`.
- Inspecter le poids des dépendances.
- Charger tard une fonction rarement utilisée.
- Ne pas envoyer de données inutiles.
- Utiliser images, polices et scripts selon les capacités de Next.js.
- Préserver les dimensions pour éviter les déplacements.
- Éviter les calculs coûteux à chaque rendu.
- Mesurer les parcours sur appareil modeste.

Un découpage supplémentaire ne garantit pas moins de travail : mesurer le nombre de requêtes et le coût d’exécution.

## Performance serveur

- Exécuter en parallèle les lectures indépendantes.
- Éviter les appels réseau internes inutiles.
- Sélectionner les champs nécessaires.
- Détecter les requêtes répétées par élément.
- Définir des délais maximums.
- Limiter corps, résultats et concurrence.
- Déplacer les opérations longues vers une tâche durable.
- Fermer les ressources et connexions.

Ne pas optimiser avec un cache avant d’avoir défini l’isolation et l’invalidation.

## Connexions de données

Le mode d’hébergement influence la gestion des connexions. Définir :

- nombre maximal par instance ;
- réutilisation ;
- intermédiaire de regroupement lorsque nécessaire ;
- délai d’acquisition ;
- durée de requête ;
- comportement en déploiement à nombreuses instances ;
- arrêt progressif.

Le nombre d’instances multiplié par les connexions de chacune ne doit pas dépasser la capacité du moteur.

## Observabilité par cas d’usage

Pour une opération critique, relier :

- requête entrante ;
- identité technique expurgée ;
- organisation selon la politique de confidentialité ;
- cas d’usage ;
- transaction ;
- appel externe ;
- tâche différée ;
- réponse et effet utilisateur.

Utiliser un identifiant de corrélation propagé aux composants autorisés. Ne pas employer un secret ou une donnée personnelle comme identifiant.

## Journaux

Un journal structuré contient :

- instant ;
- niveau ;
- environnement ;
- révision ;
- opération nommée ;
- identifiant de corrélation ;
- résultat ;
- durée ;
- erreur normalisée.

Il ne contient pas par défaut : mot de passe, jeton, cookie, corps complet, numéro financier complet ou donnée d’une autre organisation.

Éviter les phrases différentes pour le même événement. Des champs stables permettent la recherche et les alertes.

## Mesures

Mesurer au minimum lorsque pertinent :

- volume et durée des routes ;
- succès, refus et erreurs ;
- durée des cas d’usage ;
- requêtes lentes ;
- saturation du regroupement de connexions ;
- appels externes par résultat ;
- cache trouvé ou absent ;
- tâches en attente, tentatives et échecs définitifs ;
- qualité perçue dans le navigateur.

Limiter les dimensions variables afin d’éviter un nombre incontrôlé de séries. Ne pas utiliser directement un identifiant d’utilisateur ou de ressource comme dimension générale.

## Traces

Tracer les frontières coûteuses ou distribuées : route, cas d’usage, donnée, fournisseur et tâche. Propager le contexte sans faire confiance aux en-têtes externes non validés.

Échantillonner selon le volume, mais conserver une stratégie permettant d’étudier les erreurs rares et opérations critiques.

## Alertes

Une alerte doit avoir :

- condition liée à un effet réel ;
- durée évitant le bruit ;
- propriétaire ;
- niveau d’urgence ;
- procédure de diagnostic ;
- moyen de vérification et de clôture.

Ne pas alerter sur chaque exception isolée si aucune action n’est possible. Ne pas ignorer un taux d’échec élevé sous prétexte que les processus restent vivants.

## Instrumentation Next.js

Utiliser les points d’instrumentation compatibles avec la version pour initialiser une seule fois les outils serveur et navigateur.

Vérifier :

- environnement d’exécution ;
- durée d’initialisation ;
- comportement à la construction ;
- capture des erreurs de requête ;
- arrêt et vidage des données ;
- respect du consentement côté navigateur.

Une instrumentation ne doit pas transformer une panne de suivi en panne du produit sauf exigence explicite.

## Santé et capacité à recevoir du trafic

Une vérification de vie confirme que le processus fonctionne. Une vérification de capacité confirme qu’il peut recevoir une requête.

La capacité vérifie seulement les dépendances indispensables, rapidement et sans modifier de donnée. Ne pas rendre toute l’application indisponible pour une dépendance secondaire.

Prévoir des contrôles distincts pour les travailleurs de tâches.

## Construction reproductible

- Un seul gestionnaire de paquets et un fichier de verrouillage.
- Installation reproductible.
- Versions d’environnement explicites.
- Génération de clients et types déterministe.
- Migrations inventoriées.
- Aucun secret durable dans l’artefact.
- Révision identifiable.
- Construction de production exécutée avant livraison.
- Analyse du code navigateur lorsque nécessaire.

L’artefact déployé doit être celui qui a été testé.

## Modes de déploiement

### Serveur Next.js

Supporte les capacités serveur principales. Vérifier système de fichiers, mémoire, durée, arrêt et connexions.

### Fonctions à durée limitée

Vérifier absence d’état local entre requêtes, durée maximale, démarrages, connexions de données, tâches après réponse et support des flux.

### Sortie statique

Ne convient pas aux capacités nécessitant un serveur d’exécution. Confirmer formulaires, routes, traitements, authentification, revalidation et images avant ce choix.

### Adaptateur de plateforme

Vérifier la matrice des fonctions supportées pour la version exacte. Un déploiement qui construit ne prouve pas que le cache, les tâches ou les flux fonctionnent.

## Plusieurs instances

- Même artefact et même révision.
- Clé de chiffrement des traitements serveur cohérente lorsque nécessaire.
- Identifiant de déploiement pour les versions simultanées.
- Cache et invalidation coordonnés.
- Connexions de données dimensionnées globalement.
- Tâches planifiées verrouillées.
- Fichiers stockés hors disque local éphémère.
- Arrêt progressif.
- Serveur mandataire compatible avec les flux.

Tester une requête traversant plusieurs instances, pas seulement chaque instance isolément.

## Montée en charge

Augmenter la capacité après avoir identifié la limite :

- processeur ;
- mémoire ;
- base de données ;
- service externe ;
- cache ;
- file de travail ;
- réseau ;
- code navigateur.

Options : optimisation ciblée, limite d’usage, mise en cache sûre, traitement par lots, capacité verticale, plusieurs instances, partitionnement ou extraction de service.

Une extraction ajoute réseau, déploiement, contrats et observations distribuées. Ne la choisir que lorsque la frontière et le bénéfice sont démontrés.

## Déploiement progressif

Avant publication :

1. vérifier la compatibilité des migrations ;
2. vérifier la coexistence de deux versions ;
3. définir les signaux d’arrêt ;
4. déployer un artefact immuable ;
5. effectuer les contrôles de santé ;
6. tester les parcours critiques ;
7. observer erreurs, latence et données ;
8. poursuivre ou revenir.

Un retour de code ne retire pas une migration destructive. Prévoir la compatibilité avant le déploiement.

## Retour et continuité

Documenter :

- artefact précédent ;
- changement de configuration ;
- effet des migrations ;
- tâches en cours ;
- cache ;
- procédure de restauration ;
- communication ;
- vérification après retour.

Tester périodiquement sauvegarde, restauration et reprise des tâches selon la criticité.

## Contrôles obligatoires

- mesures avant et après ;
- code navigateur ;
- charge serveur et requêtes de données ;
- capacité globale des connexions ;
- journaux sans donnée sensible ;
- mesures et traces corrélées ;
- alerte déclenchée et procédure utilisable ;
- construction reproductible ;
- santé, capacité et arrêt ;
- déploiement sur plusieurs instances ;
- cache et tâches coordonnés ;
- déploiement progressif ;
- retour et restauration.

## Sources officielles

- [Liste de contrôle de production Next.js](https://nextjs.org/docs/app/guides/production-checklist)
- [Instrumentation Next.js](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation)
- [Analyse et mesures côté navigateur](https://nextjs.org/docs/app/guides/analytics)
- [Auto-hébergement de Next.js](https://nextjs.org/docs/app/guides/self-hosting)
- [Déploiement vers différentes plateformes](https://nextjs.org/docs/app/guides/deploying-to-platforms)
