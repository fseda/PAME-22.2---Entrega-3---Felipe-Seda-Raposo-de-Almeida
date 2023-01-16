class Projeto:
    def __init__(self, type_of_project, gerente, consultores = []):
        self.gerente = gerente
        self.consultores = consultores
        self.type_of_project = type_of_project
        