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

input_a_traduccion = input("Please enter a frase to translate: ")
lista_de_palabras = input_a_traduccion.split(" ")
resultado = ""

for word in lista_de_palabras:
    resultado += traductor.get (word,word)

print(resultado)



