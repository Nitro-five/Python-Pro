import math
import multiprocessing
import sys


def partial_factorial(start, end):
    """
    Вычисляет частичный факториал в диапазоне от start до end.

    :param start: Начальное число (включительно).
    :param end: Конечное число (включительно).
    :return: Частичный факториал от start до end.
    """
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def calculate_factorial(n, num_processes):
    """
    Вычисляет факториал числа n, распределяя вычисления между процессами.

    :param n: Число, для которого нужно вычислить факториал.
    :param num_processes: Количество процессов для параллельного вычисления.
    :return: Полный факториал числа n.
    """
    # Делим вычисления на части для каждого процесса
    chunk_size = math.ceil(n / num_processes)
    ranges = [(i, min(i + chunk_size - 1, n)) for i in range(1, n + 1, chunk_size)]

    # Создаем пул процессов и запускаем вычисления
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(partial_factorial, ranges)

    # Вычисляем общий факториал путем умножения частичных результатов
    factorial_result = 1
    for result in results:
        factorial_result *= result

    return factorial_result


if __name__ == "__main__":
    # Устанавливаем метод запуска процессов
    multiprocessing.set_start_method('fork')  # Для macOS и Linux
    # Убираем ограничение на число цифр для больших чисел
    sys.set_int_max_str_digits(0)

    # Задаем число, для которого нужно вычислить факториал
    n = 1000000
    # Получаем количество доступных процессоров
    num_processes = multiprocessing.cpu_count()

    print(f"Вычисляем факториал {n} с помощью {num_processes} процессов...")
    result = calculate_factorial(n, num_processes)
    print(f"Факториал {n} вычислен. Длина числа: {len(str(result))} цифр.")
