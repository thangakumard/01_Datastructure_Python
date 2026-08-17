# heapq — Heap Queue Algorithm (min-heap by default)

import heapq

"""
Python's `heapq` module implements a **binary min-heap** on top of a plain list.
The smallest element is always at index 0. All operations maintain the heap invariant.

---

# 1️⃣ What is a Heap?

A heap is a complete binary tree stored as a list where:

    heap[k] <= heap[2*k + 1]   (left child)
    heap[k] <= heap[2*k + 2]   (right child)

Index layout:

         0
        / \\
       1   2
      / \\ / \\
     3  4 5  6

⚠ Python only provides a **min-heap** natively.
  For a max-heap, negate values (see Section 7).

---

# 2️⃣ Import

```python
import heapq
```

No class needed — heapq works directly on a regular Python list.

---

# 3️⃣ heapify(x) — Convert list → heap in-place

```python
nums = [5, 3, 8, 1, 9, 2]
heapq.heapify(nums)
print(nums)   # [1, 3, 2, 5, 9, 8]  ← not sorted, but heap-ordered
```

- Rearranges the list so the heap invariant holds
- Time: O(n)  — faster than pushing n items one by one
- Space: O(1) — in-place

---

# 4️⃣ heappush(heap, item) — Push one item

```python
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)
print(heap)   # [1, 2, 8, 5]
```

- Maintains heap invariant after inserting
- Time: O(log n)

---

# 5️⃣ heappop(heap) — Pop the smallest item

```python
heap = [1, 3, 5, 7, 9]
heapq.heapify(heap)

print(heapq.heappop(heap))   # 1
print(heapq.heappop(heap))   # 3
print(heap)                  # [5, 7, 9]
```

- Always returns the minimum element
- Time: O(log n)

✅ heappop + heappush together = heap sort in O(n log n)

---

# 6️⃣ heappushpop(heap, item) — Push then pop (atomic, faster)

```python
heap = [2, 5, 8]
heapq.heapify(heap)

result = heapq.heappushpop(heap, 1)
print(result)   # 1  ← pushed 1, immediately popped it (it was smallest)

result = heapq.heappushpop(heap, 10)
print(result)   # 2  ← pushed 10, popped 2 (the actual minimum)
```

- Equivalent to: heappush then heappop, but ONE heap operation instead of two
- The returned value is min(item, heap[0])
- Time: O(log n)

Use this when you want to keep heap size fixed (e.g., "keep top-k smallest"):

```python
# maintain a heap of the 3 smallest seen
heap = []
for x in [5, 1, 8, 3, 7]:
    if len(heap) < 3:
        heapq.heappush(heap, x)
    else:
        heapq.heappushpop(heap, x)   # drop largest of the 3+1
```

---

# 7️⃣ heapreplace(heap, item) — Pop then push (atomic, faster)

```python
heap = [1, 5, 8]
heapq.heapify(heap)

result = heapq.heapreplace(heap, 3)
print(result)   # 1  ← old minimum returned
print(heap)     # [3, 5, 8]
```

- Pops the smallest first, THEN pushes the new item
- ⚠ Raises IndexError on an empty heap (unlike heappushpop)
- The returned value is always the OLD heap[0], regardless of item
- Time: O(log n)

heappushpop vs heapreplace:

| Function       | Order          | Returns       | Empty heap |
| -------------- | -------------- | ------------- | ---------- |
| heappushpop    | push → pop     | min(item, h0) | safe       |
| heapreplace    | pop → push     | old h0        | raises     |

---

# 8️⃣ nlargest(n, iterable, key=None) — Top N largest

```python
scores = [34, 90, 55, 78, 12, 99, 45]

print(heapq.nlargest(3, scores))          # [99, 90, 78]

students = [('Alice', 88), ('Bob', 95), ('Carol', 72)]
print(heapq.nlargest(2, students, key=lambda s: s[1]))
# [('Bob', 95), ('Alice', 88)]
```

- Time: O(n log k) where k = n (the count requested)
- For large k close to len(iterable), use sorted(..., reverse=True)[:k] instead

---

# 9️⃣ nsmallest(n, iterable, key=None) — Top N smallest

```python
temps = [30, 15, 22, 8, 40, 5]

print(heapq.nsmallest(3, temps))          # [5, 8, 15]

tasks = [('low', 3), ('high', 1), ('medium', 2)]
print(heapq.nsmallest(2, tasks, key=lambda t: t[1]))
# [('high', 1), ('medium', 2)]
```

- Time: O(n log k)
- For k == 1, min() is faster; for large k, use sorted()[:k]

---

# 🔟 Max-Heap — Negate values

Python has no built-in max-heap. Trick: negate all values.

```python
heap = []
for val in [3, 1, 7, 2, 9]:
    heapq.heappush(heap, -val)       # store negated

max_val = -heapq.heappop(heap)       # negate back
print(max_val)   # 9
```

---

# 1️⃣1️⃣ Priority Queue with Tuples

heappush compares tuples element by element, so store (priority, item):

```python
task_queue = []
heapq.heappush(task_queue, (2, 'write tests'))
heapq.heappush(task_queue, (1, 'fix bug'))
heapq.heappush(task_queue, (3, 'deploy'))

while task_queue:
    priority, task = heapq.heappop(task_queue)
    print(f"[{priority}] {task}")

# [1] fix bug
# [2] write tests
# [3] deploy
```

⚠ Tie-breaking: if priorities are equal, Python compares the second element.
  Use a counter to break ties safely:

```python
import itertools

counter = itertools.count()
heapq.heappush(task_queue, (1, next(counter), 'task A'))
heapq.heappush(task_queue, (1, next(counter), 'task B'))
# counter ensures items with same priority never need comparison
```

---

# 1️⃣2️⃣ Merge Sorted Iterables — heapq.merge()

```python
a = [1, 4, 7]
b = [2, 5, 8]
c = [3, 6, 9]

merged = list(heapq.merge(a, b, c))
print(merged)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

- Input iterables must already be sorted
- Returns a lazy iterator (memory efficient for large sorted files)
- Time: O(n log k) where k = number of iterables

---

# 1️⃣3️⃣ All Functions Summary

| Function                    | What it does                        | Time       |
| --------------------------- | ----------------------------------- | ---------- |
| `heapify(x)`                | list → heap in-place                | O(n)       |
| `heappush(h, item)`         | push item                           | O(log n)   |
| `heappop(h)`                | pop minimum                         | O(log n)   |
| `heappushpop(h, item)`      | push then pop (min of item and h)   | O(log n)   |
| `heapreplace(h, item)`      | pop then push (returns old min)     | O(log n)   |
| `nlargest(n, it, key=None)` | top-n largest                       | O(n log k) |
| `nsmallest(n, it, key=None)`| top-n smallest                      | O(n log k) |
| `merge(*iterables)`         | lazy merge of sorted iterables      | O(n log k) |

---

# 1️⃣4️⃣ heapq vs sorted vs bisect

| Need                       | Use              |
| -------------------------- | ---------------- |
| Repeatedly get min/max     | heapq            |
| One-time sort              | sorted() / sort()|
| Sorted insert into a list  | bisect.insort    |
| Top-k from large stream    | heapq.nsmallest  |
| Merge pre-sorted lists     | heapq.merge      |

---

# Interview One-liner

> `heapq` is Python's min-heap: push/pop in O(log n), always gives the smallest element.
> Negate values for a max-heap; use tuples for priority queues.

---

# When should YOU use heapq?

✔ Dijkstra's shortest path
✔ Prim's MST
✔ K closest / K largest / K smallest
✔ Merge K sorted lists
✔ Median of data stream (two heaps)
✔ Task scheduling by priority
✔ Top-K frequent elements

"""


