from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task


def signup(request):
    """
    Представление для регистрации пользователя.

    При GET-запросе отображается форма для регистрации пользователя.
    При POST-запросе выполняется валидация и сохранение нового пользователя,
    после чего пользователь автоматически авторизуется и перенаправляется на страницу списка задач.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Авторизуем пользователя после регистрации
            return redirect('task_list')  # Перенаправляем на страницу задач
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def create_task(request):
    """
    Представление для создания новой задачи.

    При GET-запросе отображается пустая форма для создания задачи.
    При POST-запросе проверяется форма на валидность и сохраняется новая задача, связанная с текущим пользователем.
    После успешного сохранения задачи происходит перенаправление на страницу списка задач.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Привязываем пользователя
            task.save()  # Сохраняем задачу
            return redirect('task_list')  # Перенаправление на страницу списка задач
    else:
        form = TaskForm()

    return render(request, 'create_task.html', {'form': form})


@login_required
def task_list(request):
    """
    Представление для отображения списка задач пользователя.

    Отображает все задачи, связанные с текущим пользователем.
    Только авторизованные пользователи могут видеть список своих задач.
    """
    tasks = Task.objects.filter(user=request.user)  # Получаем все задачи для текущего пользователя
    return render(request, 'task_list.html', {'tasks': tasks})
