from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели отзыва.

    Определяет настройки отображения, фильтрации и поиска отзывов в админке.

    Атрибуты:
        list_display (tuple): Поля, которые будут отображаться в списке объектов.
        list_filter (tuple): Поля, по которым можно фильтровать объекты в админке.
        search_fields (tuple): Поля, по которым можно искать объекты в админке.
    """
    list_display = ('book', 'user', 'rating', 'comment', 'created_at')
    list_filter = ('rating', 'book', 'user')
    search_fields = ('book__title', 'user__username', 'comment')

admin.site.register(Review, ReviewAdmin)
