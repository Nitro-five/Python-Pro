from django.contrib import admin
from .models import UserProfile, Category, Ad, Comment
from django.utils import timezone
from datetime import timedelta


class OlderThan30DaysFilter(admin.SimpleListFilter):
    """
    Кастомный фильтр для отображения объявлений старше 30 дней.
    В админке будет два варианта: старше 30 дней или не старше 30 дней.
    """
    title = 'older than 30 days'
    # Параметр в URL, по которому фильтруется
    parameter_name = 'older_than_30_days'

    def lookups(self, request, model_admin):
        """
        Определение значений фильтра для выбора в админке.
        Фильтр для объявлений старше 30 дней
        Фильтр для объявлений не старше 30 дней
        """
        return (
            ('yes', 'older than 30 days'),
            ('no', 'No, not older than 30 days'),
        )

    def queryset(self, request, queryset):
        """
        Применение фильтра для queryset на основе выбранного значения в админке.
        """
        now = timezone.now()
        if self.value() == 'yes':
            # Возвращаем объявления, созданные более 30 дней назад
            return queryset.filter(created_at__lte=now - timedelta(days=30))
        if self.value() == 'no':
            # Возвращаем объявления, созданные менее 30 дней назад
            return queryset.filter(created_at__gt=now - timedelta(days=30))
        return queryset


class AdAdmin(admin.ModelAdmin):
    """
    Админская модель для отображения и управления объявлениями.
    Включает фильтрацию, поиск и сортировку.
    """
    # Поля для отображения в админке
    list_display = ['title', 'price', 'category', 'created_at', 'is_active']

    # Фильтры в админке
    list_filter = ['is_active', 'category', 'created_at', 'price', OlderThan30DaysFilter]

    # Поля, по которым можно будет искать
    search_fields = ['title']

    # Параметры для сортировки
    ordering = ['created_at', 'price']

# Регистрируем модели и соответствующие им интерфейсы в админке
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Ad, AdAdmin)
admin.site.register(Comment)
