from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    # Переопределяем группы с уникальным related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Уникальное имя для обратной связи
        blank=True
    )

    # Переопределяем разрешения с уникальным related_name
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Уникальное имя для обратной связи
        blank=True
    )

    def __str__(self):
        return self.username
