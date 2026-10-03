
year = int(input("Введите год (1–9999): "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Да")
else:
    print("Нет")
