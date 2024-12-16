from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Task.

    Преобразует данные задачи из формата Python в формат JSON и наоборот.

    Атрибуты:
        id (int): ID задачи.
        title (str): Название задачи.
        description (str): Описание задачи.
        created_at (datetime): Время создания задачи.
        due_date (datetime): Дата и время, когда задача должна быть выполнена.
        status (str): Статус задачи.
        user (int): ID пользователя, который создал задачу.
    """

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'due_date', 'status', 'user']


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.

    Преобразует данные пользователя из формата Python в формат JSON и наоборот.

    Атрибуты:
        username (str): Имя пользователя.
        password (str): Пароль пользователя.
    """

    class Meta:
        model = User
        fields = ('username', 'password')
