# Tests, création, audit et livraison

Cette référence couvre l’intégration continue, le workflow de création, les contrôles, la définition de terminé, les anti-patterns et la sévérité des audits.

<!-- preserved-source-part-start: frontend-section-37 -->
# 37. CI/CD

Minimum :

```text
install déterministe
lint
format-check
typecheck
tests
build
```

Selon criticité :

- E2E ;
- accessibilité ;
- audit sécurité ;
- licences ;
- scan secrets ;
- bundle budget ;
- SEO ;
- visual regression ;
- contrat API.

Le pipeline doit échouer en cas d’échec obligatoire.

---

<!-- preserved-source-part-end: frontend-section-37 -->

<!-- preserved-source-part-start: frontend-section-39-heading -->
# 39. Workflow de création d’un module ou d’une feature

<!-- preserved-source-part-end: frontend-section-39-heading -->

<!-- preserved-source-part-start: frontend-section-39-subsection-39-1 -->
## 39.1 Déterminer le bon niveau

Avant toute création, décider si le besoin correspond à :

- une modification d’une feature existante ;
- une nouvelle feature dans un module existant ;
- un élément partagé par les features d’un module ;
- un élément partagé globalement ;
- un nouveau module.

L’agent doit justifier la destination choisie.

<!-- preserved-source-part-end: frontend-section-39-subsection-39-1 -->

<!-- preserved-source-part-start: frontend-section-39-subsection-39-2 -->
## 39.2 Analyse

- besoin ;
- domaine métier ;
- module propriétaire ;
- features concernées ;
- acteurs ;
- permissions ;
- tenant ;
- licence ;
- données ;
- états ;
- erreurs ;
- volumes ;
- responsive ;
- accessibilité ;
- SEO ;
- environnement ;
- dépendances inter-modules.

<!-- preserved-source-part-end: frontend-section-39-subsection-39-2 -->

<!-- preserved-source-part-start: frontend-section-39-subsection-39-5 -->
## 39.5 Promotion vers un niveau partagé

Avant de déplacer un élément :

- vérifier qu’il est réellement réutilisé ;
- vérifier qu’il n’embarque pas une règle métier trop spécifique ;
- choisir `shared-module/` avant `shared/` global lorsque le partage reste interne ;
- stabiliser son contrat ;
- ajouter des tests ;
- mettre à jour les imports ;
- supprimer les duplications devenues inutiles.

<!-- preserved-source-part-end: frontend-section-39-subsection-39-5 -->

<!-- preserved-source-part-start: frontend-section-39-subsection-39-6 -->
## 39.6 Conception

- types ;
- schemas ;
- API ;
- routes ;
- composants ;
- état ;
- loaders ;
- messages ;
- permissions de module et de feature ;
- politiques de route, composant et action API ;
- contrats ;
- événements ;
- API publique ;
- tests ;
- observabilité.

<!-- preserved-source-part-end: frontend-section-39-subsection-39-6 -->

<!-- preserved-source-part-start: frontend-section-39-subsection-39-7 -->
## 39.7 Implémentation

- structure ;
- manifeste ;
- services ;
- queries ;
- mutations ;
- composants ;
- page ;
- routes ;
- navigation ;
- guards ;
- retours ;
- erreurs ;
- tests ;
- docs.

<!-- preserved-source-part-end: frontend-section-39-subsection-39-7 -->

<!-- preserved-source-part-start: frontend-section-39-subsection-39-8 -->
## 39.8 Validation

- lint ;
- format ;
- typecheck ;
- tests ;
- build ;
- frontières de modules ;
- cycles ;
- manifestes ;
- lazy loading ;
- activation/désactivation ;
- responsive ;
- zoom ;
- clavier ;
- permissions ;
- erreurs ;
- requêtes ;
- config ;
- secrets ;
- performance ;
- SEO.

---

<!-- preserved-source-part-end: frontend-section-39-subsection-39-8 -->

<!-- preserved-source-part-start: frontend-section-40 -->
# 40. Checklist module et feature

## Architecture modulaire

- [ ] module parent identifié ;
- [ ] module nommé `module-<nom-métier>` ;
- [ ] `module-permissions/` présent lorsque le module possède des permissions globales ;
- [ ] feature placée sous `modules/<module>/features/` ;
- [ ] `feature-permissions/` présent pour toute feature protégée ;
- [ ] shared feature interne placée dans `shared-module/features/` ;
- [ ] primitive interne placée directement dans `shared-module/` ;
- [ ] shared feature transversale placée dans `shared/features/` ;
- [ ] infrastructure générique placée dans `shared/kernel/` ;
- [ ] manifeste de module valide ;
- [ ] API publique limitée ;
- [ ] registre de modules mis à jour ;
- [ ] routes assemblées feature → module → application ;
- [ ] navigation et permissions déclarées ;
- [ ] activation et désactivation testées si applicables ;
- [ ] lazy loading respecté ;
- [ ] frontières respectées ;
- [ ] aucun import interne inter-module ;
- [ ] aucun cycle ;
- [ ] aucune duplication inutile.


