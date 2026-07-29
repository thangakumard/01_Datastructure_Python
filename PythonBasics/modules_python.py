# ============================================================
# Python: Modules & Imports for Beginners
# ============================================================

# ============================================================
# 1. Importing a standard library module
# ============================================================
import math

print(math.pi)                     # 3.141592653589793
print(math.sqrt(16))               # 4.0
print(math.ceil(3.2))              # 4

# ============================================================
# 2. Import with alias (shorter name)
# ============================================================
import random as rnd

print(rnd.randint(1, 10))          # random int between 1 and 10
print(rnd.choice(["rock", "paper", "scissors"]))

# ============================================================
# 3. Import specific names from a module
# ============================================================
from math import sqrt, pi, factorial

print(sqrt(25))                    # 5.0  (no math. prefix needed)
print(pi)                          # 3.141592653589793
print(factorial(6))                # 720

# ============================================================
# 4. Commonly used standard library modules
# ============================================================

# --- os — interact with the operating system ---
import os

print(os.getcwd())                 # current working directory
print(os.path.exists("missing.txt"))  # False
print(os.path.join("folder", "file.txt"))  # folder/file.txt

# --- sys — system-specific parameters ---
import sys

print(sys.version)                 # Python version string
print(sys.platform)                # 'darwin', 'win32', 'linux'

# --- datetime — dates and times ---
from datetime import date, datetime, timedelta

today = date.today()
print(today)                               # 2025-01-15
print(datetime.now().strftime("%H:%M:%S")) # current time HH:MM:SS

tomorrow = today + timedelta(days=1)
print(tomorrow)

# --- random — random number generation ---
import random

print(random.random())             # float between 0.0 and 1.0
print(random.randint(1, 100))      # random int between 1 and 100
print(random.choice([1, 2, 3, 4, 5]))   # random item from list

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)                        # shuffled in place

print(random.sample(range(100), 5))  # 5 unique random numbers

# --- collections — specialized container types ---
from collections import Counter, defaultdict, OrderedDict

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(count)                       # Counter({'apple': 3, 'banana': 2, ...})
print(count.most_common(2))        # [('apple', 3), ('banana', 2)]

dd = defaultdict(int)
dd["missing_key"] += 1
print(dd["missing_key"])           # 1  (no KeyError)

# --- itertools — efficient looping tools ---
import itertools

# combinations
print(list(itertools.combinations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 3)]

# permutations
print(list(itertools.permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# chain — flatten iterables
print(list(itertools.chain([1, 2], [3, 4], [5])))
# [1, 2, 3, 4, 5]

# --- json — parse and create JSON ---
import json

data = {"name": "Alice", "age": 30, "active": True}
json_str = json.dumps(data, indent=2)   # dict → JSON string
print(json_str)

parsed = json.loads(json_str)           # JSON string → dict
print(parsed["name"])                   # Alice

# ============================================================
# 5. __name__ guard — run code only when file is executed directly
# ============================================================
# (not when imported as a module by another file)

def main():
    print("Running as main script")

if __name__ == "__main__":
    main()

# ============================================================
# Summary Table
# ============================================================
# Syntax                        | What it does
# ------------------------------+-----------------------------
# import module                 | import whole module
# import module as alias        | import with shorter name
# from module import name       | import specific item
# from module import *          | import everything (avoid!)
# __name__ == "__main__"        | guard for direct execution
#
# Module       | Common use
# -------------+----------------------------------------------
# math         | sqrt, ceil, floor, pi, factorial
# random       | randint, choice, shuffle, sample
# os           | getcwd, path.exists, path.join
# sys          | version, platform, argv
# datetime     | date.today(), datetime.now(), timedelta
# collections  | Counter, defaultdict, deque
# itertools    | combinations, permutations, chain
# json         | dumps (encode), loads (decode)
