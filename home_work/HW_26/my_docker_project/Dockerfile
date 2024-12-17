# Використовуємо образ Python
FROM python:3.10-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл вимог
COPY requirements.txt /app/

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо увесь код проекту
COPY . /app/

# Відкриваємо порт 8000
EXPOSE 8000

# Запускаємо Django сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
