from anun import AnuncioClasificados, AnuncioVehiculo, AnuncioComercial, AnuncioVivienda
from redactor import Redactor, JefeRedactor
from section import Seccion

def get_redactores_entrenimiento():
    return [
        Redactor("Pedro",1234)
    ]
    """Redactor("Juan",1234),
        Redactor("Pedro",1234),
        Redactor("Maria",1234),
        Redactor("Jose",1234),"""

def get_redactores_deportes():
    return [
        Redactor("Antonio",1234)   
    ]
    """Redactor("Christian",1234),
        Redactor("Ana",1234),
        Redactor("Andrea",1234),
        Redactor("Sebastian",1234),"""

def get_redactores_farandula():
    return [
        Redactor("Andres",1234)
    ]
    """Redactor("Pablo",1234),
        Redactor("Erika",1234),
        Redactor("Oriana",1234),
        Redactor("Cristiano",1234),"""

def procesar_articulos(seccion):
    print("Empezamos la Jornada en la seccion",seccion.name)
    for escritor in seccion.jefe_redactor.grupo_de_redactor:
        print("El escritor al mando en este momento es",escritor.nombre)
        articulo = escritor.escribir_articulo()
        print("El jefe que va a decidir es",seccion.jefe_redactor.nombre)
        seccion.jefe_redactor.decidir(articulo)


def main():

    jefe_entretenimiento = JefeRedactor("Jose Quevedo",12345,get_redactores_entrenimiento())
    jefe_deportes = JefeRedactor("Antonio Guerra",12345,get_redactores_deportes())
    jefe_farandula = JefeRedactor("Luis Bello",12345,get_redactores_farandula())

    seccion_entretenimiento = Seccion("Entrenimiento",jefe_entretenimiento)
    seccion_deportes = Seccion("Deportes",jefe_deportes)
    seccion_farandula = Seccion("Farandula",jefe_farandula)

    procesar_articulos(seccion_entretenimiento)
    procesar_articulos(seccion_deportes)
    procesar_articulos(seccion_farandula)
    





main()