from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book
from django.core.cache import cache

@receiver(post_save, sender=Book)
def update_book_cache(sender, instance, **kwargs):
    """
    Сигнал, который срабатывает после сохранения объекта модели Book.

    Этот сигнал удаляет кэшированный список книг после того, как книга была добавлена или обновлена,
    чтобы обеспечить актуальность данных в кэше.

    Аргументы:
        sender (Model): Модель, от которой был вызван сигнал (в данном случае Book).
        instance (Book): Экземпляр модели Book, который был сохранен.
        **kwargs: Дополнительные аргументы, передаваемые сигналом.
    """
    # Удаляем кэш для обновления списка книг
    cache.delete('book_list')
