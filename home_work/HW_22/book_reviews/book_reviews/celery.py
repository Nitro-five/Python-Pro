from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

def make_celery():
    """
    Функция для создания экземпляра приложения Celery и настройки его для работы с Django.

    Эта функция настраивает приложение Celery, указывая настройки из конфигурации Django
    и автоматически открывает задачи для обнаружения.

    Возвращает:
        Celery: Экземпляр приложения Celery.
    """
    # Настройка Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_reviews.settings')

    app = Celery('book_reviews')

    # Конфигурация Celery
    app.config_from_object('django.conf:settings', namespace='CELERY')

    # Автоматическое открытие задач
    app.autodiscover_tasks()

    return app

# Инициализация Celery
app = make_celery()
