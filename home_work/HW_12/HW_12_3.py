import re

def search_hashtags(text):
    """
    Извлекает хеш-теги из заданного текста.

    Аргументы:
    text (str): Текст, из которого необходимо извлечь хеш-теги.

    Возвращает:
    list: Список найденных хеш-тегов, начинающихся с '#'.
    """
    # Шаблон для поиска хеш-тегов
    template = r'#\w+'
    return re.findall(template, text)

text = (
    'Just finished reading an amazing book about #ArtificialIntelligence and #MachineLearning! '
    'It really opened my eyes to the potential of #DataScience in various industries. '
    'Can t wait to apply these concepts in my next project! Also, if you re into tech, '
    'check out #Innovation and #FutureTrends for some great insights.'
)

# Поиск хеш-тегов в тексте и вывод результата
print(search_hashtags(text))
