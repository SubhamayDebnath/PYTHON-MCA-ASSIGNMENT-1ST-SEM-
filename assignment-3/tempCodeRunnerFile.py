# Two numbers are entered through the keyboard. Write a program to find the value of one
# number raised to the power of another.
num = int(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))
result = 1
for i in range(1,exp+1):
    result*=num
print(result)