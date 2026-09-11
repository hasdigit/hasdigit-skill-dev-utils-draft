# Interface produit et expérience utilisateur

Lire ce document pour toute page, navigation, formulaire, tableau, liste, dialogue, notification, aide intégrée ou modification visuelle.

## Partir du travail réel de l’utilisateur

Avant de concevoir une interface, identifier :

- la personne qui agit et son niveau de connaissance ;
- son objectif concret ;
- la fréquence et l’urgence de l’action ;
- les informations nécessaires à sa décision ;
- les erreurs prévisibles et leur coût ;
- les permissions et l’organisation cliente actives ;
- les appareils, tailles d’écran et modes de saisie concernés.

Une interface professionnelle privilégie la compréhension, la comparaison et l’action. Ne pas transformer un outil de travail dense en page promotionnelle composée de grands slogans et de cartes décoratives.

## Hiérarchie d’une page

Une page doit rendre visibles dans cet ordre :

1. son identité et son emplacement dans le produit ;
2. son action principale, lorsqu’elle existe ;
3. les informations nécessaires à la décision ;
4. les états de chargement, d’absence, d’erreur ou de refus ;
5. les actions secondaires et l’aide contextuelle.

Utiliser un seul titre principal compréhensible. Les titres internes doivent décrire le contenu, pas la forme visuelle. Éviter les introductions longues qui repoussent l’outil principal sous la première zone visible.

## Système de design

Réutiliser les composants et règles visuelles existants avant d’en créer de nouveaux. Le système de design doit fournir :

- couleurs et contrastes sémantiques ;
- typographie ;
- espacements ;
- dimensions des contrôles ;
- icônes ;
- états interactifs ;
- règles de mouvement ;
- comportements adaptatifs ;
- thèmes et marques autorisés.

Un composant partagé doit représenter une responsabilité visuelle stable. Ne pas créer une variante générale pour un besoin isolé et ne pas dupliquer un composant existant pour éviter de comprendre son contrat.

Les couleurs, espacements et dimensions propres à une marque doivent provenir de valeurs de conception validées, pas de nombres dispersés dans les composants.

## Composants et commandes

- Utiliser un bouton pour une action et un lien pour une navigation.
- Employer une icône familière lorsqu’elle exprime mieux une commande compacte, avec un nom accessible et une infobulle si sa signification peut être ambiguë.
- Utiliser une case à cocher ou un interrupteur pour un état binaire.
- Utiliser des onglets pour plusieurs vues d’un même contexte, pas pour remplacer une navigation globale.
- Utiliser un menu lorsque plusieurs commandes secondaires doivent rester disponibles sans surcharger la page.
- Garder les dimensions des contrôles stables pendant le chargement et après une interaction.
- Ne pas utiliser une carte pour chaque section ni placer une carte dans une autre carte.

Chaque contrôle doit prévoir ses états normal, survolé, focalisé, actif, désactivé, en cours, réussi et échoué lorsque ces états sont applicables.

## Mises en page et navigation

Les mises en page persistantes de Next.js doivent conserver uniquement ce qui doit réellement survivre à la navigation. Ne pas y placer un état métier qui devrait être rechargé ou réinitialisé par route.

La navigation doit :

- indiquer la position active ;
- respecter les permissions sans présenter le masquage comme une protection ;
- rester utilisable sur petit écran et sous zoom ;
- conserver des adresses partageables pour les vues importantes ;
- produire un titre de document distinct pour chaque destination ;
- gérer clairement le retour, l’avance et le rechargement direct.

Un fil de navigation est utile lorsque la hiérarchie dépasse ce que le titre et la navigation principale rendent évident. Il ne doit pas répéter mécaniquement des segments techniques d’adresse.

## Dialogues, panneaux et menus

Utiliser un dialogue pour une décision ou une tâche courte qui doit interrompre le contexte. Utiliser une page lorsque la tâche est longue, partageable, profonde ou susceptible d’être reprise.

Un panneau latéral convient à une inspection ou une édition secondaire qui bénéficie du maintien du contexte. Il ne doit pas comprimer la page au point de rendre les deux zones inutilisables.

Pour chaque surface temporaire :

- définir l’ouverture, la fermeture et le retour du focus ;
- fermer avec la touche d’échappement lorsque ce comportement est attendu ;
- empêcher l’interaction avec l’arrière-plan si la surface est modale ;
- conserver une taille adaptée au contenu et à l’écran ;
- éviter plusieurs surfaces modales imbriquées ;
- vérifier le comportement avec la navigation par historique si la surface possède une adresse.

## Listes, tableaux et collections

Choisir la présentation selon la décision à prendre :

