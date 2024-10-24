from aiohttp import web
import asyncio


async def hello(request):
    """Обработчик для маршрута /, возвращает текст 'Main page'.

    Возвращает:
        web.Response: Ответ с текстом 'Main page'.
    """
    return web.Response(text="Main page")


async def slow(request):
    """Обработчик для маршрута /slow, имитирует задержку в 5 секунд
    перед возвращением ответа.

    Возвращает:
        web.Response: Ответ с текстом 'Slow page'.
    """
    await asyncio.sleep(5)  # Имитируем долгую операцию
    return web.Response(text="Slow page")


app = web.Application()
# Добавляем маршрут для главной страницы
app.router.add_get('/', hello)
# Добавляем маршрут для медленной страницы
app.router.add_get('/slow', slow)

if __name__ == '__main__':
    # Запуск сервера
    web.run_app(app, port=8080)