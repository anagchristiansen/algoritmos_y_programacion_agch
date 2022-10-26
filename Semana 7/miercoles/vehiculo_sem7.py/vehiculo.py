class Vehiculo:
    def __init__ (self, color, ruedas):     #parametro
        self.color = color                 #atributo
        self.ruedas = ruedas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cc):
        Vehiculo.__init__(color, ruedas)
        self.velocidad = velocidad
        self.cc = cc


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cc, carga):
        super().__init__(color, ruedas, velocidad, cc)
        self.carga = carga


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo


class Motocicllrta (Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cc):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cc= cc
        