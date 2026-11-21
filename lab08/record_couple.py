 
record = {
    "title": "Основы Python",
    "hours": 40
}

 
record["hours"] = 45

 
record["completed"] = False

 
course_pair = (record["title"], record["hours"])

 
course_name, course_hours = course_pair

 
print(f"Название курса: {course_name}")
print(f"Количество часов: {course_hours}")
print(f"Завершён: {record['completed']}")
