# variant.py — Вариант 2: количество книг и книг в коробке
total_books = int(input("Общее количество книг: "))
while total_books < 0:
    print("Ошибка: количество книг не может быть отрицательным.")
    total_books = int(input("Общее количество книг: "))

books_per_box = int(input("Количество книг в одной коробке: "))
while books_per_box <= 0:
    print("Ошибка: вместимость коробки должна быть положительной.")
    books_per_box = int(input("Количество книг в одной коробке: "))

full_boxes = total_books // books_per_box
remaining_books = total_books % books_per_box
total_boxes_needed = (total_books + books_per_box - 1) // books_per_box

print(f"Полных коробок: {full_boxes}")
print(f"Остаток книг: {remaining_books}")
print(f"Всего коробок нужно: {total_boxes_needed}")
