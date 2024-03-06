# 2. Write a Python script to check whether a given key already exists in a dictionary. 
dic1={1:10, 2:20,3:30, 5:40,7:100}
key=int(input("Enter the key that you want to check: "))
if key in dic1:
    print(f'{key} is already exists in a dictionary')
else:
    print(f'{key} is not exists in a dictionary')