def demo_set_methods_and_operations():
    print("==== Set Methods + Operations Demo ====\n")

    # Base set (duplicates automatically removed)
    st = {10, 20, 30, 40, 20}
    print("Original set:", st)

    # =============================
    # 1. SET METHODS
    # =============================

    print("\n1. Methods:")

    # add()
    st.add(50)
    print("add(50):", st)

    # remove() (errors if not present)
    st.remove(30)
    print("remove(30):", st)

    # discard() (no error if not present)
    st.discard(999)
    print("discard(999):", st)

    # pop() - removes and returns a random element
    popped = st.pop()
    print("pop(): removed", popped, "| set:", st)

    # clear()
    temp = st.copy()
    temp.clear()
    print("clear():", temp)

    # copy()
    st2 = st.copy()
    print("copy():", st2)

    # update() — add elements from another set
    st2.update({60, 70})
    print("update({60, 70}):", st2)

    # union() method
    print("\nunion():", st.union({100, 200}))

    # intersection() method
    print("intersection():", st.intersection({40, 50, 60}))

    # difference() method
    print("difference():", st.difference({10, 50}))

    # symmetric_difference() method
    print("symmetric_difference():", st.symmetric_difference({40, 50, 60}))

    # issubset(), issuperset(), isdisjoint()
    a = {1, 2}
    b = {1, 2, 3}
    c = {10}

    print("\na.issubset(b):", a.issubset(b))
    print("b.issuperset(a):", b.issuperset(a))
    print("a.isdisjoint(c):", a.isdisjoint(c))

    # =============================
    # 2. SET OPERATIONS (OPERATORS)
    # =============================
    print("\n2. Operations (using operators):")

    x = {1, 2, 3}
    y = {3, 4, 5}

    print("x | y (union):", x | y)
    print("x & y (intersection):", x & y)
    print("x - y (difference):", x - y)
    print("x ^ y (symmetric difference):", x ^ y)

    # membership
    print("\nMembership:")
    print("3 in x:", 3 in x)
    print("10 in x:", 10 in x)

    # iteration
    print("\nIterating set x:")
    for item in x:
        print(item, end=" ")

    print()

    # length
    print("\nlen(x):", len(x))

    # converting to list/tuple
    print("list(x):", list(x))
    print("tuple(x):", tuple(x))

    # frozen set
    frozen = frozenset({10, 20, 30})
    print("\nfrozenset:", frozen)

    print("\n==== End of Demo ====")

if __name__ == "__main__":
    demo_set_methods_and_operations()
