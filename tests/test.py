import unittest
import pathlib as pl
from functions_db_to_typesense import json_serial, export_table_to_jsonl, infer_types_from_jsonl_line, create_collection_and_import_data

class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))
class TestLoadMeiliSearch(unittest.TestCase):
    def test_tablet_to_json_recipes(self):
        json_serial('recipes')
        path = pl.Path("jsonl_files/recipes.jsonl")
        self.assertIsFile(path)
    

if __name__ == "__main__":
    unittest.main()