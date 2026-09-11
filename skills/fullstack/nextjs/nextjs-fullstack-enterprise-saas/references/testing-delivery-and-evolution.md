# Tests, livraison et évolution

Lire ce document pour définir les preuves, créer une capacité, corriger une régression, modifier un contrat ou des données, auditer et livrer.

## Principe

La couverture suit le risque et les frontières. Un test prouve un comportement observable, une règle métier ou une protection ; il ne reproduit pas mécaniquement l’implémentation.

Une compilation réussie ne prouve ni l’autorisation, ni la cohérence des données, ni la compatibilité d’un contrat, ni le déploiement réel.

## Contrôles statiques

- format et règles de code ;
- TypeScript strict ;
- importations interdites entre couches ;
- importation serveur dans le code navigateur ;
- dépendances circulaires ;
- schémas et contrats ;
- migrations ordonnées ;
- secrets et fichiers sensibles ;
- configuration.

Automatiser les invariants structurels importants au lieu de dépendre seulement d’une convention écrite.

## Tests unitaires

Tester sans infrastructure :

- règles du domaine ;
- valeurs métier ;
- politiques ;
- validation ;
- mapping ;
- calcul de clé de cache ;
- classification d’erreur ;
- décisions de répétition.

Un test unitaire ne doit pas nécessiter de démarrer Next.js ou une base si la règle est correctement isolée.

## Tests d’intégration

Tester avec les adaptateurs réels ou une infrastructure représentative :

- accès aux données et contraintes ;
- transaction ;
- migration ;
- gestionnaire de route et cas d’usage ;
- traitement serveur et autorisation ;
- cache ;
- file de travail ;
- adaptateur fournisseur simulé au niveau réseau.

Ne pas remplacer toutes les intégrations par des fonctions factices au point de ne jamais vérifier la sérialisation, les contraintes ou les statuts.

## Tests de contrat

Pour une interface publique :

- valider la description OpenAPI lorsqu’elle existe ;
- vérifier demandes et réponses ;
- tester champs obligatoires et facultatifs ;
- tester erreurs et statuts ;
- vérifier compatibilité avec les consommateurs ;
- détecter une rupture non annoncée.

Pour un événement : type, version, schéma, répétition et tolérance aux champs supplémentaires.

## Tests de composants

Tester les composants navigateur avec des interactions proches de l’utilisateur :

- clavier ;
- focus ;
- saisie ;
- erreur ;
- chargement ;
- soumission répétée ;
- réponse concurrente ;
- résultat.

Les composants serveur asynchrones peuvent nécessiter un test d’intégration ou de bout en bout selon le support de l’outil.

## Tests de bout en bout

Exécuter une construction proche de la production et couvrir :

- navigation directe et côté client ;
- connexion et session expirée ;
- permissions ;
- changement d’organisation ;
- parcours métier critique ;
- données réellement persistées ;
- erreurs et récupération ;
- page publique et métadonnées ;
- petit écran, zoom et clavier.

Vérifier le résultat côté serveur, pas seulement le message affiché.

## Tests de données

- contrainte de présence et unicité ;
- relation invalide ;
- deux écritures concurrentes ;
- transaction annulée ;
- isolation entre organisations ;
- requête avec volume représentatif ;
- migration ascendante ;
- coexistence de versions ;
- transfert interrompu et repris ;
- restauration de sauvegarde.

Les données de test doivent être déterministes, isolées et sans information personnelle réelle.

## Tests de sécurité

- appel direct sans interface ;
- entrée mal formée et trop grande ;
- injection ;
- identité absente ou falsifiée ;
- permission insuffisante ;
- ressource d’une autre organisation ;
- propriété sensible ;
- requête forgée ;
- origine interdite ;
- répétition ;
- webhook invalide ;
- adresse serveur vers réseau interne ;
- fichier dangereux ;
- secret dans le code navigateur, réponse ou journal.

Les contrôles automatisés complètent une revue de menace ; ils ne la remplacent pas.

## Tests de tâches et intégrations

- tâche reçue deux fois ;
- travailleur interrompu ;
- erreur temporaire puis réussite ;
- erreur permanente ;
- ordre différent ;
- fournisseur lent ;
- délai dépassé ;
- réponse mal formée ;
- limite fournisseur ;
- compensation ;
- rapprochement d’une opération critique.

## Tests de performance et capacité

Définir des objectifs avant le test. Mesurer :

- latence par route et cas d’usage ;
- débit ;
- erreurs ;
- connexions ;
- mémoire ;
- requêtes de données ;
- attente des tâches ;
- code navigateur.

