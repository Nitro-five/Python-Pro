from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


def register(request):
    """
    Обрабатывает запросы на регистрацию нового пользователя.

    При POST-запросе:
        - Проверяет валидность формы регистрации.
        - Сохраняет пользователя при успешной валидации.
        - Отображает сообщение об успешной регистрации или ошибки.

    При GET-запросе:
        - Возвращает пустую форму регистрации.

    Args:
        request: HTTP-запрос.

    Returns:
        HttpResponse: Рендеринг страницы регистрации с формой.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)  # Используем кастомную форму регистрации
        if form.is_valid():
            form.save()  # Сохраняем нового пользователя
            messages.success(request, 'Регистрация прошла успешно.')
            return redirect('login')  # Перенаправляем на страницу логина
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = RegisterForm()  # Пустая форма для GET-запроса

    return render(request, 'register.html', {'form': form})


def login_view(request):
    """
    Обрабатывает запросы на вход пользователя в систему.

    При POST-запросе:
        - Проверяет данные в форме авторизации.
        - Выполняет вход пользователя при успешной валидации.
        - Перенаправляет на главную страницу или отображает ошибки.

    При GET-запросе:
        - Возвращает пустую форму авторизации.

    Args:
        request: HTTP-запрос.

    Returns:
        HttpResponse: Рендеринг страницы логина с формой.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Получаем объект пользователя
            login(request, user)  # Авторизуем пользователя
            return redirect('home')  # Перенаправляем на главную страницу
        else:
            messages.error(request, "Неверные данные для входа.")
    else:
        form = AuthenticationForm()  # Пустая форма для GET-запроса

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """
    Обрабатывает запросы на выход пользователя из системы.

    Args:
        request: HTTP-запрос.

    Returns:
        HttpResponseRedirect: Перенаправление на страницу логина.
    """
    logout(request)  # Выход из системы
    return redirect('login')  # Перенаправляем на страницу входа


def custom_404(request, exception):
    """
    Отображает кастомную страницу ошибки 404.

    Args:
        request: HTTP-запрос.
        exception: Исключение, вызвавшее ошибку.

    Returns:
        HttpResponse: Рендеринг страницы 404 с кодом статуса 404.
    """
    return render(request, '404.html', {}, status=404)
