class MyCollection:
    def __init__(self, items):
        self.items = items


    def __len__(self):
        count = 0
        for i in self.items:
            count += 1
        return count


    def __getitem__(self, index):
        return self.items[index]


    def __iter__(self):
        return iter(self.items)


def my_len(collection):
    return collection.__len__()


def my_sum(collection):
    total = 0
    for item in collection:
        total += item
    return total


def my_min(collection):
    if not collection:
        raise ValueError("my_min() arg empty ")
    minimum = collection[0]
    for item in collection:
        if item < minimum:
            minimum = item
    return minimum



def test_my_len():
    collection = MyCollection([1, 2, 3, 4])
    assert my_len(collection) == 4, "my_len failed"


def test_my_sum():
    collection = MyCollection([1, 2, 3, 4])
    assert my_sum(collection) == 10, "my_sum failed"


def test_my_min():
    collection = MyCollection([1, 2, 3, 4])
    assert my_min(collection) == 1, "my_min failed"

    collection_empty = MyCollection([])
    try:
        my_min(collection_empty)
        assert False, "my_min did`t raise ValueError for empty collection"
    except ValueError:
        pass


if __name__ == "__main__":
    test_my_len()
    test_my_sum()
    test_my_min()
    print("Tests passed!")
