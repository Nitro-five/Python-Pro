from flask import Flask
from app.extensions import db, login_manager, migrate
from app.routes import main
from app.models import User
from app.config import Config


# Функция загрузки пользователя по ID для аутентификации.
# Используется Flask-Login для получения данных пользователя из базы данных.
@login_manager.user_loader
def load_user(user_id):
    """
    Загружает пользователя по его идентификатору.

    Эта функция используется Flask-Login для поиска пользователя по
    уникальному идентификатору в базе данных, когда требуется аутентификация.

    Аргументы:
        user_id (int): Идентификатор пользователя.

    Returns:
        User: Объект пользователя с заданным ID, или None, если пользователь не найден.
    """
    return User.query.get(int(user_id))


def create_app():
    """
    Создание и настройка приложения Flask.

    Эта функция инициализирует Flask приложение, настраивает его с
    использованием конфигурации из объекта `Config`, а также подключает
    расширения, такие как SQLAlchemy, Migrate и Flask-Login.

    В процессе работы:
        - Подключаются конфигурационные параметры.
        - Инициализируется база данных.
        - Настраивается миграция базы данных.
        - Регистрируется главный blueprint приложения.
        - Создается таблица базы данных, если она еще не существует.

    Returns:
        Flask: Инициализированное приложение Flask, готовое к запуску.
    """
    # Создание объекта Flask и настройка конфигурации из объекта Config
    app = Flask(__name__)
    app.config.from_object(Config)

    # Настройка подключения к базе данных SQLite для хранения данных о фильмах
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///film_library.db'

    # Отключение отслеживания изменений в базе данных для улучшения производительности
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Инициализация расширений с приложением
    db.init_app(app)  # Инициализация базы данных
    migrate.init_app(app, db)  # Инициализация миграции базы данных
    login_manager.init_app(app)  # Инициализация менеджера аутентификации

    # Регистрация основного blueprint приложения
    app.register_blueprint(main)

    # В этом блоке создаются все таблицы в базе данных
    # если они ещё не были созданы
    with app.app_context():
        db.create_all()

    # Возвращение готового к работе приложения
    return app
