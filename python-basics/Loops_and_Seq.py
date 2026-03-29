cities = ["Los Angeles", "London", "Tokyo"]
cities[0]  # Los Angelas
cities[-1]  # Tokyo

developer = "Jessica"
list(developer)  # ['J', 'e', 's', 's', 'i', 'c', 'a']

numbers = [1, 2, 3, 4, 5]
len(numbers)  # 5

programming_languages = ["Python", "Java", "C++", "Rust"]
programming_languages[0] = "JavaScript"
print(programming_languages)  # ['JavaScript', 'Java', 'C++', 'Rust']

programming_languages = ["Python", "Java", "C++", "Rust"]
programming_languages[10] = "JavaScript"

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list assignment index out of range
"""

developer = ["Jane Doe", 23, "Python Developer"]
del developer[1]
print(developer)  # ['Jane Doe', 'Python Developer']

programming_languages = ["Python", "Java", "C++", "Rust"]

"Rust" in programming_languages  # True
"JavaScript" in programming_languages  # False

developer = ["Alice", 25, ["Python", "Rust", "C++"]]
developer[2]  # ['Python', 'Rust', 'C++']
developer[2][1]  # 'Rust'

developer = ["Alice", 34, "Rust Developer"]
name, age, job = developer

print(name)  # 'Alice'
print(age)  # 34
print(job)  # 'Rust Developer'

developer = ["Alice", 34, "Rust Developer"]
name, *rest = developer

# If you need to collect any remaining elements from a list, you can use the asterisk (*) operator like this:
print(name)  # 'Alice'
print(rest)  # [34, 'Rust Developer']

developer = ["Alice", 34, "Rust Developer"]
name, age, job, city = developer

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
"""
desserts = ["Cake", "Cookies", "Ice Cream", "Pie", "Brownies"]
desserts[1:4]  # ['Cookies', 'Ice Cream', 'Pie']

numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2]  # [2, 4, 6]

# Append method allows you to add an item at the end of a list
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers.append(even_numbers)
print(numbers)  # [1, 2, 3, 4, 5, [6, 8, 10]]

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers.extend(even_numbers)
print(numbers)  # [1, 2, 3, 4, 5, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)  # insert's 2.5 at index 2

print(numbers)  # [1, 2, 2.5, 3, 4, 5]


numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)  # Removes the first occurence of 50

print(numbers)  # [10, 20, 30, 40, 50]

numbers = [1, 2, 3, 4, 5]
numbers.pop(1)  # The number 2 is returned

numbers = [1, 2, 3, 4, 5]
numbers.pop()  # The number 5 is returned


numbers = [1, 2, 3, 4, 5]
numbers.clear()

print(numbers)  # []

numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers)  # [1, 2, 19, 35, 41, 67]


numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(
    numbers
)  # used to sort and makes new list instead of modifying original

print(numbers)  # [19, 2, 35, 1, 67, 41]
print(sorted_numbers)  # [1, 2, 19, 35, 41, 67]

numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers)  # [1, 2, 3, 4, 5, 6]

programming_languages = ["Rust", "Java", "Python", "C++"]
programming_languages.index("Java")  # 1

programming_languages = ["Rust", "Java", "Python", "C++"]
programming_languages.index("JavaScript")

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'JavaScript' is not in list
"""

developer = ("Alice", 34, "Rust Developer")  # Python tuples

programming_languages = ("Python", "Java", "C++", "Rust")
programming_languages[0] = "JavaScript"

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'tuple' object does not support item assignment
"""

developer = ("Alice", 34, "Rust Developer")
developer[1]  # 34

numbers = (1, 2, 3, 4, 5)
numbers[-2]  # 4

numbers = (1, 2, 3, 4, 5)
numbers[7]

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list index out of range
"""

developer = "Jessica"
tuple(developer)  # ('J', 'e', 's', 's', 'i', 'c', 'a')

programming_languages = ("Python", "Java", "C++", "Rust")

"Rust" in programming_languages  # True
"JavaScript" in programming_languages  # False

developer = ("Alice", 34, "Rust Developer")
name, age, job = developer

print(name)  # 'Alice'
print(age)  # 34
print(job)  # 'Rust Developer'

developer = ("Alice", 34, "Rust Developer")
name, *rest = developer

print(name)  # 'Alice'
print(rest)  # [34, 'Rust Developer']

desserts = ("cake", "pie", "cookies", "ice cream")
desserts[1:3]  # ('pie', 'cookies')

developer = ("Jane Doe", 23, "Python Developer")
del developer[
    1
]  # If you need to remove an item from a tuple, that isn't possible because tuples are immutable.

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: "tuple" object doesn't support item deletion
"""

