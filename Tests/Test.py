# Исключения

number_1 = 10
number_2 = '11'
# print(number_2+number_1)
try:
    print(number_2+number_1)
    prnt(number_1)

except TypeError as error:
    print('Переменные должны быть числами')
    print(error)
except NameError as error:
    print(error)
finally:
    print(number_2)