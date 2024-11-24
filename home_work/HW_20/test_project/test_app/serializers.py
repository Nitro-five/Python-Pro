from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task
from datetime import date


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.

    Этот сериализатор используется для представления пользователя с полями:
    - 'username' (имя пользователя)
    - 'email' (электронная почта)
    """

    class Meta:
        model = User
        fields = ['username', 'email']


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Task.

    Этот сериализатор используется для представления задачи с полями:
    - 'title' (заголовок задачи)
    - 'description' (описание задачи)
    - 'due_date' (дата выполнения задачи)

    Включает кастомную валидацию для поля due_date, чтобы предотвратить установку даты в прошлом.
    """

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

    @staticmethod
    def validate_due_date(value):
        """
        Проверка поля due_date, чтобы дата не была в прошлом.

        Если дата выполнения задачи меньше текущей, возникает ошибка валидации.

        Args:
            value (date): дата выполнения задачи.

        Returns:
            value (date): дата, если она валидна.

        Raises:
            serializers.ValidationError: если дата меньше текущей.
        """
        if value < date.today():
            raise serializers.ValidationError("Дата не може бути в прошлом.")
        return value
