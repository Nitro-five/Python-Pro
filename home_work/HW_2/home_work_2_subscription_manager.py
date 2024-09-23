# Завдання 2: Менеджер підписки на розсилку
subscribers = []

def subscribe(name):
    subscribers.append(name)

    def confirm_subscription():
        return f"Новый подписчик {name}"

    print(confirm_subscription())

def unsubscribe(name):
    if name in subscribers:
        subscribers.remove(name)
        return (f"Подписчик отписан {name}")
    else:
        return (f"Подписчик отсутствует  {name}")

subscribe("Олена")
subscribe("Ігор")
print(subscribers)  # ['Олена', 'Ігор']
print(unsubscribe("Ігор"))  # 'Ігор успішно відписаний'
print(subscribers)  # ['Олена']
