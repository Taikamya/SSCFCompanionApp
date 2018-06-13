import sqlite3


conn = sqlite3.connect(':memory:')
c = conn.cursor()

table = ("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, 
            password text, premium int)""")
c.execute(table)

user = ("Testando", "123456", 0)

insert_query = "INSERT INTO users VALUES (NULL, ?, ?, ?)"
c.execute(insert_query, user)

c.execute("SELECT * FROM users WHERE username=?", ('Testando',))

print(c.fetchall())
conn.commit()
conn.close()
