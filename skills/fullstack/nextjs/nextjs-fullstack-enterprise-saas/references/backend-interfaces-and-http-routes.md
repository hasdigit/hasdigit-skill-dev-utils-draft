# Interfaces backend et routes HTTP

Lire ce document avant de créer ou modifier un gestionnaire de route, une interface publique, un webhook, un téléchargement ou un contrat consommé hors de l’application.

## Identifier le consommateur

Classer chaque interface :

- interne au rendu serveur Next.js ;
- interne à l’interface navigateur ;
- application mobile ou autre produit ;
- partenaire externe ;
- webhook entrant ;
- rappel après une redirection externe ;
- fichier ou flux de données ;
- interface d’administration.

Le consommateur détermine l’authentification, la stabilité, la version, les limites et la documentation nécessaires.

## Ne pas créer une route inutile

Un composant serveur peut appeler directement un cas d’usage serveur. Passer par une route HTTP interne ajoute sérialisation, réseau, authentification et gestion d’erreur sans bénéfice lorsque les deux vivent dans le même processus.

Créer une route lorsque le réseau est une vraie frontière : autre application, navigateur indépendant, fournisseur externe, webhook, fichier ou protocole public.

Les traitements serveur servent principalement les mutations du frontend Next.js. Ils ne remplacent pas un contrat public stable.

## Gestionnaire de route mince

`route.ts` doit uniquement :

1. sélectionner la méthode ;
2. lire et limiter l’entrée ;
3. valider le type de contenu et le schéma ;
4. résoudre l’identité et l’organisation ;
5. appeler un cas d’usage ;
6. convertir le résultat en statut, en-têtes et corps ;
7. journaliser le résultat de manière sûre.

La transaction, la politique métier et l’appel direct au client de données appartiennent hors de l’adaptateur.

## Contrat d’entrée

Définir pour chaque opération :

- méthode réseau ;
- adresse ;
- paramètres de chemin ;
- paramètres de recherche ;
- en-têtes requis ;
- type de contenu ;
- taille maximale ;
- schéma du corps ;
- mécanisme d’authentification ;
- permission ;
- portée de l’organisation ;
- comportement de répétition.

Une donnée TypeScript n’existe pas comme garantie au moment de l’exécution. Valider chaque entrée avec un schéma et refuser les champs inattendus lorsque leur acceptation présente un risque.

## Contrat de sortie

Définir :

- statut ;
- type de contenu ;
- forme du résultat ;
- erreurs attendues ;
- en-têtes de cache ;
- pagination ;
- politique de compatibilité ;
- données sensibles supprimées.

Retourner un objet de transfert limité. Ne pas sérialiser directement une entité de base de données ou une erreur fournisseur.

## Statuts réseau

Utiliser les statuts selon leur sens et toujours accompagner le nombre d’une explication :

- `200` (succès avec contenu) ;
- `201` (création réussie, avec emplacement lorsque pertinent) ;
- `204` (succès sans contenu) ;
- `400` (entrée invalide) ;
- `401` (identité absente ou invalide) ;
- `403` (identité valide mais permission refusée) ;
- `404` (ressource absente ou volontairement non révélée) ;
- `409` (conflit avec l’état actuel) ;
- `413` (taille dépassée) ;
- `429` (limite de fréquence atteinte) ;
- `500` (erreur interne inattendue) ;
- `503` (dépendance ou service temporairement indisponible).

Ne pas répondre systématiquement avec un succès contenant un champ d’erreur. Ne pas renvoyer un numéro sans explication compréhensible. Ne pas révéler l’existence d’une ressource d’une autre organisation lorsque cette information est sensible.

## Erreur structurée

Une erreur publique devrait contenir selon le besoin :

```ts
interface InterfacePublicRouteErrorResponse {
  errorCode: string;
  userMessage: string;
  correlationIdentifier?: string;
  fieldErrors?: Record<string, string[]>;
}
```

Le code sert à une machine et reste stable. Le message est compréhensible. L’identifiant de corrélation permet le diagnostic sans exposer la pile, la requête de données ou le fournisseur.

## Autorisation sur la ressource

Vérifier séparément :

- identité ;
- permission fonctionnelle ;
- appartenance de la ressource à l’organisation ;
- droit sur les propriétés retournées ;
- droit sur l’opération dans l’état courant.

Une permission générale de lecture ne signifie pas que toutes les lignes et colonnes sont visibles. Tester un identifiant valide appartenant à une autre organisation.

## Pagination, filtre et tri

Pour une collection :

- imposer une limite maximale ;
- utiliser une liste explicite de champs filtrables et triables ;
- choisir un ordre déterministe ;
- inclure un départage unique ;
- préférer un curseur pour les données fréquemment modifiées ;
- ne pas accepter un fragment de requête de données fourni par le consommateur.

