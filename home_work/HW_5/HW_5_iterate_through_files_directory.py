import os

"""
   Итератор для обхода всех файлов в заданном каталоге.

   Этот класс позволяет перебирать все файлы в указанном каталоге, 
   возвращая их названия и размеры в байтах.

   Параметры:
   directory : str
       Путь к каталогу, в котором нужно искать файлы.

   Методы:
   __iter__() :
       Возвращает сам объект итератора, что позволяет использовать его в циклах.

   __next__() :
       Возвращает название и размер следующего файла в каталоге.
       Если больше нет файлов для обработки, поднимает исключение StopIteration.

   Исключения:
   StopIteration :
       Поднимается, когда все файлы в каталоге были обработаны.
   """


class file_iterator:

    def __init__(self, directory):
        self.directory = directory
        self.files = os.listdir(directory)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.files):
            # Конец итерации если закончились файлы
            raise StopIteration

        file_name = self.files[self.index]
        file_path = os.path.join(self.directory, file_name)

        # Проверка на файл
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            self.index += 1
            return file_name, file_size

        self.index += 1
        # Рекурсия для следующего файла
        return self.__next__()


# Тест
if __name__ == "__main__":
    directory = "/Users/admin/Desktop/PycharmProjects/PythonPro/home_work/HW_5/collecting_statistics_images/images"

    file_iterator = file_iterator(directory)

    for file_name, file_size in file_iterator:
        print(f"Файл: {file_name}, Размер: {file_size} байт")
