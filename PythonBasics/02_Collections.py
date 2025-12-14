def demo_collections():
    lst = [1, 2, 2, 3]
    dct = {i: i*i for i in lst}
    tpl = tuple(lst)
    st = set(lst)

    print("list:", lst)
    print("tuple:", tpl)
    print("set (unique):", st)
    print("dict:", dct)

if __name__ == "__main__":
    demo_collections()