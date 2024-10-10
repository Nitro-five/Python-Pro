import os
import pytest


class FileProcessor:
    """
    Класс для работы с файлами, который позволяет записывать данные в файл
    и читать их из файла.

    Методы:
    - write_to_file(file_path: str, data: str): записывает данные в файл.
    - read_from_file(file_path: str) -> str: читает данные из файла.
    """

    @staticmethod
    def write_to_file(file_path: str, data: str):
        """
        Записывает данные в файл.

        :param file_path: Путь к файлу, в который будут записаны данные.
        """
        with open(file_path, 'w') as file:
            file.write(data)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """
        Читает данные из файла.

        :param file_path: Путь к файлу, из которого нужно прочитать данные.
        :return: Данные, прочитанные из файла.
        :raises FileNotFoundError: Если файл не найден.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Файл '{file_path}' не существует.")
        with open(file_path, 'r') as file:
            return file.read()


def test_file_write_read(tmpdir):
    """
    Тестирует запись и чтение данных из файла.
    Проверяет, что записанные данные соответствуют прочитанным.
    """
    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(file)
    assert content == "Hello, World!"


def test_file_write_empty_string(tmpdir):
    """
    Тестирует запись и чтение пустой строки.
    Проверяет, что прочитанный содержимое является пустым.
    """
    file = tmpdir.join("emptyfile.txt")
    FileProcessor.write_to_file(file, "")
    content = FileProcessor.read_from_file(file)
    assert content == ""


def test_file_write_large_data(tmpdir):
    """
    Тестирует запись и чтение большого объема данных.
    Проверяет, что записанные данные соответствуют прочитанным.
    """
    file = tmpdir.join("largefile.txt")
    large_data = "A" * 10 ** 6  # 1 МБ данных
    FileProcessor.write_to_file(file, large_data)
    content = FileProcessor.read_from_file(file)
    assert content == large_data


def test_read_non_existent_file():
    """
    Тестирует поведение при попытке чтения из несуществующего файла.
    Проверяет, что возникает исключение FileNotFoundError.
    """
    with pytest.raises(FileNotFoundError):
        FileProcessor.read_from_file("non_existent_file.txt")
