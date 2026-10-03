# variant.py — Вариант 2: отрицательные числа
n = int(input("Введите количество чисел (n >= 0): "))
while n < 0:
    print("Ошибка: n не может быть отрицательным.")
    n = int(input("Введите количество чисел (n >= 0): "))

count_negative = 0
sum_negative = 0

for i in range(n):
    number = int(input(f"Введите число {i + 1}: "))
    if number < 0:
        count_negative += 1
        sum_negative += number

print(f"Количество отрицательных чисел: {count_negative}")
print(f"Сумма отрицательных чисел: {sum_negative}")
