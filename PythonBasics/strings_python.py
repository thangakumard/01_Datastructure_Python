# ============================================================
# Python: Strings for Beginners
# ============================================================

# --- Creating strings ---
s1 = "Hello"
s2 = 'World'
s3 = """This is a
multi-line string"""
print(s1, s2)                  # Hello World

# --- Concatenation and repetition ---
full = s1 + ", " + s2 + "!"
print(full)                    # Hello, World!
print("ha" * 3)                # hahaha

# --- len() ---
print(len("Python"))           # 6

# --- Indexing (0-based, negative counts from end) ---
word = "Python"
print(word[0])                 # P
print(word[-1])                # n

# --- Slicing [start:stop:step] ---
print(word[0:3])               # Pyt   (stop is exclusive)
print(word[2:])                # thon  (start to end)
print(word[:4])                # Pyth  (beginning to stop)
print(word[::-1])              # nohtyP (reversed)

# --- Case methods ---
s = "hello world"
print(s.upper())               # HELLO WORLD
print(s.lower())               # hello world
print(s.capitalize())          # Hello world
print(s.title())               # Hello World
print(s.swapcase())            # HELLO WORLD

# --- Strip whitespace ---
padded = "   hello   "
print(padded.strip())          # "hello"
print(padded.lstrip())         # "hello   "
print(padded.rstrip())         # "   hello"

# --- Find and check ---
sentence = "I love Python"
print(sentence.find("Python"))     # 7   (index of first match, -1 if not found)
print(sentence.count("o"))         # 2
print(sentence.startswith("I"))    # True
print(sentence.endswith("Java"))   # False
print("python".isalpha())          # True  (all alphabetic)
print("123".isdigit())             # True  (all digits)
print("abc123".isalnum())          # True  (alphanumeric)

# --- Replace ---
print(sentence.replace("Python", "Java"))   # I love Java
print("a-b-c".replace("-", ""))             # abc

# --- Split and join ---
csv = "apple,banana,cherry"
fruits = csv.split(",")
print(fruits)                  # ['apple', 'banana', 'cherry']

words = ["Hello", "World"]
print(" ".join(words))         # Hello World
print("-".join(words))         # Hello-World

# --- f-strings (formatted string literals) ---
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
print(f"10 / 3 = {10 / 3:.2f}")           # 10 / 3 = 3.33
print(f"{'centered':^20}")                 # '       centered       '
print(f"{1234567:,}")                      # 1,234,567

# --- in operator ---
print("love" in sentence)      # True
print("hate" in sentence)      # False

# --- Escape characters ---
print("Line1\nLine2")          # newline
print("col1\tcol2")            # tab
print("She said \"hi\"")       # quotes inside string
print("back\\slash")           # backslash

# ============================================================
# Summary Table
# ============================================================
# Method              | What it does
# --------------------+-----------------------------------------
# s.upper()           | all uppercase
# s.lower()           | all lowercase
# s.strip()           | remove leading/trailing whitespace
# s.replace(a, b)     | replace all occurrences of a with b
# s.split(sep)        | split into list by separator
# sep.join(list)      | join list into string with separator
# s.find(sub)         | index of first match (-1 if missing)
# s.startswith(sub)   | True if string starts with sub
# s.endswith(sub)     | True if string ends with sub
# s.count(sub)        | count non-overlapping occurrences
# s[i:j]              | slice from index i to j (exclusive)
# s[::-1]             | reverse the string
