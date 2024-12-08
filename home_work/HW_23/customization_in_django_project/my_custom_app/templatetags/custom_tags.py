from django import template

register = template.Library()


@register.filter(name='reverse_string')
def reverse_string(value):
    """
    Фильтр для реверсирования строки.

    :param value: Строка, которую нужно развернуть.
    :return: Развернутая строка.
    """
    return value[::-1]


@register.simple_tag
def get_full_name(first_name, last_name):
    """
    Тег для получения полного имени.

    :param first_name: Имя.
    :param last_name: Фамилия.
    :return: Полное имя, состоящее из имени и фамилии.
    """
    return f"{first_name} {last_name}"


def global_settings(request):
    """
    Функция для добавления глобальных настроек в контекст шаблона.

    :param request: HTTP-запрос.
    :return: Словарь с глобальными настройками, такими как название сайта и текущий год.
    """
    return {
        'site_name': 'My Awesome Site',
        'year': 2024,
    }
