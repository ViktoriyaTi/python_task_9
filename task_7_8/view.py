def view_data(information):
    print(information)


def choice_convert():
    user_choice = int(input('Для отображения телефонного справочника:\n\
    в формате txt введите 1,\n\
    в формате csv введите - 2,\n\
    3 - для внесения новой информации о контакте в файл csv,\n\
    4 - для удаления контакной информации из csv файла,\n\
    5 - для обновления номера телефона,\n\
    6 - для экспорта в txt файл из csv,\n\
    7 - для экспорта в csv файл из txt.\n'))
    if 7 < user_choice or user_choice < 1:
        input_error()
    return user_choice


def input_error():
    print('ОШИБКА! Вы ввели некорретное значение. Необходимо вводить число в диапозоне от 1 до 7! Попробуйте заново.')


def add_new_information():
    print('Введите фамилию, имя и контактный номер телефона через пробел: ')
    new_information = input().split()
    return new_information


def delete_information():
    user_index = int(input(
        'Введите порядковый номер контактного лица, чью запись необходимо удалить: '))
    return (user_index - 1)


def change_phone():
    number = int(input(
        'Введите порядковый номер контактного лица для внесения изменений в его контактный номер: '))
    phone_number = int(
        input('Введите новый номер контактного телефона (только числовые значения): '))
    number = number - 1
    return number, phone_number
