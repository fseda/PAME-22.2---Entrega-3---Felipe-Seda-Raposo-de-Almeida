class Projeto:
    def __init__(self, type_of_project, manager, consultants = []):
        self.manager = manager
        self.consultants = consultants
        self.type_of_project = type_of_project
        self.remaining_steps = self.get_remaining_steps(type_of_project)

    def get_remaining_steps(self, type_of_project):
        # Desenvolvimento
        if type_of_project == 0: 
            self.remaining_steps = 4
        # Concepção
        elif type_of_project == 1: 
            self.remaining_steps = 5
        elif type_of_project == 2: 
            self.remaining_steps = 6
