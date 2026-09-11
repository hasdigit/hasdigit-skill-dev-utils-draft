# Scénarios de validation du skill Next.js

Chaque scénario est réussi uniquement si le résultat attendu est démontré et si le comportement interdit ne se produit pas.

## Nouvelle application avec App Router

- **Situation** : création d’un nouveau produit Next.js.
- **Résultat attendu** : version vérifiée, App Router choisi explicitement, couche `app/` limitée au routage et métier organisé en modules et fonctionnalités.
- **Comportement interdit** : placer tout le métier directement sous les pages.

## Projet existant avec Pages Router

- **Situation** : correction limitée dans un projet utilisant `pages/`.
- **Résultat attendu** : conventions existantes inspectées et correction compatible avec ce routeur.
- **Comportement interdit** : migration vers l’App Router sans demande ni plan.

## Frontière serveur et navigateur

- **Situation** : un composant interactif est ajouté à une page serveur.
- **Résultat attendu** : frontière `use client` limitée au composant interactif, propriétés sérialisables et absence de dépendance serveur dans le code client.
- **Comportement interdit** : convertir toute la page en composant client pour simplifier.

## Traitement serveur protégé

- **Situation** : un formulaire modifie une facture.
- **Résultat attendu** : validation, session, permission, organisation, règle métier, invalidation et résultat utilisateur sont contrôlés côté serveur.
- **Comportement interdit** : faire confiance au bouton masqué ou à l’identifiant du formulaire.

## Gestionnaire de route public

- **Situation** : une intégration externe appelle `route.ts`.
- **Résultat attendu** : méthode, entrée, signature ou session, autorisation, taille, répétition, réponse et journal sont contrôlés.
- **Comportement interdit** : considérer le fichier privé parce qu’aucun lien d’interface ne l’expose.

## Accès croisé entre organisations clientes

- **Situation** : deux organisations possèdent des ressources de même type.
- **Résultat attendu** : l’utilisateur de la première ne peut ni lire, ni modifier, ni déduire l’existence d’une ressource de la seconde.
- **Comportement interdit** : filtrer uniquement avec un identifiant reçu du navigateur.

## Cache personnalisé

- **Situation** : une page dépend de l’utilisateur et de l’organisation.
- **Résultat attendu** : rendu dynamique ou clé de cache isolée et prouvée par un test croisé.
- **Comportement interdit** : placer la réponse dans un cache global partagé.

## Invalidation après modification

- **Situation** : une donnée visible est modifiée.
- **Résultat attendu** : invalidation précise, lecture suivante correcte et absence d’effet sur les autres organisations.
- **Comportement interdit** : invalider tout le produit sans nécessité ou servir indéfiniment l’ancienne valeur.

## Métadonnées multi-marques

- **Situation** : deux domaines publics utilisent des marques différentes.
- **Résultat attendu** : titre, description, adresse canonique et image de partage correspondent à chaque domaine dans le document initial.
- **Comportement interdit** : réutiliser les métadonnées mises en cache d’une autre organisation.

## Page publique multilingue

- **Situation** : un contenu public existe dans deux langues et sur deux domaines de marque.
- **Résultat attendu** : document initial, langue, titre, adresse canonique, variantes, plan de site et formatage correspondent à chaque combinaison autorisée.
- **Comportement interdit** : produire une adresse de prévisualisation comme canonique ou mélanger une traduction et une marque.

## Secret et composant client

- **Situation** : un module serveur utilisant un secret est importé par une interface interactive.
- **Résultat attendu** : l’importation est refusée ou séparée par un contrat sûr.
- **Comportement interdit** : transmettre le secret ou l’objet serveur au composant client.

## Chargement et erreur par segment

- **Situation** : une partie de page est lente ou échoue.
- **Résultat attendu** : chargement stable, erreur compréhensible et maintien des zones indépendantes lorsque possible.
- **Comportement interdit** : écran vide ou pile technique affichée.

## Formulaire avec erreur récupérable

- **Situation** : une saisie est valide dans le navigateur mais refusée par une règle métier serveur.
- **Résultat attendu** : valeurs conservées, erreur compréhensible près du champ ou de l’action, nouvelle soumission possible et absence de modification partielle.
- **Comportement interdit** : perdre toutes les saisies ou présenter une défaillance technique générique.

## Demandes concurrentes

- **Situation** : deux recherches sont déclenchées rapidement et la première réponse arrive en dernier.
- **Résultat attendu** : seule la réponse correspondant à l’intention actuelle est affichée, sans boucle de requêtes ni mélange d’organisation.
- **Comportement interdit** : remplacer le résultat récent par une réponse devenue ancienne.

## Collection volumineuse

- **Situation** : une page affiche une collection filtrable contenant de nombreuses lignes.
- **Résultat attendu** : stratégie de pagination ou de virtualisation justifiée, filtres dans l’adresse lorsqu’ils doivent être partageables, états complets et usage au clavier préservé.
- **Comportement interdit** : charger tout le contenu sans mesure ou compresser le tableau jusqu’à le rendre illisible.

## Navigation accessible

- **Situation** : navigation côté client vers une nouvelle page.
- **Résultat attendu** : titre unique, titre principal cohérent, focus utilisable et annonce compréhensible.
- **Comportement interdit** : page sans titre descriptif ou focus perdu.

## Déploiement sur plusieurs instances

- **Situation** : plusieurs processus servent la même version.
- **Résultat attendu** : artefact identique, cache et invalidation coordonnés, identifiant de déploiement et clé serveur cohérents lorsque nécessaires.
- **Comportement interdit** : supposer que les caches locaux se synchronisent automatiquement.

## Performance d’une nouvelle dépendance client

- **Situation** : une bibliothèque interactive est ajoutée sous une frontière `use client`.
- **Résultat attendu** : besoin démontré, compatibilité vérifiée, effet sur le code navigateur mesuré et chargement limité aux routes concernées.
- **Comportement interdit** : étendre la frontière client ou accepter une augmentation non mesurée.

## Observabilité sans fuite

- **Situation** : le suivi des erreurs et des parcours est ajouté au serveur et au navigateur.
- **Résultat attendu** : initialisation unique, identifiants de corrélation, événements nommés en toutes lettres et expurgation des secrets et données personnelles.
- **Comportement interdit** : journaliser un jeton, un contenu de formulaire ou une réponse brute sensible.

## Version différente de la documentation mémorisée

- **Situation** : le projet utilise une version dont le comportement de cache a changé.
- **Résultat attendu** : version et configuration inspectées, documentation correspondante consultée et décision adaptée.
- **Comportement interdit** : appliquer une règle générale sans vérifier la version.

## Nommage compréhensible

- **Situation** : création de types et fichiers de permission.
- **Résultat attendu** : noms complets, préfixes `Interface`, `Type` et `Enumeration`, domaine et responsabilité visibles.
- **Comportement interdit** : préfixes `I`, `T`, `E` ou dossiers vagues.

## Démarrage d’une nouvelle session

- **Situation** : un agent de code, avec ou sans prise en charge de `agents/openai.yaml`, démarre dans un projet qui possède déjà certains garde-fous.
- **Résultat attendu** : le [prompt obligatoire](../installation/installation.md) lui fait lire le dossier maître, contrôler la couverture des garde-fous et les actualiser uniquement si nécessaire.
- **Comportement interdit** : considérer le skill comme réservé à une plateforme, commencer sans lire le dossier maître ou recréer aveuglément les contrôles.
