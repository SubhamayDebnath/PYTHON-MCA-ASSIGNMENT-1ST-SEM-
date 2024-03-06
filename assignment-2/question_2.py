# Any integer is input through the keyboard. Write a program to find out whether it is an odd
# number or even number.

num=int(input("Enter the number That your want to check:"))
if(num != 0 and num != 1):
    if(num % 2 == 0):
        print("even number")
    else:
        print("odd number")
else:
    print("Enter valid number")