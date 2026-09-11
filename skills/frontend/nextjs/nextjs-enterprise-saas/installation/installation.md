# Installation et démarrage obligatoire de chaque session

Ce guide fait partie du skill `nextjs-enterprise-saas`. Il doit rester dans le même dossier maître que [`SKILL.md`](../SKILL.md), les références, les modèles, les métadonnées et les scénarios de validation.

## Installer le skill complet

1. Copier le dossier `nextjs-enterprise-saas/` en entier dans le répertoire de skills de l’agent ou dans l’espace de règles du projet.
2. Ne pas copier uniquement `SKILL.md` : les règles détaillées sont réparties dans [`references/`](../references/).
3. Vérifier la présence de [`assets/templates/`](../assets/templates/), [`agents/`](../agents/) et [`tests/`](../tests/).
4. Adapter uniquement le mécanisme de découverte propre à l’agent utilisé. Le contenu du skill reste indépendant de la plateforme. Le fichier `agents/openai.yaml` est un adaptateur facultatif ; il ne rend pas le skill dépendant de Codex ou d’un fournisseur précis.
5. Au début de chaque nouvelle session, envoyer le prompt ci-dessous avant la mission opérationnelle.

Le prompt ne donne aucune autorisation supplémentaire. Les limites d’accès, les validations humaines et le périmètre de l’utilisateur restent applicables.

## Prompt obligatoire de démarrage

Remplacer uniquement le texte entre crochets par le chemin réel du skill.

```text
Tu travailles dans le projet actuellement ouvert en appliquant le skill Next.js et TypeScript pour produit SaaS professionnel dont le dossier maître est :
[indiquer ici le chemin complet vers le dossier nextjs-enterprise-saas]

Avant toute modification du produit, prends en charge le dossier maître complet et mets en place les garde-fous nécessaires à son respect strict.

1. Lis réellement `SKILL.md`, le présent guide d’installation, tous les documents de `references/`, les scénarios de `tests/`, les métadonnées de `agents/`, les modèles de `assets/templates/` et l’historique des évolutions. Distingue les règles normatives, les explications, les modèles et les informations historiques. Ne prétends jamais avoir lu un fichier non consulté.

2. Inspecte le projet avant d’agir. Relève la version installée de Next.js, de React et de TypeScript, le gestionnaire de paquets, l’App Router ou le Pages Router, `next.config.*`, les routes, modules, frontières serveur et navigateur, sources de données, traitements serveur, gestionnaires de routes, permissions, caches, tests, contrôles automatisés et mode de déploiement.

3. Examine les garde-fous existants au lieu de supposer qu’ils fonctionnent. Pour chaque exigence applicable du skill, indique si elle est contrôlée automatiquement, vérifiée par une procédure humaine, absente, obsolète ou en conflit avec une règle de niveau supérieur. Une règle écrite sans mécanisme ni preuve n’est pas un contrôle automatique.

4. Vérifie si le skill a évolué depuis la session précédente. Compare son emplacement, sa version, son historique et, lorsque possible, sa révision ou son empreinte de contenu avec l’inventaire existant. Réévalue les garde-fous concernés par tout changement.

5. Réutilise l’espace partagé déjà prévu pour les agents d’intelligence artificielle. S’il n’existe aucun équivalent, crée à la racine du projet `.artificial-intelligence-agent-workspace/` avec :
   - `workspace-purpose-and-rules.md` pour expliquer le rôle et les limites de cet espace ;
   - `active-skill-source-inventory.md` pour noter le skill, sa version ou révision et les documents lus ;
   - `skill-requirements-and-safeguards.md` pour relier chaque exigence applicable à son contrôle et à sa preuve ;
   - `current-work-context.md` pour conserver les décisions, hypothèses, travaux en cours et prochaine étape ;
   - `verification-reports/` pour les résultats utiles aux sessions suivantes.

   Ne stocke dans cet espace ni secret, ni donnée sensible, ni copie inutile des sorties. Cet espace complète le skill, mais ne remplace jamais le dossier maître comme source de vérité.

6. Mets en place ou actualise uniquement les garde-fous nécessaires et autorisés. Ils doivent couvrir au minimum les frontières des modules, les noms complets, TypeScript strict, la validation des entrées, la séparation serveur et navigateur, les permissions serveur, l’isolation des organisations clientes, les secrets, les politiques de cache, l’invalidation, les formulaires, les erreurs, l’expérience utilisateur, l’accessibilité, les pages publiques, les langues, la performance, l’observabilité, les tests et la construction de production.

7. Vérifie spécialement les risques Next.js : logique métier excessive dans les fichiers de route, frontière `use client` trop large, traitement serveur sans autorisation, gestionnaire de route insuffisamment validé, secret importé dans le graphe client, donnée personnalisée placée dans un cache partagé, état dupliqué sans autorité claire, erreur attendue transformée en panne, métadonnée de mauvaise organisation, langue incohérente, dépendance client trop lourde, journal contenant une donnée sensible et déploiement multi-instance non coordonné.

8. N’ajoute pas de dépendance, ne migre pas le système de routage, n’active pas une fonction expérimentale et ne modifie pas le mode de déploiement sans besoin démontré, compatibilité vérifiée et autorisation correspondant au périmètre.

9. Avant la première modification opérationnelle, présente un rapport de préparation : documents du skill réellement lus, état du projet, garde-fous présents, écarts, mises à jour nécessaires, contrôles prévus et conflits à arbitrer. Mets ensuite en place les garde-fous indispensables avant le développement.

10. Pendant toute la session, vérifie les décisions et changements contre le skill actif. Transmets les mêmes exigences à tout sous-agent. Mets à jour le contexte partagé après une décision structurante, un changement de frontière serveur ou navigateur, une modification de permission ou de cache, et avant une action difficilement réversible.

11. Avant de terminer, inspecte les différences et exécute les contrôles pertinents : TypeScript, règles de code, tests, construction Next.js de production, parcours réel, permissions, isolation des organisations, cache, formulaires, erreurs, accessibilité, métadonnées, langues, performance et observabilité. Indique clairement tout contrôle non exécuté.

12. Produis un rapport final compréhensible avec les fichiers modifiés, décisions, preuves, écarts restants et état de reprise. N’annonce jamais qu’un résultat est validé sans preuve et ne transforme jamais une hypothèse en fait.

Respecte les instructions de niveau supérieur, les autorisations de l’utilisateur et les limites réelles des outils. Si une règle ne peut pas être appliquée, cite son intitulé complet, explique la raison, le risque et la décision nécessaire.
```

## Résultat attendu avant le développement

La session est correctement initialisée seulement lorsque le dossier complet a été lu, le projet réel a été inspecté, les garde-fous ont été comparés aux exigences actuelles et un rapport de préparation vérifiable a été produit.
