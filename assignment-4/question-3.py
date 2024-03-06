# Write a program in python to calculate sum of Fibonacci series.

def fibonacciSeries(num):
    i=0
    n1=0
    n2=1
    sum=0
    while i < num:
        if i <= 1:
            next=i
        else:
            next=n1+n2
            n1=n2
            n2=next
        sum+=next
        i+=1
    print(f"sum of Fibonacci series is {sum}")
fibonacciSeries(12)