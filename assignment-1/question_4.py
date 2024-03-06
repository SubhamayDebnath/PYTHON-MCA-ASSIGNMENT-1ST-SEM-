# Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program
# to convert this temperature into Centigrade degrees

fahrenheit=int(input("Enter the Temperature of a city in fahrenheit :"))
centigrade=(fahrenheit-32)*5/9
answer=round(centigrade, 2)
print("The Temperature of a city in centigrade:",centigrade)