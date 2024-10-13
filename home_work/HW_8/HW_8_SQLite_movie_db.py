import sqlite3

from mypy.types import names


# Подключение к БД
def connect_to_db():
    return sqlite3.connect('cinema.db')


# Создаём таблицы
def create_tabl():
    with connect_to_db() as con:
        """
        Объект, который позволяет выполнять SQL-запросы на базе данных. 
        Через него можно выполнять запросы, получать результаты.
        """
        cursor = con.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY
        title TEXT NOT NULL
        release_year INTEGER NOT NULL
        genre TEXT NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS actors (
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        birth_year INTEGER NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS movie_cast (
        movie_id INTEGER,
        actor_id INTEGER,
        PRIMARY KEY(movie_id, actor_id),
        FOREIGN KEY(movie_id) REFERENCES movies(id),
        FOREIGN KEY(actor_id) REFERENCES actors(id)
        )
        ''')
        # сохранение изменений в БД
        con.commit()


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
        cursor.execute("INSERT INFO actors (first_name, last_name, birth_year,) VALUES (?, ?, ?)",
                       (first_name, last_name, birth_year))
        con.commit()
    print(f"Актёр {first_name} {last_name} добавлен в БД.")


# Добовлем актёров в фильм
def add_actor_in_movies ():
    movie_id = input("Введите id фильма:")
    first_name_id = input("Ожидаю id для имени актёра")
    last_name_id = input("Ожидаю id для имени фамилии актёра")

    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute("INSERT INFO movie_cast (movie_id, first_name_id, last_name_id) VALUES (?, ?, ?)",
                       (movie_id, first_name_id, last_name_id))

# Показываем все фильмы с актёрами
def view_movies_actor():
    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute('''
            SELECT movie.title, GROUP_CONTACT(actors.first_name, '', actors.last_name)
            FROM movies
            INNER JOIN movies_cast ON movies.id = movie_cast.movie_id
            INNER JOIN actors ON movie_cast.actor_id = actors.id
            GROUP BY movies.id
        ''')
        movies=cursor.fetchall()
    print("Фильмы и актёры:")

    #movie[0] - это первый элемент этого кортежа, который содержит название фильма
    #movie[1] - это второй элемент кортежа, который содержит список актеров

    for movie in movies:
        print(f"Фільм: {movie[0]}, Актори: {movie[1]}")

# Функция показывает жанры
def view_unique_genres():
    with connect_to_db() as con:
        cursor = con.cursor()
        cursor.execute('''
            SELECT DISTINCT genre FORM movies 
        ''')
        rows = cursor.fetchall()
        print("Уникальные жанры:")
        for row in rows:
            print(f"{row[0]}")




