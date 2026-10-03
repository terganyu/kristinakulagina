# statistics.py
n = int(input("Введите количество чисел (n >= 1): "))
while n < 1:
    print("Ошибка: n должно быть не меньше 1.")
    n = int(input("Введите количество чисел (n >= 1): "))


total = 0
positive_count = 0

# Вводим первое число для инициализации максимума
first_number = int(input(f"Введите число 1: "))
total += first_number
if first_number > 0:
    positive_count += 1
maximum = first_number


# Вводим остальные n-1 чисел
for i in range(2, n + 1):
    number = int(input(f"Введите число {i}: "))
    total += number
    if number > 0:
        positive_count += 1
    if number > maximum:
        maximum = number

print(f"Сумма: {total}")
print(f"Количество положительных: {positive_count}")
print(f"Максимум: {maximum}")
