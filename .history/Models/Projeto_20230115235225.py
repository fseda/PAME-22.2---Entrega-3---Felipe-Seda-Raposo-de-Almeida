class Projeto:
    def __init__(self, tipo_de_projeto, gerente, consultores = []):
        self.gerente = gerente
        self.consultores = consultores
        self.tipo_de_projeto = tipo_de_projeto
        