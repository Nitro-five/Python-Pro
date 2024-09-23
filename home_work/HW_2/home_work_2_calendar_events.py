# Завдання 5: Календар подій

events = []

def events_calendar():
    def new_events(event):
        events.append(event)
        print(f"Добавлен новый эвент '{event}'")

    def delete_event(event):
        if event in events:
            events.remove(event)
            print(f"Удалён эвент '{event}'")
        else:
            print(f"Такого эвента '{event}' не найдено")

    def views(event):
        if events:
            print(f"Эвенты:")

            for event in events:
                print(event)
        else:
            print(f"Нет эвентов")

    return new_events,delete_event,views
new_events,delete_event,views = events_calendar() # распаковка кортежа 

new_events("Отбытие поезда")
new_events("Перелёт")
views(events)
delete_event("Перелёт")
views(events)

