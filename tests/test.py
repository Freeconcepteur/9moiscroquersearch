import unittest
import pathlib as pl
import json
from functions_db_to_typesense import export_table_to_jsonl, infer_types_from_jsonl_line, create_collection_and_import_data

class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))
class TestTypeSense(TestCaseBase):
    def test_table_to_json(self):
        tables = ['recipes', 'articles', 'food', 'questions',
                  'recommendations']
        for table in tables:
            export_table_to_jsonl(table)
            path = pl.Path(f"jsonl_files/{table}.jsonl")
            self.assertIsFile(path)
    
    def test_infer_types_from_jsonl_line(self):
        result = infer_types_from_jsonl_line(json.dumps({"title": "Article de test"}))
        self.assertEqual([{"name": "title", "type": "string"}], result)

    def test_create_collection_and_import_data(self):
        tables = ['recipes', 'articles', 'food', 'questions',
            'recommendations']
        for table in tables:
            result = create_collection_and_import_data(f"jsonl_files/{table}.jsonl")
            self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()