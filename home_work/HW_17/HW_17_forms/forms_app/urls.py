from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  # Маршрут для регистрации нового пользователя
                  path('register/', views.register_view, name='register'),

                  # Маршрут для редактирования профиля пользователя
                  path('edit_profile/', views.edit_profile_view, name='edit_profile'),

                  # Маршрут для изменения пароля пользователя
                  path('change_password/', views.change_password_view, name='change_password'),

                  # Маршрут для отображения профиля пользователя
                  path('profile/', views.profile_view, name='profile'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
