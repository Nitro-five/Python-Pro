class ProductWithGetSet:
    def __init__(self, name, price):
        self._name = name
        self._price = 0.0
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._price = round(float(value), 2)
        else:
            raise ValueError("Цена должна быть неотрицательным числом")

    def __repr__(self):
        return f"ProductWithGetSet(name={self._name}, price={self._price})"


class ProductWithProperty:
    def __init__(self, name, price):
        self._name = name
        self._price = 0.0
        self.price = price

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
        return f"ProductWithProperty(name={self._name}, price={self.price})"


class PriceDescriptor:
    def __init__(self):
        self.value = 0.0

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.value = round(float(value), 2)
        else:
            raise ValueError("Цена должна быть неотрицательным числом")


class ProductWithDescriptor:
    price = PriceDescriptor()

    def __init__(self, name, price):
        self._name = name
        self.price = price

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f"ProductWithDescriptor(name={self.name}, price={self.price})"


def test_product_classes():
    print("Testing ProductWithGetSet")
    product1 = ProductWithGetSet("Sample Product 1", 19.99)
    print(product1)
    print("Current Price:", product1.get_price())

    product1.set_price(25.5)
    print("Updated Price:", product1.get_price())

    try:
        product1.set_price(-10)
    except ValueError as e:
        print(e)


    print("\nTesting ProductWithProperty")
    product2 = ProductWithProperty("Sample Product 2", 29.99)
    print(product2)
    print("Current Price:", product2.price)

    product2.price = 35.5
    print("Updated Price:", product2.price)

    try:
        product2.price = -5
    except ValueError as e:
        print(e)


    print("\nTesting ProductWithDescriptor")
    product3 = ProductWithDescriptor("Sample Product 3", 39.99)
    print(product3)
    print("Current Price:", product3.price)

    product3.price = 45.0
    print("Updated Price:", product3.price)

    try:
        product3.price = -15
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    test_product_classes()
