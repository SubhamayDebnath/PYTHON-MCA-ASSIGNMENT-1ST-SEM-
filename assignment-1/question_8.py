# If a five-digit number is input through the keyboard, write a program to reverse the number.

num=int(input("Enter The number : "))
num1=(num % 10)
num2=(num // 10) % 10
num3=(num // 100) % 10
num4=(num // 1000) % 10
num5=(num // 10000) % 10
rev=((((num1 * 10 + num2) * 10 + num3) * 10 + num4) * 10 + num5)
print("Reverse The Number :",rev);
