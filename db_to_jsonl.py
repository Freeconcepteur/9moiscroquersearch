import mysql.connector
import json
import os
from datetime import date, datetime
import requests


# Exemple d'utilisation de la fonction
export_table_to_jsonl("recipes")
export_table_to_jsonl("articles")
export_table_to_jsonl("food")
export_table_to_jsonl("questions")
export_table_to_jsonl("recommendations")
