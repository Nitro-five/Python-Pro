from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Link, Click
from .forms import LinkForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.timezone import now
from django.db.models import Count


def index(request):
    """
    Представление для главной страницы, где пользователи могут ввести оригинальную ссылку
    и получить короткую ссылку. Если пользователь авторизован, ссылка будет ассоциирована с его учетной записью.
    """
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            user = request.user if request.user.is_authenticated else None
            link, created = Link.objects.get_or_create(original_url=original_url, user=user)
            return render(request, "links/index.html", {"form": form, "link": link})
    else:
        form = LinkForm()
    return render(request, "links/index.html", {"form": form})


def redirect_to_original(request, short_url):
    """
    Представление для перенаправления по короткой ссылке на оригинальную ссылку.
    При каждом клике на ссылку, увеличивается количество кликов и создается запись в модели Click.
    """
    link = get_object_or_404(Link, short_url=short_url)
    link.clicks += 1
    link.save()

    # Определение устройства и страны (здесь страна остается 'Unknown', можно расширить функциональность)
    device = request.META.get('HTTP_USER_AGENT', 'Unknown')
    country = 'Unknown'

    # Создание записи о клике
    Click.objects.create(link=link, user_ip=request.META['REMOTE_ADDR'], device=device, country=country)

    # Перенаправление на оригинальную ссылку
    return redirect(link.original_url)


@login_required
def user_links(request):
    """
    Представление для отображения списка ссылок пользователя с подсчетом уникальных кликов.
    Показывает все сокращенные ссылки пользователя и количество уникальных кликов по каждой из них.
    """
    links = Link.objects.filter(user=request.user).annotate(unique_clicks=Count('clicks_data__user_ip', distinct=True))
    return render(request, "links/user_links.html", {"links": links})


def register(request):
    """
    Представление для регистрации нового пользователя. После успешной регистрации и входа,
    пользователь перенаправляется на главную страницу.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
