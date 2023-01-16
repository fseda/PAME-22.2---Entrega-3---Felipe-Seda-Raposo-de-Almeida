import os
import csv
import bcrypt

class Gerente:
    def __init__(self, username, password):
        self.id = self.__create_id()
        # self.__username = self.username(username)
        # self.__password = self.password(password)
        self.__username = username
        self.__password = password
        self.__create_gerente()

        self.projetos = []

    # Criado em ordem sequencial
    def __create_id(self):  

        if os.path.exists('Gerente.csv'):
            # Ler Gerente.csv para saber qual o id para o próximo Gerente deve ser
            with open('Gerente.csv', 'r') as file:
                reader = csv.reader(file)
                return len(list(reader))
        else:
            return 0
        
    # "Hash" a senha para maior proteção
    def __hash_password(self, password):
        # Se não tiver o bcrypt instalado a senha é guardada "crua"
        try:
            re turn bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        except:
        return password

    def __create_gerente(self):

        # Adicionar gerente à base de dados
        with open('Gerente.csv', 'a') as file:
        fieldnames = ['id', 'username', 'password']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        print(self.id)

        writer.writerow({
            'id': self.id,
            'username': self.__username,
            'password': self.password,
        })

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
        return self.__hash_password(password)

