from pathlib import Path
from storage import load_records, save_records
from logic import add_record, find_records, set_completed, delete_record, statistics

def main():
    folder = Path(__file__).resolve().parent
    data_path = folder / "data.json"
    
    try:
        records = load_records(data_path)
    except (ValueError, OSError) as e:
        print(f"Критическая ошибка при загрузке данных: {e}")
        return
    
    while True:
        print("\n=== Меню управления списком книг ===")
        print("1. Показать все записи")
        print("2. Добавить книгу")
        print("3. Найти книги")
        print("4. Изменить статус книги")
        print("5. Удалить книгу")
        print("6. Показать статистику")
        print("7. Сохранить данные")
        print("8. Выйти")
        
        choice = input("Выберите действие (1–8): ").strip()
        
        if choice == "1":
            show_all_records(records)
        elif choice == "2":
            add_new_book(records)
        elif choice == "3":
            search_books(records)
        elif choice == "4":
            change_book_status(records)
        elif choice == "5":
            delete_book(records)
        elif choice == "6":
            show_statistics(records)
        elif choice == "7":
            save_current_data(records, data_path)
        elif choice == "8":
            exit_program(records, data_path)
            break
        else:
            print("Неверная команда. Попробуйте снова.")

def show_all_records(records):
    if not records:
        print("Нет записей")
        return
    print("\nСписок книг:")
    for record in sorted(records, key=lambda x: x["id"]):
        status = "Прочитана" if record["completed"] else "Не прочитана"
        print(f"ID: {record['id']}, Название: {record['title']}, "
              f"Категория: {record['category']}, Страниц: {record['amount']}, Статус: {status}")

def add_new_book(records):
    while True:
        title = input("Название книги: ").strip()
        if title:
            break
        print("Название не может быть пустым.")
    
    while True:
        category = input("Категория: ").strip()
        if category:
            break
        print("Категория не может быть пустой.")
    
    while True:
        try:
            amount = int(input("Количество страниц: "))
            if amount >= 0:
                break
            else:
                print("Количество страниц должно быть неотрицательным.")
        except ValueError:
            print("Введите целое число.")
    
    new_id = add_record(records, title, category, amount)
    print(f"Книга '{title}' добавлена с ID {new_id}")

def search_books(records):
    query = input("Введите поисковую строку: ").strip()
    if not query:
        print("Поисковая строка не может быть пустой.")
        return
    found = find_records(records, query)
    if not found:
        print("Ничего не найдено.")
    else:
        print(f"\nНайдено {len(found)} книг:")
        for record in found:
            status = "Прочитана" if record["completed"] else "Не прочитана"
            print(f"ID: {record['id']}, Название: {record['title']}, Статус: {status}")

def change_book_status(records):
    try:
        record_id = int(input("ID книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return
    
    status_input = input("Статус (да/нет): ").strip().lower()
    if status_input in ("да", "yes", "1"):
        completed = True
    elif status_input in ("нет", "no", "0"):
        completed = False
    else:
        print("Неверный статус. Используйте 'да' или 'нет'.")
        return
    
    if set_completed(records, record_id, completed):
        print(f"Статус книги с ID {record_id} изменён.")
    else:
        print(f"Книга с ID {record_id} не найдена.")

def delete_book(records):
    try:
        record_id = int(input("ID книги для удаления: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return
    
    confirm = input(f"Удалить книгу с ID {record_id}? (да/нет): ").strip().lower()
    if confirm in ("да", "yes"):
        if delete_record(records, record_id):
            print(f"Книга с ID {record_id} удалена.")
        else:
            print(f"Книга с ID {record_id} не найдена.")
    else:
        print("Удаление отменено.")

def show_statistics(records):
    stats = statistics(records)
    print("\nСтатистика:")
    print(f"Всего книг: {stats['total']}")
    print(f"Прочитано: {stats['completed']}")
    print(f"Не прочитано: {stats['not_completed']}")
    print(f"Общее количество страниц: {stats['total_amount']}")
    print("По категориям:")
    for category, pages in stats["categories"]:
        print(f"  {category}: {pages} страниц")

def save_current_data(records, path):
    try:
        save_records(path, records)
        print("Данные успешно сохранены.")
    except OSError as e:
        print(f"Ошибка сохранения: {e}")

def exit_program(records, path):
    save_choice = input("Сохранить данные перед выходом? (да/нет): ").strip().lower()
    if save_choice in ("да", "yes"):
        try:
            save_records(path, records)
            print("Данные сохранены. До свидания!")
        except OSError as e:
            print(f"Ошибка при сохранении: {e}. Программа завершает работу.")
    else:
        print("До свидания!")

if __name__ == "__main__":
    main()
