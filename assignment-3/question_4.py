# Write a program to print all the ASCII values and their equivalent characters using a while
# loop. The ASCII values vary from 0 to 255[chr(110) will print ascii character of the value 110.
# ord('A') will print corresponding ASCII value of 'A']
ascii_value = 0
while ascii_value <= 255:
    print(f"ASCII Value: {ascii_value}, Character: {chr(ascii_value)}")
    ascii_value += 1
