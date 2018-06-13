import sqlite3


def create_user_table():
    global cursor
    table = "CREATE TABLE IF NOT EXISTS users (id int, username text, password text)"

    cursor.execute(table)
    user = (1, 'Testando', '123456')

    insert_query = "INSERT INTO users VALUES (?, ?, ?)"
    cursor.execute(insert_query, user)
    return


connection = sqlite3.connect("sscf.db")
cursor = connection.cursor()
create_user_table()
connection.commit()
connection.close()
