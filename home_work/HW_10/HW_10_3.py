import random
import multiprocessing
import time


def calc_sum(array_slice):
    """
    Вычисляет сумму элементов массива и измеряет время обработки.

    Аргументы:
    array_slice -- список чисел, для которого нужно вычислить сумму.

    Возвращает:
    Сумму элементов массива.
    """
    start_time = time.time()
    result = sum(array_slice)
    end_time = time.time()
    processing_time = end_time - start_time
    print(f"Время обработки сегмента: {processing_time:.4f} секунд")
    return result


def main():
    """
    Главная функция программы. Генерирует большой массив случайных чисел,
    разбивает его на сегменты и вычисляет сумму элементов параллельно
    с использованием нескольких процессов.
    """
    large_array = [random.randint(1, 100) for _ in range(10 ** 6)]

    num_processes = 4
    segment_size = len(large_array) // num_processes
    segments = [large_array[i:i + segment_size] for i in range(0, len(large_array), segment_size)]

    with multiprocessing.Pool(processes=num_processes) as pool:
        result = pool.map(calc_sum, segments)

    total_sum = sum(result)

    print(f'Общая сумма массива: {total_sum}')


if __name__ == '__main__':
    main()
