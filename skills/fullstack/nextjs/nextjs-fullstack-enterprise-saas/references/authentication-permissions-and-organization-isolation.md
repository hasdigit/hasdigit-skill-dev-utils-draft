# Authentification, permissions et isolation des organisations

Lire ce document pour toute session, connexion, invitation, changement d’organisation, route privée, traitement serveur, donnée sensible ou identité de service.

## Concepts distincts

- **Authentification** : prouver l’identité.
- **Session** : conserver de manière sûre l’état de connexion.
- **Autorisation** : décider ce que l’identité peut faire.
- **Permission** : capacité métier explicite.
- **Rôle** : groupe administrable de permissions.
- **Politique** : décision utilisant permission, ressource et contexte.
- **Organisation cliente** : périmètre isolé des données et droits d’un client.

Ne jamais réduire ces responsabilités au nom général `auth`.

## Bibliothèque maintenue

Pour une authentification réelle, préférer une bibliothèque ou un fournisseur maintenu qui correspond aux exigences : sessions, renouvellement, révocation, connexion externe, authentification renforcée et récupération.

Une implémentation personnalisée doit être justifiée par une contrainte forte, révisée comme un composant de sécurité et testée au-delà du parcours nominal.

## Session

Une session doit définir :

- mode de stockage ;
- durée inactive et durée maximale ;
- renouvellement ;
- révocation ;
- rotation après changement sensible ;
- comportement sur plusieurs appareils ;
- réaction à un changement de rôle ou d’organisation ;
- attributs de cookie lorsque le navigateur est concerné.

Ne pas stocker dans le navigateur une autorité que le serveur ne revérifie pas. Un jeton signé peut devenir obsolète après une révocation ou un changement de droit ; définir la stratégie de fraîcheur.

## Résoudre le contexte serveur

À chaque opération sensible :

1. vérifier la session ;
2. résoudre l’utilisateur ;
3. résoudre l’organisation active depuis une association fiable ;
4. charger les appartenances et politiques nécessaires ;
5. vérifier la permission ;
6. vérifier la ressource dans le même périmètre ;
7. retourner uniquement les données autorisées.

Ne pas accepter l’organisation active uniquement depuis un champ de formulaire, un paramètre de route ou un en-tête contrôlé par le navigateur.

## Permissions métier

Nommer une permission selon la capacité :

```text
billing.invoice.read
billing.invoice.create
billing.invoice.payment.record
billing.invoice.cancel
```

La page, le bouton, le traitement serveur et la route HTTP appliquent la même identité métier lorsqu’ils représentent la même action. Ne pas inventer une permission par surface technique.

Un rôle regroupe les permissions ; le code demande la permission nécessaire au lieu de répéter des comparaisons de noms de rôle dans tout le produit.

## Politiques contextuelles

La permission seule peut être insuffisante. Une politique peut vérifier :

- organisation propriétaire ;
- auteur ou responsable ;
- état de la ressource ;
- limite de plan ;
- séparation des responsabilités ;
- heure ou zone autorisée ;
- consentement ;
- relation avec une autre ressource.

La décision doit être centralisée, testable et nommée dans le vocabulaire métier.

## Couche d’accès aux données

La fonction qui lit une donnée sensible applique une autorisation sécurisée ou exige un contexte déjà vérifié avec un contrat impossible à fabriquer depuis le navigateur.

Elle doit :

- fonctionner uniquement sur le serveur ;
- filtrer par organisation ;
- limiter les champs ;
- distinguer ressource absente et refus selon la politique de confidentialité ;
- éviter une mise en cache globale d’une décision personnalisée.

Un composant serveur peut adapter l’interface après un contrôle, mais la couche de données protège toujours la ressource.

## Traitements serveur

Chaque traitement serveur est un point d’entrée réseau. Il vérifie à nouveau session, permission, organisation, ressource et état métier.

Une fermeture sur un identifiant, une propriété cachée de formulaire ou l’absence de bouton visible ne constitue pas une protection.

