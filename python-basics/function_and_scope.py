# Prompting users for input
name = input("What is your name?")  # User types Sukhraj and presses enter
print("Hello", name)  # Output: Hello Sukhraj

print(int(3.14))  # 3
print(int("42"))  # 42
print(int(True))  # 1
print(int(False))  # 0


# Example custom function named hello that prints the string Hello World
def hello():
    print("Hello World")


hello()  # Hello World

# Python relies on indentation to deternmine which groups of statements belong together.


# Simple funtion that prints the sum of two numbers
def calculate_sum(a, b):
    print(a + b)


# Calling the function to sum together numbers
calculate_sum(3, 4)

# calculate_sum()  # TypeError: calculate_sum() missing 2 req positional arguments: 'a' and 'b'

# Functions also use a special return keyword to exit the function and return a value.


def calculate_sum(a, b):
    print(a + b)


my_sum = calculate_sum(3, 1)  # 4
print(my_sum)  # None


def calculate_sum(a, b):
    return a + b


my_sum = calculate_sum(3, 1)
print(my_sum)  # 4

# To correctly determine scope, Python follows the LEGB rule, which stands for the following:
# Local scope (L): Variables defined in functions or classes.
# Enclosing scope (E): Variables defined in enclosing or nested functions.
# Global scope (G): Variables defined at the top level of the module or file.
# Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.


# Local scope means that a variable declared inside a function or class can only be accessed within that function or class
def my_func():
    my_var = 10
    print(my_var)


# Calling my_func will output 10, but printing my_var outside the function will lead to a NameError.
def my_func():
    my_var = 10  # Locally scoped to my_func
    print(my_var)


my_func()  # 10

print(my_var)  # NameError: name 'my_var' is not defined


# Enclosing scope means that a function that's nested inside another function can access the variables of the function its nested within.
def outer_func():
    msg = "Hello there!"

    def inner_func():
        print(msg)

    inner_func()


outer_func()  # Hello there!


def outer_func():
    msg = "Hello there!"
    print(res)

    def inner_func():
        res = "How are you?"  # outer function can't access this
        print(msg)

    inner_func()


outer_func()  # NameError: name 'res' is not defined

# One solution to this problem


def outer_func():
    msg = "Hello there!"
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = "How are you?"
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified


outer_func()

# Output:
# Hello there!
# How are you?


# Global scope examples meaning the variable is declared outside of functions and classes which can be accessed from anywhere
my_var = 100


def show_var():
    print(my_var)


show_var()  # 100
print()  # 100

# You can also use the global keyword to make a variable globally accesible from inside a function
my_var_1 = 7


def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)


show_vars()  # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2)  # 10

my_var = 10  # A global variable


def change_var():
    global my_var  # Allows modification of a global variable
    my_var = 20


change_var()

print(my_var)  # my_var is now modified globally to 20


print(str(45))  # '45'
print(type(3.14))  # <class 'float'>
print(isinstance(3, str))  # False
