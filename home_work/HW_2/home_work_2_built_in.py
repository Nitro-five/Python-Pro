# Завдання 1: Built-in область видимості (демонстрація використання вбудованих функцій та їх перекриття локальними функціями).
def my_sum():
    print('This is my custom sum function!')



lst_num = [1, 2, 3, 4, 5]

print("Сумма:", sum(lst_num))

my_sum()
print("Сумма:", sum(lst_num))


# Ответы на вопросы :
# 1)локальная функция перекрывает встроенную в текущей области видимости .
# 2)Импортировать встроенную функцию из модуля "builtin"