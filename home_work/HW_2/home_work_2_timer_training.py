# Завдання 4: Таймер для тренування
default_time = 60

def training_session(lap):
    time_lap = default_time

    def time_settings(new_time):
        nonlocal  time_lap
        time_lap = new_time
        print(f"Время раунда изменено на {time_lap} минут.")

    for i in range(1, lap + 1):
        print(f"Раунд {i}: продолжительность {time_lap} минут.")

        if input(f"Изменения для следующего раунду (раунд {i + 1})? (да/нет): ").lower() == "да":
            new_time = int(input("напишите новое время для следующего раунду (в минутах): "))
            time_settings(new_time)

training_session(3)