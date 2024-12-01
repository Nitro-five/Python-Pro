from django.shortcuts import render, redirect
from .forms import UserForm


def login_view(request):
    """
    Представление для обработки логина пользователя.

    Обрабатывает POST-запрос с данными формы пользователя, сохраняет имя в cookies,
    а возраст в сессии. После успешной валидации данных пользователя перенаправляет
    на страницу приветствия.

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.

    Возвращает:
        HttpResponse: Ответ с перенаправлением или отрисовка формы.
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # Получаем имя из формы
            name = form.cleaned_data['name']

            # Преобразуем имя в строку, игнорируя неподдерживаемые символы
            name = str(name).encode('utf-8', 'ignore').decode('utf-8')

            # Получаем возраст
            age = form.cleaned_data['age']

            # Создаём ответ с перенаправлением на страницу приветствия
            response = redirect('greeting')

            # Сохраняем имя в cookies (1 час)
            response.set_cookie('name', name, max_age=3600)

            # Сохраняем возраст в сессии
            request.session['age'] = age

            return response
    else:
        form = UserForm()

    return render(request, 'login.html', {'form': form})


def greeting_view(request):
    """
    Представление для отображения страницы приветствия.

    Получает имя пользователя из cookies и возраст из сессии.
    Если оба значения присутствуют, отрисовывает страницу приветствия,
    в противном случае перенаправляет пользователя на страницу логина.

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.

    Возвращает:
        HttpResponse: Ответ с отрисованной страницей или перенаправление.
    """
    name = request.COOKIES.get('name', None)
    age = request.session.get('age', None)

    if name and age:
        return render(request, 'greeting.html', {'name': name, 'age': age})
    else:
        return redirect('login')


def logout_view(request):
    """
    Представление для выхода пользователя.

    Удаляет имя из cookies и возраст из сессии, а затем перенаправляет
    пользователя на страницу логина.

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.

    Возвращает:
        HttpResponse: Ответ с перенаправлением на страницу логина.
    """
    response = redirect('login')
    response.delete_cookie('name')
    del request.session['age']
    return response
