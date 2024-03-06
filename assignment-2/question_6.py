# If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to
# determine the youngest of the three.
ram_age=int(input("Enter the age of Ram :"))
shyam_age=int(input("Enter the age of Shyam :"))
ajay_age=int(input("Enter the age of Ajay :"))
if(ram_age < shyam_age and ram_age < ajay_age ):
    print("Ram is the youngest of the three")
elif(shyam_age < ram_age and shyam_age < ajay_age):
    print("Shyam is the youngest of the three")
elif(ajay_age < ram_age and ajay_age < shyam_age):
    print("Ajay is the youngest of the three")
else:
    print("same age")