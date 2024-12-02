import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from user_book_app import views

app_name = 'user_book_app'
"""
Список URL-путей для приложения user_book_app.

Включает URL-адреса для различных представлений, таких как домашняя страница, вход,
регистрация, отображение книг, статистика авторов, импорт книг и другие.

Атрибуты:
    app_name (str): Имя приложения для использования в пространстве имен (namespace).
    urlpatterns (list): Список путей, которые определяют, какие представления обрабатывают 
                         запросы на определенные URL.
"""
urlpatterns = [
    path('admin/', admin.site.urls),  # Административная панель Django
    path('', views.home, name='home'),  # Домашняя страница
    path('login/', views.login_view, name='login'),  # Страница логина
    path('greeting/', views.greeting_view, name='greeting'),  # Страница приветствия
    path('books/', views.book_list, name='book_list'),  # Страница с книгами
    path('register/', views.register, name='register'),  # Страница регистрации
    path('author_stats/', views.author_stats, name='author_stats'),  # Страница статистики авторов
    path('logout/', views.logout_view, name='logout'),  # Выход из системы
    path('books/import/', views.import_books_view, name='import_books'),  # Импорт книг
    path('__debug__/', include(debug_toolbar.urls)),  # URL для отображения панели отладки (debug toolbar)
]
