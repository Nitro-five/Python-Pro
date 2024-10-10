import pytest
from unittest.mock import patch


class BankAccount:
    """
    Класс, представляющий банковский счет.

    Атрибуты:
        balance (float): Текущий баланс счета.
    """

    def __init__(self):
        """Инициализирует новый экземпляр класса BankAccount с балансом 0.0."""
        self.balance = 0.0

    def deposit(self, amount: float):
        """
        Пополняет баланс счета.

        Параметры:
            amount (float): Сумма для пополнения. Должна быть положительной.

        Исключения:
            ValueError: Если сумма меньше или равна 0.
        """
        if amount <= 0:
            raise ValueError("Сумма должна быть больше или равно 0")
        self.balance += amount

    def withdraw(self, amount: float):
        """
        Снимает средства с счета.

        Параметры:
            amount (float): Сумма для снятия. Должна быть положительной и не превышать текущий баланс.

        Исключения:
            ValueError: Если сумма меньше или равна 0.
            ValueError: Если сумма превышает текущий баланс.
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше или равно 0")
        if amount > self.balance:
            raise ValueError("Кончились деньги на счету")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Возвращает текущий баланс счета.

        Возвращает:
            float: Текущий баланс.
        """
        return self.balance


@pytest.fixture
def bank_account():
    """
    Фикстура для создания объекта банковского счета.

    Возвращает:
        BankAccount: Новый экземпляр класса BankAccount с балансом 0.0.
    """
    return BankAccount()


@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (100.0, 100.0),
    (50.0, 50.0),
    (200.0, 200.0)
])
def test_deposit(bank_account, deposit_amount, expected_balance):
    """
    Тестирует метод deposit для разных сумм пополнения.

    Параметры:
        bank_account (BankAccount): Экземпляр банковского счета.
        deposit_amount (float): Сумма для пополнения.
        expected_balance (float): Ожидаемый баланс после пополнения.
    """
    bank_account.deposit(deposit_amount)
    assert bank_account.get_balance() == expected_balance


@pytest.mark.parametrize("withdraw_amount, initial_balance, expected_balance", [
    (50.0, 100.0, 50.0),
    (30.0, 30.0, 0.0),
])
def test_withdraw(bank_account, withdraw_amount, initial_balance, expected_balance):
    """
    Тестирует метод withdraw для разных сумм снятия.

    Параметры:
        bank_account (BankAccount): Экземпляр банковского счета.
        withdraw_amount (float): Сумма для снятия.
        initial_balance (float): Начальный баланс перед снятием.
        expected_balance (float): Ожидаемый баланс после снятия.
    """
    bank_account.deposit(initial_balance)
    bank_account.withdraw(withdraw_amount)
    assert bank_account.get_balance() == expected_balance


@pytest.mark.parametrize("withdraw_amount, initial_balance", [
    (100.0, 50.0),  
])
def test_withdraw_insufficient_funds(bank_account, withdraw_amount, initial_balance):
    """
    Тестирует метод withdraw на случай недостатка средств.

    Параметры:
        bank_account (BankAccount): Экземпляр банковского счета.
        withdraw_amount (float): Сумма для снятия.
        initial_balance (float): Начальный баланс перед снятием.

    Ожидает:
        ValueError: Если попытаться снять сумму, превышающую баланс.
    """
    bank_account.deposit(initial_balance)
    with pytest.raises(ValueError, match="Кончились деньги на счету"):
        bank_account.withdraw(withdraw_amount)


@pytest.mark.skip(reason="Пропускаємо тест на зняття з порожнього рахунку")
def test_withdraw_empty_account(bank_account):
    """
    Пропускает тест на снятие средств с пустого счета.

    Ожидает:
        ValueError: При попытке снять средства с пустого счета.
    """
    with pytest.raises(ValueError, match="Кончились деньги на счету"):
        bank_account.withdraw(50.0)


@pytest.mark.parametrize("invalid_amount", [
    (0),
    (-50.0)
])
def test_invalid_deposit(bank_account, invalid_amount):
    """Тестирует метод deposit на случай недопустимых сумм."""
    with pytest.raises(ValueError, match="Сумма должна быть больше или равно 0"):
        bank_account.deposit(invalid_amount)


@pytest.mark.parametrize("invalid_amount", [
    (0),
    (-50.0)
])
def test_invalid_withdraw(bank_account, invalid_amount):
    """Тестирует метод withdraw на случай недопустимых сумм."""
    with pytest.raises(ValueError, match="Сумма снятия должна быть больше или равно 0"):
        bank_account.withdraw(invalid_amount)


if __name__ == "__main__":
    account = BankAccount()
    account.deposit(100.0)
    account.withdraw(50.0)
    balance = account.get_balance()
    print(balance)
