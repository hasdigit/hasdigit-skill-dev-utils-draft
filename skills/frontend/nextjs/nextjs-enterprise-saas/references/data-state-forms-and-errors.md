# Données, état, formulaires et erreurs

Lire ce document pour toute lecture de données, interaction, formulaire, synchronisation avec l’adresse, appel réseau, mise à jour anticipée ou gestion d’erreur.

## Une seule autorité par information

Avant de créer un état, déterminer où se trouve son autorité :

- base de données ou service serveur ;
- adresse de la page ;
- état local d’un composant ;
- contexte partagé dans le navigateur ;
- configuration ;
- cache dérivé d’une autre source.

Ne pas conserver la même information comme autorité indépendante à plusieurs endroits. Une copie destinée à l’affichage doit avoir une règle claire de synchronisation et de péremption.

## Choisir le niveau d’état

### Donnée serveur

Une donnée persistée, partagée ou soumise à autorisation appartient au serveur. La charger dans un composant serveur ou une fonction serveur autorisée lorsque l’interaction n’exige pas une lecture directe depuis le navigateur.

### État dans l’adresse

Placer dans l’adresse web les valeurs qui doivent survivre au rechargement, au partage ou à l’historique : recherche, filtre, tri, page, onglet métier et sélection navigable.

Valider les paramètres à chaque entrée. Une adresse peut être fabriquée manuellement et ne constitue jamais une source de confiance.

### État local dans le navigateur

Réserver l’état local aux interactions temporaires : champ en cours, panneau ouvert, élément survolé ou étape non encore confirmée.

### État global dans le navigateur

Créer un état global seulement lorsque plusieurs zones éloignées doivent partager une information réellement commune et interactive. Une session, une donnée serveur ou un paramètre d’adresse ne doit pas être copié dans un magasin global sans raison et stratégie de synchronisation.

## Lecture des données

- Charger au plus près de la responsabilité qui consomme la donnée.
- Exécuter en parallèle les lectures indépendantes.
- Commencer une lecture tôt et attendre son résultat tard lorsque cela réduit une chaîne séquentielle.
- Sélectionner uniquement les champs nécessaires.
- Appliquer l’autorisation dans la fonction de lecture.
- Définir la fraîcheur et la portée du cache.
- Prévoir chargement, absence et erreur.

Un composant serveur peut appeler directement une fonction serveur. Ne pas créer un gestionnaire de route interne uniquement pour reproduire cet appel par le réseau.

## Lectures déclenchées dans le navigateur

Une lecture navigateur est pertinente pour une interaction très dynamique, une actualisation indépendante, une interface de navigation du navigateur ou un fournisseur exclusivement client.

Elle doit gérer :

- demande en cours ;
- réponse devenue ancienne après une nouvelle demande ;
- annulation lorsque possible ;
- déduplication ;
- durée de validité ;
- nouvelle tentative limitée ;
- erreur et récupération ;
- session expirée ;
- changement d’organisation cliente.

Une dépendance instable dans un effet peut produire une boucle de requêtes. Stabiliser l’intention, pas seulement la référence technique. Tester les saisies rapides, changements de route et démontages de composant.

## Formulaires avec traitement serveur

Un traitement serveur peut recevoir les données d’un formulaire et permet une amélioration progressive. Il reste un point d’entrée réseau.

Le traitement doit :

1. lire uniquement les champs attendus ;
2. valider les types, tailles, formats et règles métier ;
3. vérifier session, permission, organisation et ressource ;
4. effectuer la modification de manière cohérente ;
5. gérer les répétitions dangereuses ;
6. invalider les lectures concernées ;
7. retourner un résultat limité destiné à l’utilisateur ;
8. journaliser sans information sensible inutile.

Le navigateur peut vérifier rapidement un format, mais le serveur répète toujours la validation complète.

## Résultat explicite d’une action

Pour une erreur attendue, préférer un résultat discriminé compréhensible à une exception générique :

```ts
type TypeInvoicePaymentResult =
  | {
      status: "completed";
      paymentIdentifier: string;
      userMessage: string;
    }
  | {
      status: "invalid-input";
      fieldErrors: Record<string, string[]>;
      userMessage: string;
    }
  | {
      status: "permission-denied";
      userMessage: string;
    }
  | {
      status: "failed";
      correlationIdentifier: string;
      userMessage: string;
    };
```

Le type doit suivre les conventions de [nommage et types](naming-and-types.md). Les messages ne doivent révéler ni l’existence d’une ressource inaccessible ni les détails de l’infrastructure.

