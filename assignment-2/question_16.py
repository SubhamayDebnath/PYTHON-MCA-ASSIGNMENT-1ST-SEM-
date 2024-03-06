# If the three sides of a triangle are entered through the keyboard, write a program to check
# whether the triangle is isosceles, equilateral, scalene or right angled triangle.
angle1=int(input("Enter the 1st angle: "))
angle2=int(input("Enter the 2nd angle: "))
angle3=int(input("Enter the 3rd angle: "))
if angle1 == angle2 and angle2 == angle3:
    print("The Given Triangle is equilateral")
elif angle1 == angle2 or angle2 == angle3 or angle3== angle1:
    print("The given Triangle is isosceles")
elif pow(angle1,2)+pow(angle2,2)==pow(angle3,2) or pow(angle1,2)+pow(angle3,2)==pow(angle2,2) or pow(angle2,2)+pow(angle3,2)==pow(angle1,2):
    print("The given Triangle is right angled triangle")
else:
    print("The given Triangle is scalene")