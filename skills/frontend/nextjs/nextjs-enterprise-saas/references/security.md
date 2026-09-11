# Sécurité Next.js

Lire ce document pour toute modification touchant une entrée externe, une session, une donnée sensible, un secret, un traitement serveur, un gestionnaire de route, une intégration, un fichier, une image distante ou un déploiement.

## Modèle de menace

Une application Next.js réunit du code serveur et du code envoyé au navigateur dans le même projet. Une importation mal placée peut donc transformer une donnée privée ou une dépendance serveur en fuite.

Avant le code, identifier :

- les données sensibles ;
- les secrets ;
- les acteurs autorisés et hostiles ;
- les points d’entrée réseau ;
- les frontières serveur et navigateur ;
- la portée de l’organisation cliente ;
- les caches ;
- les intégrations externes ;
- les journaux et outils d’observation.

## Secrets et variables d’environnement

- Toute variable rendue publique par la convention de Next.js doit être considérée visible dans le navigateur.
- Un secret reste dans un module exclusivement serveur.
- Ne jamais transmettre un secret comme propriété d’un composant client.
- Ne jamais inclure un secret dans le document HTML, une métadonnée, une adresse, un message d’erreur ou un journal.
- Séparer les secrets de construction et les secrets d’exécution.
- Faire échouer clairement le démarrage lorsqu’un secret obligatoire manque.
- Prévoir rotation, portée minimale et révocation.

Utiliser une protection d’importation serveur telle que `server-only` lorsque le projet la supporte. Cette protection complète la revue des dépendances, elle ne la remplace pas.

## Validation des entrées

Valider côté serveur :

- paramètres de route ;
- paramètres de recherche ;
- formulaires ;
- corps de requête ;
- cookies et en-têtes ;
- variables d’environnement ;
- réponses externes ;
- métadonnées de fichier ;
- événements et webhooks.

La validation doit contrôler type, taille, format, valeurs autorisées et cohérence métier. Une validation TypeScript seule n’existe plus au moment de l’exécution et ne protège pas une entrée réseau.

## Traitements serveur et gestionnaires de routes

Les traitements serveur et les méthodes de `route.ts` sont des points d’entrée réseau.

Ils doivent appliquer :

- authentification ;
- autorisation ;
- isolation de l’organisation ;
- validation ;
- limitation de taille ;
- protection contre les répétitions dangereuses ;
- limitation de débit lorsque nécessaire ;
- résultats minimisés ;
- erreurs expurgées ;
- journalisation sûre.

Les identifiants techniques générés par Next.js ne remplacent pas ces contrôles.

Lorsqu’un serveur mandataire ou plusieurs origines sont autorisés à appeler un traitement, configurer les origines explicitement et au périmètre minimal. Ne pas élargir une liste d’origines pour contourner une erreur sans comprendre la topologie.

## Sessions et cookies

- Utiliser des bibliothèques maintenues lorsque le contexte le permet.
- Stocker uniquement les informations nécessaires.
- Protéger les cookies avec les attributs adaptés au transport, au navigateur et au risque.
- Renouveler et invalider les sessions selon leur niveau de sensibilité.
- Ne pas accepter un rôle ou une organisation uniquement depuis une donnée modifiable par le navigateur.
- Effectuer les décisions sensibles à partir d’une source serveur fiable.

## Scripts injectés et contenu HTML

Éviter l’insertion de contenu HTML non maîtrisé. Toute utilisation de `dangerouslySetInnerHTML` doit disposer d’une justification, d’une purification adaptée et de tests hostiles.

Définir une politique de sécurité du contenu compatible avec les scripts réellement utilisés. Préférer des valeurs aléatoires par réponse ou des empreintes autorisées aux règles générales permissives.

Ne pas introduire `unsafe-eval`, une origine générale ou un script tiers sans évaluation documentée.

## Requêtes serveur vers des adresses externes

Lorsqu’une adresse provient directement ou indirectement d’un utilisateur :

- utiliser une liste de domaines et de protocoles autorisés ;
- refuser les réseaux internes et adresses locales non nécessaires ;
- limiter redirections, taille et durée ;
- vérifier la résolution finale ;
- ne pas transmettre automatiquement les cookies ou en-têtes privés.

Appliquer ces règles aux importations d’images distantes, aperçus, webhooks sortants et intégrations.

## Téléversement et téléchargement de fichiers

Pour un téléversement :

- limiter la taille avant traitement coûteux ;
- vérifier le type réel et pas uniquement l’extension ;
- neutraliser le nom fourni ;
- stocker hors des chemins exécutables ;
- analyser les contenus à risque ;
- vérifier l’organisation propriétaire ;
- utiliser une adresse temporaire à portée minimale lorsque nécessaire.

Pour un téléchargement, vérifier l’autorisation juste avant de produire le fichier et empêcher toute traversée de chemin.

## Cache et confidentialité

Une réponse privée ne doit pas entrer dans un cache public ou partagé. La clé de cache doit inclure toutes les dimensions qui changent le résultat, notamment l’organisation, l’utilisateur, la langue et la permission lorsque nécessaire.

Tester la succession de deux utilisateurs et de deux organisations sur une même instance. Vérifier également l’invalidation après changement de rôle ou de marque.

## Erreurs et journaux

Le message utilisateur ne doit pas exposer :

- pile technique ;
- requête de base de données ;
- chemin interne ;
- secret ;
- jeton ;
- détail d’une autre organisation ;
- réponse brute d’un fournisseur.

Le journal technique contient uniquement les éléments nécessaires au diagnostic, avec un identifiant de corrélation et une expurgation des données sensibles.

## En-têtes et transport

Évaluer et configurer selon le produit :

- sécurité du transport ;
- politique de sécurité du contenu ;
- protection contre l’intégration dans une page hostile ;
- type de contenu strict ;
- politique de référent ;
- permissions accordées aux fonctions du navigateur ;
- cache des réponses sensibles.

Tester les en-têtes sur la réponse réellement déployée, y compris derrière un serveur mandataire ou un réseau de diffusion.

## Dépendances et construction

- Verrouiller les versions avec le mécanisme du gestionnaire de paquets.
- Examiner les alertes de sécurité et leur applicabilité réelle.
- Retirer les dépendances inutilisées.
- Vérifier les scripts exécutés pendant l’installation.
- Éviter une mise à jour majeure sans lecture des migrations.
- Rechercher les secrets et fichiers sensibles dans les différences avant publication.
- Produire un artefact de construction reproductible.

## Vérification minimale

- appel direct d’un traitement sans interface ;
- entrée mal formée et trop volumineuse ;
- accès à une autre organisation ;
- composant client inspecté pour les secrets ;
- cache partagé entre deux contextes ;
- erreur inattendue sans fuite ;
- origine ou signature invalide ;
- réponse et en-têtes de production ;
- audit des dépendances ;
- recherche de données sensibles dans la sortie de construction.

## Sources officielles

- [Guide de sécurité des données Next.js](https://nextjs.org/docs/app/guides/data-security)
- [Guide d’authentification Next.js](https://nextjs.org/docs/app/guides/authentication)
- [Configuration des traitements serveur](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions)
- [Variables d’environnement Next.js](https://nextjs.org/docs/app/guides/environment-variables)
