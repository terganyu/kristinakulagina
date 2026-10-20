text = input("Введите строку: ")

try:
    # Разбиваем строку на слова, очищаем их и фильтруем по условию
    result = [
        word.strip(".,!?;:").lower()
        for word in text.split()
        if word.strip(".,!?;:") and word.strip(".,!?;:").lower().endswith('я')
    ]
    
    if result:
        for word in result:
            print(word)
        print(f"Количество: {len(result)}")
    else:
        print("Нет совпадений")
        print("Количество: 0")

except Exception as e:
    print(f"Произошла ошибка: {e}")
    print("Нет совпадений")
    print("Количество: 0")
