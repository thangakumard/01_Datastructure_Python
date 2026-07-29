# ============================================================
# Python: Lambda Functions for Beginners
# ============================================================
# lambda arguments: expression
# A lambda is a small anonymous (unnamed) function.
# It can take any number of arguments but only one expression.
# ============================================================

# --- Basic lambda ---
square = lambda x: x ** 2
print(square(5))                   # 25

add = lambda a, b: a + b
print(add(3, 4))                   # 7

greet = lambda name: f"Hello, {name}!"
print(greet("Alice"))              # Hello, Alice!

# --- Equivalent regular function ---
def square_fn(x):
    return x ** 2

print(square_fn(5))                # 25  (same as lambda)

# ============================================================
# Where lambdas are most useful
# ============================================================

# --- sorted() with key ---
words = ["banana", "apple", "kiwi", "cherry"]

# Sort by string length
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'banana', 'cherry']

# Sort by last character
print(sorted(words, key=lambda w: w[-1]))
# ['banana', 'apple', 'kiwi', 'cherry']

# Sort list of dicts by a field
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob",   "age": 25},
    {"name": "Carol", "age": 35},
]
print(sorted(people, key=lambda p: p["age"]))
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, ...]

# --- max() / min() with key ---
print(max(words, key=lambda w: len(w)))    # banana  (longest)
print(min(words, key=lambda w: len(w)))    # kiwi    (shortest)

# --- map() with lambda ---
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)                     # [2, 4, 6, 8, 10]

# --- filter() with lambda ---
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)                       # [2, 4]

# --- Conditional expression inside lambda ---
absolute = lambda x: x if x >= 0 else -x
print(absolute(-7))                # 7
print(absolute(3))                 # 3

# --- Lambda with multiple arguments ---
power = lambda base, exp: base ** exp
print(power(2, 8))                 # 256

# ============================================================
# When NOT to use lambda
# ============================================================
# If the logic is complex or needs a name, use def instead.

# Hard to read (avoid this):
fn = lambda x: x**2 if x > 0 else 0 if x == 0 else -(x**2)

# Easier to read as a named function:
def signed_square(x):
    if x > 0:
        return x ** 2
    elif x == 0:
        return 0
    else:
        return -(x ** 2)

print(signed_square(-3))           # -9

# ============================================================
# Summary
# ============================================================
# Use case                   | Example
# ---------------------------+----------------------------------
# Simple one-liner           | lambda x: x * 2
# sorted() key               | sorted(items, key=lambda x: x[1])
# map() transformation       | map(lambda x: x+1, nums)
# filter() condition         | filter(lambda x: x>0, nums)
# max/min with key           | max(items, key=lambda x: x["score"])
