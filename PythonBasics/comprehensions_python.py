# ============================================================
# Python: Comprehensions for Beginners
# ============================================================
# Comprehensions are a concise way to create lists, dicts,
# sets, and generators from existing iterables.
# ============================================================

# ============================================================
# 1. List Comprehension
# ============================================================
# Syntax: [expression for item in iterable if condition]

# Without comprehension
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print(squares)                      # [1, 4, 9, 16, 25]

# With comprehension (same result, one line)
squares = [n ** 2 for n in range(1, 6)]
print(squares)                      # [1, 4, 9, 16, 25]

# With condition — only even numbers
evens = [n for n in range(1, 11) if n % 2 == 0]
print(evens)                        # [2, 4, 6, 8, 10]

# Transforming strings
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(upper_words)                  # ['HELLO', 'WORLD', 'PYTHON']

# Nested loop in comprehension
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)                        # [(1, 3), (1, 4), (2, 3), (2, 4)]

# ============================================================
# 2. Dict Comprehension
# ============================================================
# Syntax: {key: value for item in iterable if condition}

# Square mapping
sq_map = {n: n ** 2 for n in range(1, 6)}
print(sq_map)                       # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)                      # {1: 'a', 2: 'b', 3: 'c'}

# Filter dict — keep items where value > 2
filtered = {k: v for k, v in original.items() if v > 2}
print(filtered)                     # {'c': 3}

# ============================================================
# 3. Set Comprehension
# ============================================================
# Syntax: {expression for item in iterable if condition}
# Result is a set — no duplicates

nums = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {n ** 2 for n in nums}
print(unique_squares)               # {1, 4, 9, 16}

# ============================================================
# 4. Generator Expression
# ============================================================
# Syntax: (expression for item in iterable if condition)
# Like a list comprehension but memory-efficient — computes
# values one at a time instead of building a full list.

gen = (n ** 2 for n in range(1, 6))
print(gen)                          # <generator object ...>
print(next(gen))                    # 1
print(next(gen))                    # 4

# Pass directly to sum / max / min — no list needed
total = sum(n ** 2 for n in range(1, 6))
print(total)                        # 55

# ============================================================
# 5. Practical Examples
# ============================================================

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for row in matrix for n in row]
print(flat)                         # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extract only digits from a mixed string
data = "a1b2c3d4"
digits = [ch for ch in data if ch.isdigit()]
print(digits)                       # ['1', '2', '3', '4']

# Word lengths
sentence = "the quick brown fox"
lengths = {word: len(word) for word in sentence.split()}
print(lengths)                      # {'the': 3, 'quick': 5, 'brown': 5, 'fox': 3}

# ============================================================
# Summary Table
# ============================================================
# Type        | Syntax                             | Result
# ------------+------------------------------------+----------
# List        | [expr for x in it if cond]         | list
# Dict        | {k: v for x in it if cond}         | dict
# Set         | {expr for x in it if cond}         | set
# Generator   | (expr for x in it if cond)         | generator
