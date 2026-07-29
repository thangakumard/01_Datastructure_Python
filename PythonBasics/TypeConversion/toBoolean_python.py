# ============================================================
# Python: Converting Different Data Types to Boolean
# ============================================================
# Use bool() to convert a value to True or False.
# Rule of thumb: "empty or zero" → False, everything else → True
# ============================================================

# --- int to bool ---
print(bool(1))                     # True
print(bool(0))                     # False
print(bool(-5))                    # True   (any non-zero int is True)

# --- float to bool ---
print(bool(3.14))                  # True
print(bool(0.0))                   # False  (only 0.0 is False)

# --- str to bool ---
print(bool("hello"))               # True   (non-empty string is True)
print(bool(""))                    # False  (empty string is False)
print(bool("False"))               # True   (non-empty string, not the bool value!)

# --- list to bool ---
print(bool([1, 2, 3]))             # True
print(bool([]))                    # False  (empty list is False)

# --- tuple to bool ---
print(bool((1, 2)))                # True
print(bool(()))                    # False  (empty tuple is False)

# --- dict to bool ---
print(bool({"key": "value"}))      # True
print(bool({}))                    # False  (empty dict is False)

# --- set to bool ---
print(bool({1, 2, 3}))            # True
print(bool(set()))                 # False  (empty set is False)

# --- None to bool ---
print(bool(None))                  # False  (None is always False)

# ============================================================
# Beginner gotcha: bool("False") is True!
# ============================================================
user_input = "False"
print(bool(user_input))            # True  — because the string is non-empty

# To check a string's intent, compare it explicitly
print(user_input.lower() == "true")   # False
print(user_input.lower() == "false")  # True

# ============================================================
# Practical use: bool() in if conditions
# ============================================================
name = ""
if not bool(name):
    print("Name is empty")         # Name is empty

items = [1, 2, 3]
if bool(items):
    print("List has items")        # List has items

# Python evaluates truthiness automatically — bool() is optional here
if name:
    print("Has name")
else:
    print("No name provided")      # No name provided

# ============================================================
# Summary Table
# ============================================================
# Type     | Falsy values          | Truthy values
# ---------+-----------------------+------------------------
# int      | 0                     | any non-zero int
# float    | 0.0                   | any non-zero float
# str      | "" (empty)            | any non-empty string
# list     | [] (empty)            | any non-empty list
# tuple    | () (empty)            | any non-empty tuple
# dict     | {} (empty)            | any non-empty dict
# set      | set() (empty)         | any non-empty set
# None     | None (always False)   | —
