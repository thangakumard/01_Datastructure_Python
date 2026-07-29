# ============================================================
# Python: File I/O for Beginners
# ============================================================
# Always use "with open(...)" — it automatically closes the
# file even if an error occurs.
# ============================================================

import os

FILENAME = "sample.txt"

# ============================================================
# 1. Write to a file (creates file if it doesn't exist)
# ============================================================
with open(FILENAME, "w") as f:       # "w" overwrites existing content
    f.write("Line 1: Hello\n")
    f.write("Line 2: World\n")
    f.write("Line 3: Python\n")

print("File written.")

# ============================================================
# 2. Read entire file at once
# ============================================================
with open(FILENAME, "r") as f:       # "r" is read mode (default)
    content = f.read()
    print(content)
# Line 1: Hello
# Line 2: World
# Line 3: Python

# ============================================================
# 3. Read line by line
# ============================================================
with open(FILENAME, "r") as f:
    for line in f:
        print(line.strip())           # strip() removes trailing \n

# ============================================================
# 4. Read all lines into a list
# ============================================================
with open(FILENAME, "r") as f:
    lines = f.readlines()
    print(lines)
    # ['Line 1: Hello\n', 'Line 2: World\n', 'Line 3: Python\n']

# ============================================================
# 5. Append to a file (does not overwrite)
# ============================================================
with open(FILENAME, "a") as f:       # "a" is append mode
    f.write("Line 4: Appended\n")

with open(FILENAME, "r") as f:
    print(f.read())

# ============================================================
# 6. Read a specific line by index
# ============================================================
with open(FILENAME, "r") as f:
    lines = f.readlines()
    print(lines[0].strip())           # Line 1: Hello

# ============================================================
# 7. Write a list of lines at once
# ============================================================
new_lines = ["alpha\n", "beta\n", "gamma\n"]
with open("output.txt", "w") as f:
    f.writelines(new_lines)

# ============================================================
# 8. Check if a file exists before reading
# ============================================================
if os.path.exists(FILENAME):
    print(f"{FILENAME} exists")
else:
    print(f"{FILENAME} not found")

# ============================================================
# 9. File seek — move to a specific position
# ============================================================
with open(FILENAME, "r") as f:
    f.seek(0)                          # move to beginning
    first_char = f.read(1)
    print(first_char)                  # L
    print(f.tell())                    # 1 (current position)

# ============================================================
# 10. Handling FileNotFoundError safely
# ============================================================
try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found — handle gracefully.")

# ============================================================
# Cleanup sample files
# ============================================================
os.remove(FILENAME)
os.remove("output.txt")
print("Sample files cleaned up.")

# ============================================================
# Summary Table
# ============================================================
# Mode  | Meaning
# ------+-----------------------------------------------------
# "r"   | read (default) — file must exist
# "w"   | write — creates or overwrites
# "a"   | append — creates or adds to end
# "x"   | exclusive create — fails if file exists
# "rb"  | read binary (images, PDFs, etc.)
# "wb"  | write binary
#
# Method        | What it does
# --------------+---------------------------------------------
# f.read()      | read entire file as a string
# f.readline()  | read one line
# f.readlines() | read all lines into a list
# f.write(s)    | write string s to file
# f.writelines()| write a list of strings
# f.seek(n)     | move cursor to byte position n
# f.tell()      | return current cursor position
