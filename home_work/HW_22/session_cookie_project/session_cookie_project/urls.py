from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_to_login(request):
    """
    Представление для перенаправления пользователя на страницу входа.

    Перенаправляет запросы с корня сайта ('/') на страницу входа ('/login').

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.

    Возвращает:
        HttpResponseRedirect: Перенаправление на страницу входа.
    """
    return redirect('login')

    """
    Основные маршруты URL проекта.

    Включает маршруты для административной панели, страницы входа и перенаправление с корня.

    Атрибуты:
        path: str — путь URL.
        view: view function — функция представления для обработки запроса.
        include: str — включение маршрутов из другого приложения.
    """


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', redirect_to_login),
    path('login/', include('user_app.urls')), ]
