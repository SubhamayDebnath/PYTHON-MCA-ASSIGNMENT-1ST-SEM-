# Write a program in C to calculate Power(a,b) using function.
def powerNum(x,y):
    res=x
    i=1
    while(i < y):
        res=res*x
        i+=1
    return res

num=int(input("Enter the number:"))
Pow=int(input("Enter the power:"))
print(powerNum(num,Pow))

