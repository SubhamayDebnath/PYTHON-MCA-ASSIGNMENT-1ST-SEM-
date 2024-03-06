# WAP to calculate the length of a string, avoid space
str=input("Enter the string :")
# method 1
# str2=str.replace(" ","")
# print(len(str2))

#method 2
str3=""
for i in str:
    if(i != " "):
        str3+=i
count=0
for j in str3:
    count+=1
# print(len(str3))
print(count)