Un curseur doit être opaque pour le consommateur, validé et lié aux paramètres qui déterminent la liste lorsque nécessaire.

## Version et compatibilité

Versionner lorsqu’un contrat possède plusieurs consommateurs indépendants ou une évolution non coordonnée.

Une évolution compatible peut :

- ajouter un champ facultatif ;
- ajouter une nouvelle opération ;
- accepter une valeur supplémentaire si les consommateurs tolèrent l’inconnu.

Une évolution incompatible peut :

- supprimer ou renommer un champ ;
- changer son type ou son sens ;
- rendre obligatoire une donnée auparavant facultative ;
- modifier un statut ou une règle de pagination ;
- restreindre silencieusement un comportement utilisé.

Pour une rupture : nouvelle version, période de transition, inventaire des consommateurs, mesures d’usage, date de retrait et guide de migration.

## Description OpenAPI

Pour une interface partagée, maintenir une description conforme à une version choisie de la spécification OpenAPI. Elle doit permettre à une personne et à un outil de comprendre :

- opérations ;
- entrées et sorties ;
- mécanismes de sécurité ;
- erreurs ;
- exemples expurgés ;
- versions et serveurs.

Valider la description automatiquement et vérifier qu’elle correspond au comportement réel. Ne pas générer une documentation qui présente un contrat plus large que ce que l’autorisation permet.

## Origines et navigateurs

Le partage entre origines, souvent appelé CORS dans le standard web, doit utiliser une liste minimale d’origines, méthodes et en-têtes autorisés.

- Ne pas réfléchir automatiquement une origine reçue.
- Ne pas autoriser toutes les origines avec des informations d’identification.
- Répondre correctement aux demandes préalables avec la méthode `OPTIONS`.
- Tester la réponse derrière le serveur mandataire réel.

Une politique d’origine ne remplace ni authentification ni autorisation.

## Limitation des ressources

Définir selon le risque :

- taille du corps ;
- nombre d’éléments ;
- complexité des filtres ;
- durée maximale ;
- fréquence par identité, organisation, adresse ou clé ;
- concurrence ;
- coût d’une exportation ou recherche.

Une limite doit produire une erreur claire et être observable. Éviter une clé de limitation qui permet à une organisation de bloquer toutes les autres.

## Répétition sûre

Les créations financières, commandes externes et webhooks doivent reconnaître une répétition. Utiliser un identifiant de répétition avec :

- portée définie ;
- unicité protégée ;
- durée de conservation ;
- empreinte de la demande lorsque nécessaire ;
- retour du résultat précédent ou conflit explicite.

Ne pas supposer qu’une méthode réseau protège automatiquement des doubles appels.

## Webhooks

Un webhook entrant doit :

- lire le corps brut si la vérification de signature l’exige ;
- vérifier signature, horodatage et source ;
- refuser une ancienneté excessive ;
- enregistrer l’identifiant unique de l’événement ;
- répondre rapidement ;
- déplacer le traitement lourd vers une tâche durable ;
- rendre les répétitions sans danger ;
- isoler l’organisation à partir d’une association vérifiée.

Ne pas placer un secret durable dans l’adresse. Ne pas journaliser le corps complet par défaut.

## Fichiers et flux

Pour un téléversement : taille, type réel, nom neutralisé, autorisation, stockage, analyse de sécurité et propriété d’organisation.

Pour un téléchargement : autorisation juste avant émission, type correct, nom sûr, limite et absence de traversée de chemin.

Utiliser un flux lorsque le contenu est volumineux et que l’hébergement le supporte. Tester interruption, délai, mémoire et reprise.

## Contrôles obligatoires

- appel direct sans interface utilisateur ;
- méthode non autorisée ;
- type de contenu absent ou incorrect ;
- corps mal formé, trop grand ou contenant des champs inattendus ;
- session absente et permission refusée ;
- ressource d’une autre organisation ;
- propriétés sensibles absentes ;
- pagination stable sous modification ;
- répétition de création et de webhook ;
- origine autorisée et interdite ;
- limite de débit et délai ;
- compatibilité avec la version précédente ;
- concordance entre description et comportement.

## Sources officielles

- [Next.js comme backend pour son frontend](https://nextjs.org/docs/app/guides/backend-for-frontend)
- [Gestionnaires de routes Next.js](https://nextjs.org/docs/app/api-reference/file-conventions/route)
- [Spécification OpenAPI](https://spec.openapis.org/oas/latest.html)
- [Risques de sécurité propres aux interfaces de programmation](https://owasp.org/API-Security/)
