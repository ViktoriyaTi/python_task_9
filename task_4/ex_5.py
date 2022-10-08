# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример:
# файл1: 2x^2 + 7x + 5
# файл2: 4x^2 + 3x + 9
# результат: 6x^2 + 10x + 14

with open('file_task_4_ex_4', 'r') as file_1:
    data = file_1.readline()
    #print(data)
lst = data.split()          
ist=[int(i) for i in lst]
#print(ist)
with open('file_task_4_ex_4_2', 'r') as file_2:
    data1 = file_2.readline()
    #print(data1)
lst1 = data1.split()        
ist1=[int(i) for i in lst1]
#print(ist1)

res= list(map(sum, zip(ist,ist1)))
print(res)

with open('file_task_4_rezult','w') as rezult:
    rezult.write(f'{res[0]}x^{2} + {res[1]}x + {res[2]} = 0')