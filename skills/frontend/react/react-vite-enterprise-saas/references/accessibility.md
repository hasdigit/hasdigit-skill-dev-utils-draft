# Accessibilité, responsive et interaction

Cette référence couvre l’adaptation aux écrans, le zoom, le reflow, la sémantique interactive et les exigences d’accessibilité.

<!-- preserved-source-part-start: frontend-section-16 -->
# 16. Responsive et adaptatif

## 16.1 Exigence non négociable

Toutes les interfaces doivent fonctionner sur :

- très petit mobile ;
- mobile standard ;
- grand mobile ;
- tablette portrait ;
- tablette paysage ;
- petit ordinateur ;
- desktop moyen ;
- grand écran ;
- écran très large.

## 16.2 Mobile-first

Concevoir d’abord le comportement mobile.

## 16.3 Règles de layout

Utiliser :

- flexbox ;
- grid ;
- `minmax`;
- `clamp`;
- dimensions fluides ;
- containers ;
- `max-width`;
- breakpoints cohérents ;
- `min-width: 0` dans les flex/grid lorsque nécessaire.

Éviter :

- largeur fixe globale ;
- hauteur fixe sur contenu dynamique ;
- `100vw` lorsque cela déborde ;
- positionnement absolu structurel ;
- margin négative fragile ;
- scroll horizontal global.

## 16.4 Tables

Pour les petits écrans :

- scroll horizontal local ;
- colonnes prioritaires ;
- mode carte ;
- détail dépliable ;
- actions regroupées.

## 16.5 Navigation

La sidebar doit :

- être fixe ou persistante sur grand écran ;
- devenir drawer ou navigation mobile ;
- gérer overlay ;
- gérer focus ;
- gérer fermeture ;
- ne pas dépasser ;
- ne pas créer de double scroll.

## 16.6 Modales

Sur mobile :

- plein écran ou drawer si nécessaire ;
- bouton de fermeture visible ;
- contenu scrollable ;
- clavier virtuel géré ;
- focus géré ;
- actions accessibles.

---

<!-- preserved-source-part-end: frontend-section-16 -->

<!-- preserved-source-part-start: frontend-section-17 -->
# 17. Zoom, viewport et reflow

## 17.1 Viewport

Toujours :

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

Jamais :

```html
maximum-scale=1
user-scalable=no
```

## 17.2 Niveaux de test

Tester :

- 100 % ;
- 125 % ;
- 150 % ;
- 200 % ;
- taille de texte augmentée ;
- portrait ;
- paysage.

## 17.3 Causes fréquentes d’ouverture « déjà zoomée »

Vérifier :

- `min-width` globale ;
- image sans `max-width`;
- tableau hors conteneur ;
- `100vw`;
- transform sur root ;
- position absolue ;
- sidebar trop large ;
- modal fixe ;
- viewport incorrect ;
- police ou champ provoquant un zoom mobile ;
- input inférieur à une taille lisible sur certains navigateurs mobiles.

## 17.4 Correction

Corriger la cause.

Ne pas masquer le débordement globalement.

---

<!-- preserved-source-part-end: frontend-section-17 -->

<!-- preserved-source-part-start: frontend-section-18 -->
# 18. Curseur et sémantique interactive

## 18.1 Règles

- `cursor: text` uniquement pour l’éditable ;
- `cursor: pointer` pour actions et liens ;
- curseur par défaut pour texte ordinaire ;
- `button` pour action ;
- `a` pour navigation ;
- `contenteditable` uniquement avec justification.

## 18.2 Interdictions

- caret sur texte statique ;
- `div` cliquable non accessible ;
- `user-select: none` global ;
- `cursor-text` global ;
- gestionnaire de clic sans clavier ;
- faux bouton.

---

<!-- preserved-source-part-end: frontend-section-18 -->

<!-- preserved-source-part-start: frontend-section-31 -->
# 31. Accessibilité

Cible minimale : WCAG 2.2 AA.

Toujours :

- HTML sémantique ;
- navigation clavier ;
- focus visible ;
- ordre logique ;
- labels ;
- descriptions ;
- aria-live ;
- contrastes ;
- information non dépendante de la couleur ;
- alt ;
- modales accessibles ;
- reduced motion ;
- touch targets ;
- zoom ;
- reflow ;
- langue ;
- tableaux structurés.

Ne pas utiliser ARIA pour remplacer un élément natif approprié.

---

<!-- preserved-source-part-end: frontend-section-31 -->
