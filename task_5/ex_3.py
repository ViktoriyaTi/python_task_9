# ИГРА_КРЕСТИКИ НОЛИКИ
# ДВА игрока

information = print('\nИГРА : КРЕСТИКИ НОЛИКИ\n  ')
display = list(range(1,10))
victory = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]


def print_on_display():
    print(display[0], end ='  ')
    print(display[1], end ='  ')
    print(f'{display[2]}\n')

    print(display[3], end ='  ')
    print(display[4], end ='  ')
    print(f'{display[5]}\n')

    print(display[6], end ='  ')
    print(display[7], end ='  ')
    print(display[8])


def step_display(step,symbol):
    i = display.index(step)
    display[i] = symbol


def get_result (k):
    win = ''
    if k >= 3 and k < 9:
        for i in victory:
            if display[i[0]] == 'X' and display[i[1]] == 'X' and display[i[2]] == 'X':
                win = 'X'
            if display[i[0]] == 'O' and display[i[1]] == 'O' and display[i[2]] == 'O':
                win = 'O'
    elif k == 9:
        win = 'НИЧЬЯ'
    else: win = ''
    return win


def count_use_function(function):
    global counter
    counter += 1
    return counter


game_over = False
player1 = True
counter = 0
while game_over == False:
    print_on_display()
    if player1 == True:
        symbol = 'X'
        step = int(input('\nПервый игрок, введите число вместо которого поставим крестик? '))
    else:
        symbol = 'O'
        step = int(input('\nВторой игрок, введите число вместо которого поставим нолик? '))
    step_display(step,symbol)
    k = count_use_function(step_display)
    win = get_result(k)
    if win != '' and win != 'НИЧЬЯ':
        game_over = True
        print_on_display()
        print(f' Игрок, который ходил "{win}" -  ПОБЕДИТЕЛЬ!!!')
    elif win == 'НИЧЬЯ':
        game_over = True
        print_on_display()
        print('НИЧЬЯ')   
    else:
        game_over = False
    player1 = not (player1)





