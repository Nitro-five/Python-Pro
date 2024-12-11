from django.apps import AppConfig

class MyAppConfig(AppConfig):
    """
    Класс конфигурации для приложения 'my_app'.

    Этот класс определяет настройки по умолчанию для приложения и регистрирует
    его в реестре приложений Django. Включает:
    - Тип первичного ключа по умолчанию для моделей.
    - Имя приложения, как оно определено в структуре проекта.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_app'