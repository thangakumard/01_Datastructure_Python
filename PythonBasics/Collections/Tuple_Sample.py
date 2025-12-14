def demo_tuple_methods_and_operations():
    print("==== Tuple Methods + Operations Demo ====\n")

    # Base tuple
    tpl = (10, 20, 30, 20, 40, 20)
    print("Original tuple:", tpl)

    # =============================
    # 1. TUPLE METHODS
    # =============================

    # ----- count() -----
    print("\n1. Methods:")
    print("count(20):", tpl.count(20))

    # ----- index() -----
    print("index(20):", tpl.index(20))  # first occurrence
    print("index(20, 2):", tpl.index(20, 2))  # with starting index

    # =============================
    # 2. TUPLE OPERATIONS
    # =============================
    print("\n2. Operations:")

    # ----- length -----
    print("len(tpl):", len(tpl))

    # ----- indexing -----
    print("tpl[0]:", tpl[0])
    print("tpl[-1]:", tpl[-1])

    # ----- slicing -----
    print("tpl[1:4]:", tpl[1:4])
    print("tpl[:3]:", tpl[:3])
    print("tpl[3:]:", tpl[3:])

    # ----- concatenation -----
    t2 = (50, 60)
    print("tpl + t2:", tpl + t2)

    # ----- repetition -----
    print("tpl * 2:", tpl * 2)

    # ----- membership -----
    print("20 in tpl:", 20 in tpl)
    print("100 in tpl:", 100 in tpl)

    # ----- iteration -----
    print("\nIterating through tuple:")
    for item in tpl:
        print(item, end=" ")
    print()

    # ----- tuple unpacking -----
    a, b, c, d, e, f = tpl
    print("\nUnpacked values:", a, b, c, d, e, f)

    # ----- min, max -----
    print("\nmin(tpl):", min(tpl))
    print("max(tpl):", max(tpl))

    # ----- sum -----
    print("sum(tpl):", sum(tpl))

    # ----- sorting (returns list, not tuple) -----
    print("\nsorted(tpl):", sorted(tpl))  # sorted list
    print("sorted(tpl, reverse=True):", sorted(tpl, reverse=True))

    # Convert sorted list back to tuple
    print("tuple(sorted(tpl)):", tuple(sorted(tpl)))

    # ----- converting tuple to list -----
    lst = list(tpl)
    print("\nConverted to list:", lst)

    # modify list
    lst.append(999)
    print("List after append:", lst)

    # convert back to tuple
    new_tuple = tuple(lst)
    print("New tuple from modified list:", new_tuple)

    print("\n==== End of Demo ====")

if __name__ == "__main__":
    demo_tuple_methods_and_operations()