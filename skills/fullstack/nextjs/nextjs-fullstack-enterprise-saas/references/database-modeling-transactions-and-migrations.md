# Données, transactions et migrations

Lire ce document avant de créer ou modifier une table, collection, contrainte, index, requête, transaction, migration, sauvegarde ou politique de conservation.

## Partir du métier

Le modèle de données protège des faits métier, pas seulement des formes d’écran. Avant de créer une structure, identifier :

- l’objet métier ;
- son propriétaire ;
- son organisation cliente ;
- son cycle de vie ;
- ses invariants ;
- ses relations ;
- les volumes et accès attendus ;
- les obligations de conservation et suppression ;
- les événements qui expliquent son évolution.

Ne pas créer une table par composant ni stocker toute évolution dans un champ général pour éviter de modéliser le domaine.

## Propriété des données

Chaque table ou collection appartient à un module. Seul ce module modifie directement ses données privées.

Un autre module utilise l’interface publique, une vue de lecture ou un événement. Une clé étrangère n’accorde pas automatiquement le droit de modifier la table cible.

Documenter toute donnée partagée : propriétaire, lecteurs autorisés, rythme de mise à jour et procédure d’évolution.

## Identité

Distinguer :

- identifiant interne de persistance ;
- identifiant public exposable ;
- identifiant d’un fournisseur ;
- clé métier ;
- identifiant de l’organisation cliente.

Ne pas permettre au consommateur de choisir une clé interne sensible. Un identifiant difficile à deviner ne remplace aucune autorisation.

## Contraintes

Protéger dans la base les invariants qu’elle peut garantir de manière fiable :

- présence obligatoire ;
- unicité ;
- relation valide ;
- plage de valeurs ;
- état autorisé ;
- absence de doublon ;
- appartenance d’organisation lorsque le moteur le permet.

Une validation applicative améliore le message utilisateur. La contrainte protège contre les écritures concurrentes et les autres chemins d’accès.

Pour un produit multi-organisation, vérifier si une unicité est globale ou limitée à l’organisation. Une contrainte mal définie peut empêcher deux clients d’utiliser la même référence ou autoriser un doublon dangereux dans un même client.

## Valeurs monétaires, temps et précision

- Représenter l’argent avec une unité et une précision explicites.
- Ne pas utiliser un nombre flottant imprécis pour une valeur financière.
- Stocker l’instant avec une convention de fuseau horaire maîtrisée.
- Conserver séparément le fuseau métier lorsque l’affichage ou une échéance en dépend.
- Définir les règles d’arrondi dans le domaine.
- Ne pas confondre date civile, instant précis et durée.

## Accès aux données

Un accès aux données doit :

- recevoir une organisation vérifiée lorsque le périmètre l’exige ;
- utiliser des requêtes paramétrées ;
- sélectionner uniquement les colonnes nécessaires ;
- retourner un objet limité ;
- distinguer absence, conflit et panne ;
- ne pas exposer les détails du client de données au domaine ;
- être observable sans journaliser les valeurs sensibles.

Éviter un dépôt général capable de lire n’importe quelle table. Préférer une interface liée à une intention du module.

## Requêtes et index

Concevoir un index à partir d’une requête et d’un volume mesurés. Vérifier :

- colonnes de filtre ;
- ordre et tri ;
- organisation cliente ;
- sélectivité ;
- coût d’écriture ;
- espace ;
- plan d’exécution ;
- comportement avec les volumes de production.

Détecter les lectures répétées par élément d’une liste. Grouper ou joindre lorsque cela réduit réellement le coût sans produire une réponse surdimensionnée.

Toute collection possède une limite. Une exportation complète doit utiliser un parcours spécifique, contrôlé et observable.

## Frontière de transaction

Une transaction regroupe les modifications qui doivent réussir ou échouer ensemble selon le métier.

Le cas d’usage définit cette unité. L’adaptateur de données fournit le mécanisme. Éviter une transaction globale couvrant des opérations indépendantes.

Dans une transaction :

- lire les données nécessaires avec le niveau de verrouillage adapté ;
- vérifier les invariants ;
- écrire les changements ;
- enregistrer les événements durables nécessaires ;
- confirmer ou annuler ensemble.