## Routes HTTP

Chaque méthode d’un gestionnaire de route possède sa propre politique. Une lecture et une modification peuvent exiger des permissions différentes.

Distinguer :

- session utilisateur ;
- jeton d’application ;
- clé de service ;
- signature de webhook ;
- lien temporaire à portée limitée.

Ne pas réutiliser une clé générale pour toutes les intégrations.

## Interception de requête et mises en page

Le fichier d’interception peut rediriger rapidement. Une mise en page peut adapter la navigation. Aucun des deux ne remplace les contrôles au niveau des cas d’usage et données.

Next.js possède plusieurs points d’entrée et des rendus imbriqués. Une protection placée uniquement sur une mise en page peut laisser accessible un traitement serveur ou une route.

## Changement d’organisation

Lorsqu’un utilisateur appartient à plusieurs organisations :

- vérifier l’appartenance au moment du changement ;
- invalider ou séparer les caches personnalisés ;
- vider les sélections incompatibles ;
- interrompre les demandes en cours devenues anciennes ;
- mettre à jour les journaux et événements ;
- ne pas conserver une donnée de l’organisation précédente à l’écran.

Tester deux changements rapides et un onglet navigateur ancien.

## Invitations et adhésions

Une invitation doit avoir :

- organisation cible ;
- rôle ou permissions proposés ;
- destinataire ;
- expiration ;
- usage unique ;
- révocation ;
- validation de l’adresse ou de l’identité ;
- journal d’acceptation.

Une invitation ne doit pas permettre de choisir une autre organisation ou d’élever son rôle lors de l’acceptation.

## Identités de service

Une machine possède une identité distincte d’un utilisateur. Définir :

- propriétaire ;
- portée ;
- permissions minimales ;
- environnements ;
- expiration et rotation ;
- révocation ;
- traçabilité ;
- limite de débit.

Ne pas utiliser un compte administrateur humain partagé par une intégration.

## Administration et élévation

Les actions administratives sensibles doivent exiger selon le risque :

- authentification récente ;
- facteur supplémentaire ;
- justification ;
- approbation distincte ;
- journal immuable ;
- notification ;
- durée d’élévation limitée.

Un mode de support ne doit pas contourner silencieusement l’isolation des organisations.

## Cache des décisions

Une décision peut être mise en cache seulement si la clé inclut toutes les dimensions : utilisateur, organisation, politique, ressource ou version de rôle.

Définir durée et invalidation après :

- révocation de session ;
- changement de rôle ;
- retrait d’une organisation ;
- modification de politique ;
- changement d’état de ressource.

En cas de doute ou d’indisponibilité du cache, refuser de manière sûre pour une opération sensible.

## Messages de refus

Distinguer pour l’utilisateur :

- connexion nécessaire ;
- session expirée ;
- permission insuffisante ;
- fonctionnalité non incluse ;
- ressource absente ;
- vérification temporairement impossible.

Ne pas révéler l’existence ou les propriétés d’une ressource d’une autre organisation.

## Contrôles obligatoires

- session valide, absente, expirée et révoquée ;
- permission présente et absente ;
- rôle changé pendant une session ;
- ressource inexistante ;
- ressource d’une autre organisation ;
- identifiant falsifié ;
- appel direct du traitement serveur ;
- appel direct de chaque méthode de route ;
- organisation modifiée dans le navigateur ;
- changement rapide entre deux organisations ;
- invitation expirée, réutilisée ou modifiée ;
- identité de service hors de sa portée ;
- cache de permission invalidé ;
- action administrative tracée.

## Sources officielles

- [Authentification et autorisation dans Next.js](https://nextjs.org/docs/app/guides/authentication)
- [Sécurité de la directive serveur](https://nextjs.org/docs/app/api-reference/directives/use-server)
- [Risques de sécurité des interfaces de programmation](https://owasp.org/API-Security/)
