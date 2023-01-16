from Models.Usuário import Usuário

class Consultor(Usuário):
    def __init__(self, id, username, password):
        super().__init__(id, username, password)
        