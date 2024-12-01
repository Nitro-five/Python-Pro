from django.urls import path
from . import views

"""
URL-паттерны для аутентификации пользователя.

Обрабатывает запросы для страниц:
    - login/ — страница входа.
    - greeting/ — страница приветствия после успешного входа.
    - logout/ — страница выхода.

Атрибуты:
    path: str — путь URL.
    view: view function — функция представления для обработки запроса.
    name: str — имя URL-шаблона для использования в шаблонах и редиректах.
"""

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('greeting/', views.greeting_view, name='greeting'),
    path('logout/', views.logout_view, name='logout'),
]
