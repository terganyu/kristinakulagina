def average(numbers):
    """Вернуть среднее значение списка чисел или None, если список пуст."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Демонстрация работы
data = input("Введите числа через пробел: ").strip()
numbers = list(map(float, data.split())) if data else []

result = average(numbers)
if result is None:
    print("Нет данных")
else:
    print(f"Среднее: {result:.2f}")
