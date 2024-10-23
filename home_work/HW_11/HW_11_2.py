import aiohttp
import asyncio


async def fetch_content(url: str) -> str:
    """
    Выполняет HTTP-запрос к указанному URL и возвращает содержимое страницы.

    Параметры:
    url (str): URL страницы для запроса.

    Возвращает:
    str: Содержимое страницы или сообщение об ошибке.
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                # Вызывает ошибку, если статус-код не успешный
                response.raise_for_status()
                # Возвращает содержимое страницы
                return await response.text()
    except aiohttp.ClientError as e:
        return f"Ошибка при подключении к {url}: {str(e)}"


async def fetch_all(urls: list) -> list:
    """
    Загружает содержимое всех страниц из переданного списка URL параллельно.

    Параметры:
    urls (list): Список URL-адресов для загрузки.

    Возвращает:
    list: Список содержимого страниц или сообщений об ошибках.
    """
    tasks = [fetch_content(url) for url in urls]
    # Запускаем все задачи параллельно
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = [
        "https://docs.python.org/3/library/asyncio.html",
        "https://www.deepl.com/en/translator",
        "https://www.serpa.com.ua",
    ]
    contents = asyncio.run(fetch_all(urls))

    for url, content in zip(urls, contents):
        print(f"\nСодержимое для {url}:\n{content}")
