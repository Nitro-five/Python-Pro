import pytest


class AgeVerifier:
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18


# Параметризованный тест
@pytest.mark.parametrize('age, expected', [
    (17, False),
    (18, True),
    (20, True),
    (120, True),
])
def test_is_adult(age, expected):
    assert AgeVerifier.is_adult(age) == expected


# Тест с ошибочным возрастом (отрицательные значения)
@pytest.mark.skip(reason="Общие условие скиппа")
@pytest.mark.parametrize('age', [-1, -100, -50])
def test_is_adult_error_age(age):
    pass


# Тест с маловероятными значениями возраста (больше 120 лет)
@pytest.mark.skipif(lambda: True, reason="Неправильный возраст")
@pytest.mark.parametrize('age', [121, 130, 150])
def test_is_adult_unlikely_age(age):
    assert AgeVerifier.is_adult(age) == False


if __name__ == "__main__":
    age = 20
    is_adult=AgeVerifier.is_adult(age)
    print(f"Человек возрастом {age} является взрослым: {is_adult}")
