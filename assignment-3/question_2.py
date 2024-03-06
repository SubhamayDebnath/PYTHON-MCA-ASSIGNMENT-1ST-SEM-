# Write a program to find the factorial value of any number entered through the keyboard.
num=int(input("Enter a number to find its factorial:"))
if num > 0:
    fact=1
    for i in range(1,num+1):
        fact*=i
    print("Factorial of ",num,"is ",fact)
else:
    print("Please enter positive number")
