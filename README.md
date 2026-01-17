# 01_Datastructure_Python
# 🔹 1. Basic Data Types (int, float, bool, str)

### Conceptual

1. Difference between `int` and `float`?
| Feature    | `int`            | `float`                      |
| ---------- | ---------------- | ---------------------------- |
| Stores     | Whole numbers    | Decimal numbers              |
| Example    | `10`, `-5`       | `10.5`, `-3.14`              |
| Precision  | Exact            | Approximate (floating point) |
| Memory     | Less             | More                         |
| Operations | Faster           | Slightly slower              |
| Conversion | `int(5.9)` → `5` | `float(5)` → `5.0`           |

Key point:
    int has no decimal part, float always has decimal precision.

2. What is implicit vs explicit type conversion?
3. How does Python handle integer overflow?
4. What is truthy and falsy in Python?
5. Difference between `==` and `is`?

### Practical

6. Convert float `12.9` to int. What happens?
7. Convert string `"123"` to integer safely.
8. Reverse a string without using slicing.
9. Count vowels in a string.
10. Check if a number is palindrome.

---

# 🔹 2. Strings

### DataType & Conversion

11. Convert list of chars to string.
12. Convert string to list of words.
13. Difference between `join()` and `split()`?
14. Convert `"True"` to boolean – is it possible?
15. Remove duplicates from string.

### Looping

16. Print each character using loop.
17. Find frequency of each character.
18. Reverse words in a sentence.
19. Print only digits from string.
20. Find longest word in sentence.

---

# 🔹 3. Lists

### DataType

21. Difference between list and tuple.
22. What is shallow vs deep copy?
23. Time complexity of append, pop?
24. Difference between `extend()` and `append()`?
25. When to use list comprehension?

### Looping

26. Print even numbers from list.
27. Reverse list using loop.
28. Find second largest number.
29. Remove duplicates using loop.
30. Count frequency of elements.

### Type Conversion

31. Convert list → tuple.
32. Convert list → set.
33. Convert list of strings → list of ints.
34. Convert nested list to flat list.
35. Convert list to dictionary.

---

# 🔹 4. Tuples

36. Why tuples are immutable?
37. Convert tuple → list.
38. Find index of element.
39. Loop through tuple.
40. Swap values using tuple unpacking.
41. Count occurrences of element.
42. Convert tuple of pairs → dict.
43. Remove duplicates from tuple.
44. Sort tuple.
45. Difference between `(1)` and `(1,)`?

---

# 🔹 5. Sets

46. Difference between set and list.
47. Why set doesn’t allow duplicates?
48. Convert list → set.
49. Find union, intersection, difference.
50. Loop through set.
51. Check subset and superset.
52. Remove elements safely.
53. Convert set → list.
54. Find common elements between 2 lists.
55. When to use frozenset?

---

# 🔹 6. Dictionaries

### DataType

56. Difference between dict and OrderedDict.
57. Keys rules in dictionary.
58. Can list be key? Why?
59. Difference between get() and [].
60. How to merge two dicts?

### Looping

61. Loop keys only.
62. Loop values only.
63. Loop key-value pairs.
64. Find max value key.
65. Count word frequency using dict.

### Type Conversion

66. Convert list of tuples → dict.
67. Convert dict → list of keys.
68. Convert dict → list of values.
69. Convert dict → tuple.
70. Sort dictionary by values.

---

# 🔹 7. Looping (for, while)

71. Difference between for & while.
72. What is infinite loop?
73. Use of break & continue.
74. Print numbers 1–100.
75. Print prime numbers.
76. Fibonacci series.
77. Factorial using loop.
78. Nested loops example.
79. Pattern printing.
80. Reverse number using loop.

---

# 🔹 8. Type Conversion (Casting)

81. int → float
82. float → int
83. str → int (safe way)
84. list → tuple
85. tuple → list
86. list → set
87. set → list
88. dict → list
89. list → dict
90. bool → int

---

# 🔹 9. Mixed Data Structure Problems

91. Flatten nested list.
92. Remove duplicate dictionaries.
93. Sort list of tuples.
94. Group anagrams.
95. Convert list of dicts → single dict.
96. Find common keys in dicts.
97. Merge lists without duplicates.
98. Count elements in nested list.
99. Find max value in dict of lists.
100. Reverse dictionary.

---

# 🔹 10. Advanced Logic

101. Check if list is sorted.
102. Rotate list k times.
103. Find missing number.
104. Find duplicate number.
105. Two sum problem.
106. Intersection of 3 lists.
107. Find pairs with sum.
108. Convert Roman → integer.
109. String compression.
110. Balanced parentheses.

---

# 🔹 11. Tricky Output Questions

111. What is output of:

```python
print(bool("False"))
```

112.

```python
a = [1,2,3]
b = a
b.append(4)
print(a)
```

113.

```python
print(type({}))
```

114.

```python
print(set([1,1,2,2]))
```

115.

```python
print(1 == True)
```

---

# 🔹 12. Real-World Scenario Questions

116. Read CSV → dict.
117. Parse JSON → Python object.
118. Remove null values from list.
119. Count API response status codes.
120. Convert input string → number safely.

---

# 🔹 Bonus (Interview Favorite)

121. Difference between mutable & immutable?
122. Memory behavior of lists vs tuples.
123. When to use set vs dict?
124. Time complexity of searching in list vs set.
125. Why dict lookup is fast?
