data = input("Введите целые числа через пробел: ").strip()
original = list(map(int, data.split())) if data else []
transformed = [abs(num) for num in original]

print(f"Исходный список: {original}")
print(f"Новый список: {transformed}")
