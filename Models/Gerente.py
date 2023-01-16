from Models.Usuário import Usuário

from constants import OK, FAILED

class Gerente(Usuário):
    def __init__(self, id, username, password):
        super().__init__(id, username, password)
        self.quit_projects_requests = []

    def quit_project(self, project_id, consultant):
        request = {
            'Projeto ID': project_id, 
            'Consultor': consultant
        }

        # Evita pedidos duplos 
        for quit_project_request in self.quit_projects_requests:
            if quit_project_request == request:
                return FAILED
        
        self.quit_projects_requests.append(request)
        
        return OK
    

        
    
        