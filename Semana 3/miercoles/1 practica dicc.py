currency_digit = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency_input = input("Please enter a currency: ")

print(currency_digit.get(currency_input.lower(), "Currency not found"))