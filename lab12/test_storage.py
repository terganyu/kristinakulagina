import unittest
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from storage import load_records, save_records, validate_records

class TestStorage(unittest.TestCase):

    def test_load_empty_file(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "data.json"
            path.write_text("[]", encoding="utf-8")
            records = load_records(path)
            self.assertEqual(records, [])

    def test_save_and_load(self):
        test_data = [
            {"id": 1, "title": "Тест", "category": "Категория", "amount": 100, "completed": False}
        ]
        with TemporaryDirectory() as directory:
            path = Path(directory) / "test.json"
            save_records(path, test_data)
            loaded = load_records(path)
            self.assertEqual(loaded, test_data)

    def test_validate_correct_data(self):
        correct_data = [
            {"id": 1, "title": "Книга", "category": "Жанр", "amount": 200, "completed": False}
        ]
        validate_records(correct_data)  # Не должно вызвать исключения

    def test_validate_invalid_id(self):
        invalid_data = [{"id": -1, "title": "Книга", "category": "Жанр", "amount": 200, "completed": False}]
        with self.assertRaises(ValueError):
            validate_records(invalid_data)

if __name__ == "__main__":
    unittest.main()
