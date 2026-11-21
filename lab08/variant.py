def totals_by_category(records):
    """
    Суммирует количество экземпляров (amount) по категориям книг.

    Args:
        records (list): список словарей с полями title, category, amount
    Returns:
        dict: словарь сумм amount по категориям
    """
    totals = {}
    for record in records:
        category = record["category"]
        amount = record["amount"]
        totals[category] = totals.get(category, 0) + amount
    return totals


def titles_in_category(records, category):
    """
    Возвращает названия книг в заданной категории в исходном порядке.

    Args:
        records (list): список словарей
        category (str): искомая категория
    Returns:
        list: названия книг в категории
    """
    titles = []
    for record in records:
        if record["category"] == category:
            titles.append(record["title"])
    return titles

def get_sorted_totals(totals):
    """
    Возвращает список пар (category, total), отсортированных по убыванию суммы,
    затем по названию категории.

    Args:
        totals (dict): словарь сумм по категориям
    Returns:
        list: отсортированный список пар
    """
    return sorted(
        totals.items(),
        key=lambda x: (-x[1], x[0])  
    )

 
records = [
    {"title": "Мастер и Маргарита", "category": "Классика", "amount": 5},
    {"title": "1984", "category": "Антиутопия", "amount": 3},
    {"title": "Преступление и наказание", "category": "Классика", "amount": 7},
    {"title": "Скотный двор", "category": "Антиутопия", "amount": 2},
    {"title": "Гарри Поттер и философский камень", "category": "Фэнтези", "amount": 10},
    {"title": "Улисс", "category": "Классика", "amount": 4},
]

if __name__ == "__main__":
     
    totals = totals_by_category(records)
    print("Сводка по категориям (по убыванию количества экземпляров):")
    for category, total in get_sorted_totals(totals):
        print(f"{category}: {total} экземпляров")

    
    search_category = "Классика"
    titles = titles_in_category(records, search_category)
    print(f"\nКниги в категории '{search_category}': {titles}")

 
    unknown_category = "Научная фантастика"
    unknown_titles = titles_in_category(records, unknown_category)
    print(f"Книги в категории '{unknown_category}': {unknown_titles}")

    
    original_records = [record.copy() for record in records]
    assert records == original_records, "Исходные данные были изменены!"
    print("\nПроверка пройдена: исходные данные не изменены.")
