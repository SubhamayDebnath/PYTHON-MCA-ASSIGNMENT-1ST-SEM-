decimal_number = int(input("Enter a decimal number: "))
result = ""
if decimal_number == 0:
    result = "0"
else:
    while decimal_number > 0:
        remainder = decimal_number % 8
        result = str(remainder) + result
        decimal_number = decimal_number // 8

print(f"The octal equivalent is: {result}")
