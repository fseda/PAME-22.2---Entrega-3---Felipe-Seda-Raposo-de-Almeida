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
        return 
    
    def 

    