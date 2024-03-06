# Write a program uppercase Half String.
str=input("Enter the string :")
# method 1
halfStr=len(str)//2 
# upperHalf=str[:halfStr].upper()
# print(upperHalf+str[halfStr:])
# method 2
str2=""
str3=""
for i in range(halfStr):
    str2+=str[i]
for j in range(halfStr,len(str)):
    str3+=str[j]
print(str2.upper()+str3)