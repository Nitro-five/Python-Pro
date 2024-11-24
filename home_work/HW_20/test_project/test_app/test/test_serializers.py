import pytest
from datetime import date, timedelta
from django.contrib.auth.models import User
from home_work.HW_20.test_project.test_app.serializers import TaskSerializer
from home_work.HW_20.test_project.test_app.models import Task


# Тест на валидные данные
@pytest.mark.django_db
def test_valid_task_with_user_serializer():
    user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

    task_data = {
        'title': 'Test Task',
        'description': 'Test description.',
        'due_date': date.today() + timedelta(days=1),  # Задача должна быть на завтра
        'user': {
            'username': 'testuser',
            'email': 'test@example.com'
        }
    }

    serializer = TaskSerializer(data=task_data)
    assert serializer.is_valid()  # Ожидаем, что сериализатор будет валиден


# Тест на некорректного пользователя (пользователь не существует)
@pytest.mark.django_db
def test_invalid_task_with_invalid_user():
    task_data = {
        'title': 'Test Task',
        'description': 'Test description.',
        'due_date': date.today() + timedelta(days=1),
        'user': {
            'username': 'invaliduser',  # Пользователь с таким именем не существует
            'email': 'invalid@example.com'
        }
    }

    serializer = TaskSerializer(data=task_data)
    assert not serializer.is_valid()  # Ожидаем, что сериализатор не будет валиден
    assert 'user' in serializer.errors  # Ошибка должна быть в поле user


# Тест на отсутствие обязательного поля 'title'
@pytest.mark.django_db
def test_invalid_task_serializer_missing_title():
    task_data = {
        'description': 'Test description.',
        'due_date': date.today() + timedelta(days=1),  # Завтрашняя дата
    }

    serializer = TaskSerializer(data=task_data)
    assert not serializer.is_valid()  # Ожидаем, что сериализатор не будет валиден
    assert 'title' in serializer.errors  # Ошибка должна быть в поле title


# Тест на некорректную дату выполнения (в прошлом)
@pytest.mark.django_db
def test_invalid_due_date_in_past():
    task_data = {
        'title': 'Test Task',
        'description': 'Test description.',
        'due_date': date.today() - timedelta(days=1),  # Дата в прошлом
    }

    serializer = TaskSerializer(data=task_data)
    assert not serializer.is_valid()  # Ожидаем, что сериализатор не будет валиден
    assert 'due_date' in serializer.errors  # Ошибка должна быть в поле due_date
