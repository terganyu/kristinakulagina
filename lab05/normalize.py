import re

text = input("Введите текст: ")
original_length = len(text)

# Убираем пробелы по краям и заменяем все последовательности пробельных символов на один пробел
normalized = re.sub(r'\s+', ' ', text.strip())
new_length = len(normalized)
word_count = len(normalized.split()) if normalized else 0

print(f"Исходная длина: {original_length}")
print(f"Новая длина: {new_length}")
print(f"Нормализованный текст: '{normalized}'")
print(f"Количество слов: {word_count}")
