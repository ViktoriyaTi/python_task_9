# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2x² + 4x + 5 = 0

from random import randint
k = 2
a = randint(0,100)
b = randint(0,100)
c = randint(0,100)
lst = f'{a} {b} {c}'

a1 = randint(0,100)
b1 = randint(0,100)
c1 = randint(0,100)
lst1 = f'{a1} {b1} {c1}'

with open('file_task_4_ex_4','w') as data:
    data.write(f'{lst}\n')
    data.write(f'{a}x^{k} + {b}x + {c} = 0')
with open('file_task_4_ex_4_2','w') as data:
    data.write(f'{lst1}\n')
    data.write(f'{a1}x^{k} + {b1}x + {c1} = 0')    
    