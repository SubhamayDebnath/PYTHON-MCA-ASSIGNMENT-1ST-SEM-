# Import the 'pprint' function from the 'pprint' module to pretty-print dictionaries.
from pprint import pprint

# Create a dictionary 'dict_nums' with keys 'x', 'y', and 'z', and lists of numbers as values.
dict_nums = dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40)))

# Pretty-print the 'dict_nums' dictionary to improve readability.
pprint(dict_nums)

# Print the value at the 4th index of the 'x', 'y', and 'z' lists in 'dict_nums'.
print(dict_nums["x"][4])
print(dict_nums["y"][4])
print(dict_nums["z"][4])

# Iterate through the key-value pairs in 'dict_nums' and print the key and its associated value.
for k, v in dict_nums.items():
    print(k, "has value", v)
