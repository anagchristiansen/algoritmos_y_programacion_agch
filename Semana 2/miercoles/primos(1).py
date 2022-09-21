number = int(input("please enter a number"))
aux = number - 1
cont = 0

while aux > 1:
    aux -= 1
    if number % aux == 0:
        cont +=1
    aux -= 1

if cont > 0:
    print (f"the number {number} is prime")
else:
     print (f"the number {number} is not prime")