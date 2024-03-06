# . A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for
# 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after
# 30 days your membership will be cancelled. Write a program to accept the number of days
# the member is late to return the book and display the fine or the appropriate message.
days=int(input("Enter the days: "))
if days>0 and days < 5:
    fine=.50 * days
elif days > 5 and days < 10:
    fine=1*days
elif days > 10:
    fine=5*days
    if days> 30:
        print("your membership will be cancelled. \n");
print("You have to pay Rs.",fine ,"fine.");