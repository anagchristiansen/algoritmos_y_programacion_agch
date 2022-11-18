from bebida import Bebida, Alcohol,Refresco


almacen_desactualizado = {
            "Alcohol":
        [
        	{ "nombre": "Linaje", "marca": "Santa Teresa", "grado": 40, "tipo": "Ron", "disponible": True },
        	{ "nombre": "Black Label 18", "marca": "Jonnie Walker", "grado": 43, "tipo": "Whisky", "disponible": True },
        	{ "nombre": "Solera Verde", "marca": "Polar", "grado": 6, "tipo": "Cerveza", "disponible": True }
        ], 
            "Refresco":
        [
        	{ "nombre": "Maltin Polar", "marca": "Polar", "azucar": 7, "sabor": "Malta", "disponible": True },
        	{ "nombre": "Pepsi", "marca": "Pepsico", "azucar": 7, "sabor": "Cola", "disponible": True },
        	{ "nombre": "Chinoto", "marca": "The Coca-Cola Company", "azucar": 4, "sabor": "Limon", "disponible": True }
        ] 
     }


#Bono
def bebida_mayor_grado():
    while True:

        for prod, articulos in almacen_desactualizado.items():
             for information in articulos:

                grado_alcohol = information.get("grado")
                nombre_beb = information.get("nombre")
                n = 0

                if grado_alcohol > n:
                    n = grado_alcohol

                else:
                    print(f"la bebida con mayor grado alcoholico es {n}")

        break



def mostrar_alc():
    alcohol = Alcohol
    [
        	{ "nombre": "Linaje", "marca": "Santa Teresa", "grado": 40, "tipo": "Ron", "disponible": True },
        	{ "nombre": "Black Label 18", "marca": "Jonnie Walker", "grado": 43, "tipo": "Whisky", "disponible": True },
        	{ "nombre": "Solera Verde", "marca": "Polar", "grado": 6, "tipo": "Cerveza", "disponible": True }
        ]
    return alcohol
   

def mostrar_ref():
    refresco = Refresco[
        	{ "nombre": "Maltin Polar", "marca": "Polar", "azucar": 7, "sabor": "Malta", "disponible": True },
        	{ "nombre": "Pepsi", "marca": "Pepsico", "azucar": 7, "sabor": "Cola", "disponible": True },
        	{ "nombre": "Chinoto", "marca": "The Coca-Cola Company", "azucar": 4, "sabor": "Limon", "disponible": True }
        ]
    return refresco


#print (mostrar())
    # for prod, articulos in almacen_desactualizado.items():
    #         for information in articulos:
                
    #             name_prod = information.get("nombre")
    #             brand_prod = information.get("marca")

    #             print(name_prod, brand_prod)
            


def main():
    
    print("\n **** M E N U **** \n")
    inventario = input("Select the type of drink you want to chose:\n-1 ✔ Alcohol \n-2 ✔ Refresco\n")

    if inventario == 1:
        print(mostrar_alc())


    if inventario == 2:
        print(mostrar_ref())

main()
