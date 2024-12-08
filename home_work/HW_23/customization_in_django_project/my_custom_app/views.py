from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializers import MyModelSerializer
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .models import MyModel, RequestMetric


def home_view(request):
    """
    Представление для домашней страницы.

    :param request: HTTP-запрос.
    :return: Ответ с рендером домашней страницы.
    """
    return render(request, 'home.html')


class CustomView(View):
    """
    Класс для обработки кастомных представлений.

    Этот класс обрабатывает GET-запросы и возвращает текстовый ответ.
    """

    def get(self, request):
        """
        Обработка GET-запроса.

        :param request: HTTP-запрос.
        :return: Текстовый ответ.
        """
        return HttpResponse("This is a custom view", content_type="text/plain")


class MyModelViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с моделью MyModel.

    Предоставляет полный набор операций для работы с моделью MyModel,
    включая фильтрацию и поиск по полю 'name'.
    """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['name']


def register(request):
    """
    Представление для регистрации нового пользователя.

    Обрабатывает форму регистрации, создаёт нового пользователя и авторизует его.

    :param request: HTTP-запрос.
    :return: Ответ с рендером страницы регистрации.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем пользователя
            login(request, user)  # Авторизуем пользователя после регистрации
            return redirect('home')  # Перенаправляем на домашнюю страницу (или другую страницу)
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration.html', {'form': form})


def mymodel_list(request):
    """
    Представление для отображения списка объектов MyModel.

    :param request: HTTP-запрос.
    :return: Ответ с рендером страницы со списком объектов.
    """
    mymodels = MyModel.objects.all()
    return render(request, 'mymodel_list.html', {'mymodels': mymodels})


class RequestMetricView(View):
    """
    Представление для получения информации о количестве запросов.

    Возвращает количество запросов в формате JSON.
    """

    def get(self, request):
        """
        Обработка GET-запроса для получения количества запросов.

        :param request: HTTP-запрос.
        :return: Ответ в формате JSON с количеством запросов.
        """
        metric, created = RequestMetric.objects.get_or_create(id=1)
        return JsonResponse({'request_count': metric.count})
