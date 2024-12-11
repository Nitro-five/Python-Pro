from django.db import models
from elasticsearch_dsl import Document, Text, Date
from elasticsearch_dsl.connections import connections

# Создание соединения с Elasticsearch
connections.create_connection(hosts=['http://localhost:9200'])

class DataDocument(models.Model):
    """
    Модель для представления документа в базе данных.

    Поля:
    - title (CharField): Заголовок документа (максимум 100 символов).
    - description (TextField): Описание документа.
    - created_at (DateTimeField): Дата и время создания документа (заполняется автоматически).
    """
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        """
        Возвращает строковое представление объекта (заголовок документа).
        """
        return self.title
