from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from .forms import CustomUserCreationForm
from .models import Book, Author
from .tasks import import_books_from_csv
from .forms import ReviewForm


def home(request):
    """
    Представление для главной страницы.

    Отображает главную страницу сайта.

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.

    Возвращает:
        HttpResponse: Ответ с отрисовкой главной страницы.
    """
    return render(request, 'home.html')


def register(request):
    """
    Представление для страницы регистрации пользователя.

    Обрабатывает POST-запросы с данными формы регистрации. После успешной регистрации
    перенаправляет на страницу логина.

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.

    Возвращает:
        HttpResponse: Ответ с отрисовкой страницы регистрации или перенаправлением на страницу логина.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    """
    Представление для страницы логина.

    Обрабатывает POST-запросы с данными для аутентификации. После успешной аутентификации
    пользователя перенаправляет на главную страницу.

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.

    Возвращает:
        HttpResponse: Ответ с отрисовкой страницы логина или перенаправлением на главную страницу.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """
    Представление для выхода из системы.

    Завершается выходом пользователя и перенаправлением на главную страницу.

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.

    Возвращает:
        HttpResponseRedirect: Перенаправление на главную страницу после выхода.
    """
    logout(request)
    return redirect('home')


def book_detail(request, book_id):
    """
    Представление для страницы с подробной информацией о книге.

    Отображает информацию о книге и позволяет оставлять отзывы.

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.
        book_id (int): Идентификатор книги.

    Возвращает:
        HttpResponse: Ответ с отрисовкой страницы книги и формы отзыва.
    """
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm()

    return render(request, 'book_detail.html', {'book': book, 'form': form})


@login_required
def greeting_view(request):
    """
    Представление для приветственной страницы.

    Доступно только авторизованным пользователям. Отображает приветственную страницу.

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.

    Возвращает:
        HttpResponse: Ответ с отрисовкой приветственной страницы.
    """
    return render(request, 'greeting.html')


@login_required
def book_list(request):
    """
    Представление для страницы списка книг.

    Загружает список книг, используя кеш для оптимизации производительности.
    Если книги не найдены в кеше, выполняется запрос к базе данных и данные кешируются.

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.

    Возвращает:
        HttpResponse: Ответ с отрисовкой страницы списка книг.
    """
    cached_books = cache.get('book_list')
    if not cached_books:
        books = Book.objects.select_related('author').prefetch_related('reviews').all()
        cache.set('book_list', books, timeout=60 * 15)  # Кешируем на 15 минут
    else:
        books = cached_books

    return render(request, 'book_list.html', {'books': books})


@login_required
def author_stats(request):
    """
    Представление для страницы статистики авторов.

    Отображает статистику по авторам, включая средний рейтинг и количество книг.

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.

    Возвращает:
        HttpResponse: Ответ с отрисовкой страницы статистики авторов.
    """
    authors = Author.objects.annotate(
        avg_rating=Avg('books__reviews__rating'),
        book_count=Count('books')
    )
    return render(request, 'author_stats.html', {'authors': authors})


@login_required
def import_books_view(request):
    """
    Представление для импорта книг из CSV файла.

    Обрабатывает POST-запросы с файлом CSV, сохраняет файл и запускает задачу импорта через Celery.

    Аргументы:
        request (HttpRequest): HTTP-запрос пользователя.

    Возвращает:
        HttpResponse: Ответ с отрисовкой страницы импорта книг или информацией о задаче.
    """
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']

        fs = FileSystemStorage()
        filename = fs.save(csv_file.name, csv_file)
        file_url = fs.url(filename)

        task = import_books_from_csv.apply_async(args=[fs.path(filename)])

        return render(request, 'import_books.html', {'task_id': task.id, 'file_url': file_url})

    return render(request, 'import_books.html')
