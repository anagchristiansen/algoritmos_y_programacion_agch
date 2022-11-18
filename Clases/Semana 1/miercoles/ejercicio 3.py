deposit = float (input ("Enter the amount you would like to place:"))
profit = deposit * 0.04
year1 = deposit  + profit
profit = year1 * 0.04
year2= year1 + profit
profit= year2 * 0.04
year3 = year2 + profit
print (f"In one year you will earn {round(year1,2)}")
print (f"In two years you will earn {round(year2,2)}")
print(f"In one year you will earn {round(year1,2)}")
print(f"In three years you will earn {round(year3,2)}")