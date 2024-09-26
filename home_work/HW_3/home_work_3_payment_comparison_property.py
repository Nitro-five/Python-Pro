class ProductWithProperty:
    def __init__(self, name, price):
        self._name = name
        self._price = 0.0  # Инициализация скрытого атрибута
        self.price = price  # Установка через сеттер

    @property
    def price(self):
        return self._price


    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._price = round(float(value), 2)
        else:
            raise ValueError("Цена должна быть неотрицательным числом")

    def __repr__(self):
        return f"Product(name={self._name}, price={self.price})"


if __name__ == "__main__":
    product = ProductWithProperty("Sample Product", 19.99)
    print(product)

    product.price = 25.5
    print("Updated Price:", product.price)

    try:
        product.price = -10
    except ValueError as e:
        print(e)