## Permissions

- [ ] permission de module colocalisée dans `module-permissions/` ;
- [ ] permission de feature colocalisée dans `feature-permissions/` ;
- [ ] codes décrivant des capacités métier ;
- [ ] aucune permission liée au nom d’un bouton ou composant ;
- [ ] policies routes déclarées ;
- [ ] policies composants déclarées ;
- [ ] policies actions API déclarées ;
- [ ] appels publics explicitement marqués publics ;
- [ ] catalogue absent de `.env` ;
- [ ] manifeste de feature agrégé par le module ;
- [ ] backend identifié comme autorité finale ;
- [ ] cache invalidé au changement de tenant ou session ;


## SaaS

- [ ] aucun branding figé ;
- [ ] thème via tokens ;
- [ ] logo configurable ;
- [ ] tenant isolé ;
- [ ] cache tenant-safe ;
- [ ] fallback sûr.

## TypeScript

- [ ] strict ;
- [ ] aucun any injustifié ;
- [ ] validation runtime ;
- [ ] schémas.

## API

- [ ] client centralisé ;
- [ ] erreurs ;
- [ ] timeout ;
- [ ] annulation ;
- [ ] retry borné ;
- [ ] correlation ID.

## UX

- [ ] loader ;
- [ ] succès ;
- [ ] erreur ;
- [ ] vide ;
- [ ] confirmation ;
- [ ] double clic empêché.

## Responsive

- [ ] très petit écran ;
- [ ] mobile ;
- [ ] tablette ;
- [ ] desktop ;
- [ ] grand écran ;
- [ ] zoom 200 % ;
- [ ] aucun overflow global.

## Sécurité

- [ ] permission ;
- [ ] backend autoritaire ;
- [ ] tenant ;
- [ ] aucun secret ;
- [ ] XSS ;
- [ ] logs sûrs.

## Accessibilité

- [ ] clavier ;
- [ ] focus ;
- [ ] labels ;
- [ ] contraste ;
- [ ] aria-live ;
- [ ] modal.

## Tests

- [ ] succès ;
- [ ] erreurs ;
- [ ] permission ;
- [ ] tenant ;
- [ ] responsive ;
- [ ] accessibilité ;
- [ ] E2E critique.

---

<!-- preserved-source-part-end: frontend-section-40 -->

<!-- preserved-source-part-start: frontend-section-41 -->
# 41. Definition of Done

Une tâche n’est terminée que si les critères pertinents sont satisfaits.

## Fonctionnel

- [ ] besoin couvert ;
- [ ] cas nominaux ;
- [ ] erreurs ;
- [ ] aucun faux succès ;
- [ ] aucune action silencieuse.

## Architecture modulaire

- [ ] module parent explicite ;
- [ ] features correctement rattachées ;
- [ ] responsabilités séparées ;
- [ ] composants épurés ;
- [ ] `shared-module/features/` utilisé pour les capacités partagées du module ;
- [ ] primitives du module correctement colocalisées ;
- [ ] `shared/features/` utilisé pour les fonctionnalités transversales ;
- [ ] `shared/kernel/` réservé à l’infrastructure générique ;
- [ ] API publique minimale ;
- [ ] manifeste cohérent ;
- [ ] registre mis à jour ;
- [ ] frontières vérifiées ;
- [ ] aucun import interne inter-module ;
- [ ] aucun cycle ;
- [ ] cohérence.

## Permissions et politiques

- [ ] permissions de module dans `module-permissions/` ;
- [ ] permissions de feature dans `feature-permissions/` ;
- [ ] une permission métier réutilisée sur les surfaces correspondantes ;
- [ ] aucune duplication route/composant/API injustifiée ;
- [ ] chaque route possède un mode d’accès explicite ;
- [ ] chaque action API possède une politique explicite ;
- [ ] chaque composant sensible possède une politique ;
- [ ] catalogue typé ou généré depuis une source unique ;
- [ ] aucune permission métier dans `.env` ;
- [ ] contrôle backend confirmé ;
- [ ] tests de refus présents ;

## SaaS

- [ ] branding configurable ;
- [ ] thèmes configurables ;
- [ ] light/dark/system ;
- [ ] logo dynamique ;
- [ ] configuration validée ;
- [ ] absence de fuite tenant ;
- [ ] SEO tenant préservé.

## Erreurs

- [ ] toutes interceptées aux frontières ;
- [ ] normalisées ;
- [ ] messages clairs ;
- [ ] logs ;
- [ ] pas de données sensibles ;
- [ ] reprise proposée.

## Chargement

