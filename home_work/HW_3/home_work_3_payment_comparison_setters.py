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
        return f"Product(name={self._name}, price={self._price})"

if __name__ == "__main__":
    product = ProductWithGetSet("Sample Product", 19.99)
    print(product)

    product.set_price(25.5)
    print("Updated Price:", product.get_price())

    try:
        product.set_price(-10)
    except ValueError as e:
        print(e)  # Price must be a non-negative number.
