# ============================================================
# Python: Converting Different Data Types to Float
# ============================================================
# Use float() to convert a value to a floating-point number.
# ============================================================

# --- int to float ---
age = 25
age_float = float(age)
print(type(age_float), age_float)          # <class 'float'> 25.0

# --- str (integer string) to float ---
num_str = "42"
num_float = float(num_str)
print(type(num_float), num_float)          # <class 'float'> 42.0

# --- str (decimal string) to float ---
price_str = "9.99"
price_float = float(price_str)
print(type(price_float), price_float)      # <class 'float'> 9.99

# --- str with scientific notation to float ---
sci_str = "1.5e3"
sci_float = float(sci_str)
print(type(sci_float), sci_float)          # <class 'float'> 1500.0

# --- bool to float ---
print(float(True))                         # 1.0
print(float(False))                        # 0.0

# --- special float values from string ---
print(float("inf"))                        # inf
print(float("-inf"))                       # -inf
print(float("nan"))                        # nan  (not a number)

# ============================================================
# What float() cannot convert
# ============================================================

# Strings with text fail
# float("9.99 USD")                        # ValueError

# None fails
# float(None)                              # TypeError

# list / dict / set fail
# float([1.0])                             # TypeError

# ============================================================
# Float precision — a beginner gotcha
# ============================================================
print(0.1 + 0.2)                           # 0.30000000000000004  (not exactly 0.3)

# Use round() when exact decimal display matters
print(round(0.1 + 0.2, 2))                # 0.3

# ============================================================
# Practical use: arithmetic with mixed int and float
# ============================================================
a = 7
b = 2
print(a / b)                               # 3.5   (/ always returns float)
print(float(a) + 0.5)                      # 7.5

# ============================================================
# Summary Table
# ============================================================
# Type         | Example value  | float() result | Note
# -------------+----------------+----------------+---------------------
# int          | 25             | 25.0           |
# str (int)    | "42"           | 42.0           |
# str (float)  | "9.99"         | 9.99           |
# str (sci)    | "1.5e3"        | 1500.0         | scientific notation
# bool         | True / False   | 1.0 / 0.0      |
# str "inf"    | "inf"          | inf            | infinity
# str "nan"    | "nan"          | nan            | not a number
# None         | None           | TypeError      | not supported
# list/dict    | [1.0]          | TypeError      | not supported
