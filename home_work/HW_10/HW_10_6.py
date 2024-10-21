import random
import concurrent.futures
import time

class Organism:
    def __init__(self, id):
        self.id = id
        self.nutrition = random.uniform(0.5, 2.0)
        self.reproduction = random.uniform(0.5, 2.0)

    def __repr__(self):
        return f"Организм {self.id}: питание = {self.nutrition:.2f}, размножение = {self.reproduction:.2f}"

def process_organism(organism):
    # Имитируем время обработки
    time.sleep(random.uniform(0.1, 0.5))
    # Здесь можно добавить логику обработки организма
    return organism

def evolve_population(population):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Обрабатываем каждого организма в отдельном процессе
        results = list(executor.map(process_organism, population))
    return results

# Начальная популяция
population = [Organism(i) for i in range(10)]
print("Начальная популяция:")
for org in population:
    print(org)

# Эволюция
population = evolve_population(population)
print("\nОбработанная популяция:")
for org in population:
    print(org)
