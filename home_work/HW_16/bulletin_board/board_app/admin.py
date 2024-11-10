from django.contrib import admin
from .models import UserProfile, Category, Ad, Comment
from datetime import timedelta
from django.utils import timezone


class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'created_at', 'is_active']
    list_filter = ['is_active', 'category', 'created_at']  # Фильтры по полям

    # Добавим фильтр по дате (например, фильтр для объявлений старше 30 дней)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        now = timezone.now()

        # Фильтруем по состоянию объявления и возрасту объявления (старше 30 дней)
        if 'older_than_30_days' in request.GET:
            queryset = queryset.filter(created_at__lte=now - timedelta(days=30))

        return queryset

    # Добавление фильтра по старости объявления в интерфейсе
    def get_search_results(self, request, queryset, search_term):
        if search_term == 'older_than_30_days':
            now = timezone.now()
            queryset = queryset.filter(created_at__lte=now - timedelta(days=30))
        return queryset, False


# Регистрируем модель и админский интерфейс
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Ad, AdAdmin)
admin.site.register(Comment)
