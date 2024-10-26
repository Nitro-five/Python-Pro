import re


def search_email(text):
    """
    Ищет все адреса электронной почты в данном тексте.

    Аргументы:
    text (str): Текст, в котором необходимо найти адреса электронной почты.

    Возвращает:
    list: Список всех найденных адресов электронной почты.
    """
    template = r'[a-zA-Z0-9](?:[a-zA-Z0-9._]*[a-zA-Z0-9])?@[a-zA-Z0-9]+\.(?:[a-zA-Z]{2,6})'
    return re.findall(template, text)


text = (
    'Lorem Ipsum is simply dummy text of the user123@mywebsite.net printing and typesetting industry. '
    'Lorem Ipsum has been the industrys standard dummy john.doe@gmail.com text ever since the 1500s, '
    'example@domain.com when an unknown printer took a galley of type and scrambled it to make a type specimen '
    'book alice123@yahoo.com.'
)

# Поиск всех адресов электронной почты в тексте и вывод результата
print(search_email(text))
