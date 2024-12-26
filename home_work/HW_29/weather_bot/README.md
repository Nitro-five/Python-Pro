# Telegram Weather Bot

## Описание
Этот проект представляет собой Telegram-бота, который предоставляет информацию о погоде в указанном городе. Бот использует API OpenWeather для получения данных о погоде и взаимодействует с пользователем через Telegram.

## Как запустить проект?

### Шаг 1: Установите зависимости
Убедитесь, что Python версии 3.8 или выше установлен на вашем компьютере. Затем выполните следующие команды для создания виртуального окружения и установки зависимостей:

```bash
python -m venv venv
source venv/bin/activate  # Для macOS и Linux
venv\Scripts\activate   # Для Windows
pip install -r requirements.txt
```

### Шаг 2: Настройте переменные окружения
Создайте файл `.env` в корневой директории проекта и добавьте в него следующие строки:

```
API_KEY=<ваш_ключ_от_OpenWeather>
TELEGRAM_BOT_TOKEN=<ваш_токен_бота_Telegram>
```

Замените `<ваш_ключ_от_OpenWeather>` и `<ваш_токен_бота_Telegram>` на ваши актуальные значения.

### Шаг 3: Запустите Django-проект
Выполните миграции базы данных и запустите бота с помощью следующей команды:

```bash
python manage.py run_bot
```

Если всё настроено правильно, в терминале появится сообщение: "Запускаем бота...". Теперь бот готов к работе.

## Используемые API

1. **Telegram Bot API**
   - Для взаимодействия с пользователем через Telegram.
   - [Документация](https://core.telegram.org/bots/api)

2. **OpenWeather API**
   - Для получения информации о погоде.
   - [Документация](https://openweathermap.org/api)

## Пример работы программы

### 1. Команда /start
Пользователь вводит `/start` и получает приветственное сообщение:
```
Привет! Я ваш бот для погоды. Используйте команду /help, чтобы узнать доступные функции.
```

### 2. Команда /weather
Пользователь вводит `/weather`, бот запрашивает название города:
```
Введите название города:
```

Пользователь вводит название, например, `Киев`. Бот отвечает:
```
Погода в Киев: 12°C, ясно.
```

### 3. Команда /help
Пользователь вводит `/help` и получает список доступных команд:
```
Доступные команды:
/start - начать работу
/help - справка
/weather - узнать погоду.
```

### 4. Обработка ошибок
Если город введён неверно или недоступен, бот сообщает об этом:
```
Ошибка: город не найден.
```
