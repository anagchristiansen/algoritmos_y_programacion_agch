number = int(input("Introduce un número para saber si es par o impar, y positivo o negativo: "))

if number%2 == 0:
     if number > 0:
        print(f"el numero {number} es par y positivo")
     elif number == 0: 
        print(f"el numero {number} es par")
     else:
        print(f"el numero {number} es par y negativo")

else:
    if number > 0:
        print(f"el numero {number} es impar y positivo")
    else:
        print(f"el numero {number} es impar y negativo")