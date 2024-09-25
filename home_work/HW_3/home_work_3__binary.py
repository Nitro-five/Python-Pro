class BinaryNumber:
    def __init__(self, binary_str):
        if not all(bit in '01' for bit in binary_str):
            raise ValueError("Binary number must only contain 0s and 1s.")
        self.binary_str = binary_str

    def __and__(self, other):
        return self._binary_operation(other, lambda a, b: '1' if a == '1' and b == '1' else '0')

    def __or__(self, other):
        return self._binary_operation(other, lambda a, b: '1' if a == '1' or b == '1' else '0')

    def __xor__(self, other):
        return self._binary_operation(other, lambda a, b: '1' if a != b else '0')

    def __invert__(self):
        return BinaryNumber(''.join('1' if bit == '0' else '0' for bit in self.binary_str))

    def _binary_operation(self, other, operation):
        if isinstance(other, BinaryNumber):
            max_length = max(len(self.binary_str), len(other.binary_str))
            # print('Max_lenght:',max_length)
            a = self.binary_str.zfill(max_length)
            b = other.binary_str.zfill(max_length)
            # print('a,b:',a,b)
            result = ''.join(operation(a_bit, b_bit) for a_bit, b_bit in zip(a, b))
            return BinaryNumber(result)
        return NotImplemented

    def __repr__(self):
        return f"BinaryNumber('{self.binary_str}')"

    def __str__(self):
        return self.binary_str



def test_binary_operations():
    a = BinaryNumber("1100")  # 12
    b = BinaryNumber("1010")  # 10

    print(a,b)
    assert str(a & b) == "1000", "Ошибка: неверный результат AND"
    assert str(a | b) == "1110", "Ошибка: неверный результат OR"
    assert str(a ^ b) == "0110", "Ошибка: неверный результат XOR"
    assert str(~a) == "0011", "Ошибка: неверный результат NOT"

    print("тесты пройдены")

if __name__ == "__main__":
    test_binary_operations()
