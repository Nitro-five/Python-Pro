from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class BookAPITests(APITestCase):
    """
    Тесты для API работы с книгами.

    Этот класс тестирует основные операции с книгами через API, такие как:
    - Получение списка книг
    - Создание новой книги
    - Удаление книги администратором

    Используются тестовые данные, включая пользователя и авторизацию с помощью JWT токенов.
    """

    def setUp(self):
        """
        Подготовка данных для тестов.

        Создается тестовая книга и пользователь для тестирования. Также генерируется JWT токен для
        аутентификации запросов.
        """
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            genre="Fiction",
            publication_year=2020
        )
        self.user = User.objects.create_user(username="testuser", password="password")
        self.token = str(RefreshToken.for_user(self.user).access_token)

    def test_get_books(self):
        """
        Тест на получение списка книг.

        Выполняет GET-запрос для получения списка всех книг, проверяя, что статус ответа равен 200 OK.
        """
        url = reverse('book-list')  # Получаем URL для списка книг
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        """
        Тест на создание новой книги.

        Выполняет POST-запрос для добавления новой книги через API, проверяя, что книга была успешно создана
        и статус ответа равен 201 Created.
        """
        url = reverse('book-list')  # Получаем URL для создания новой книги
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'genre': 'Fantasy',
            'publication_year': 2021
        }
        response = self.client.post(url, data, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_book_admin(self):
        """
        Тест на удаление книги администратором.

        Для этого теста создается суперпользователь, который выполняет DELETE-запрос на удаление книги.
        Ожидаемый результат: статус ответа 204 No Content, подтверждающий успешное удаление.
        """
        admin_user = User.objects.create_superuser(username="admin", password="password")
        self.client.force_authenticate(user=admin_user)  # Аутентификация как администратор
        url = reverse('book-detail', args=[self.book.id])  # URL для удаления конкретной книги
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
