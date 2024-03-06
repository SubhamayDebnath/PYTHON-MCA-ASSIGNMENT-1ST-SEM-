import math
x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
r=float(input("Enter the radius of circle: "))
x1=int(input("Enter the value of x1 : "))
y1=int(input("Enter the value of y1 : "))

distance=math.sqrt(math.pow((x1-x),2)+math.pow((y1-y),2))
if r == distance:
    print("same point")
elif r < distance:
    print("out of the radius")
else:
    print("in the circle ")