# ── Live demos (run this file to see output) ──────────────────────────────────

print("=" * 50)
print("heapify")
nums = [5, 3, 8, 1, 9, 2]
heapq.heapify(nums)
print(nums)                          # [1, 3, 2, 5, 9, 8]

print("\nheappush")
heap = []
for v in [5, 2, 8, 1]:
    heapq.heappush(heap, v)
print(heap)                          # [1, 2, 8, 5]

print("\nheappop")
print(heapq.heappop(heap))           # 1
print(heapq.heappop(heap))           # 2

print("\nheappushpop")
heap = [2, 5, 8]
heapq.heapify(heap)
print(heapq.heappushpop(heap, 1))    # 1 (pushed 1, it was smallest, popped immediately)
print(heapq.heappushpop(heap, 10))   # 2 (pushed 10, real min 2 was popped)

print("\nheapreplace")
heap = [1, 5, 8]
heapq.heapify(heap)
print(heapq.heapreplace(heap, 3))    # 1 (old min returned)
print(heap)                          # [3, 5, 8]

print("\nnlargest / nsmallest")
scores = [34, 90, 55, 78, 12, 99, 45]
print(heapq.nlargest(3, scores))     # [99, 90, 78]
print(heapq.nsmallest(3, scores))    # [12, 34, 45]

print("\nMax-heap via negation")
heap = []
for v in [3, 1, 7, 2, 9]:
    heapq.heappush(heap, -v)
print(-heapq.heappop(heap))          # 9

print("\nPriority queue with tuples")
pq = []
heapq.heappush(pq, (2, 'write tests'))
heapq.heappush(pq, (1, 'fix bug'))
heapq.heappush(pq, (3, 'deploy'))
while pq:
    pri, task = heapq.heappop(pq)
    print(f"  [{pri}] {task}")

print("\nmerge sorted iterables")
print(list(heapq.merge([1, 4, 7], [2, 5, 8], [3, 6, 9])))
