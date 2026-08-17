'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''
# Initialize a dictionary
user = {"name": "Alice", "role": "Admin"}

# 1. Safely read a value
status = user.get("status", "Inactive")  # Returns "Inactive"

# 2. Get views of data
all_keys = user.keys()      # dict_keys(['name', 'role'])
all_pairs = user.items()    # dict_items([('name', 'Alice'), ('role', 'Admin')])

# 3. Add or update data
user.update({"role": "Superadmin", "verified": True})

# 3b. Check if a key exists, then update or add it
if "email" in user:
    user["email"] = "thanga@test.com"
else:
    user["email"] = "thanga@test.com"

# 4. Safely insert with default
user.setdefault("theme", "dark")  # Adds "theme": "dark"

# 5. Remove elements
removed_role = user.pop("role")   # Removes "role", returns "Superadmin"
last_item = user.popitem()        # Removes and returns ('theme', 'dark')

# 6. Reset the dictionary
user.clear()                      # user becomes {}

