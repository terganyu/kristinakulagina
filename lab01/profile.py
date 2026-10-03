# Запрос данных у пользователя
surname = input("Введите фамилию: ")
name = input("Введите имя: ")
group = input("Введите группу: ")
city = input("Введите город: ")

# Возраст — целое число от 1 до 120
age = int(input("Введите возраст (1–120 лет): "))
while age < 1 or age > 120:
    print("Ошибка: возраст должен быть от 1 до 120 лет.")
    age = int(input("Введите возраст (1–120 лет): "))


favorite_subject = input("Введите любимый предмет: ")
# Часы подготовки — неотрицательное дробное число
study_hours = float(input("Введите количество часов подготовки в неделю: "))
while study_hours < 0:
    print("Ошибка: количество часов не может быть отрицательным.")
    study_hours = float(input("Введите количество часов подготовки в неделю: "))

# Расчёты
age_in_4_years = age + 4
total_hours_4_weeks = study_hours * 4
average_hours_per_day = study_hours / 7


# Вывод карточки
print("" + "="*40)
print("КАРТОЧКА СТУДЕНТА")
print("="*40)
print(f"Полное имя: {name} {surname}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age}")
print(f"Возраст через 4 года: {age_in_4_years}")
print(f"Любимый предмет: {favorite_subject}")
print(f"Часы подготовки в неделю: {study_hours:.2f}")
print(f"Часы подготовки за 4 недели: {total_hours_4_weeks:.2f}")
print(f"Среднее время подготовки в день: {average_hours_per_day:.2f}")
print("="*40)