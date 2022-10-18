def view_data(information):
    print(information)


def choice_convert():
    user_choice = int(input('Для отображения телефонного справочника в формате txt введите 1, в формате csv введите - 2,\n3 - для экспорта в csv файл из txt, \n4 - для экспорта в txt файл из csv\n'))
    if 4 < user_choice or user_choice < 1:
        input_error()
    return user_choice


def input_error():
    print('ОШИБКА! Вы ввели некорретное значение. Необходимо вводить число 1 или 2 или 3 или 4! Попробуйте заново')
