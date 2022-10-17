import random 

def generar_tickets():

    tickets = []

    while True:
        try:
            amt = int(input("Ingrese la cantidad de tickets a generar"))
            if amt == 0:
                raise Exception
            break

        except: 
            print("ingreso inválido")

        while len(tickets) < amt:
            t = random.randint(10000000 , 99999999)
            if not t in tickets:
                tickets.append(t)

        return tickets


def elegir_ganador(t):
    return random.choice(t)
