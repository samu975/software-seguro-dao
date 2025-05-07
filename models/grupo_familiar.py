class GrupoFamiliar:
    def __init__(self, id_familiar=None, id_funcionario=None, nombre='', parentesco='', edad=0):
        self.id_familiar = id_familiar
        self.id_funcionario = id_funcionario
        self.nombre = nombre
        self.parentesco = parentesco
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} - {self.parentesco} ({self.edad} años)"
