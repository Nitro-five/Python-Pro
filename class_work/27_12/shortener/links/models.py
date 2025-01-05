from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class Link(models.Model):
    """
    Модель для хранения информации о ссылках, как оригинальных, так и коротких.
    Каждый объект Link представляет одну ссылку, включая ее оригинальную версию,
    короткую ссылку, информацию о пользователе, который создал ссылку, и количество кликов.
    """
    original_url = models.URLField(unique=True, verbose_name="Оригинальная ссылка")
    """
    Поле для хранения оригинальной URL-ссылки. Это обязательное поле, которое должно быть уникальным.
    """
    short_url = models.CharField(max_length=8, unique=True, verbose_name="Короткая ссылка")
    """
    Поле для хранения короткой ссылки, которая будет уникальной. Ссылку генерирует система автоматически.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    """
    Поле для связи с пользователем, который создал короткую ссылку. Это необязательное поле.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    """
    Поле для хранения времени создания ссылки. Заполняется автоматически.
    """
    clicks = models.PositiveIntegerField(default=0, verbose_name="Количество кликов")
    """
    Поле для хранения количества кликов по короткой ссылке. Изначально установлено на 0.
    """

    def save(self, *args, **kwargs):
        """
        Метод для сохранения объекта. Если короткая ссылка не была задана, она генерируется автоматически.
        Генерация короткой ссылки происходит с использованием функции get_random_string.
        """
        if not self.short_url:
            self.short_url = get_random_string(8)
        super().save(*args, **kwargs)

class Click(models.Model):
    """
    Модель для хранения информации о кликах по сокращенным ссылкам.
    Каждый объект Click представляет один клик по ссылке, включая информацию о пользователе,
    времени клика, устройстве и стране.
    """
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name="clicks_data")
    """
    Связь с моделью Link. Каждый клик привязан к одной ссылке.
    """
    user_ip = models.GenericIPAddressField()
    """
    Поле для хранения IP-адреса пользователя, который кликнул по ссылке.
    """
    clicked_at = models.DateTimeField(auto_now_add=True)
    """
    Поле для хранения времени клика. Заполняется автоматически при каждом новом клике.
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    """
    Временная метка для клика. Может использоваться для дальнейшего анализа.
    """
    device = models.CharField(max_length=50, default='Unknown')
    """
    Поле для хранения типа устройства (мобильное, ПК и т.д.). По умолчанию установлено 'Unknown'.
    """
    country = models.CharField(max_length=100, default='Unknown')
    """
    Поле для хранения страны пользователя, который кликнул по ссылке. По умолчанию установлено 'Unknown'.
    """
