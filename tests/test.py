import unittest
from db_to_jsonl import json_serial, export_table_to_jsonl
from import_typesense import infer_types_from_jsonl_line, create_collection_and_import_data

class TestLoadMeiliSearch(unittest.TestCase):
    def test_tablet_to_json_recipes(self):
        result = json_serial()
        self.assertEqual(result, ['a'])
    

if __name__ == "__main__":
    unittest.main()