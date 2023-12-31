# 9moiscroquersearch
## Projet de Recherche Optimisée avec Typesense et MySQL

![Moteur de recherche](Images/engine.png)


## Introduction
Ce projet propose une solution innovante pour l'amélioration des fonctionnalités de recherche dans les applications, en combinant la puissance d'une base de données MySQL avec la rapidité et la flexibilité du moteur de recherche Typesense. Conçu pour offrir une expérience utilisateur améliorée, ce système intègre des technologies avancées pour une récupération rapide et précise des données.

## Caractéristiques
Intégration Typesense-MySQL: Synchronisation des données entre MySQL et Typesense pour une recherche optimisée.
Infrastructure Dockerisée: Utilisation de Docker pour une mise en place et un déploiement aisés du moteur de recherche Typesense.
Automatisation du Processus de Recherche: Scripts pour l'initialisation automatique et la mise à jour des données de recherche dans Typesense.
Composants

## Docker Compose
Le fichier docker-compose.yml facilite la configuration et le déploiement du service Typesense dans un environnement Docker. Cette approche garantit une configuration consistante et une portabilité accrue.

https://typesense.org/docs/guide/install-typesense.html#docker

```py
version: '3.4'
services:
  typesense:
    image: typesense/typesense:0.25.1
    restart: on-failure
    ports:
      - "8108:8108"
    volumes:
      - ./typesense-data:/data
    command: '--data-dir /data --api-key=<API KEY> --enable-cors'
```

Dans les deux cas, après avoir créé le docker-compose.yml, vous devez créer le répertoire typesense-data et exécuter le docker-compose.

```sh
mkdir $(pwd)/typesense-data

docker-compose up
```

## Python Libraries

```pip install -r requirements.txt```

## Fichiers de configuration
Vous devez modifier le fichier de configuration situé dans __.env__ avec les informations de votre base de données et de votre serveur typesense.

## Script d'Initialisation
Le script __search_engine_init.py__ joue un rôle crucial en initialisant le moteur de recherche avec des données pertinentes. Il exporte les données de MySQL, les convertit au format JSONL, et les importe dans Typesense.

Dans __search_engine_init.py__, vous devez modifier les tables qui seront chargées dans typesense server.

```py
export_table_to_jsonl("recettes")
export_table_to_jsonl("articles")
export_table_to_jsonl("food")
export_table_to_jsonl("questions")
export_table_to_jsonl("recommandations")
```

## Fonctions d'Intégration
__functions_db_to_typesense.py__ contient des fonctions essentielles pour exporter les données de MySQL, inférer les schémas de données, et importer ces données dans Typesense, assurant ainsi une intégration fluide.

- __export_table_to_jsonl()__ : convertir la table sélectionnée et ses champs au format JSON.
- __create_collection_and_import_data()__ : Charger la base de données au format JSON dans la structure d’index Typesense.

## Flask Server

### Utilisation
Pour lancer le server flask, il faut entrer la ligne de commande ci-dessous dans le terminal:
```sh
flask --app server.py --debug run
```
Le server flask permet de configurer des routes (url) qui vont être utilisée:

* soit pour charger une table,
exemple: 
Pour charger la table food on va taper:
http://localhost:5000/9moisacroquer/UpdateCollection?table_name=food

* soit pour effectuer une recherche:
exemple:
on entre dans la barre de recherche les termes à rechercher et le serveur va faire plusieurs requêtes dans les tables, préalablement chargées, à l'adresse suivante:
http://localhost:5000/9moisacroquer/SearchCollection
si les termes sont: carences en fer, il va rechercher tous les textes contenant "fer", "carences" et "carences fer".

### Structure de réponse SearchCollection:
```py
{
  "recommendations": { # Nom de la table
    "facet_counts": [],
    "found": 1,
    "hits": [
      {
        "document": { # Colonnes de la table
          "description": "Si vous faites votre mayonnaise maison (contient des oeufs crus), consommez cet aliment dans les heures qui suivent sa préparation.\n            Si vous l'achetez en version industrielle, veillez à bien respecter les dates de consommation et consommez-le directement après ouverture.\n            Vous pouvez également essayer notre recette de mayonnaise sans oeuf.",
          "el_id": 20,
          "id": "19",
          "img": "/images/recommandations/autorise_mais.png",
          "status": "autorise_mais",
          "title": "plat_mayo"
        },
        "highlight": { # Highlight extrait exactement la partie du texte où le terme recherché a été trouvé
          "description": {
            "matched_tokens": [
              "recette"
            ], # L'extrait
            "snippet": "pouvez également essayer notre <mark>recette</mark> de mayonnaise sans oeuf."
          }
        },
        "highlights": [ # Highlight extrait exactement la partie du texte où le terme recherché a été trouvé
          {
            "field": "description",
            "matched_tokens": [
              "recette"
            ], # L'extrait
            "snippet": "pouvez également essayer notre <mark>recette</mark> de mayonnaise sans oeuf."
          }
        ], # text_match représente le score
        "text_match": 578730123365187700,
        "text_match_info": {
          "best_field_score": "1108091338752",
          "best_field_weight": 15,
          "fields_matched": 1,
          "score": "578730123365187705",
          "tokens_matched": 1
        }
      }
    ],
    "out_of": 63,
    "page": 1,
    "request_params": {
      "collection_name": "recommendations",
      "per_page": 10,
      "q": "recette kiwi"
    },
    "search_cutoff": false,
    "search_time_ms": 5
  },
```


## Tests
Pour exécuter les tests :

```py
python tests/test.py
```

### Demo
Pour l’exécution de la démonstration suffit d’ouvrir la page ci-dessous dans un navigateur:

``` demo_html/search.html ```

## Contribution
Les fiers participants sont:
* [Jhonatan Caldeira](https://github.com/JhonatanCaldeira)
* [Cedric Lagrand'court](https://github.com/Freeconcepteur)
* [Joachim Lombardi](https://github.com/JoachimLombardi)
* [Mhoudini Saïd](https://github.com/mhoudini)

Avec l'aimable participation des formateurs:
* [Adrien Dulac](https://github.com/dtrckd)
* [Antonys Schultz](https://github.com/DeVerMyst)

## Licence
[MIT](https://choosealicense.com/licenses/mit/)
