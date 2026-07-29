# ============================================================
# Python: Common Math Operations for Beginners
# ============================================================

import math

# ============================================================
# 1. Basic Arithmetic Operators
# ============================================================
print(10 + 3)          # 13  addition
print(10 - 3)          # 7   subtraction
print(10 * 3)          # 30  multiplication
print(10 / 3)          # 3.3333...  division (always float)
print(10 // 3)         # 3   floor division (drops decimal)
print(10 % 3)          # 1   modulus (remainder)
print(2 ** 10)         # 1024  exponentiation (2 to the power 10)

# ============================================================
# 2. Built-in Math Functions (no import needed)
# ============================================================

# abs() — absolute value (removes negative sign)
print(abs(-7))         # 7
print(abs(7))          # 7
print(abs(-3.5))       # 3.5

# max() — largest value
print(max(3, 7, 1))                    # 7
print(max([10, 25, 5, 18]))            # 25  (works on a list too)
print(max("apple", "banana", "kiwi"))  # kiwi  (alphabetical comparison)

# min() — smallest value
print(min(3, 7, 1))                    # 1
print(min([10, 25, 5, 18]))            # 5
print(min("apple", "banana", "kiwi"))  # apple

# sum() — total of an iterable
print(sum([1, 2, 3, 4, 5]))           # 15
print(sum([1, 2, 3], 10))             # 16  (10 is the starting value)

# round() — round to nearest, with optional decimal places
print(round(3.7))          # 4
print(round(3.2))          # 3
print(round(3.14159, 2))   # 3.14
print(round(2.5))          # 2   (banker's rounding — rounds to even)
print(round(3.5))          # 4

# pow() — exponentiation (same as **)
print(pow(2, 10))          # 1024
print(pow(2, 10, 100))     # 24   (2**10 mod 100 — efficient for large nums)

# divmod() — returns (quotient, remainder) as a tuple
print(divmod(10, 3))       # (3, 1)

# ============================================================
# 3. math Module Functions
# ============================================================

# math.sqrt() — square root
print(math.sqrt(25))       # 5.0
print(math.sqrt(2))        # 1.4142135623730951

# math.ceil() — round UP to nearest integer
print(math.ceil(3.1))      # 4
print(math.ceil(3.9))      # 4
print(math.ceil(-3.1))     # -3

# math.floor() — round DOWN to nearest integer
print(math.floor(3.9))     # 3
print(math.floor(3.1))     # 3
print(math.floor(-3.1))    # -4

# math.factorial() — n!
print(math.factorial(5))   # 120  (5 * 4 * 3 * 2 * 1)
print(math.factorial(0))   # 1

# math.gcd() — greatest common divisor
print(math.gcd(48, 18))    # 6

# math.lcm() — least common multiple (Python 3.9+)
print(math.lcm(4, 6))      # 12

# math.log() — natural log (base e)
print(math.log(math.e))    # 1.0

# math.log(x, base) — log with custom base
print(math.log(100, 10))   # 2.0  (log base 10 of 100)
print(math.log2(8))        # 3.0  (log base 2 of 8)
print(math.log10(1000))    # 3.0

# math.pi and math.e — useful constants
print(math.pi)             # 3.141592653589793
print(math.e)              # 2.718281828459045

# ============================================================
# 4. Practical Examples
# ============================================================

# Find the hypotenuse of a right triangle (a=3, b=4)
a, b = 3, 4
hypotenuse = math.sqrt(a**2 + b**2)
print(hypotenuse)          # 5.0

# Clamp a value between min and max bounds
value = 150
clamped = max(0, min(100, value))
print(clamped)             # 100

# Check if a number is even or odd using %
for n in [2, 5, 8, 11]:
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

# ============================================================
# Summary Table
# ============================================================
# Function          | Example              | Result
# ------------------+----------------------+------------------
# abs(x)            | abs(-7)              | 7
# max(a, b, ...)    | max(3, 7, 1)         | 7
# min(a, b, ...)    | min(3, 7, 1)         | 1
# sum(iterable)     | sum([1,2,3])         | 6
# round(x, n)       | round(3.14159, 2)    | 3.14
# pow(x, y)         | pow(2, 10)           | 1024
# divmod(x, y)      | divmod(10, 3)        | (3, 1)
# math.sqrt(x)      | math.sqrt(25)        | 5.0
# math.ceil(x)      | math.ceil(3.1)       | 4
# math.floor(x)     | math.floor(3.9)      | 3
# math.factorial(n) | math.factorial(5)    | 120
# math.gcd(a, b)    | math.gcd(48, 18)     | 6
# math.log(x, base) | math.log(100, 10)    | 2.0
