from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Определение кастомного поля UpperCaseTextField
class UpperCaseTextField(models.Field):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 255)
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'varchar(%s)' % self.max_length

    def get_prep_value(self, value):
        if value is not None:
            return value.upper()
        return value


class AnotherModel(models.Model):
    name = models.CharField(max_length=100)


class MyModel(models.Model):
    objects = None
    name = UpperCaseTextField()  # Используем кастомное поле UpperCaseTextField
    description = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Добавляем внешний ключ на саму модель
    related_model = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def count_characters(self):
        return len(self.description)

    @classmethod
    def custom_sql_query(cls):
        return cls.objects.raw('SELECT * FROM my_custom_app_mymodel WHERE name LIKE %s', ['%test%'])


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )


class RequestMetric(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Request Metric: {self.count} requests"
