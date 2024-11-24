from django.urls import path
from . import views

urlpatterns = [
    # Путь для создания новой задачи
    path('create/', views.create_task, name='create_task'),  # Страница для создания новой задачи

    # Путь для отображения списка задач пользователя
    path('', views.task_list, name='task_list'),  # Главная страница с списком задач

    # Путь для регистрации нового пользователя
    path('signup/', views.signup, name='signup'),  # Страница для регистрации нового пользователя
]
