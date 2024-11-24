from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    objects = None
    title = models.CharField(max_length=255)  # Заголовок задачи
    description = models.TextField()  # Описание задачи
    due_date = models.DateField()  # Дата выполнения задачи
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)  # Связь с пользователем

    def __str__(self):
        return self.title  # Возвращаем заголовок задачи при отображении объекта
