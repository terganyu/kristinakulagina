data = input("Введите целые числа через пробел: ").strip()
numbers = list(map(int, data.split())) if data else []

if not numbers:
    print("Нет данных")
else:
    max_value = max(numbers)
    positions = [index for index, value in enumerate(numbers) if value == max_value]
    print(positions)
