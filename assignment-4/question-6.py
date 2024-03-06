
def sum(n):
    sum_pos = 0
    sum_neg = 0

    for i in range(n):
        num = int(input(f"Enter element {i + 1}: "))
        
        if num > 0:
            sum_pos += num
        elif num < 0:
            sum_neg += num

    print(f"Sum of positive numbers: {sum_pos}")
    print(f"Sum of negative numbers: {sum_neg}")
n = int(input("Enter the number of elements: "))
sum(n)