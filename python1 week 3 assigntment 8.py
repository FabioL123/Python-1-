# Ask the user to enter marks for three subjects
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

# Calculate the average
average = (mark1 + mark2 + mark3) / 3

# Determine the grade based on average
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display the grade
print("Your grade is:", grade) 