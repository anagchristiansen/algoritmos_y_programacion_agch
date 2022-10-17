
from loteria__funct import generar_tickets, elegir_ganador

def main():
    
    tickets = generar_tickets()
    print(tickets)

    print(elegir_ganador(tickets))
    

main()
