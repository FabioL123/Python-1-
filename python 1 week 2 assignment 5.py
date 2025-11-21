#prompt the user to enter a time duration in hours

hours = float(input("enter time in hours:"))

#convert hours to minutes and seconds

minutes = hours * 60
seconds = hours * 3600

# display the converted time

print("time in minutes:", minutes)
print("time in seconds:", seconds)

