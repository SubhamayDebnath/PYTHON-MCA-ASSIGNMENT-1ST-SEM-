# The distance between two cities (in km.) is input through the keyboard. Write a program to
# convert and print this distance in meters, feet, inches and centimeters.

distance=int(input("Enter Distance between two cities (in km): "))
distance_in_meters=distance * 1000;
distance_in_feet=distance * 3280.84;
distance_in_inches=distance * 39370.1;
distance_in_centimeters=distance * 100000;
print("Distance in meters :",distance_in_meters)
print("Distance in feet :",distance_in_feet)
print("Distance in inches :",distance_in_inches)
print("Distance in centimeters",distance_in_centimeters)