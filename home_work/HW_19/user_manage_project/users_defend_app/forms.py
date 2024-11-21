from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    """
    Форма регистрации нового пользователя.

    Поля:
        - username (CharField): Имя пользователя.
        - email (EmailField): Адрес электронной почты.
        - password (CharField): Пароль пользователя, отображается как скрытое поле.
        - password_confirm (CharField): Подтверждение пароля, отображается как скрытое поле.

    Методы:
        - clean_password_confirm(): Проверяет совпадение пароля и его подтверждения.
    """
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Пароль"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label="Подтверждение пароля"
    )

    class Meta:
        """
        Метаданные для формы.

        Атрибуты:
            model: Модель, на основе которой создается форма (User).
            fields: Поля, которые будут доступны в форме (username, email, password).
        """
        model = User
        fields = ['username', 'email', 'password']

    def clean_password_confirm(self):
        """
        Проверяет, что пароль и подтверждение пароля совпадают.

        Raises:
            forms.ValidationError: Если пароли не совпадают.

        Returns:
            str: Подтвержденный пароль.
        """
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")
        return password_confirm


class LoginForm(forms.Form):
    """
    Форма входа для пользователя.

    Поля:
        - username (CharField): Имя пользователя.
        - password (CharField): Пароль пользователя, отображается как скрытое поле.
    """
    username = forms.CharField(max_length=150, label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
