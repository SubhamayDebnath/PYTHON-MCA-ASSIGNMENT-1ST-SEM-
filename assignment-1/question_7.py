# If a five-digit number is input through the keyboard, write a program to calculate the sum of
# its digits.(Hint: Use the modulus operator ‘%’)

num=int(input("Enter The number : "))
num1=(num % 10)
num2=(num // 10) % 10
num3=(num // 100) % 10
num4=(num // 1000) % 10
num5=(num // 10000) % 10
sum=( num1 + num2 + num3 + num4 + num5)
print("the sum of its digits :" , sum)