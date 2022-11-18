# datos = {}
# datos = input("Enter your name ")
# datos += input("Enter your age ")
# datos += input("Enter your mail ")
# datos += input("Enter your phone number ")

# print(datos)

datos = {}

while True:
    key_datos = input("Please enter what you whant to save: ")
    valor_data = input("Enter the value you whant to save: ")
    datos [key_datos] = valor_data
    print ("Data: ")

    for key_datos, valor_data in datos.items():
        print(f"Your {key_datos}: {valor_data}")
