# Завдання 6: Калькулятор з використанням замикань

def create_calculato(operator):
    def add(x,y):
        return x+y
    def minus(x,y):
        return x-y
    def multiple(x,y):
        return x*y
    def division(x,y):
        if y==0:
            raise ValueError ("Деление на 0 недопустимо!")
        else:
            return x/y

    if operator == '+':
        return add
    elif operator == '-':
        return minus
    elif operator == '*':
        return multiple
    elif operator == '/':
        return division
    else:
        raise ValueError(" Неизвестный оператор ")

add_calc = create_calculato('+')
minus_calc = create_calculato('-')
mult_calc = create_calculato('*')
div_calc = create_calculato('/')

print(f"сложение {add_calc(9, 8)}")
print(f'Вычетание {mult_calc(5,4)}')
print(f'Умножение {mult_calc(3,12)}')
print(f'Деление {div_calc(25,5)}')
#print(f'Деление на 0 {div_calc(1,0)}')