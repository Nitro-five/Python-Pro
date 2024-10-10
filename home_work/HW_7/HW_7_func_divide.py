import pytest


def divide(a: int, b: int) -> float:
    """
    Делит два числа.

    Параметры:
    a (int): Делимое число.
    b (int): Знаменатель. Не может быть нулем.

    Возвращает:
    float: Результат деления a на b.

    Исключения:
    ZeroDivisionError: Если b равно нулю.
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return a / b


def test_divide():
    """
    Тестирует функцию divide с различными наборами значений.
    Проверяет, что результаты деления корректны.
    """
    assert divide(10, 2) == 5.0
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0


def test_zero_divide():
    """
    Тестирует функцию divide на случай, когда знаменатель равен нулю.
    Проверяет, что возникает исключение ZeroDivisionError.
    """
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_param_divide():
    """
    Параметризованный тест для функции divide.
    Проверяет деление на нескольких наборах значений.
    """
    test_cases = [
        (10, 2, 5.0),
        (20, 4, 5.0),
        (-20, 4, -5.0),
        (0, 1, 0.0),
        (1, 0.5, 2.0)
    ]
    for a, b, expected in test_cases:
        assert divide(a, b) == expected


if __name__ == "__main__":
    print(divide(10, 2))
