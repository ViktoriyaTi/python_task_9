from model import import_data
from model import export_data_to_csv
from model import export_data_to_txt
from model import add_information as add
from model import del_information as delete
from model import update_information as update
from view import view_data
from view import choice_convert
from view import add_new_information
from view import delete_information
from view import change_phone


def button_click():
    user_number = choice_convert()
    if user_number == 1:
        view_data(import_data("phone_directory.txt"))
    elif user_number == 2:
        view_data(import_data("csv_phone_directory.csv"))
    elif user_number == 3:
        new_info = add_new_information()
        add("csv_phone_directory.csv", new_info)
    elif user_number == 4:
        index = delete_information()
        delete("csv_phone_directory.csv", index)
    elif user_number == 5:
        index, new_phone_number = change_phone()
        update("csv_phone_directory.csv", index, new_phone_number)
    elif user_number == 6:
        export_data_to_txt("csv_phone_directory.csv")
    else:
        export_data_to_csv("phone_directory.txt")
