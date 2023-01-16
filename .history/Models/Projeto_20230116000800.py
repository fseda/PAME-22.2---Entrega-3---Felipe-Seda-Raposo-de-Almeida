class Projeto:
    def __init__(self, type_of_project, manager, consultores = []):
        self.manager = manager
        self.consultores = consultores
        self.type_of_project = type_of_project
        