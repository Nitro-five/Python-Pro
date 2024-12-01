from django import forms


class UserForm(forms.Form):
    """
    Форма для ввода имени и возраста пользователя.

    Атрибуты:
        name (CharField): Поле для ввода имени пользователя (максимум 100 символов).
        age (IntegerField): Поле для ввода возраста пользователя.
    """
    name = forms.CharField(max_length=100, label="Ваше имя")
    age = forms.IntegerField(label="Ваш возраст")
