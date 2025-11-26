def is_prime(number):
    # Prime numbers must be greater than 1
    if number <= 1:
        return False

    # Check for factors
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


# Asking the user for input
num = int(input("Enter a positive integer: "))

# Displaying the result
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")