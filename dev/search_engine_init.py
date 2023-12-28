from dotenv import load_dotenv
import os
from functions_db_to_typesense import export_table_to_jsonl, create_collection_and_import_data


# Charger les variables d'environnement depuis .env
load_dotenv()

# Configuration de Typesense
TYPESENSE_API_KEY = os.getenv("TYPESENSE_API_KEY")
TYPESENSE_HOST = os.getenv("TYPESENSE_HOST")

# Génération des fihciers JSONL
export_table_to_jsonl("recipes")
export_table_to_jsonl("articles")
export_table_to_jsonl("food")
export_table_to_jsonl("questions")
export_table_to_jsonl("recommendations")

# Chemin du dossier contenant les fichiers JSONL
jsonl_folder_path = "jsonl_files"

# Liste des fichiers dans le dossier json_files et appel de la fonction
for filename in os.listdir(jsonl_folder_path):
    if filename.endswith('.jsonl'):
        file_path = os.path.join(jsonl_folder_path, filename)
        create_collection_and_import_data(file_path)