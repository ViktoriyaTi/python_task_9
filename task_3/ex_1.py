# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def amount_in_odd_positions (sp):
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            sum = sum + lst[i]
    return sum


lst = [2, 3, 5, 9, 3]
print(amount_in_odd_positions(lst))
