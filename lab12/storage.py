import json
from pathlib import Path

def load_records(path):
    """
    Загружает записи из JSON-файла.
    
    Args:
        path (Path): путь к файлу
    
    Returns:
        list: список записей или пустой список при отсутствии файла
    
    Raises:
        ValueError: при ошибке структуры данных
        OSError: при ошибке файлового доступа
    """
    if not path.exists():
        print("Файл data.json не найден. Начинаем с пустого списка.")
        return []
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        validate_records(data)
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка чтения JSON: {e}")
    except OSError as e:
        raise OSError(f"Ошибка доступа к файлу: {e}")

def save_records(path, records):
    """
    Сохраняет записи в JSON-файл.
    
    Args:
        path (Path): путь к файлу
        records (list): список записей
    
    Raises:
        OSError: при ошибке записи
    """
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(records, file, ensure_ascii=False, indent=2)
    except OSError as e:
        raise OSError(f"Ошибка записи файла: {e}")

def validate_records(records):
    """Проверяет структуру данных."""
    if not isinstance(records, list):
        raise ValueError("Данные должны быть списком")
    
    seen_ids = set()
    for i, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"Запись {i} не является словарём")
        
      
        for field in ["id", "title", "category", "amount", "completed"]:
            if field not in record:
                raise ValueError(f"Отсутствует поле '{field}' в записи {i}")
        
       
        if type(record["id"]) is not int or record["id"] <= 0:
            raise ValueError(f"Поле 'id' должно быть положительным целым числом в записи {i}")
        if not isinstance(record["title"], str) or not record["title"].strip():
            raise ValueError(f"Поле 'title' должно быть непустой строкой в записи {i}")
        if not isinstance(record["category"], str) or not record["category"].strip():
            raise ValueError(f"Поле 'category' должно быть непустой строкой в записи {i}")
        if type(record["amount"]) is not int or record["amount"] < 0:
            raise ValueError(f"Поле 'amount' должно быть неотрицательным целым числом в записи {i}")
        if type(record["completed"]) is not bool:
            raise ValueError(f"Поле 'completed' должно быть логическим в записи {i}")
        
        
        if record["id"] in seen_ids:
            raise ValueError(f"Повторяющийся id: {record['id']}")
        seen_ids.add(record["id"])
