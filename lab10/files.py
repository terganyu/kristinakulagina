def read_matrix(path):
    """
    Читает матрицу из файла с проверкой формата.
    
    Формат:
    - Первая строка: два положительных целых числа — строки и столбцы.
    - Далее ровно указанное количество строк с указанным количеством чисел.
    
    Args:
        path (Path): путь к файлу
    
    Returns:
        list: матрица (список списков целых чисел)
    
    Raises:
        ValueError: при ошибке формата с указанием номера строки
        FileNotFoundError: если файл не существует
    """
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        raise ValueError("Файл пуст.")

    # Разбор заголовка
    header_parts = lines[0].strip().split()
    if len(header_parts) != 2:
        raise ValueError("Строка 1: ожидалось 2 числа (строки и столбцы).")

    try:
        rows = int(header_parts[0])
        cols = int(header_parts[1])
    except ValueError:
        raise ValueError("Строка 1: строки и столбцы должны быть целыми числами.")

    if rows <= 0 or cols <= 0:
        raise ValueError("Строка 1: количество строк и столбцов должно быть > 0.")

    # Проверка количества строк данных
    data_lines = lines[1:]
    if len(data_lines) != rows:
        raise ValueError(f"Ожидалось {rows} строк данных, но найдено {len(data_lines)}.")

    matrix = []
    for i, line in enumerate(data_lines, start=2):
        line = line.strip()
        if not line:  # Пропускаем пустые строки
            raise ValueError(f"Строка {i}: пустая строка данных.")

        elements = line.split()
        if len(elements) != cols:
            raise ValueError(f"Строка {i}: ожидалось {cols} чисел, но найдено {len(elements)}.")

        row = []
        for j, elem in enumerate(elements):
            try:
                row.append(int(elem))
            except ValueError:
                raise ValueError(f"Строка {i}, столбец {j + 1}: не число '{elem}'.")
        matrix.append(row)

    return matrix
