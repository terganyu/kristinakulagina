from table import row_sums, column_sums, diagonal_pattern, transform

def run_tests():
    print("Запуск тестов...")

    
    test_matrix = [[1, 2, 3], [4, 5, 6]]
    assert row_sums(test_matrix) == [6, 15], "Ошибка в суммах строк"
    assert column_sums(test_matrix) == [5, 7, 9], "Ошибка в суммах столбцов"

 
    single_matrix = [[7]]
    assert row_sums(single_matrix) == [7], "Ошибка для матрицы 1x1 (суммы строк)"
    assert column_sums(single_matrix) == [7], "Ошибка для матрицы 1x1 (суммы столбцов)"
    assert diagonal_pattern(1) == [[0]], "Ошибка диагонального узора размера 1"

  
    vertical_matrix = [[1], [-1], [0]]
    assert row_sums(vertical_matrix) == [1, -1, 0], "Ошибка сумм строк для 3x1"
    assert column_sums(vertical_matrix) == [0], "Ошибка сумм столбцов для 3x1"

    
    empty_matrix = []
    assert row_sums(empty_matrix) == [], "Ошибка для пустой матрицы (суммы строк)"
    assert column_sums(empty_matrix) == [], "Ошибка для пустой матрицы (суммы столбцов)"
    assert transform(empty_matrix) == [], "Ошибка преобразования пустой матрицы"

  
    expected_pattern = [[0, 1, 1], [2, 0, 1], [2, 2, 0]]
    assert diagonal_pattern(3) == expected_pattern, "Ошибка диагонального узора 3x3"

 
    control_matrix = [[-2, 0, 3], [4, -5, 6]]
    expected_transform = [[-2, 0, 1], [1, -5, 1]]
    assert transform(control_matrix) == expected_transform, "Ошибка преобразования контрольной матрицы"

 
    original = [[1, -2], [3, 0]]
    transformed = transform(original)
    transformed[0][0] = 999   
    assert original == [[1, -2], [3, 0]], "Исходная матрица была изменена!"

    print("Все тесты пройдены успешно!")

if __name__ == "__main__":
    run_tests()
