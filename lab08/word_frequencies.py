import string

def word_counts(text):
    """
    Подсчитывает частоту слов в тексте.
    
    Args:
        text (str): входной текст
    
    Returns:
        dict: словарь «слово → количество»
    """
    if not text:
        return {}
    
    
    words = text.lower().split()
    counts = {}
    
    for word in words:
        
        cleaned_word = word.strip(string.punctuation)
        if cleaned_word:   
            counts[cleaned_word] = counts.get(cleaned_word, 0) + 1
    
    return counts

def print_word_counts(counts):
    """Выводит пары «слово: количество» в алфавитном порядке."""
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")
print(word_counts("Python, python! SQL"))  
print(word_counts("!!!"))   
