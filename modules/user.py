class User(object):

    def __init__(self, _id, username, password, premium=False):
        super().__init__()
        self.id = _id
        self.username = username
        self.password = password
        self.premium = premium
