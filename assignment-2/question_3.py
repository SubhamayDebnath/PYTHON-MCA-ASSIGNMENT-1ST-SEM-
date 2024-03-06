# Any year is input through the keyboard. Write a program to determine whether the year is a
# leap year or 

year=int(input("Enter the year that you want to check :"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0  :
    print("Leap year")
else:
    print("not leap year")





