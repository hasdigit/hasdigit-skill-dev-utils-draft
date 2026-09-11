# Cache, tâches différées et intégrations

Lire ce document pour toute mise en cache, invalidation, tâche planifiée, traitement différé, événement, webhook ou service externe.

## Cache fondé sur la version réelle

Le comportement du cache Next.js évolue selon la version et la configuration. Inspecter :

- version installée ;
- activation des composants de cache ;
- directives utilisées ;
- gestionnaires de cache personnalisés ;
- environnement à une ou plusieurs instances ;
- réseau de diffusion ou serveur mandataire ;
- mécanismes d’invalidation disponibles.

Ne pas appliquer une règle mémorisée sans vérifier la documentation correspondant au projet.

## Classifier la donnée

Avant la mise en cache, classer :

- publique et identique pour tous ;
- publique mais variable par langue ou marque ;
- propre à une organisation ;
- propre à un utilisateur ;
- dépendante d’une permission ;
- sensible ou trop volatile pour être partagée.

Documenter : clé, portée, fraîcheur, invalidation, propriétaire, comportement en cas d’échec et coordination entre instances.

## Clé d’isolation

La clé inclut toutes les dimensions qui changent le résultat :

- route ou cas d’usage ;
- paramètres ;
- langue ;
- marque ;
- organisation vérifiée ;
- utilisateur ou permission si nécessaire ;
- version du contrat ou de la politique.

Ne pas construire une clé d’organisation depuis une valeur navigateur non autorisée.

Une réponse privée ne doit pas entrer dans un cache public, même si son adresse ne contient pas d’information personnelle.

## Fraîcheur

Définir le délai acceptable entre la réalité métier et la valeur servie. Une durée arbitraire n’est pas une stratégie.

Choisir entre :

- lecture dynamique ;
- cache pendant une même requête ;
- cache partagé avec durée ;
- revalidation après durée ;
- invalidation immédiate après modification ;
- actualisation en arrière-plan.

Une permission ou un solde critique peut exiger une lecture plus fraîche qu’un catalogue public.

## Invalidation

Après une modification :

1. confirmer la réussite de la transaction ;
2. identifier les vues réellement affectées ;
3. invalider par une clé, une étiquette ou un chemin précis compatible avec la version ;
4. vérifier la lecture suivante ;
5. confirmer l’absence d’effet sur les autres organisations ;
6. observer les échecs d’invalidation.

Éviter une invalidation générale lorsqu’une invalidation ciblée est fiable. Ne pas invalider avant la confirmation d’une transaction.

## Plusieurs instances

Un cache local n’est pas automatiquement partagé. Pour plusieurs instances :

- utiliser un stockage partagé ou coordonner les invalidations ;
- synchroniser les étiquettes selon le mécanisme du framework ;
- vérifier les caches du réseau de diffusion ;
- tester une modification sur une instance et la lecture sur une autre ;
- définir le comportement lors d’une perte du stockage partagé.

Une réponse dynamique marquée privée ne doit pas être rendue publique par une configuration externe.

## Travail après réponse

La fonction `after` de Next.js exécute un travail après la production d’une réponse dans les limites de durée et de plateforme. Elle convient à un effet court et non critique tel qu’une mesure ou un journal.

Elle ne garantit pas à elle seule :

- livraison durable ;
- survie à une interruption brutale ;
- nombre illimité de tentatives ;
- traitement long ;
- exécution unique ;
- orchestration complexe.

Ne pas l’utiliser pour une opération financière, un courriel obligatoire, une conversion longue ou une synchronisation indispensable sans mécanisme durable complémentaire.

## Tâche durable

Une tâche qui doit survivre à une requête utilise une file ou un stockage durable avec :

- identifiant unique ;
- type et version ;
- état ;
- organisation ;
- données minimales ;
- instant de création ;
- nombre de tentatives ;
- prochaine exécution ;
- délai maximum ;
- résultat ou erreur expurgée.

Le producteur enregistre la tâche sans risque de perte. Le travailleur réclame, renouvelle ou libère le travail selon le mécanisme choisi.

## États d’une tâche

Utiliser des états compréhensibles :

- en attente ;
- en cours ;
- réussie ;
- échouée temporairement ;
- échouée définitivement ;
- annulée.

Définir les transitions autorisées. Une tâche bloquée en cours doit pouvoir être détectée et reprise sans produire un double effet dangereux.

