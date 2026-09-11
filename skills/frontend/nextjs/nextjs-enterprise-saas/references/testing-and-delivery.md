# Tests, audit et livraison Next.js

Lire ce document pour définir les preuves, créer une fonctionnalité, corriger une régression, auditer le produit ou préparer un déploiement.

## Principe

La couverture doit être proportionnée au risque. Un test doit prouver un comportement observable ou une frontière importante, pas seulement reproduire l’implémentation.

Une modification n’est pas terminée parce que le code compile dans l’éditeur. Les contrôles disponibles doivent être exécutés dans une configuration proche de la production.

## Niveaux de contrôle

### Contrôles statiques

- format et règles de code ;
- TypeScript strict ;
- importations interdites entre modules ;
- importations serveur accidentelles dans le graphe client ;
- dépendances circulaires ;
- recherche de secrets ;
- validation de configuration.

### Tests unitaires

Réserver les tests unitaires aux fonctions déterministes : validation, politiques, transformations, normalisation d’erreur, calcul de clé de cache et règles métier.

### Tests de composants

Tester les composants client interactifs avec des événements proches de l’usage réel. Vérifier clavier, focus, chargement, erreur, soumission répétée et résultat.

### Tests d’intégration

Tester ensemble les couches qui portent un contrat important : traitement serveur et politique, gestionnaire de route et validation, module et accès aux données, thème et organisation cliente.

### Tests de bout en bout

Exécuter le produit dans un navigateur contre une construction proche de la production. Couvrir les parcours critiques, la navigation directe et côté client, les permissions, les erreurs et l’isolation des organisations.

Les composants serveur asynchrones ne sont pas entièrement pris en charge par tous les outils unitaires. Préférer un test d’intégration ou de bout en bout lorsque l’outil ne reproduit pas fidèlement le comportement du framework.

## Matrice minimale selon le changement

| Changement | Preuves minimales |
|---|---|
| Fonction pure | TypeScript et test unitaire ciblé |
| Composant client | Test de composant, clavier et états interactifs |
| Composant serveur | Test d’intégration ou de bout en bout avec données et autorisation |
| Nouvelle page | Navigation directe, navigation côté client, métadonnées, chargement, erreur et absence |
| Traitement serveur | Validation, session absente, permission refusée, succès, erreur et invalidation |
| Gestionnaire de route | Méthodes, statuts, validation, autorisation, taille, cache et répétition |
| Politique de cache | Cache froid, cache chaud, isolation, fraîcheur et invalidation |
| Thème ou marque | rendu serveur initial, hydratation, contraste et absence de mélange entre organisations |
| Déploiement | construction de production, démarrage, santé, arrêt et comportement multi-instance concerné |

## Scénarios obligatoires pour une action critique

- succès ;
- entrée invalide ;
- session absente ou expirée ;
- permission absente ;
- ressource absente ;
- tentative d’accès à une autre organisation ;
- erreur métier ;
- service externe indisponible ;
- délai dépassé ;
- réponse externe mal formée ;
- soumission répétée ;
- navigation interrompue ;
- nouvelle tentative ;
- invalidation de cache ;
- petit écran ;
- zoom ;
- clavier ;
- thème ou marque alternative.

## Tests du routage

Vérifier :

- chargement direct par adresse ;
- navigation avec `Link` ;
- retour et avance du navigateur ;
- segments dynamiques valides et invalides ;
- paramètres de recherche ;
- route absente ;
- erreur de segment ;
- mise en page correcte ;
- route parallèle ou interceptée lorsqu’elle existe ;
- passage entre App Router et Pages Router lorsqu’ils coexistent.

Ne pas tester uniquement le chemin nominal depuis la page d’accueil.

## Tests des frontières serveur et navigateur

- confirmer qu’un secret n’apparaît pas dans le code livré au navigateur ;
- confirmer que les propriétés transmises sont sérialisables ;
- vérifier l’absence d’hydratation incohérente ;
- mesurer l’effet d’une nouvelle frontière `use client` sur le code client ;
- vérifier les fournisseurs de contexte et bibliothèques exigeant le navigateur ;
- tester le rendu sans JavaScript lorsque le parcours public doit rester lisible.

## Tests des traitements serveur

Appeler le traitement par le parcours normal et, lorsque l’outil le permet, directement sans l’interface.

Vérifier :

- validation serveur ;
- authentification ;
- autorisation sur la ressource ;
- organisation cliente ;
- résultat utilisateur ;
- absence de fuite dans l’erreur ;
- comportement d’une demande répétée ;
- invalidation et lecture après modification ;
- limite de taille pour les formulaires ou fichiers concernés.

## Tests des gestionnaires de routes

- chaque méthode autorisée ;
- méthode non autorisée ;
- contenu et type de réponse ;
- statuts attendus ;
- paramètres et corps mal formés ;
- session, permission et organisation ;
- limitation de taille et de débit lorsqu’elle existe ;
- en-têtes de cache ;
- origine ou signature ;
- répétition d’un webhook ou d’une modification.

