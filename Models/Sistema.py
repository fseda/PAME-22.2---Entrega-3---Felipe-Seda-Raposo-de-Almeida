from Consultor import Consultor
from Gerente import Gerente
from Projeto import Projeto

class Sistema:
    def __init__(self):
        self.users = [] # Lista de Usuários
        self.projects = [] # Lista de Projetos

        self.logged_in_type_of_user = None
        self.logged_in_user = None

    def create_manager(self, username, password):
        id = len(self.managers)
        self.managers.append(Gerente(id=id, username=username, password=password))
        return self.managers[id]
    
    def create_consultant(self, username, password):
        id = len(self.consultants)
        self.consultants.append(Gerente(id=id, username=username, password=password))
        return self.consultants[id]

    def create_project(self, tipo_de_projeto, manager, consultants):
        pass

    def username_taken(self, username):
        for user in self.users:
            if user.username == username:
                return True
        
        
        return False

    def login(self, username, password):
        pass