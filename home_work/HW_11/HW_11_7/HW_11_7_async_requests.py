import aiohttp
import asyncio
import time

async def fetch(session, url, index):
    async with session.get(url) as response:
        print(f"Запрос {index + 1}: {response.status}", flush=True)
        return response.status

async def async_requests(url, count):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, i) for i in range(count)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    url = "https://docs.python.org/3/library/asyncio-task.html"
    count = 500

    try:
        start_time = time.time()
        print("Начало выполнения...", flush=True)
        asyncio.run(async_requests(url, count))
        end_time = time.time()
        print("Все запросы выполнены.", flush=True)
        print(f"Асинхронный подход: {end_time - start_time:.2f} секунд", flush=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}", flush=True)
