import concurrent.futures
import time


def sear_txt_file(filename, search_txt):
    """
    Ищет заданный текст в указанном файле.

    Аргументы:
        filename (str): Путь к файлу, в котором производится поиск.
        search_txt (str): Текст для поиска в файле.

    Возвращает:
        str: Сообщение о результате поиска, включая информацию о времени выполнения.
    """
    start_time = time.time()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if search_txt in line:
                    elapsed_time = time.time() - start_time
                    return f'Обнаружен в {filename}: {line.strip()} (время: {elapsed_time:.5f} сек)'
    except Exception as e:
        elapsed_time = time.time() - start_time
        return f'Ошибка при работе с текстом {filename}: {str(e)} (время: {elapsed_time:.5f} сек)'
    elapsed_time = time.time() - start_time
    return f'Текст отсутствует в {filename} (время: {elapsed_time:.5f} сек)'


def main():
    """
    Главная функция для выполнения программы.

    Запрашивает текст для поиска и создает потоки для поиска
    текста в нескольких файлах одновременно.
    """
    search_txt = input('Укажите текст: ')
    file_paths = [
        '/Users/admin/Desktop/PycharmProjects/PythonPro/home_work/HW_10/HW_10_5/file1.txt',
        '/Users/admin/Desktop/PycharmProjects/PythonPro/home_work/HW_10/HW_10_5/file2.txt',
        '/Users/admin/Desktop/PycharmProjects/PythonPro/home_work/HW_10/HW_10_5/file3.txt'
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(sear_txt_file, file, search_txt): file for file in file_paths}

    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(result)


if __name__ == '__main__':
    main()
