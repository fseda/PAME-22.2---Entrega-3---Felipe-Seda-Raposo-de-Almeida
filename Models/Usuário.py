class Usuário:
    def __init__(self, id: int, username: str, password: str):
        self.id = id
        self.__username = username
        self.__password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username
        return username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
        return self.__password

