def row_sums(matrix):
    """Возвращает список сумм строк."""
    if not matrix:
        return []
    return [sum(row) for row in matrix]


def column_sums(matrix):
    """Возвращает список сумм столбцов."""
    if not matrix or not matrix[0]:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    return [sum(matrix[i][j] for i in range(rows)) for j in range(cols)]

def diagonal_pattern(size):
    """Создаёт квадратную таблицу с диагональным узором."""
    if size < 1:
        raise ValueError("Размер должен быть >= 1")
    matrix = []
    for row in range(size):
        new_row = []
        for col in range(size):
            if row == col:
                new_row.append(0)
            elif row < col:
                new_row.append(1)
            else:   
                new_row.append(2)
        matrix.append(new_row)
    return matrix

def transform(matrix):
    """
    Преобразование: положительные числа заменяются единицами (вариант 2).
    Для пустой матрицы возвращает пустую матрицу.
    """
    if not matrix:
        return []
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            if element > 0:
                new_row.append(1)
            else:
                new_row.append(element)
        result.append(new_row)
    return result
