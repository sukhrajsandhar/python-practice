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
