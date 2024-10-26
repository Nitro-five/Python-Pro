import re

def search_phone(phone):
    """
    Ищет телефонные номера в различных форматах в заданной строке.

    Аргументы:
    phone (str): Текст, в котором необходимо найти телефонные номера.

    Возвращает:
    list: Список всех найденных телефонных номеров в различных форматах.
    """
    template = r'(?:\(\d{3}\)\s*|\d{3}[-.])?\d{3}[-.]\d{4}|\d{10}'
    return re.findall(template, phone)

phone = (
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry.(123) 456-7890 Lorem Ipsum has "
    "123-456-7890 been the industry's 123.456.7890 standard dummy text ever 1234567890 since the 1500s, when "
    "an unknown printer took a galley of type and scrambled it to make a type specimen book."
)

# Поиск всех телефонных номеров в строке и вывод результата
print(search_phone(phone))
