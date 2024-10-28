import re

text = 'This is a test string with code AB12CD34 and some other text.'


def search_template(text):
    """
    Проверяет, содержится ли в тексте строка формата AB12CD34,
    где A, B, C, D — большие буквы, а 1, 2, 3, 4 — цифры.

    Аргументы:
    text (str): Текст для проверки.

    Возвращает:
    MatchObject или None: Если найдено совпадение, возвращает объект совпадения, иначе None.
    """
    # Шаблон для поиска: две большие буквы, две цифры, две большие буквы, две цифры
    template = r'[A-Z]{2}\d{2}[A-Z]{2}\d{2}'

    # Ищем совпадение в тексте и возвращаем результат
    return re.search(template, text)


# Печатаем результат: если совпадение найдено, выводим его
# Используем .group() для получения найденной строки
result = search_template(text)
if result:
    print(f'Найдено совпадение: {result.group()}')
else:
    print('Совпадение не найдено.')
