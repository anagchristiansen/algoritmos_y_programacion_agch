import random
from article import Articulo

class Redactor:                                     #las acciones son los métodos
    def __init__(self, cedula, nombre):    
        self.ci = cedula                           #atributos
        self.nombre = nombre

    def escribir_articulo(self):
        print("estoy escribiendo un articulo")
        articulo = Articulo(
            input("Titulo: "),
            input("Cuerpo: "),
            input("Fecha: "),
            input("Resumen: "),
            input("Imagenes: "),
            )
        print("Termine el articulo", articulo.titulo)
        return articulo

class JefeRedactor(Redactor):
    def __init__(self, cedula, nombre, grupo):
        super().__init__(cedula, nombre)
        self.grupo_de_redactor = grupo

    def supervisar(self):
        print("Todo esta bien con los redactores")

    def decidir(self,articulo):
        if random.random() > 0.5:
            print("El ariculo", articulo.titulo, "fue aprobado")
            articulo.fecha_publicacion = "HOY"
        else:
            print("El ariculo", articulo.tiulo, "no fue aprobado")
            