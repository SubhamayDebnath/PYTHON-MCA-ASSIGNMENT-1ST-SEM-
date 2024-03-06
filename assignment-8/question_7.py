# Write a Python program to map two lists into a dictionary. 
dic1=[6,2,3,100]
dic2=["Subhamay","Uchchhas","Sudipta","hello"]
dic3={}
n=0
for i in dic1:
    dic3[i]=i
for j in dic1:
    dic3[j]=dic2[n]
    n+=1
print(dic3)
