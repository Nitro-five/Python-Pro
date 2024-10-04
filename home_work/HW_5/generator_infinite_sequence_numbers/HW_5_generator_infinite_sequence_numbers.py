"""
Генератор бесконечной последовательности четных чисел.

Генерирует четные числа, начиная с 0 и продолжая в бесконечность,
поочередно возвращая их одно за другим.

Возвращает:
int
    Следующее четное число в последовательности.
"""


def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

    """
    Менеджер контекста, который генерирует четные числа до заданного лимита
    и записывает их в файл.

    Параметры:
    ----------
    limit : int
        Максимальное количество четных чисел для генерации.
    file_path : str
        Путь к файлу для сохранения четных чисел.

    Методы:
    __enter__() :
        Открывает файл для записи и генерирует четные числа до заданного лимита.

    __exit__(exc_type, exc_val, exc_tb) :
        Закрывает файл при выходе из контекста.
    """


class limited_even_numbers:

    # Инициализирует менеджер контекста.
    def __init__(self, limit, file_path):

        self.limit = limit
        self.file_path = file_path
        self.file = None

    """
    Входит в контекст менеджера.

    Открывает файл для записи и генерирует четные числа.

    Возвращает:
    limited_even_numbers
    Экземпляр менеджера контекста.
    """

    def __enter__(self):

        self.file = open(self.file_path, 'w', encoding='utf-8')
        for count, number in enumerate(even_numbers()):
            if count >= self.limit:
                break
            self.file.write(f"{number}\n")
        return self

    # Выходит из контекста менеджера.
    def __exit__(self, exc_type, exc_val, exc_tb):

        if self.file:
            self.file.close()


# Тест
if __name__ == "__main__":
    limit = 100
    # Путь к файлу
    file_path = '/Users/admin/Desktop/PycharmProjects/PythonPro/home_work/HW_5/generator_infinite_sequence_numbers/even_numbers.txt'

    with limited_even_numbers(limit, file_path) as manager:
        print(f"Создано {manager.limit} парних чисел в '{manager.file_path}'.")
