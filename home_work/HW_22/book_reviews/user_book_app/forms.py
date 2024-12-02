from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Форма для создания и редактирования отзыва о книге.

    Используется для ввода данных отзыва, таких как книга, рейтинг и комментарий.

    Атрибуты:
        book (ForeignKey): Книга, к которой относится отзыв.
        rating (IntegerField): Рейтинг книги от 1 до 5.
        comment (TextField): Комментарий к книге.
    """
    class Meta:
        model = Review
        fields = ['book', 'rating', 'comment']  # Поля, которые будут доступны в форме
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }


class CustomUserCreationForm(UserCreationForm):
    """
    Форма для регистрации нового пользователя.

    Расширяет стандартную форму UserCreationForm, добавляя поле для email и настраивая
    внешний вид формы.

    Атрибуты:
        email (EmailField): Поле для ввода email пользователя.
    """
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        """
        Инициализация формы, добавление CSS-класса 'form-control' ко всем полям формы.

        Аргументы:
            *args: Позиционные аргументы.
            **kwargs: Ключевые аргументы.
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
