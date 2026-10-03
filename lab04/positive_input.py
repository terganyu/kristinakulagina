# positive_input.py
attempts = 0
number = int(input("Введите положительное число: "))

while number <= 0:
    attempts += 1
    print("Число не положительное, попробуйте ещё раз.")
    number = int(input("Введите положительное число: "))

square = number ** 2
print(f"Квадрат числа: {square}")
print(f"Количество отклонённых попыток: {attempts}")
