import asyncio


async def slow_task():
    """Имитирует выполнение длительной задачи,
    задерживая выполнение на 10 секунд.
    """
    await asyncio.sleep(10)


async def main():
    """Основная асинхронная функция, которая пытается
    выполнить slow_task() с таймаутом 5 секунд.
    Если задача не успевает завершиться, выводит сообщение об ошибке.
    """
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        print("Час выполнения заведения превышен.")

    # Запуск основной асинхронной функции


if __name__ == "__main__":
    asyncio.run(main())
