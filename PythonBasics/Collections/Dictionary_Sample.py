def demo_dictionary_methods_and_operations():
    print("==== Dictionary Methods + Operations Demo ====\n")

    # Base dictionary
    d = {"a": 1, "b": 2, "c": 3}
    print("Original dict:", d)

    # =============================
    # 1. DICTIONARY METHODS
    # =============================
    print("\n1. Methods:")
    # Insert new key-value pair
    d["d"] = 4
    print("\nAfter inserting d['d'] = 4:", d)

    # get()
    print("get('a'):", d.get("a"))
    print("get('x', 'Not Found'):", d.get("x", "Not Found"))

    # keys(), values(), items()
    print("keys():", list(d.keys()))
    print("values():", list(d.values()))
    print("items():", list(d.items()))

    # update()
    d.update({"d": 4})
    print("\nupdate({'d': 4}):", d)

    # pop()
    popped_value = d.pop("b")
    print("pop('b'): removed", popped_value, "| dict:", d)

    # popitem()
    popped_item = d.popitem()
    print("popitem(): removed", popped_item, "| dict:", d)

    # setdefault()
    print("\nsetdefault('c'):", d.setdefault("c"))      # existing key
    print("setdefault('x', 100):", d.setdefault("x", 100))  # new key
    print("After setdefault:", d)

    # clear()
    temp = d.copy()
    temp.clear()
    print("clear():", temp)

    # copy()
    d_copy = d.copy()
    print("copy():", d_copy)

    # fromkeys()
    new_dict = dict.fromkeys(["k1", "k2", "k3"], 0)
    print("fromkeys(['k1','k2','k3'],0):", new_dict)

    # =============================
    # 2. DICTIONARY OPERATIONS
    # =============================
    print("\n2. Operations:")

    # length
    print("len(d):", len(d))

    # indexing / accessing
    print("d['a']:", d["a"])

    # assignment
    d["y"] = 999
    print("After assigning d['y'] = 999:", d)

    # membership
    print("'a' in d:", "a" in d)
    print("'z' in d:", "z" in d)

    # deleting keys
    del d["a"]
    print("After del d['a']:", d)

    # looping keys
    print("\nLooping keys:")
    for key in d:
        print(key, end=" ")

    # looping values
    print("\nLooping values:")
    for value in d.values():
        print(value, end=" ")

    # looping items
    print("\nLooping items:")
    for key, value in d.items():
        print(f"{key} -> {value}")

    # dictionary comprehension
    print("\nDictionary comprehension (squares):")
    comp = {k: v*v for k, v in {"p": 2, "q": 3}.items()}
    print(comp)

    # merging dicts (Python 3.9+)
    d1 = {"a": 10, "b": 20}
    d2 = {"b": 999, "c": 30}
    merged = d1 | d2   # overwrites b
    print("\nMerging dicts using | :", merged)

    # merging using update()
    d3 = d1.copy()
    d3.update(d2)
    print("Merging dicts using update():", d3)

    # sorted keys
    print("\nSorted keys:", sorted(d))

    #sort by values
    d1 = {"a": 3, "b": 1, "c": 2}
    sorted_d = dict(sorted(d1.items(), key=lambda item: item[1]))
    print(sorted_d)


    # convert to list of keys/values/items
    print("list(d.keys()):", list(d.keys()))
    print("list(d.values()):", list(d.values()))
    print("list(d.items()):", list(d.items()))

    print("\n==== End of Demo ====")


if __name__ == "__main__":
    demo_dictionary_methods_and_operations()