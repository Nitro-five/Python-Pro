'''
Функция analyze_object принимает любой объект и выводит:
Тип объекта
Список всех методов и атрибутов объекта
Тип каждого объекта
'''

def analyze_object(obj):
    # Вывод объекта
    print(f'Тип объекта {type(obj)}')

    # Получаем список атрибутов
    method_attributes= dir(obj)

    #перебирает все имена атрибутов и методов из списка method_attributes
    for item in method_attributes:
        attr_value = getattr(obj, item)
        print(f'{item}: {type(attr_value)}')


#пример исползования
class MyClass:
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


obj = MyClass("World")
analyze_object(obj)
