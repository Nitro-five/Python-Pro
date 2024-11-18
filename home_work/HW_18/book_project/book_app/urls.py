from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Настройка документации Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Library API",
        default_version='v1',
        description="API for managing books",
        contact=openapi.Contact(email="info@library.com"),
    ),
    public=True,
)

# Роутер для BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # Добавляем маршрут для Swagger документации
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),

    # Добавляем маршруты для API
    path('api/', include(router.urls)),
]
