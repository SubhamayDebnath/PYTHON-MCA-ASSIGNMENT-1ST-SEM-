# According to the Gregorian calendar, it was Monday on the date 01/01/1900. If any year is
# input through the keyboard write a program to find out what is the day on 1 st January of
# this year.

year=int(input("Enter the year:"))
year=(year-1)-1900
leap_year=year//4
total_year=(year-leap_year)
total_days=(total_year*365)+(leap_year * 366)+1
day=total_days % 7
if(day==0):
    print("mon")
elif(day==1):
    print("tue")
elif(day==2):
    print("wed")
elif(day==3):
    print("thu")
elif(day==4):
    print("Fri")
elif(day==5):
    print("Sat")
elif(day==6):
    print("Sun")
