from cgi import print_arguments


number= input ("please enter a whole number")
aux = 1

if number.isnumeric ():
    number = int(number)
    while number >= aux:
        if aux + 2 > number:
            print(aux)
        else:
            print(aux, end= ",")
        aux+=2

        print (aux,end=",")
    
else:
     print("error")

