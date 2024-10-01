"""
Декоратор, который логирует вызовы всех методов класса.

Параметры:
    cls: Класс, методы которого будут логироваться.

Возвращает:
    Новый класс, который оборачивает оригинальный и логирует вызовы его методов.
"""


def log_methods(cls):
    class Wrapped(cls):
        # Переопределяет доступ к атрибутам объекта.
        def __getattribute__(self, name):
            # Получает атрибут с помощью родительского метода.
            attr = super().__getattribute__(name)
            if callable(attr):
                def wrapper(*args, **kwargs):
                    # Логирование вызова метода
                    print(f"Logging: {name} called with {args} {kwargs}")
                    return attr(*args, **kwargs)

                return wrapper
            return attr

    return Wrapped


@log_methods
class MyClass:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


# Приклад використання
obj = MyClass()
print(obj.add(5, 3))  # Logging: add called with (5, 3)
print(obj.subtract(5, 3))  # Logging: subtract called with (5, 3)
