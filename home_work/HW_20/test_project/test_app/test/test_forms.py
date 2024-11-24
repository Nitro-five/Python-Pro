import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from ..forms import TaskForm


@pytest.mark.django_db
def test_valid_task_form():
    """
    Тест для проверки валидной формы создания задачи.

    В этом тесте:
    - Создаётся пользователь.
    - Заполняются данные для создания задачи (с завтрашней датой).
    - Форма проверяется на валидность.
    - Проверяется, что данные после очистки соответствуют введённым.
    """
    user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

    data = {
        'title': 'New Task',
        'description': 'Description of the task.',
        'due_date': timezone.localdate() + timezone.timedelta(days=1),  # Завтрашняя дата
    }

    form = TaskForm(data=data)
    assert form.is_valid()

    cleaned_data = form.cleaned_data
    assert cleaned_data['title'] == data['title']
    assert cleaned_data['description'] == data['description']
    assert cleaned_data['due_date'] == data['due_date']


@pytest.mark.django_db
def test_invalid_task_form_empty_fields():
    """
    Тест для проверки формы с пустыми обязательными полями.

    В этом тесте:
    - Проверяется, что форма с пустыми полями не является валидной.
    - Проверяется наличие ошибок в обязательных полях (title, description, due_date).
    """
    data = {
        'title': '',
        'description': '',
        'due_date': '',
    }

    form = TaskForm(data=data)
    assert not form.is_valid()

    assert 'title' in form.errors
    assert 'description' in form.errors
    assert 'due_date' in form.errors


@pytest.mark.django_db
def test_due_date_in_past():
    """
    Тест для проверки формы с датой выполнения задачи в прошлом.

    В этом тесте:
    - Проверяется, что дата выполнения задачи не может быть в прошлом.
    - Проверяется, что форма с такой датой не будет валидной.
    """
    data = {
        'title': 'New Task',
        'description': 'Description of the task.',
        'due_date': timezone.localdate() - timezone.timedelta(days=1),  # Дата в прошлом
    }

    form = TaskForm(data=data)
    assert not form.is_valid()
    assert 'due_date' in form.errors  # Ошибка должна быть на поле due_date
