import unittest
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from analysis import validate_todos, completion_counts, top_users, select_tasks


class TestAnalysis(unittest.TestCase):

    def setUp(self):
        """Создаёт тестовые данные."""
        self.test_data = [
            {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
            {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
            {"id": 3, "userId": 10, "title": "Строки", "completed": True},
            {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
            {"id": 5, "userId": 5, "title": "Списки", "completed": True}
        ]

    def test_validate_valid_data(self):
        """Проверка корректных данных."""
        validate_todos(self.test_data)   

    def test_completion_counts(self):
        """Проверка подсчёта выполненных задач."""
        counts = completion_counts(self.test_data)
        self.assertEqual(counts, {5: 2, 10: 2})

    def test_top_users(self):
        """Проверка поиска лидеров."""
        counts = {5: 2, 10: 2}
        top = top_users(counts)
        self.assertEqual(top, [5, 10])

    def test_select_tasks_variant2(self):
        """Проверка индивидуального варианта 2 (завершённые задачи)."""
        tasks = select_tasks(self.test_data, 5)
        self.assertEqual(tasks, [1, 5])

        tasks_unknown = select_tasks(self.test_data, 999)
        self.assertEqual(tasks_unknown, [])

    def test_empty_data(self):
        """Проверка пустой структуры."""
        empty_counts = top_users({})
        self.assertEqual(empty_counts, [])

if __name__ == "__main__":
    unittest.main()
