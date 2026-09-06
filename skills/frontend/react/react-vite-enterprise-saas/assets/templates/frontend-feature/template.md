# Template de création d’une feature frontend

Utiliser ce document comme procédure de création. La feature reste rattachée à un module parent et son nom décrit sa capacité métier complète.

## Informations à renseigner

- Nom complet de la feature :
- Module parent :
- Capacité métier :
- Permission métier :
- Routes et composants :
- Contrats et données :
- États, erreurs et messages :
- Tests et critères d’acceptation :

<!-- preserved-source-part-start: frontend-section-39-subsection-39-4 -->
## 39.4 Création d’une feature

Pour une nouvelle feature :

1. identifier son module parent ;
2. créer la structure dans `module-<nom>/features/<feature>/` ;
3. créer `feature-permissions/` avec catalogue, policies et manifeste ;
4. définir types et schémas ;
4. définir services, queries et mutations ;
5. créer composants et pages ;
6. définir routes de feature ;
7. intégrer les routes au module ;
8. définir permissions ;
9. gérer loaders et erreurs ;
10. écrire les tests ;
11. documenter l’API publique éventuelle.

<!-- preserved-source-part-end: frontend-section-39-subsection-39-4 -->
