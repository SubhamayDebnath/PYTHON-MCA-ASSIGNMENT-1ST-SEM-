# Write a program to count the Number of matching characters in a pair of string.
str=input("Enter the first string: ")
str2=input("Enter the second string: ")
str3=""
count=0
for i in str:   
    if i in str2 and i not in str3:
        str3+=i
        count+=1
print(f"The matching characters in a pair of string : {str3}")
print(f"the Number of matching characters in a pair of string : {count}")