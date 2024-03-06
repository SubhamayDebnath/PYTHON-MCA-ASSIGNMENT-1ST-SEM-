def calculateHCF(num1,num2):
    p=num1
    q=num2
    while num1 != num2:
        if num1 > num2:
            num1=num1-num2
        else:
            num2=num2-num1
    print(f"H.C.F of {p} and {q} is {num1}")

calculateHCF(25,20)