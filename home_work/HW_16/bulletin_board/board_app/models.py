from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Модель профиля пользователя, связанная с встроенной моделью User.

    Атрибуты:
        user (OneToOneField): Связь с пользователем.
        phone_number (CharField): Номер телефона пользователя (необязательное поле).
        address (TextField): Адрес пользователя (необязательное поле).
    """
    # Связь с пользователем
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Возвращает строковое представление профиля пользователя.

        Возвращает:
            str: Имя пользователя.
        """
        return self.user.username


class Category(models.Model):
    """
    Модель категории для объявлений.

    Атрибуты:
        name (CharField): Уникальное название категории.
        description (TextField): Описание категории.
    """
    # Уникальное название категории
    name = models.CharField(max_length=100, unique=True)
    # Описание категории
    description = models.TextField()

    def __str__(self):
        """
        Возвращает строковое представление категории.

        Возвращает:
            str: Название категории.
        """
        return self.name


class Ad(models.Model):
    """
    Модель объявления на доске объявлений.

    Атрибуты:
        title (CharField): Заголовок объявления.
        description (TextField): Описание объявления.
        price (DecimalField): Цена объявления.
        created_at (DateTimeField): Дата и время создания объявления.
        updated_at (DateTimeField): Дата и время последнего обновления.
        is_active (BooleanField): Статус активности объявления.
        user (ForeignKey): Связь с пользователем, который создал объявление.
        category (ForeignKey): Связь с категорией, к которой относится объявление.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, related_name='ads', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='ads', on_delete=models.CASCADE)

    def clean(self):
        """
        Валидация поля price.

        Проверяет, чтобы цена была положительным числом. Если цена меньше или равна нулю,
        возникает исключение ValidationError.
        """
        if self.price <= 0:
            raise ValidationError('Цена должна быть положительным числом.')

    def __str__(self):
        """
        Возвращает строковое представление объявления.

        Возвращает:
            str: Заголовок объявления.
        """
        return self.title

    def short_description(self):
        """
        Метод для получения краткого описания объявления (первые 100 символов).

        Возвращает:
            str: Краткое описание объявления.
        """
        return self.description[:100]

    def deactivate_after_30_days(self):
        """
        Метод для деактивации объявления через 30 дней после его создания.

        Если с момента создания объявления прошло 30 дней, оно автоматически
        становится неактивным.
        """
        from django.utils import timezone
        if self.created_at + timezone.timedelta(days=30) < timezone.now():
            self.is_active = False
            self.save()


class Comment(models.Model):
    """
    Модель комментария к объявлению.

    Атрибуты:
        content (TextField): Текст комментария.
        created_at (DateTimeField): Дата и время создания комментария.
        ad (ForeignKey): Связь с объявлением, к которому был оставлен комментарий.
        user (ForeignKey): Связь с пользователем, который оставил комментарий.
    """
    # Текст комментария
    content = models.TextField()
    # Дата и время создания
    created_at = models.DateTimeField(auto_now_add=True)
    # Связь с объявлением
    ad = models.ForeignKey(Ad, related_name='comments', on_delete=models.CASCADE)
    # Связь с пользователем
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        """
        Возвращает строковое представление комментария.

        Возвращает:
            str: Сообщение о комментарии с именем пользователя и заголовком объявления.
        """
        return f"Комментарий от {self.user.username} к объявлению {self.ad.title}"
