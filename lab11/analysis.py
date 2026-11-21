import json

def validate_todos(data):
    """
    Проверяет структуру данных todos.
    
    Args:
        data: данные для проверки
    
    Raises:
        ValueError: при нарушении структуры данных
    """
    if not isinstance(data, list):
        raise ValueError("Корень должен быть списком")
    
    seen_ids = set()
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Элемент {i} не является словарём")
        
        
        for field in ["id", "userId", "title", "completed"]:
            if field not in item:
                raise ValueError(f"Отсутствует поле '{field}' в элементе {i}")
        
      
        if type(item["id"]) is not int or item["id"] <= 0:
            raise ValueError(f"Поле 'id' должно быть положительным целым числом в элементе {i}")
        if type(item["userId"]) is not int or item["userId"] <= 0:
            raise ValueError(f"Поле 'userId' должно быть положительным целым числом в элементе {i}")
        if not isinstance(item["title"], str) or not item["title"]:
            raise ValueError(f"Поле 'title' должно быть непустой строкой в элементе {i}")
        if type(item["completed"]) is not bool:
            raise ValueError(f"Поле 'completed' должно быть логическим в элементе {i}")
        
       
        if item["id"] in seen_ids:
            raise ValueError(f"Повторяющийся id: {item['id']}")
        seen_ids.add(item["id"])

def completion_counts(todos):
    """Возвращает словарь количества выполненных задач для всех пользователей."""
    counts = {}
    
    for task in todos:
        user_id = task["userId"]
        counts.setdefault(user_id, 0)
        if task["completed"]:
            counts[user_id] += 1
    return counts

def top_users(counts):
    """Возвращает отсортированный список идентификаторов с максимальным количеством выполненных задач."""
    if not counts:
        return []
    max_count = max(counts.values())
    if max_count == 0:
        return []
 
    top = [user_id for user_id, count in counts.items() if count == max_count]
    return sorted(top)

def select_tasks(todos, user_id, parameter=None):
    """
    Отбирает завершённые задачи указанного пользователя (вариант 2).
    
    Args:
        todos (list): список задач
        user_id (int): идентификатор пользователя
        parameter: не используется (None)
    
    Returns:
        list: список идентификаторов задач
    """
    result_ids = []
    for task in todos:
        if task["userId"] == user_id and task["completed"]:
            result_ids.append(task["id"])
    return result_ids