## Erreurs attendues et défaillances inattendues

### Erreur attendue

Une entrée invalide, un refus métier, une ressource absente ou une permission manquante fait partie du comportement du produit. La représenter comme un résultat et l’afficher près de l’action concernée.

### Défaillance inattendue

Une indisponibilité, une incohérence ou une erreur de programmation doit atteindre la frontière d’erreur appropriée. Elle doit être enregistrée avec un identifiant de corrélation, sans exposer de pile technique à l’utilisateur.

Ne pas entourer tout le code d’un bloc qui transforme indistinctement chaque erreur en même message. Cette pratique détruit l’information nécessaire au diagnostic et peut intercepter des mécanismes de contrôle du framework.

## Frontières d’erreur Next.js

- `error.tsx` traite les défaillances non gérées d’un segment et doit permettre une récupération sûre.
- `global-error.tsx` couvre la racine lorsque la défaillance empêche la mise en page principale de fonctionner.
- `not-found.tsx` représente une absence contrôlée, pas une panne générale.
- Une erreur attendue d’un formulaire doit revenir comme résultat, pas dépendre uniquement d’une frontière d’exception.

Placer les frontières assez près pour préserver les zones indépendantes, sans dupliquer le même traitement à chaque niveau.

## Taxonomie minimale

Chaque projet devrait distinguer avec des noms complets :

- entrée invalide ;
- session absente ou expirée ;
- permission refusée ;
- ressource absente ;
- conflit de modification ;
- limite métier atteinte ;
- service externe indisponible ;
- délai dépassé ;
- réponse externe invalide ;
- erreur interne inattendue.

Une normalisation centrale peut convertir les erreurs techniques vers cette taxonomie. Elle ne doit pas supprimer la cause dans les journaux autorisés.

## Mise à jour anticipée de l’interface

Une mise à jour anticipée affiche le résultat supposé avant la confirmation serveur. L’utiliser uniquement lorsque :

- la réussite est probable ;
- l’annulation ou la correction est claire ;
- l’échec ne crée pas une fausse preuve dangereuse ;
- l’état serveur reste l’autorité ;
- les réponses dans un ordre différent sont gérées.

Ne pas afficher comme définitivement payé, supprimé ou autorisé un élément avant confirmation lorsque l’erreur aurait un coût important.

## Répétition, nouvelle tentative et cohérence

- Rendre une opération répétée sûre lorsqu’un double appel est plausible.
- Utiliser un identifiant de répétition pour les opérations financières ou externes lorsque nécessaire.
- Ne relancer automatiquement que les opérations dont la répétition est sûre.
- Limiter le nombre de tentatives et augmenter le délai entre elles.
- Ne pas relancer automatiquement une erreur de validation ou de permission.
- Conserver l’ordre logique des réponses lorsque plusieurs demandes se chevauchent.

## Téléversement, export et traitements différés

Un téléversement doit fournir progression, annulation lorsque possible, validation serveur, limite de taille, résultat durable et reprise compréhensible.

Un export volumineux ou un traitement long devrait devenir une tâche suivie plutôt qu’une requête bloquante. L’interface doit indiquer son état, permettre de retrouver le résultat et ne pas inventer une réussite avant la fin réelle.

## Cache et état

Le cache est une copie dérivée, jamais l’autorité métier. Documenter sa clé, sa portée, sa fraîcheur et son invalidation dans [Routage, rendu et cache](routing-rendering-and-cache.md).

Après une modification, vérifier le résultat serveur puis actualiser l’interface avec le mécanisme supporté par la version. Éviter de maintenir simultanément une copie locale, une copie globale et une copie mise en cache sans règle de résolution.

## Contrôles obligatoires

- rechargement direct et retour dans l’historique ;
- deux demandes rapides dont les réponses arrivent dans l’ordre inverse ;
- changement d’organisation pendant une donnée en cours ;
- formulaire invalide, autorisé, refusé et répété ;
- erreur attendue et défaillance inattendue ;
- service lent, indisponible et réponse mal formée ;
- mise à jour anticipée réussie puis échouée ;
- cache invalidé et lecture suivante ;
- session expirée pendant l’action ;
- traitement différé repris dans une nouvelle session.

## Sources officielles

- [Gestion des erreurs dans l’App Router](https://nextjs.org/docs/app/getting-started/error-handling)
- [Formulaires avec les traitements serveur](https://nextjs.org/docs/app/guides/forms)
- [Composants serveur et composants client](https://nextjs.org/docs/app/getting-started/server-and-client-components)
