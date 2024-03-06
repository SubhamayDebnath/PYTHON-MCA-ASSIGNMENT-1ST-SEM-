# Write a program to check whether a triangle is valid or not, when the three angles of the
# triangle are entered through the keyboard. A triangle is valid if the sum of all the three
# angles is equal to 180 degrees
angle1=int(input("Enter the degree of angle 1:"))
angle2=int(input("Enter the degree of angle 2:"))
angle3=int(input("Enter the degree of angle 3:"))
total_angles=(angle1+angle2+angle3)
if(total_angles == 180):
    print("valid")
else:
    print("not valid")