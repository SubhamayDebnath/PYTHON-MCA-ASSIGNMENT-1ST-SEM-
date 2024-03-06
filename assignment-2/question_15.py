# If the three sides of a triangle are entered through the keyboard, write a program to check
# whether the triangle is valid or not. The triangle is valid if the sum of two sides is greater
# than the largest of the three sides

angle1=int(input("Enter the 1st angle of triangle: "))
angle2=int(input("Enter the 2nd angle of triangle: "))
angle3=int(input("Enter the 3rd angle of triangle: "))
total_angle=angle1+angle2+angle3
if total_angle==180:
    if((angle3+angle2) > angle1 or (angle2+angle3) > angle2 or (angle2 + angle1) > angle3):
        print("Valid Triangle")
    else:
        print("not Valid Triangle")
else:
    print("Please enter valid triangle")