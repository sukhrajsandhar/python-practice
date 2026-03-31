# dictionary = {key1: value1, key2: value2}
# Pizza example:
pizza = {
    "name": "Margherita Pizza",
    "price": 8.9,
    "calories_per_slice": 250,
    "toppings": ["mozzarella", "basil"],
}

pizza = dict(
    [
        ("name", "Margherita Pizza"),
        ("price", 8.9),
        ("calories_per_slice", 250),
        ("toppings", ["mozzarella", "basil"]),
    ]
)

# dictionary[key]
pizza["name"]
# Output: 'Margherita Pizza'

pizza["name"] = "Margherita"
print(pizza["name"])  # 'Margherita'

# dictionary.get(key, default)

pizza.get("toppings", [])  # ['mozzarella', 'basil']

pizza.keys()
# dict_keys(['name', 'price', 'calories_per_slice'])

pizza.values()
# dict_values(['Margherita Pizza', 8.9, 250])

pizza.items()
# dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])

pizza.pop("price", 10)
# pizza.pop("total_price")  # KeyError

pizza.popitem()  # In python 3.7 version removes the last inserted item.

pizza.update({"price": 15, "total_time": 25})
"""{
    'name': 'Margherita Pizza',
    'price': 15,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil'],
    'total_time': 25
}"""
# New updated dictionary

products = {
    "Laptop": 990,
    "Smartphone": 600,
    "Tablet": 250,
    "Headphones": 70,
}

for price in products.values():
    print(price)
"""
Output:
        990
        600
        250
        70
"""

for product in products.keys():
    print(product)

# Or

for product in products:
    print(product)

"""
Laptop
Smartphone
Tablet
Headphones
"""

for product in products.items():
    print(product)
"""
('Laptop', 990)
('Smartphone', 600)
('Tablet', 250)
('Headphones', 70)
"""

products = {
    "Laptop": 990,
    "Smartphone": 600,
    "Tablet": 250,
    "Headphones": 70,
}

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

# {"Laptop": 792, "Smartphone": 480, "Tablet": 200, "Headphones": 56}

for product in enumerate(products):
    print(product)

"""
(0, 'Laptop')
(1, 'Smartphone')
(2, 'Tablet')
(3, 'Headphones')
"""

for price in enumerate(products.values()):
    print(price)

"""
(0, 990)
(1, 600)
(2, 250)
(3, 70)
"""

for index, price in enumerate(products.values()):
    print(index, price)
"""
0 990
1 600
2 250
3 70
"""

for index, product in enumerate(products.items()):
    print(index, product)
"""
0 ('Laptop', 990)
1 ('Smartphone', 600)
2 ('Tablet', 250)
3 ('Headphones', 70)
"""

for index, product in enumerate(products.items(), 1):
    print(index, product)
"""
1 ('Laptop', 990)
2 ('Smartphone', 600)
3 ('Tablet', 250)
4 ('Headphones', 70)
"""

# Sets in python
my_set = {1, 2, 3, 4, 5}

set()  # Set
{}  # Dictionary

my_set.add(6)
# Updated set: {1, 2, 3, 4, 5, 6}

# But if you try to add an element that's already in the set then only one will be kept.
my_set.add(5)
# Updated set: {1, 2, 3, 4, 5, 6}

my_set.remove(4)
my_set.discard(4)
# .remove() will raise a KeyError if the element is not found, while the .discard() method will not.

# .clear() method removes all the elements from the set.
my_set.clear()

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set))  # False
print(my_set.issuperset(your_set))  # False

print(my_set.isdisjoint(your_set))  # False
# ^ Basically checks if both sets are unique to each other

my_set | your_set  # {1, 2, 3, 4, 5, 6}
# "|" returns a new set with all the elements from both sets

my_set & your_set  # {2, 3, 4}
# "&" return a new set with only the elements that the sets have in common.

my_set - your_set  # {1, 5}
# returns a new set with elements only the first set has

my_set ^ your_set  # {1, 5, 6}
# returns a new set with elements that are only in 1 or the other but not in both.
