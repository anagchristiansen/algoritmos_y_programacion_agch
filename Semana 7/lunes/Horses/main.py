from Horse import Horse
from Valida import Valid
from Race import Race

def main():

    print("W E L C O M E\n")
    valids = int(input("Please enter how many valids wil we have: \n"))
    races = int(input("Please enter how many races wil we have in each day: \n"))

    hosrse1 = Horse("El rayo veloz",1)
    hosrse2 = Horse("Gustavo",2)
    hosrse3 = Horse("El caballo maravilla",3)
    hosrse4 = Horse("Superman",4)
    hosrse5 = Horse("Caballo random",5)
    hosrse6 = Horse("El mas crak",6)

    for valid in range(valids):
        race_list = []
        horse_list = [hosrse1, hosrse2, hosrse3, hosrse4,hosrse5, hosrse6]

        for race in range(races):
            race_list.append(Race(race, horse_list))

#            for race in race_list:
                
    

main()

