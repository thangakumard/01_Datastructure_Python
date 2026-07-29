# ============================================================
# Python: Iterators & Iteration Tools for Beginners
# ============================================================

# ============================================================
# 1. range() — generate a sequence of numbers
# ============================================================
print(list(range(5)))              # [0, 1, 2, 3, 4]
print(list(range(1, 6)))           # [1, 2, 3, 4, 5]
print(list(range(0, 10, 2)))       # [0, 2, 4, 6, 8]  (step)
print(list(range(5, 0, -1)))       # [5, 4, 3, 2, 1]  (countdown)

for i in range(3):
    print(i, end=" ")              # 0 1 2
print()

# ============================================================
# 2. enumerate() — loop with index and value
# ============================================================
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple
# 1 banana
# 2 cherry

# Start index from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry

# ============================================================
# 3. zip() — iterate multiple iterables in parallel
# ============================================================
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78

# zip stops at the shortest iterable
a = [1, 2, 3]
b = ["x", "y"]
print(list(zip(a, b)))             # [(1, 'x'), (2, 'y')]

# Unzip — transpose pairs back
pairs = [(1, "a"), (2, "b"), (3, "c")]
nums, letters = zip(*pairs)
print(nums)                        # (1, 2, 3)
print(letters)                     # ('a', 'b', 'c')

# ============================================================
# 4. map() — apply a function to every element
# ============================================================
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)                     # [1, 4, 9, 16, 25]

# With a named function
def double(x):
    return x * 2

print(list(map(double, numbers)))  # [2, 4, 6, 8, 10]

# Map over strings
words = ["hello", "world"]
print(list(map(str.upper, words))) # ['HELLO', 'WORLD']

# ============================================================
# 5. filter() — keep elements that pass a condition
# ============================================================
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)                       # [2, 4, 6, 8]

words = ["", "hello", "", "world", ""]
non_empty = list(filter(None, words))   # None removes falsy values
print(non_empty)                   # ['hello', 'world']

# ============================================================
# 6. sorted() and reversed()
# ============================================================
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(nums))                # [1, 1, 2, 3, 4, 5, 6, 9]
print(sorted(nums, reverse=True))  # [9, 6, 5, 4, 3, 2, 1, 1]

# Sort by custom key
words = ["banana", "apple", "kiwi", "cherry"]
print(sorted(words, key=len))      # ['kiwi', 'apple', 'banana', 'cherry']

print(list(reversed([1, 2, 3])))   # [3, 2, 1]

# ============================================================
# 7. any() and all()
# ============================================================
nums = [2, 4, 6, 7, 8]
print(any(n % 2 != 0 for n in nums))   # True  (at least one is odd)
print(all(n % 2 == 0 for n in nums))   # False (not all are even)

flags = [True, True, True]
print(all(flags))                  # True

# ============================================================
# 8. iter() and next() — manually stepping an iterator
# ============================================================
items = [10, 20, 30]
it = iter(items)
print(next(it))                    # 10
print(next(it))                    # 20
print(next(it))                    # 30
# next(it) now would raise StopIteration

# ============================================================
# Summary Table
# ============================================================
# Function      | What it does
# --------------+----------------------------------------------
# range(n)      | generate 0..n-1
# enumerate(it) | yield (index, value) pairs
# zip(a, b)     | pair elements from two iterables
# map(fn, it)   | apply fn to every element
# filter(fn,it) | keep elements where fn returns True
# sorted(it)    | return sorted list (original unchanged)
# reversed(it)  | iterate in reverse order
# any(it)       | True if at least one element is truthy
# all(it)       | True if every element is truthy
# iter(it)      | get iterator object
# next(it)      | get next value from iterator
