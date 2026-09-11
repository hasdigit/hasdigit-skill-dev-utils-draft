# Scénarios de validation du skill Next.js fullstack

Un scénario réussit seulement si le résultat attendu est démontré et si le comportement interdit ne se produit pas.

## Nouvelle application fullstack

- **Situation** : création d’un produit Next.js avec interface, routes backend et base de données.
- **Résultat attendu** : versions et hébergement vérifiés, modules métier définis, couches visibles, données possédées et contrôles prévus avant le code.
- **Comportement interdit** : placer toutes les pages, routes et requêtes directement dans `app/`.

## Projet existant non structuré

- **Situation** : ajout limité dans un projet où `lib/` contient des responsabilités mélangées.
- **Résultat attendu** : modification compatible et limitée, nouvelle capacité correctement possédée, dette existante documentée.
- **Comportement interdit** : refonte générale non demandée ou duplication de la structure confuse.

## Nouvelle fonctionnalité dans un module existant

- **Situation** : ajout du paiement de facture dans le module de facturation.
- **Résultat attendu** : dossier de fonctionnalité vertical, responsabilités locales conservées ensemble et partage limité aux éléments réellement communs.
- **Comportement interdit** : disperser la capacité dans des dossiers globaux ou importer les détails privés d’une autre fonctionnalité.

## Lecture pendant le rendu serveur

- **Situation** : une page serveur charge une facture.
- **Résultat attendu** : appel direct d’une lecture autorisée et limitée du module.
- **Comportement interdit** : appel réseau vers une route interne du même processus.

## Route publique

- **Situation** : une application mobile doit lire des factures.
- **Résultat attendu** : gestionnaire de route mince, contrat documenté, version, validation, permission, organisation, pagination et réponses limitées.
- **Comportement interdit** : exposer directement l’entité de base de données.

## Traitement serveur

- **Situation** : le frontend crée une facture avec un formulaire.
- **Résultat attendu** : adaptateur mince, validation serveur, cas d’usage, transaction, répétition sûre, invalidation et résultat utilisateur.
- **Comportement interdit** : logique métier et client de données directement dans le traitement.

## Accès croisé entre organisations

- **Situation** : un identifiant valide d’une autre organisation est envoyé.
- **Résultat attendu** : refus sans fuite, filtre de données, politique et test croisé.
- **Comportement interdit** : faire confiance à l’organisation reçue du navigateur.

## Concurrence

- **Situation** : deux demandes confirment simultanément le même paiement.
- **Résultat attendu** : contrainte, verrouillage ou identifiant de répétition empêchant le double effet.
- **Comportement interdit** : lecture puis écriture non protégées.

## Transaction et fournisseur externe

- **Situation** : une écriture locale doit déclencher un envoi externe.
- **Résultat attendu** : transaction locale cohérente et intention durable traitée après confirmation.
- **Comportement interdit** : transaction ouverte pendant un appel lent ou événement perdu après l’écriture.

## Migration incompatible

- **Situation** : une colonne utilisée doit être renommée.
- **Résultat attendu** : extension compatible, transfert reprenable, bascule vérifiée et retrait ultérieur.
- **Comportement interdit** : renommage et suppression immédiats pendant un déploiement progressif.

## Transfert interrompu

- **Situation** : un transfert massif s’arrête au milieu.
- **Résultat attendu** : lots répétables, reprise au bon point, mesures et vérification finale.
- **Comportement interdit** : relancer depuis zéro avec doublons ou corruption.

## Cache personnalisé

- **Situation** : une lecture dépend de l’utilisateur et de l’organisation.
- **Résultat attendu** : lecture dynamique ou clé démontrant l’isolation, avec invalidation ciblée.
- **Comportement interdit** : cache global partagé.

## Plusieurs instances

- **Situation** : une instance modifie une donnée et une autre la lit.
- **Résultat attendu** : cache et invalidation coordonnés, connexions dimensionnées et artefact cohérent.
- **Comportement interdit** : supposer la synchronisation des caches locaux.

## Travail après réponse

- **Situation** : un courriel obligatoire doit être envoyé après une action.
- **Résultat attendu** : tâche durable, répétable, observable et reprenable.
- **Comportement interdit** : dépendre seulement de `after` sans garantie de livraison.

## Webhook répété

- **Situation** : un fournisseur envoie deux fois le même événement.
- **Résultat attendu** : signature, date et identifiant vérifiés, effet métier unique et réponse rapide.
- **Comportement interdit** : doubler l’opération.

## Fournisseur indisponible

- **Situation** : un service externe ralentit puis échoue.
- **Résultat attendu** : délai, tentatives limitées, coupe-circuit, erreur compréhensible et observation.
- **Comportement interdit** : attente sans limite ou fausse réussite.

## Fichier dangereux

- **Situation** : un fichier volumineux avec extension trompeuse est envoyé.
- **Résultat attendu** : refus précoce, type réel, nom neutralisé, autorisation et stockage sûr.
- **Comportement interdit** : stocker directement sous le nom fourni.

## Contrat incompatible

- **Situation** : un champ public doit changer de type.
- **Résultat attendu** : inventaire des consommateurs, nouvelle version, période de transition et test de compatibilité.
- **Comportement interdit** : changement silencieux.

## Erreur compréhensible

- **Situation** : une opération échoue dans la base de données.
- **Résultat attendu** : message humain, code stable expliqué, identifiant de corrélation et journal expurgé.
- **Comportement interdit** : pile, requête ou code seul présenté à l’utilisateur.

## Frontière navigateur

- **Situation** : une bibliothèque interactive importe un module serveur.
- **Résultat attendu** : construction refusée ou séparation par un contrat sûr et limité.
- **Comportement interdit** : secret ou client de données livré au navigateur.

## Page publique multi-marque

- **Situation** : deux domaines et deux langues partagent l’application.
- **Résultat attendu** : contenu initial, titre, adresse canonique, langue, image et cache correspondent à chaque combinaison.
- **Comportement interdit** : servir les métadonnées d’une autre organisation.

## Montée en charge

- **Situation** : la latence augmente sous charge.
- **Résultat attendu** : limite mesurée, options comparées et correction ciblée vérifiée.
- **Comportement interdit** : extraire un service ou ajouter un cache sans diagnostic.

## Déploiement avec migration

- **Situation** : code et schéma évoluent pendant que deux versions coexistent.
- **Résultat attendu** : compatibilité dans les deux sens nécessaires, signaux d’arrêt et retour réaliste.
- **Comportement interdit** : dépendre immédiatement d’une suppression irréversible.

## Nommage compréhensible

- **Situation** : création de contrats, tables et dossiers.
- **Résultat attendu** : mots complets, préfixes `Interface`, `Type`, `Enumeration`, domaine et responsabilité visibles.
- **Comportement interdit** : `I`, `T`, `E`, `utils`, `svc`, `dto` ou codes sans explication.

## Agent de code indépendant

- **Situation** : un agent ne reconnaît pas `agents/openai.yaml`.
- **Résultat attendu** : il charge le dossier maître et applique toutes les règles via son mécanisme disponible.
- **Comportement interdit** : considérer le skill comme réservé à Codex.

## Nouvelle session

- **Situation** : des garde-fous existent déjà mais le skill a évolué.
- **Résultat attendu** : le [prompt obligatoire](../installation/installation.md) compare versions, couverture et preuves avant de modifier.
- **Comportement interdit** : recréer aveuglément ou commencer sans lecture.
