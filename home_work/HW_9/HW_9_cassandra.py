# Отвечает за подключение к кластеру Cassandra
from cassandra.cluster import Cluster
# Используется для выполнения запросов к Cassandra.
from cassandra.query import SimpleStatement
# Для создания уникальных идентификаторов (UUID)
import uuid
import datetime

# Подключение к кластеру Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('your_keyspace')


# 1. Create: Добавление нового лог-записи
def create_event_log(user_id, event_type, metadata):
    # Генерация уникального идентификатора события
    event_id = uuid.uuid4()
    # Текущая дата и время
    timestamp = datetime.datetime.now()
    query = f"""
    INSERT INTO event_logs (event_id, user_id, event_type, timestamp, metadata)
    VALUES (%s, %s, %s, %s, %s)
    """
    session.execute(query, (event_id, user_id, event_type, timestamp, metadata))


# 2. Read: Получение всех событий определенного типа за последние 24 часа
def read_event_logs(event_type):
    # Дата 24 часа назад
    timestamp_24h_ago = datetime.datetime.now() - datetime.timedelta(days=1)
    query = f"""
    SELECT * FROM event_logs
    WHERE event_type = %s AND timestamp >= %s
    """
    statement = SimpleStatement(query)
    # Выполнение запроса
    rows = session.execute(statement, (event_type, timestamp_24h_ago))
    return rows


# 3. Update: Обновление метаданных
def update_event_log(event_id, event_type, timestamp, metadata):
    query = f"""
    UPDATE event_logs 
    SET metadata = %s 
    WHERE event_type = %s AND timestamp = %s AND event_id = %s
    """
    # Выполнение обновления
    session.execute(query, (metadata, event_type, timestamp, event_id))


# 4. Delete: Удаление старых событий (старше 7 дней)
def delete_old_events(event_type):
    timestamp_7_days_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    query = f"""
    SELECT event_id, timestamp FROM event_logs 
    WHERE event_type = %s AND timestamp < %s
    """
    # Получаем события для удаления
    rows = session.execute(query, (event_type, timestamp_7_days_ago))

    for row in rows:
        # Удаляем каждое событие по его ключам
        delete_query = f"""
        DELETE FROM event_logs 
        WHERE event_type = %s AND timestamp = %s AND event_id = %s
        """
        # Выполнение удаления
        session.execute(delete_query, (row.event_type, row.timestamp, row.event_id))


# Примеры использования
if __name__ == "__main__":
    # Добавление нового лог-записи
    create_event_log(uuid.uuid4(), 'login', '{"info": "User logged in"}')

    print("Event logs for 'login':")
    rows = read_event_logs('login')
    for row in rows:
        # Вывод каждой записи
        print(row)

        # Обновление метаданных для первого события
        update_event_log(row.event_id, row.event_type, row.timestamp, '{"info": "Updated info"}')

    # Удаление старых событий и передаем event_type
    delete_old_events('login')

# Закрытие соединения
cluster.shutdown()
