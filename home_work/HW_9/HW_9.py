from pymongo import MongoClient
from datetime import datetime, timedelta

# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27018/')
db = client['online_store']

# Создание коллекций
products_collection = db['products']
orders_collection = db['orders']

# 1. Добавление продуктов
def add_products():
    """Добавляет случайные продукты в коллекцию продуктов."""
    products_collection.insert_many([
        {"name": "Игровая клавиатура", "price": 900, "category": "Компьютерные аксессуары", "stock": 5},
        {"name": "Гарнитура", "price": 150, "category": "Аудио", "stock": 10},
        {"name": "Смарт-часы", "price": 250, "category": "Электроника", "stock": 8},
        {"name": "Электронная книга", "price": 200, "category": "Литература", "stock": 12},
        {"name": "Проектор", "price": 1200, "category": "Электроника", "stock": 4}
    ])
    print("Продукты добавлены.")


# 2. Добавление заказов
def add_orders():
    """Добавляет случайные заказы в коллекцию заказов."""
    orders_collection.insert_many([
        {
            "orderNumber": 1,
            "client": "Алексей",
            "products": [{"productId": "1", "quantity": 1}],
            "totalAmount": 900,
            "orderDate": datetime.now()
        },
        {
            "orderNumber": 2,
            "client": "Елена",
            "products": [{"productId": "2", "quantity": 1}],
            "totalAmount": 150,
            "orderDate": datetime.now() - timedelta(days=5)
        },
        {
            "orderNumber": 3,
            "client": "Станислав",
            "products": [{"productId": "3", "quantity": 1}],
            "totalAmount": 250,
            "orderDate": datetime.now() - timedelta(days=10)
        },
        {
            "orderNumber": 4,
            "client": "Кристина",
            "products": [{"productId": "4", "quantity": 1}],
            "totalAmount": 200,
            "orderDate": datetime.now() - timedelta(days=2)
        }
    ])
    print("Заказы добавлены.")


# 3. Извлечение заказов за последние 30 дней
def get_recent_orders():
    """Извлекает и выводит заказы, сделанные за последние 30 дней."""
    thirty_days_ago = datetime.now() - timedelta(days=30)
    recent_orders = orders_collection.find({"orderDate": {"$gte": thirty_days_ago}})

    print("Заказы за последние 30 дней:")
    for order in recent_orders:
        print(order)

# 4. Обновление количества продукта на складе
def update_product_stock(product_name):
    """Обновляет количество указанного продукта на складе."""
    products_collection.update_one(
        {"name": product_name},
        {"$inc": {"stock": -1}}  # Уменьшить количество на 1
    )
    print(f"Количество продукта '{product_name}' обновлено.")

# 5. Удаление продуктов, которые больше не доступны
def delete_unavailable_products():
    """Удаляет продукты, которые больше не доступны (с нулевым запасом)."""
    products_collection.delete_many({"stock": 0})
    print("Продукты, которые больше не доступны, удалены.")

# 6. Подсчет общего количества проданных продуктов за определенный период
def count_sold_products():
    """Подсчитывает общее количество проданных продуктов за весь период."""
    pipeline = [
        {"$unwind": "$products"},
        {"$group": {"_id": "$products.productId", "totalSold": {"$sum": "$products.quantity"}}}
    ]
    sold_products = orders_collection.aggregate(pipeline)

    print("Общее количество проданных продуктов:")
    for product in sold_products:
        print(product)

# 7. Подсчет общей суммы всех заказов клиента
def total_spent_by_client(client_name):
    """Подсчитывает общую сумму всех заказов указанного клиента."""
    pipeline = [
        {"$match": {"client": client_name}},
        {"$group": {"_id": None, "totalSpent": {"$sum": "$totalAmount"}}}
    ]
    total_spent = list(orders_collection.aggregate(pipeline))

    if total_spent:
        print(f"Общая сумма всех заказов клиента '{client_name}': {total_spent[0]['totalSpent']}")
    else:
        print(f"Клиент '{client_name}' не имеет заказов.")

# 8. Создание индекса для поля 'category'
def create_index():
    """Создает индекс для поля 'category' в коллекции продуктов."""
    products_collection.create_index([("category", 1)])
    print("Индекс для поля 'category' создан.")

# Вызов функций
if __name__ == "__main__":
    add_products()
    add_orders()
    get_recent_orders()
    update_product_stock("Игровая клавиатура")
    delete_unavailable_products()
    count_sold_products()
    total_spent_by_client("Алексей")
    create_index()
