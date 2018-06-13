import sqlite3


class User(object):
    TABLE_NAME = 'users'

    def __init__(self, _id, username, password, premium=False):
        super().__init__()
        self.id = _id
        self.username = username
        self.password = password
        self.premium = premium

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('sscf.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username=?".format(
            table=cls.TABLE_NAME)
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
