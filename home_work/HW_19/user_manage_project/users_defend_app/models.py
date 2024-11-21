from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель пользователя, унаследованная от AbstractUser, с переопределением полей
    и добавлением уникальных имен для обратных связей в ManyToMany полях.

    Атрибуты:
        username (CharField): Уникальное имя пользователя с максимальной длиной 150 символов.
        email (EmailField): Уникальный адрес электронной почты.
        password (CharField): Поле для хранения пароля с максимальной длиной 255 символов.
        groups (ManyToManyField): Связь с моделью 'auth.Group', имеет уникальное related_name 'custom_user_set'.
        user_permissions (ManyToManyField): Связь с моделью 'auth.Permission', имеет уникальное related_name 'custom_user_permissions_set'.
    """

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Уникальное имя для обратной связи
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Уникальное имя для обратной связи
        blank=True
    )

    def __str__(self):
        """
        Возвращает строковое представление модели пользователя.

        Returns:
            str: Имя пользователя (username).
        """
        return self.username
