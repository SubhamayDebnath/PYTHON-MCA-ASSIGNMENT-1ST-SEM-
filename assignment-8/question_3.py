# 3. Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20,4:6}
# dic2={3:30, 4:40,5:2}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 36, 4: 40, 5: 52, 6: 60}

dic1={1:10, 2:20,4:6}
dic2={3:30, 4:40,5:2}
dic3={5:50,6:60}
dic4={}
for i in dic1.keys():
    dic4[i]=dic1[i]
for j in dic2.keys():
    if  j in dic4.keys():
        dic4[j]=dic4[j]+dic2[j]
    else:
        dic4[j]=dic2[j]
for k in dic3.keys():
    if  k in dic4.keys():
        dic4[k]=dic4[k]+dic3[k]
    else:
        dic4[k]=dic3[k]
print(dic4)
    
