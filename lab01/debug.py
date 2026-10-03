print("ФРАГМЕНТ А")
print("Ожидаемый результат: сумма чисел 5, а не строка '23'.")
print(f"Тип first до преобразования: {type('2')}")
print(f"Тип second до преобразования: {type('3')}")
first = "2"
second = "3"
# Исправление: преобразуем строки в числа
first_num = int(first)
second_num = int(second)
result_a = first_num + second_num
print(f"Результат: {result_a}")
print(f"Тип результата: {type(result_a)}\n")

print("ФРАГМЕНТ Б")
print("Ожидаемый результат: возраст через год (например, 18 при вводе 17).")
age_input = input("Возраст: ")
print(f"Тип age до преобразования: {type(age_input)}")
# Исправление: преобразуем строку в число
age = int(age_input)
result_b = age + 1
print(f"Возраст через год: {result_b}")
print(f"Тип результата: {type(result_b)}\n")

print("ФРАГМЕНТ В")
print("Ожидаемый результат: среднее трёх чисел (4, 7, 10) = 7.0.")
first = 4
second = 7
third = 10
# Исправление: добавляем скобки для правильного порядка операций
average = (first + second + third) / 3
print(f"Среднее: {average}")
print(f"Тип результата: {type(average)}")
