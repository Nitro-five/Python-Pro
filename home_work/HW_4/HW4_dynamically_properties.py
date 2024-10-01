"""
Класс DynamicProperties позволяет динамически добавлять свойства объекту
через метод add_property() с использованием встроенной функции property().

Атрибуты:
_properties : dict
    Внутренний словарь для хранения динамических свойств и их значений.
"""


class DynamicProperties:
    """
    Инициализирует объект DynamicProperties, создавая пустой словарь _properties
    для хранения значений свойств.
    """

    def __init__(self):
        self._properties = {}

    # Динамически добавляет новое свойство в класс с заданным именем и значением по умолчанию.
    def add_property(self, name, default_value=None):
        # Возвращает значение свойства. Если свойство не задано, возвращает значение по умолчанию.
        def getter(instance):
            return instance._properties.get(name, default_value)

        # Устанавливает значение свойства в словарь _properties.
        def setter(instance, value):
            instance._properties[name] = value

        # Динамически добавляем свойство в класс с использованием функции property
        setattr(self.__class__, name, property(getter, setter))


# Пример использования
if __name__ == "__main__":
    obj = DynamicProperties()
    obj.add_property('name', 'default_name')  # Добавляем свойство 'name'
    print(obj.name)  # Вывод: default_name
    obj.name = "Python"  # Устанавливаем новое значение
    print(obj.name)  # Вывод: Python
