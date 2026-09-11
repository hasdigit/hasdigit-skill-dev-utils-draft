# Pages publiques, métadonnées et internationalisation

Lire ce document pour toute page publique, domaine personnalisé, marque, langue, métadonnée, image de partage, plan de site ou règle d’indexation.

## Classifier la page

Avant toute décision, classer la route :

- publique et destinée à être indexée ;
- publique mais exclue de l’indexation ;
- privée derrière une session ;
- propre à une organisation cliente ;
- propre à une langue ou une région ;
- temporaire, prévisualisée ou non canonique.

Cette classification détermine le rendu, le cache, l’adresse canonique, les métadonnées et les contrôles de confidentialité.

## Contenu initial utile

Une page publique destinée aux moteurs de recherche doit fournir son contenu principal dans le document HTML initial, le langage de structure envoyé par le serveur. Ne pas dépendre uniquement d’un chargement navigateur pour le titre, la description ou le contenu essentiel.

Le rendu initial doit correspondre à la bonne organisation, à la bonne marque, à la bonne langue et à la bonne adresse. Tester la réponse réellement produite, pas seulement l’apparence après navigation côté client.

## Métadonnées

Utiliser l’objet statique, la fonction `generateMetadata` ou les fichiers spéciaux de Next.js selon la variabilité réelle.

Chaque page publique indexable doit définir lorsque pertinent :

- titre unique et descriptif ;
- description utile ;
- adresse canonique absolue ;
- langue et variantes disponibles ;
- directives d’indexation ;
- image et texte de partage ;
- icônes de marque ;
- données structurées correspondant au contenu visible.

Les métadonnées sont produites côté serveur. Elles ne doivent contenir ni secret, ni donnée de session, ni information appartenant à une autre organisation cliente.

Le titre sert aussi à l’annonce des navigations par les technologies d’assistance. Il doit décrire la destination avant le nom de marque générique.

## Domaines et marques multiples

Résoudre le domaine avec une liste de domaines autorisés. Ne pas faire confiance sans validation à l’en-tête d’hôte transmis par une infrastructure intermédiaire.

Pour chaque organisation ou marque :

- valider le domaine canonique ;
- résoudre logo, couleurs, nom public et coordonnées ;
- définir les langues autorisées ;
- isoler les caches de page et de métadonnées ;
- empêcher le repli silencieux vers la marque d’une autre organisation ;
- prévoir un thème sûr si la configuration est invalide.

Une adresse canonique ne doit pas être construite depuis une valeur non vérifiée. Les environnements de prévisualisation ne doivent pas devenir canoniques par accident.

## Images de partage et icônes

Les images générées pour les réseaux sociaux sont des réponses publiques et potentiellement mises en cache.

- Utiliser uniquement des données publiques autorisées.
- Isoler la clé par marque, langue, route et version de contenu.
- Définir dimensions, texte de remplacement et solution de repli.
- Restreindre les images distantes à des sources approuvées.
- Tester une erreur de police, d’image ou de donnée.
- Vérifier qu’une ancienne marque ne reste pas visible après une modification.

## Plan de site et règles d’indexation

Le plan de site doit contenir uniquement les adresses canoniques publiques réellement accessibles. Ne jamais y inclure un espace privé, une prévisualisation, un jeton ou une adresse propre à une session.

Pour un grand nombre de pages, répartir les plans de site selon une responsabilité stable et vérifier les limites des consommateurs. Une date de modification doit provenir d’un changement réel, pas de l’heure de chaque construction.

Les règles `robots.txt` orientent les robots coopératifs. Elles ne protègent aucune donnée privée. La protection repose sur l’autorisation serveur.

## Données structurées

Les données structurées doivent :

- correspondre au contenu visible ;
- être sérialisées sans insertion de contenu dangereux ;
- utiliser des adresses absolues validées ;
- respecter la langue et la marque actives ;
- éviter toute donnée personnelle non nécessaire ;
- être testées dans le document final.

Ne pas inventer une note, un prix, une disponibilité ou une relation uniquement pour enrichir l’affichage dans un moteur de recherche.

## Routage par langue

Une langue est un ensemble de préférences linguistiques et de formatage. Définir :

- les langues prises en charge ;
- la langue par défaut ;
- la stratégie d’adresse ;
- la détection initiale ;
- le changement volontaire par l’utilisateur ;
- le comportement pour une langue invalide ;
- les liens entre variantes.

Lorsque la langue fait partie de l’adresse, valider le segment avant de charger des ressources. Une redirection fondée sur les préférences du navigateur doit rester prévisible et ne pas créer de boucle.

Le choix explicite de l’utilisateur doit primer sur une nouvelle détection automatique selon la politique du produit.

## Traductions et formatage

- Centraliser les messages selon un mécanisme versionné.
- Utiliser des clés descriptives liées au sens, pas à la position visuelle.
- Détecter les traductions absentes pendant les contrôles automatisés.
- Prévoir les pluriels et variables selon la langue.
- Utiliser les fonctions de formatage pour dates, nombres, devises et fuseaux horaires.
- Définir la langue et la direction du document.
- Tester les textes plus longs et les écritures de droite à gauche lorsqu’elles sont prises en charge.

Ne pas construire une phrase traduite par concaténation de fragments dont l’ordre dépend du français.

## Cache et invalidation

La clé de cache d’un contenu public variable doit inclure toutes les dimensions qui modifient le résultat : route, langue, marque, domaine ou version publiée.

Après un changement de contenu, de traduction ou de marque :

1. invalider les pages concernées ;
2. invalider les métadonnées et images de partage concernées ;
3. vérifier au moins deux langues et deux marques lorsque le produit les prend en charge ;
4. confirmer qu’aucune réponse d’une organisation ne fuit vers une autre.

## Contrôles obligatoires

- document HTML initial sans exécution du code navigateur ;
- navigation directe et navigation côté client ;
- titre, description, adresse canonique et directives d’indexation ;
- plan de site et règles pour les robots ;
- image de partage et icônes ;
- données structurées ;
- domaine autorisé et domaine falsifié ;
- langue par défaut, autre langue et langue invalide ;
- formatage de date, nombre, devise et fuseau horaire ;
- deux marques successives sur le même serveur ;
- cache froid, cache chaud et invalidation ;
- absence de donnée privée dans les réponses publiques.

## Sources officielles

- [Métadonnées et images de partage Next.js](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)
- [Internationalisation avec Next.js](https://nextjs.org/docs/app/guides/internationalization)
- [Convention de plan de site Next.js](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
