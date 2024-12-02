from django.conf import settings
from django.contrib import admin
from django.urls import path, include

"""
Список URL-путей для основного приложения.

Включает стандартный путь для административной панели Django и подключение URL-путей 
приложения 'user_book_app'. Также добавляется панель отладки, если режим DEBUG включен.

Атрибуты:
    urlpatterns (list): Список маршрутов для обработки запросов.
"""
urlpatterns = [
    path('admin/', admin.site.urls),  # Административная панель Django
    path('', include('user_book_app.urls')),  # Основные маршруты приложения 'user_book_app'
]

# Добавление панели отладки, если включен режим DEBUG
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
