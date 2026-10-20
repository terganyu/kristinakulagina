def select_numbers(numbers, threshold):
    """Вернуть список чисел, которые меньше порога."""
    return [num for num in numbers if num < threshold]

# Демонстрация работы
data = input("Введите целые числа через пробел: ").strip()
threshold = int(input("Введите порог: "))

numbers = list(map(int, data.split())) if data else []
result = select_numbers(numbers, threshold)

print(f"Исходный список: {numbers}")
print(f"Порог: {threshold}")
print(f"Числа меньше порога: {result}")
print(f"Количество: {len(result)}")
