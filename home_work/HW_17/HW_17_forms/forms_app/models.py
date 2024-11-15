from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Модель профиля пользователя, связанная с пользователем (User).

    В этой модели хранится дополнительная информация о пользователе, которая не входит в стандартную модель User:
    - Биография пользователя (bio)
    - Дата рождения (birth_date)
    - Город проживания (location)
    - Аватар пользователя (avatar)

    Атрибуты:
        user (OneToOneField): Связь с пользователем. Один профиль может быть привязан только к одному пользователю.
        bio (TextField): Биография пользователя. Поле может быть пустым.
        birth_date (DateField): Дата рождения пользователя. Может быть пустым.
        location (CharField): Город проживания пользователя. Может быть пустым.
        avatar (ImageField): Аватар пользователя. Может быть пустым, изображение загружается в папку 'avatars/'.

    Методы:
        __str__(self): Возвращает имя пользователя (username), связанное с профилем.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        """
        Возвращает строковое представление объекта.

        Для модели UserProfile строковое представление - это имя пользователя, связанного с профилем.

        Возвращает:
            str: Имя пользователя (username) связанного с этим профилем.
        """
        return self.user.username
