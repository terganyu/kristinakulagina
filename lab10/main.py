from pathlib import Path
from files_lab import read_matrix
from table import row_sums, column_sums

def read_positive_integer():
    """Повторяет ввод, пока не получено целое число > 0."""
    while True:
        try:
            number = int(input("Введите целое число больше нуля: "))
            if number > 0:
                return number
            else:
                print("Число должно быть больше нуля.")
        except ValueError:
            print("Не целое число. Попробуйте ещё раз.")

def selected_sum(matrix):
    """
    Сумма отрицательных элементов матрицы (вариант 2).
    
    Args:
        matrix (list): прямоугольная матрица (список списков)
    
    Returns:
        int: сумма отрицательных элементов
    """
    total = 0
    for row in matrix:
        for element in row:
            if element < 0:
                total += element
    return total

def main():
    # Задание 1: надёжный ввод размера
    print("=== Задание 1: Надёжный ввод ===")
    size = read_positive_integer()
    print(f"Получено число: {size}")

    # Задание 2 и 3: чтение матрицы и создание отчёта
    print("\n=== Задание 2–3: Чтение матрицы и отчёт ===")
    folder = Path(__file__).resolve().parent
    input_path = folder / "matrix.txt"
    output_path = folder / "report.txt"

    try:
        # Чтение матрицы
        matrix = read_matrix(input_path)

        # Вычисления
        row_totals = row_sums(matrix)
        col_totals = column_sums(matrix)
        variant_result = selected_sum(matrix)

        # Формирование отчёта
        report_lines = [
            f"Суммы строк: {' '.join(map(str, row_totals))}",
            f"Суммы столбцов: {' '.join(map(str, col_totals))}",
            f"Результат варианта: {variant_result}"
        ]

        # Запись отчёта (только после успешной проверки данных)
        with open(output_path, "w", encoding="utf-8") as report_file:
            report_file.write("\n".join(report_lines) + "\n")

        print("Отчёт успешно создан: report.txt")
        print("\nСодержимое отчёта:")
        for line in report_lines:
            print(line)

    except FileNotFoundError:
        print(f"Ошибка: файл {input_path} не найден.")
    except UnicodeError:
        print(f"Ошибка кодировки файла {input_path}.")
    except ValueError as e:
        print(f"Ошибка формата данных: {e}")
    except OSError as e:
        print(f"Ошибка файлового доступа: {e}")

if __name__ == "__main__":
    main()
