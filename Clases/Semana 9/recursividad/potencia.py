def potencia(n,p):
   
    if p == 0:
        return 1

    else:
        n**p
        return n * potencia()


def main():
    n = int(input("introduzca la base: "))
    p = int(input("introduzca la potencia: "))
    print(potencia(n, p))

main()