nombre = input("Por favor, ingrese su nombre: ")
edad = int(input("Ingrese su edad en digitos: "))
precio_entrada = 2

if edad <= 4:
    precio_entrada -= 2
if 4 < edad <= 18:
    precio_entrada -= 0.5
if edad >= 60:
    precio_entrada -= 1

print (f"El cliente: {nombre} tiene {edad} años, y debe pagar {precio_entrada}$")

