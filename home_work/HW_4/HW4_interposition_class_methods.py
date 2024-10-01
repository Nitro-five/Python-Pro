"""
Класс Proxy переадресовывает вызовы методов переданного объекта,
дополнительно логируя информацию о каждом вызове.

Атрибуты:
    _obj: Объект, для которого создается прокси.

Методы:
    __getattr__(name): Переадресует вызовы методов объекта и логирует их.
"""


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Инициализирует прокси с заданным объектом.
    def __getattr__(self, name):
        # Переадресация вызовов методов
        attr = getattr(self._obj, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                # Логирование вызова
                print(f"Calling method: {name} with args: {args}")
                return attr(*args, **kwargs)

            return wrapper
        return attr


# Приклад використання
class MyClass:
    def greet(self, name):
        return f"Hello, {name}!"


obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))
