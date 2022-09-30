# Задайте числами список из N элементов, заполненных из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите целое число: '))
numbers = list(range(-n,n+1))
print(numbers)
x = open('file.txt', 'r')
position1 = int(x.readline())
position2 = int(x.readline(2))
x.close()
product_of_numbers = 1
for i in range(len(numbers)):
    if i ==position1 or i ==position2:
        product_of_numbers *= numbers[i] 
print(product_of_numbers)

