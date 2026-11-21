from table import row_sums, column_sums, diagonal_pattern, transform

def input_matrix():
    """Ввод прямоугольной матрицы с проверкой длины строк."""
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Строка {i + 1} (через пробел): ").split()
            if len(row_input) != columns:
                print(f"Ошибка: нужно ровно {columns} чисел. Повторите ввод.")
            else:
                try:
                    row = [int(x) for x in row_input]
                    matrix.append(row)
                    break
                except ValueError:
                    print("Ошибка: введите целые числа через пробел.")
    return matrix

def print_matrix(matrix, title="Матрица"):
    """Вывод матрицы с заголовком."""
    print(f"\n{title}:")
    for row in matrix:
        print(*row)

def main():
     
    print("=== Ввод прямоугольной матрицы ===")
    matrix = input_matrix()

   
    row_sums_result = row_sums(matrix)
    col_sums_result = column_sums(matrix)

    print_matrix(matrix, "Исходная матрица")
    print(f"Суммы строк: {row_sums_result}")
    print(f"Суммы столбцов: {col_sums_result}")

    
    print("\n=== Диагональный узор ===")
    size = int(input("Введите размер для диагонального узора (>=1): "))
    pattern = diagonal_pattern(size)
    print_matrix(pattern, f"Диагональный узор {size}x{size}")

   
    print("\n=== Преобразование матрицы (положительные → 1) ===")
    transformed = transform(matrix)
    print_matrix(matrix, "Исходная матрица")
    print_matrix(transformed, "Преобразованная матрица")

if __name__ == "__main__":
    main()