## Répétition et tentatives

Un travailleur traite toujours la possibilité d’un doublon. Utiliser :

- identifiant de répétition ;
- contrainte d’unicité ;
- vérification d’état ;
- écriture atomique ;
- opération fournisseur répétable ;
- enregistrement du résultat.

Relancer uniquement les erreurs temporaires. Limiter les tentatives, augmenter le délai et ajouter une variation pour éviter que toutes les tâches recommencent ensemble.

Une erreur permanente va dans un état inspectable avec procédure de correction et de relance autorisée.

## Tâches planifiées

Une tâche planifiée doit définir :

- fuseau horaire ;
- comportement après une exécution manquée ;
- verrouillage entre instances ;
- durée maximale ;
- répétition sûre ;
- surveillance ;
- propriétaire opérationnel.

Ne pas supposer qu’une expression de calendrier ne s’exécute qu’une fois dans une infrastructure distribuée.

## Événements métier

Un événement décrit un fait accompli et contient :

- nom complet ;
- version ;
- identifiant ;
- date ;
- organisation ;
- origine ;
- données minimales ;
- identifiant de corrélation.

Les consommateurs tolèrent les doublons et les champs supplémentaires compatibles. Ne pas exposer une structure de table interne comme contrat d’événement.

## Adaptateur d’intégration

Chaque fournisseur est derrière un adaptateur qui convertit le contrat métier vers son format.

L’adaptateur définit :

- authentification ;
- adresses autorisées ;
- délai maximum ;
- limite de concurrence ;
- politique de nouvelle tentative ;
- répétition ;
- mapping des erreurs ;
- journalisation expurgée ;
- mesures ;
- comportement en environnement de test.

Le domaine ne doit pas connaître les types du fournisseur.

## Résilience d’un appel externe

- Délai maximum obligatoire.
- Nouvelle tentative seulement pour une opération sûre et une erreur temporaire.
- Limite du nombre de tentatives.
- Coupe-circuit lorsque les échecs répétés menacent le système.
- Limite de concurrence pour protéger ressources locales et fournisseur.
- Solution de repli seulement si elle reste correcte pour l’utilisateur.

Ne pas masquer une indisponibilité par une fausse réussite.

## Paiement et opérations critiques

- Utiliser les identifiants de répétition du fournisseur.
- Enregistrer l’intention avant l’appel lorsque nécessaire.
- Ne jamais se fier uniquement à la redirection navigateur pour confirmer un paiement.
- Vérifier le webhook signé et rapprocher l’état.
- Conserver les montants, devises et identifiants sans ambiguïté.
- Prévoir les états intermédiaires et compensations.

## Courriels et notifications

Une notification obligatoire devient une tâche durable. Définir modèle, langue, destinataire, organisation, consentement, répétition et état d’envoi.

Ne pas inclure de secret dans un lien. Utiliser un jeton temporaire, à portée limitée et usage unique lorsque nécessaire.

## Stockage de fichiers

L’adaptateur de stockage doit définir :

- chemin logique ou clé ;
- propriétaire d’organisation ;
- type et taille ;
- chiffrement ;
- durée ;
- adresse temporaire ;
- suppression ;
- analyse ;
- comportement de remplacement.

Ne pas dépendre du disque local d’une instance lorsque le déploiement est éphémère ou multiple.

## Contrôles obligatoires

- cache froid, chaud, expiré et invalidé ;
- deux utilisateurs et deux organisations ;
- modification sur une instance et lecture sur une autre ;
- perte du cache partagé ;
- interruption pendant un travail après réponse ;
- tâche reçue deux fois ;
- travailleur interrompu puis repris ;
- erreur temporaire et permanente ;
- tâche planifiée sur deux instances ;
- fournisseur lent, indisponible et réponse invalide ;
- webhook répété et dans le désordre ;
- opération critique rapprochée avec le fournisseur ;
- fichier absent ou stockage indisponible.

## Sources officielles

- [Revalidation avec les composants de cache Next.js](https://nextjs.org/docs/app/getting-started/revalidating)
- [Modèle de cache antérieur de Next.js](https://nextjs.org/docs/app/guides/caching-without-cache-components)
- [Fonction `after` de Next.js](https://nextjs.org/docs/app/api-reference/functions/after)
- [Auto-hébergement et coordination du cache](https://nextjs.org/docs/app/guides/self-hosting)
