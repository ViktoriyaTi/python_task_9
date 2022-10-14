# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел. 
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. 
# Ввод чисел продолжается до ввода пустой строки.
# Пример: 36 12 144 18 - 6

from math import gcd

lst = []
line = input('Введите список натуральных чисел через ENTER,\nввод чисел продолжается до ввода пустой строки: \n')
while line:
    lst.append(line)
    line = input()
print(lst)
lst = list(map(int, lst))
print(lst)
sp = []
for i in range(0,len(lst)-1):
    a = gcd(lst[i],lst[i+1])
    sp.append(a)
    for j in range(0,len(sp)-1):
        res = gcd(sp[j],sp[j+1])
print(res)
