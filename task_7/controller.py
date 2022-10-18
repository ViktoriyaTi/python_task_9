from model import import_data
from model import export_data_to_csv
from model import export_data_to_txt
from view import view_data
from view import choice_convert 

def button_click():
    user_number = choice_convert()
    if user_number == 1:
        view_data(import_data("phone_directory.txt"))
    elif user_number == 2:
        view_data(import_data("csv_phone_directory.csv"))
    elif user_number == 3:
        export_data_to_csv("phone_directory.txt")
    else:
        export_data_to_txt("csv_phone_directory.csv")