programming_languages = ("Rust", "Java", "Python", "C++", "Rust")
programming_languages.count("Rust")  # 2

programming_languages = ("Rust", "Java", "Python", "C++", "Rust")
programming_languages.count("JavaScript")  # 0

# programming_languages.count()

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: tuple.count() takes exactly one argument (0 given)
"""

programming_languages = ("Rust", "Java", "Python", "C++", "Rust", "Python")
programming_languages.index("Python", 3)  # 5
# Here we are starting the search at index 3 because Python shows up twice in our tuple

programming_languages.index("Python", 2, 5)  # 2
# Here we are starting the search at index 2 but stopped it at index 5 (not including index 5 while searching)

numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers)  # [2, 3, 7, 13, 18, 45, 67, 78]

programming_languages = ("Rust", "Java", "Python", "C++", "Rust", "Python")
sorted(programming_languages, key=len)

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

programming_languages = ("Rust", "Java", "Python", "C++", "Rust", "Python")

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']

# Loops -------------------------------------- Below

programming_languages = ["Rust", "Java", "Python", "C++"]

for language in programming_languages:
    print(language)

# ^ Will print out the entire list, Make sure of your indentation

for char in "code":
    print(char)

# Out put will be each character on a new line.

categories = ["Fruit", "Vegetable"]
foods = ["Apple", "Carrot", "Banana"]

for category in categories:
    for food in foods:
        print(category, food)

# Output:
# Fruit Apple
# Fruit Carrot
# Fruit Banana
# Vegetable Apple
# Vegetable Carrot
# Vegetable Banana

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-5): "))
    if guess != secret_number:
        print("Wrong! Try again.")

print("You got it!")

developer_names = ["Jess", "Naomi", "Tom"]

for developer in developer_names:
    if developer == "Naomi":
        break
    print(developer)  # Only Jess is printed

developer_names = ["Jess", "Naomi", "Tom"]

for developer in developer_names:
    if developer == "Naomi":
        continue
    print(developer)

# Continue skips the second iteration of the loop so only Jess and Tom are printed

words = ["sky", "apple", "rhythm", "fly", "orange"]

for word in words:
    for letter in word:
        if letter.lower() in "aeiou":
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")


# What Are Ranges and How Can You Use Them in a Loop?
# range(start, stop, step)

# Example for sequence of itegers between 1 and 4:
for num in range(1, 5):
    print(num)

# Sequence of integers between 2 and 10 in increments of 2
for num in range(2, 11, 2):
    print(num)

# If you dont provide any arguments to range(), then you'll get a TypeError
# The range() function only accepts integers as arguments, so if you enter a float value then you'll get a TypeError

for num in range(40, 0, -10):
    print(num)

numbers = list(range(2, 11, 2))
print(numbers)  # [2, 4, 6, 8, 10]

languages = ["Spanish", "English", "Russian", "Chinese"]

languages = ["Spanish", "English", "Russian", "Chinese"]

index = 0

for language in languages:
    print(f"Index {index} and language {language}")
    index += 1  # Keeps track of each index

languages = ["Spanish", "English", "Russian", "Chinese"]

list(enumerate(languages))  # Easier way of tracking
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

languages = ["Spanish", "English", "Russian", "Chinese"]

for index, language in enumerate(languages):
    print(f"Index {index} and language {language}")

# The enumerate() function also accepts an optional start argument that specifies the starting value for the count.
languages = ["Spanish", "English", "Russian", "Chinese"]

for index, language in enumerate(languages, 1):
    print(f"Index {index} and language {language}")


developers = ["Naomi", "Dario", "Jessica", "Tom"]
ids = [1, 2, 3, 4]

list(zip(developers, ids))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]
