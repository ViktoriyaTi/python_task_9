# Реализуйте алгоритм перемешивания списка 
# (метод random.shuffle использовать нельзя, но другие методы из библиотеки random - можно)

import random

first_list = [1, 2, 3, 4, 5]
print ("Первичный список : " + str(first_list))
changed_list = random.sample(first_list, len(first_list))
print ("Перемешанный список : " +  str(changed_list))


# from random import *
# originallist=list('12345')
# print(originallist)
# p = ''.join([choice(originallist) for x in range(len(originallist))])
# print(p) #Получается рандомное с повторением