- tableau pour comparer plusieurs attributs alignés ;
- liste pour parcourir des éléments moins structurés ;
- grille pour des éléments principalement visuels ;
- vue détaillée pour une quantité d’information incompatible avec l’espace disponible.

Toute collection doit définir :

- chargement initial ;
- absence de résultat ;
- erreur ;
- recherche et filtres ;
- tri ;
- pagination ou chargement progressif ;
- sélection ;
- actions groupées ;
- conservation pertinente de l’état dans l’adresse.

Préférer une pagination serveur pour les grands ensembles. Utiliser un curseur lorsque l’ordre et les modifications fréquentes rendent une pagination par numéro instable. Utiliser un défilement continu seulement si la consultation séquentielle prime sur le repérage et le retour à une position précise.

La virtualisation est justifiée par une mesure de volume ou de performance. Elle doit préserver le clavier, la lecture assistée, la hauteur de défilement et la restauration de position.

## Chargement et progression

Afficher le chargement au niveau de la partie réellement en attente. Une mise en page stable et un contenu partiel utile sont préférables à un écran entièrement bloqué.

- Un bouton en cours conserve son libellé ou une largeur stable.
- Une action répétable dangereuse est désactivée ou rendue sûre.
- Un squelette doit ressembler à la structure réelle sans simuler un contenu trompeur.
- Une opération longue indique sa progression lorsqu’elle est connue.
- Une opération différée explique que l’utilisateur peut quitter la page et où retrouver son résultat.

Les fichiers `loading.tsx` et les frontières d’attente doivent être placés selon le besoin utilisateur, pas ajoutés automatiquement à chaque dossier.

## Retour après chaque action

Toute action doit produire un résultat observable :

- succès confirmé ;
- erreur compréhensible ;
- validation près du champ concerné ;
- état actualisé après modification ;
- prochaine action possible ;
- référence vers un traitement différé lorsque nécessaire.

Une notification temporaire ne doit pas être l’unique preuve d’un changement important. Mettre aussi à jour la zone concernée et conserver une trace durable lorsque le métier l’exige.

Pour une suppression ou une opération irréversible, expliquer clairement l’objet, l’effet et les possibilités de récupération. Ne pas demander une confirmation générique pour chaque action sans évaluer le risque réel.

## Formulaires

Un formulaire doit :

- utiliser les capacités natives du langage HTML, le langage de structure des pages, avant une solution personnalisée ;
- conserver les valeurs après une erreur récupérable ;
- distinguer aide, avertissement et erreur ;
- afficher les erreurs de validation près des champs et un résumé lorsque nécessaire ;
- indiquer clairement l’état de soumission ;
- résister à une soumission répétée ;
- annoncer le succès et l’échec ;
- fonctionner autant que raisonnablement possible avant le chargement complet du code navigateur.

La validation dans le navigateur améliore l’expérience. Seule la validation serveur protège la donnée. Lire [Données, état, formulaires et erreurs](data-state-forms-and-errors.md) pour la frontière complète.

## Aide et prise en main

L’aide doit être accessible au moment où la question apparaît : libellé clair, exemple, explication courte, lien vers une procédure ou message d’état.

Ne pas remplacer des noms compréhensibles par une visite guidée obligatoire. Une prise en main progressive peut présenter une fonction avancée, mais l’interface principale doit rester compréhensible sans mémoriser cette visite.

Les textes doivent employer le vocabulaire du métier, expliquer les conséquences et éviter les codes internes. Un code de diagnostic peut être affiché en complément d’un message humain, jamais seul.

## Adaptation et accessibilité

Les contraintes de petit écran, zoom, clavier, contraste, mouvement réduit et technologies d’assistance font partie de la conception initiale. Lire [Accessibilité, tailles d’écran et navigation](accessibility.md) et exécuter ses contrôles pour toute modification visuelle.

## Contrôle avant livraison

- parcours principal compréhensible sans documentation externe ;
- titre, hiérarchie et action principale visibles ;
- navigation directe, côté client, retour et rechargement ;
- chargement, absence, erreur, refus et succès ;
- formulaire invalide, valide, répété et interrompu ;
- liste vide, filtrée, paginée et volumineuse ;
- petit écran, écran large, zoom et texte long ;
- clavier et technologie d’assistance sur le parcours critique ;
- marque, thème et langue alternatifs ;
- absence de duplication inutile du système de design.

## Sources officielles

- [Formulaires avec les traitements serveur Next.js](https://nextjs.org/docs/app/guides/forms)
- [Accessibilité dans Next.js](https://nextjs.org/docs/architecture/accessibility)
