import json

"""
Контекстный менеджер для работы с файлами конфигураций в формате JSON.

Параметры:
file_path : str
    Путь к файлу конфигураций в формате JSON.

Пример использования:
with ConfigManager('config.json') as config:
    config['new_key'] = 'new_value'
    config['existing_key'] = 'updated_value'
"""


class ConfigManager:
    """
    Инициализация экземпляра ConfigManager.

    Параметры:
        file_path : str
        Путь к файлу конфигураций.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.config = {}

    """
    Вход в контекст менеджера.

    Загружает конфигурацию из указанного файла.

    Возвращает:
    dict
    Словарь, содержащий конфигурацию из файла.
    """

    def __enter__(self):
        with open(self.file_path, 'r') as file:
            self.config = json.load(file)
        return self.config

    """
    Выход из контекст менеджера.

    Сохраняет изменения в конфигурации обратно в файл.

    Параметры:
        exc_type : type
        Тип исключения, если оно произошло (иначе None).
    exc_value : Exception
        Значение исключения, если оно произошло (иначе None).
    traceback : traceback
        Объект трассировки стека, если исключение произошло (иначе None).
    """

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.file_path, 'w') as file:
            json.dump(self.config, file, indent=4)


# Использование контекстного менеджера
if __name__ == "__main__":
    config_file_path = 'config.json'

    with ConfigManager(config_file_path) as config:
        # Внесение изменений в конфигурацию
        config['Port'] = 'port'
        config['2213'] = '1111'
