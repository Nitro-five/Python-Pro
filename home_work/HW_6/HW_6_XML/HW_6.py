import xml.etree.ElementTree as ET


def load_products(filename):
    """
    Читает XML-файл и возвращает список продуктов.

    Параметры:
    filename : str
        Имя XML-файла для чтения.

    Возвращает:
    list
        Список продуктов, где каждый продукт представлен как словарь
        с ключами 'name' и 'quantity'.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    products = []
    for product in root.findall('product'):
        name = product.find('name').text
        quantity = int(product.find('quantity').text)
        products.append({'name': name, 'quantity': quantity})

    return products


def print_products(products):
    """
    Выводит названия продуктов и их количество.

    Параметры:
    products : list
        Список продуктов.

    """
    for product in products:
        print(f"Название: {product['name']}, Количество: {product['quantity']}")


def update_quantity(filename, product_name, new_quantity):
    """
    Изменяет количество товара в XML-файле.

    Параметры:
    filename : str
        Имя XML-файла для обновления.
    product_name : str
        Название продукта, количество которого нужно изменить.
    new_quantity : int
        Новое количество продукта.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    for product in root.findall('product'):
        name = product.find('name').text
        if name == product_name:
            product.find('quantity').text = str(new_quantity)
            break

    # Сохраняем изменения в файл
    tree.write(filename)


def main():
    filename = 'products.xml'

    # Читаем продукты из файла
    products = load_products(filename)

    # Выводим названия продуктов и их количество
    print_products(products)

    # Пример изменения количества товара
    product_name = 'Продукт 1'
    new_quantity = 15
    update_quantity(filename, product_name, new_quantity)
    print(f"Количество продукта '{product_name}' изменен на {new_quantity}.")


if __name__ == "__main__":
    main()
