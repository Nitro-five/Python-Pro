"""
URL configuration for HW_17_forms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Основные URL-адреса проекта
urlpatterns = [
    # Маршрут для панели администратора Django
    path('admin/', admin.site.urls),

    # Маршрут для пользовательских URL-адресов (используется include для подключения urls.py приложения 'forms_app')
    path('user/', include('forms_app.urls')),
]

# Включение поддержки медиафайлов только в режиме отладки (DEBUG)
if settings.DEBUG:
    # Подключаем статичные медиафайлы, такие как изображения, через MEDIA_URL и MEDIA_ROOT
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
