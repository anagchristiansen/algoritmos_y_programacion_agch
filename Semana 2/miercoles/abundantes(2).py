number = int(input("please enter a number"))
aux = number -1
acum = 0

while aux > 1:
    if number % aux == 0:
        acum += aux
    aux -= 1

if acum > number:
    print (f" The numbe {number} is abundant")
else:
    print (f" The numbe {number} is not abundant")
