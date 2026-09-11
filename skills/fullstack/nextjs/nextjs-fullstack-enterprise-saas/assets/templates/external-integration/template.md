# Modèle d’intégration externe

## Identité

- Fournisseur ou système :
- Finalité métier :
- Module propriétaire :
- Environnements :
- Données échangées :
- Niveau de sensibilité :

## Frontière

- Contrat métier interne :
- Adaptateur fournisseur :
- Types externes isolés :
- Conversion des entrées :
- Conversion des résultats :
- Erreurs normalisées :

## Authentification et secrets

- Identité utilisée :
- Portée minimale :
- Stockage du secret :
- Rotation :
- Révocation :
- Responsabilité :

## Appels sortants

- Adresses autorisées :
- Délai maximum :
- Limite de concurrence :
- Opérations répétables :
- Nouvelle tentative :
- Coupe-circuit :
- Limites du fournisseur :

## Événements entrants

- Adresse du webhook :
- Signature :
- Tolérance d’horodatage :
- Identifiant unique :
- Réponse rapide :
- Tâche durable :
- Gestion des doublons et du désordre :

## Cohérence

- Transaction locale :
- Intention durable :
- États intermédiaires :
- Rapprochement :
- Compensation :
- Source de vérité :

## Sécurité et conformité

- Données minimisées :
- Consentement :
- Conservation :
- Région :
- Journaux expurgés :
- Suppression chez le fournisseur :

## Observabilité

- Nom des opérations :
- Identifiant de corrélation :
- Mesures :
- Alertes :
- Tableau de suivi :

## Preuves

- Succès :
- Délai dépassé :
- Indisponibilité :
- Réponse mal formée :
- Répétition :
- Webhook invalide et répété :
- Interruption et reprise :
- Environnement de test :

## Retrait

- Données à récupérer :
- Contrats à remplacer :
- Secrets à révoquer :
- Tâches et webhooks à arrêter :
- Date et propriétaire :
