import sqlite3
from datetime import datetime


def create_tables():
    """Создает необходимые таблицы в базе данных SQLite, если они не существуют.

    Создаваемые таблицы:
        - movies: Содержит данные о фильмах (id, title, release_year, genre).
        - actors: Содержит данные об актерах (id, first_name, last_name, birth_year).
        - movies_cast: Связующая таблица для ассоциации фильмов с актерами.
    """
    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        release_year INTEGER NOT NULL,
        genre TEXT NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS actors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        birth_year INTEGER NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies_cast (
        movie_id INTEGER,
        actor_id INTEGER,
        PRIMARY KEY(movie_id, actor_id),
        FOREIGN KEY(movie_id) REFERENCES movies(id),
        FOREIGN KEY(actor_id) REFERENCES actors(id)
        )
        ''')

        con.commit()


def connect_to_db():
    """Устанавливает соединение с базой данных SQLite (cinema.db).

    Возвращает:
        sqlite3.Connection: Объект соединения с базой данных.
    """
    return sqlite3.connect('cinema.db')


def add_movie():
    """Запрашивает у пользователя данные о фильме (название, год выпуска, жанр) и добавляет новый фильм в базу данных."""
    title = input("Название фильма:")
    release_year = int(input("Год выпуска фильма:"))
    genre = input("Жанр фильма:")

    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?)",
                       (title, release_year, genre))
        print("Фильм добавлен")


def add_actor():
    """Запрашивает у пользователя данные об актере (имя, фамилия, год рождения) и добавляет нового актера в базу данных."""
    first_name = input("Имя актёра:")
    last_name = input("Фамилия актёра:")
    birth_year = int(input("Год рождения"))

    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO actors (first_name, last_name, birth_year) VALUES (?, ?, ?)",
                       (first_name, last_name, birth_year))
        con.commit()
    print(f"Актёр {first_name} {last_name} добавлен в БД.")


def add_actor_in_movies():
    """Позволяет пользователю ассоциировать актера с фильмом.

    Запрашивает ID фильма и ID актера. Проверяет существование обоих перед добавлением связи
    в таблицу movies_cast.
    """
    try:
        movie_id = int(input("Введите ID фильма: "))
        actor_id = int(input("Введите ID актёра: "))

        with connect_to_db() as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
            if not cursor.fetchone():
                print("Ошибка: фильм с таким ID не найден.")
                return

            cursor.execute("SELECT * FROM actors WHERE id = ?", (actor_id,))
            if not cursor.fetchone():
                print("Ошибка: актёр с таким ID не найден.")
                return

            cursor.execute("INSERT INTO movies_cast (movie_id, actor_id) VALUES (?, ?)",
                           (movie_id, actor_id))
            con.commit()

            print("Актёр успешно добавлен в фильм.")
    except ValueError:
        print("Ошибка: введите корректный номер ID.")
    except sqlite3.IntegrityError:
        print("Ошибка: актёр уже связан с этим фильмом.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def get_unique_genres():
    """Извлекает список уникальных жанров фильмов из базы данных.

    Возвращает:
        list: Список уникальных жанров.
    """
    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute('SELECT DISTINCT genre FROM movies')
        return [row[0] for row in cursor.fetchall()]


def average_age_of_actors_by_genre():
    """Вычисляет и отображает средний возраст актеров для выбранного жанра."""
    genres = get_unique_genres()  # Получаем уникальные жанры

    if not genres:
        print("Нет доступных жанров.")
        return

    print("Доступные жанры:")
    for index, genre in enumerate(genres, start=1):
        print(f"{index}. {genre}")

    try:
        choice = int(input("Выберите номер жанра (от 1 до {}): ".format(len(genres))))
        '''проверка: если введенное значение choice меньше 1 или больше количества жанров, 
        то это считается некорректным выбором'''

        if choice < 1 or choice > len(genres):
            print(f"Неверный выбор. Пожалуйста, выберите номер от 1 до {len(genres)}.")
            return

        genre = genres[choice - 1]
    except ValueError:
        print("Ошибка: введите корректный номер.")
        return

    # Логика для подсчёта среднего возраста актёров по выбранному жанру
    current_year = datetime.now().year

    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute('''
            SELECT birth_year 
            FROM actors
            INNER JOIN movies_cast ON actors.id = movies_cast.actor_id
            INNER JOIN movies ON movies_cast.movie_id = movies.id
            WHERE movies.genre = ?
        ''', (genre,))

        birth_years = cursor.fetchall()

    if not birth_years:
        print(f"Нет актеров для жанра '{genre}'.")
        return

    ages = [current_year - birth_year[0] for birth_year in birth_years]
    average_age = sum(ages) / len(ages)

    print(f'Средний возраст актёров в жанре "{genre}": {average_age:.2f} лет')


def view_movies_actor():
    """Отображает все фильмы вместе с их связанными актерами."""
    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute('''
            SELECT movies.title, GROUP_CONCAT(actors.first_name || ' ' || actors.last_name) AS actors
            FROM movies
            INNER JOIN movies_cast ON movies.id = movies_cast.movie_id
            INNER JOIN actors ON movies_cast.actor_id = actors.id
            GROUP BY movies.title
        ''')
        movies = cursor.fetchall()

    if movies:
        print("Фильмы и актёры:")
        for movie in movies:
            print(f"Фильмы: {movie[0]}, актёры: {movie[1]}")
    else:
        print("Нет данных для отображения.")


def view_unique_genres():
    """Извлекает и отображает уникальные жанры фильмов из базы данных."""
    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute('SELECT DISTINCT genre FROM movies')
        rows = cursor.fetchall()
        print("Уникальные жанры:")
        for row in rows:
            print(f"{row[0]}")


def show_movie_count_by_genre():
    """Считает и отображает количество фильмов по жанрам."""
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT genre, COUNT(*) FROM movies GROUP BY genre')
        rows = cursor.fetchall()
        print("Жанры и количество фильмов:")
        for row in rows:
            print(f"{row[0]}: {row[1]}")


def show_movies_with_page():
    """Отображает фильмы в пагинированном формате (по 5 фильмов на странице)."""
    page = 1
    while True:
        with connect_to_db() as con:
            cursor = con.cursor()
            limit = 5
            offset = (page - 1) * limit
            cursor.execute('SELECT title FROM movies LIMIT ? OFFSET ?', (limit, offset))
            rows = cursor.fetchall()
            if not rows:
                print('Последняя страница')
                break
            print(f"Страница {page}:")
            for row in rows:
                print(row[0])

        action = input("Нажмите 'n' для следующей страницы или 'q' для выхода: ")
        if action == 'n':
            page += 1
        elif action == 'q':
            break


def show_actors_and_movies():
    """Отображает все имена актеров и названия фильмов в базе данных."""
    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute('''
            SELECT first_name || ' ' || last_name AS actor_name FROM actors
            UNION
            SELECT title AS movie_title FROM movies        
        ''')
        rows = cursor.fetchall()
        print("Актёры и фильмы:")
        for row in rows:
            print(row[0])


def search_movie_by_title():
    """Позволяет пользователю искать фильмы по названию, используя ключевое слово."""
    search_keyword = input("Введите ключевое слово для поиска в названии фильма: ")

    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute('''
            SELECT title, release_year, genre
            FROM movies
            WHERE title LIKE ?
        ''', ('%' + search_keyword + '%',))
        movies = cursor.fetchall()

        if movies:
            print("Найденные фильмы:")
            for movie in movies:
                print(f"Фильм: {movie[0]}, Год: {movie[1]}, Жанр: {movie[2]}")
        else:
            print("Фильмы с таким названием не найдены.")


def view_all_actors():
    """Извлекает и отображает всех актеров в базе данных вместе с их ID."""
    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute("SELECT id, first_name, last_name FROM actors")
        rows = cursor.fetchall()
        print("Актёры в базе данных:")
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}")


def view_all_movies():
    """Извлекает и отображает все фильмы в базе данных вместе с их ID."""
    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute("SELECT id, title FROM movies")
        rows = cursor.fetchall()
        print("Фильмы в базе данных:")
        for row in rows:
            print(f"ID: {row[0]}, Название: {row[1]}")


def main_menu():
    """Отображает главное меню и обрабатывает действия пользователя."""
    create_tables()
    while True:
        print("\n1. Добавить фильм")
        print("2. Добавить актера")
        print("3. Показать все фильмы с актерами")
        print("4. Показать уникальные жанры")
        print("5. Показать количество фильмов по жанрам")
        print("6. Показать средний год рождения актеров")
        print("7. Поиск фильма по названию")
        print("8. Показать фильмы (с пагинацией)")
        print("9. Показать имена всех актеров и названия всех фильмов")
        print("10. Связать актеров и фильм")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            add_actor()
        elif choice == "3":
            view_movies_actor()
        elif choice == "4":
            view_unique_genres()
        elif choice == "5":
            show_movie_count_by_genre()
        elif choice == "6":
            average_age_of_actors_by_genre()
        elif choice == "7":
            search_movie_by_title()
        elif choice == "8":
            show_movies_with_page()
        elif choice == "9":
            show_actors_and_movies()
        elif choice == "10":
            view_all_actors(), view_all_movies(), add_actor_in_movies()
        elif choice == "0":
            break
        else:
            print("Не удалось обработать команду, попробуйте еще раз")


if __name__ == "__main__":
    view_unique_genres()
    main_menu()
