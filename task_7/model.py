

def import_data(filename):
    with open(filename,'r',encoding='utf8') as data:
        data = data.read()
    return(data)


def export_data_to_csv(file_name):
    with open(file_name, 'r', encoding = 'utf8') as infile:
        data = infile.read()
    data = data.replace('\n', ';')
    data = data.replace(';;', '\n')
    out_csv = open('new_csv_phone_directory.csv', 'w', encoding = 'utf8')
    out_csv.writelines(data)


def export_data_to_txt(file_name):
    with open(file_name, 'r', encoding = 'utf8') as infile:
        data = infile.read()
    data = data.replace('\n','\n\n')
    data = data.replace(';','\n')
    out_txt = open('new_txt_phone_directory.txt', 'w', encoding = 'utf8')
    out_txt.writelines(data)


