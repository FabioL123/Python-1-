# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Classify the age
if age < 18:
    category = "Minor"
elif age <= 65:
    category = "Adult"
else:
    category = "Senior citizen"

# Display the category
print("You are classified as:", category)  