from django.urls import path
from . import views

app_name = 'analytics'
"""
Маршруты для приложения 'analytics', отвечающие за отображение статистики.

Включает:
- Главная страница аналитики (analytics_home).
"""

urlpatterns = [
    path('', views.analytics_home, name='analytics_home'),
]
