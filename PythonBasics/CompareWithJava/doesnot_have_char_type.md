# Character Data Type in Python

## Does Python have a `char` data type?

**No. Python does not have a separate `char` (character) data type.**

In Python, a single character is represented as a **string (`str`) containing exactly one character**.

```python
ch = 'A'

print(type(ch))
# <class 'str'>
```

So, unlike Java, Python does not have a primitive `char` type.

## Python vs Java

| Feature | Java | Python |
|---|---|---|
| Character data type | `char` | No separate `char` type |
| Example | `char ch = 'A';` | `ch = 'A'` |
| Type of `'A'` | `char` | `str` |
| Multiple characters | `String` | `str` |
| Character size | 16-bit UTF-16 code unit | Unicode string |
| String indexing | Returns `char` | Returns a string of length 1 |

### Java

```java
char ch = 'A';
System.out.println(ch);
```

Here, `ch` is of type `char`.

### Python

```python
ch = 'A'
print(ch)
print(type(ch))
```

Output:

```text
A
<class 'str'>
```

Here, `ch` is a `str`, not a `char`.

## Single Character vs String

Python uses the same `str` type for both a single character and multiple characters:

```python
a = 'A'
name = 'Python'

print(type(a))
# <class 'str'>

print(type(name))
# <class 'str'>
```

The difference is simply the length:

```python
print(len(a))
# 1

print(len(name))
# 6
```

## Character Access

Python strings can be indexed to access individual characters:

```python
word = "Python"

print(word[0])
# P

print(type(word[0]))
# <class 'str'>
```

Notice that `word[0]` returns a `str` containing one character.

In Java:

```java
String word = "Python";

char ch = word.charAt(0);
```

`charAt(0)` returns a `char`.

## Character Comparison

You can compare single-character strings directly:

```python
ch = 'A'

if ch == 'A':
    print("Character is A")
```

You can also check whether a value contains exactly one character:

```python
ch = 'A'

if len(ch) == 1:
    print("It is a single character")
```

## Important Point

Python's `str` is a **sequence of Unicode characters**. There is no separate primitive character type.

Therefore:

```text
Java:
'A'  → char
"ABC" → String

Python:
'A'  → str
"ABC" → str
```

## Summary

- Python **does not have a separate `char` data type**.
- A single character is represented using `str`.
- `'A'` has type `str`.
- `"ABC"` also has type `str`.
- A single character can be identified using `len(value) == 1`.
- Python strings support Unicode characters.

### Quick Interview Answer

> **Python does not have a separate character (`char`) data type. A single character is represented as a string (`str`) of length one. For example, `'A'` is of type `str`, whereas Java has a separate primitive `char` type.**
