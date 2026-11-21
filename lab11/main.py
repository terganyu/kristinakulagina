import json
from pathlib import Path
from analysis import validate_todos, completion_counts, top_users, select_tasks

def read_positive_integer():
    """Повторяет ввод, пока не получено целое число > 0."""
    while True:
        try:
            number = int(input("Введите идентификатор пользователя (целое число > 0): "))
            if number > 0:
                return number
            else:
                print("Число должно быть больше нуля.")
        except ValueError:
            print("Не целое число. Попробуйте ещё раз.")

def main():
    
    folder = Path(__file__).resolve().parent
    input_path = folder / "todos.json"
    leaders_path = folder / "leaders.json"
    selected_path = folder / "selected.json"

    try:
   
        with open(input_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        validate_todos(data)
 
        counts = completion_counts(data)
        top_users_list = top_users(counts)
  
        leader_task_ids = []
        for task in data:
            if task["userId"] in top_users_list and task["completed"]:
                leader_task_ids.append(task["id"])

 
        with open(leaders_path, "w", encoding="utf-8") as file:
            json.dump({"taskIds": leader_task_ids}, file, ensure_ascii=False, indent=2)


     
        user_id = read_positive_integer()
        selected_tasks = select_tasks(data, user_id)

        with open(selected_path, "w", encoding="utf-8") as file:
            json.dump({"user_id": user_id, "taskIds": selected_tasks}, file, ensure_ascii=False, indent=2)

   
        print("\n=== Сводка анализа ===")
        print(f"Количество выполненных задач по пользователям: {counts}")
        print(f"Лидеры (максимальное количество): {top_users_list}")
        print(f"Задачи лидеров (id): {leader_task_ids}")
        print(f"\nВыбранные задачи для пользователя {user_id}: {selected_tasks}")

    except FileNotFoundError:
        print(f"Ошибка: файл {input_path} не найден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
    except ValueError as e:
        print(f"Ошибка структуры данных: {e}")
    except OSError as e:
        print(f"Ошибка файлового доступа: {e}")

if __name__ == "__main__":
    main()
