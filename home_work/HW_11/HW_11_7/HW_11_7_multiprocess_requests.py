import requests
import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

def fetch(url, index):
    """
    Выполняет HTTP-запрос к указанному URL и возвращает статус-код ответа.

    Параметры:
    url (str): URL-адрес, к которому будет отправлен запрос.
    index (int): Индекс запроса, используемый для внутренней обработки (не используется в данной функции).

    Возвращает:
    int: Статус-код ответа от сервера.
    """
    response = requests.get(url)
    return response.status_code

def multiprocess_requests(url, count):
    """
    Выполняет заданное количество HTTP-запросов к указанному URL с использованием процессов.

    Параметры:
    url (str): URL-адрес, к которому будут отправлены запросы.
    count (int): Количество запросов для выполнения.
    """
    with ProcessPoolExecutor(max_workers=10) as executor:
        # Запускаем запросы в нескольких процессах
        executor.map(lambda i: fetch(url, i), range(count))

if __name__ == "__main__":
    multiprocessing.set_start_method('fork')
    url = "https://docs.python.org/3/library/asyncio-task.html"
    count = 500

    start_time = time.time()
    multiprocess_requests(url, count)
    end_time = time.time()

    print(f"Многопроцессорный подход: {end_time - start_time:.2f} секунд")
