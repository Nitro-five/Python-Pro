from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm


def register_view(request):
    """
    Представление для регистрации нового пользователя.

    Если запрос POST, форма регистрации проверяется и сохраняется. Создается новый пользователь,
    а также создается его профиль, если он еще не существует. После успешной регистрации пользователь
    авторизуется и перенаправляется на страницу профиля.

    Если запрос GET, отображается пустая форма регистрации.

    Возвращает:
        Рендерит шаблон с формой регистрации или перенаправляет на страницу профиля после успешной регистрации.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Создаем профиль пользователя, если его еще нет
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            # Выполняем вход пользователя
            login(request, user)
            messages.success(request, 'Регистрация успешна!')
            return redirect('profile')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def profile_view(request):
    """
    Представление для отображения профиля пользователя.

    Проверяется наличие профиля пользователя. Если профиль не существует, он создается автоматически.
    Возвращает:
        Рендерит шаблон с данными профиля пользователя.
    """
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # Если профиль не существует, создаем его
        profile = UserProfile.objects.create(user=request.user)

    return render(request, 'profile.html', {'profile': profile})


@login_required
def edit_profile_view(request):
    """
    Представление для редактирования профиля пользователя.

    Если профиль пользователя не существует, он будет создан. При отправке формы с POST-запросом,
    если форма валидна, изменения сохраняются в базе данных. После сохранения редирект на страницу профиля.

    Если запрос GET, отображается форма для редактирования профиля.

    Возвращает:
        Рендерит шаблон с формой для редактирования профиля.
    """
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # Если профиль не существует, создаем его
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Сохраняем изменения в профиле
            form.save()
            messages.success(request, 'Профиль обновлён!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


@login_required
def change_password_view(request):
    """
    Представление для изменения пароля пользователя.

    При отправке POST-запроса форма пароля проверяется, и если она валидна, сохраняется новый пароль.
    После успешного изменения пароля, пользователь перенаправляется на страницу профиля.

    При GET-запросе отображается форма для изменения пароля.

    Возвращает:
        Рендерит шаблон с формой для изменения пароля.
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пароль изменён!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})
