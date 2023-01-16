from constants import OK, CONSULTANT_NOT_IN_PROJECT, PROJECT_ADVANCE_ALREADY_REQUESTED, NOT_ADVANCED,\
    DES, CON, IDV


class Projeto:
    def __init__(self, id, name, type_of_project, manager: str, consultants: list[str] = []):
        self.id: int = id
        self.name: str = name
        self.__manager: str = manager
        self.__consultants: list[str] = consultants
        self.type_of_project: int = type_of_project # DES = 11 | CON = 12 | IDV = 13
        self.remaining_steps = self.get_remaining_steps(type_of_project)
        self.advance_project_request = {'Requested': False, 'Requested_From': None}

    def get_remaining_steps(self, type_of_project):
        # Desenvolvimento
        if type_of_project == DES: 
            return 4
        
        # Concepção
        elif type_of_project == CON: 
            return 5
        
        # Identidade Visual
        elif type_of_project == IDV: 
            return 6
    
    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager):
        self.__manager = manager

    @property
    def consultants(self):
        return self.__consultants

    def create_advance_project_request(self, consultant):
        # Se já existe pedido de avanço
        if self.advance_project_request['Requested']:
            print('already advanced')
            return PROJECT_ADVANCE_ALREADY_REQUESTED

        # Consultor que fez pedido não está no projeto
        if consultant not in self.consultants:
            print('not in project')
            return CONSULTANT_NOT_IN_PROJECT

        self.advance_project_request['Requested'] = True
        self.advance_project_request['RequestedFrom'] = consultant

        return OK

    def advance_project(self, decision):
        if decision:
            self.remaining_steps -= 1
            return OK
        return NOT_ADVANCED