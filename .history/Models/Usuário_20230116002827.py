import csv
import bcrypt

class User:
    def __init__(self, id, username, password):
        self.id = id
        # self.__username = self.username(username)
        # self.__password = self.password(password)
        self.__username = username
        self.__password = password
        self.__create_user()

        self.projetos = []

    # "Hash" a senha para maior proteção
    def __hash_password(self, password):
        # Se não tiver o bcrypt instalado a senha é guardada "crua"
        try:
            return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        except:
            return password

    # def __create_user(self):

    #     # Adicionar user à base de dados
    #     with open('User.csv', 'a') as file:
    #         fieldnames = ['id', 'username', 'password']
    #         writer = csv.DictWriter(file, fieldnames=fieldnames)

    #     writer.writerow({
    #         'id': self.id,
    #         'username': self.__username,
    #         'password': self.password,
    #     })

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
        self.__password = self.__hash_password(password)
        return self.__password

