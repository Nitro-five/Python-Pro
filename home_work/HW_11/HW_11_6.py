import aiohttp
import asyncio


async def download_image(url, filename):
    """Загружает изображение по указанному URL и сохраняет его в файл.

    Параметры:
        url (str): URL изображения для загрузки.
        filename (str): Имя файла, в который будет сохранено изображение.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(filename, 'wb') as f:
                    f.write(await response.read())
                print(f"Картинка {filename} загрузилась успешно.")
            else:
                print(f"Не вышло загрузить {url}: статус {response.status}")


async def main():
    """Основная асинхронная функция, создающая задачи для загрузки изображений.

    Загружает изображения по заранее определенным URL-адресам и обрабатывает их параллельно.
    """
    urls = [
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHRlV4HfrwX_MyYs0duw4QT-6hAsfAxT6ndQ&s',
        'https://64.media.tumblr.com/6d8e49a21ba6294e689ad40b89388649/b7d30ba8878444e3-c0/s1280x1920/ec9a6f41d212c44deb2d0ef9cbdd907a78e2b463.jpg',
        'https://i.pinimg.com/236x/b2/cc/76/b2cc76b12ab9708b2df6b65bedbd8997.jpg',
    ]
    tasks = []

    for i, url in enumerate(urls):
        # Генерация имя файла для сохранения изображения
        filename = f'image_{i + 1}.jpg'
        # Добавляем задачу загрузки изображения
        tasks.append(download_image(url, filename))
        # Запускаем все задачи параллельно
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    """Запускает основную асинхронную функцию для загрузки изображений."""
    asyncio.run(main())
