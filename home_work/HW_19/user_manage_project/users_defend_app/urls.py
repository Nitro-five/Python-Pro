from django.urls import path
from . import views

"""
URL-адрес для регистрации пользователя.

- Путь: 'register/'
- Представление: views.register
- Имя маршрута: 'register'
- Путь: 'login/'
- Представление: views.login_view
- Имя маршрута: 'login'
 - Путь: 'logout/'
- Представление: views.logout_view
 - Имя маршрута: 'logout'
"""
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

# Обработчик ошибки 404
handler404 = 'user_manage_project.views.custom_404'
"""
Кастомный обработчик для ошибок 404 (страница не найдена).

- Путь к обработчику: 'user_manage_project.views.custom_404'
"""
