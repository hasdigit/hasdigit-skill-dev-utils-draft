# Scénarios et niveaux de test

Utiliser ces scénarios pour choisir une couverture proportionnée et vérifier les parcours fonctionnels, les permissions, les erreurs, le responsive et l’accessibilité.

<!-- preserved-source-part-start: frontend-section-36 -->
# 36. Tests

## 36.1 Niveaux

- unitaires ;
- composants ;
- intégration ;
- E2E ;
- visuels ;
- accessibilité ;
- contrat ;
- performance.

## 36.2 Scénarios obligatoires

Pour une action critique :

- succès ;
- validation ;
- erreur métier ;
- réseau ;
- timeout ;
- 401 ;
- 403 ;
- 404 ;
- 409 ;
- 422 ;
- 429 ;
- 500 ;
- réponse mal formée ;
- annulation ;
- double clic ;
- navigation ;
- retry ;
- permission absente ;
- mauvais tenant ;
- liste vide ;
- grand volume ;
- mobile ;
- zoom ;
- clavier.

## 36.3 Outils possibles

- Vitest ;
- React Testing Library ;
- MSW ;
- Playwright ;
- axe-core ;
- régression visuelle approuvée.

---

<!-- preserved-source-part-end: frontend-section-36 -->

## Scénario supplémentaire : initialisation des garde-fous au démarrage d’une session

- **Situation initiale** : une nouvelle session reçoit le chemin du dossier maître du skill et ouvre une application qui possède déjà une partie de ses contrôles de qualité.
- **Action** : la session applique le [prompt obligatoire de démarrage](../installation/installation.md).
- **Résultat attendu** : le dossier maître est inventorié, les exigences applicables sont comparées aux contrôles du projet et les garde-fous manquants ou devenus obsolètes sont ajoutés ou actualisés sans destruction des conventions valides.
- **Comportement interdit** : commencer le développement sans rapport de préparation, considérer une règle écrite comme un contrôle automatique, installer une dépendance injustifiée ou ignorer une évolution du skill.
- **Preuve attendue** : inventaire de la source active, correspondance entre exigences et garde-fous, résultats des contrôles TypeScript, architecture, permissions, sécurité, accessibilité, tests et livraison qui sont pertinents pour le projet.
