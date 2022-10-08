# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей (2,3,5,7,11,13,17...)числа N .


def prime_factors(x):
   i = 2
   lst = []
   while i * i <= x:
       while x % i == 0:
           lst.append(i)
           x = x / i
       i = i + 1
   if x > 1:
       lst.append(int(x))
   return lst


n = int(input('Введите натуральное число:= '))
print(prime_factors(n))