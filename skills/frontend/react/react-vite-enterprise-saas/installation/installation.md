# Installation et démarrage obligatoire de chaque session

Ce guide fait partie du skill `frontend-react-vite-enterprise-saas`. Il doit rester dans le même dossier maître que [`SKILL.md`](../SKILL.md), les références d’architecture, les modèles, les métadonnées et les scénarios de test.

## Installer le skill complet

1. Copier le dossier `react-vite-enterprise-saas/` en entier dans le répertoire de skills de l’environnement cible.
2. Ne pas copier uniquement `SKILL.md` : les exigences d’architecture, de nommage, de permissions, de sécurité, d’accessibilité, de tests et de livraison sont réparties dans les ressources du skill.
3. Vérifier que [`SKILL.md`](../SKILL.md), [`references/`](../references/), [`assets/templates/`](../assets/templates/), [`agents/`](../agents/) et [`tests/`](../tests/) sont présents.
4. Recharger l’environnement lorsque la plateforme l’exige.
5. Au début de chaque nouvelle session, envoyer le prompt obligatoire ci-dessous avant de demander une modification du produit.

Le prompt ne donne aucune autorisation supplémentaire à l’agent. Les limites d’accès, les confirmations requises et le périmètre défini par l’utilisateur restent applicables.

## Prompt obligatoire de démarrage d’une nouvelle session

Remplacer uniquement le texte entre crochets par le chemin réel. Conserver le reste du prompt.

```text
Tu travailles dans le projet frontend actuellement ouvert en appliquant la compétence React, TypeScript et Vite Enterprise SaaS dont le dossier maître est :
[indiquer ici le chemin complet vers le dossier react-vite-enterprise-saas]

Avant toute modification du projet, prends en charge le dossier maître complet de cette compétence et mets en place les garde-fous nécessaires à son respect strict.

Procédure obligatoire de démarrage :

1. Analyse intégralement le dossier maître de la compétence. Lis `SKILL.md`, tous les documents de `references/`, le présent guide d’installation, les scénarios de `tests/`, les métadonnées de `agents/`, les modèles de `assets/templates/` et l’historique des évolutions. Distingue clairement les règles normatives, les explications, les modèles de sortie et les éléments historiques. Ne prétends jamais avoir lu un fichier que tu n’as pas réellement consulté.

2. Inspecte le projet avant d’agir. Recherche les instructions existantes destinées aux agents, l’architecture, les conventions de dossiers et de fichiers, la configuration TypeScript, les outils de contrôle de style, les tests, les contrôles automatisés déclenchés à chaque changement, les mécanismes de permissions, les protections de sécurité, les contrôles d’accessibilité et les critères de livraison. Travaille avec les conventions déjà présentes et ne détruis, ne remplace ou ne déplace aucun dispositif existant sans nécessité démontrée.

3. Compare chaque exigence applicable de la compétence avec les garde-fous du projet. Pour chaque exigence, indique si elle est déjà appliquée automatiquement, couverte par une vérification humaine documentée, absente, devenue obsolète ou en conflit avec une règle de niveau supérieur. Une simple mention dans un document ne constitue pas une preuve d’application automatique.

4. Vérifie si la compétence a évolué depuis la dernière session. Compare au minimum son emplacement, son historique des évolutions et, lorsque le projet le permet, son empreinte de contenu ou sa révision source avec l’inventaire enregistré par les sessions précédentes. Si la compétence a changé, réévalue tous les garde-fous concernés et mets à jour uniquement ceux qui doivent l’être.

5. Réutilise l’espace partagé déjà prévu pour les agents d’intelligence artificielle lorsqu’il existe. S’il n’existe aucun équivalent, crée à la racine du projet le dossier `.artificial-intelligence-agent-workspace/` avec une organisation compréhensible telle que :
   - `workspace-purpose-and-rules.md` pour expliquer le rôle du dossier et ses limites ;
   - `active-skill-source-inventory.md` pour identifier le dossier maître, la version ou la révision réellement lue et la date de vérification ;
   - `skill-requirements-and-safeguards.md` pour relier chaque exigence applicable à son garde-fou et à sa preuve ;
   - `current-work-context.md` pour conserver les décisions, hypothèses, travaux en cours et prochaines étapes utiles aux sessions suivantes ;
   - `verification-reports/` pour les comptes rendus de contrôle nécessaires à la continuité.

   N’utilise pas ce dossier pour stocker des secrets, des données sensibles, des fichiers générés inutiles ou des notes personnelles sans valeur pour les autres sessions. Cet espace complète la compétence, mais ne remplace jamais le dossier maître comme source de vérité.

6. Mets en place ou actualise des garde-fous proportionnés au projet. Ils doivent notamment couvrir les frontières de modules et de fonctionnalités, les dépendances autorisées, les noms complets et compréhensibles, les préfixes TypeScript écrits en toutes lettres, les permissions côté interface et côté serveur, l’isolation des organisations clientes appelées tenants, la sécurité, la gestion des erreurs, l’accessibilité, l’adaptation aux tailles d’écran, le zoom, les tests, la construction de production et les critères de livraison.

7. Ne crée pas des contrôles uniquement décoratifs. Lorsqu’une exigence peut être vérifiée automatiquement de manière fiable, intègre-la aux outils existants de contrôle, de test ou d’intégration continue. Lorsqu’elle exige un jugement humain, ajoute un point de contrôle explicite avec une preuve attendue. N’ajoute pas une nouvelle dépendance ou une configuration générale sans vérifier sa compatibilité et sa nécessité.

8. Utilise des noms complets et un langage compréhensible dans le code appartenant au projet, les dossiers, les fichiers, les types, les documents et les rapports. N’emploie pas un préfixe réduit tel que `I`, `T` ou `E` pour représenter une interface, un type ou une énumération. Utilise les mots complets `Interface`, `Type` et `Enumeration`, sauf contrainte externe ou fichier généré clairement documenté.

9. Avant la première modification fonctionnelle, présente un rapport de préparation indiquant : les fichiers du skill réellement lus, les garde-fous déjà présents, les écarts détectés, les mises à jour nécessaires, les contrôles qui serviront de preuves et les éventuels conflits à faire arbitrer. Mets ensuite en place les garde-fous autorisés qui sont indispensables avant de commencer la mission.

10. Pendant toute la session, vérifie chaque décision d’architecture et chaque changement de code contre la compétence active. Exécute les contrôles pertinents après les changements, maintiens le contexte partagé après toute décision structurante et transmets les mêmes exigences à tout sous-agent avant sa contribution.

11. Avant de terminer la session, exécute les validations pertinentes et produis un rapport compréhensible indiquant les exigences respectées, les preuves disponibles, les écarts restants, les décisions prises et l’état exact permettant à une autre session de reprendre sans inventer le contexte.

Respecte les instructions de niveau supérieur, les autorisations de l’utilisateur et les limites réelles des outils. Si une règle de la compétence ne peut pas être appliquée, indique précisément la règle concernée, la raison, le risque et la décision nécessaire. Ne contourne jamais une limitation et ne transforme jamais une hypothèse en fait.
```

## Résultat attendu avant le développement

La session est correctement initialisée seulement lorsque :

- le dossier maître complet a été inventorié et les documents normatifs applicables ont été lus ;
- les garde-fous existants ont été contrôlés au lieu d’être supposés ;
- les écarts importants ont été corrigés ou explicitement signalés ;
- la continuité entre sessions dispose d’un emplacement partagé, compréhensible et non sensible ;
- le rapport de préparation identifie les preuves qui permettront de vérifier le respect du skill.
