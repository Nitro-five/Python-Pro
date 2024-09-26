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
        return f"Product(name={self.name}, price={self.price})"


if __name__ == "__main__":
    product = ProductWithDescriptor("Sample Product", 19.99)
    print(product)

    product.price = 25.5
    print("Updated Price:", product.price)

    try:
        product.price = -10
    except ValueError as e:
        print(e)
