import sqlite3


# Создаём таблицы, если их нет
def create_tables():
    with connect_to_db() as con:
        cursor = con.cursor()

        # Создание таблицы для фильмов
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        release_year INTEGER NOT NULL,
        genre TEXT NOT NULL
        )
        ''')

        # Создание таблицы для актёров
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS actors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        birth_year INTEGER NOT NULL
        )
        ''')

        # Создание таблицы для связи между фильмами и актёрами (movie_cast)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies_cast (
        movie_id INTEGER,
        actor_id INTEGER,
        PRIMARY KEY(movie_id, actor_id),
        FOREIGN KEY(movie_id) REFERENCES movies(id),
        FOREIGN KEY(actor_id) REFERENCES actors(id)
        )
        ''')

        # Сохраняем изменения
        con.commit()


# Подключение к БД
def connect_to_db():
    return sqlite3.connect('cinema.db')


# Добавляем новый фильм
def add_movie():
    title = input("Название фильма:")
    release_year = int(input("Год выпуска фильма:"))
    genre = input("Жанр фильма:")

    with connect_to_db() as con:
        cursor = con.cursor()
        """
        Запись новых данных в табл movies 
        Вместо знаков ? подставляются конкретные значения, передаваемые в виде кортежа
        """
        cursor.execute("INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?)",
                       (title, release_year, genre))
        print("Фильм добавлен")


# Добавляем нового актёра
def add_actor():
    first_name = input("Имя актёра:")
    last_name = input("Фамилия актёра:")
    birth_year = int(input("Год рождения"))
    """
    Запись новых данных в табл actors 
    Вместо знаков ? подставляются конкретные значения, передаваемые в виде кортежа
    """
    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO actors (first_name, last_name, birth_year) VALUES (?, ?, ?)",
                       (first_name, last_name, birth_year))
        con.commit()
    print(f"Актёр {first_name} {last_name} добавлен в БД.")


# Добавляем актёров в фильм
def add_actor_in_movies():
    movie_id = input("Введите id фильма: ")
    actor_id = input("Введите id актёра: ")

    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO movie_cast (movie_id, actor_id) VALUES (?, ?)",
                       (movie_id, actor_id))
        con.commit()

        # Проверим, что запись добавилась в таблицу
        cursor.execute("SELECT * FROM movie_cast WHERE movie_id = ? AND actor_id = ?", (movie_id, actor_id))
        result = cursor.fetchall()
        if result:
            print("Актёр успешно добавлен в фильм.")
        else:
            print("Ошибка: актёр не был добавлен.")



# Показываем все фильмы с актёрами
def view_movies_actor():
    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute('''
            SELECT movies.title, GROUP_CONCAT(actors.first_name || ' ' || actors.last_name) AS actors
            FROM movies
            INNER JOIN movie_cast ON movies.id = movie_cast.movie_id
            INNER JOIN actors ON movie_cast.actor_id = actors.id
            GROUP BY movies.title
        ''')
        movies = cursor.fetchall()

    if movies:  # Если есть фильмы, выводим их
        print("Фильмы и актёры:")
        for movie in movies:
            print(f"Фильмы: {movie[0]}, актёры: {movie[1]}")
    else:
        print("Нет данных для отображения.")



# Функция показывает жанры
def view_unique_genres():
    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute('''
            SELECT DISTINCT genre FROM movies 
        ''')
        rows = cursor.fetchall()
        print("Уникальные жанры:")
        for row in rows:
            print(f"{row[0]}")


# Функция показывает кол во фильмов за жанром
def show_movie_count_by_genre():
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT genre, COUNT(*) FROM movies
            GROUP BY genre
        ''')
        rows = cursor.fetchall()
        print("Жанри и кол во фильмов:")
        for row in rows:
            print(f"{row[0]}: {row[1]}")


# Функция показывает страницы
def show_movies_with_page():
    page = 1
    while True:
        with connect_to_db() as con:
            cursor = con.cursor()
            # Кол во фильмов на странице
            limit = 5
            offset = (page - 1) * limit
            cursor.execute('''
                SELECT title FROM movies
                LIMIT ? OFFSET ?
            ''', (limit, offset)
                           )
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


# Функция для показывает актёров и фильмы
def show_actors_and_movies():
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


# Функция для поиска фильма по его названию
def search_movie_by_title():
    search_keyword = input("Введите ключевое слово для поиска в названии фильма: ")

    with connect_to_db() as con:
        cursor = con.cursor()
        # Используем % для частичного совпадения
        cursor.execute('''
            SELECT title, release_year, genre
            FROM movies
            WHERE title LIKE ?
        ''', ('%' + search_keyword + '%',))  # Используем % для частичного совпадения
        movies = cursor.fetchall()

        if movies:
            print("Найденные фильмы:")
            for movie in movies:
                print(f"Фильм: {movie[0]}, Год: {movie[1]}, Жанр: {movie[2]}")
        else:
            print("Фильмы с таким названием не найдены.")


# Реализация меню
def main_menu():
    create_tables()
    while True:
        print("\n1. Додати фільм")
        print("2. Додати актора")
        print("3. Показати всі фільми з акторами")
        print("4. Показати унікальні жанри")
        print("5. Показати кількість фільмів за жанром")
        print("6. Показати середній рік народження акторів у фільмах певного жанру")
        print("7. Пошук фільму за назвою")
        print("8. Показати фільми (з пагінацією)")
        print("9. Показати імена всіх акторів та назви всіх фільмів")
        print("0. Вихід")

        choice = input("Виберіть дію: ")

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
            print("Ця функція ще не реалізована.")
        elif choice == "7":
            search_movie_by_title()
        elif choice == "8":
            show_movies_with_page()
        elif choice == "9":
            show_actors_and_movies()
        elif choice == "0":
            break
        else:
            print("Не удалось обработать команду , попробуйте ещё раз")


if __name__ == "__main__":
    main_menu()
