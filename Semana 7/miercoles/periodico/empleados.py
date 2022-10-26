class Trabajadores:
    def __init__(self,cedula, nombre, seccion):
        self.cedula = cedula
        self.nombre = nombre
        self.seccion = seccion

class Jefe(Trabajadores):
    def __init__(self, cedula, nombre, seccion, puesto):
        super().__init__(cedula, nombre, seccion)