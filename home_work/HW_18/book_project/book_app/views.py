from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    Представление для работы с книгами.

    Этот ViewSet предоставляет все стандартные действия для работы с книгами:
    - Получение списка всех книг
    - Получение информации о конкретной книге
    - Создание, обновление и удаление книги

    Основные параметры:
    - queryset: Список всех книг в базе данных.
    - serializer_class: Сериализатор, используемый для преобразования данных книги.
    - permission_classes: Права доступа, ограничивающие доступ к действиям.
    - filter_backends: Используемые фильтры для поиска и фильтрации.
    - filterset_fields: Поля для фильтрации.
    - search_fields: Поля, по которым будет осуществляться поиск.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author', 'genre', 'publication_year']
    search_fields = ['title']

    def perform_destroy(self, instance):
        """
        Метод для выполнения удаления книги. Только администратор может удалить книгу.

        Параметры:
            instance (Book): Объект книги, который нужно удалить.

        Исключения:
            PermissionDenied: Если пользователь не является администратором.
        """
        if not self.request.user.is_staff:
            raise PermissionDenied("You do not have permission to delete this book.")
        instance.delete()

    def get_queryset(self):
        """
        Метод для получения списка книг с фильтрацией по параметрам запроса.

        Фильтры:
            author (str): Фильтрация по автору книги.
            genre (str): Фильтрация по жанру книги.
            year (int): Фильтрация по году публикации.

        Возвращаемое значение:
            queryset: Отфильтрованный список книг.
        """
        queryset = super().get_queryset()
        author = self.request.query_params.get('author', None)
        genre = self.request.query_params.get('genre', None)
        year = self.request.query_params.get('year', None)

        if author:
            queryset = queryset.filter(author__icontains=author)
        if genre:
            queryset = queryset.filter(genre__icontains=genre)
        if year:
            queryset = queryset.filter(publication_year=year)

        return queryset

    def get_permissions(self):
        """
        Метод для получения прав доступа к действиям в зависимости от типа действия.

        Изменяет класс прав доступа для действия удаления (destroy), предоставляя доступ
        только администраторам.

        Возвращаемое значение:
            permission_classes: Список прав доступа для текущего действия.
        """
        if self.action == 'destroy':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
