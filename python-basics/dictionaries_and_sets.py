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
