import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix

class TestReadMatrix(unittest.TestCase):

    def test_valid_matrix(self):
        """Проверка корректной матрицы 2×3."""
        with TemporaryDirectory() as directory:
            path = Path(directory) / "matrix.txt"
            path.write_text("2 3\n1 -2 3\n4 0 -6\n", encoding="utf-8")
            result = read_matrix(path)
            self.assertEqual(result, [[1, -2, 3], [4, 0, -6]])

    def test_single_element(self):
        """Матрица 1×1."""
        with TemporaryDirectory() as directory:
            path = Path(directory) / "matrix.txt"
            path.write_text("1 1\n0\n", encoding="utf-8")
            self.assertEqual(read_matrix(path), [[0]])

    def test_empty_file(self):
        """Пустой файл."""
        with TemporaryDirectory() as directory:
            path = Path(directory) / "empty.txt"
            path.touch()  # Создаём пустой файл
            with self.assertRaises(ValueError) as context:
                read_matrix(path)
            self.assertIn("Файл пуст", str(context.exception))

    def test_invalid_header(self):
        """Неверный заголовок."""
        with TemporaryDirectory() as directory:
            path = Path(directory) / "matrix.txt"
            path.write_text("0 3\n", encoding="utf-8")
            with self.assertRaises(ValueError) as context:
                read_matrix(path)
            self.assertIn("должно быть > 0", str(context.exception))

    def test_missing_data_rows(self):
        """Недостаточное количество строк данных."""
        with TemporaryDirectory() as directory:
            path = Path(directory) / "matrix.txt"
            path.write_text("2 1\n7\n", encoding="utf-8")
            with self.assertRaises(ValueError) as context:
                read_matrix(path)
            self.assertIn("Ожидалось 2 строк данных", str(context.exception))

    def test_non_numeric_cell(self):
        """Нечисловая ячейка."""
        with TemporaryDirectory() as directory:
            path = Path(directory) / "matrix.txt"
            path.write_text("1 2\n1 x\n", encoding="utf-8")
            with self.assertRaises(ValueError) as context:
                read_matrix(path)
            self.assertIn("не число 'x'", str(context.exception))

    def test_file_not_found(self):
        """Отсутствующий файл."""
        nonexistent_path = Path("nonexistent.txt")
        with self.assertRaises(FileNotFoundError):
            read_matrix(nonexistent_path)

if __name__ == "__main__":
    unittest.main()
