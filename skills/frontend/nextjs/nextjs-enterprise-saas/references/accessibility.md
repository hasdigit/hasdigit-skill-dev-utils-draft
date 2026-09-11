# Accessibilité, tailles d’écran et navigation

Lire ce document pour toute interface, navigation, formulaire, tableau, dialogue, chargement, erreur ou contenu animé.

## Exigence générale

L’accessibilité n’est pas une finition. Elle fait partie des critères fonctionnels et doit être vérifiée pendant la conception, le développement et les tests.

Respecter au minimum le niveau de conformité demandé par le produit. Lorsqu’aucun niveau n’est indiqué, viser les règles reconnues d’accessibilité du Web et signaler les points non vérifiés.

## Structure sémantique

- Utiliser les éléments HTML selon leur fonction.
- Conserver une hiérarchie de titres compréhensible.
- Fournir un titre de page unique et descriptif.
- Associer chaque champ à son libellé.
- Utiliser un bouton pour une action et un lien pour une navigation.
- Donner un texte alternatif utile aux images porteuses de sens.
- Marquer comme décoratifs les éléments qui ne transmettent aucune information.
- Ne pas remplacer une structure correcte par des rôles ajoutés artificiellement.

## Navigation Next.js

Next.js annonce les changements de route en utilisant d’abord le titre du document, puis le premier titre principal, puis l’adresse. Chaque page doit donc fournir un titre précis et un titre principal cohérent.

Après une navigation côté client :

- vérifier que le nouveau contenu est annoncé ;
- placer le focus lorsque le parcours l’exige ;
- conserver un ordre de tabulation logique ;
- éviter qu’une mise en page persistante laisse un focus dans une zone disparue ;
- tester les routes parallèles, dialogues interceptés et retours arrière lorsqu’ils sont utilisés.

## Clavier et focus

Toutes les actions doivent être utilisables sans souris.

- Le focus doit rester visible.
- L’ordre du focus doit suivre le sens du contenu.
- Un dialogue place le focus à l’ouverture, le retient pendant son usage et le rend à l’élément déclencheur à la fermeture.
- La touche d’échappement ferme une surface temporaire lorsque ce comportement est attendu.
- Aucun piège clavier ne doit exister.
- Les raccourcis doivent éviter les conflits avec le navigateur et les technologies d’assistance.

Ne jamais utiliser un élément `div` ou `span` comme bouton lorsque l’élément natif convient.

## Tailles d’écran et adaptation

Concevoir d’abord pour l’espace contraint, puis enrichir lorsque l’espace augmente.

- Éviter les largeurs fixes pour les zones de contenu.
- Utiliser des limites minimales et maximales cohérentes.
- Autoriser le retour à la ligne des textes longs.
- Prévoir les traductions plus longues.
- Empêcher les boutons et contrôles de sortir de leur conteneur.
- Conserver des cibles tactiles utilisables.
- Tester les orientations portrait et paysage pertinentes.
- Préserver une partie utile du contenu lorsqu’un clavier virtuel apparaît.

Un tableau doit choisir explicitement entre défilement horizontal local, colonnes prioritaires, vue détaillée ou présentation alternative. Ne pas compresser les données jusqu’à les rendre illisibles.

## Zoom et redistribution du contenu

- Ne jamais désactiver le zoom.
- Ne pas utiliser `user-scalable=no` ou une échelle maximale restrictive.
- Tester le zoom du navigateur et l’agrandissement du texte.
- Autoriser la redistribution du contenu sans chevauchement.
- Ne pas masquer un défaut global avec `overflow-x: hidden`.
- Vérifier les éléments fixes, les menus, les dialogues et les notifications sous zoom.

## Chargement et contenu progressif

Les fichiers `loading.tsx` et les frontières d’attente doivent préserver une structure stable.

- Annoncer un chargement uniquement lorsqu’il apporte une information utile.
- Éviter les annonces répétitives pendant une progression rapide.
- Utiliser `aria-busy` lorsque le contexte le justifie.
- Ne pas déplacer brutalement le focus lorsque le contenu arrive.
- Réserver l’espace nécessaire pour limiter les déplacements visuels.
- Respecter la préférence de réduction des animations.

## Formulaires

- Fournir un libellé visible.
- Indiquer les champs obligatoires autrement que par la couleur.
- Relier l’aide et l’erreur au champ.
- Conserver la valeur saisie après une erreur récupérable.
- Placer un résumé d’erreurs lorsqu’un formulaire long le nécessite.
- Déplacer le focus vers l’erreur principale seulement lorsque cela aide réellement.
- Désactiver une soumission répétée sans rendre l’état incompréhensible.
- Annoncer le succès ou l’échec du traitement serveur.

## Couleur, thème et contraste

- Respecter les contrastes demandés pour le texte, les icônes et les limites de contrôle.
- Ne jamais transmettre une information uniquement par la couleur.
- Tester toutes les marques et tous les thèmes autorisés.
- Valider les couleurs configurables avant activation.
- Maintenir les styles de focus dans chaque thème.
- Prévoir une solution sûre lorsqu’une combinaison de marque est insuffisante.

## Erreurs, absence et refus

Chaque état doit être compréhensible et actionnable :

- erreur de validation ;
- erreur réseau ;
- session expirée ;
- permission refusée ;
- ressource absente ;
- liste vide ;
- service temporairement indisponible.

Ne pas afficher uniquement un code. Ajouter un titre, une explication et la prochaine action utile.

## Médias et mouvement

- Fournir sous-titres et transcription lorsque nécessaires.
- Permettre la pause d’un contenu animé ou automatique.
- Respecter la préférence de mouvement réduit.
- Éviter les clignotements dangereux.
- Ne pas démarrer un son automatiquement sans contrôle clair.

## Contrôles automatisés et manuels

Les règles de contrôle de code et les outils d’analyse automatisée détectent une partie des problèmes seulement.

Compléter par :

- navigation complète au clavier ;
- lecture avec une technologie d’assistance sur les parcours critiques ;
- zoom et agrandissement du texte ;
- contrôle du contraste ;
- tailles d’écran réelles ;
- thème clair, sombre et marques configurables ;
- navigation directe et côté client ;
- chargement progressif et erreurs.

## Sources officielles

- [Accessibilité dans Next.js](https://nextjs.org/docs/architecture/accessibility)
- [Règles internationales pour l’accessibilité du Web](https://www.w3.org/WAI/standards-guidelines/wcag/)
