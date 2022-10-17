from ast import While


def factorial (n):
    
    f = 1

    for x in range(2, n+1):
        f *= x
    
    return f


def main():
    while True:
        try:
            numero = int(input("Ingrese un número natural: "))
            if numero == 0:
                raise Exception
            break

        except: 
            print("ingreso inválido")

    respuesta = factorial(numero)

    print(f"El factorian de {numero} es {respuesta}")

main()