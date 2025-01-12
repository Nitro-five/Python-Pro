from app.extensions import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """
    Модель пользователя, которая используется для хранения данных о пользователе в базе данных.

    Эта модель наследует от `UserMixin`, который предоставляет методы для работы с сессиями и аутентификацией пользователей
    (например, для Flask-Login).

    Атрибуты:
        id (int): Уникальный идентификатор пользователя (первичный ключ).
        username (str): Уникальное имя пользователя.
        email (str): Уникальный адрес электронной почты пользователя.
        password (str): Пароль пользователя (хранится в зашифрованном виде).
    """
    id = db.Column(db.Integer, primary_key=True)  # Уникальный идентификатор пользователя
    username = db.Column(db.String(80), unique=True, nullable=False)  # Имя пользователя
    email = db.Column(db.String(120), unique=True, nullable=False)  # Электронная почта пользователя
    password = db.Column(db.String(128), nullable=False)  # Зашифрованный пароль пользователя


class Director(db.Model):
    """
    Модель режиссера, которая используется для хранения данных о режиссерах в базе данных.

    Атрибуты:
        id (int): Уникальный идентификатор режиссера (первичный ключ).
        name (str): Имя режиссера (должно быть уникальным).
    """
    __tablename__ = 'directors'  # Указываем имя таблицы в базе данных

    id = db.Column(db.Integer, primary_key=True)  # Уникальный идентификатор режиссера
    name = db.Column(db.String(80), unique=True, nullable=False)  # Имя режиссера

    def __repr__(self):
        """
        Представление объекта режиссера.

        Этот метод используется для отображения строки, которая представляет объект режиссера,
        обычно используется в отладке или при выводе объектов на экран.

        Returns:
            str: Представление имени режиссера в виде строки.
        """
        return f'<Director {self.name}>'


class Film(db.Model):
    """
    Модель фильма, которая используется для хранения данных о фильмах в базе данных.

    Атрибуты:
        id (int): Уникальный идентификатор фильма (первичный ключ).
        title (str): Название фильма (должно быть уникальным).
        release_year (int): Год выпуска фильма.
        rating (float): Рейтинг фильма (по умолчанию 0.0).
        poster (str): Путь к изображению постера фильма.
        description (str): Описание фильма.
        director_id (int): Идентификатор режиссера, связанного с фильмом (внешний ключ).
        director (Director): Режиссер фильма (связь с моделью Director).
    """
    __tablename__ = 'films'  # Указываем имя таблицы в базе данных

    id = db.Column(db.Integer, primary_key=True)  # Уникальный идентификатор фильма
    title = db.Column(db.String(80), unique=True, nullable=False)  # Название фильма
    release_year = db.Column(db.Integer, nullable=False)  # Год выпуска фильма
    rating = db.Column(db.Float, nullable=False, default=0.0)  # Рейтинг фильма
    poster = db.Column(db.String(80), unique=True, nullable=False)  # Путь к изображению постера
    description = db.Column(db.Text, unique=True, nullable=False)  # Описание фильма
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'), nullable=False)  # Внешний ключ для режиссера
    director = db.relationship('Director', backref='films', lazy=True)  # Связь с моделью Director

    def __repr__(self):
        """
        Представление объекта фильма.

        Этот метод используется для отображения строки, которая представляет объект фильма,
        обычно используется в отладке или при выводе объектов на экран.

        Returns:
            str: Представление названия фильма в виде строки.
        """
        return f'<Film {self.title}>'
