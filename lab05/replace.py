text = input("Введите текст: ")

colon_count = 0
new_chars = []

# Проходим по каждому символу
for char in text:
    if char == ':':
        new_chars.append('-')
        colon_count += 1
    else:
        new_chars.append(char)

# Собираем новую строку
new_text = ''.join(new_chars)

print(f"Количество замен: {colon_count}")
print(f"Новая строка: '{new_text}'")
