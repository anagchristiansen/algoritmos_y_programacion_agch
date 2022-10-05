
import numbers


def main ():
    number= int(input ("Please enter a number: "))
    divisor = number - 1

    if number % divisor == 0:
        number = 1
    else: print("Please enter a valid number: ")

main ()
    