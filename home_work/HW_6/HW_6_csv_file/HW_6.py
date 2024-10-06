import json


def load_books(filename):
    """
    Читает книги из JSON-файла и возвращает список книг.

    Параметры:
    filename : str
        Имя JSON-файла для чтения.

    Возвращает:
    list
        Список книг, где каждая книга представлена как словарь с ключами
        'назва', 'автор', 'рік' и 'наявність'.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Загружаем и возвращаем список книг
            return json.load(file)
    except FileNotFoundError:
        return []


def print_available_books(books):
    """
    Выводит на экран список доступных книг.

    Параметры:
    books : list
        Список книг, представленный в виде словарей.

    Возвращает:
    None
    """
    available_books = [book for book in books if book['наявність']]

    message = "Доступні книги:" if available_books else "Немає доступних книг."
    print(message)

    for book in available_books:
        print(f"Назва: {book['назва']}, Автор: {book['автор']}, Рік: {book['рік']}")


def add_book(filename, new_book):
    """
    Добавляет новую книгу в JSON-файл.

    Параметры:
    filename : str
        Имя JSON-файла для добавления книги.
    new_book : dict
        Словарь с информацией о новой книге, содержащий ключи
        'назва', 'автор', 'рік' и 'наявність'.

    Возвращает:
    None
    """
    # Загружаем существующие книги
    books = load_books(filename)
    books.append(new_book)
    # Сохраняем обновлённый список книг
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def main():
    # Имя файла для хранения книг
    filename = 'books.json'

    # Загружаем книги
    books = load_books(filename)
    # Выводим доступные книги
    print_available_books(books)

    new_book = {
        "назва": "Книга 3",
        "автор": "Автор 3",
        "рік": 2021,
        "наявність": True
    }

    add_book(filename, new_book)
    print("Нова книга додана.")


if __name__ == "__main__":
    main()
