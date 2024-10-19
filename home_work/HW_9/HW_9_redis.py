import redis
import time


class UserSessionManager:
    """
    Менеджер сессий пользователей, использующий Redis для хранения и управления сессиями.

    Атрибуты:
        redis_client (redis.StrictRedis): Клиент для взаимодействия с Redis.

    Методы:
        create_session(user_id, session_token):
            Создает новую сессию для указанного пользователя и сохраняет её в Redis.

        read_session(user_id):
            Извлекает данные сессии для указанного пользователя из Redis.

        update_session(user_id):
            Обновляет время последней активности сессии для указанного пользователя.

        delete_session(user_id):
            Удаляет сессию указанного пользователя из Redis.
    """

    def __init__(self, redis_host='localhost', redis_port=6379):
        """
        Инициализирует объект UserSessionManager.

        Аргументы:
            redis_host (str): Хост Redis (по умолчанию 'localhost').
            redis_port (int): Порт Redis (по умолчанию 6379).
        """
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

    def create_session(self, user_id, session_token):
        """
        Создает новую сессию для указанного пользователя.

        Аргументы:
            user_id (str): Уникальный идентификатор пользователя.
            session_token (str): Токен сессии для аутентификации.

        Возвращает:
            None
        """
        login_time = time.time()
        session_data = {
            'session_token': session_token,
            'login_time': login_time
        }
        # Сохранение данных в Redis
        self.redis_client.hmset(f'session:{user_id}', session_data)
        # Устанавливаем TTL на 30 минут (1800 секунд)
        self.redis_client.expire(f'session:{user_id}', 1800)
        print(f'Сессия создана для пользователя с id: {user_id}')

    def read_session(self, user_id):
        """
        Извлекает данные сессии для указанного пользователя.

        Аргументы:
            user_id (str): Уникальный идентификатор пользователя.

        Возвращает:
            dict или None: Возвращает словарь с данными сессии или None, если сессия не найдена.
        """
        session_data = self.redis_client.hgetall(f'session:{user_id}')
        if session_data:
            return {
                'user_id': user_id,
                'session_token': session_data['session_token'],
                'login_time': session_data['login_time']
            }
        else:
            return None

    def update_session(self, user_id):
        """
        Обновляет время последней активности сессии для указанного пользователя.

        Аргументы:
            user_id (str): Уникальный идентификатор пользователя.

        Возвращает:
            None
        """
        current_time = time.time()
        self.redis_client.hset(f'session:{user_id}', 'login_time', current_time)
        # Обновляем TTL при каждом обновлении сессии
        self.redis_client.expire(f'session:{user_id}', 1800)
        print(f'Сессия пользователя {user_id} была обновлена')

    def delete_session(self, user_id):
        """
        Удаляет сессию указанного пользователя из Redis.

        Аргументы:
            user_id (str): Уникальный идентификатор пользователя.

        Возвращает:
            None
        """
        self.redis_client.delete(f'session:{user_id}')
        print(f'Сессия была удалена для пользователя {user_id}')


# Тест
if __name__ == "__main__":
    session_manager = UserSessionManager()
    session_manager.create_session('user1234', 'token_xyz')
    session_info = session_manager.read_session('user1234')
    print(session_info)
    session_manager.update_session('user1234')
    session_manager.delete_session('user1234')
