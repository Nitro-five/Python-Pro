import doctest


def is_even(n: int) -> bool:
    """
    Проверка на парность числа

    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(0)
    True
    >>> is_even(-4)
    True
    >>> is_even(-3)
    False
    """
    return n % 2 == 0


def fibonacci(n: int) -> int:
    """
    Возращает n число Фиббоначи.

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(10)
    55
    >>> fibonacci(-1)
    Traceback (most recent call last):
        ...
    ValueError: Отрицательные числа недопустимы!
    """
    if n < 0:
        raise ValueError("Отрицательные числа недопустимы!")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    doctest.testmod()
    print(fibonacci(12))
