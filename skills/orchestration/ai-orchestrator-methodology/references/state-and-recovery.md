# État, protection des données et récupération

Lire cette référence lorsqu’une tâche exige une continuité, un stockage d’état, une protection de données, un point de contrôle, une reprise ou une récupération de contexte.

<!-- preserved-source-part-start: orchestrator-section-3 -->
## 3. Protection de toutes les données

### 3.1 Classification et minimisation

Avant toute persistance ou délégation, l’orchestrateur DOIT :

1. inventorier les données nécessaires ;
2. les classer PUBLIC, INTERNAL, CONFIDENTIAL ou SECRET selon le contexte ;
3. minimiser la quantité transmise ou conservée ;
4. expurger secrets, identifiants, données personnelles et contenu non nécessaire ;
5. remplacer les valeurs retirées par une référence sécurisée ou un marqueur explicite ;
6. limiter les accès au strict nécessaire ;
7. enregistrer la classification et la justification des exceptions.

Une copie expurgée NE DOIT PAS être dite intégrale. Aucun secret réel dans STATE_DIRECTORY, contrats, journaux, preuves ou réponse ; une référence sûre l’identifie sans le révéler.

### 3.2 Stockage et permissions

STATE_DIRECTORY et espaces isolés DOIVENT employer les permissions les plus restrictives et NE DOIVENT PAS être publiés/versionnés par défaut. Si le projet l’impose, séparer métadonnées partageables et données sensibles, puis vérifier le diff.

Les sorties volumineuses ou sensibles NE DOIVENT PAS être copiées intégralement ; conserver portion nécessaire, empreinte, provenance et référence autorisée.

### 3.3 Rétention et clôture

STANDARD/HIGH_RISK DOIT définir la rétention. À la clôture : conservation justifiée, archivage expurgé ou purge autorisée. Toute purge exige cible résolue, autorisation et récupérabilité déclarée.

### 3.4 Secret-canari

Les tests de fuite DOIVENT employer un canari synthétique, jamais un secret réel. Il n’entre que dans l’entrée autorisée et DOIT être absent de toute destination non autorisée. Toute fuite entraîne FAIL, suspension de diffusion et traitement d’incident.

---

<!-- preserved-source-part-end: orchestrator-section-3 -->

<!-- preserved-source-part-start: orchestrator-section-4 -->
## 4. État persistant et points de contrôle transactionnels

### 4.1 Registres canoniques

Pour STANDARD et HIGH_RISK, STATE_DIRECTORY DOIT fournir les fonctions suivantes, quel que soit leur format physique :

| Registre | Contenu |
|---|---|
| request | Demande originale expurgée de manière traçable, portée et résultat attendu. |
| requirements | Exigences identifiées, autorité créatrice, critère, statut et preuve. |
| plan | Étapes, missions, dépendances, propriétaires, risques et états. |
| decisions | Décisions, motifs, alternatives, autorité et décision remplacée. |
| artifacts | Cibles logiques/réelles, rédacteur, génération, empreinte et intégration. |
| verification | Contrôles, résultats, preuves, fraîcheur et éléments STALE. |
| handoff | Index sélectif de reprise, état courant et prochaine action exacte. |

L’agent NE DOIT PAS modifier une source de référence, sauf demande qui en fait une cible. Il conserve si possible snapshot ou empreinte ; pour une cible, référence initiale et évolutions. Un résumé reste un index, jamais l’unique source, décision ou preuve.

### 4.2 Révision transactionnelle

Chaque point DOIT créer une révision immuable avec :

- task_identifier ;
- schema_version ;
- revision monotone et unique ;
- parent_revision ;
- empreintes des entrées actives ;
- empreintes ou identifiants de génération des artefacts ;
- auteur ;
- horodatage si une source temporelle fiable existe, sinon UNAVAILABLE ;
- état de préparation ;
- marqueur final COMMITTED.

Procédure obligatoire :

1. créer une révision nouvelle sans modifier la dernière révision fiable ;
2. écrire les registres et références nécessaires ;
3. relire les champs obligatoires et valider les empreintes ;
4. écrire COMMITTED seulement après validation ;
5. publier ou mettre à jour CURRENT seulement après COMMITTED ;
6. vérifier que CURRENT désigne la nouvelle révision lisible.

Une publication atomique disponible DOIT être utilisée ; sinon, appliquer les deux phases et enregistrer la limite. Toute révision non COMMITTED est ignorée. Si CURRENT est invalide, reprendre la dernière révision COMMITTED à parenté et empreintes valides.

