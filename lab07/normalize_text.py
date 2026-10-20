import re

def normalize_text(text):
    """Вернуть текст в нижнем регистре, без лишних пробелов."""
    # Убираем пробелы по краям и заменяем последовательности пробельных символов на один пробел
    normalized = re.sub(r'\s+', ' ', text.strip())
    return normalized.lower()

# Демонстрация работы
text = input("Введите текст: ")
result = normalize_text(text)
print(f"Нормализованный текст: '{result}'")
