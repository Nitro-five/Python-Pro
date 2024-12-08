from django.apps import AppConfig


class MyCustomAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_custom_app'

    def ready(self):
        import my_custom_app.signals
