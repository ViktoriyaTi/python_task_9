# ИГРА_КОНФЕТЫ
# БОТ
from random import randint


def input_value(user):
    number = int(input(f'{user},введите количество конфет, которое возьмете от 1 до 28: '))
    while number <= 0 or number >= max_sweet_at_time + 1:
        number = int(input(f' {user}, ОШИБКА!!! Введите корректное количество конфет в диапозоне от 1 до 28 включительно: '))
    return number
    

information = print('\nПравила игры:\n На столе лежит 2021 конфета.\n Играют два игрока (БОТ против человека) делая ход друг после друга.\n' 
' Первый ход определяется жеребьёвкой.\n За один ход можно забрать не более чем 28 конфет.\n'
' Все конфеты оппонента достаются сделавшему последний ход.\n')
total_sweets = 2021
max_sweet_at_time = 28 
player_1 = input("Введите имя игрока: ").capitalize()
player_2 = 'Бот'
choice_step = randint(0,1)
if choice_step == 0:
    print(f'По жребию первым ходит игрок {player_1}')
else:
    print(f'По жребию первым ходит игрок {player_2}')
while total_sweets > max_sweet_at_time:
    if choice_step == 0:
        sweet_1 = input_value(player_1)
        total_sweets -= sweet_1
        choice_step = 1
        print(f'Походил игрок {player_1} забрал(а) {sweet_1} конфет(ы), осталось на столе всего= {total_sweets}')
    else:
        sweet_2 = randint(1,max_sweet_at_time)
        total_sweets -= sweet_2
        print(f'Походил игрок {player_2} забрал(а) {sweet_2} конфет(ы), осталось на столе всего= {total_sweets}')
        choice_step = 0
if choice_step == 0:  
    print(f'ПОЗДРАВЛЯЕМ! Выиграл игрок {player_1}, к сожалению, проиграл игрок {player_2}')
else:
    print(f'ПОЗДРАВЛЯЕМ! Выиграл {player_2}, к сожалению, проиграл игрок {player_1}')


# ИГРА_КОНФЕТЫ
# УМНЫЙ БОТ


# def input_value(user):
#     number = int(input(f'{user},введите количество конфет, которое возьмете от 1 до 28: '))
#     while number <= 0 or number >= max_sweet_at_time + 1:
#         number = int(input(f' {user}, ОШИБКА!!! Введите корректное количество конфет в диапозоне от 1 до 28 включительно: '))
#     return number


# information = print('\nПравила игры:\n На столе лежит 2021 конфета.\n Играют два игрока ("умный" БОТ против человека) делая ход друг после друга.\n' 
# ' Первый ход определяется жеребьёвкой.\n За один ход можно забрать не более чем 28 конфет.\n'
# ' Все конфеты оппонента достаются сделавшему последний ход.\n')
# total_sweets = 2021
# max_sweet_at_time = 28 
# player_1 = input("Введите имя игрока: ").capitalize()
# player_2 = 'Бот'
# choice_step = randint(0,1)
# if choice_step == 0:
#     print(f'По жребию первым ходит игрок {player_1}')
# else:
#     print(f'По жребию первым ходит игрок {player_2}')
# while total_sweets > max_sweet_at_time:
#     if choice_step == 0:
#         sweet_1 = input_value(player_1)
#         total_sweets -= sweet_1
#         choice_step = 1
#         print(f'Походил игрок {player_1} забрал(а) {sweet_1} конфет(ы), осталось на столе всего= {total_sweets}')
#     else:
#         if total_sweets % 29 > 0:
#            sweet_2 = total_sweets % 29
#            total_sweets -= sweet_2
#            print(f'Походил игрок {player_2} забрал(а) {sweet_2} конфет(ы), осталось на столе всего= {total_sweets}')
#            choice_step = 0
#         else: 
#             sweet_2 = randint(1,max_sweet_at_time)   
# if choice_step == 0:  
#     print(f'ПОЗДРАВЛЯЕМ! Выиграл игрок {player_1}, к сожалению, проиграл игрок {player_2}')
# else:
#     print(f'ПОЗДРАВЛЯЕМ! Выиграл {player_2}, к сожалению, проиграл игрок {player_1}')