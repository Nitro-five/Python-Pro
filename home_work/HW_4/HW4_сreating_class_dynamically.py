"""
Функция create_class(class_name, methods) создает класс с заданным именем и методами.
Методы передаются в виде словаря, где ключи - это названия методов, а значения
"""
def create_class(class_name, methods):
    #Динамическое создание класса через функцию type и наследования от базового класса object
    return type(class_name, (object,), methods)


# Пример использования
def say_hello(self):
    return "Hello!"


def say_goodbye(self):
    return "Goodbye!"


methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}

MyDynamicClass = create_class("MyDynamicClass", methods)

obj = MyDynamicClass()
print(obj.say_hello())  # Hello!
print(obj.say_goodbye())  # Goodbye!
