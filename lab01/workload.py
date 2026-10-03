# Ввод данных по первому предмету
subject1 = input("Введите название первого предмета: ")
lessons1 = int(input(f"Введите количество занятий по {subject1} в неделю: "))
while lessons1 < 0:
    print("Ошибка: количество занятий не может быть отрицательным.")
    lessons1 = int(input(f"Введите количество занятий по {subject1} в неделю: "))
duration1 = int(input(f"Введите продолжительность одного занятия по {subject1} (в минутах): "))
while duration1 <= 0:
    print("Ошибка: продолжительность должна быть положительным числом.")
    duration1 = int(input(f"Введите продолжительность одного занятия по {subject1} (в минутах): "))

# Ввод данных по второму предмету
subject2 = input("Введите название второго предмета: ")
lessons2 = int(input(f"Введите количество занятий по {subject2} в неделю: "))
while lessons2 < 0:
    print("Ошибка: количество занятий не может быть отрицательным.")
    lessons2 = int(input(f"Введите количество занятий по {subject2} в неделю: "))
duration2 = int(input(f"Введите продолжительность одного занятия по {subject2} (в минутах): "))
while duration2 <= 0:
    print("Ошибка: продолжительность должна быть положительным числом.")
    duration2 = int(input(f"Введите продолжительность одного занятия по {subject2} (в минутах): "))

# Доступное время в часах
available_hours = float(input("Введите доступное время на неделю (в часах): "))
total_minutes_subject1 = lessons1 * duration1
total_minutes_subject2 = lessons2 * duration2
total_load_minutes = total_minutes_subject1 + total_minutes_subject2
total_load_hours = total_load_minutes / 60
free_time_hours = available_hours - total_load_hours
load_4_weeks_hours = total_load_hours * 4

# Проверка, что доступное время не меньше нагрузки
while free_time_hours < 0:
    print(f"Ошибка: доступное время ({available_hours} ч) меньше суммарной нагрузки ({total_load_hours:.2f} ч).")
    available_hours = float(input("Введите доступное время на неделю (в часах): "))
    free_time_hours = available_hours - total_load_hours

# Вывод результатов
print("\n" + "-"*50)
print("УЧЕБНАЯ НАГРУЗКА")
print("-"*50)
print(f"{subject1}: {total_minutes_subject1} минут в неделю")
print(f"{subject2}: {total_minutes_subject2} минут в неделю")
print(f"Общая нагрузка: {total_load_minutes} минут или {total_load_hours:.2f} часов")
print(f"Остаток свободного времени: {free_time_hours:.2f} часов")
print(f"Нагрузка за 4 недели: {load_4_weeks_hours:.2f} часов")
print("-"*50)
