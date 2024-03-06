# The length & breadth of a rectangle and radius of a circle are input through the keyboard.
# Write a program to calculate the area & perimeter of the rectangle, and the area &
# circumference of the circle.


print("For rectangle")
length=int(input("Enter The length of rectangle :"))
breadth=int(input("Enter The Breadth of rectangle :"))
area_of_rectangle=length*breadth
perimeter_of_rectangle=(length + breadth)*2
print("Area of rectangle",area_of_rectangle)
print("Perimeter of rectangle",perimeter_of_rectangle)

print("For Circle")

radius=int(input("Enter The radius of circle :"))
area_of_circle=(3.14 * radius * radius)
circumference_of_the_circle=(2 * 3.14 * radius)
print("Area of Circle",area_of_circle)
print("Circumference of the circle",circumference_of_the_circle)