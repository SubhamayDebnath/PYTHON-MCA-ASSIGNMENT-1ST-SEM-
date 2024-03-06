str=input("Enter the string :")
str2=""
for i  in str:
    str2=str2 + chr(ord(i)-32)
print(str2)
