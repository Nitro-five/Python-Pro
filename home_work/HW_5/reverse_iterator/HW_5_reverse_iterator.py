"""
Класс ReverseFileReader реализует итератор для считывания текстового файла в обратном порядке,
пропуская пустые строки.

Атрибуты:
    filename (str): Имя файла, который будет считываться.
    file (file object): Объект файла, открытый для чтения.
    lines (list): Список непустых строк, считанных из файла.
    index (int): Индекс, указывающий на текущую строку для считывания (начинается с последней строки).

Методы:
    __init__(self, filename): Конструктор класса, открывает файл и считывает все непустые строки.
    __iter__(self): Возвращает сам объект, реализующий итерацию.
    __next__(self): Возвращает следующую непустую строку из файла в обратном порядке.
                    При достижении начала файла вызывает StopIteration для завершения итерации при достижении начала файла.
"""


class ReverseFileReader:

    def __init__(self, filename):
        self.file = open(filename, 'r')
        # Считываем строки и фильтруем непустые и пустые
        self.lines = [line.rstrip('\n') for line in self.file if line.strip()]
        self.index = len(self.lines) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            line = self.lines[self.index]
            self.index -= 1
            return line
        else:
            self.file.close()
            raise StopIteration


# Использование
filename = 'Golf R.txt'
for line in ReverseFileReader(filename):
    print(line)
