# . A five-digit number is entered through the keyboard. Write a program to obtain the reversed
# number and to determine whether the original and reversed numbers are equal or not.
num=int(input("Enter The number : "))
num1=(num % 10)
num2=(num // 10) % 10
num3=(num // 100) % 10
num4=(num // 1000) % 10
num5=(num // 10000) % 10
rev=((((num1 * 10 + num2) * 10 + num3) * 10 + num4) * 10 + num5)
if num == rev:
    print("the original and reversed numbers are equal")
else:
    print("the original and reversed numbers are not equal")

