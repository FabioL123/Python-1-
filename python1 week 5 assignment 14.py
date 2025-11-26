
def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

# Ask the user for input
b = int(input("Enter the base: "))
e = int(input("Enter the exponent: "))

# Display the result
print("Result:", power(b, e))