import json
import mysql.connector
from flask import Flask, request
import os
from functions_db_to_typesense import export_table_to_jsonl, create_collection_and_import_data, search9mois
from dotenv import load_dotenv

app = Flask(__name__)

# Create json files from database and import them into Typesense
@app.route("/9moisacroquer/UpdateCollection", methods=['GET'])
def update_collection():
    table_name = request.args.get('table_name')
    try:
        export_table_to_jsonl(table_name)
        # Chemin du dossier contenant les fichiers JSONL
        jsonl_folder_path = "jsonl_files"
        # Liste des fichiers dans le dossier json_files et appel de la fonction
        for filename in os.listdir(jsonl_folder_path):
            if filename.endswith('.jsonl'):
                file_path = os.path.join(jsonl_folder_path, filename)
                create_collection_and_import_data(file_path)
        return json.dumps({"Success": "Table updated"})
    except Exception as e:
        return json.dumps({"Error": str(e)})

# Search a query in Collection
@app.route("/9moisacroquer/SearchCollection", methods=['GET'])
def search_collection():
    query = request.args.get('query')
    try:
        search9mois(query)
        return json.dumps({"Success": "Query results"})
    except Exception as e:
        return json.dumps({"Error": str(e)})

if __name__ == '__main__':
    app.run(debug=True) 

