# Write a program to least Frequent Character in String

input_string = "i need paisa"
char_frequency = {}

for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

least_frequent_char = min(char_frequency, key=char_frequency.get)

print(f"The least frequent character in '{input_string}' is: {least_frequent_char}")