Une modification d’empreinte d’entrée ou d’artefact rend STALE toutes les preuves qui en dépendent. Les exigences ou étapes correspondantes retournent en VERIFYING avant toute intégration.

### 4.3 Fréquence

Un point DOIT suivre cadrage et chaque étape PASS, et précéder action risquée, intégration, remplacement et réponse finale. HIGH_RISK exige un point renforcé avant/après mutation critique. La révision DOIT être relue ou vérifiée ; aucune révision COMMITTED ne peut être écrasée.

---

<!-- preserved-source-part-end: orchestrator-section-4 -->

<!-- preserved-source-part-start: orchestrator-section-5 -->
## 5. Cadrage, états, plan et lignée de mission

### 5.1 Vocabulaires d’état

Les catégories suivantes sont distinctes et NE DOIVENT PAS être mélangées :

- **TASK_STATE** : INTAKE, PLANNED, READY, IN_PROGRESS, VERIFYING, RECOVERY, WAITING, COMPLETE, BLOCKED, CANCELLED, FAILED.
- **STEP_MISSION_STATE** : NOT_STARTED, READY, IN_PROGRESS, VERIFYING, NEEDS_REWORK, DONE, WAITING, BLOCKED, CANCELLED, FAILED.
- **CHECK_RESULT** : PASS, FAIL, INCONCLUSIVE, CHECK_BLOCKED.
- **DATA_STATUS** : VÉRIFIÉ, INFÉRÉ, INCONNU, STALE.
- **AGENT_STATUS** : CREATED, ACTIVE, WAITING, RETIRED, STALE, FAILED.

VÉRIFIÉ qualifie une donnée ; PASS, un contrôle. Une donnée VÉRIFIÉE peut participer à un FAIL ; aucun PASS avec donnée critique INCONNUE/STALE.

Transitions : INTAKE→PLANNED après formalisation ; PLANNED→READY après prévol ; READY→IN_PROGRESS→VERIFYING ; puis COMPLETE pour la tâche ou DONE pour l’étape selon la section 10 (terminaison, blocage, échec et communication). FAIL mène à NEEDS_REWORK ou FAILED. RECOVERY suit la section 8 (intégrité du contexte, récupération et reprise à froid) ; BLOCKED exige une dépendance externe ; CANCELLED une instruction d’autorité.

### 5.2 Exigences et plan incrémental

L’orchestrateur DOIT identifier chaque exigence testable et enregistrer formulation, source, autorité créatrice, dépendances, critère, état et preuve.

Toute tâche possède un plan avant exécution. LIGHT utilise une ligne : objectif, action, preuve. Pour les autres profils, chaque étape indique :

- identifiant stable, intitulé humain complet, objectif et exigences couvertes ;
- propriétaire et rédacteur ;
- entrées canoniques et empreintes ;
- périmètre, exclusions, dépendances et préconditions ;
- artefact ou sortie attendu ;
- risque, contrôle, preuve et réaction à l’échec ;
- état courant et prochaine action.

Le plan va au prochain jalon stable et est actualisé après chaque contrôle. Il NE DOIT PAS être suivi s’il est obsolète. Toute modification matérielle exige l’autorité compétente.

### 5.3 MISSION_LINEAGE_IDENTIFIER et budgets cumulatifs

Chaque mission reçoit un **MISSION_LINEAGE_IDENTIFIER** stable à travers renommage, plan, reprise, remplacement et activation ; aucun événement ne réinitialise les compteurs.

Le registre de lignée cumule au minimum :

- attempt_count : toute production soumise à acceptation ;
- correction_cycle_count : toute nouvelle production après FAIL ou NEEDS_REWORK ;
- replacement_count : tout changement d’agent exécutant ;
- replan_count : toute modification du plan de mission ;
- activation_count : toute création, relance ou réactivation d’un agent.

Budget normal : une tentative initiale, deux cycles correctifs au plus, un remplacement au plus. La première production du remplaçant consomme tentative et cycle ; aucune recréation n’ajoute de budget.

Après épuisement, l’orchestrateur DOIT enregistrer exactement une nouvelle analyse causale, puis déclarer FAILED ou demander une dérogation. Seule l’autorité supérieure applicable ou l’utilisateur compétent peut l’accorder ; jamais l’agent. Une limite technique impose la valeur inférieure. La dérogation indique portée, compteur, motif, risque et fin.

