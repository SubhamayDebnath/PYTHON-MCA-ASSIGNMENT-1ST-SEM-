# Write a Python script to merge two Python dictionarie
dic1={1:10, 2:20,4:6}
dic2={3:30, 6:40,5:2}
dic3={}
for i in dic1.keys():
    dic3[i]=dic1[i]
for j in dic2.keys():
    dic3[j]=dic2[j]
print(dic3)