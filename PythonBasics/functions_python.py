# ============================================================
# Python: Functions for Beginners
# ============================================================

# --- Basic function ---
def greet():
    print("Hello, World!")

greet()                        # Hello, World!

# --- Function with parameters ---
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")            # Hello, Alice!

# --- Function with return value ---
def add(a, b):
    return a + b

result = add(3, 5)
print(result)                  # 8

# --- Default parameter values ---
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")              # Hello, Mr. Smith!
greet_with_title("Johnson", "Dr.")     # Hello, Dr. Johnson!

# --- Keyword arguments (order doesn't matter) ---
def describe(name, age, city):
    print(f"{name} is {age} years old from {city}.")

describe(age=25, city="New York", name="Alice")
# Alice is 25 years old from New York.

# --- Returning multiple values (as a tuple) ---
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)               # 1 9

# --- *args — variable number of positional arguments ---
def total(*args):
    return sum(args)

print(total(1, 2, 3))          # 6
print(total(10, 20, 30, 40))   # 100

# --- **kwargs — variable number of keyword arguments ---
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

show_info(name="Alice", age=25, city="New York")
# name: Alice
# age: 25
# city: New York

# --- Combining *args and **kwargs ---
def mixed(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

mixed(1, 2, 3, name="Alice", role="admin")
# args: (1, 2, 3)
# kwargs: {'name': 'Alice', 'role': 'admin'}

# --- Docstring — documenting a function ---
def square(n):
    """Return the square of n."""
    return n ** 2

print(square(4))               # 16
print(square.__doc__)          # Return the square of n.

# --- Nested functions ---
def outer():
    def inner():
        print("Inside inner()")
    inner()

outer()                        # Inside inner()

# --- Recursive function ---
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))            # 120

# ============================================================
# Summary
# ============================================================
# Concept          | Syntax example
# -----------------+------------------------------------------
# Basic function   | def name():
# Parameters       | def name(a, b):
# Default param    | def name(a, b="default"):
# Keyword args     | name(b=2, a=1)
# Return value     | return value
# Multiple return  | return a, b  → unpacked as a, b = fn()
# *args            | def fn(*args): → tuple of extra positional
# **kwargs         | def fn(**kwargs): → dict of extra keyword
