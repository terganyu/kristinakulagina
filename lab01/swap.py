# swap.py
first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

print("Исходные значения:")
print(f"Первая аудитория: {first_room}")
print(f"Вторая аудитория: {second_room}")

temp = first_room
first_room = second_room
second_room = temp

print("После обмена:")
print(f"Первая аудитория: {first_room}")
print(f"Вторая аудитория: {second_room}")
