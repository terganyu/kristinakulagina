# variant.py — Вариант 2: заполненность хранилища
value = int(input("Введите значение заполненности (0–100): "))

if value < 0 or value > 100:
    print("Ошибка диапазона")
elif 0 <= value <= 49:
    print("Свободно")
elif 50 <= value <= 89:
    print("Мало места")
else:  # 90–100
    print("Почти заполнено")
