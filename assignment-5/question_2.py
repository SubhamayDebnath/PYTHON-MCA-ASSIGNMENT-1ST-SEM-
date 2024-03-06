# Write a program to take binary input numbers and convert it to an integer without 
# using int() function.
a=input("Enter The string of digits:")
num=0
for i in a:
    num=num*10 + (ord(i)-48) 
j=0
decimal=0
while(num != 0):
    dec=num%10
    decimal=decimal + dec * pow(2,j)
    num=num//10
    j+=1
print(decimal)
