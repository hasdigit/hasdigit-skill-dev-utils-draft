# Sécurité frontend

Cette référence traite de l’authentification, des frontières de sécurité, des attaques par injection de script, des secrets et de l’évaluation des dépendances.

<!-- preserved-source-part-start: frontend-section-27-heading -->
# 27. Sécurité frontend et gouvernance des permissions

<!-- preserved-source-part-end: frontend-section-27-heading -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-1 -->
## 27.1 Authentification

Préférer :

- cookie HttpOnly ;
- Secure ;
- SameSite ;
- BFF ;
- OAuth2/OIDC ;
- PKCE ;
- rotation ;
- expiration courte.

Éviter les tokens sensibles dans localStorage.

<!-- preserved-source-part-end: frontend-section-27-subsection-27-1 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-15 -->
## 27.15 XSS

- éviter `dangerouslySetInnerHTML`;
- assainir le contenu riche ;
- utiliser une CSP ;
- valider les entrées ;
- encoder les sorties.

<!-- preserved-source-part-end: frontend-section-27-subsection-27-15 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-16 -->
## 27.16 Secrets

Aucun secret dans :

- code ;
- variables Vite ;
- bundle ;
- storage ;
- source map publique ;
- log ;
- HTML.

<!-- preserved-source-part-end: frontend-section-27-subsection-27-16 -->

<!-- preserved-source-part-start: frontend-section-27-subsection-27-17 -->
## 27.17 Dépendances

Évaluer :

- sécurité ;
- licence ;
- maintenance ;
- taille ;
- réputation ;
- compatibilité.
<!-- preserved-source-part-end: frontend-section-27-subsection-27-17 -->
