import random
import multiprocessing
import time
import math


def calc_sum(array_slice):
    start_time = time.time()
    result = sum(array_slice)
    end_time = time.time()
    processing_time = end_time - start_time
    print(f"Время обработки сегмента: {processing_time:.4f} секунд")
    return result


def main():
    large_array = [random.randint(1, 100) for _ in range(10 ** 6)]

    num_processes = 4
    segment_size = math.ceil(len(large_array) / num_processes)
    segments = [large_array[i:i + segment_size] for i in range(0, len(large_array), segment_size)]

    start_time = time.time()
    with multiprocessing.Pool(processes=num_processes) as pool:
        result = pool.map(calc_sum, segments)
    end_time = time.time()

    total_sum = sum(result)

    print(f'Общая сумма массива: {total_sum}')
    print(f'Общее время выполнения: {end_time - start_time:.4f} секунд')


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    main()
