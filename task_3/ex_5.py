# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


def fibbonacci_positiv(number):
    if number == 0:
        return 0
    elif number in [1,2]:
        return 1
    else:
        return fibbonacci_positiv(number-1) + fibbonacci_positiv(number-2) 


def fibbonacci_negative(number):
    if number==-1:
        return 1
    elif number==-2:
        return -1
    else:
        return fibbonacci_negative(number+2) - fibbonacci_negative(number+1) 


n=int(input('Введите целое число для создания списка чисел Фибоначчи:= '))    
lst1 = []
for i in range(0,n):
    lst1.append(fibbonacci_positiv(i))
lst2 = []
for i in range(-(n),0):
    lst2.append(fibbonacci_negative(i))
print(lst2+lst1)

