# Rendu frontend, accessibilité et pages publiques

Lire ce document pour toute page, composant, navigation, mise en page, thème, langue, métadonnée ou donnée traversant la frontière serveur et navigateur.

## Projet et version

Identifier :

- App Router, Pages Router ou coexistence ;
- version de Next.js et de React ;
- comportement de cache configuré ;
- fichiers spéciaux utilisés ;
- système de design ;
- langues et marques ;
- routes publiques et privées ;
- exigences d’indexation.

Ne pas migrer un Pages Router ou activer une fonction expérimentale sans besoin, compatibilité et plan de retour.

## Composants serveur par défaut

Utiliser un composant serveur lorsqu’il :

- charge une donnée ;
- applique une lecture autorisée ;
- accède à une configuration privée ;
- compose un contenu sans interaction navigateur ;
- réduit le code envoyé au navigateur.

Appeler directement le cas d’usage ou la lecture serveur. Ne pas ajouter un aller-retour vers une route interne.

## Composants navigateur limités

Utiliser `use client` seulement pour :

- événements interactifs ;
- état local ;
- effets de cycle de vie ;
- fonction du navigateur ;
- bibliothèque exigeant le navigateur.

La directive crée une frontière. Tout module importé dessous peut entrer dans le code livré. Vérifier dépendances, poids, secrets et données.

Transmettre des objets sérialisables et minimisés. Ne pas transmettre une entité complète ou un résultat contenant des colonnes inutiles.

## Fichiers spéciaux

- `page.tsx` compose une page.
- `layout.tsx` compose une mise en page persistante.
- `loading.tsx` fournit un chargement de segment.
- `error.tsx` traite une défaillance du segment.
- `not-found.tsx` représente une absence contrôlée.
- `route.ts` expose une frontière réseau et ne peut pas partager le même segment qu’une page.

Garder ces fichiers minces et rattachés à des capacités de module nommées.

## Navigation et état dans l’adresse

Placer dans l’adresse les états partageables et rechargeables : recherche, filtre, tri, page et onglet métier.

Valider les paramètres. Ne jamais y placer un secret, un jeton, une donnée personnelle inutile ou un état éphémère.

Tester navigation directe, navigation côté client, retour, avance, rechargement et adresse invalide.

Une mise en page ne constitue pas l’unique protection d’une route ou donnée.

## Autorité de chaque état

Choisir une seule autorité :

- le serveur pour une donnée persistée, partagée ou autorisée ;
- l’adresse pour un filtre, tri, page, recherche ou onglet devant être partagé et rechargé ;
- le composant navigateur pour une interaction locale temporaire ;
- un contexte navigateur pour une information réellement partagée entre plusieurs zones interactives ;
- la configuration pour une valeur d’environnement ou de produit.

Ne pas copier indépendamment une même donnée dans le serveur, l’adresse et plusieurs stockages navigateur. Une copie dérivée doit définir sa synchronisation, sa fraîcheur et sa remise à zéro après un changement d’utilisateur ou d’organisation.

## Stratégie de rendu

Choisir par route et source de données :

- contenu préparé à l’avance pour une donnée publique stable ;
- rendu dynamique pour une donnée liée à la requête ou la session ;
- cache avec revalidation pour une donnée partageable avec fraîcheur définie ;
- chargement navigateur pour une interaction réellement client ;
- rendu progressif pour afficher une structure utile pendant une partie lente.

Documenter fraîcheur, portée, erreur, invalidation et effet multi-instance.

## Expérience produit

Une application professionnelle privilégie la compréhension et l’action :

- titre et emplacement clairs ;
- action principale identifiable ;
- données organisées pour comparaison ;
- commandes utilisant les composants existants ;
- chargement localisé ;
- absence, refus, erreur et réussite ;
- aide au moment utile ;
- densité adaptée au travail fréquent.

Éviter les grandes sections promotionnelles, les cartes décoratives et les mises en page qui repoussent l’outil principal.

Un dialogue convient à une décision courte qui interrompt le parcours. Une page convient à une tâche longue, partageable ou reprenable. Un panneau latéral convient à une inspection secondaire si les deux zones restent utilisables. Chaque surface temporaire doit gérer ouverture, fermeture, focus, touche d’échappement et retour au déclencheur.

L’aide doit apparaître au moment utile : libellé clair, exemple, explication courte ou lien vers une procédure. Une visite guidée ne doit pas compenser des noms incompréhensibles.

