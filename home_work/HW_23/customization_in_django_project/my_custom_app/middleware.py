import logging
from .models import RequestMetric
from datetime import datetime


class AddCustomHeaderMiddleware:
    """
    Middleware для добавления кастомного заголовка в каждый ответ.
    Этот middleware добавляет заголовок 'X-Custom-Header' со значением 'Hello, World!'
    в каждый HTTP-ответ.
    """

    def __init__(self, get_response):
        """
        Инициализация middleware.

        :param get_response: Функция для получения ответа после обработки запроса.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Обработка запроса и добавление кастомного заголовка в ответ.

        :param request: Входящий HTTP-запрос.
        :return: Ответ с добавленным кастомным заголовком.
        """
        response = self.get_response(request)
        response['X-Custom-Header'] = 'Hello, World!'
        return response


logger = logging.getLogger('django')


class RequestCountMiddleware:
    """
    Middleware для подсчёта количества запросов в логах.
    Этот middleware увеличивает счётчик запросов и логирует его в Django.
    """

    def __init__(self, get_response):
        """
        Инициализация middleware.

        :param get_response: Функция для получения ответа после обработки запроса.
        """
        self.get_response = get_response
        self.request_count = 0

    def __call__(self, request):
        """
        Обработка запроса, увеличение счётчика запросов и логирование.

        :param request: Входящий HTTP-запрос.
        :return: Ответ после обработки запроса.
        """
        self.request_count += 1
        logger.info(f"Request #{self.request_count} received at {datetime.now()}")
        response = self.get_response(request)
        return response


class RequestCountMiddleware:
    """
    Middleware для увеличения счётчика запросов в базе данных и логирования.
    Этот middleware увеличивает счётчик запросов в базе данных и записывает информацию
    в лог с количеством запросов.
    """

    def __init__(self, get_response):
        """
        Инициализация middleware.

        :param get_response: Функция для получения ответа после обработки запроса.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Обработка запроса, увеличение счётчика запросов в базе данных и логирование.

        :param request: Входящий HTTP-запрос.
        :return: Ответ после обработки запроса.
        """
        metric, created = RequestMetric.objects.get_or_create(id=1)
        metric.count += 1
        metric.save()

        logger.info(f"Request #{metric.count} received at {datetime.now()}")
        response = self.get_response(request)
        return response
