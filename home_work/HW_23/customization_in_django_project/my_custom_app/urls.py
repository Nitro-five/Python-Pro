from django.urls import path, include
from . import views
from .views import MyModelViewSet
from rest_framework.routers import DefaultRouter

# Инициализация маршрутизатора для API
router = DefaultRouter()
router.register(r'mymodel', MyModelViewSet)

urlpatterns = [
    path('', views.home_view, name='home'),
    path('mymodel/', views.mymodel_list, name='mymodel_list'),
    path('api/', include(router.urls)),  # Подключение API маршрутов
    path('metrics/', views.RequestMetricView.as_view(), name='request-metrics'),
    path('register/', views.register, name='register'),
]
