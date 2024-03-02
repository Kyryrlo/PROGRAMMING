from ast import Delete
from sqlite3 import *
from sqlite3 import Error
#--------------------------Functsionid----------------------------------------------------------
def creat_connection(path: str):
    """Uhendus andmebaasiga
    """
    connection = None
    try:
        connection = connect(path)
        print("Uhendus on educdlt tehtud")
    except Error as e:
        print(f"Tekkus viga '{e}'")
    return connection 
def execute_query(connection: str, query: str):
    """Tabeli loomine
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud")
    except Error as e:
        print(f"Viga '{e}' tabeli lomisega")
def execute_read_query(connection, query: str):
    '''Tabeli andmete vaatamine
    '''
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
     print(f"Viga '{e}'")
def execute_delete_query(connection, query: str):
    '''Tabeli/andmete eemaldamine
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabeli/andmete on kustatud")
    except Error as e:
        print(f"Viga '{e}'")


#--------------------------SQL laused----------------------------------------------------------
create_users_table = """
CREATE TABLE IF NOT EXISTS users(
id integer primary key AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT, 
student BOOLEAN
);
"""
create_users = """
INSERT INTO
    users(name, age, gender, student)
VALUES
    ('Mati',45,'mees',false),
    ('Kaadri',18,'naine',true),
    ('Andres',25,'mees',true),
    ('Mari',65,'naine',true),
    ('Anna',97,'naine',false);
"""
select_users = "SELECT * FROM users"
delete_data_from_users = """
DELETE FROM users 
WHERE student = true
"""
talete_table_users = "DROP TABLE users"
#---------------------------Kasutamine---------------------------------------------------------
conn = creat_connection("G:/Шкила/PROGRAMMING/WORK ON LESSONS/PythonApplication1/AppData/data.db")
execute_query(conn, create_users_table)
execute_query(conn, create_users)

users = execute_read_query(conn, select_users)
print("Kasutajate andmend:")
for user in users:
    print(user)
    
execute_delete_query(conn,delete_data_from_users)

users = execute_read_query(conn, select_users)
print("Kustutatud tudengid, on jaanud neid kellel student = 0:")
for user in users:
    print(user)
    
execute_delete_query(conn,talete_table_users)
