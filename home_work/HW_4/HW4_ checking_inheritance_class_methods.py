import inspect

"""
Анализирует наследование класса и выводит все методы,
которые он наследует от базовых классов.

Параметры:
    cls (type): Класс для анализа.
"""


def analyze_inheritance(cls):
    # Получаем все базовые классы
    base_classes = cls.__bases__

    inherited_methods = set()

    # Перебираем базовые классы
    for base in base_classes:
        # Получаем все методы базового класса
        methods = [name for name, _ in inspect.getmembers(base, predicate=inspect.isfunction)]
        inherited_methods.update(methods)

    # Вывод
    print(f"Методы, унаследованные классом {cls.__name__} от базовых классов:")
    if inherited_methods:
        for method in inherited_methods:
            print(f"- {method}")
    else:
        print("<нет унаследованных методов>")


# Пример использования
class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass


analyze_inheritance(Child)
