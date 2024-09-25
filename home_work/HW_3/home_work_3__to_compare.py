class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented


    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age
        return NotImplemented


    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented


    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


def main():

    people = [
        Person("Max", 23),
        Person("Bob", 25),
        Person("Alex", 18),
        Person("Vlad", 21)
    ]

    print("До сортировки :")
    for person in people:
        print(person)

    sorted_people = sorted(people)

    print("\n После:")
    for person in sorted_people:
        print(person)

if __name__ == "__main__":
    main()
