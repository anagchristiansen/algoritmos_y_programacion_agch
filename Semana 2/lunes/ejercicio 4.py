print("Welcome to Bella Napoli")
option = input("Please eneter an option: \n1-Vegetarian \n2-Non Venetarian \n")
if option.isnumeric():
    option=int(option)
    if option == 1:
        ingredient = input("Please eneter ingredient: \n1-Pimiento \n2-Tofu")
        if ingredient== "1":
            ingredient = "Pimiento"
        else:ingredient
