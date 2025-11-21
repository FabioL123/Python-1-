# Prompt the user to enter a positive integer
n = int(input("Enter a positive integer: "))

# Check if the number is positive
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Collatz sequence:")
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n)  # Print the last number 1 