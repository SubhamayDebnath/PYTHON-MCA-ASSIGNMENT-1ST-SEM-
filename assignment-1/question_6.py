# Two numbers are input through the keyboard into two locations C and D. Write a program to
# interchange the contents of C and D.

c = int(input("Enter The 1st number :"))
d = int(input("Enter The 2nd number :"))
print("two number before interchange ", c , d)
temp=c
c=d
d=temp
print("two number after interchange ", c , d)