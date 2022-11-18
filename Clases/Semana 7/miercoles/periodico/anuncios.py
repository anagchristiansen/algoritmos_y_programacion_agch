class AnuncioComercial:
    def __init__(self, imagen, seccion):
        self.imagen = imagen
        self.seccion = seccion  


class AnuncioClasificados:
    def __init__(self, precio, fecha_publicacion, dias, tipos):
        self.precio = precio
        self.fecha_de_publicacion = fecha_publicacion
        self.cantidad_dias = dias
        self.tipos = tipos

class AnuncioVehiculo(AnuncioClasificados):
    def __init__(self, precio, fecha_publicacion, dias, marca, modelo, año):
        super().__init__(precio, fecha_publicacion, dias, "Vehículo")
        self.marca = marca
        self.modelo = modelo
        self.año = año

class AnuncioVivienda(AnuncioClasificados):
    def __init__(self, precio, fecha_publicacion, dias, m2, baño):
        super().__init__(precio, fecha_publicacion, dias, "Vehículo")
        self.m2 = m2
        self.baño = baño
