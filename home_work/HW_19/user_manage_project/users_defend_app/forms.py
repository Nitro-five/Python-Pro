from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Пароль"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label="Подтверждение пароля"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        # Проверка совпадения паролей
        if password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")
        return password_confirm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
