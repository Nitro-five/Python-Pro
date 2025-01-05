# qr_code/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<str:short_url>/', views.generate_qr, name='generate_qr'),
]
