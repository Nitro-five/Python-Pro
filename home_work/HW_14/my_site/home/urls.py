from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    re_path(r'^post/(?P<id>\d+)/$', views.post_view, name='post'),
    re_path(r'^profile/(?P<username>[a-zA-Z]+)/$', views.profile_view, name='profile'),
    re_path(r'^event/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.event_view, name='event'),
]

"""
URL конфигурация для приложения.

Содержит маршруты для различных представлений:
- home_view: домашняя страница.
- about_view: страница "О нас".
- contact_view: страница "Контакты".
- post_view: страница отдельного поста, идентифицированного по id.
- profile_view: страница профиля пользователя, идентифицированного по имени пользователя.
- event_view: страница события, идентифицированного по дате (год, месяц, день).
"""
