from flask import Blueprint, request, jsonify
from app.models import Film, Director
from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models import User
from app.extensions import db

# Создание главного blueprint для всех маршрутов
main = Blueprint('main', __name__)

# Маршрут для добавления нового режиссера в базу данных
@main.route('/add-director', methods=['POST'])
def add_director():
    """
    Добавление нового режиссера в базу данных.

    Ожидает JSON с ключом 'name', который является именем нового режиссера.
    Если имя не предоставлено, возвращает ошибку 400.

    Returns:
        JSON: Ответ с ID и именем нового режиссера.
    """
    data = request.get_json()
    name = data['name']
    if not name:
        return jsonify({"error: name is required"}), 400
    director = Director(name=name)
    db.session.add(director)
    db.session.commit()
    return jsonify({"id": director.id, "name": director.name}), 201

# Маршрут для получения списка всех режиссеров
@main.route('/directors-list', methods=['GET'])
def get_directors():
    """
    Получение списка всех режиссеров из базы данных.

    Возвращает JSON со списком всех режиссеров, их ID и именами.

    Returns:
        JSON: Список всех режиссеров.
    """
    directors = Director.query.all()
    result = [{"id": d.id, "name": d.name} for d in directors]
    return jsonify(result), 200

# Маршрут для обновления информации о режиссере
@main.route('/update-director/<int:director_id>', methods=['PUT'])
def update_director(director_id):
    """
    Обновление информации о существующем режиссере.

    Ожидает JSON с новым именем режиссера. Если имя предоставлено, обновляет его в базе данных.

    Args:
        director_id (int): ID режиссера, информацию о котором нужно обновить.

    Returns:
        JSON: Сообщение о успешном обновлении.
    """
    director = Director.query.get_or_404(director_id)
    data = request.get_json()
    name = data['name']
    if name:
        director.name = name
    db.session.commit()
    return jsonify({"message": "director updated successfully"}), 200

# Маршрут для удаления режиссера из базы данных
@main.route('/director-delete/<int:director_id>', methods=['DELETE'])
def delete_director(director_id):
    """
    Удаление режиссера из базы данных. Если режиссер связан с фильмами, их режиссера меняют на 'unknown'.

    Args:
        director_id (int): ID режиссера, которого нужно удалить.

    Returns:
        JSON: Сообщение о том, что режиссер был успешно удален.
    """
    director = Director.query.get(director_id)
    if not director:
        return jsonify({"error": "director not found"}), 404
    unknown = director.query.filter_by(name="unknown").first()
    if not unknown:
        unknown = Director(name="unknown")
        db.session.add(unknown)
        db.session.commit()
    for film in director.films:
        film.director_id = unknown.id
        db.session.add(film)
    db.session.delete(director)
    db.session.commit()
    return jsonify({"message": "director deleted successfully"}), 200

# Маршрут для добавления нового фильма
@main.route('/films', methods=['POST'])
def add_films():
    """
    Добавление нового фильма в базу данных.

    Ожидает JSON с полями 'title', 'release_year', 'rating', 'director_id'.
    Если все данные присутствуют, создает новый фильм и сохраняет его в базе данных.

    Returns:
        JSON: Ответ с ID и названием нового фильма.
    """
    data = request.get_json()
    title = data.get('title')
    release_year = data.get('release_year')
    rating = data.get('rating')
    director_id = data.get('director_id')
    if not all([title, release_year, rating, director_id]):
        return jsonify({"error": "all fields are required"}), 400
    film = Film(title=title, release_year=int(release_year), director_id=int(director_id), rating=float(rating))
    db.session.add(film)
    db.session.commit()
    return jsonify({"id": film.id, "title": film.title}), 201

# Маршрут для получения списка всех фильмов
@main.route('/films-list', methods=['GET'])
def get_films():
    """
    Получение списка всех фильмов с их деталями.

    Возвращает JSON со списком всех фильмов, их ID, названием, годом выпуска, рейтингом и именем режиссера.

    Returns:
        JSON: Список всех фильмов.
    """
    films = Film.query.all()
    result = [{
        "id": f.id,
        "title": f.title,
        "release_year": f.release_year,
        "rating": f.rating,
        "director": f.director.name,
    } for f in films]
    return jsonify(result), 200

# Маршрут для удаления фильма
@main.route('/delete-film/<int:film_id>', methods=['DELETE'])
def delete_film(film_id):
    """
    Удаление фильма из базы данных.

    Если фильм найден, он удаляется. В случае ошибки возвращается ошибка 500.

    Args:
        film_id (int): ID фильма, который нужно удалить.

    Returns:
        JSON: Сообщение о том, что фильм был удален.
    """
    film = Film.query.get(film_id)
    if not film:
        return jsonify({"error": "film not found"}), 404
    try:
        db.session.delete(film)
        db.session.commit()
        return jsonify({"message": "film deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Маршрут для обновления данных о фильме
@main.route('/update-film/<int:film_id>', methods=['PUT', 'PATCH'])
def update_film(film_id):
    """
    Обновление данных о фильме.

    Ожидает JSON с новыми данными для фильма. Поддерживает частичное обновление (PUT/PATCH).

    Args:
        film_id (int): ID фильма, который нужно обновить.

    Returns:
        JSON: Сообщение о том, что фильм был обновлен.
    """
    film = Film.query.get(film_id)
    if not film:
        return jsonify({"error": "film not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "no input data provided"}), 400
    try:
        if 'title' in data:
            film.title = data['title']
        if "release_year" in data:
            film.release_year = int(data['release_year'])
        if 'rating' in data:
            film.rating = float(data['rating'])
        if 'description' in data:
            film.description = data['description']
        if 'director_id' in data:
            director = Director.query.get(data['director_id'])
            if not director:
                return jsonify({"error": "director not found"}), 404
            film.director_id = data["director_id"]

        db.session.commit()
        return jsonify({"message": "film updated successfully", "film": {
            "id": film.id,
            "title": film.title,
            "release_year": film.release_year,
            "rating": film.rating,
            "description": film.description,
            "director_id": film.director_id
        }}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Маршрут для входа пользователя
@main.route("/login", methods=["GET", "POST"])
def login():
    """
    Страница входа для пользователя.

    Если метод запроса POST, выполняется проверка данных формы. В случае успешного входа происходит
    перенаправление на главную страницу. В случае неудачи показывается сообщение об ошибке.

    Returns:
        HTML: Страница входа.
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("main.home"))
        flash("Invalid username or password")
    return render_template("login.html")

# Маршрут для регистрации нового пользователя
@main.route("/register", methods=["GET", "POST"])
def register():
    """
    Страница регистрации нового пользователя.

    Если метод запроса POST, происходит создание нового пользователя с хешированным паролем.
    В случае успешной регистрации, пользователь перенаправляется на страницу входа.

    Returns:
        HTML: Страница регистрации.
    """
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email is already registered. Please use a different one.", "danger")
            return redirect(url_for("main.register"))

        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("main.login"))

    return render_template("register.html")

# Маршрут для выхода пользователя
@main.route("/logout")
@login_required
def logout():
    """
    Выход пользователя из системы.

    После выхода пользователя перенаправляет на страницу входа.

    Returns:
        Redirect: Перенаправление на страницу входа.
    """
    logout_user()
    return redirect(url_for("main.login"))

# Главная страница, доступная только после входа
@main.route('/')
@login_required
def home():
    """
    Главная страница, доступная только для авторизованных пользователей.

    Returns:
        HTML: Страница с приветствием.
    """
    return render_template("index.html")
