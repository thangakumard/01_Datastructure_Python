# Demonstrations of different ways to initialize defaultdict in Python
# Copy–paste friendly with clear comments

from collections import defaultdict


# -------------------------------------------------------------
# 1️⃣ Default to 0  (Perfect for frequency / counting problems)
# -------------------------------------------------------------
freq = defaultdict(int)

freq["apple"] += 1
freq["apple"] += 1
freq["banana"] += 1

print("1️⃣ defaultdict(int):", freq)
# Output → {'apple': 2, 'banana': 1}



# -------------------------------------------------------------
# 2️⃣ Default to empty list  (Great for grouping values)
# -------------------------------------------------------------
group = defaultdict(list)

group["even"].append(2)
group["even"].append(4)
group["odd"].append(1)

print("2️⃣ defaultdict(list):", group)
# Output → {'even': [2, 4], 'odd': [1]}



# -------------------------------------------------------------
# 3️⃣ Default to empty set  (Useful when you want unique values)
# -------------------------------------------------------------
unique_map = defaultdict(set)

unique_map["letters"].add('a')
unique_map["letters"].add('a')   # duplicate ignored
unique_map["letters"].add('b')

print("3️⃣ defaultdict(set):", unique_map)
# Output → {'letters': {'a', 'b'}}



# -------------------------------------------------------------
# 4️⃣ Default to empty dict  (Useful for nested dict building)
# -------------------------------------------------------------
nested_dict = defaultdict(dict)

nested_dict["user"]["name"] = "John"
nested_dict["user"]["age"] = 30

print("4️⃣ defaultdict(dict):", nested_dict)
# Output → {'user': {'name': 'John', 'age': 30}}



# -------------------------------------------------------------
# 5️⃣ Default using lambda (Custom default value)
# -------------------------------------------------------------
default_100 = defaultdict(lambda: 100)

print("5️⃣ defaultdict(lambda:100) →", default_100["x"])
# Accessing creates key 'x' with value 100
print("Now dict is:", default_100)
# Output → {'x': 100}



# -------------------------------------------------------------
# 6️⃣ Nested defaultdict (auto-creates deeper levels)
# -------------------------------------------------------------
# Two-level nested defaultdict
two_level = defaultdict(lambda: defaultdict(int))

two_level["player"]["score"] += 5
two_level["player"]["coins"] += 10

print("6️⃣ Two-level nested defaultdict:", two_level)
# Output → {'player': {'score': 5, 'coins': 10}}

# Infinite-level nesting trick
tree = lambda: defaultdict(tree)
infinite_nested = tree()

infinite_nested["a"]["b"]["c"] = 50

print("   Infinite nested defaultdict example:", infinite_nested)
# Output like {'a': {'b': {'c': 50}}}



# -------------------------------------------------------------
# 7️⃣ Default to a custom class
# -------------------------------------------------------------
class Person:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0

people = defaultdict(Person)

print("7️⃣ Custom object default:", people["p1"].name)
# Output → Unknown

people["p1"].name = "Alice"
people["p1"].age = 25

print("Updated person object:", people["p1"].name, people["p1"].age)
# Output → Alice 25
