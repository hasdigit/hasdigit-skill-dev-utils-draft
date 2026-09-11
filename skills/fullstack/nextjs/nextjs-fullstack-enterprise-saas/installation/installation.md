# Installation et démarrage obligatoire de chaque session

Ce guide appartient au skill `nextjs-fullstack-enterprise-saas`. Conserver ensemble [`SKILL.md`](../SKILL.md), les références, modèles, scénarios, métadonnées et l’historique.

## Installer le dossier maître complet

1. Copier le dossier `nextjs-fullstack-enterprise-saas/` complet dans le répertoire de skills ou l’espace de règles de l’agent utilisé.
2. Ne pas copier seulement `SKILL.md` : les décisions détaillées résident dans [`references/`](../references/).
3. Vérifier la présence de [`assets/templates/`](../assets/templates/), [`tests/`](../tests/) et [`agents/`](../agents/).
4. Adapter uniquement le mécanisme de découverte de la plateforme. `agents/openai.yaml` est facultatif et ne rend pas le skill dépendant de Codex ou d’un fournisseur.
5. Envoyer le prompt suivant au début de chaque nouvelle session avant la tâche opérationnelle.

Le prompt ne donne aucune autorisation supplémentaire. Les accès, validations humaines et limites de l’utilisateur restent applicables.

## Prompt obligatoire de démarrage

Remplacer uniquement le texte entre crochets par le chemin réel.

```text
Tu travailles dans le projet actuellement ouvert en appliquant le skill Next.js fullstack pour produit SaaS professionnel dont le dossier maître est :
[indiquer ici le chemin complet vers le dossier nextjs-fullstack-enterprise-saas]

Avant toute modification, prends en charge le dossier maître complet et mets en place les garde-fous nécessaires à son respect strict.

1. Lis réellement `SKILL.md`, le guide d’installation, tous les documents de `references/`, les scénarios de `tests/`, les modèles de `assets/templates/`, les métadonnées de `agents/` et l’historique. Distingue règles normatives, explications, modèles et informations historiques. Ne prétends jamais avoir lu un fichier non consulté.

2. Inspecte le projet réel. Relève les versions de Next.js, React, TypeScript, de l’environnement JavaScript et du gestionnaire de paquets ; l’App Router ou le Pages Router ; `next.config.*` ; la base de données ; le client de données ; les migrations ; les caches ; les files de travail ; les tâches planifiées ; les intégrations ; les tests ; la construction ; l’hébergement et le nombre d’instances.

3. Cartographie les parcours de bout en bout : pages, composants serveur et navigateur, traitements serveur, routes HTTP, cas d’usage, domaine, accès aux données, tables, transactions, permissions, organisations clientes, événements, tâches, intégrations et retours utilisateur. N’invente pas une frontière absente.

4. Examine les garde-fous existants. Pour chaque exigence applicable du skill, indique si elle est automatisée, contrôlée par une procédure humaine, absente, obsolète ou en conflit avec une instruction supérieure. Une règle écrite sans mécanisme ni preuve n’est pas un contrôle automatique.

5. Vérifie si le skill a évolué depuis la session précédente. Compare son emplacement, sa version, son historique et, lorsque possible, sa révision ou son empreinte avec l’inventaire existant. Réévalue tout garde-fou touché par une évolution.

6. Réutilise l’espace partagé existant pour les agents. S’il n’existe aucun équivalent, crée `.artificial-intelligence-agent-workspace/` avec :
   - `workspace-purpose-and-rules.md` pour la responsabilité et les limites ;
   - `active-skill-source-inventory.md` pour le skill, sa version et les fichiers lus ;
   - `skill-requirements-and-safeguards.md` pour relier exigences, contrôles et preuves ;
   - `fullstack-architecture-and-data-flow.md` pour les modules, couches, routes et flux ;
   - `database-and-contract-change-register.md` pour les migrations et contrats en cours ;
   - `current-work-context.md` pour les décisions, hypothèses, travail et prochaine étape ;
   - `verification-reports/` pour les résultats utiles aux sessions suivantes.

   Ne stocke aucun secret, jeton, donnée personnelle ou copie inutile. Cet espace aide la continuité, mais le dossier maître reste la source normative.

7. Mets en place ou actualise seulement les garde-fous nécessaires et autorisés. Ils doivent couvrir selon le projet : noms complets, préfixes `Interface`, `Type` et `Enumeration`, frontières des modules et couches, importations serveur et navigateur, TypeScript strict, validation, contrats de routes, permissions, isolation des organisations, requêtes paramétrées, transactions, migrations, cache, répétition sûre, tâches durables, secrets, accessibilité, observabilité, tests et construction.

8. Vérifie spécialement les risques fullstack Next.js : logique métier dans `page.tsx`, `route.ts` ou un traitement serveur ; route publique non inventoriée ; appel réseau interne inutile ; accès aux données sans organisation ; transaction incomplète ; migration destructive ; réponse contenant trop de champs ; cache privé partagé ; tâche critique confiée seulement à `after` ; webhook non vérifié ; dépendance fournisseur dans le domaine ; secret livré au navigateur ; déploiement multi-instance non coordonné.

9. Ne migre pas le routage, ne remplace pas la base de données, n’ajoute pas une file de travail, n’extrait pas un service, ne modifie pas un contrat public, ne lance pas une migration destructive et ne change pas le déploiement sans besoin démontré, compatibilité, stratégie de retour et autorisation correspondant au périmètre.

10. Avant le développement, présente un rapport de préparation : documents lus, état réel, architecture, données, contrats, garde-fous, écarts, risques, contrôles prévus et conflits à arbitrer. Mets en place les garde-fous indispensables avant le changement opérationnel.

11. Pendant la session, vérifie chaque décision contre le skill actif. Transmets les mêmes règles à tout sous-agent, avec les noms complets des exigences et les explications nécessaires. Mets à jour le contexte partagé après une décision architecturale, un changement de contrat, une migration, une modification de permission, de cache, de tâche ou avant une action difficilement réversible.

12. Avant de terminer, inspecte les différences et exécute les contrôles pertinents : TypeScript, règles de code, tests unitaires, intégration, contrats, migrations, bout en bout, sécurité, construction Next.js, parcours réel, permissions, organisations, cache, tâches, accessibilité, performance, santé et déploiement. Indique tout contrôle non exécuté.

13. Produis un rapport final compréhensible : fichiers modifiés, décisions, contrats et données changés, migrations, preuves, risques, limites et état de reprise. N’annonce jamais un résultat validé sans preuve et ne transforme jamais une hypothèse en fait.

Respecte toujours les instructions de niveau supérieur, les autorisations et les limites réelles des outils. Si une règle ne peut pas être appliquée, cite son intitulé complet, explique la cause, le risque et la décision requise.
```

## Résultat attendu avant le développement

La session est initialisée seulement lorsque le dossier complet a été lu, le flux fullstack réel a été cartographié, les garde-fous ont été comparés au skill actuel et un rapport de préparation vérifiable a été produit.
