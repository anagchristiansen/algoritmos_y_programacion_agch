number= input("Please enter a number:")
if number.isnumeric ():
    number = int(number)
    if number%2 == 0:
        print (f"the number {number} is even")
    else:
        print(f"The number {number} id odd")

else:
    print("Error")