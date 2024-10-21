# Завдання 7: Трекер витрат
import unittest

total_expense = 0.0

def change_total_expense(amount):
    global total_expense
    total_expense += amount

def get_expense():
    return total_expense

def user_expense():
    while True:
        print("\n1. Добавить расходы")
        print("2. Общие расходы")
        print("3. Стоп программы")
        choice = input("Предлагаемые действия (1/2/3): ")

        if choice == '1':
            try:
                amount = float(input("Сумма расходов: "))
                if amount < 0:
                    print("Затраты должны быть больше 0")
                else:
                    change_total_expense(amount)
                    print(f"Добавление расходов: {amount:.2f}")
            except ValueError:
                print("Нужно правильное число.")

        elif choice == '2':
            print(f"Общие затраты: {get_expense():.2f}")

        elif choice == '3':
            print("Стоп")
            break

        else:
            print("Давайте попробуем ещё раз")

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        # Сбросим общую сумму перед каждым тестом
        global total_expense
        total_expense = 0.0

    def test_change_total_expense(self):
        change_total_expense(100.0)
        self.assertEqual(get_expense(), 100.0)

        change_total_expense(50.0)
        self.assertEqual(get_expense(), 150.0)

        change_total_expense(-30.0)
        self.assertEqual(get_expense(), 120.0)

    def test_get_expense(self):
        self.assertEqual(get_expense(), 0.0)
        change_total_expense(200.0)
        self.assertEqual(get_expense(), 200.0)

if __name__ == '__main__':
    unittest.main()
