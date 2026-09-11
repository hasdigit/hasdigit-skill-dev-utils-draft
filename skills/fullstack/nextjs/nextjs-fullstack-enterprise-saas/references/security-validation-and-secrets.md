# Sécurité, validation et secrets

Lire ce document pour toute entrée externe, session, route, traitement serveur, donnée sensible, fichier, intégration, configuration ou journal.

## Modèle de menace

Avant le code, identifier :

- données et opérations sensibles ;
- acteurs légitimes et hostiles ;
- frontières de confiance ;
- points d’entrée réseau ;
- code livré au navigateur ;
- privilèges du serveur ;
- organisations clientes ;
- fournisseurs externes ;
- caches, journaux et sauvegardes ;
- conséquences d’une lecture, modification ou indisponibilité abusive.

Prioriser les protections selon l’effet réel. Une règle générale sans menace identifiée peut donner une fausse impression de sécurité.

## Frontières de confiance

Considérer comme externe jusqu’à validation :

- paramètres de route et de recherche ;
- corps, cookies et en-têtes ;
- formulaire et fichier ;
- réponse d’un fournisseur ;
- message de file de travail ;
- variable d’environnement ;
- donnée persistée dont le schéma n’est pas garanti ;
- valeur transmise par un composant navigateur ;
- contenu d’un webhook.

TypeScript ne valide pas une valeur au moment de l’exécution.

## Validation

Valider à la frontière :

- type ;
- présence ;
- longueur et taille ;
- format ;
- valeurs autorisées ;
- cohérence entre champs ;
- règle métier ;
- organisation et permission.

Transformer ensuite vers un type métier sûr. Ne pas propager un objet externe général dans les couches internes.

La validation navigateur sert l’utilisateur. La validation serveur protège le système.

## Secrets et configuration

- Garder les secrets dans un gestionnaire ou mécanisme serveur autorisé.
- Toute variable utilisant le préfixe public de Next.js est visible dans le navigateur.
- Séparer secrets de construction et secrets d’exécution.
- Limiter chaque secret à une finalité, un environnement et des permissions.
- Prévoir rotation, révocation et réponse à une fuite.
- Échouer clairement lorsqu’un secret obligatoire manque.
- Ne jamais placer un secret dans l’adresse, une métadonnée, un message utilisateur ou un journal.

Utiliser `server-only` pour empêcher une importation accidentelle dans le code navigateur lorsque compatible. Cette protection complète l’architecture ; elle ne remplace pas la minimisation des données.

## Frontière serveur et navigateur

Tout module sous `use client` doit être traité comme livrable au navigateur. Inspecter ses importations, constantes et données.

Un composant navigateur ne reçoit que les champs nécessaires. Ne pas transmettre une entité complète puis masquer certains champs dans l’affichage.

Une fonction exécutée sur le serveur ne devient pas sûre automatiquement. Elle vérifie identité, autorisation, organisation, entrée et ressource à chaque appel.

## Injection dans les données

- Utiliser les paramètres fournis par le client de données.
- Ne jamais concaténer une entrée dans une requête.
- Limiter dynamiquement les colonnes de tri et filtre à une liste autorisée.
- Vérifier les expressions de recherche avancée.
- Appliquer le même principe aux commandes système, modèles de courriel et autres langages interprétés.

Un outil de mapping de données réduit certains risques mais n’autorise pas à transmettre directement un objet externe dans une opération générale.

## Contenu navigateur

Éviter l’insertion de contenu HTML non maîtrisé. Une utilisation de `dangerouslySetInnerHTML` exige purification adaptée, justification et tests hostiles.

Configurer une politique de sécurité du contenu compatible avec les scripts nécessaires. Ne pas élargir les sources ou activer une exécution dangereuse pour corriger rapidement un script tiers.

Encoder les données selon leur contexte : texte, attribut, adresse, script ou style. Une purification conçue pour un contexte ne garantit pas les autres.

## Requêtes forgées et origines

Protéger les mutations utilisant une session navigateur contre les requêtes forgées depuis un autre site. Vérifier les protections fournies par Next.js et la bibliothèque de session, puis tester la topologie réelle derrière les serveurs mandataires.

Configurer les origines supplémentaires des traitements serveur uniquement lorsqu’elles sont nécessaires et validées. Une liste générale annule la protection attendue.

La politique de partage entre origines d’une route HTTP ne remplace pas la protection contre les requêtes forgées, l’authentification ou l’autorisation.

## Requêtes serveur vers l’extérieur

Lorsqu’une adresse dépend d’une entrée :

