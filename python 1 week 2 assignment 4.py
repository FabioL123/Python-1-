# prompt the user to enter the coordinates of the first point

x1 = float( input( "enter x1:"))

y1 = float( input( "enter y1:"))

#prompt the user to enter the coordinates of the second point

x2 = float(input("enter x2: "))

y2 = float( input(" enter y2: "))


#calculate the distance using the distance formula

distance = (x2 -x1) **2 + (y2 - y1) **2

#display the result

print("the distance between the two points is:" ,distance)
