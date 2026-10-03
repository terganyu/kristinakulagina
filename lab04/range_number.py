# range_numbers.py
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))


if a < b:
    for number in range(a, b + 1):
        print(number)
elif a > b:
    for number in range(a, b - 1, -1):
        print(number)
else:  # a == b
    print(a)