## Tests du cache

Un test de cache doit rendre visible la différence entre :

1. première lecture ;
2. lecture répétée ;
3. modification ;
4. invalidation ;
5. lecture après invalidation.

Ajouter deux utilisateurs et deux organisations pour détecter un mélange de données. Pour un déploiement distribué, effectuer l’invalidation sur une instance et la lecture sur une autre lorsque l’infrastructure peut être testée.

## Tests des métadonnées et de l’indexation

Pour une page publique :

- inspecter le document HTML réellement retourné ;
- vérifier titre, description, adresse canonique et langue ;
- vérifier les images de partage ;
- tester au moins deux organisations ou marques ;
- vérifier le plan de site et les règles d’indexation concernés ;
- confirmer l’absence de données privées.

## Contrôles de construction

Exécuter les commandes définies par le projet. Elles devraient couvrir :

- TypeScript ;
- règles de code ;
- tests ;
- construction Next.js de production ;
- démarrage de l’artefact produit lorsque possible ;
- contrôle des dépendances ;
- analyse du poids envoyé au navigateur lorsque le changement le justifie.

Ne pas corriger un échec en désactivant une règle sans analyser sa cause.

## Intégration continue

Le processus automatisé doit échouer clairement lorsqu’un contrôle obligatoire échoue.

Ordre recommandé :

1. installation reproductible des dépendances ;
2. validation de la configuration non secrète ;
3. TypeScript et règles de code ;
4. tests unitaires et d’intégration ;
5. construction de production ;
6. tests de bout en bout sur l’artefact ;
7. contrôles de sécurité et dépendances ;
8. publication immuable ;
9. vérification après déploiement.

Les secrets de test doivent être séparés de la production et limités au besoin.

## Livraison et déploiement

Avant de choisir une cible, inventorier les capacités utilisées :

- serveur Node.js ;
- sortie statique ;
- diffusion progressive ;
- traitements serveur ;
- gestionnaires de routes ;
- génération statique incrémentale ;
- composants de cache ;
- optimisation d’images ;
- tâches exécutées après réponse ;
- stockage persistant ;
- plusieurs instances.

La plateforme doit supporter les fonctions réellement utilisées. Un adaptateur tiers doit être vérifié pour la version et les capacités nécessaires.

### Plusieurs instances

Vérifier :

- même artefact et même identifiant de construction ;
- clé de chiffrement cohérente pour les traitements serveur lorsque nécessaire ;
- identifiant de déploiement pour les déploiements progressifs ;
- cache partagé ou coordination d’invalidation ;
- absence de dépendance à un disque local éphémère ;
- arrêt progressif et requêtes en cours ;
- compatibilité du serveur mandataire avec la diffusion progressive.

### Réseau de diffusion et serveur mandataire

Contrôler les clés de cache, cookies, en-têtes variables, réponses privées et durées. Une mauvaise configuration externe peut annuler les garanties du serveur Next.js.

## Définition de terminé

Le travail est terminé uniquement si :

- les critères fonctionnels sont satisfaits ;
- les permissions serveur sont prouvées ;
- l’isolation des organisations est testée ;
- les erreurs et états de chargement sont visibles ;
- les frontières serveur et navigateur sont correctes ;
- le cache et l’invalidation sont documentés ;
- l’interface est accessible et adaptable ;
- les métadonnées publiques sont correctes ;
- TypeScript, tests et construction réussissent ;
- le déploiement ciblé supporte les fonctions utilisées ;
- la documentation utile est mise à jour ;
- les contrôles non exécutés sont explicitement déclarés.

## Niveaux de sévérité pour un audit

### Bloquant critique

- fuite de secret ou de donnée entre organisations ;
- traitement serveur non autorisé ;
- cache public contenant une réponse privée ;
- construction de production impossible ;
- perte ou corruption de données.

### Majeur

- permission appliquée uniquement dans l’interface ;
- route critique sans validation ;
- frontière client exposant trop de données ;
- invalidation incohérente ;
- parcours essentiel inaccessible au clavier ;
- déploiement multi-instance non coordonné.

### Important

- fichier de route contenant trop de logique métier ;
- nom ou structure difficile à comprendre ;
- test significatif absent ;
- erreur utilisateur insuffisante ;
- poids client augmenté sans justification.

### Amélioration

- harmonisation non bloquante ;
- documentation complémentaire ;
- optimisation mesurée mais non urgente.

## Sources officielles

- [Guide des tests Next.js](https://nextjs.org/docs/app/guides/testing)
- [Déploiement vers différentes plateformes](https://nextjs.org/docs/app/guides/deploying-to-platforms)
- [Guide d’auto-hébergement](https://nextjs.org/docs/app/guides/self-hosting)
