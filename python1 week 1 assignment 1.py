# Prompt the user to enter principal amount, interest rate, and time period
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in %): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the calculated simple interest
print("The simple interest is:", simple_interest)