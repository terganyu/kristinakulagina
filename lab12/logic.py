def add_record(records, title, category, amount):
    """Добавляет новую запись."""
   
    new_id = max((record["id"] for record in records), default=0) + 1
    
    new_record = {
        "id": new_id,
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False
    }
    records.append(new_record)
    return new_id

def find_records(records, query):
    """Ищет записи по подстроке в названии (без учёта регистра)."""
    query = query.strip().lower()
    if not query:
        return []
    found = []
    for record in records:
        if query in record["title"].lower():
            found.append(record)
    return found

def set_completed(records, record_id, completed):
    """Изменяет статус выполнения записи."""
    for record in records:
        if record["id"] == record_id:
            record["completed"] = completed
            return True
    return False

def delete_record(records, record_id):
    """Удаляет запись по ID."""
    for i, record in enumerate(records):
        if record["id"] == record_id:
            del records[i]
            return True
    return False

def statistics(records):
    """Вычисляет статистику по записям."""
    total = len(records)
    completed_count = sum(1 for r in records if r["completed"])
    not_completed_count = total - completed_count
    total_amount = sum(r["amount"] for r in records)
     
    category_stats = {}
    for record in records:
        category = record["category"]
        category_stats[category] = category_stats.get(category, 0) + record["amount"]
    
     
    sorted_categories = sorted(category_stats.items())
    
    return {
        "total": total,
        "completed": completed_count,
        "not_completed": not_completed_count,
        "total_amount": total_amount,
        "categories": sorted_categories
    }
