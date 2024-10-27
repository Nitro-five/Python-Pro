import re

date_data = "25/10/2024"


def change_date_formate(date_data):
    '''
        Преобразует дату из формата DD/MM/YYYY в формат DD-MM-YYYY.

        Аргументы:
        date_data (str): Дата в формате DD/MM/YYYY.

        Возвращает:
        str: Дата в формате DD-MM-YYYY.
    '''
    template = r'^(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})$'
    match = re.match(template, date_data)

    ## Получение значений дня, месяца и года из соответствия
    day = match.group('day')
    month = match.group('month')
    year = match.group('year')

    return f'{day}-{month}-{year}'


print(change_date_formate(date_data))
