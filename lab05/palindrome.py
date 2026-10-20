text = input("Введите текст: ")

# Очищаем текст: убираем обычные пробелы и приводим к нижнему регистру
cleaned = text.replace(" ", "").lower()

if not cleaned:
    print("Нет текста")
else:
    is_palindrome = True
    length = len(cleaned)
    
    # Сравниваем символы с начала и конца, двигаясь к центру
    for i in range(length // 2):
        if cleaned[i] != cleaned[length - i - 1]:
            is_palindrome = False
            break
    
    if is_palindrome:
        print("Палиндром")
    else:
        print("Не палиндром")
