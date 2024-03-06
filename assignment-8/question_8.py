#  Write a Python program to get the maximum and minimum values of a dictionary.
dic1={1:10, 2:20,3:300, 5:40,7:2}
max=0
min=dic1[1]
for i in dic1.keys():
    if dic1[i] > max:
        max=dic1[i]
    if dic1[i] < min:
        min=dic1[i]
print(f"Maximum values {max} and minimum values {min} of a dictionary")