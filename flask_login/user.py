class User():

    def __init__(self, username, password):
        self._id = None
        self._username = username
        self._password = password
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False

    def assign_ID(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def get_username(self):
        return self._username

    def authenticate(self, password):
        if password == self._password:
            return True
        return False

    def __str__(self):
        return str(self._id) + ' ' + self._username + ' ' +  self._password


class UserManager():
    def __init__(self):
        self._users = {}
        self._nUsers = 0
        self._username_id_table = {}
    
    def add_user(self, newUser):
        newUser.assign_ID(self._nUsers)
        self._users[newUser.get_id()] = newUser
        self._username_id_table[newUser.get_username()] = newUser.get_id()
        self._nUsers += 1

    def get_user(self, targetId):
        if targetId in self._users.keys():
            return self._users[targetId]
        return None
    
    def __str__(self):
        toReturn = []
        for user in self._users.keys():
            toReturn.append(str(self._users[user]))
        return ''.join(toReturn)

    def login(self, username, password):
        if username in self._username_id_table.keys():
            if self._users[self._username_id_table[username]].authenticate(password):
                return self._users[self._username_id_table[username]]
        return None

    @property
    def users(self):
        return self._users

