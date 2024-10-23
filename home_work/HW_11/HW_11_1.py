import asyncio
import random

async def download_page(url: str):
    """
    Симулирует загрузку страницы по заданному URL.

    Параметры:
    url (str): URL страницы для загрузки.

    Ожидает случайный промежуток времени от 1 до 5 секунд
    и выводит сообщение о завершении загрузки.
    """
    sleep_time = random.randint(1, 5)
    await asyncio.sleep(sleep_time)
    print(f'Загружен {url} за {sleep_time} сек.')


async def main(urls):
    """
    Основная асинхронная функция, которая инициирует загрузку страниц.

    Создает список URL-адресов и запускает асинхронные задачи
    для их загрузки параллельно. Ждет завершения всех задач.
    """

    list_search_url = [download_page(url) for url in urls]
    await asyncio.gather(*list_search_url)

if __name__ == "__main__":
    urls = [
        "https://google.com",
        "https://yahoo.org",
        "https://serpa.net",
    ]
    asyncio.run(main(urls))
