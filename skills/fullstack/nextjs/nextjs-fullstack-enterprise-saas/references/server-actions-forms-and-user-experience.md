# Traitements serveur, formulaires et expérience utilisateur

Lire ce document pour une mutation initiée par l’interface, un formulaire, une mise à jour anticipée, un chargement, une erreur ou un retour d’action.

## Choisir entre traitement serveur et route HTTP

Utiliser un traitement serveur lorsque l’action appartient au frontend Next.js et bénéficie de l’intégration au rendu et aux formulaires.

Utiliser une route HTTP lorsque :

- un consommateur externe doit l’appeler ;
- le contrat doit être documenté et versionné indépendamment ;
- le contenu n’est pas lié à une action d’interface ;
- une méthode, un flux ou un protocole réseau précis est nécessaire.

Les traitements serveur sont destinés principalement aux mutations. Ne pas les utiliser comme mécanisme général de lecture : leurs appels peuvent être ordonnés de manière séquentielle selon le framework.

## Adaptateur mince

Un traitement serveur doit :

1. recevoir une entrée limitée ;
2. la valider côté serveur ;
3. vérifier session, permission, organisation et ressource ;
4. appeler un cas d’usage ;
5. invalider les lectures concernées après réussite ;
6. retourner un résultat destiné à l’interface.

Il ne doit pas contenir directement une transaction complexe, un accès général aux données ou une politique dupliquée.

## Formulaire progressivement utilisable

Utiliser les capacités natives du langage HTML, le langage de structure des pages, avant une interaction entièrement personnalisée.

Un formulaire doit rester aussi fonctionnel que raisonnablement possible pendant le chargement du code navigateur. Ajouter un composant navigateur lorsque l’état en cours, la validation interactive ou une mise à jour anticipée apporte une valeur réelle.

Chaque champ possède :

- nom complet ;
- libellé visible ;
- type adapté ;
- aide lorsque nécessaire ;
- indication des contraintes ;
- erreur reliée au champ ;
- valeur conservée après une erreur récupérable.

## Validation en deux niveaux

Le navigateur fournit un retour rapide avec les contraintes natives ou une validation interactive. Le serveur répète toujours :

- type ;
- taille ;
- format ;
- relation entre champs ;
- règle métier ;
- permission ;
- organisation ;
- état actuel de la ressource.

Ne pas transmettre directement l’objet du formulaire à la base de données.

## Résultat discriminé

Modéliser les résultats attendus :

```ts
type TypeCreateInvoiceActionResult =
  | { status: "idle" }
  | { status: "created"; invoiceIdentifier: string; userMessage: string }
  | {
      status: "invalid-input";
      fieldErrors: Record<string, string[]>;
      userMessage: string;
    }
  | { status: "permission-denied"; userMessage: string }
  | {
      status: "failed";
      correlationIdentifier: string;
      userMessage: string;
    };
```

Une erreur attendue revient comme résultat. Une défaillance inattendue atteint la frontière d’erreur appropriée après journalisation sûre.

## État en cours

Pendant une soumission :

- garder le contrôle identifiable ;
- empêcher une répétition dangereuse ;
- annoncer l’état lorsque nécessaire ;
- ne pas bloquer les parties indépendantes ;
- conserver une mise en page stable ;
- permettre l’annulation seulement si elle est réelle et sûre.

Désactiver un bouton sans explication peut rendre l’interface incompréhensible. Afficher l’action en cours ou la raison du blocage.

## Retour après action

Toute action produit un effet visible :

- réussite confirmée ;
- donnée actualisée ;
- erreur près de l’action ;
- possibilité de corriger ;
- prochaine étape ;
- emplacement d’un résultat différé.

Une notification temporaire ne doit pas être l’unique preuve d’une modification importante. Actualiser aussi le contenu concerné.

## Répétition sûre

Protéger les opérations dont un double appel aurait un effet :