- [ ] loader adapté ;
- [ ] double clic empêché ;
- [ ] `finally`;
- [ ] progressif ;
- [ ] stabilité layout.

## Requêtes

- [ ] aucune boucle ;
- [ ] annulation ;
- [ ] race condition gérée ;
- [ ] retry contrôlé ;
- [ ] cache correct.

## Responsive

- [ ] mobile ;
- [ ] tablette ;
- [ ] desktop ;
- [ ] zoom ;
- [ ] reflow ;
- [ ] aucun scroll horizontal global.

## Portabilité

- [ ] pas de hardcoding critique ;
- [ ] variables documentées ;
- [ ] runtime config ;
- [ ] local ;
- [ ] production ;
- [ ] base path ;
- [ ] build reproductible.

## Sécurité

- [ ] auth ;
- [ ] permissions ;
- [ ] tenant ;
- [ ] secrets ;
- [ ] XSS ;
- [ ] logs.

## Accessibilité

- [ ] clavier ;
- [ ] focus ;
- [ ] labels ;
- [ ] contraste ;
- [ ] erreurs annoncées ;
- [ ] zoom ;
- [ ] reduced motion.

## Tests

- [ ] lint ;
- [ ] format ;
- [ ] typecheck ;
- [ ] tests ;
- [ ] build ;
- [ ] E2E si nécessaire ;
- [ ] accessibilité.

## Documentation

- [ ] décisions ;
- [ ] variables ;
- [ ] permissions ;
- [ ] limites ;
- [ ] migration ;
- [ ] tests exécutés.

---

<!-- preserved-source-part-end: frontend-section-41 -->

<!-- preserved-source-part-start: frontend-section-42 -->
# 42. Anti-patterns à détecter activement

- features placées directement à la racine hors module ;
- module sans responsabilité métier claire ;
- module nommé `main`, `general`, `misc` ou `utils` ;
- import direct des internes d’un autre module ;
- import de `shared/` global vers un module ;
- `shared-module/` important les détails internes d’une feature ;
- feature protégée sans `feature-permissions/` ;
- permission de feature stockée uniquement au niveau module ;
- permission nommée d’après un bouton, une page ou un appel Axios ;
- trois permissions techniques pour une seule capacité métier ;
- catalogue de permissions dans `.env` ;
- appel API métier sans politique déclarée ;
- route protégée et action API utilisant des permissions contradictoires ;
- moteur générique de permissions contenant tout le catalogue métier ;
- API publique réexportant tout un module ;
- registre de modules contenant de la logique métier ;
- dépendance circulaire inter-module ;
- module chargé statiquement alors qu’il est désactivable ;
- création d’un micro-frontend sans justification ;
- composant monolithique ;
- appels API dans JSX ;
- `useEffect` en boucle ;
- dépendance instable ;
- catch vide ;
- erreur console invisible ;
- message technique utilisateur ;
- token dans localStorage sans décision ;
- permission dispersée ;
- couleur en dur ;
- logo en dur ;
- URL en dur ;
- tenant non isolé ;
- thème appliqué composant par composant ;
- configuration non validée ;
- largeur fixe ;
- zoom désactivé ;
- overflow caché ;
- bouton sans loader ;
- double soumission ;
- liste sans stratégie ;
- table non responsive ;
- modal inaccessible ;
- div cliquable ;
- any ;
- duplication ;
- dépendance inutile ;
- Context énorme ;
- état dérivé ;
- aucune Error Boundary ;
- aucune page erreur ;
- console privée indexable ;
- metadata tenant uniquement côté client sur page publique ;
- cache CDN ne variant pas par tenant.

---

<!-- preserved-source-part-end: frontend-section-42 -->

<!-- preserved-source-part-start: frontend-section-43 -->
# 43. Grille de sévérité pour audit

## P0 — Bloquant critique

- fuite inter-tenant ;
- secret exposé ;
- contournement permission ;
- perte de données ;
- faux succès sur action critique ;
- XSS exploitable ;
- application inutilisable.

## P1 — Majeur

- violation des frontières inter-modules ;
- dépendance circulaire entre modules ;
- mauvais module activé pour un tenant ;
- erreurs non visibles ;
- boucle de requêtes ;
- absence de responsive ;
- mauvaise gestion auth ;
- branding tenant incorrect ;
- page publique SEO incorrecte ;
- double soumission destructive.

## P2 — Important

- dette architecturale ;
- composant monolithique ;
- accessibilité significativement dégradée ;
- performance importante ;
- duplication ;
- test critique absent.

## P3 — Amélioration

- cohérence visuelle mineure ;
- optimisation légère ;
- documentation secondaire ;
- refactoring non urgent.

L’agent doit traiter les P0 avant toute autre amélioration.

---

<!-- preserved-source-part-end: frontend-section-43 -->
