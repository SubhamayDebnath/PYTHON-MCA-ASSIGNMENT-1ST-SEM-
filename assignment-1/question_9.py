# If a four-digit number is input through the keyboard, write a program to obtain the sum of
# the first and last digit of this number

num=int(input("Enter The number : "))
num1=(num % 10)
num4=(num // 1000) % 10
sum=(num4 + num1)
print("the sum of the first and last digit of this number :",sum);