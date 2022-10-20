import csv


def import_data(filename):  # прочитать всю информацию
    with open(filename, 'r', encoding='utf8') as data:
        data = data.read()
    return (data)


def export_data_to_csv(file_name):  # экспорт в csv
    with open(file_name, 'r', encoding='utf8') as infile:
        data = infile.read()
    data = data.replace('\n', ';')
    data = data.replace(';;', '\n')
    out_csv = open('new_csv_phone_directory.csv', 'w', encoding='utf8')
    out_csv.writelines(data)


def export_data_to_txt(file_name):  # экспорт в txt
    with open(file_name, 'r', encoding='utf8') as infile:
        data = infile.read()
    data = data.replace('\n', '\n\n')
    data = data.replace(';', '\n')
    out_txt = open('new_txt_phone_directory.txt', 'w', encoding='utf8')
    out_txt.writelines(data)


def add_information(file_name, new_info):  # добавление информации
    with open(file_name, 'a', encoding='utf8', newline='') as data:
        data = csv.writer(data, delimiter=';')
        data.writerow(new_info)


def csv_data_open(file_name):
    with open(file_name, encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        res = list(file_csv)
    return res


def del_information(file_name, index):  # удаление информации
    data_csv = csv_data_open(file_name)
    del data_csv[index]
    with open(file_name, "w", encoding="utf8", newline='') as file:
        data = csv.writer(file, delimiter=';')
        for row in data_csv:
            data.writerow(row)


def update_information(file_name, index, phone):  # обновление информации
    data_csv = csv_data_open(file_name)
    data_csv[index][2] = phone
    with open(file_name, "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in data_csv:
            writer.writerow(row)
