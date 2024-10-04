import shutil
import os

"""
Менеджер контекста для создания резервной копии файла перед его обработкой.

Этот класс позволяет безопасно обрабатывать важные файлы. Он создает резервную копию
указанного файла перед его изменением и восстанавливает резервную копию в случае возникновения ошибки.

Параметры:
file_path : str
    Путь к файлу, который необходимо обработать.
new_content : str
    Новый вміст, который будет записан в файл.
"""


class backup_manager:
    """
    Инициализация экземпляра BackupManager.

    Параметры:
    file_path : str
        Путь к файлу, который нужно обрабатывать.
    new_content : str
        Новый контент, который будет записан в файл.
    """

    def __init__(self, file_path, new_content):

        self.file_path = file_path
        self.new_content = new_content
        self.backup_path = f"{file_path}.bak"

    """
    Создает резервную копию файла перед его обработкой.

    Возвращает:
    str
        Путь к оригинальному файлу.
    """

    def __enter__(self):

        shutil.copy2(self.file_path, self.backup_path)
        return self.file_path

    """
    Завершает обработку файла.

    Если обработка прошла успешно, оригинальный файл будет
    заменен новым содержимым. Если возникла ошибка, резервная копия
    будет восстановлена.

    Параметры:
    exc_type : type
        Тип исключения, если оно произошло (иначе None).
    exc_value : Exception
        Значение исключения, если оно произошло (иначе None).
    traceback : traceback
        Объект трассировки стека, если исключение произошло (иначе None).
    """

    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is None:
            with open(self.file_path, 'w') as file:
                file.write(self.new_content)
            os.remove(self.backup_path)
        else:
            shutil.copy2(self.backup_path, self.file_path)
            print(f"Ошибка: {exc_value}. Резервная копия обновлена.")


if __name__ == "__main__":
    new_file_content = (
        "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. "
        "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
        " Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. "
        "Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. "
        "Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. "
        "Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. "
        "Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet."
        " Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui."
        " Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum."
        " Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. "
        "Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. "
        "Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales,"
        " augue velit cursus nunc,")
    with backup_manager('important_file.txt', new_file_content) as file:
        pass
