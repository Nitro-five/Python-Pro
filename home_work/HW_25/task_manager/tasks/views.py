from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели Task.

    Предоставляет методы для выполнения стандартных операций CRUD с задачами:
    создание, чтение, обновление и удаление.

    Атрибуты:
        queryset (QuerySet): Запрос для получения всех задач.
        serializer_class (TaskSerializer): Сериализатор для преобразования данных задачи.
        permission_classes (list): Список классов разрешений, в данном случае доступ только для авторизованных пользователей.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Возвращает отфильтрованный список задач в зависимости от параметра 'status'.

        Если параметр 'status' передан в запросе, фильтрует задачи по статусу.
        В противном случае возвращает все задачи. Задачи сортируются по времени их создания.

        Returns:
            QuerySet: Отфильтрованный и отсортированный список задач.
        """
        queryset = super().get_queryset()
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        return queryset.order_by('created_at')