- autoriser des protocoles et domaines précis ;
- refuser les adresses locales et réseaux internes non nécessaires ;
- vérifier la destination après résolution et redirection ;
- limiter nombre de redirections, durée et taille ;
- ne pas transmettre automatiquement cookies, jetons ou en-têtes internes ;
- protéger les métadonnées de l’infrastructure.

Appliquer ces règles aux aperçus d’adresse, imports d’image, rappels et services mandataires.

## Fichiers

Pour un téléversement :

- limite avant traitement coûteux ;
- type réel et extension ;
- nom neutralisé ;
- stockage non exécutable ;
- analyse adaptée au risque ;
- organisation propriétaire ;
- état de traitement ;
- suppression et conservation.

Pour un téléchargement, vérifier l’autorisation juste avant l’émission et empêcher la traversée de chemin.

Une adresse temporaire doit avoir une portée, une durée et une opération limitées.

## Limitation des abus

Protéger selon le risque :

- connexion et récupération de compte ;
- invitation ;
- recherche coûteuse ;
- génération de fichier ;
- envoi de message ;
- paiement ;
- webhook ;
- création automatisée.

Combiner limites par identité, organisation, adresse réseau ou ressource lorsque nécessaire. Prévoir un comportement en cas de stockage de limitation indisponible.

Une limite ne doit pas permettre à un client de provoquer le refus de tous les autres.

## Chiffrement et données sensibles

- Utiliser le chiffrement du transport.
- Utiliser les capacités de chiffrement au repos de l’infrastructure.
- Ajouter un chiffrement applicatif seulement avec une gestion de clés, une rotation et un besoin démontrés.
- Ne pas inventer un algorithme.
- Hacher les mots de passe avec une bibliothèque spécialisée et des paramètres maintenus.
- Ne pas réutiliser une clé entre environnements ou finalités.

Le chiffrement ne remplace pas les permissions, la minimisation ni la suppression.

## Erreurs et journaux

Ne jamais exposer :

- pile technique ;
- requête de données ;
- chemin interne ;
- secret ou jeton ;
- corps brut sensible ;
- réponse fournisseur complète ;
- information d’une autre organisation.

Le message public contient une explication et, lorsque disponible, un identifiant de corrélation. Le journal technique conserve la cause utile après expurgation.

Ne pas journaliser par défaut les mots de passe, codes temporaires, cookies, en-têtes d’autorisation, numéros financiers complets ou contenu de formulaire.

## En-têtes et transport

Évaluer :

- sécurité du transport ;
- politique de sécurité du contenu ;
- protection contre l’intégration dans une page hostile ;
- type de contenu strict ;
- politique de référent ;
- permissions des fonctions du navigateur ;
- cache des réponses sensibles.

Tester les en-têtes sur la réponse déployée, pas seulement dans la configuration source.

## Dépendances et chaîne de construction

- Verrouiller les dépendances.
- Examiner les scripts d’installation.
- Évaluer les alertes selon le chemin réellement utilisé.
- Retirer les paquets inutiles.
- Ne pas exécuter un générateur non vérifié avec des secrets de production.
- Rechercher les secrets et fichiers sensibles avant publication.
- Protéger les identités de construction et déploiement.

Une mise à jour urgente reste soumise aux tests proportionnés au risque.

## Sauvegardes et environnements

Les sauvegardes contiennent les mêmes données sensibles que la production. Protéger accès, chiffrement, durée, copie et restauration.

Séparer les environnements et leurs identités. Ne pas permettre à un environnement de développement d’accéder implicitement à la production.

## Contrôles obligatoires

- appel direct de chaque point d’entrée ;
- entrée mal formée, inattendue et trop volumineuse ;
- injection dans filtre, tri et recherche ;
- session absente, permission refusée et autre organisation ;
- requête forgée depuis une origine non autorisée ;
- adresse externe redirigée vers un réseau interne ;
- fichier trompeur ou trop grand ;
- limite de débit et concurrence ;
- inspection du code navigateur et de la construction pour les secrets ;
- erreur inattendue sans fuite ;
- journaux et sauvegardes expurgés et protégés ;
- en-têtes sur le déploiement réel ;
- analyse des dépendances.

## Sources officielles

- [Sécurité des données Next.js](https://nextjs.org/docs/app/guides/data-security)
- [Configuration des traitements serveur](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions)
- [Variables d’environnement Next.js](https://nextjs.org/docs/app/guides/environment-variables)
- [Risques de sécurité des interfaces de programmation](https://owasp.org/API-Security/)
