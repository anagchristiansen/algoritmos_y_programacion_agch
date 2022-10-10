from ast import While


def print_welcome():
    print("\n***** W E L C O M E *****\n")


def get_user_option(dict):
    for key, value in dict.items():
        for key_interno, value_interno in value.items():
                print(f"{key} - {value_interno}", end ="")
        print("")

    return input("Please enter ")


def get_client_data(study):
    client = {
            "name" : input("Please enter the client name: "),
            "id" : input("Please enter the client id: "),    
            "age" : input("Please enter the client age: "),
            "gender" : input("Please enter the client gender M or F: \n"),
            "study" : study
            }
    return client

def print_invoice(client):
    print("\n R E C E I P T \n")
    print("ID:", client.get ("id"))
    print("Age:", client.get ("age"))
    print("Gender:", client.get ("gender"))
    print("NetAmount:", client.get (""))




def main():
    studies_dict_values = {
                            "U": {
                                    "name" : "Ultrasonido",
                                    "price" : 8900 , 
                                    },
                            "T": {
                                    "name" : "Tomografía",
                                    "price" : 12640 , 
                                    },
                            "R": {
                                    "name" : "Resonancia",
                                    "price" : 15600 , 
                                    }
                                    }

    clients = []
    
    print_welcome()
    while True:
        option = get_user_option(studies_dict_values)
        client = get_client_data(option)
        print_invoice(client)



        clients.append(client)


main()