'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''
def demo_list_methods_and_operations():
    print("==== List Methods + Operations Demo ====\n")

    # Base list
    lst = [10, 20, 30, 20, 40]
    print("Original list:", lst)

    # =============================
    # 1. LIST METHODS
    # =============================

    print("\n1. Methods:")

    # append()
    lst.append(50)
    print("append(50):", lst)

    # insert()
    lst.insert(1, 15)
    print("insert(1, 15):", lst)

    # remove()
    lst.remove(20)  # removes first occurrence
    print("remove(20):", lst)

    # pop()
    popped = lst.pop()  # last element
    print("pop(): removed", popped, "| list:", lst)

    popped_at_2 = lst.pop(2)
    print("pop(2): removed", popped_at_2, "| list:", lst)

    # clear()
    lst_copy = lst.copy()
    lst_copy.clear()
    print("clear():", lst_copy)

    # index()
    lst2 = [10, 20, 30, 40, 50]
    print("\nindex(30):", lst2.index(30))

    # count()
    print("count(20):", lst2.count(20))

    # sort()
    unsorted_list = [5, 3, 8, 1]
    unsorted_list.sort()
    print("\nsort():", unsorted_list)

    # sort(reverse=True)
    unsorted_list.sort(reverse=True)
    print("sort(reverse=True):", unsorted_list)

    # reverse()
    temp_lst = [1, 2, 3, 4]
    temp_lst.reverse()
    print("reverse():", temp_lst)

    # copy()
    new_list = lst2.copy()
    print("copy():", new_list)

    # extend()
    lst2.extend([60, 70])
    print("extend([60, 70]):", lst2)

    # =============================
    # 2. LIST OPERATIONS
    # =============================
    print("\n2. Operations:")

    # length
    print("len(lst2):", len(lst2))

    # indexing
    print("lst2[0]:", lst2[0])
    print("lst2[-1]:", lst2[-1])

    # slicing
    print("lst2[1:4]:", lst2[1:4])
    print("lst2[:3]:", lst2[:3])
    print("lst2[3:]:", lst2[3:])

    # concatenation
    print("lst2 + [80, 90]:", lst2 + [80, 90])

    # repetition
    print("[1, 2] * 3:", [1, 2] * 3)

    # membership
    print("30 in lst2:", 30 in lst2)
    print("999 in lst2:", 999 in lst2)

    # iteration
    print("\nIterating lst2:")
    for item in lst2:
        print(item, end=" ")
    print()

    # min, max, sum
    print("\nmin(lst2):", min(lst2))
    print("max(lst2):", max(lst2))
    print("sum(lst2):", sum(lst2))

    # sorted() (returns new list)
    print("\nsorted(lst2):", sorted(lst2))
    print("sorted(lst2, reverse=True):", sorted(lst2, reverse=True))

    # list comprehension
    squares = [x*x for x in lst2]
    print("\nList comprehension (squares):", squares)

    # converting from tuple to list
    tpl = (1, 2, 3)
    print("\nConverted tuple → list:", list(tpl))

    # list unpacking
    a, b, c = [100, 200, 300]
    print("Unpacked values:", a, b, c)

    print("\n==== End of Demo ====")
    
if __name__ == "__main__":
    demo_list_methods_and_operations()


    """
    Here’s a **complete matrix of Python List methods** with their **time complexity** and **description** 👇
(This is interview-grade and practical)

---

# 📌 Python List Methods – Time Complexity Matrix

| Method  | Syntax                 | Time Complexity | Description             |
| ------- | ---------------------- | --------------- | ----------------------- |
| append  | `lst.append(x)`        | **O(1)**        | Add element at end      |
| extend  | `lst.extend(iterable)` | **O(k)**        | Add k elements          |
| insert  | `lst.insert(i, x)`     | **O(n)**        | Insert at index         |
| pop     | `lst.pop()`            | **O(1)**        | Remove last             |
| pop(i)  | `lst.pop(i)`           | **O(n)**        | Remove at index         |
| remove  | `lst.remove(x)`        | **O(n)**        | Remove first occurrence |
| clear   | `lst.clear()`          | **O(n)**        | Remove all              |
| index   | `lst.index(x)`         | **O(n)**        | Find index              |
| count   | `lst.count(x)`         | **O(n)**        | Count value             |
| sort    | `lst.sort()`           | **O(n log n)**  | Sort in-place           |
| reverse | `lst.reverse()`        | **O(n)**        | Reverse list            |
| copy    | `lst.copy()`           | **O(n)**        | Shallow copy            |

---

# 📌 List Access Operations

| Operation    | Syntax     | Time     |
| ------------ | ---------- | -------- |
| Index access | `lst[i]`   | **O(1)** |
| Slice        | `lst[a:b]` | **O(k)** |
| Membership   | `x in lst` | **O(n)** |
| Length       | `len(lst)` | **O(1)** |

---

# 📌 Insert/Delete Complexity Summary

| Position  | Cost     |
| --------- | -------- |
| End       | **O(1)** |
| Beginning | **O(n)** |
| Middle    | **O(n)** |

---

# 📌 Why insert/remove is O(n)?

Because Python lists are:

> **Dynamic arrays**

Elements after insertion/deletion must be **shifted**.

---

# 📌 Example

```python
lst = [1,2,3,4]
lst.insert(1, 99)   # shift [2,3,4]
```

---

# 📌 Interview One-liner

> Python list is a dynamic array.
> Insertion/deletion in middle is O(n).
> Append is O(1) amortized.

---

# 📌 Space Complexity

| Operation | Space |
| --------- | ----- |
| append    | O(1)  |
| copy      | O(n)  |
| slicing   | O(k)  |

---

# 📌 Common Traps

| Code           | Cost   |
| -------------- | ------ |
| `pop(0)`       | ❌ O(n) |
| `insert(0, x)` | ❌ O(n) |
| `lst += other` | O(k)   |

---

# 📌 When to use list?

✔ Random access
✔ Stack
✔ Small datasets
✔ Ordered storage

---

# 📌 Comparison

| Structure | Best for     |
| --------- | ------------ |
| list      | index access |
| deque     | queue        |
| set       | lookup       |
| dict      | key lookup   |

---

    """