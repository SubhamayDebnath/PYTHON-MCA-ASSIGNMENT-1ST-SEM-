num=int(input("Enter the number: "))
n=0
r=0
s=0
e=0
g=0
m=False
count=0
while n < 5:
    r=num % 10
    s+=r
    if r % 2==0:
        e+=r
    g=g*10+r
    for i  in range(2,r):
        if r % i ==0:
            m=True
        if m!=True:
            count+=1
    num//=10
    n+=1
print("The sum of Digits: ",s)
print("The sum of Even Digits: ",e)
print("Reverse Number: ",g)
print("Count the prime number :",count)
