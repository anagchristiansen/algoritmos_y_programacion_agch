from ast import While
from cgi import print_exception
from unicodedata import name

def es_primo(rif):
    numero = int(rif[-1])
    aux = numero - 1
    
    while aux > 1:
        if numero % aux == 0:
            return False
        aux -=1
    return True



def main():

    products = {"1": {
                     "name" : "Químico",
                        "price" : 1000 , 
                                    },
                "2": {
                        "name" : "Farmaceutico",
                        "price" : 2500 , 
                                    },
                "3": {
                       "name" : "Biologico",
                        "price" : 4000 , 
                                    }
                                    }


    #For final Data:
    option_q = 0
    option_f = 0
    option_b = 0
    discount_c = 0
    discount_r = 0
    rif_max = 0
    max_purchase = 0
    total_day = 0



    while True:

        print("\n******* W E L C O M E *******\n")

        rif =  input ("Please enter your rif: \n")
        type_payment = input ("Please enter your payment type: \nC - One time \nB - Credit: \n")
        product_code = input ("Please enter the product code: \n1 - Quimico \n2 - Farmaceuico: \n3 - Biologico: \n")

        product_cost = products.get(product_code).get("price")

        #Descuento
        discount = 0 
        if type_payment == "C":
            discount += product_cost*0.03
        if product_cost % 2 == 0:
            discount += product_cost*0.02
        if es_primo(rif):
            discount += product_cost*0.05
        
        #Taxes
        tax = 0
        if product_code != "2":
            tax = product_cost*0.12
        
        total = product_cost - discount + tax


        print("\n***** R E C E I P T ******\n")
        print(f"User rif: {rif} \n")
        print("Producto: " , products.get(product_code).get("name"))
        print(f"\nMétodo de pago: {type_payment}\n")
        print(f"Descuento aplicado: {discount}$\n")
        print(f"Tax:.... {tax}$ \n")
        print(f"Monto a pagrar: ...... {total}$\n")

        #Final Data
        if product_code == "1":
            option_q += 1
        elif product_code == "2":
            option_f += 1
        elif product_code == "3":
            option_b += 1

        if type_payment == "c":
            discount_c += discount
        elif type_payment == "r":
            discount_r += discount
        if total >  max_purchase:
            rif_max = rif 
            max_purchase = total
        
        total_day += total



        salida = input("Would you like to exit? \n1 - Yes \n2 - No \n")
        if salida == "1":
            break

    print("\n E N D   O F  T H E   D A Y \n")
    print(f"compradores de productos:\nQuímicos: {option_q} \nFarmaceuticos: {option_f} \nBiológicos: {option_b}\n")
    print(f"Loss on discounts: \nOne time: {discount_c}$ \nCredit: {discount_r}$\n")
    print(f"The higuest shop rif: {rif_max}\n")
    print(f"Total today: {total_day}$ \n")




main()