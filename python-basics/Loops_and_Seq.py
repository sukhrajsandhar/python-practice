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
