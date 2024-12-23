from django.db import models

class MyModel(models.Model):
    """
    Модель MyModel предназначена для хранения информации о сущности с именем.
    Это пример простой модели Django, которая может быть расширена для различных нужд.

    Атрибуты:
        name (str): Поле для хранения имени сущности. Максимальная длина — 100 символов.
    """

    # Поле для хранения имени
    name = models.CharField(max_length=100)
