from gettext import translation


traductor = {}
pares_palabras = input("Please enter the words in the format <palabra>:<traducción>: ")
dicc_de_traducciones = pares_palabras.split(",")

for pares_palabras in dicc_de_traducciones:
    valores_lista = pares_palabras.split(":")
    print(valores_lista)
#['hello', 'hola']
    key_english = valores_lista[0]
    valor_español = valores_lista[1]
    traductor[key_english] = valor_español




