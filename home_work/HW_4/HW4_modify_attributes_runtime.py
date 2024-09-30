"""
   Класс MutableClass позволяет динамически добавлять и удалять атрибуты
   объектов этого класса.

   Методы:
       add_attribute(name, value): Добавляет атрибут с заданным именем и значением.
       remove_attribute(name): Удаляет атрибут с заданным именем, если он существует.
   """
class MutableClass:
    def add_attribute(self, name, value):
        setattr(self, name, value)

    def remove_attribute(self, name):
        if hasattr(self, name):
            delattr(self, name)
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

# Пример использования
obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python

obj.remove_attribute("name")
# print(obj.name)  # Виникне помилка, атрибут видалений

