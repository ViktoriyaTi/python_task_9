# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def difference_between_max_and_min_fractional_part (lst):
    lst2 =[]
    for i in lst:
        lst2.append(i - int(i))
    lst2.sort()
    result = lst2[-1] - lst2[0]
    print(f'Разница между max и min значением дробной части элементов:= {result}')


lst = list(map(float, input('Введите список из вещественных чисел через пробел: ').split()))
difference_between_max_and_min_fractional_part(lst)