Tester montée progressive, pointe réaliste et récupération. Un test qui surcharge un service partagé sans autorisation est interdit.

## Matrice minimale

| Changement | Preuves minimales |
|---|---|
| Règle métier | Test unitaire et cas limites |
| Cas d’usage | Test d’application avec autorisation et résultat |
| Accès aux données | Test d’intégration, contraintes et organisation |
| Route HTTP | Contrat, validation, sécurité, statuts et limites |
| Traitement serveur | Appel direct, permission, répétition et invalidation |
| Migration | Version déployée, données représentatives, coexistence et retour |
| Tâche durable | Répétition, interruption, tentatives et échec définitif |
| Intégration | Réponse réelle simulée au réseau, délai et erreur |
| Composant navigateur | Interaction, clavier et états |
| Page publique | Document initial, métadonnées, marque et langue |
| Cache | froid, chaud, isolation, invalidation et plusieurs instances |
| Déploiement | construction, santé, parcours critique et retour |

## Processus d’intégration continue

Ordre recommandé à adapter :

1. installation reproductible ;
2. validation des fichiers générés et de configuration ;
3. format, TypeScript et dépendances ;
4. tests unitaires ;
5. tests d’intégration avec données isolées ;
6. validation des contrats et migrations ;
7. construction de production ;
8. tests de bout en bout ;
9. contrôles de sécurité et dépendances ;
10. publication d’un artefact immuable ;
11. migration compatible ;
12. déploiement progressif et contrôle après publication.

Le processus échoue clairement lorsqu’un contrôle obligatoire échoue. Ne pas convertir un échec en avertissement pour terminer une livraison.

## Évolution d’un contrat

Avant une modification :

- inventorier les consommateurs ;
- classer compatible ou incompatible ;
- ajouter des tests de compatibilité ;
- publier la nouvelle forme ;
- mesurer l’usage de l’ancienne ;
- communiquer la migration ;
- retirer seulement après la période annoncée.

Une interface interne entre modules mérite aussi une transition lorsqu’elle possède plusieurs consommateurs.

## Évolution d’une architecture

Une refonte doit préciser :

- problème mesuré ;
- limites de l’existant ;
- options ;
- décision ;
- étapes réversibles ;
- compatibilité ;
- preuves ;
- conditions d’arrêt ;
- suppression de l’ancien chemin.

Éviter une architecture parallèle permanente. Une transition a un propriétaire et une date de réévaluation.

## Définition de terminé

Le travail est terminé uniquement si :

- critères fonctionnels satisfaits ;
- noms et responsabilités compréhensibles ;
- frontières et dépendances respectées ;
- permissions et isolation prouvées ;
- données et transactions cohérentes ;
- contrat compatible ou migration fournie ;
- cache, tâches et intégrations contrôlés ;
- erreurs et résultats visibles ;
- accessibilité vérifiée ;
- performance mesurée lorsque touchée ;
- observabilité suffisante ;
- TypeScript, tests et construction réussis ;
- migration et déploiement vérifiés ;
- documentation mise à jour ;
- contrôles non exécutés déclarés.

## Audit par sévérité

### Bloquant critique

- fuite de secret ou de données entre organisations ;
- route ou traitement sensible sans autorisation ;
- corruption ou perte de données ;
- migration destructive non récupérable ;
- cache public contenant une réponse privée ;
- construction ou démarrage impossible.

### Majeur

- permission uniquement dans l’interface ;
- contrat public cassé ;
- transaction incohérente ;
- tâche critique non durable ;
- webhook non vérifié ;
- absence de coordination multi-instance ;
- parcours essentiel inaccessible.

### Important

- route contenant trop de métier ;
- nom ou dossier ambigu ;
- test significatif absent ;
- requête non bornée ;
- erreur difficile à diagnostiquer ;
- dépendance client lourde non mesurée.

### Amélioration

- harmonisation non bloquante ;
- documentation complémentaire ;
- optimisation démontrée mais non urgente.

## Compte rendu

Indiquer :

- révision testée ;
- environnement ;
- commandes et parcours ;
- résultats ;
- données ou contrats modifiés ;
- contrôles non exécutés ;
- risques ;
- prochaine action.

Ne jamais présenter une intuition, une lecture de code ou une commande non exécutée comme une preuve d’exécution.

## Sources officielles

- [Tests dans Next.js](https://nextjs.org/docs/app/guides/testing)
- [Liste de contrôle de production Next.js](https://nextjs.org/docs/app/guides/production-checklist)
- [Déploiement vers différentes plateformes](https://nextjs.org/docs/app/guides/deploying-to-platforms)
