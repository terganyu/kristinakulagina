import unittest
from logic import add_record, find_records, set_completed, delete_record, statistics

class TestLogic(unittest.TestCase):
    def setUp(self):
        self.records = [
            {"id": 1, "title": "Книга 1", "category": "Фантастика", "amount": 200, "completed": False},
            {"id": 2, "title": "Книга 2", "category": "Детектив", "amount": 300, "completed": True}
        ]

    def test_add_record(self):
        new_id = add_record(self.records, "Новая книга", "Фэнтези", 400)
        self.assertEqual(new_id, 3)
        self.assertEqual(len(self.records), 3)

    def test_find_records(self):
        found = find_records(self.records, "книга")
        self.assertEqual(len(found), 2)

        found_empty = find_records(self.records, "")
        self.assertEqual(found_empty, [])

    def test_set_completed(self):
        result = set_completed(self.records, 1, True)
        self.assertTrue(result)
        self.assertTrue(self.records[0]["completed"])

        result_unknown = set_completed(self.records, 999, True)
        self.assertFalse(result_unknown)

    def test_delete_record(self):
        result = delete_record(self.records, 1)
        self.assertTrue(result)
        self.assertEqual(len(self.records), 1)

        result_unknown = delete_record(self.records, 999)
        self.assertFalse(result_unknown)

    def test_statistics(self):
        stats = statistics(self.records)
        self.assertEqual(stats["total"], 2)
        self.assertEqual(stats["completed"], 1)
        self.assertEqual(stats["not_completed"], 1)
        self.assertEqual(stats["total_amount"], 500)

if __name__ == "__main__":
    unittest.main()
