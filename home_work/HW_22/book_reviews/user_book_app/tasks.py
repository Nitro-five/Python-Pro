from celery import shared_task
import csv
from django.core.exceptions import ObjectDoesNotExist
from .models import Book, Author
import time

@shared_task
def import_books_from_csv(csv_file_path):
    """
    Задача Celery для импорта книг из CSV файла.

    Эта задача обрабатывает импорт данных книг из предоставленного CSV файла. Она читает данные
    из CSV, создает или находит авторов, а затем добавляет книги в базу данных.

    Аргументы:
        csv_file_path (str): Путь к CSV файлу, содержащему данные для импорта.

    Возвращает:
        str: Строка, подтверждающая успешное завершение импорта.
    """
    start_time = time.time()

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Получаем или создаем автора
            author_name = row.get('author')
            author, created = Author.objects.get_or_create(name=author_name)

            # Создаем книгу
            Book.objects.create(
                title=row.get('title'),
                summary=row.get('summary', 'No summary available.'),
                author=author
            )

    end_time = time.time()
    print(f"Import took {end_time - start_time} seconds.")
    return f"Books import from {csv_file_path} completed."
