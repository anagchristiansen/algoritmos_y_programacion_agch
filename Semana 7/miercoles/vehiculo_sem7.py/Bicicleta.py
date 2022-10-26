
import imp
from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo


class Motocicllrta (Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cc):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cc= cc