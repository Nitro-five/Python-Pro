from django.shortcuts import render
from links.models import Link, Click
from django.db.models import Count
from django.utils.timezone import now, timedelta


def analytics_home(request):
    """
    Представление для отображения аналитики пользователей, включая:
    - Общее количество кликов по ссылкам пользователя
    - Статистика по устройствам (PC, Tablet, Mobile, Unknown)
    - Статистика по странам
    - Статистика кликов за последние 30 дней

    Если пользователь не авторизован, будет отображено сообщение об ошибке.

    Args:
        request: Объект запроса от клиента.

    Returns:
        render: Рендерит шаблон 'analytics/user_statistics.html' с данными статистики.
    """
    if request.user.is_authenticated:
        # Получаем ссылки пользователя
        user_links = Link.objects.filter(user=request.user)

        # Общее количество кликов по ссылкам пользователя
        total_clicks = Click.objects.filter(link__in=user_links).count()

        # Статистика по устройствам
        device_stats = Click.objects.filter(link__in=user_links).values('device').annotate(count=Count('id'))
        device_data = {
            "PC": 0,
            "Tablet": 0,
            "Mobile": 0,
            "Unknown": 0,
        }
        for device in device_stats:
            device_data[device['device']] = device['count']

        # Статистика по странам
        country_stats = Click.objects.filter(link__in=user_links).values('country').annotate(count=Count('id'))

        # Статистика кликов за последние 30 дней
        last_30_days = now() - timedelta(days=30)
        clicks_last_30_days = Click.objects.filter(link__in=user_links, timestamp__gte=last_30_days).count()

        return render(request, 'analytics/user_statistics.html', {
            'total_clicks': total_clicks,
            'device_data': device_data,
            'country_stats': country_stats,
            'clicks_last_30_days': clicks_last_30_days,
        })
    else:
        return render(request, 'analytics/user_statistics.html',
                      {'error': 'Вы должны быть авторизованы, чтобы видеть аналитику.'})
