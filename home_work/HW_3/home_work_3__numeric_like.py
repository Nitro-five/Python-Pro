import math

class Vector:


    def __init__(self,x,y):
        self.y = y
        self.x= x


    def __add__(self, other):
        if isinstance(other,Vector):
            return Vector(self.x + other.x, self.y + other.y)
#NotImplemented используется в методах для обозначения того, что операция не поддерживается для данного типа объекта.
        return NotImplemented


    def __sub__(self, other):
        if isinstance(other,Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented


    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented


    def __lt__(self, other):
        if isinstance(other, Vector):
            return self.length() < other.length()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.length() == other.length()
        return NotImplemented


    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

def main():
    print("Введите координаты первого вектора (x y):")
    x1, y1 = map(float, input().split())
    v1 = Vector(x1, y1)

    print("Введите координаты второго вектора (x y):")
    x2, y2 = map(float, input().split())
    v2 = Vector(x2, y2)

    print("\nРезультаты операций:")
    print(f"Сложение: {v1 + v2}")
    print(f"Вычитание: {v1 - v2}")
    print(f"Умножение первого вектора на 2: {v1 * 2}")
    print(f"Длина первого вектора: {v1.length()}")
    print(f"Длина второго вектора: {v2.length()}")


if __name__ == "__main__":
    main()
