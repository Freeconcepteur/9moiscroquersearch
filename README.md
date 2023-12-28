# 9moiscroquersearch
## Projet de Recherche Optimisée avec Typesense et MySQL

### Introduction
Ce projet propose une solution innovante pour l'amélioration des fonctionnalités de recherche dans les applications, en combinant la puissance d'une base de données MySQL avec la rapidité et la flexibilité du moteur de recherche Typesense. Conçu pour offrir une expérience utilisateur améliorée, ce système intègre des technologies avancées pour une récupération rapide et précise des données.

### Caractéristiques
Intégration Typesense-MySQL: Synchronisation des données entre MySQL et Typesense pour une recherche optimisée.
Infrastructure Dockerisée: Utilisation de Docker pour une mise en place et un déploiement aisés du moteur de recherche Typesense.
Automatisation du Processus de Recherche: Scripts pour l'initialisation automatique et la mise à jour des données de recherche dans Typesense.
Composants

### Docker Compose
Le fichier docker-compose.yml facilite la configuration et le déploiement du service Typesense dans un environnement Docker. Cette approche garantit une configuration consistante et une portabilité accrue.

https://typesense.org/docs/guide/install-typesense.html#docker

```json
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

In both cases, after create the docker-compose.yml, you have to create the typesense-data directory and execute the docker-compose.

```sh
mkdir $(pwd)/typesense-data

docker-compose up
```

### Python Libraries

```pip install -r requirements.txt```

### Fichiers de configuration
Vous devez modifier le fichier de configuration situé dans __.env__ avec les informations de votre base de données et de votre serveur typesense.

### Script d'Initialisation
Le script __search_engine_init.py__ joue un rôle crucial en initialisant le moteur de recherche avec des données pertinentes. Il exporte les données de MySQL, les convertit au format JSONL, et les importe dans Typesense.

Dans __search_engine_init.py__, vous devez modifier les tables qui seront chargées dans typesense server.

```py
export_table_to_jsonl("recettes")
export_table_to_jsonl("articles")
export_table_to_jsonl("food")
export_table_to_jsonl("questions")
export_table_to_jsonl("recommandations")
```

### Fonctions d'Intégration
__functions_db_to_typesense.py__ contient des fonctions essentielles pour exporter les données de MySQL, inférer les schémas de données, et importer ces données dans Typesense, assurant ainsi une intégration fluide.

- __export_table_to_jsonl()__ : convertir la table sélectionnée et ses champs au format JSON.
- __create_collection_and_import_data()__ : Charger la base de données au format JSON dans la structure d’index Typesense.

### Flask Server

### Utilisation
[Instructions sur la façon d'utiliser le projet, y compris la mise en place de l'environnement, l'exécution des scripts, et toute autre étape nécessaire.]

### Contribution
[Informations sur la façon de contribuer au projet, y compris les directives de contribution, le processus de soumission des pull requests, etc.]

### Licence
[MIT](https://choosealicense.com/licenses/mit/)
