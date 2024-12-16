from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
"""
URL-конфигурация для приложения задач.

Используется DefaultRouter для автоматической генерации маршрутов для всех 
стандартных действий в `TaskViewSet` (создание, чтение, обновление, удаление).

Маршруты:
    - /tasks/ : для работы с задачами.
"""
