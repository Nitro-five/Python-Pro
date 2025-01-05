from django.contrib import admin
from django.urls import path, include
from links import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('my-links/', views.user_links, name='user_links'),
    path('qr/', include('qr_code.urls')),
    path('analytics/', include('analytics.urls')),
    path('<str:short_url>/', views.redirect_to_original, name='redirect'),
]
