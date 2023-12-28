import mysql.connector
import json
import os
from datetime import date, datetime
import requests
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

def json_serial(obj):
    """Fonction d'aide pour sérialiser les objets date et datetime en JSON."""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def export_table_to_jsonl(table_name):
    # Connexion à la base de données MySQL
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=os.getenv("DB_PORT")  # Ajout du port ici
    )
    cursor = conn.cursor()

    # Obtenir les noms des colonnes de la table
    cursor.execute(f"DESCRIBE {table_name}")
    columns = [column[0] for column in cursor.fetchall()]

    # Exécuter la requête pour extraire les données
    cursor.execute(f"SELECT * FROM {table_name}")

    # Créer et ouvrir le fichier JSONL
    with open(f"jsonl_files/{table_name}.jsonl", "w") as file:
        for row in cursor:
            # Structurer la ligne en utilisant les noms des colonnes
            data = dict(zip(columns, row))

            # Renommer les champs
            if 'id' in data:
                data['el_id'] = data.pop('id')
            if 'question' in data:
                data['title'] = data.pop('question')
            if 'name' in data:
                data['title'] = data.pop('name')
            if 'answer' in data:
                data['content'] = data.pop('answer')
            if 'review' in data:
                data['content'] = data.pop('review')

            # Écrire la ligne JSON dans le fichier, en utilisant json_serial pour les dates
            file.write(json.dumps(data, default=json_serial) + "\n")

    # Fermer la connexion
    cursor.close()
    conn.close()


# Exemple d'utilisation de la fonction
export_table_to_jsonl("recipes")
export_table_to_jsonl("articles")
export_table_to_jsonl("food")
export_table_to_jsonl("questions")
export_table_to_jsonl("recommendations")
