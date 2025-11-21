#prompt the user to enter weight & height

weight = float(input("enter your weight in kilograms: "))

height = float(input("enter your height in meters: "))

#calculate BMI

bmi = weight / (height ** 2)

#display the calculated bmi
print(" your bmi is:", bmi)
