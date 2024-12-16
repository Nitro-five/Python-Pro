from ninja import NinjaAPI
from .models import Task
from .schemas import TaskSchema, TaskCreateSchema
from django.contrib.auth.models import User

api = NinjaAPI()

@api.get("/tasks", response=list[TaskSchema])
def get_tasks(request):
    """
    Получает список всех задач.

    Args:
        request: HTTP запрос.

    Returns:
        list[TaskSchema]: Список задач.
    """
    tasks = Task.objects.all()
    return tasks

@api.post("/tasks", response=TaskSchema)
def create_task(request, task: TaskCreateSchema):
    """
    Создает новую задачу.

    Args:
        request: HTTP запрос.
        task (TaskCreateSchema): Данные новой задачи.

    Returns:
        TaskSchema: Созданная задача.
    """
    user = User.objects.get(id=1)
    new_task = Task.objects.create(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        status=task.status,
        user=user
    )
    return new_task

@api.get("/tasks/{task_id}", response=TaskSchema)
def get_task(request, task_id: int):
    """
    Получает задачу по ID.

    Args:
        request: HTTP запрос.
        task_id (int): ID задачи.

    Returns:
        TaskSchema: Найденная задача.
    """
    task = Task.objects.get(id=task_id)
    return task

@api.put("/tasks/{task_id}", response=TaskSchema)
def update_task(request, task_id: int, task: TaskCreateSchema):
    """
    Обновляет задачу по ID.

    Args:
        request: HTTP запрос.
        task_id (int): ID задачи, которую нужно обновить.
        task (TaskCreateSchema): Новые данные для задачи.

    Returns:
        TaskSchema: Обновленная задача.
    """
    task_obj = Task.objects.get(id=task_id)
    task_obj.title = task.title
    task_obj.description = task.description
    task_obj.due_date = task.due_date
    task_obj.status = task.status
    task_obj.save()
    return task_obj

@api.delete("/tasks/{task_id}")
def delete_task(request, task_id: int):
    """
    Удаляет задачу по ID.

    Args:
        request: HTTP запрос.
        task_id (int): ID задачи, которую нужно удалить.

    Returns:
        dict: Сообщение о успешном удалении задачи.
    """
    task = Task.objects.get(id=task_id)
    task.delete()
    return {"message": "Task deleted"}
