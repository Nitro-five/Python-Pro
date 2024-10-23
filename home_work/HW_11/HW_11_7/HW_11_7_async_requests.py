import aiohttp
import asyncio
import time

async def fetch(session, url, index):
    """
    Выполняет асинхронный HTTP-запрос к указанному URL и выводит статус-код ответа.

    Параметры:
    session (aiohttp.ClientSession): Сессия для выполнения запросов.
    url (str): URL-адрес, к которому будет отправлен запрос.
    index (int): Индекс запроса, используемый для вывода информации.

    Возвращает:
    int: Статус-код ответа от сервера.
    """
    async with session.get(url) as response: 
        print(f"Запрос {index + 1}: {response.status}")
        return response.status

async def async_requests(url, count):
    """
    Выполняет заданное количество асинхронных HTTP-запросов к указанному URL.

    Параметры:
    url (str): URL-адрес, к которому будут отправлены запросы.
    count (int): Количество запросов для выполнения.
    """
    # Создаем сессию для выполнения запросов
    async with aiohttp.ClientSession() as session:
        # Создаем задачи для каждого запроса
        tasks = [fetch(session, url, i) for i in range(count)]
        # Ждем завершения всех задач
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    url = "https://httpbin.org/get"
    count = 500

    start_time = time.time()
    asyncio.run(async_requests(url, count))
    end_time = time.time()

    print(f"Асинхронный подход: {end_time - start_time:.2f} секунд")
