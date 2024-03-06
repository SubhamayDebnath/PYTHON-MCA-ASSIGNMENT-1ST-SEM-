str=input("enter the String :")
count=0
vowels="AEIOUaeiou"
for ch in str:
    if ord(ch) >= 65 and ord(ch) <= 90 or ord(ch) >= 97 and ord(ch) <=122:
        if ch not in vowels:
            count+=1
print(count)

 