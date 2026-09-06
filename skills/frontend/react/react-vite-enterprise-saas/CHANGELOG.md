# Historique des évolutions du skill frontend

## Réorganisation non publiée

- Transformation du document monolithique en skill autonome et références thématiques.
- Conservation vérifiable de tout le contenu du document source.
- Colocalisation des templates, scénarios et métadonnées avec le skill frontend.
- Ajout d’un guide d’installation autonome et d’un prompt obligatoire pour contrôler ou actualiser les garde-fous au démarrage de chaque session.

<!-- preserved-source-part-start: frontend-section-47 -->
# 47. Historique de version

## Version 1.1.0

Évolution majeure de l’architecture des permissions et des espaces partagés :

- séparation de `module-permissions/` et `feature-permissions/` ;
- ajout des politiques `routes/`, `components/` et `api-actions/` ;
- adoption du principe « une permission métier, plusieurs surfaces d’application » ;
- ajout des manifestes de permissions par feature ;
- agrégation des manifestes au niveau module ;
- interdiction du catalogue de permissions dans `.env` ;
- TypeScript retenu par défaut ;
- YAML ou JSON autorisé uniquement comme source de vérité génératrice ;
- ajout de `shared/features/` pour les fonctionnalités transversales ;
- ajout de `shared/kernel/` pour l’infrastructure commune ;
- ajout de `shared-module/features/` pour les capacités partagées au sein d’un module ;
- distinction entre shared features et primitives techniques ;
- ajout des règles de cohérence entre route, composant et action API ;
- ajout des tests de politiques, de refus et d’unicité des permissions.

## Baseline modulaire précédente

La baseline précédente avait introduit :

- le niveau `modules/` ;
- l’obligation d’au moins un module ;
- `shared-module/` ;
- les manifestes et le registre des modules ;
- les frontières de dépendance ;
- le lazy loading ;
- l’activation par tenant, licence ou feature flag.

---

<!-- preserved-source-part-end: frontend-section-47 -->
