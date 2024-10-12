import sqlite3


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
        gener TEXT NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS actors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
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
