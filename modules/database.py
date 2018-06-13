import sqlite3
# from pprint import pprint as pp


def connect():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, 
                 password text, premium integer)""")
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT *  FROM users")
    rows = c.fetchall()
    conn.close()
    return rows


def insert(username, password, premium=0):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?)", (username, password, premium))
    conn.commit()
    conn.close()


def update(id, username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("UPDATE users SET username=?, password=? WHERE id=?", (username, password, id))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()


def search(username=""):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    rows = c.fetchall()
    conn.close()
    return rows


connect()
# insert('Pablo Viado-Vittar', 'sougay24', 0)
# insert('Dimi Lindo', 'soufoda69', 1)
# insert('Evelynda', 'unicornios', 0)
# insert('Tinha Matos', 'queroMato', 1)
# print(f"Viewing the Database: {view()}")
# print("Searching for user: %s \n" % search('Pablo'))
# print(f"User {delete(1)} was deleted.")
# print(f"Viewing the Database: {view()}")
# update(4, 'Agostinha Matos', 'amoKiko')
# print(f"User {search('Agostinha')} was just updated!")
