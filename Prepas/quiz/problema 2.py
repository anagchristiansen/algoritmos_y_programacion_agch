juegos = {
    "Shooter": [
        {
            "id": 1,
            "name": "Overwatch2",
            "price": 60  
        },
        {
            "id": 2,
            "name": "Valorant",
            "price": 0
        },
        {
            "id": 3,
            "name": "Pixel Gun 3D",
            "price": 10
        }
    ],
    "RPG": [
        {
            "id": 4,
            "name": "Pokemon",
            "price": 50  
        },
        {
            "id": 5,
            "name": "Final Fantasy Exvius",
            "price": 0
        }
    ],
    "Open World": [
        {
            "id": 6,
            "name": "Minecraft",
            "price": 60  
        },
        {
            "id": 7,
            "name": "Cyberpunk 2077",
            "price": 60
        },
        {
            "id": 8,
            "name": "GTA V",
            "price": 40
        }
    ],  
}

print("\n****** WELCOME ******")
while True:
    inicio = input("\nSelect your next action: \n \n1- Available games \n2- Shop and register \n3- Statistics \n action: ")

    # while inicio <= 3:
    #     inicio = int(inicio)
    # 

    if int(inicio) == 1:
        print("\nTHE AVAILABLE GAMES AT THIS TIME:")
        for category, games in juegos.items():
            for information in games:

                id_game = information.get("id")
                name_game = information.get("name")
                price_game = information.get("price")


                print(f"\n{name_game} (id:{id_game}): {price_game}$")



    if int(inicio) == 2:
        name= input("Please enter you name and last name: ")
        ci= input("Please enter your personal id: ")
        number_game= int(input("Please enter the id of the game you selected: "))
        
        if number_game == 1:
            print("\nRECEIPE: \n")
            print(f"\n Client: {name} \n id: {ci} \n Overwatch2......60$")

        if number_game == 2:
            print("\nRECEIPE: \n")
            print(f"\n Client: {name} \n id: {ci} \n The game Valorant is free")

        if number_game == 3:
                    print("\nRECEIPE: \n")
                    print(f"\n Client: {name} \n id: {ci} \n Pixel Gun 3D......10$")
        
        if number_game == 4:
                    print("\nRECEIPE: \n")
                    print(f"\n Client: {name} \n id: {ci} \n Pokemon......50$")

        if number_game == 5:
            print("\nRECEIPE: \n")
            print(f"\n Client: {name} \n id: {ci} \n The game Final Fantasy Exvius is free")
        
        if number_game == 6:
                    print("\nRECEIPE: \n")
                    print(f"\n Client: {name} \n id: {ci} \n Minecraft......60$")

        if number_game == 7:
                    print("\nRECEIPE: \n")
                    print(f"\n Client: {name} \n id: {ci} \n Cyberpunk 2077......60$")

        if number_game == 8:
                    print("\nRECEIPE: \n")
                    print(f"\n Client: {name} \n id: {ci} \n GTA V......40$")

                    #YOSE QUE ESTO ESTA SUPER ARCAICO PERDON SERGIO TEN PIEDAD se te quiere <3
                    #no se las estadisticas porque no registre los datos perdon hago mi mayor esfuerzo.

        

        ci_descuento = int(input("please enter a number"))
        aux = ci_descuento - 1
        cont = 0

        while aux > 1:
            aux -= 1
            if ci_descuento % aux == 0:
                cont +=1
            aux -= 1

        if cont > 0:
            print (f"You may save 40%")

        
       
       
       
       
       
        # for category, games in juegos.items():
        #     for information in games:

        #         id_game = information.get("id")
        #         name_game = information.get("name")
        #         price_game = information.get("price")

        #         compra = {}
        
       # factura = print(f"{name}\n ci: {ci}\n )


