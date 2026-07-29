# ============================================================
# Python: Conditionals for Beginners
# ============================================================

# --- Basic if / elif / else ---
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
# Grade: C

# --- Comparison operators ---
print(5 == 5)      # True   equal
print(5 != 3)      # True   not equal
print(5 > 3)       # True   greater than
print(5 < 3)       # False  less than
print(5 >= 5)      # True   greater than or equal
print(5 <= 4)      # False  less than or equal

# --- Logical operators: and, or, not ---
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")    # Entry allowed

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("Day off!")         # Day off!

is_raining = False
if not is_raining:
    print("Go outside!")      # Go outside!

# --- in and not in ---
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)          # True
print("grape" not in fruits)      # True

# --- is vs == ---
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)      # True   (same values)
print(a is b)      # False  (different objects in memory)
print(a is c)      # True   (same object)

# --- Ternary (one-line if/else) ---
age = 20
status = "adult" if age >= 18 else "minor"
print(status)      # adult

# --- Nested if ---
num = 15
if num > 0:
    if num % 2 == 0:
        print(f"{num} is positive and even")
    else:
        print(f"{num} is positive and odd")   # 15 is positive and odd
else:
    print(f"{num} is negative")

# --- Checking None, empty, zero with if ---
values = [None, 0, "", [], {}, "hello", 42, [1, 2]]
for v in values:
    if v:
        print(f"{repr(v):15} → Truthy")
    else:
        print(f"{repr(v):15} → Falsy")

# --- match statement (Python 3.10+) ---
command = "quit"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "quit":
        print("Quitting...")   # Quitting...
    case _:
        print("Unknown command")

# ============================================================
# Summary
# ============================================================
# Operator / Keyword | Meaning
# -------------------+-----------------------------------
# ==, !=             | equal, not equal
# >, <, >=, <=       | comparison
# and, or, not       | logical operators
# in, not in         | membership test
# is, is not         | identity (same object in memory)
# x if cond else y   | ternary expression
# match / case       | structural pattern matching (3.10+)
