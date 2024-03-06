# Any year is entered through the keyboard, write a program to determine whether the year is
# leap or not. Use the logical operators && and ||.

year=int(input("Enter the year that you want to check :"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0  :
    print("Leap year")
else:
    print("not leap year")