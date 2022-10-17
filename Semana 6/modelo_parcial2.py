from ast import While


def main():

    products = {"Q": {
                     "name" : "Químico",
                        "price" : 1000 , 
                                    },
                "F": {
                        "name" : "Farmaceutico",
                        "price" : 2500 , 
                                    },
                "B": {
                       "name" : "Biologico",
                        "price" : 4000 , 
                                    }
                                    }


while True:
    name =  input ("Please enter your rif: ")
    type_payment = input ("Please enter your payment type: \nC - One time \nR - Credit: \nC")
    product_code = input ("Please enter the product code: \nQ - Quimico \nB - Biologico: ")

main()