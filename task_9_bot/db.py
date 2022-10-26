import sqlite3

# инициализация соединения с БД
def init_database(file_name):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    return cursor


def show_all(cursor):    
# показать всех сотрудников в консоли
    cursor.execute("SELECT * FROM employeers")
    results = cursor.fetchall()
    print(results)


# добавить сотрудника
def add_person(file_name, surname, name, personal_number, job_title):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO employeers (surname, name, personal_number, job_title)" f"VALUES ('{surname}','{name}','{personal_number}','{job_title}')")
    conn.commit()
    print(("Добавлена новая запись - успешно!"))
    conn.close()


# поиск записи
def find_person(file_name, surname):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM employeers WHERE surname like '%{surname}%'")
    results = cursor.fetchall()
    if results == []:
        print('Искомый сотрудник в базе данных отсутствует') 
    else: print(results)
    return results


# удалить сотрудника
def del_person(file_name, del_surname):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employeers WHERE surname=?", (del_surname,))
    conn.commit() 
    print(f"Удаление записи о сотруднике по фамилии {del_surname} прошла успешно!")
    conn.close()


# обновить данные о сотруднике
def update_info(file_name, old_surname, new_surname):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE employeers SET surname = '{new_surname}' WHERE surname like '%{old_surname}%'")
    conn.commit() 
    print(f"Фамилия сотрудника {old_surname}, обновлена на {new_surname} - успешно!")
    conn.close()


