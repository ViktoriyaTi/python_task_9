# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; 	[2, 3, 5, 6] => [12, 15]


def product_of_number(sp):
     res = []
     while len(sp) > 1:
         res.append(sp[0]*sp[-1])
         del sp[0]
         del sp[-1] 
     if len(sp) == 1: 
        res.append(sp[0]**2)       
     return res


lst = list(map(int, input('Введите числа через пробел: ').split()))
print(product_of_number(lst))





