import sqlite3


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
    c.execute("SELECT * FROM users ORDER BY id")
    all_rows = c.fetchall()
    conn.close()
    return all_rows


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
