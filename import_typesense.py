import os
import json
import requests
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Configuration de Typesense
TYPESENSE_API_KEY = os.getenv("TYPESENSE_API_KEY")
TYPESENSE_HOST = os.getenv("TYPESENSE_HOST")

def infer_types_from_jsonl_line(line):
    data = json.loads(line)
    schema = []

    for key, value in data.items():
        if isinstance(value, int):
            field_type = "int32"  # ou "int64" si nécessaire
        elif isinstance(value, float):
            field_type = "float"
        elif isinstance(value, bool):
            field_type = "bool"
        else:
            field_type = "string"  # Par défaut

        schema.append({"name": key, "type": field_type})

    return schema

def create_collection_and_import_data(jsonl_file_path):
    # Déterminer le nom de la collection à partir du nom du fichier
    collection_name = os.path.basename(jsonl_file_path).split('.')[0]

    # Lire les premières lignes du fichier pour déterminer les fields
    with open(jsonl_file_path, 'r') as file:
        first_line = file.readline()
        fields = infer_types_from_jsonl_line(first_line)

    # Supprimer la collection si elle existe déjà
    requests.delete(f"{TYPESENSE_HOST}/collections/{collection_name}",
                    headers={"X-TYPESENSE-API-KEY": TYPESENSE_API_KEY})

    # Créer une nouvelle collection avec le schéma déterminé
    schema = {"name": collection_name, "fields": fields}
    requests.post(
        f"{TYPESENSE_HOST}/collections",
        headers={"X-TYPESENSE-API-KEY": TYPESENSE_API_KEY, "Content-Type": "application/json"},
        json=schema
    )

    # Importer les données dans la collection
    with open(jsonl_file_path, 'r') as file:
        documents = file.read()
    

    response = requests.post(
        f"{TYPESENSE_HOST}/collections/{collection_name}/documents/import",
        headers={"X-TYPESENSE-API-KEY": TYPESENSE_API_KEY, "Content-Type": "text/plain"},
        data=documents
    )
    print(f"Importé dans {collection_name}: {response.status_code}")




# Chemin du dossier contenant les fichiers JSONL
jsonl_folder_path = "jsonl_files"

# Liste des fichiers dans le dossier json_files et appel de la fonction
for filename in os.listdir(jsonl_folder_path):
    if filename.endswith('.jsonl'):
        file_path = os.path.join(jsonl_folder_path, filename)
        create_collection_and_import_data(file_path)