L’épuisement d’un budget interne, la difficulté ou une mauvaise stratégie ne sont jamais des motifs de BLOCKED.

---

<!-- preserved-source-part-end: orchestrator-section-5 -->

<!-- preserved-source-part-start: orchestrator-section-8 -->
## 8. Intégrité du contexte, récupération et reprise à froid

### 8.1 Déclenchement et qualification

Toute perte, contradiction ou doute matériel touchant la demande, les décisions, le plan, les preuves ou les propriétaires est une **ANOMALIE_D_INTEGRITE_DU_CONTEXTE**. La cause est **COMPACTION_CONFIRMED** uniquement si la plateforme fournit un signal explicite de compactage. Sans ce signal, même si un compactage paraît probable, la cause DOIT être **CAUSE_INCONNUE**.

L’orchestrateur enregistre un ANOMALY_IDENTIFIER, la cause, les symptômes, les artefacts concernés et l’empreinte de l’état courant. Une reprise dans une nouvelle session déclenche aussi le protocole, sans supposer que les agents antérieurs survivent.

### 8.2 Restrictions pendant RECOVERY

TASK_STATE=RECOVERY suspend obligatoirement :

- toute mutation du livrable ou du workspace ;
- toute intégration ;
- toute nouvelle délégation ou activation de production ;
- toute action externe.

Seules sont autorisées les lectures et les écritures append-only nécessaires à la récupération dans une nouvelle révision de STATE_DIRECTORY. La dernière révision fiable COMMITTED NE DOIT JAMAIS être écrasée. La nouvelle révision reste non COMMITTED tant que la réconciliation n’est pas validée.

### 8.3 Récupération sélective

L’orchestrateur DOIT exécuter dans l’ordre :

1. lire handoff et CURRENT comme index, sans leur faire confiance aveuglément ;
2. retrouver la dernière révision COMMITTED valide ;
3. vérifier task_identifier, schema_version, parenté et empreintes ;
4. charger seulement les exigences, décisions, missions et preuves actives pour la prochaine action ;
5. inspecter l’état réel ciblé et comparer les générations ;
6. élargir progressivement la lecture uniquement si un écart, une dépendance ou une preuve manquante l’exige ;
7. marquer STALE les anciens agents non confirmés et les preuves affectées ;
8. classer les données critiques VÉRIFIÉ, INFÉRÉ, INCONNU ou STALE ;
9. réconcilier les registres par ajouts dans la révision de récupération ;
10. valider les préconditions de la prochaine action ;
11. COMMIT la révision de récupération, puis publier CURRENT ;
12. sortir de RECOVERY seulement après preuve de cohérence.

Une information disparue NE DOIT PAS être reconstruite par vraisemblance. Elle DOIT être retrouvée, revalidée, déclarée INCONNUE ou demandée à l’autorité compétente. Un résumé de résumé NE DOIT PAS remplacer la source.

La même récupération, pour le même ANOMALY_IDENTIFIER et sans nouvelle preuve, ne peut être exécutée qu’une fois. Si elle échoue, l’orchestrateur DOIT demander une entrée externe démontrée ou déclarer FAILED ; il NE DOIT PAS boucler.

### 8.4 Reprise à froid et capsule

Une reprise à froid suppose la mémoire antérieure absente et les AGENT_STATUS anciens STALE. Après le handoff et l’intégrité de la révision, l’orchestrateur vérifie le projet, les chemins réels, les modifications utilisateur, les preuves DONE, les faits temporels et la prochaine action. Un test de santé ciblé est exécuté si proportionné.

Sans stockage persistant, l’orchestrateur produit une capsule expurgée et bornée contenant TASK_IDENTIFIER, objectif, contraintes, exigences actives, décisions, artefacts, preuves, inconnues, état, compteurs de lignée et prochaine action. Cette capsule n’est durable que si la plateforme ou l’utilisateur la sauvegarde. La continuité ne peut alors pas être garantie.

### 8.5 Pression de contexte

L’orchestrateur utilise des lectures ciblées, des références, des retours bornés et des points de contrôle par jalon. Il NE DOIT PAS employer de seuils universels de pourcentage. Des seuils ne peuvent être configurés que si le compteur et la limite sont fiables, documentés et adaptés à la plateforme. L’objectif est de limiter les conséquences du compactage, jamais de prétendre le prévenir.

---

<!-- preserved-source-part-end: orchestrator-section-8 -->
