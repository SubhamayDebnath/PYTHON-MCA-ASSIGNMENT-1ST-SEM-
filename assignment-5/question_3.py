# WAP to remove i^th character of a string
str=input('Enter the string :')
indexOfString=(input("Enter the character of string that you want to remove: "))
# method 1
# result=str.replace(indexOfString,'')
# print(result)
# method 2
str1=""
for i in str:
    if i != str[str.index(indexOfString)]:
        str1+=i
print(str1)
