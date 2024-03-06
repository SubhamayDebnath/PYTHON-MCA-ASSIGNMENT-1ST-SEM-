
##Given three points (x1, y1), (x2, y2) and (x3, y3), write a program to check if all the three
##points fall on one straight line.
x1=int(input("Enter the value of x1:"))
y1=int(input("Enter the value of y1:"))
x2=int(input("Enter the value of x2:"))
y2=int(input("Enter the value of y2:"))
x3=int(input("Enter the value of x3:"))
y3=int(input("Enter the value of y3:"))

m=(y2-y1)//(x2-x1)
n=(y3-y2)//(x3-x2)

if m==n:
    print("the three points fall on one straight line")
else:
    print("the three points not fall on one straight line")
