def common_topics(first, second):
    """
    Возвращает отсортированный список общих тем.
    
    Args:
        first (list): первый список тем
        second (list): второй список тем
    
    Returns:
        list: отсортированный список общих тем
    """
    set1 = set(first)
    set2 = set(second)
    common = set1 & set2   
    return sorted(common)

def all_topics(first, second):
    """
    Возвращает отсортированный список всех уникальных тем.
    
    Args:
        first (list): первый список тем
        second (list): второй список тем
    
    Returns:
        list: отсортированный список всех уникальных тем
    """
    set1 = set(first)
    set2 = set(second)
    all_themes = set1 | set2   
    return sorted(all_themes)
first = ["python", "sql", "python"]
second = ["sql", "git"]

print(common_topics(first, second))   
print(all_topics(first, second))      
