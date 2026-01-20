"""
Collection	Method / Attribute	Kind	Time Complexity	Signature / Example	What it does (notes)
deque	append	method	O(1)	d.append(x)	Add x to the right end.
deque	appendleft	method	O(1)	d.appendleft(x)	Add x to the left end.
deque	clear	method	O(n)	d.clear()	Remove all elements.
deque	copy	method	O(n)	d.copy()	Shallow copy.
deque	count	method	O(n)	d.count(x)	Count occurrences of x.
deque	extend	method	O(k)	d.extend(iterable)	Extend right side by k elements from iterable.
deque	extendleft	method	O(k)	d.extendleft(iterable)	Extend left side by k elements (added in reverse order).
deque	index	method	O(n)	d.index(x[, start[, stop]])	Find first index of x.
deque	insert	method	O(n)	d.insert(i, x)	Insert x at position i (may shift elements).
deque	pop	method	O(1)	d.pop()	Remove and return rightmost element.
deque	popleft	method	O(1)	d.popleft()	Remove and return leftmost element.
deque	remove	method	O(n)	d.remove(x)	Remove first occurrence of x.
deque	reverse	method	O(n)	d.reverse()	Reverse in place.
deque	rotate	method	O(r)	d.rotate(n=1)	Rotate by r = abs(n) mod len(d).
deque	maxlen	attribute	O(1)	d.maxlen	Maximum size (None if unbounded).

Counter	elements	method	O(T)	c.elements()	Iterate elements repeating each as its count (T = sum of positive counts).
Counter	most_common	method	O(n log n) (or O(n log k))	c.most_common([n])	List of (elem, count) pairs, highest first.
Counter	subtract	method	O(k)	c.subtract([iterable-or-mapping])	Subtract counts from k incoming items/pairs (can go negative).
Counter	total	method	O(n)	c.total()	Sum of counts over n distinct keys (Py 3.10+).
Counter	update	method	O(k)	c.update([iterable-or-mapping])	Add counts from k incoming items/pairs.
Counter	clear	method	O(n)	m.clear()	Remove all items.
Counter	copy	method	O(n)	m.copy()	Shallow copy.
Counter	fromkeys	classmethod	O(k)	type(m).fromkeys(iterable, value=None)	Create new mapping from k keys.
Counter	get	method	O(1) avg	m.get(key, default=None)	Return value for key or default.
Counter	items	method	O(1)	m.items()	View of (key, value) pairs (lazy view).
Counter	keys	method	O(1)	m.keys()	View of keys (lazy view).
Counter	pop	method	O(1) avg	m.pop(key[, default])	Remove key and return value (or default).
Counter	popitem	method	O(1) avg	m.popitem()	Remove and return last inserted (key, value).
Counter	setdefault	method	O(1) avg	m.setdefault(key, default=None)	Get key; if missing set to default and return it.
Counter	update	method	O(k)	m.update([other], **kwargs)	Update from another mapping/iterable of k pairs.
Counter	values	method	O(1)	m.values()	View of values (lazy view).

defaultdict	default_factory	attribute	O(1)	d.default_factory	Callable used to supply missing values (or None).
defaultdict	__missing__	method	O(1) avg	d.__missing__(key)	Called by d[key] when key is missing; creates default if factory set.
defaultdict	clear	method	O(n)	m.clear()	Remove all items.
defaultdict	copy	method	O(n)	m.copy()	Shallow copy.
defaultdict	fromkeys	classmethod	O(k)	type(m).fromkeys(iterable, value=None)	Create new mapping from k keys.
defaultdict	get	method	O(1) avg	m.get(key, default=None)	Return value for key or default.
defaultdict	items	method	O(1)	m.items()	View of (key, value) pairs (lazy view).
defaultdict	keys	method	O(1)	m.keys()	View of keys (lazy view).
defaultdict	pop	method	O(1) avg	m.pop(key[, default])	Remove key and return value (or default).
defaultdict	popitem	method	O(1) avg	m.popitem()	Remove and return last inserted (key, value).
defaultdict	setdefault	method	O(1) avg	m.setdefault(key, default=None)	Get key; if missing set to default and return it.
defaultdict	update	method	O(k)	m.update([other], **kwargs)	Update from another mapping/iterable of k pairs.
defaultdict	values	method	O(1)	m.values()	View of values (lazy view).

OrderedDict	move_to_end	method	O(1) avg	od.move_to_end(key, last=True)	Move existing key to end (or beginning if last=False).
OrderedDict	popitem	method	O(1) avg	od.popitem(last=True)	Remove & return (key, value) from end (or start if last=False).
OrderedDict	clear	method	O(n)	m.clear()	Remove all items.
OrderedDict	copy	method	O(n)	m.copy()	Shallow copy.
OrderedDict	fromkeys	classmethod	O(k)	type(m).fromkeys(iterable, value=None)	Create new mapping from k keys.
OrderedDict	get	method	O(1) avg	m.get(key, default=None)	Return value for key or default.
OrderedDict	items	method	O(1)	m.items()	View of (key, value) pairs (lazy view).
OrderedDict	keys	method	O(1)	m.keys()	View of keys (lazy view).
OrderedDict	pop	method	O(1) avg	m.pop(key[, default])	Remove key and return value (or default).
OrderedDict	setdefault	method	O(1) avg	m.setdefault(key, default=None)	Get key; if missing set to default and return it.
OrderedDict	update	method	O(k)	m.update([other], **kwargs)	Update from another mapping/iterable of k pairs.
OrderedDict	values	method	O(1)	m.values()	View of values (lazy view).

namedtuple	_make	classmethod	O(f)	T._make(iterable)	Create instance from iterable (f = number of fields).
namedtuple	_asdict	method	O(f)	t._asdict()	Return mapping of field names to values.
namedtuple	_replace	method	O(f)	t._replace(**kwargs)	Return new instance replacing specified fields.
namedtuple	_fields	attribute	O(1)	T._fields	Tuple of field names.
namedtuple	_field_defaults	attribute	O(1)	T._field_defaults	Dict of field default values (if provided).
namedtuple	tuple ops	inherited	len: O(1); idx: O(1); iter: O(n)	len(t), t[i], for x in t	namedtuple instances are tuples; support all tuple operations.

ChainMap	maps	attribute	O(1)	cm.maps	List of underlying mappings (first map searched first).
ChainMap	new_child	method	O(1)	cm.new_child(m=None)	Return new ChainMap with a new map prepended (optionally m).
ChainMap	parents	property	O(1)	cm.parents	ChainMap of all maps except the first.
ChainMap	__getitem__	method	O(m) avg	cm[key]	Lookup across m maps (each dict lookup ~O(1) avg).
ChainMap	get	method	O(m) avg	cm.get(key, default=None)	Return first found value across maps.
ChainMap	keys	method	O(U)	cm.keys()	Key view over union of keys (U = total unique keys across maps).
ChainMap	items	method	O(U)	cm.items()	Items view where first-found value wins.
ChainMap	values	method	O(U)	cm.values()	Values corresponding to keys().

list	append	method	O(1) amortized	lst.append(x)	Add element at end.
list	extend	method	O(k)	lst.extend(iterable)	Append k elements from iterable.
list	insert	method	O(n)	lst.insert(i, x)	Insert at index i (shifts elements).
list	remove	method	O(n)	lst.remove(x)	Remove first occurrence of value x.
list	pop	method	O(1)	lst.pop()	Remove and return last element.
list	pop(i)	method	O(n)	lst.pop(i)	Remove and return element at index i (shifts elements).
list	clear	method	O(n)	lst.clear()	Remove all items.
list	index	method	O(n)	lst.index(x[, start[, stop]])	Return first index of value x.
list	count	method	O(n)	lst.count(x)	Count occurrences of x.
list	sort	method	O(n log n)	lst.sort(key=None, reverse=False)	Sort in place (Timsort).
list	reverse	method	O(n)	lst.reverse()	Reverse in place.
list	copy	method	O(n)	lst.copy()	Shallow copy.
list	len	operation	O(1)	len(lst)	Number of elements.
list	contains	operation	O(n)	x in lst	Membership test (linear scan).
list	get item	operation	O(1)	lst[i]	Index access.
list	slice	operation	O(k)	lst[a:b]	Slice copy of length k.
str	capitalize	method	O(n)	s.capitalize()	Return copy with first char capitalized.
str	casefold	method	O(n)	s.casefold()	Aggressive lowercasing for comparisons.
str	center	method	O(n + w)	s.center(width[, fillchar])	Pad to width w.
str	count	method	O(n)	s.count(sub[, start[, end]])	Count non-overlapping occurrences.
str	encode	method	O(n)	s.encode(encoding='utf-8', errors='strict')	Encode to bytes.
str	endswith	method	O(k)	s.endswith(suffix[, start[, end]])	Check suffix (k=len(suffix)).
str	expandtabs	method	O(n)	s.expandtabs(tabsize=8)	Replace tabs with spaces.
str	find	method	O(n)	s.find(sub[, start[, end]])	Find substring; -1 if not found.
str	format	method	O(out)	s.format(*args, **kwargs)	Format string; cost depends on output size.
str	format_map	method	O(out)	s.format_map(mapping)	Format with mapping; cost depends on output size.
str	index	method	O(n)	s.index(sub[, start[, end]])	Like find but raises ValueError if not found.
str	isalnum	method	O(n)	s.isalnum()	True if all chars alnum and non-empty.
str	isalpha	method	O(n)	s.isalpha()	True if all chars alphabetic and non-empty.
str	isascii	method	O(n)	s.isascii()	True if all chars are ASCII.
str	isdecimal	method	O(n)	s.isdecimal()	True if all chars are decimal.
str	isdigit	method	O(n)	s.isdigit()	True if all chars are digits.
str	isidentifier	method	O(n)	s.isidentifier()	True if valid Python identifier.
str	islower	method	O(n)	s.islower()	True if all cased chars are lowercase.
str	isnumeric	method	O(n)	s.isnumeric()	True if all chars are numeric.
str	isprintable	method	O(n)	s.isprintable()	True if all chars are printable.
str	isspace	method	O(n)	s.isspace()	True if all chars are whitespace.
str	istitle	method	O(n)	s.istitle()	True if string is titlecased.
str	isupper	method	O(n)	s.isupper()	True if all cased chars are uppercase.
str	join	method	O(out)	sep.join(iterable)	Join strings; cost proportional to total output size.
str	ljust	method	O(n + w)	s.ljust(width[, fillchar])	Pad on right to width w.
str	lower	method	O(n)	s.lower()	Lowercase copy.
str	lstrip	method	O(n)	s.lstrip([chars])	Trim leading chars/whitespace.
str	maketrans	staticmethod	O(k)	str.maketrans(x[, y[, z]])	Create translation table from k mappings/chars.
str	partition	method	O(n)	s.partition(sep)	Split into 3-tuple at first sep.
str	removeprefix	method	O(k)	s.removeprefix(prefix)	Remove prefix if present.
str	removesuffix	method	O(k)	s.removesuffix(suffix)	Remove suffix if present.
str	replace	method	O(n)	s.replace(old, new[, count])	Replace occurrences; cost proportional to output size.
str	rfind	method	O(n)	s.rfind(sub[, start[, end]])	Find from right; -1 if not found.
str	rindex	method	O(n)	s.rindex(sub[, start[, end]])	Like rfind but raises ValueError if not found.
str	rjust	method	O(n + w)	s.rjust(width[, fillchar])	Pad on left to width w.
str	rpartition	method	O(n)	s.rpartition(sep)	Split into 3-tuple at last sep.
str	rsplit	method	O(n)	s.rsplit(sep=None, maxsplit=-1)	Split from right.
str	rstrip	method	O(n)	s.rstrip([chars])	Trim trailing chars/whitespace.
str	split	method	O(n)	s.split(sep=None, maxsplit=-1)	Split into list.
str	splitlines	method	O(n)	s.splitlines(keepends=False)	Split at line boundaries.
str	startswith	method	O(k)	s.startswith(prefix[, start[, end]])	Check prefix (k=len(prefix)).
str	strip	method	O(n)	s.strip([chars])	Trim both ends.
str	swapcase	method	O(n)	s.swapcase()	Swap case copy.
str	title	method	O(n)	s.title()	Titlecase copy.
str	translate	method	O(n)	s.translate(table)	Map characters via translation table.
str	upper	method	O(n)	s.upper()	Uppercase copy.
str	zfill	method	O(n + w)	s.zfill(width)	Pad with zeros on left to width w.
str	len	operation	O(1)	len(s)	Number of characters.
str	contains	operation	O(n)	sub in s	Substring search.
str	get char	operation	O(1)	s[i]	Index access returns 1-char string.
str	slice	operation	O(k)	s[a:b]	Substring copy of length k.
"""