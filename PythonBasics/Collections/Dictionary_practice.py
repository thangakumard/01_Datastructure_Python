d = {"name": "John", "age": 30, "city": "New York"}
print("****************")
print(d)

d = {"name": "John", "age": 35}
print("After reassigning values:", d)

print(d.get("name"))
#Inserting a new key-value pair
d["email"] = "john@example.com" 
print("After inserting email:", d)

#Insert a new key-value pair using update() method
d.update({"phone": "1234567890"})
print("Insert using update method:", d)

#Insert a new key-value pair using setdefault() method
# this method returns the value of the item with the specified key
# If the key does not exist, it inserts the key with the specified value
value = d.setdefault("country", "USA")
print("Insert using setdefault method:", d, "Returned value:", value)

value1 = d.setdefault("name", "Thanga")
print("Insert using setdefault method for an existing key:", d, "Existing Value is NOT CHANGED Returned value:", value1)

#Updating an existing key-value pair
d["age"] = 31
print("After updating age:", d)

#Updating multiple key-value pairs using update() method
d.update({
    "phone": "123-456-7890",
    "married": False
})
print("After updating multiple values using update method:", d)

#Removing a key-value pair
"""
del d[key] raises a KeyError if the key doesn’t exist. 
You can handle it using try–except, check key existence before deleting, 
or safely use pop(key, default).
÷≥
        You only want to delete
        You know the key exists

Use pop() when:
    You want the removed value
    You want safe deletion with a default
"""

d["city"] = "New York"  
print("Before popping city:", d)

popped_value = d.pop("city")
print("After popping city:", popped_value, "from", d)

#Try to pop again with the same key
try:
    city = d.pop("city")
except KeyError:
    print("Key 'city' does not exist")

#pop with default value - Exception will not be raised if the key does not exist
popped_value = d.pop("city", "Unknown")
print("Popped city with default value:", popped_value)

#popitem() method removes and returns an arbitrary (key, value) pair from the dictionary
"""
popitem() returns a tuple
Tuples support:
        unpacking
        index-based access
"""
popped_item = d.popitem()
print("Popped item:", popped_item, "from", d)
#to unpack the popped item - Using tuple unpacking
key, value = popped_item
print("Key:", key)
print("Value:", value)
#tunpack the popped item - Using indexing
key = popped_item[0]
value = popped_item[1]

#Accessing the popped item - directly accessing the tuple elements
key, value = d.popitem()
print("Key:", key)
print("Value:", value)

#Removing a key-value pair using del statement
try:
    del d["city"]
except KeyError:
    print("Key 'city' does not exist")




#Iterating through the dictionary
for key, value in d.items():
    print("key:", key, "value:", value)

#Checking if a key exists in the dictionary
if "name" in d:
    print("Key 'name' exists in the dictionary")


