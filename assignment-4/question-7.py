# Write a program in python to check whether an inputted number is palindrome.

def checkPalindrome(num):
    temp=num
    rev=0
    while(num > 0):
        dig=num % 10
        rev=rev*10+dig
        num=num // 10
    if rev == temp :
        print(f"{temp} is palindrome number")
    else:
        print(f"{temp} is not palindrome number")
checkPalindrome(12356)