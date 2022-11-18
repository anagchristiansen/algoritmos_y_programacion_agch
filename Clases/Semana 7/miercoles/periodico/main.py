from redactor import Redactor, JefeRedactor
from seccion import Seccion

def get_redactores_entretenimiento():
    return [
        Redactor("Pedro", 1234),
        Redactor("Juan", 1234),
        Redactor("Maria", 1234),
        Redactor("Jose", 1234)
    ]

def get_redactores_deporte():
    return [
        Redactor("Cristian", 1234),
        Redactor("Ana", 1234),
        Redactor("Andrea", 1234),
        Redactor("Sebastian", 1234)
    ]

def get_redactores_farandula():
    return [
        Redactor("Adres", 1234),
        Redactor("Pablo", 1234),
        Redactor("Erika", 1234),
        Redactor("Oriana", 1234),
        Redactor("Cristiano", 1234)
    ]

def procesar_articulos(seccion):
    for escritor in seccion.jefe_redactor.grupo_de_redactor:
        print("Empezamos la jornada en la seccion", seccion.nombre)
        print("El escritor al mando en este momento es", escritor.nombre)
        articulo = escritor.escribir_articulo()
        seccion.jefe_redactor.decidir(articulo)

def main():

    jefe_entretenimiento = JefeRedactor("Jose Quevedo", 12345, get_redactores_entretenimiento)
    jefe_deportes = JefeRedactor("Antonio Guerra", 12345, get_redactores_deporte)
    jefe_farandula = JefeRedactor("Luis Bello", 12345, get_redactores_farandula)

    seccion_entretenimiento = Seccion("Entretenimiento", jefe_entretenimiento)
    seccion_deporte = Seccion("Deporte", jefe_deportes)
    seccion_efarandula = Seccion("Entretenimiento", jefe_farandula)

    procesar_articulos(seccion_entretenimiento)
    procesar_articulos(seccion_deporte)
    procesar_articulos(seccion_efarandula)