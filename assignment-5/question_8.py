# Python program to check if a string has at least one letter and one number
str=input("Enter the string :")
m=0
n=0
p=0
for i in str:
    if i >= 'A' and i <= 'Z' or i >='a' and i <= 'z':
        m+=1
    elif  i >= '0' and i <= '9':
        n+=1
    elif i == " ":
        p+=1

print(f"{str} has : {m} no. alphabets , {n} no. numbers and {p} no. space")