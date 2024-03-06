# Write a program to capitalize the first and last character of each word in a string

str=input("Enter the string :")
# firstStrChar=str[0:1].upper()
# lastStrChar=str[-1:].upper()
# str2=str.replace(str[0],'')
# str3=str2.replace(str2[len(str2)-1],'')
# print(firstStrChar+str3+lastStrChar)
firstChar=str[0].upper()
lastChar=str[len(str)-1].upper()
str2=''
for i in range(1,(len(str)-1)):
    str2+=str[i]
str3=firstChar+str2+lastChar
print(str3)