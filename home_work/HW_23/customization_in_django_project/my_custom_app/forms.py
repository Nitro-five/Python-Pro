from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, MyModel


def validate_only_letters(value):
    """
    Проверяет, что значение состоит только из букв.

    :param value: Значение, которое проверяется.
    :raises ValidationError: Если значение содержит символы, отличные от букв.
    """
    if not value.isalpha():
        raise ValidationError('Ожидаем только буквы')


class MyModelForm(forms.ModelForm):
    """
    Форма для модели MyModel. Используется для ввода и валидации данных.

    Поля формы:
    - name: строка, только буквы.
    - description: текстовое описание.
    """

    class Meta:
        model = MyModel
        fields = ['name', 'description']

    name = forms.CharField(validators=[validate_only_letters])


class CustomSelectWidget(forms.Select):
    """
    Кастомный виджет для поля Select с дополнительными аттрибутами.

    Виджет добавляет кастомный класс 'custom-select' для использования в HTML.
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализация кастомного виджета Select.

        :param args: Позиционные аргументы.
        :param kwargs: Ключевые аргументы, включая атрибуты для HTML.
        """
        kwargs['attrs'] = {'class': 'custom-select'}
        super().__init__(*args, **kwargs)


class CustomUserCreationForm(UserCreationForm):
    """
    Форма для создания пользователя с дополнительным полем для номера телефона.

    Поля формы:
    - username: имя пользователя.
    - phone_number: номер телефона.
    - password1: пароль.
    - password2: подтверждение пароля.
    """

    phone_number = forms.CharField(max_length=15, required=True, help_text="Введите номер телефона")

    class Meta:
        model = CustomUser
        fields = ('username', 'phone_number', 'password1', 'password2')
