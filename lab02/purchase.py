# purchase.py
price = int(input("Цена одной тетради (руб.): "))
while price < 0:
    print("Ошибка: цена не может быть отрицательной.")
    price = int(input("Цена одной тетради (руб.): "))

count = int(input("Количество тетрадей: "))
while count < 0:
    print("Ошибка: количество не может быть отрицательным.")
    count = int(input("Количество тетрадей: "))


paid = int(input("Внесённая сумма (руб.): "))
while paid < price * count:
    print(f"Ошибка: внесённая сумма меньше стоимости покупки ({price * count} руб.).")
    paid = int(input("Внесённая сумма (руб.): "))

cost = price * count
change = paid - cost

print(f"Стоимость: {cost} руб.")
print(f"Сдача: {change} руб.")
