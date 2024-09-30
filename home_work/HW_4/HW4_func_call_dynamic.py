"""
Функция call_function принимает объект,
название метода в виде строки
и произвольные аргументы для этого метода.
"""

def call_function(obj, method_name, *args):
    method = getattr(obj, method_name)

    return method(*args)


# Пример использование
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calc = Calculator()
print(call_function(calc, "add", 10, 5))  # 15
print(call_function(calc, "subtract", 10, 5))  # 5
