import sqlite3


# инициализация соединения с БД
def init_database(file_name):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    return cursor


def show_all(cursor):    
# показать всех сотрудников в консоле
    cursor.execute("SELECT * from employeers")
    results = cursor.fetchall()
    print(results)


# добавить сотрудника
def add_person(file_name, surname, name, job_title):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO employeers (surname, name, job_title)" f"VALUES ('{surname}','{name}','{job_title}')")
    conn.commit()
    cursor.close()


