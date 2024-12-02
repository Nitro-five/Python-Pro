from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Author(models.Model):
    """
    Модель автора книги.

    Описание автора, включая имя и биографию.

    Атрибуты:
        name (CharField): Имя автора.
        biography (TextField): Биография автора.

    Методы:
        __str__(): Возвращает имя автора.
    """
    name = models.CharField(max_length=200)
    biography = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Модель книги.

    Описание книги, включая название, автора, аннотацию и рейтинг.

    Атрибуты:
        title (CharField): Название книги.
        author (ForeignKey): Автор книги.
        summary (TextField): Аннотация книги.
        rating (DecimalField): Рейтинг книги (до 3 цифр, 2 знака после запятой).

    Методы:
        __str__(): Возвращает название книги.

    Мета:
        indexes: Индекс по полю `title` для оптимизации поиска.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    summary = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    class Meta:
        indexes = [
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title


class Review(models.Model):
    """
    Модель отзыва на книгу.

    Описание отзыва, включая пользователя, книгу, рейтинг, комментарий и дату создания.

    Атрибуты:
        user (ForeignKey): Пользователь, оставивший отзыв.
        book (ForeignKey): Книга, к которой оставлен отзыв.
        rating (PositiveIntegerField): Рейтинг книги (от 1 до 5).
        comment (TextField): Комментарий пользователя.
        created_at (DateTimeField): Дата и время создания отзыва.

    Методы:
        __str__(): Возвращает строковое представление отзыва (пользователь и книга).

    Мета:
        indexes: Индекс по полю `rating` для оптимизации поиска.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews", default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['rating']),
        ]

    def __str__(self):
        return f"Review by {self.user.username} on {self.book.title}"
