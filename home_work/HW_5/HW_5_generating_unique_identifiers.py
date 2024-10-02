"""
Класс UniqueHashGenerator реализует итератор для генерации уникальных хеш-идентификаторов
на основе простого подсчета.

Атрибуты:
    count (int): Счетчик для создания уникальных хешей.

Методы:
    __iter__(self): Возвращает сам объект, реализующий итерацию.
    __next__(self): Возвращает новый уникальный хеш-идентификатор при каждом вызове.
"""


class UniqueHashGenerator:

    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Генерация уникального идентификатора на основе счетчика
        unique_id = f"unique_id_{self.count}"
        self.count += 1
        return unique_id


# Тест
hash_generator = UniqueHashGenerator()

for _ in range(500):
    print(next(hash_generator))
