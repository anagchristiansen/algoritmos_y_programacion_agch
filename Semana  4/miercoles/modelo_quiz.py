from ast import While

products = {
        "mobiles": {
            "Apple": [
                {
                    "id": 1,
                    "name": "iPhone 7",
                    "price": 300
                },
                {
                    "id": 2,
                    "name": "iPhone 8",
                    "price": 350
                },
                {
                    "id": 3,
                    "name": "iPhone Xr",
                    "price": 450
                },
                {
                    "id": 4,
                    "name": "iPhone Xs",
                    "price": 460
                },
                {
                    "id": 5,
                    "name": "iPhone 11",
                    "price": 900
                },
                {
                    "id": 6,
                    "name": "iPhone 12",
                    "price": 1100
                },
                {
                    "id": 7,
                    "name": "iPhone 13",
                    "price": 1300
                },
            ],
            "Samsung": [
                {
                    "id": 8,
                    "name": "Samsung Galaxy Beam",
                    "price": 150
                },
                {
                    "id": 9,
                    "name": "Samsung Galaxy S6",
                    "price": 200
                },
                {
                    "id": 10,
                    "name": "Samsung Galaxy S7",
                    "price": 300
                },
            ],
            "Xiaomi": [
                {
                    "id": 11,
                    "name": "Xiaomi Redmi Note 8",
                    "price": 250
                },
                {
                    "id": 12,
                    "name": "Xiaomi Redmi Note 8 Pro",
                    "price": 300
                },
            ]
        },
        "laptops": {
            "DELL": [
                {
                    "id": 13,
                    "name": "Dell Inspiron 15",
                    "price": 600
                },
                {
                    "id": 14,
                    "name": "Dell Latitude 14",
                    "price": 650
                },
            ],
            "MAC": [
                {
                    "id": 15,
                    "name": "MacBook Pro 13",
                    "price": 900
                },
                {
                    "id": 16,
                    "name": "MacBook M1",
                    "price": 1500
                },
            ]
        },
    }


print("\n******** WELCOME ********\n")

while True:

        print("\n P R I N C I P A L   M E N U \n")
        menu = input("Please enter one of the following options: \n1- Catalog \n2- Process shopping \n3- Exit \n")

        if menu.isnumeric:
            menu = int (menu)
        else:
            pass

        if menu == 1:
            print("\n C A T A L O G:\n")
            catalogo = input(f"What device would you like to have information about? \n1- mobile \n2- laptops \n")
            
            if catalogo ==  1:

                 for device, brands in products.items() :
                    for brand, device_info in brands.items():
                        for data in device_info:
                        
                            prod_number = int(data.get("id"))
                            prod_name = data.get("name")
                            prod_price = data.get("price")

                        
                        if prod_number < 13:
                            print(brand)
                            print(f"\n (id:{prod_number}) {prod_name}\n price: {prod_price}$ \n")