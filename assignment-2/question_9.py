# Given the length and breadth of a rectangle, write a program to find whether the area of the
# rectangle is greater than its perimeter. For example, the area of the rectangle with length = 5
# and breadth = 4 is greater than its perimeter

length=int(input("Enter the length of rectangle: "))
breadth=int(input("Enter the breadth of rectangle:"))
area=(length + breadth)
perimeter=2*(length + breadth)

if(area < perimeter):
    print("Area is greater than Perimeter")
else:
    print("Perimeter is greater than Area")

