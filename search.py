import requests
import json
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis .env
load_dotenv()

# Configuration de Typesense
TYPESENSE_API_KEY = os.getenv("TYPESENSE_API_KEY")
TYPESENSE_HOST = os.getenv("TYPESENSE_HOST")

def search9mois(query):
    # Fonction pour effectuer une recherche sur toutes les collections dans Typesense.

    typesense_api_key = TYPESENSE_API_KEY
    typesense_host = TYPESENSE_HOST

    # Obtenir la liste des collections
    collections_response = requests.get(
        f"{typesense_host}/collections",
        headers={"X-TYPESENSE-API-KEY": typesense_api_key}
    )
    collections = json.loads(collections_response.text)

    # Recherche dans chaque collection
    results = {}
    for collection in collections:
        collection_name = collection['name']
        search_response = requests.get(
            f"{typesense_host}/collections/{collection_name}/documents/search",
            params={"q": query, "query_by": "*"},
            headers={"X-TYPESENSE-API-KEY": typesense_api_key}
        )
        results[collection_name] = json.loads(search_response.text)

    return results

# Utilisation de la fonction

query = "chocolat"
search_results = search9mois(query)

# Affichage des résultats
print(search_results)