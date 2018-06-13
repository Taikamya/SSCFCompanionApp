import sqlite3


class User(object):

    def __init__(self, _id, username, password, premium):
        super().__init__()
        self.id = _id
        self.username = username
        self.password = password
        self.premium = premium

    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = c.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        conn.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        query = "SELECT * FROM users WHERE id=?"
        result = c.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        conn.close()
        return user
