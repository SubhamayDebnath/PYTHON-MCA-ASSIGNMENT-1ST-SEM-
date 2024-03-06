# # Write a program to remove all duplicates from a given string in Python, keeping the 
# # first character only
# # str=input("Enter the string: ")
# # str2=""
# # for i in str:
# #     if i not in str2:
# #         str2+=i
# # print(str2)
# string = "hello world"
# print(string)
# # Create a dictionary to store character frequencies
# char_freq = {}

# # Count the frequency of each character in the string
# for char in string:
#     if char in char_freq:
#         char_freq[char] += 1
#     else:
#         char_freq[char] = 1

# # Find characters with odd frequencies
# odd_freq_chars = [char for char, freq in char_freq.items() if freq % 2 != 0]

# print("Characters with odd frequencies in the string:")
# for char in odd_freq_chars:
#     print(char)
