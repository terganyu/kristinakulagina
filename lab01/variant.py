# variant.py
# Позиция 1
qty1 = int(input("Количество единиц первой позиции: "))
price1 = float(input("Цена за единицу первой позиции: "))

# Позиция 2
qty2 = int(input("Количество единиц второй позиции: "))
price2 = float(input("Цена за единицу второй позиции: "))

delivery = float(input("Стоимость доставки: "))
paid = float(input("Внесённая сумма: "))
discount_percent = float(input("Скидка на товары в процентах (0–100): "))
while discount_percent < 0 or discount_percent > 100:
    print("Ошибка: скидка должна быть от 0 до 100.")
    discount_percent = float(input("Скидка на товары в процентах (0–100): "))

cost1 = qty1 * price1
cost2 = qty2 * price2
total_goods = cost1 + cost2
discount_amount = total_goods * (discount_percent / 100)
total_after_discount = total_goods - discount_amount
total_with_delivery = total_after_discount + delivery
change = paid - total_with_delivery

print("\n" + "-" * 50)
print("РАСЧЁТ ЗАКАЗА (ВАРИАНТ 2)")
print("-" * 50)
print(f"Стоимость первой позиции: {cost1:.2f}")
print(f"Стоимость второй позиции: {cost2:.2f}")
print(f"Итого стоимость товаров: {total_goods:.2f}")
print(f"Размер скидки: {discount_amount:.2f}")
print(f"Стоимость товаров со скидкой: {total_after_discount:.2f}")
print(f"Доставка: {delivery:.2f}")
print(f"Итоговая сумма к оплате: {total_with_delivery:.2f}")
print(f"Внесено: {paid:.2f}")
print(f"Сдача: {change:.2f}")
print("-" * 50)
