def sum_digits(number):
    """Вернуть сумму цифр модуля числа."""
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

# Демонстрация работы
num = int(input("Введите целое число: "))
result = sum_digits(num)
print(f"Сумма цифр: {result}")
