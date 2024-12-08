def some_context_processor(request):
    """
    Контекстный процессор для добавления глобальных значений в контекст шаблона.

    :param request: HTTP-запрос.
    :return: Словарь с глобальными значениями, такими как название сайта и текущий год.
    """
    return {
        'site_name': 'my_custom_app',
        'current_year': 2024
    }
