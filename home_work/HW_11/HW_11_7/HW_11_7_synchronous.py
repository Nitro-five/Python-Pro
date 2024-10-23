import requests
import time

def synchronous_requests(url, count):
    """
    Выполняет заданное количество HTTP-запросов к указанному URL.

    Параметры:
    url (str): URL-адрес, к которому будут отправлены запросы.
    count (int): Количество запросов для выполнения.

    Возвращает:
    list: Список статус-кодов ответов от сервера.
    """
    results = []
    for _ in range(count):
        response = requests.get(url)
        print(f"Запрос {_ + 1}: {response.status_code}")
        results.append(response.status_code)
    return results

if __name__ == "__main__":
    url = "https://docs.python.org/3/library/asyncio-task.html"
    count = 500

    start_time = time.time()  # Запоминаем время начала выполнения
    synchronous_requests(url, count)  # Выполняем запросы
    end_time = time.time()  # Запоминаем время окончания выполнения

    print(f"Синхронный подход: {end_time - start_time:.2f} секунд")  # Выводим время выполнения
