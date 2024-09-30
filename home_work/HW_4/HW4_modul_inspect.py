import importlib
import inspect
"""
Функция analyze_module отвечает за:
извлекает и выводит список его функций и классов, включая их сигнатуры.
"""
def analyze_module(module_name):
    module = importlib.import_module(module_name)

    # Получение всех атрибутов модуля
    attributes = dir(module)
    #Генерация списка из имен атрибутов модуля, которые являются вызываемыми объектами
    functions = [attr for attr in attributes if callable(getattr(module, attr))]
    classes = inspect.getmembers(module, inspect.isclass)

    # Обработка функций
    print(f"Функции в модуле {module_name}:")
    if not functions:
        print("<нет функций в модуле>")
    else:
        for function_name in functions:
            function_obj = getattr(module, function_name)
            # Относительно безопасно запускаем блок кода чтобы избжедать ошибок
            try:
                sig = inspect.signature(function_obj)
                print(f"- {function_name}{sig}")
            except ValueError:
                print(f"- {function_name} (сигнатура не найдена)")


    # Обработка классов
    print(f" Классы в модуле {module_name}:")
    if not classes:
        print("<нет классов в модуле>")
    else:
        for class_name, class_obj in classes:
            print(f"- {class_name} {inspect.signature(class_obj)}")

# Вызов функции с параметром
analyze_module("math")
