from django.shortcuts import render


def home_view(request):
    """
    Обработчик для домашней страницы.

    :param request: HTTP-запрос.
    :return: HTTP-ответ с рендером шаблона 'home.html'.
    """
    return render(request, 'home.html')


def about_view(request):
    """
    Обработчик для страницы "О нас".

    :param request: HTTP-запрос.
    :return: HTTP-ответ с рендером шаблона 'about.html'.
    """
    return render(request, 'about.html')


def contact_view(request):
    """
    Обработчик для страницы "Контакты".

    :param request: HTTP-запрос.
    :return: HTTP-ответ с рендером шаблона 'contact.html'.
    """
    return render(request, 'contact.html')


def post_view(request, id):
    """
    Обработчик для страницы поста.

    :param request: HTTP-запрос.
    :param id: Идентификатор поста.
    :return: HTTP-ответ с рендером шаблона 'post.html' и контекстом, содержащим id поста.
    """
    return render(request, 'post.html', {'id': id})


def profile_view(request, username):
    """
    Обработчик для страницы профиля пользователя.

    :param request: HTTP-запрос.
    :param username: Имя пользователя.
    :return: HTTP-ответ с рендером шаблона 'profile.html' и контекстом, содержащим имя пользователя.
    """
    return render(request, 'profile.html', {'username': username})


def event_view(request, year, month, day):
    """
    Обработчик для страницы события.

    :param request: HTTP-запрос.
    :param year: Год события.
    :param month: Месяц события.
    :param day: День события.
    :return: HTTP-ответ с рендером шаблона 'event.html' и контекстом, содержащим дату события.
    """
    return render(request, 'event.html', {'year': year, 'month': month, 'day': day})
