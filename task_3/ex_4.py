# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 	45 -> 101101, 	3 -> 11, 	2 -> 10


def decimal_to_binary(value):
    remainder = ''
    while value > 0:
        remainder = str(value % 2) + remainder
        value//=2
    return(remainder)    


number = int(input('Введите целое число: = '))
print(decimal_to_binary(number))