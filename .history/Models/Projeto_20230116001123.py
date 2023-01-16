class Projeto:
    def __init__(self, type_of_project, manager, consultants = []):
        self.manager = manager
        self.consultants = consultants
        self.type_of_project = type_of_project
        self.remaining_steps = self.remaining_steps(type_of_project)

    def remaining_steps(self, type_of_project):
        if type_of_project == 0: # Desenvolvimento
            self.remaining_steps = 4
        elif type_of_project == 1: # Concepç