Ne pas effectuer un appel réseau lent pendant une transaction ouverte, sauf contrainte démontrée et délai strict.

## Concurrence

Prévoir deux demandes valides visant la même donnée.

Solutions possibles selon le besoin :

- contrainte d’unicité ;
- verrouillage optimiste avec numéro de version ;
- verrouillage de ligne ;
- niveau d’isolation plus strict ;
- opération atomique ;
- identifiant de répétition ;
- sérialisation par file de travail.

Une lecture suivie d’une écriture sans protection peut perdre une modification. Tester explicitement les appels simultanés pour les opérations critiques.

## Événements durables

Lorsqu’une modification locale doit provoquer un appel externe, enregistrer l’intention durablement dans la même transaction que la donnée métier lorsque le risque de perte est inacceptable.

Un travailleur envoie ensuite l’événement avec :

- identifiant unique ;
- type et version ;
- organisation ;
- date ;
- données minimales ;
- nombre de tentatives ;
- prochaine tentative ;
- résultat ou erreur expurgée.

Le consommateur doit supporter les doublons.

## Migration de schéma

Chaque migration doit être :

- versionnée ;
- déterministe ;
- révisée ;
- testée sur une copie représentative ;
- compatible avec le déploiement prévu ;
- observable ;
- accompagnée d’une stratégie de retour ou de correction.

Ne pas modifier une migration déjà exécutée en production. Ajouter une nouvelle migration corrective.

## Évolution sans interruption

Pour une modification incompatible, utiliser une progression :

1. **étendre** : ajouter une nouvelle structure compatible ;
2. **déployer** : écrire dans l’ancienne et la nouvelle forme si nécessaire ;
3. **transférer** : remplir les anciennes données par lots reprenables ;
4. **vérifier** : comparer les comptes et invariants ;
5. **basculer** : lire la nouvelle forme ;
6. **observer** : confirmer l’absence de régression ;
7. **retirer** : supprimer l’ancienne forme dans une livraison ultérieure.

Une seule migration qui renomme, transforme et supprime peut rendre impossible un retour rapide.

## Transfert massif de données

Un transfert doit être :

- découpé en lots ;
- reprenable ;
- répétable sans corruption ;
- limité en charge ;
- mesuré ;
- vérifié par totaux et échantillons ;
- capable de s’arrêter proprement.

Ne pas verrouiller une grande table pendant une durée inconnue sans analyse du moteur et essai réaliste.

## Retour et récupération

Un retour peut signifier :

- revenir au code précédent ;
- désactiver une lecture nouvelle ;
- appliquer une migration corrective ;
- restaurer une sauvegarde ;
- rejouer des événements.

Une migration destructive n’est pas annulée automatiquement par un retour de code. Tester les sauvegardes et la restauration, pas uniquement leur création.

Définir les objectifs de perte maximale de données et de temps de reprise lorsque le produit l’exige.

## Suppression et conservation

Définir :

- suppression logique ou physique ;
- durée de conservation ;
- obligations légales et contractuelles ;
- anonymisation ;
- propagation aux sauvegardes et fournisseurs ;
- effet sur les journaux et événements ;
- droit de restauration.

Une suppression logique ne protège pas une donnée et ne satisfait pas automatiquement une demande d’effacement.

## Données de test et remplissage initial

- Ne jamais utiliser des données personnelles de production sans procédure autorisée d’anonymisation.
- Séparer le remplissage nécessaire au produit des exemples de développement.
- Rendre les scripts répétables et liés à un environnement explicite.
- Interdire une exécution destructive implicite en production.

## Contrôles obligatoires

- contraintes sur présence, unicité et relations ;
- deux organisations utilisant des références similaires ;
- deux écritures concurrentes ;
- transaction réussie et annulée ;
- erreur d’intégration après écriture locale ;
- migration depuis la version réellement déployée ;
- coexistence de deux versions applicatives ;
- transfert interrompu puis repris ;
- volume et plan de requête représentatifs ;
- sauvegarde restaurée ;
- suppression et conservation ;
- absence de donnée réelle dans les jeux de test.

## Références à adapter au moteur choisi

- [Isolation des transactions PostgreSQL](https://www.postgresql.org/docs/current/transaction-iso.html)
- Consulter également la documentation officielle du moteur, du client de données et de l’outil de migration réellement installés.
