class Bebida:
    def __init__(self, nombre: str, marca: str, disponible:bool):
        self.name = nombre
        self.brand = marca
        self.available = disponible

    def mostrar(self):
        print(f"Nombre: {self.name} ({self.brand})\nDisponible: {self.available}\n")


class Alcohol(Bebida):
    def __init__(self, nombre:str, marca:str, disponible:bool, grado:str, tipo:float):
        super().__init__(nombre, marca, disponible)
        self.grade = grado
        self.type = tipo

class Refresco(Bebida):
    def __init__(self, nombre:str, marca:str, disponible:bool, azucar:float, sabor:str):
        super().__init__(nombre, marca, disponible)
        self.sugar = azucar
        self.flavor = sabor