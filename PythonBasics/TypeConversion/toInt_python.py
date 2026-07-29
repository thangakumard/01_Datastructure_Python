# ============================================================
# Python: Converting Different Data Types to Integer
# ============================================================
# Use int() to convert a value to an integer.
# int() truncates decimals — it does NOT round.
# ============================================================

# --- str to int (numeric string only) ---
age_str = "25"
age = int(age_str)
print(type(age), age)                  # <class 'int'> 25

# --- float to int (decimal part is dropped) ---
price = 9.99
price_int = int(price)
print(type(price_int), price_int)      # <class 'int'> 9

pi = 3.7
print(int(pi))                         # 3  (truncated, not rounded)

# --- bool to int ---
print(int(True))                       # 1
print(int(False))                      # 0

# --- binary string to int (base 2) ---
binary_str = "1010"
print(int(binary_str, 2))             # 10

# --- octal string to int (base 8) ---
octal_str = "17"
print(int(octal_str, 8))              # 15

# --- hexadecimal string to int (base 16) ---
hex_str = "1F"
print(int(hex_str, 16))               # 31

# ============================================================
# What int() cannot convert
# ============================================================

# Float string fails — convert to float first, then to int
float_str = "9.99"
# int(float_str)                       # ValueError: invalid literal
result = int(float(float_str))
print(result)                          # 9

# Strings with text fail
# int("25 years")                      # ValueError

# None fails
# int(None)                            # TypeError

# list / dict / set fail
# int([1, 2])                          # TypeError

# ============================================================
# Practical use: user input is always a string
# ============================================================
user_input = "42"                      # simulating input()
number = int(user_input)
print(number + 8)                      # 50

# ============================================================
# Summary Table
# ============================================================
# Type         | Example value  | int() result   | Note
# -------------+----------------+----------------+------------------
# str (int)    | "25"           | 25             | must be numeric
# str (float)  | "9.99"         | ValueError     | use int(float(x))
# float        | 9.99           | 9              | truncates decimal
# bool         | True / False   | 1 / 0          |
# str (binary) | "1010"         | 10             | int(x, 2)
# str (octal)  | "17"           | 15             | int(x, 8)
# str (hex)    | "1F"           | 31             | int(x, 16)
# None         | None           | TypeError      | not supported
# list/dict    | [1, 2]         | TypeError      | not supported
