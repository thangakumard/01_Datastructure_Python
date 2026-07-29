# ============================================================
# Python: Converting Different Data Types to String
# ============================================================
# Use str() to convert any value to its string representation.
# ============================================================

# --- int to str ---
age = 25
age_str = str(age)
print(type(age_str), age_str)          # <class 'str'> 25

# --- float to str ---
price = 9.99
price_str = str(price)
print(type(price_str), price_str)      # <class 'str'> 9.99

# --- bool to str ---
is_active = True
active_str = str(is_active)
print(type(active_str), active_str)    # <class 'str'> True

# --- None to str ---
value = None
value_str = str(value)
print(type(value_str), value_str)      # <class 'str'> None

# --- list to str ---
colors = ["red", "green", "blue"]
colors_str = str(colors)
print(type(colors_str), colors_str)    # <class 'str'> ['red', 'green', 'blue']

# --- tuple to str ---
coordinates = (10, 20)
coord_str = str(coordinates)
print(type(coord_str), coord_str)      # <class 'str'> (10, 20)

# --- dict to str ---
person = {"name": "Alice", "age": 30}
person_str = str(person)
print(type(person_str), person_str)    # <class 'str'> {'name': 'Alice', 'age': 30}

# --- set to str ---
unique_nums = {1, 2, 3}
set_str = str(unique_nums)
print(type(set_str), set_str)          # <class 'str'> {1, 2, 3}

# --- bytes to str ---
raw = b"hello"
bytes_str = str(raw)
print(type(bytes_str), bytes_str)      # <class 'str'> b'hello'

# To get a clean string from bytes, decode it instead:
decoded = raw.decode("utf-8")
print(type(decoded), decoded)          # <class 'str'> hello

# ============================================================
# Practical use: string concatenation requires str conversion
# ============================================================
score = 95
message = "Your score is: " + str(score)
print(message)                         # Your score is: 95

# f-strings auto-convert values — no str() needed
print(f"Your score is: {score}")       # Your score is: 95

# format() also handles conversion
print("Your score is: {}".format(score))  # Your score is: 95

# ============================================================
# Summary Table
# ============================================================
# Type     | Example value     | str() result
# ---------+-------------------+-----------------------------
# int      | 42                | '42'
# float    | 3.14              | '3.14'
# bool     | True              | 'True'
# None     | None              | 'None'
# list     | [1, 2]            | '[1, 2]'
# tuple    | (1, 2)            | '(1, 2)'
# dict     | {'a': 1}          | "{'a': 1}"
# set      | {1, 2}            | '{1, 2}'
# bytes    | b'hi'             | "b'hi'"  (use .decode() for clean text)
