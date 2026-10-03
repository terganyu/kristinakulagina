# time_parts.py
total_seconds = int(input("Введите общее количество секунд: "))
while total_seconds < 0:
    print("Ошибка: количество секунд не может быть отрицательным.")
    total_seconds = int(input("Введите общее количество секунд: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours} ч {minutes} мин {seconds} с")
