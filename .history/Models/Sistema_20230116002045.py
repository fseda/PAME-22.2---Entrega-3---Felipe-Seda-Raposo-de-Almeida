from Consultor import Consultor
from Gerente import Gerente
from Projeto import Projeto

class Sistema:
    def __init__(self):
        self.managers = [] # Lista de Gerentes
        self.consultants = [] # Lista de Consultores
        self.projects = [] # Lista de Projetos

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
        for manager in self.managers:
            if manager.username == username:
                return True
        
        for consultant in self.consultants:
            if consultant.username == username:
                return True