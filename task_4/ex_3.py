# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int,input('Введите последовательность чисел: ').split()))
sp=[i for i in lst if lst.count(i)== 1]
print(sp)


#Другой вариант записи
# lst = list(map(int,input('Введите последовательность чисел: ').split()))
# sp=[]
# for i in lst:
#     if lst.count(i)== 1:
#         sp.append(i)
# print(sp)        