# Creating Strings
my_str_1 = "Hello"

# Multi Line Strings
my_str_3 = """Multiline
                String"""

# Use opposite kind of quotes when creating strings with quotation marks
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

# Or you can simply use backslash (\) before the quotation marks
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

# The in operator can check if the string contains one or more chracters
my_str = "Hello world"

print("Hello" in my_str)  # True
print("hey" in my_str)  # False
print("hi" in my_str)  # False
print("e" in my_str)  # True
print("f" in my_str)  # False

# Get the length of a string
my_str = "Hello World"
print(len(my_str))  # 11

# Accessing different characters in a string
my_str = "Hello World"

print(my_str[0])  # H
print(my_str[6])  # W
