import asyncio


async def producer(queue):
    """
    Функция-изготовитель, которая добавляет 5 заданий в очередь с задержкой.

    Параметры:
    queue (asyncio.Queue): Очередь, в которую будут добавлены задания.
    """
    for i in range(5):
        # Добавляем задание в очередь с задержкой в 1 секунду
        await asyncio.sleep(1)
        task = f"Задание {i + 1}"
        await queue.put(task)
        print(f"Добавлено: {task}")


async def consumer(queue):
    """
    Функция-потребитель, которая обрабатывает задания из очереди.

    Параметры:
    queue (asyncio.Queue): Очередь, из которой будут извлекаться задания.
    """
    while True:
        # Ждем задание из очереди
        task = await queue.get()
        # Проверка на сигнал завершения
        if task is None:
            break
        # Имитируем выполнение задания с задержкой в 2 секунды
        print(f"Обработка: {task}")
        await asyncio.sleep(2)
        queue.task_done()


async def main():
    """
    Основная функция, которая управляет процессом добавления и обработки заданий.
    Запускает функции producer и consumer, а также ожидает их завершения.
    """
    queue = asyncio.Queue()

    # Запускаем producer
    prod_task = asyncio.create_task(producer(queue))

    # Запускаем несколько consumer (например, 3) с помощью gather
    cons_tasks = [asyncio.create_task(consumer(queue)) for _ in range(3)]

    # Ждем завершения producer
    await prod_task

    # Завершаем потребителей, добавляя сигнал завершения в очередь
    for _ in cons_tasks:
        # Добавляем сигнал завершения для каждого потребителя
        await queue.put(None)

    # Ждем, пока все задания будут обработаны
    await queue.join()

    # Ждем завершения всех потребителей
    await asyncio.gather(*cons_tasks)


if __name__ == "__main__":
    # Запускаем основную функцию
    asyncio.run(main())
