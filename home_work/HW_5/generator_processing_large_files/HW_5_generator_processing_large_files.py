"""
Генератор, который читает строки из текстового файла и возвращает только те строки,
которые содержат заданное ключевое слово.

Параметры:
file_path : str
    Путь к текстовому файлу для чтения.
keyword : str
    Ключевое слово для фильтрации строк.

Возвращает:
str
    Строки из файла, которые содержат ключевое слово (без пробелов в начале и в конце).
"""


def filter_lines(file_path, keyword):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword in line:
                yield line.strip()


"""
Читает строки из входного файла, фильтрует их по заданному ключевому слову 
и записывает отфильтрованные строки в новый файл.

Параметры:

input_file : str
    Путь к входному файлу для чтения.
output_file : str
    Путь к выходному файлу для записи отфильтрованных строк.
keyword : str
    Ключевое слово для фильтрации строк.
"""


def write_filtered_lines(input_file, output_file, keyword):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for line in filter_lines(input_file, keyword):
            out_file.write(line + '\n')


# Тест
if __name__ == "__main__":
    input_file = '/Users/admin/Desktop/PycharmProjects/PythonPro/home_work/HW_5/reverse_iterator/Golf R.txt'
    output_file = '/Users/admin/Desktop/PycharmProjects/PythonPro/home_work/HW_5/generator_processing_large_files/filtered_log.txt'
    keyword = 'Golf'

    write_filtered_lines(input_file, output_file, keyword)
