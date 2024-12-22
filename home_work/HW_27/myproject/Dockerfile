FROM python:3.10-slim

# Встановлюємо системні залежності для компіляції пакунків, включаючи libmysqlclient
RUN apt-get update && \
    apt-get install -y \
    gcc \
    libpq-dev \
    musl-dev \
    pkg-config \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл requirements.txt в контейнер
COPY requirements.txt /app/

# Перевіряємо наявність файлів у директорії /app
RUN ls -l /app/

# Встановлюємо залежності з requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо інші файли проекту
COPY . /app/

# Налаштовуємо середовище
ENV PYTHONUNBUFFERED 1

# Відкриваємо порт для доступу
EXPOSE 8000

# Запускаємо сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
