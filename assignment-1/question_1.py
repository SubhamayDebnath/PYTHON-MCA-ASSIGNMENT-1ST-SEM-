# Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic
# salary, and house rent allowance is 20% of basic salary. Write a program to calculate his
# gross salary

basic_salary=int(input("Enter Your Basic Salary: "))
dearness_allowance=0.4*basic_salary
house_rent_allowance=0.2*basic_salary
gross_salary=basic_salary+dearness_allowance+house_rent_allowance
print("Gross Salary: ",gross_salary)
