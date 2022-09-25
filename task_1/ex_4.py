# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

print ('Введите номер четверти = ')
quoter_number = int(input())
if quoter_number > 4 or quoter_number < 1:
    print('Ошибка, вы ввели число не из диапозона возможных значений номера четверти')
elif quoter_number == 1:
    print(f'Диапозон возможных координат точек в {quoter_number} четверти = X > 0, Y > 0')
elif quoter_number == 2:
    print(f'Диапозон возможных координат точек в {quoter_number} четверти = X < 0, Y > 0')
elif quoter_number == 3:
    print(f'Диапозон возможных координат точек в {quoter_number} четверти = X < 0, Y < 0')
else:
    print(f'Диапозон возможных координат точек в {quoter_number} четверти = X > 0, Y < 0')
    