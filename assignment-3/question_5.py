# Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each
# digit of the number is equal to the number itself, then the number is called an Armstrong
# number. For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )

for num in range(1, 501):
    num_digits = len(str(num))
    temp = num
    sum_cubes = 0
    while temp > 0:
        digit = temp % 10
        sum_cubes=sum_cubes + digit ** num_digits
        temp =temp // 10
    if num == sum_cubes:
        print(f"Armstrong number: {num}")

