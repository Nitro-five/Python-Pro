# Завдання 3: Магазин замовлень з акційними знижками
discount = 0.1

def create_order(price):
    print(f"Начальная цена: {price}")
    discount_price = price * (1-discount)
    print(f"Цена со скидкой: {discount_price}")

    def new_discount(add_discount):
        nonlocal discount_price
        discount_price = discount_price * (1-add_discount)

    new_discount(0.06)
    print(f"Цена после VIP скидки: {discount_price}")

create_order(1000)
