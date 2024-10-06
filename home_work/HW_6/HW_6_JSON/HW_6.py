import json


# Функція для завантаження книг з файлу
def load_books(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Функція для виведення доступних книг
def print_available_books(books):
    available_books = [book for book in books if book['наявність']]
    if available_books:
        print("Доступні книги:")
        for book in available_books:
            print(f"Назва: {book['назва']}, Автор: {book['автор']}, Рік: {book['рік']}")
    else:
        print("Немає доступних книг.")


# Функція для додавання нової книги
def add_book(filename, new_book):
    books = load_books(filename)
    books.append(new_book)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def main():
    filename = 'books.json'

    books = load_books(filename)

    print_available_books(books)

    new_book = {
        "назва": "Книга 4",
        "автор": "Автор 3",
        "рік": 2023,
        "наявність": False
    }

    add_book(filename, new_book)
    print("Нова книга додана.")


if __name__ == "__main__":
    main()
