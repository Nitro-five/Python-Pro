import zipfile
import os

"""
Менеджер контекста для архивации файлов.
Этот класс позволяет автоматически создавать ZIP-архив и добавлять файлы
во время обработки в блоке with.
Параметры:
archive_name : str
    Имя архива (с расширением .zip), который будет создан.

"""


class zip_manager:
    """
    Инициализация экземпляра zip_manager.

    Параметры:
    archive_name : str
        Имя архива, который нужно создать.
    """

    def __init__(self, archive_name):
        self.archive_name = archive_name
        self.zip_file = None

    """
    Создает архив и открывает его для записи.

    Возвращает:
    zipfile.ZipFile
        Объект ZIP-архива, в который можно добавлять файлы.
    """

    def __enter__(self):
        self.zip_file = zipfile.ZipFile(self.archive_name, 'w', zipfile.ZIP_DEFLATED)
        return self.zip_file

        """
        Закрывает архив после завершения работы.

        Параметры:
        ----------
        exc_type : type
            Тип исключения, если оно произошло (иначе None).
        exc_value : Exception
            Значение исключения, если оно произошло (иначе None).
        traceback : traceback
            Объект трассировки стека, если исключение произошло (иначе None).
        """

    def __exit__(self, exc_type, exc_value, traceback):
        if self.zip_file:
            self.zip_file.close()
            print(f"Архив '{self.archive_name}' успешно создан.")


# Тест
if __name__ == "__main__":
    archive_name = 'my_archive.zip'

    with zip_manager(archive_name) as zip_manager:
        zip_manager.write('file1.txt', arcname='file1.txt')
        zip_manager.write('file2.txt', arcname='file2.txt')
