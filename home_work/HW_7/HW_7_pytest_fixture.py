import pytest


class UserManager:
    """
    Класс для управления пользователями.
    """

    def __init__(self):
        # Инициализирует пустой словарь для хранения пользователей
        self.users = {}

    def add_user(self, name: str, age: int):
        """Добавляет пользователя с именем и возрастом."""
        self.users[name] = age

    def remove_user(self, name: str):
        """Удаляет пользователя по имени."""
        if name in self.users:
            del self.users[name]

    def get_all_users(self) -> list:
        """Возвращает список всех пользователей."""
        return list(self.users.items())


"""
Декоратор из библиотеки pytest, который позволяет создавать фикстуры
"""


@pytest.fixture
def user_manager():
    """Фикстура для предварительной настройки UserManager с несколькими пользователями."""
    um = UserManager()
    um.add_user("Alice", 30)  # Добавляем пользователя Alice
    um.add_user("Bob", 25)  # Добавляем пользователя Bob
    return um


def test_add_user(user_manager):
    """Тестирование метода add_user."""
    # Добавляем нового пользователя Charlie
    user_manager.add_user("Charlie", 28)
    # Проверяем, что пользователь добавлен
    assert ("Charlie", 28) in user_manager.get_all_users()


def test_remove_user(user_manager):
    """Тестирование метода remove_user."""
    # Удаляем пользователя Alice
    user_manager.remove_user("Alice")
    # Проверяем, что пользователь удален
    assert ("Alice", 30) not in user_manager.get_all_users()


def test_get_all_users(user_manager):
    """Тестирование метода get_all_users."""
    users = user_manager.get_all_users()
    assert len(users) == 2
    assert ("Alice", 30) in users
    assert ("Bob", 25) in users


def test_remove_user_skip(user_manager):
    """Тест, который пропускается, если меньше трех пользователей."""
    user_manager.remove_user("Alice")
    user_manager.remove_user("Bob")

    # Если осталось меньше трех пользователей, пропускаем тест
    if len(user_manager.get_all_users()) < 3:
        pytest.skip("Пропускаем тест, так как меньше трех пользователей.")
