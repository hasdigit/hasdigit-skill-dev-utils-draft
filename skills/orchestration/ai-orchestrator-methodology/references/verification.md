# Vérification, preuves et conformité

Lire cette référence pour qualifier une information, vérifier une étape, décider d’une intégration ou évaluer la conformité et la terminaison.

<!-- preserved-source-part-start: orchestrator-section-7 -->
## 7. Données vérifiées, preuve par étape et fraîcheur

### 7.1 Qualification des données

Une donnée n’est VÉRIFIÉE qu’après examen proportionné de :

- sa provenance identifiable ;
- l’autorité de la source pour l’affirmation concernée ;
- sa fraîcheur au moment d’usage ;
- son intégrité ou son empreinte si disponible ;
- sa corroboration lorsque le risque, l’ambiguïté ou la faiblesse de la source l’exige.

Une source primaire et directement autoritative peut suffire seule si ce choix est justifié. Une conclusion fondée mais non directement observée est INFÉRÉE. Une information manquante ou contradictoire est INCONNUE. Une preuve dont l’entrée, l’artefact, l’autorité ou la fraîcheur a changé est STALE.

Chaque statut DOIT pointer vers sa provenance et sa date fiable, ou indiquer UNAVAILABLE. L’orchestrateur NE DOIT PAS promouvoir INFÉRÉ, INCONNU ou STALE en VÉRIFIÉ sans nouvelle vérification.

### 7.2 Porte après chaque étape

À la fin de chaque étape, l’exécutant fournit sa preuve et l’orchestrateur contrôle :

1. le livrable attendu ;
2. le périmètre et la génération des entrées ;
3. chaque critère d’acceptation concerné ;
4. les effets secondaires et données sensibles ;
5. les hypothèses, lacunes et informations STALE ;
6. la reproductibilité ou la traçabilité de la preuve ;
7. la mise à jour transactionnelle de l’état.

Le CHECK_RESULT est PASS, FAIL, INCONCLUSIVE ou CHECK_BLOCKED. Seul PASS autorise STEP_MISSION_STATE=DONE. FAIL mène à NEEDS_REWORK dans le budget restant ou à FAILED. INCONCLUSIVE impose une preuve supplémentaire ou une décision d’autorité. CHECK_BLOCKED n’autorise STEP_MISSION_STATE=BLOCKED que si la condition externe de la section 10 (terminaison, blocage, échec et communication) est démontrée.

Une preuve peut être une sortie de test, un diff inspecté, une mesure reproductible, une référence source précise, une requête de lecture ou une inspection structurée. Une affirmation de l’auteur n’est pas une preuve. La vérification finale ne remplace aucune porte intermédiaire.

### 7.3 Fraîcheur et changement de génération

Juste avant intégration et avant réutilisation d’une preuve matérielle, l’orchestrateur DOIT vérifier les empreintes ou générations actives. Tout changement marque les preuves dépendantes STALE, réouvre les étapes concernées en VERIFYING et interdit COMPLETE jusqu’à revalidation.

Pour une information temporellement instable, la fraîcheur requise dépend du risque et du besoin utilisateur. Une date ancienne ou inconnue est signalée ; l’orchestrateur NE DOIT PAS présenter comme actuelle une donnée non actualisée.

---

<!-- preserved-source-part-end: orchestrator-section-7 -->

<!-- preserved-source-part-start: orchestrator-section-11 -->
## 11. Matrice de conformité

STANDARD et HIGH_RISK exigent cette matrice à chaque porte concernée et avant état terminal. LIGHT applique seulement les lignes pertinentes à son action et à sa preuve.

| Identifiant | Contrôle | Preuve minimale | Échec |
|---|---|---|---|
| C-01 | Autorité, profil et risque | Hiérarchie native, profil et justification | Suspendre et recadrer. |
| C-02 | Prévol, expertise et STATE_DIRECTORY | Capacités, lacunes, chemins réels | Appliquer repli ou INCONNU. |
| C-03 | Protection des données | Classification, expurgation, permissions, rétention | Interdire persistance ou délégation. |
| C-04 | État transactionnel | Révision, parent, empreintes, COMMITTED, CURRENT | Revenir au dernier COMMITTED. |
| C-05 | Exigences, plan et lignée | Critères, étapes, MISSION_LINEAGE_IDENTIFIER, compteurs | Corriger avant production. |
| C-06 | Délégation à valeur nette | DELEGATE ou LOCAL justifié, contrat complet | Ne pas activer la mission. |
| C-07 | Écriture et intégration | Rédacteur, chemin réel, génération, diff | Refuser ou rebaser. |
| C-08 | Statuts et provenance | Catégories séparées, autorité, fraîcheur | Requalifier, marquer STALE. |
| C-09 | Vérification par étape | CHECK_RESULT et preuve liée | NEEDS_REWORK, INCONCLUSIVE ou FAILED. |
| C-10 | Intégrité du contexte | ANOMALY_IDENTIFIER, cause correcte, récupération sélective | Maintenir RECOVERY. |
| C-11 | Budget et garde-fous | Compteurs cumulatifs, données protégées, contrôles | Analyse causale ou suspension. |
| C-12 | COMPLETE | Toutes preuves obligatoires PASS ou renonciation formelle | Interdire COMPLETE. |
| C-13 | BLOCKED | BLOCKER_IDENTIFIER, condition externe, action de déblocage | Employer WAITING ou FAILED. |
| C-14 | Handoff et clôture | Révision/capsule, prochaine action, rétention | Corriger avant remise. |
| C-15 | Langage accessible, noms complets et références auto-explicatives | Noms sans abréviation contrôlée ; chaque code ou référence accompagné de son intitulé et de son explication ; contrat de sous-agent conforme | Reformuler et renvoyer en révision avant transmission. |

---

<!-- preserved-source-part-end: orchestrator-section-11 -->
