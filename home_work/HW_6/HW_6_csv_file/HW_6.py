import csv


def read_students(filename: str) -> list:
    """
    Читает данные студентов из CSV-файла и возвращает список студентов.

    Параметры:
    filename : str
        Имя CSV-файла для чтения.

    Возвращает:
    list
        Список студентов, где каждый студент представлен как словарь с ключами
        'Ім'я', 'Вік' и 'Оцінка'.
    """
    students = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students


def calculate_average_grade(students: list) -> float:
    """
    Вычисляет среднюю оценку студентов.

    Параметры:
    students : list
        Список студентов, где каждый студент представлен как словарь с ключом
        'Оцінка'.

    Возвращает:
    float
        Средняя оценка студентов. Если список пуст, возвращает 0.
    """
    total_grade = 0
    for student in students:
        total_grade += int(student['Оцінка'])
    return total_grade / len(students) if students else 0


def add_student(filename: str, name: str, age: str, grade: str) -> None:
    """
    Добавляет нового студента в CSV-файл.

    Параметры:
    filename : str
        Имя CSV-файла, в который будет добавлен новый студент.
    name : str
        Имя нового студента.
    age : str
        Возраст нового студента.
    grade : str
        Оценка нового студента.

    Возвращает:
    None
    """
    with open(filename, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, grade])


if __name__ == "__main__":
    """
    Основной блок программы, который выполняется при запуске скрипта.

    Читает данные студентов из CSV-файла, вычисляет и выводит среднюю оценку,
    а также позволяет пользователю ввести данные нового студента и добавляет их в файл.
    """
    filename = 'students.csv'

    # Чтение данных из CSV-файла
    students = read_students(filename)

    # Вывод средней оценки
    average_grade = calculate_average_grade(students)
    print(f"Средняя оценка студентов: {average_grade:.2f}")

    # Добавление нового студента
    new_name = input("Введите имя нового студента: ")
    new_age = input("Введите возраст нового студента: ")
    new_grade = input("Введите оценку нового студента: ")

    add_student(filename, new_name, new_age, new_grade)
    print(f"Студент '{new_name}' добавлен в файлу.")