- paiement ;
- invitation ;
- création de commande ;
- envoi externe ;
- génération facturée ;
- suppression.

Combiner état en cours dans l’interface, identifiant de répétition et contrainte serveur selon le risque. L’interface seule n’empêche pas un appel fabriqué.

## Mise à jour anticipée

Afficher un résultat avant confirmation seulement lorsque :

- la réussite est probable ;
- le retour arrière est clair ;
- l’échec ne crée pas une fausse preuve grave ;
- l’état serveur reste l’autorité ;
- les réponses concurrentes sont maîtrisées.

Ne pas afficher un paiement, une autorisation ou une suppression définitive avant confirmation si l’erreur présente un coût important.

## Demandes concurrentes

Pour une recherche, un filtre ou une modification rapide :

- identifier l’intention courante ;
- annuler la demande précédente lorsque possible ;
- ignorer une réponse devenue ancienne ;
- empêcher une boucle due à un effet instable ;
- réinitialiser après changement d’organisation ;
- ne pas mélanger des résultats de deux routes.

Tester volontairement des réponses dans l’ordre inverse.

## Erreurs et frontières Next.js

- `error.tsx` traite une défaillance non gérée du segment.
- `global-error.tsx` traite une défaillance empêchant la racine de fonctionner.
- `not-found.tsx` représente une absence contrôlée.
- Une erreur de formulaire attendue reste près du formulaire.

Une frontière doit afficher un message compréhensible, permettre une nouvelle tentative seulement si elle est sûre et ne pas exposer la pile technique.

## Listes et collections

Une collection doit définir :

- chargement ;
- absence ;
- erreur ;
- filtre ;
- tri ;
- pagination ;
- sélection ;
- action groupée ;
- état dans l’adresse lorsque partageable.

Préférer une pagination serveur pour les grands ensembles. Limiter le nombre d’éléments et conserver un ordre déterministe.

## Dialogues et opérations destructives

Utiliser un dialogue pour une décision courte qui doit interrompre le parcours. Utiliser une page pour une tâche longue, partageable ou reprise plus tard.

Une confirmation destructive doit nommer l’objet, l’effet, la possibilité de récupération et l’action exacte. Ne pas demander une confirmation générique pour chaque action sans risque réel.

## Accessibilité

- Bouton pour une action, lien pour une navigation.
- Focus visible et ordre logique.
- Erreurs reliées aux champs.
- Résultat annoncé sans interrompre inutilement.
- Utilisation complète au clavier.
- Zoom et textes longs sans chevauchement.
- Contraste dans toutes les marques.
- Mouvement réduit respecté.

## Traitement long

Une opération qui dépasse raisonnablement la durée d’une requête devient une tâche durable. L’interface reçoit un identifiant de suivi et affiche :

- état en attente ;
- progression lorsqu’elle est fiable ;
- résultat ;
- erreur et possibilité de reprise ;
- emplacement où retrouver le travail après avoir quitté la page.

Ne pas laisser une requête ouverte sans limite pour simuler une file de travail.

## Contrôles obligatoires

- formulaire avant et après chargement du code navigateur lorsque applicable ;
- entrée vide, invalide et trop longue ;
- session expirée, permission refusée et autre organisation ;
- double soumission ;
- réponses concurrentes dans l’ordre inverse ;
- erreur métier et défaillance inattendue ;
- perte de réseau et nouvelle tentative ;
- mise à jour anticipée réussie et annulée ;
- invalidation et lecture après modification ;
- clavier, focus, zoom et technologie d’assistance ;
- traitement long repris après une nouvelle session.

## Sources officielles

- [Formulaires avec traitements serveur Next.js](https://nextjs.org/docs/app/guides/forms)
- [Modification des données dans Next.js](https://nextjs.org/docs/app/getting-started/mutating-data)
- [Gestion des erreurs Next.js](https://nextjs.org/docs/app/getting-started/error-handling)
