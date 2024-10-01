"""
Метакласс SingletonMeta обеспечивает, что класс имеет только один экземпляр.
Если экземпляр уже существует, возвращается тот же объект.
"""


class SingletonMeta(type):
    _instances = {}

    """
    Переопределяет вызов класса. Если экземпляр класса уже создан,
    возвращает его; иначе создает новый экземпляр.

    Аргументы:
    cls : тип
        Класс, для которого создается экземпляр.
    *args : любые
        Позиционные аргументы, переданные конструктору.
    **kwargs : любые
        Именованные аргументы, переданные конструктору.
    """

    def __call__(cls, *args, **kwargs):
        # Если экземпляр класса еще не создан, создаем его
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


"""
Класс Singleton использует метакласс SingletonMeta для гарантии,
что будет создан только один экземпляр класса.
"""


class Singleton(metaclass=SingletonMeta):

    def __init__(self):
        print("Creating instance")


# Приклад використання
obj1 = Singleton()  # Виведе: Creating instance
obj2 = Singleton()  # Не виведе нічого, оскільки екземпляр вже існує

print(obj1 is obj2)  # Виведе: True
