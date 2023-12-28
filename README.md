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

### Script d'Initialisation
Le script search_engine_init.py joue un rôle crucial en initialisant le moteur de recherche avec des données pertinentes. Il exporte les données de MySQL, les convertit au format JSONL, et les importe dans Typesense.

### Fonctions d'Intégration
functions_db_to_typesense.py contient des fonctions essentielles pour exporter les données de MySQL, inférer les schémas de données, et importer ces données dans Typesense, assurant ainsi une intégration fluide.

### Utilisation
[Instructions sur la façon d'utiliser le projet, y compris la mise en place de l'environnement, l'exécution des scripts, et toute autre étape nécessaire.]

### Contribution
[Informations sur la façon de contribuer au projet, y compris les directives de contribution, le processus de soumission des pull requests, etc.]

### Licence
[Informations sur la licence sous laquelle le projet est distribué.]