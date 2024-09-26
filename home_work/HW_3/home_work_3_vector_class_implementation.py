#Размерность вектора указывает, сколько компонент (координат) он содержит.

import math

class Vector:
    def __init__(self, *components):
        self.components = components


    def __add__(self, other):

        if len(self.components) != len(other.components):
            raise ValueError("Векторы должны быть одинаковой размерности для сложения.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):

        if len(self.components) != len(other.components):
            raise ValueError("Векторы должны быть одинаковой размерности для вычитания.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))


    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Векторы должны быть одинаковой размерности для умножения.")
        return sum(a * b for a, b in zip(self.components, other.components))


    def length(self):
        return math.sqrt(sum(x ** 2 for x in self.components))


    def __lt__(self, other):
        return self.length() < other.length()


    def __eq__(self, other):
        return self.length() == other.length()


    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print("v1:", v1)  # Vector(1, 2, 3)
    print("v2:", v2)  # Vector(4, 5, 6)

    v3 = v1 + v2
    print("v1 + v2:", v3)  # Vector(5, 7, 9)

    v4 = v1 - v2
    print("v1 - v2:", v4)  # Vector(-3, -3, -3)

    scalar_product = v1 * v2
    print("v1 * v2:", scalar_product)  # 32

    print("Длина v1:", v1.length())  # Длина вектора v1
    print("Длина v2:", v2.length())  # Длина вектора v2

    print("v1 < v2?", v1 < v2)  # True или False в зависимости от длин
    print("v1 == v2?", v1 == v2)  # True или False
