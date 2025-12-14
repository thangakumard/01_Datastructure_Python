def show_datatypes():
    i = 42                     # int
    f = 3.14                   # float
    s = "hello"                # str
    b = True                   # bool
    l = [1, 2, 3]              # list
    t = (1, 2)                 # tuple (immutable)
    d = {"a": 1, "b": 2}       # dict
    se = {1, 2, 3}             # set

    print("int:", i)
    print("float:", f)
    print("str:", s.upper())
    print("bool:", b)
    print("list + append:", l + [4])
    print("tuple:", t)
    print("dict keys:", list(d.keys()))
    print("set membership (2 in se):", 2 in se)

if __name__ == "__main__":
    show_datatypes()