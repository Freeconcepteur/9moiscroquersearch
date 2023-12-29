import unittest
import pathlib as pl
import json
import os
import sys
import requests
import mysql.connector
from mysql.connector.errors import InterfaceError

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PARENT_DIR)

from functions_db_to_typesense import export_table_to_jsonl, infer_types_from_jsonl_line, create_collection_and_import_data
from dotenv import load_dotenv



class TestCaseBase(unittest.TestCase):
    """TestCaseBase Class that extends unittest.TestCase"""

    def assertIsFile(self, path):
        """Do a validation test over a pathFile, return a AssertionError if the file doesn't exists"""
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))
class TestTypeSense(TestCaseBase):
    """TestTypeSense Class that extends TestCaseBase"""

    def test_load_dotenv(self):
        """Do a validation test over .env to check if all environment variables were loaded"""
        result = load_dotenv()
        self.assertTrue(result)
    
    def test_mysql_connection(self):
        """ Do a validation test over the mysql connection """
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT") 
        )
        cursor = conn.cursor()
        
        self.assertNotEqual(InterfaceError, conn.ping())

    def test_table_to_json(self):
        """
        Do a validation test over functions_db_to_typesense.export_table_to_jsonl
        to check if the all the json files are created at the end of the execution.
        """
        tables = ['recipes', 'articles', 'food', 'questions',
                  'recommendations']
        for table in tables:
            export_table_to_jsonl(table)
            path = pl.Path(f"jsonl_files/{table}.jsonl")
            self.assertIsFile(path)
    
    def test_infer_types_from_jsonl_line(self):
        """
        Do a validation test over functions_db_to_typesense.infer_types_from_jsonl_line
        to check if the types are correctly infered.
        """
        result = infer_types_from_jsonl_line(json.dumps({"title": "Article de test"}))
        self.assertEqual([{"name": "title", "type": "string"}], result)

    def test_create_collection_and_import_data(self):
        """
        Do a validation test over functions_db_to_typesense.create_collection_and_import_data
        to check if TypeSense collection are correcly loaded.
        """
        tables = ['recipes', 'articles', 'food', 'questions',
            'recommendations']
        for table in tables:
            result = create_collection_and_import_data(f"jsonl_files/{table}.jsonl")
            self.assertIsNone(result)
        
    def test_update_collection(self):
        """ Do a validation test over test_update_collection in Flask Server """
        result = requests.get(
            "http://localhost:5000/9moisacroquer/UpdateCollection",
            params={"table_name": 'food'}
        )
        self.assertTrue(result.ok)

if __name__ == "__main__":
    unittest.main()