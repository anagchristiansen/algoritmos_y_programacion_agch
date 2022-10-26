import random

class Race:
    def __init__(self, number, horses_list):
        
        self.number = number
        horses_list = horses_list

    def start_race(self):
        print("PARTIDAAAA!!\n")

    def choose_winner(self, horses):
        print("The winner is", random.choice(horses).name)