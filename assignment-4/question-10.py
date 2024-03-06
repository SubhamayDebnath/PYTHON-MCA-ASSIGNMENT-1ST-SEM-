# Write a program in python to calculate factorial of a natural number

def factorialOfNaturalNumber(num):
    i=1
    fact=1
    while i <= num:
        fact*=i
        i+=1
    print(f"Factorial of natural number is {fact}")
factorialOfNaturalNumber(5)