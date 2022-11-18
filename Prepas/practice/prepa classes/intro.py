class Employee:
    
    num_emoployee = 0
    raise_amount = 1.04

    
    def __init__(self, firstName: str, lastName: str, pay: int ):
        self.firstName = firstName
        self.lastName = lastName
        self.email = f"{firstName.lower()}.{lastName.lower()}@correo.unimet.edu.ve"
        self.pay = pay

    def full_name(self):
        return f"{self.firstName} {self.lastName}"

    def rais_amount(self):
        self.pay = int(self.pay * self.raise_amount)

    

    print(__dict__)                   #imprime la informacion de esa variable, si uso print __dict__ 
                                            # regresa un diccionario con la informacion de empleado. sino dvuelve un espacio en la memoria

