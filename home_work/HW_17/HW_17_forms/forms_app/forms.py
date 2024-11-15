from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile


class RegistrationForm(forms.ModelForm):
    """
    Форма для регистрации нового пользователя.

    Включает в себя поля для имени пользователя, email, пароля и подтверждения пароля.
    Реализованы дополнительные проверки:
    - Проверка на совпадение паролей.
    - Проверка на уникальность имени пользователя и email.
    - Проверка минимальной длины пароля.
    """

    # Поля формы для пароля и подтверждения пароля
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password_confirm(self):
        """
        Проверка совпадения пароля и его подтверждения.

        Возвращает подтверждение пароля, если оно совпадает с основным паролем.
        Если пароли не совпадают, выбрасывает исключение ValidationError.
        """
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise ValidationError('Пароли не совпадают.')
        return password_confirm

    def clean_username(self):
        """
        Проверка уникальности имени пользователя.

        Проверяет, существует ли уже пользователь с таким именем. Если существует, выбрасывает исключение ValidationError.
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Это имя уже существует. Выберите другое.')
        return username

    def clean_email(self):
        """
        Проверка уникальности email.

        Проверяет, существует ли уже пользователь с таким email. Если существует, выбрасывает исключение ValidationError.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Этот email уже зарегистрирован.')
        return email

    def clean_password(self):
        """
        Проверка на минимальную длину пароля.

        Убедитесь, что пароль содержит не менее 8 символов. Если пароль слишком короткий, выбрасывает исключение ValidationError.
        """
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('Пароль должен содержать не менее 8 символов.')
        return password


class UserProfileForm(forms.ModelForm):
    """
    Форма для редактирования профиля пользователя.

    Включает в себя поля для биографии, даты рождения, города проживания и аватара.
    """

    class Meta:
        model = UserProfile
        fields = ['bio', 'birth_date', 'location', 'avatar']

    birth_date = forms.DateField(
        widget=forms.TextInput(attrs={'placeholder': 'ДД.ММ.ГГГГ'}),
        input_formats=['%d.%m.%Y']
    )
    """
    Поле для ввода даты рождения. Использует текстовое поле с плейсхолдером и ограничение на формат даты 'ДД.ММ.ГГГГ'.
    """
