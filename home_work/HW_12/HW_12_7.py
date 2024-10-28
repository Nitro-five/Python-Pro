import re


def search_ipv4(ip_data):
    """
    Извлекает все действительные IPv4-адреса из предоставленного текста.

    IPv4-адрес состоит из четырех чисел, разделенных точками.
    Каждое число должно находиться в диапазоне от 0 до 255.

    Аргументы:
    ip_data (str): Текст, из которого необходимо извлечь IPv4-адреса.

    Возвращает:
    list: Список действительных IPv4-адресов.
    """
    template = r'(?:\d{1,3}\.){3}\d{1,3}'

    addresses = re.findall(template, ip_data)

    valid_addresses = []
    for i in addresses:
        parts = i.split('.')
        valid = True

        for num in parts:
            # Проверяем, что каждое число в диапазоне от 0 до 255
            if not (0 <= int(num) <= 255):
                valid = False
                # Прерываем цикл, если одно из чисел недопустимо
                break

        if valid:
            # Добавляем адрес в список действительных, если он прошёл проверку
            valid_addresses.append(i)

    return valid_addresses


ip_data = ('Here are some IP addresses: 192.168.1.1, 255.255.255.255, '
           '10.0.0.256 (invalid), 172.16.254.1 and 0.0.0.0.')

print(search_ipv4(ip_data))
