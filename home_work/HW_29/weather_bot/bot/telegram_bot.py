import os
import time
import logging
import requests
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    CallbackContext,
    filters,
)
# Django settings
from django.conf import settings

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='app.log',  # Файл для логов
    filemode='a'  # Режим добавления (a - append)
)

# Состояния разговора
ASK_CITY = 1


async def start(update: Update, context: CallbackContext):
    """
    Обрабатывает команду /start.

    При вызове команды /start бот отправляет приветственное сообщение.

    Аргументы:
        update (Update): Объект обновления, содержащий информацию о сообщении.
        context (CallbackContext): Контекст обработки команды.
    """
    logging.info("Команда /start была вызвана.")
    await update.message.reply_text(
        "Привет! Я ваш бот для погоды. Используйте команду /help, чтобы узнать доступные функции.")


async def help_command(update: Update, context: CallbackContext):
    """
    Обрабатывает команду /help.

    При вызове команды /help бот отправляет список доступных команд.

    Аргументы:
        update (Update): Объект обновления, содержащий информацию о сообщении.
        context (CallbackContext): Контекст обработки команды.
    """
    logging.info("Команда /help была вызвана.")
    await update.message.reply_text(
        "Доступные команды:\n/start - начать работу\n/help - справка\n/weather - узнать погоду.")


async def weather(update: Update, context: CallbackContext):
    """
    Обрабатывает команду /weather.

    При вызове команды /weather бот запрашивает у пользователя название города
    для получения информации о погоде.

    Аргументы:
        update (Update): Объект обновления, содержащий информацию о сообщении.
        context (CallbackContext): Контекст обработки команды.
    """
    logging.info("Команда /weather была вызвана.")
    await update.message.reply_text("Введите название города:")
    return ASK_CITY


async def ask_city(update: Update, context: CallbackContext):
    """
    Обрабатывает введенное пользователем название города и возвращает информацию
    о погоде в этом городе.

    Запрашивает информацию с API погоды и отправляет результат пользователю.

    Аргументы:
        update (Update): Объект обновления, содержащий информацию о сообщении.
        context (CallbackContext): Контекст обработки команды.

    Возвращает:
        ConversationHandler.END: Завершает текущий разговор.
    """
    city = update.message.text
    api_key = settings.API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    start_time = time.time()

    try:
        response = requests.get(url)
        data = response.json()
        duration = time.time() - start_time

        if data.get("cod") != 200:
            error_message = data.get('message', 'неизвестная ошибка')
            logging.warning(
                f"Неуспешный запрос для города {city}. Ошибка: {error_message}. Время выполнения: {duration:.2f} сек.")
            await update.message.reply_text(f"Ошибка: {error_message}.")
        else:
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            logging.info(
                f"Успешный запрос для города {city}. Погода: {temp}°C, {weather}. Время выполнения: {duration:.2f} сек.")
            await update.message.reply_text(f"Погода в {city}: {temp}°C, {weather}.")
    except Exception as e:
        duration = time.time() - start_time
        logging.error(f"Ошибка при обработке запроса для города {city}: {e}. Время выполнения: {duration:.2f} сек.")
        await update.message.reply_text(f"Произошла ошибка: {e}")

    return ConversationHandler.END


async def cancel(update: Update, context: CallbackContext):
    """
    Обрабатывает команду /cancel для отмены текущего действия.

    При вызове команды /cancel бот отменяет текущий запрос и завершает разговор.

    Аргументы:
        update (Update): Объект обновления, содержащий информацию о сообщении.
        context (CallbackContext): Контекст обработки команды.

    Возвращает:
        ConversationHandler.END: Завершает текущий разговор.
    """
    await update.message.reply_text("Отменено.")
    return ConversationHandler.END


def run_bot():
    """
    Запускает бота и настраивает обработку команд.

    Создает объект Application и добавляет обработчики команд /start, /help, /weather.
    Настроен обработчик для обработки ввода города пользователем и получения прогноза погоды.

    Логирует действия и ошибки, связанные с запросами к API погоды.

    Примечание:
        Запуск бота происходит с использованием токена, который должен быть
        храниться в настройках Django (settings.TELEGRAM_BOT_TOKEN).
    """
    token = settings.TELEGRAM_BOT_TOKEN
    application = Application.builder().token(token).build()

    # Разговорный обработчик для команды /weather
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("weather", weather)],
        states={
            ASK_CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_city)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Другие команды
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Запуск
    logging.info("Бот запущен. Ожидаем команды...")
    application.run_polling()
