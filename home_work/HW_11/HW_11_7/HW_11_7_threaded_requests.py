import requests
import time
from concurrent.futures import ThreadPoolExecutor

def fetch(url, index):
    """
    Выполняет HTTP-запрос к указанному URL и выводит статус-код ответа.

    Параметры:
    url (str): URL-адрес, к которому будет отправлен запрос.
    index (int): Индекс запроса, используемый для вывода информации.

    Возвращает:
    int: Статус-код ответа от сервера.
    """
    response = requests.get(url)
    print(f"Запрос {index + 1}: {response.status_code}")
    return response.status_code

def threaded_requests(url, count):
    """
    Выполняет заданное количество HTTP-запросов к указанному URL с использованием потоков.

    Параметры:
    url (str): URL-адрес, к которому будут отправлены запросы.
    count (int): Количество запросов для выполнения.
    """
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Запускаем запросы в потоках
        executor.map(lambda i: fetch(url, i), range(count))

if __name__ == "__main__":
    url = "https://docs.python.org/3/library/asyncio-task.html"
    count = 500

    start_time = time.time()
    threaded_requests(url, count)
    end_time = time.time()

    print(f"Многопоточный подход: {end_time - start_time:.2f} секунд")
