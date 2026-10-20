data = input("Введите целые числа через пробел: ").strip()
numbers = list(map(int, data.split())) if data else []
selected = [num for num in numbers if num < 0]
sorted_selected = sorted(selected)

print(f"Выборка: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Отсортированная копия: {sorted_selected}")
