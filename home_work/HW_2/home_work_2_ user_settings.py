# Завдання 8: Зберігання налаштувань користувача
def create_user_settings():
    settings = {
        'theme': 'light',
        'language': 'en',
        'notifications': True
    }

    def get_setting(key):
        return settings.get(key, "Поробуй ещё раз")

    def set_setting(key, value):
        if key in settings:
            settings[key] = value
            return f"Настройки '{key}' изменены на '{value}'"
        else:
            return "что то пошло не так "

    def view():
        return settings

    return get_setting, set_setting, view


get_setting, set_setting, view_settings = create_user_settings()

print(view_settings())

print(set_setting('theme', 'dark'))
print(set_setting('language', 'uk'))
print(set_setting('notifications', False))
print(view_settings())
print(get_setting('unknown'))
