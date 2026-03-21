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

print(my_str[-1])  # d
print(my_str[-2])  # l

# Strings are immutable data types in Python.
# Meaning you can reassign a different string to a variable.
greeting = "hi"
greeting = "hello"
print(greeting)  # hello

# But cannot directly modify a string
greeting = "hi"
# greeting[0] = "H"  # TypeError

# String Concatination
my_str_1 = "Hello"
my_str_2 = "World"
str_plus_str = my_str_1 + " " + my_str_2
print(str_plus_str)  # Hello World

# But you will get a Type Error when you try to concatenate a string with a number.
name = "John Doe"
age = 26

# name_and_age = name + age
# print(name_and_age)  # Type Error: can only concatenate string (not "not")

# To fix this you can covert the number into a string with the built-in str() function
name = "John Doe"
age = 26

name_and_age = name + str(age)
print(name_and_age)  # John Doe26

# One way of preforming both concatenation and assignment in one step (+=)
name_and_age = name  # Start with the name
name_and_age += str(age)

print(name_and_age)  # John Doe26

# Using F strings to embed variables or expressions using {} curly braces.
name = "John Doe"
age = 26
name_and_age = f"My name is {name} and I am {age} years old"
print(name_and_age)  # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f"The sum of {num1} and {num2} is {num1 + num2}")  # The sum of 5 and 10 is 15

# Note that we dont need to convert non string types with the str() function.
# Variables are are converted under the hood into a string during the interpolation process.

# The process of inserting variables and expressions into a string is called string interpolation.


# String slicing
# string[start:stop]

my_str = "Hello World"
print(my_str[1:4])  # ell

# stop index is non-inclusive, so [1:4] just extracted characters from index 1 and up to but not including the char at index 4.

my_str = "Hello World"
print(my_str[:7])  # Hello w

# Extracts starting from 0 till 1 char before index 7

print(my_str[8:])  # rld
print(my_str)  # Hello world

# Slicing doesnt modify the original string.

print(my_str[:])  # Hello World
# Extracts the whole string.

# Optional Parameter for step which is used to specify the increment between each index in the slice.
# string[start:stop:step]

my_str = "Hello World"
print(my_str[0:11:2])  # Hlowrd
# Extracts every second character.

print(my_str[::-1])  # dlrow olleH


# Common String Methods
# upper() Return a new string with all characters converted to uppercase.
my_str = "Hello World"
uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD
# lower() Return a new string with all characters converted to lowercase.
lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world
# strip() Return a new string with the speicified leading and trailing characters removed. If no argument passed it removes leading and trailing whitespace.
my_str = "  hello world  "
trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # hello world
# replace(old, new) Returns a new string with all occurences of old replaced by new.
replaced_my_str = my_str.replace("hello", "hi")
print(replaced_my_str)  # hi world
# split(separator) Splits a string on a specified separator into a list of strings. If no separator specified, it splits on whitespace.
split_words = my_str.split()
print(split_words)  # ["hello", "world"]
# join(iterable) Joins elements of an iterable into a string with a separator.
my_list = ["hello", "world"]

joined_my_str = " ".join(my_list)
print(joined_my_str)  # hello world

# startswith(prefix) Returns a boolean indicating if a string starts with the specified prefix.
starts_with_hello = my_str.startswith("hello")
print(starts_with_hello)  # True

ends_with_world = my_str.endswith("world")
print(ends_with_world)  # True

# find (substring): Returns the index of the first occurence of substring, or -1 if its doesn't find one.
world_index = my_str.find("world")
print(world_index)  # 6

# count(substring) Returns the number of times a substring appears in a string.
o_count = my_str.count("o")
print(o_count)  # 2

capitalized_my_str = (
    my_str.capitalize()
)  # returns a new string with capitaized first char and other chars lowercased.
print(capitalized_my_str)  # Hello world

is_all_upper = my_str.isupper()
print(is_all_upper)  # False

my_str = "hello world"

is_all_lower = my_str.islower()
print(is_all_lower)  # True
