# Завдання 10: Створення товарів для онлайн-магазину
def create_product(name, price, quantity):
    def update_price(new_price):
        nonlocal price
        price = new_price
        return f"Цена товара '{name}' изменена {price:.2f} UAH"

    def product_info():
        return {
            'name': name,
            'price': price,
            'quantity': quantity
        }

    return update_price, product_info

if __name__ == "__main__":
    update_price, product_info = create_product("яблоко", 1.50, 100)

    print(product_info())
    print(update_price(2.00))
    print(product_info())
