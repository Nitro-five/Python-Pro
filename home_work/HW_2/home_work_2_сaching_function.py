# Завдання 9: Кешування результатів функції
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

@memoize
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) #Каждое следующее число является суммой двух предыдущих:F(n)=F(n−1)+F(n−2)

if __name__ == "__main__":
    num = int(input("Введите номер числа Фибоначчи: "))
    result = fibonacci(num)
    print(f"Число Фибоначчи для {num} = {result}")
