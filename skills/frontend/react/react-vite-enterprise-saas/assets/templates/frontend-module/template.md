# Template de création d’un module frontend

Utiliser ce document comme procédure de création. Le nom du module doit employer des mots métier complets et sa responsabilité doit être compréhensible sans ouvrir son implémentation.

## Informations à renseigner

- Nom complet du module :
- Responsabilité métier :
- Utilisateurs concernés :
- Permissions appartenant au module :
- Features initiales :
- Dépendances autorisées :
- Routes et navigation :
- États, erreurs et preuves attendues :

<!-- preserved-source-part-start: frontend-section-39-subsection-39-3 -->
## 39.3 Création d’un nouveau module

Lorsqu’un nouveau module est justifié :

1. choisir un nom métier stable ;
2. créer `modules/module-<nom>/` ;
3. créer son manifeste ;
4. définir son API publique ;
5. créer `features/` ;
6. créer `shared-module/` si nécessaire ;
7. définir routes et navigation ;
8. définir permissions ;
9. définir contrats et événements ;
10. définir providers et état ;
11. enregistrer le module dans le registre ;
12. configurer le lazy loading ;
13. documenter les dépendances ;
14. écrire les tests de frontières ;
15. mettre à jour la documentation.

<!-- preserved-source-part-end: frontend-section-39-subsection-39-3 -->
