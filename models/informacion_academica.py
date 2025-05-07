class InformacionAcademica:
    def __init__(self, id_academica=None, id_funcionario=None, universidad='', nivel_estudio='', titulo=''):
        self.id_academica = id_academica
        self.id_funcionario = id_funcionario
        self.universidad = universidad
        self.nivel_estudio = nivel_estudio
        self.titulo = titulo

    def __str__(self):
        return f"{self.nivel_estudio} en {self.titulo} - {self.universidad}"
