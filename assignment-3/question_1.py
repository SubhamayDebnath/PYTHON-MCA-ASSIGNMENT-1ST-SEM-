# Write a program to calculate overtime pay of 10 employees. Overtime is paid at the rate of Rs.
# 12.00 per hour for every hour worked above 40 hours. Assume that employees do not work for
# fractional part of an hour
workers=10
for i in range(1,workers+1):
    print("Employee no:",i)
    work_hour=int(input("Enter the working hour of employee:"))
    if work_hour > 40:
        over_time=work_hour-40;
        over_time_amount=over_time*12.00
        print("Overtime Payment Of employee is : ",over_time_amount)
    else:
        print("employees do not work for fractional part of an hour")