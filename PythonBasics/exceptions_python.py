# ============================================================
# Python: Exception Handling for Beginners
# ============================================================

# ============================================================
# 1. Basic try / except
# ============================================================
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")   # Cannot divide by zero!

# --- Catching the error message ---
try:
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")         # ValueError: invalid literal for int()...

# ============================================================
# 2. Multiple except blocks
# ============================================================
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
    except TypeError:
        print("Error: both arguments must be numbers")

safe_divide(10, 0)       # Error: division by zero
safe_divide(10, "2")     # Error: both arguments must be numbers

# ============================================================
# 3. except with multiple exception types
# ============================================================
def parse_index(data, index):
    try:
        return int(data[index])
    except (IndexError, ValueError) as e:
        print(f"Error: {e}")

parse_index(["1", "abc", "3"], 1)    # Error: invalid literal...
parse_index(["1", "2"], 5)           # Error: list index out of range

# ============================================================
# 4. else — runs only if no exception occurred
# ============================================================
try:
    number = int("42")
except ValueError:
    print("Not a valid number")
else:
    print(f"Parsed successfully: {number}")  # Parsed successfully: 42

# ============================================================
# 5. finally — always runs, exception or not
# ============================================================
def read_data(filename):
    f = None
    try:
        f = open(filename, "r")
        return f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    finally:
        print("Cleanup: closing file if open")
        if f:
            f.close()

read_data("missing.txt")
# File 'missing.txt' not found.
# Cleanup: closing file if open

# ============================================================
# 6. Raising exceptions
# ============================================================
def set_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)                           # Age cannot be negative: -5

# ============================================================
# 7. Common built-in exceptions
# ============================================================
exceptions = {
    "ValueError":       "Wrong value type  → int('abc')",
    "TypeError":        "Wrong data type   → '2' + 2",
    "ZeroDivisionError":"Divide by zero    → 1 / 0",
    "IndexError":       "Index out of range→ [1,2][5]",
    "KeyError":         "Missing dict key  → {}['x']",
    "AttributeError":   "Missing attribute → None.upper()",
    "FileNotFoundError":"File missing      → open('x.txt')",
    "NameError":        "Undefined var     → print(x)",
    "ImportError":      "Module not found  → import foo",
}
for name, desc in exceptions.items():
    print(f"  {name:<20} {desc}")

# ============================================================
# 8. Custom exception class
# ============================================================
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")
        self.balance = balance
        self.amount = amount

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(e)                  # Cannot withdraw 200, balance is 100

# ============================================================
# Summary
# ============================================================
# Block      | Runs when
# -----------+--------------------------------------------------
# try        | always — wrap risky code here
# except     | an exception of the specified type is raised
# else       | the try block completed with NO exception
# finally    | always, exception or not (cleanup code here)
# raise      | manually trigger an exception
