#deque (Double-Ended Queue) is a high-performance data structure

from collections import deque

"""
Here’s a **complete, structured guide to `deque` methods and their usage** in Python 👇
(`deque` = Double Ended Queue from `collections`)

---

# 1️⃣ Import & Creation

```python
from collections import deque

dq = deque()                 # empty
dq = deque([1,2,3])          # from list
dq = deque("abc")            # from iterable
dq = deque(maxlen=5)         # fixed size
```

---

# 2️⃣ Core Methods (Insertion & Removal)

| Method          | Purpose           |
| --------------- | ----------------- |
| `append(x)`     | Add to right      |
| `appendleft(x)` | Add to left       |
| `pop()`         | Remove from right |
| `popleft()`     | Remove from left  |

### Examples

```python
dq.append(10)
dq.appendleft(5)

dq.pop()
dq.popleft()
```

---

# 3️⃣ Extend Operations

| Method                 | Description                           |
| ---------------------- | ------------------------------------- |
| `extend(iterable)`     | Add multiple to right                 |
| `extendleft(iterable)` | Add multiple to left (reversed order) |

```python
dq.extend([4,5,6])
dq.extendleft([1,2,3])   # inserts as 3,2,1
```

---

# 4️⃣ Rotation

| Method       | Description  |
| ------------ | ------------ |
| `rotate(n)`  | Rotate right |
| `rotate(-n)` | Rotate left  |

```python
dq.rotate(2)     # right
dq.rotate(-2)    # left
```

---

# 5️⃣ Removal & Searching

| Method      | Purpose                 |
| ----------- | ----------------------- |
| `remove(x)` | Remove first occurrence |
| `count(x)`  | Count occurrences       |
| `index(x)`  | Find index              |

```python
dq.remove(3)
dq.count(2)
dq.index(5)
```

---

# 6️⃣ Size & State

| Method    | Description        |
| --------- | ------------------ |
| `len(dq)` | Number of elements |
| `clear()` | Remove all         |
| `maxlen`  | Capacity (if set)  |

```python
len(dq)
dq.clear()
print(dq.maxlen)
```

---

# 7️⃣ Access Elements

```python
dq[0]      # first
dq[-1]     # last
```

⚠ Random access is **slower** than list

---

# 8️⃣ Copying

```python
new_dq = dq.copy()
```

---

# 9️⃣ Fixed-size deque behavior

```python
dq = deque(maxlen=3)

dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)

print(dq)   # deque([2,3,4])
```

👉 Oldest element removed automatically

---

# 10️⃣ Stack Implementation

```python
stack = deque()
stack.append(1)
stack.append(2)
stack.pop()
```

---

# 11️⃣ Queue Implementation

```python
queue = deque()
queue.append("A")
queue.append("B")
queue.popleft()
```

---

# 12️⃣ Sliding Window

```python
dq = deque(maxlen=3)

for i in range(6):
    dq.append(i)
    print(dq)
```

---

# 13️⃣ BFS (Graph Traversal)

```python
from collections import deque

q = deque([start])

while q:
    node = q.popleft()
    for n in graph[node]:
        q.append(n)
```

---

# 14️⃣ All Methods Summary

| Method         | Use            |
| -------------- | -------------- |
| append(x)      | Add right      |
| appendleft(x)  | Add left       |
| pop()          | Remove right   |
| popleft()      | Remove left    |
| extend(it)     | Add many right |
| extendleft(it) | Add many left  |
| rotate(n)      | Rotate         |
| remove(x)      | Remove element |
| clear()        | Remove all     |
| copy()         | Shallow copy   |
| count(x)       | Count          |
| index(x)       | Find position  |
| maxlen         | Capacity       |
| len()          | Size           |

---

# 15️⃣ deque vs list

| Feature       | deque     | list   |
| ------------- | --------- | ------ |
| pop left      | O(1)      | O(n)   |
| append        | O(1)      | O(1)   |
| memory        | Efficient | More   |
| random access | Slower    | Faster |

---

# Interview One-liner

> `deque` is a double-ended queue that supports O(1) insertion and deletion from both ends.

---

# When should YOU use deque?

✔ BFS
✔ Sliding window
✔ Queue/Stack
✔ Real-time streaming
✔ Rate limiters
✔ Undo/Redo



"""