## Système de design

Utiliser des valeurs de conception pour couleur, typographie, espacement, dimensions et mouvement. Les valeurs sémantiques décrivent l’intention, puis les marques fournissent des variantes validées.

Réutiliser les composants existants. Une variante nouvelle doit représenter un besoin durable, pas contourner le contrat du composant.

Séparer primitives visuelles, composants composés et composants métier.

## Adaptation aux écrans

- Concevoir depuis l’espace contraint.
- Utiliser des limites de largeur cohérentes.
- Autoriser le retour à la ligne.
- Prévoir les traductions longues.
- Garder les contrôles dans leur conteneur.
- Tester portrait, paysage et clavier virtuel lorsque concernés.
- Choisir explicitement le comportement des tableaux.

Ne pas masquer une mise en page cassée par un débordement global caché.

## Accessibilité

- Structure HTML sémantique.
- Titre de document et titre principal cohérents.
- Libellé pour chaque champ.
- Bouton pour action, lien pour navigation.
- Utilisation complète au clavier.
- Focus visible et restauré après dialogue.
- Contraste dans chaque marque.
- Information jamais transmise uniquement par la couleur.
- Zoom non désactivé et redistribution sans chevauchement.
- Mouvement réduit respecté.
- Texte alternatif selon le sens de l’image.

Next.js annonce une navigation en utilisant notamment le titre du document. Chaque page doit donc fournir un titre distinct et descriptif.

## Pages publiques

Classer chaque page :

- publique indexable ;
- publique non indexable ;
- privée ;
- propre à une marque ;
- propre à une langue ;
- prévisualisation.

Une page indexable fournit son contenu essentiel dans le document HTML initial, le langage de structure envoyé par le serveur.

## Métadonnées

Définir selon le besoin :

- titre ;
- description ;
- adresse canonique ;
- langues alternatives ;
- règle d’indexation ;
- image de partage ;
- icônes ;
- données structurées ;
- plan de site.

Les métadonnées appartiennent au serveur et ne contiennent aucune donnée privée. Leur cache doit être isolé par route, marque, langue et domaine.

Valider le domaine avant de construire une adresse canonique. Une adresse de prévisualisation ne doit pas devenir canonique.

## Langues et formatage

Définir :

- langues prises en charge ;
- langue par défaut ;
- stratégie d’adresse ;
- détection ;
- choix explicite de l’utilisateur ;
- comportement pour une langue invalide ;
- direction du document ;
- fuseau horaire, dates, nombres et devises.

Ne pas concaténer des fragments de phrase dont l’ordre ne fonctionne que dans une langue. Tester les textes longs et les écritures de droite à gauche lorsqu’elles sont prises en charge.

## Permissions dans l’interface

L’interface peut cacher ou désactiver une action pour éviter une demande inutile. Le serveur vérifie toujours l’autorisation.

Un refus visible doit expliquer ce que l’utilisateur peut faire ensuite sans révéler une ressource sensible.

Après un changement d’organisation, retirer immédiatement les données et sélections de l’organisation précédente.

## Images, polices et scripts

- Utiliser les composants Next.js lorsque leurs garanties correspondent au déploiement.
- Fournir des dimensions ou proportions stables aux images.
- Définir les tailles réellement affichées.
- Charger prioritairement uniquement les ressources principales.
- Limiter familles et variantes de police.
- Différer les scripts tiers non essentiels.
- Évaluer consentement, sécurité, données et performance de chaque script.

## Contrôles obligatoires

- rendu serveur initial ;
- navigation directe et côté client ;
- frontière serveur et navigateur inspectée ;
- absence de secret dans le code livré ;
- chargement, absence, refus, erreur et succès ;
- formulaire et collection concernés ;
- petit écran, grand écran, zoom et texte long ;
- clavier et technologie d’assistance ;
- thème, marque et langue alternatifs ;
- titre, adresse canonique, plan de site et image de partage ;
- cache isolé entre deux organisations ;
- poids du code navigateur après une nouvelle dépendance.

## Sources officielles

- [Composants serveur et composants navigateur](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Métadonnées et images de partage](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)
- [Internationalisation avec Next.js](https://nextjs.org/docs/app/guides/internationalization)
- [Accessibilité dans Next.js](https://nextjs.org/docs/architecture/accessibility)
