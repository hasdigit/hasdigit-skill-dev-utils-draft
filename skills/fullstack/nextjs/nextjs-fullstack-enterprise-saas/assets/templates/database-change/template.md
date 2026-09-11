# Modèle de changement de données

## Contexte

- Module propriétaire :
- Besoin métier :
- Structure actuelle :
- Structure cible :
- Volumes concernés :
- Environnements concernés :

## Invariants

- Données à préserver :
- Contraintes actuelles :
- Nouvelles contraintes :
- Isolation des organisations :
- Conservation et suppression :

## Compatibilité

- Version applicative actuellement déployée :
- Ancien code avec nouveau schéma :
- Nouveau code avec ancien schéma :
- Coexistence pendant le déploiement :
- Consommateurs externes :

## Étapes

1. Extension compatible :
2. Écriture transitoire :
3. Transfert par lots :
4. Vérification :
5. Bascule de lecture :
6. Observation :
7. Retrait ultérieur :

## Transfert

- Taille des lots :
- Point de reprise :
- Répétition sûre :
- Limite de charge :
- Mesures de progression :
- Contrôle des totaux :

## Concurrence et disponibilité

- Verrous :
- Durée attendue :
- Effet sur les écritures :
- Effet sur les lectures :
- Arrêt sans danger :

## Sauvegarde et retour

- Sauvegarde vérifiée :
- Test de restauration :
- Signal d’arrêt :
- Retour du code :
- Migration corrective :
- Perte maximale acceptable :
- Temps de reprise attendu :

## Observabilité

- Journaux :
- Mesures :
- Alertes :
- Propriétaire pendant l’exécution :

## Preuves

- Test depuis le schéma déployé :
- Données représentatives :
- Deux versions simultanées :
- Interruption et reprise :
- Contraintes et transaction :
- Performance :
- Restauration :

## Autorisation

- Personne ou rôle autorisant l’exécution :
- Fenêtre prévue :
- Décision finale :
