import unittest


class StringHandling:
    def reverse_string(self, s: str) -> str:
        return s[::-1]

    def capitalize_string(self, s: str) -> str:
        return s.capitalize()

    def count_vowels(self, s: str) -> int:
        # Определяем набор голосных букв
        vowels = 'aeiouAEIOU'
        # Подсчитываем количество голосных в строке
        vowel_count = sum(1 for char in s if char in vowels)
        return vowel_count


# Тест
class TestStringHandling(unittest.TestCase):

    def setUp(self):
        """
        Внутри метода setUp создается экземпляр класса StringHandling и сохраняется в атрибуте self.handler.
        Это позволяет использовать self.handler в каждом тестовом методе, чтобы вызывать методы
        этого класса без необходимости повторно создавать его.
        """
        self.handler = StringHandling()

    @unittest.skip("Skipping reverse_string test for empty string.")
    def test_reverse_string_empty(self):
        """
        Тестирование метода reverse_string с пустой строкой.
        Пропускается.
        """
        self.assertEqual(self.handler.reverse_string(""), "")

    def test_reverse_string(self):
        """
        Тестирование метода reverse_string
        """
        self.assertEqual(self.handler.reverse_string("hello"), "olleh")
        self.assertEqual(self.handler.reverse_string("123"), "321")
        self.assertEqual(self.handler.reverse_string("!@#"), "#@!")

    def test_capitalize_string(self):
        """
        Тестирование метода test_capitalize_string
        """
        self.assertEqual(self.handler.capitalize_string("hello"), "Hello")
        self.assertEqual(self.handler.capitalize_string("world"), "World")
        self.assertEqual(self.handler.capitalize_string("123abc"), "123abc")
        self.assertEqual(self.handler.capitalize_string(""), "")

    def test_count_vowels(self):
        """
        Тестирование метода count_vowels
        """
        self.assertEqual(self.handler.count_vowels("hello"), 2)
        self.assertEqual(self.handler.count_vowels("world"), 1)
        self.assertEqual(self.handler.count_vowels("123"), 0)
        self.assertEqual(self.handler.count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(self.handler.count_vowels("!@#$%^&*()"), 0)


if __name__ == "__main__":
    handler = StringHandling()
    print(handler.reverse_string("hello"))
    print(handler.capitalize_string("hello"))
    print(handler.count_vowels("hello"))

    unittest.main()
