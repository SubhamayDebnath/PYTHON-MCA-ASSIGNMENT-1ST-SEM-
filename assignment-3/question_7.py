positive_count = 0
negative_count = 0
zero_count = 0

while True: 
    inp = (input("Enter a number (type exit to stop): "))
    if (inp.lower())=='exit':
        break
    else:
        num=float(inp)
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
print("\nCount of positive numbers:", positive_count)
print("Count of negative numbers:", negative_count)
print("Count of zeros:", zero_count)
