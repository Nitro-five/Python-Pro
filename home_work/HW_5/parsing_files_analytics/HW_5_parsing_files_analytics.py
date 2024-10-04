"""
Генератор, который читает лог-файл и возвращает строки с ошибками (коды статуса 4XX и 5XX).

Параметры:
----------
file_path : str
    Путь к лог-файлу.
"""


def error_log_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Разделяем строку на части и проверяем код статуса
            parts = line.split()
            if len(parts) > 0:
                # Код статуса предположительно перед размером ответа
                status_code = parts[-2]
                if (status_code.startswith('4') or status_code.startswith('5')) and len(status_code) == 3:
                    yield line.strip()


"""
Записывает ошибки из лог-файла в новый файл.

Параметры:
input_file_path : str
    Путь к входному лог-файлу.
output_file_path : str
    Путь к выходному файлу, куда будут записаны ошибки.
"""


def write_errors_to_file(input_file_path, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for error in error_log_generator(input_file_path):
            output_file.write(error + '\n')  # Записываем ошибку в файл


# Тест
if __name__ == "__main__":
    input_log_file = "/Users/admin/Desktop/PycharmProjects/PythonPro/home_work/HW_5/parsing_files_analytics/log_file.log"
    output_error_file = "/Users/admin/Desktop/PycharmProjects/PythonPro/home_work/HW_5/parsing_files_analytics/errors_file.txt"
    write_errors_to_file(input_log_file, output_error_file)
