class Vehicle:
    def __init__(self, brand1, model, color, year):
        self.__brand = brand1
        self.model = model
        self.color = color
        self.year = year

    
    def get_color(self):                      #llama al self
        return self.__brand   
   
    def print_color(self):                        #atibutos privados, Métodos públicos
        print("El color es", self.color)       