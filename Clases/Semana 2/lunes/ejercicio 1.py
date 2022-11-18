num1= input("Please enter  number: ")
num2= input("Please enter  number: ")
is_valid = True

if num1.isnumeric():
    num1= float(num1)
else:
    is_valid= True   

if num2.isnumeric():
    num2= float(num2)
else:
    is_valid= False

print(num1 / num2)
if is_valid:
    if num2 == 0:
        print("Error")

