# Write a program to accept the strings which contain all vowels

str=input('Enter the string: ')
vowels="AEIOUaeiou"
str2=""
for i in str:
    for j in vowels:
        if i == j:
            str2+=i
if str2==str:
    print("the strings which contain all vowels")
else:
    print("the strings which doesn't contain all vowels")
