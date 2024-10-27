import re
import string

def check_password(password):
    """
    Проверяет, является ли пароль надежным.

    Надежный пароль должен соответствовать следующим критериям:
    - Длина пароля не менее 8 символов.
    - Содержит хотя бы одну цифру.
    - Содержит хотя бы одну маленькую букву.
    - Содержит хотя бы одну большую букву.
    - Содержит хотя бы один специальный символ (например, @, #, $, %, & и т. д.).

    Аргументы:
    password (str): Пароль, который нужно проверить.

    Возвращает:
    bool: True, если пароль надежный, иначе False.
    """
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not any(char in string.punctuation for char in password):
        return False

    return True

# Список паролей для проверки
passwords = [
    "Password1@",
    "pass",
    "Pass123",
    "Password@",
    "P@ssword1"
]

# Проверка паролей и вывод результата
for i in passwords:
    print(f"{i}: {'Прошёл проверку' if check_password(i) else 'Не прошёл'}")
