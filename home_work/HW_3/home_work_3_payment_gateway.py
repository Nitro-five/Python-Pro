class Price:
    def __init__(self, amount):
        self.amount = round(float(amount), 2)


    def __add__(self, other):
        if isinstance(other, Price):
            return Price(self.amount + other.amount)
        raise TypeError("Операнды должны быть типа 'Price'.")


    def __sub__(self, other):
        if isinstance(other, Price):
            return Price(self.amount - other.amount)
        raise TypeError("Операнды должны быть типа 'Price'.")


    def __lt__(self, other):
        if isinstance(other, Price):
            return self.amount < other.amount
        raise TypeError("Операнды должны быть типа  'Price'.")


    def __eq__(self, other):
        if isinstance(other, Price):
            return self.amount == other.amount
        raise TypeError("Операнды должны быть типа 'Price'.")


    def __repr__(self):
        return f"Price({self.amount:.2f})"


if __name__ == "__main__":
    price1 = Price(12.416)
    price2 = Price(6.99)

    print(price1)
    print(price2)

    total_price = price1 + price2
    print("Total:", total_price)

    difference = price1 - price2
    print("Difference:", difference)

    print(" price1 < price2?", price1 < price2)  # False
    print(" price1 == price2?", price1 == price2)  # False
