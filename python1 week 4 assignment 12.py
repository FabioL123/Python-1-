# Prompt the user to enter the number of rows
rows = int(input("Enter the number of rows: "))

# Print a right triangle pattern of asterisks
for i in range(1, rows + 1):
    print("*" * i)