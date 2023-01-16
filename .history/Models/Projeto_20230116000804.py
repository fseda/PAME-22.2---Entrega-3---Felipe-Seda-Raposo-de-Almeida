class Projeto:
    def __init__(self, type_of_project, manager, consultants = []):
        self.manager = manager
        self.consultants = consultants
        self.type_of_project = type_of_project
        