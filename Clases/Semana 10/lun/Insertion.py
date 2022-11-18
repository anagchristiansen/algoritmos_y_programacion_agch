def main():
    
    lista = [6,5,3,1,8,7,2,4]
    
    for i in range(len(lista)):
        temp = i
        valor = lista[i]
        j = i - 1
        while j > 0 and lista[i] < lista[j]:
            lista[temp] = lista[j]
            temp -= 1
            lista[j]= valor
            temp -= 1
            j -= 1
        print()

main()