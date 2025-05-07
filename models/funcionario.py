class Funcionario:
    def __init__(self, id_funcionario=None, tipo_identificacion='', numero_identificacion='', nombres='',
                 apellidos='', estado_civil='', sexo='', direccion='', telefono='', fecha_nacimiento=''):
        self.id_funcionario = id_funcionario
        self.tipo_identificacion = tipo_identificacion
        self.numero_identificacion = numero_identificacion
        self.nombres = nombres
        self.apellidos = apellidos
        self.estado_civil = estado_civil
        self.sexo = sexo
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.numero_identificacion})"
