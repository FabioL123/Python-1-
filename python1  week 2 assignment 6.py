#ask the user to enter an amount in usd

usd = float(input("enter amount in usd:"))

#fixed exchange rate from usd to EUR

exchange_rate = 0.91  #1 usd = 0.91 EUR

#convert usd to EUR
EUR = usd * exchange_rate

# display the converted amount

print("amount in EUR:", EUR)