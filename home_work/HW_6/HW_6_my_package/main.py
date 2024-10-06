from .my_package import factorial, gcd, to_upper, del_spaces


def main():
    num = 5
    print(f"Факториал {num}: {factorial(num)}")

    a, b = 48, 18
    print(f"Наибольший общий делитель чисел {a} и {b}: {gcd(a, b)}")

    text = "  Hello, World!  "
    print(f"Текст верхнем регистре: '{to_upper(text)}'")
    print(f"Результат: '{del_spaces(text)}'")


if __name__ == "__main__":
    main()
