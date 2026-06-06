# ============================================================
#   PES University · UE20CS901 — Python for Data Science
#   ESA Previous Year Questions — Section A
#   Papers: Feb 2025, May 2025, Oct 2024, Mar 2024 (both),
#           Nov 2023, Aug 2021, Jul 2021, Model Set
#   Format: Question → Explanation (comment) → Code
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce
import random


# ╔══════════════════════════════════════════════════════════╗
# ║         FEBRUARY 2025 ESA                               ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# Q1(a) Difference between is and ==
# ──────────────────────────────────────────

# == checks whether two objects have the SAME VALUE
# is  checks whether two variables point to the SAME OBJECT in memory
#
# Two lists with identical values are NOT the same object in memory
# A variable assigned from another variable SHARES the same object

a = [1, 2, 3]
b = [1, 2, 3]   # same values, but a NEW list object in memory
c = a            # c points to the EXACT SAME object as a

print(a == b)    # → True  (values are equal)
print(a is b)    # → False (different objects in memory)
print(a is c)    # → True  (same object — c is just another name for a)

# Rule of thumb:
#   Use == to compare values
#   Use is  ONLY to check for None / True / False (e.g. if x is None)


# ──────────────────────────────────────────
# Q1(b) How does zip() work?
# ──────────────────────────────────────────

# zip() takes two or more iterables and pairs up their elements
# into tuples, position by position.
# Stops at the SHORTEST iterable if lengths differ.

names = ["Alice", "Bob"]
ages  = [25, 30]

for name, age in zip(names, ages):
    print(name, age)
# Output:
# Alice 25
# Bob 30

# zip() also works with 3+ iterables
cities = ["BLR", "DEL"]
for name, age, city in zip(names, ages, cities):
    print(name, age, city)

# Convert to a list of tuples
pairs = list(zip(names, ages))
print(pairs)    # → [('Alice', 25), ('Bob', 30)]


# ──────────────────────────────────────────
# Q1(c) Difference between loc[] and iloc[]
# ──────────────────────────────────────────

# loc[]  — LABEL-based: uses row/column NAMES, inclusive on both ends
# iloc[] — INTEGER position-based: uses numbers like Python list indices

df = pd.DataFrame({
    'Name':   ['Alice', 'Bob', 'Carol'],
    'Salary': [50000, 70000, 60000]
})

print(df.loc[0, 'Name'])     # → 'Alice'  (row label 0, column named 'Name')
print(df.iloc[0, 1])          # → 50000   (row position 0, column position 1)

# Key difference on slicing:
# df.loc[0:2]  → includes rows 0, 1, AND 2  (stop is INCLUSIVE)
# df.iloc[0:2] → includes rows 0 and 1 only (stop is EXCLUSIVE, like Python)


# ──────────────────────────────────────────
# Q1(d) What is Broadcasting in NumPy?
# ──────────────────────────────────────────

# Broadcasting = NumPy automatically expands smaller arrays to match
# the shape of larger arrays for arithmetic operations.
# This avoids the need for explicit loops.

arr = np.array([1, 2, 3])
print(arr + 10)    # → [11 12 13]
# The scalar 10 is "broadcast" (stretched) to match shape (3,)
# and added to every element

# 2D example: add a row vector to every row of a matrix
mat = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
print(mat + row)
# → [[11 22 33]
#    [14 25 36]]


# ──────────────────────────────────────────
# Q1(e) Difference between any() and all()
# ──────────────────────────────────────────

# any() → True if AT LEAST ONE element is True (or truthy)
# all() → True only if ALL elements are True (or truthy)
# Both short-circuit: stop as soon as the result is determined

nums = [True, False, True]
print(any(nums))   # → True   (at least one True exists)
print(all(nums))   # → False  (not ALL are True — False blocks it)

# With conditions on a NumPy array
arr = np.array([5, 10, 15])
print((arr > 0).all())    # → True  (all positive)
print((arr > 7).any())    # → True  (some are > 7)
print((arr > 7).all())    # → False (not all > 7 — 5 is not)


# ──────────────────────────────────────────
# Q2(a) Count occurrences of unique values in a Pandas Series
# ──────────────────────────────────────────

# value_counts() returns a Series where:
#   Index = unique values
#   Values = how many times each appears (sorted descending by default)

s = pd.Series(['A', 'B', 'A', 'C', 'B', 'A'])
print(s.value_counts())
# A    3
# B    2
# C    1

# Normalize to get proportions instead of counts
print(s.value_counts(normalize=True))


# ──────────────────────────────────────────
# Q2(b) Difference between axis=0 and axis=1
# ──────────────────────────────────────────

# axis=0 → operate DOWN the rows → result is per COLUMN (column-wise)
# axis=1 → operate ACROSS columns → result is per ROW (row-wise)
# Memory Aid: axis=0 collapses rows (you get one value per column)
#             axis=1 collapses columns (you get one value per row)

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.sum(axis=0))   # → A=6, B=15  (sum each column)
print(df.sum(axis=1))   # → 5, 7, 9   (sum each row)


# ──────────────────────────────────────────
# Q2(c) Difference between reshape() and resize()
# ──────────────────────────────────────────

# reshape() → returns a NEW view with a different shape. ORIGINAL unchanged.
#             Total number of elements MUST stay the same.
# resize()  → modifies the ORIGINAL array in-place. Can change total size
#             (pads with 0s if larger, truncates if smaller).

a = np.array([1, 2, 3, 4])

b = a.reshape(2, 2)     # new array — a is untouched
print(b)
# [[1 2]
#  [3 4]]
print(a)                # → [1 2 3 4]  still unchanged

a.resize(2, 2)          # modifies a IN-PLACE
print(a)
# [[1 2]
#  [3 4]]


# ──────────────────────────────────────────
# Q2(d) Lazy Evaluation in map() and filter()
# ──────────────────────────────────────────

# map() and filter() return ITERATOR objects, not lists.
# They do NOT compute results immediately (lazy evaluation).
# Values are computed only when the iterator is consumed
# (e.g., by list(), next(), or a for loop).
# This saves memory for large data.

nums = [1, 2, 3]
result = map(lambda x: x * 2, nums)  # nothing computed yet!
print(result)                          # → <map object ...>
print(list(result))                    # → [2, 4, 6]  computed NOW

# Same with filter()
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(list(evens))    # → [2, 4]


# ──────────────────────────────────────────
# Q2(e) Merge two DataFrames on a common column
# ──────────────────────────────────────────

# pd.merge() performs SQL-style JOIN operations.
# Default is INNER JOIN — only rows with matching keys in BOTH tables.

df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2], 'Marks': [85, 90]})

result = pd.merge(df1, df2, on='ID')
print(result)
#    ID   Name  Marks
# 0   1  Alice     85
# 1   2    Bob     90

# Other join types: how='left', how='right', how='outer'


# ╔══════════════════════════════════════════════════════════╗
# ║         MAY 2025 ESA                                    ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# Q1(a) How are dictionaries different from lists?
# ──────────────────────────────────────────

# List:       ordered, accessed by INTEGER index, allows duplicates
# Dictionary: unordered (insertion-ordered in Python 3.7+),
#             accessed by KEYS (any hashable type), keys must be unique

# List — access by position
a = [10, 20, 30]
print(a[1])           # → 20  (index 1)

# Dictionary — access by key
d = {"name": "Ram", "age": 21}
print(d["name"])      # → Ram  (key "name")

# Dictionaries are best for LABELLED data; lists for ORDERED sequences


# ──────────────────────────────────────────
# Q1(b) Lambda function vs regular function
# ──────────────────────────────────────────

# Lambda: anonymous, one-line, single expression, no 'return' keyword
# Regular: named, multi-line, can have multiple statements/returns

# Lambda
square_lam = lambda x: x * x
print(square_lam(5))    # → 25

# Regular function (equivalent)
def square_reg(x):
    return x * x

print(square_reg(5))    # → 25

# Key differences:
#   Lambda  → anonymous, one expression, used inline (map/filter/sort)
#   Regular → named, multiple lines, reusable, can have docstrings


# ──────────────────────────────────────────
# Q1(c) String immutability in Python
# ──────────────────────────────────────────

# Immutable = once created, the contents CANNOT be changed.
# Any "modification" actually creates a brand new string object.

s = "Python"
# s[0] = 'J'    # ❌ TypeError: 'str' object does not support item assignment

# To "change" a string, create a NEW one:
s = "Jython"    # s now points to a completely new string object
print(s)        # → Jython

# Practical implication: string methods like .upper() also return NEW strings
print("hello".upper())   # → HELLO  (original "hello" still exists unchanged)


# ──────────────────────────────────────────
# Q1(d) Slice 'PythonProgramming' to get 'thonPro'
# ──────────────────────────────────────────

# String slicing syntax: string[start : stop : step]
#   start = inclusive, stop = EXCLUSIVE
#
# 'PythonProgramming'
#  P  y  t  h  o  n  P  r  o  g  r  a  m  m  i  n  g
#  0  1  2  3  4  5  6  7  8  9 ...
#
# Target: 'thonPro'
#   't' is at index 2
#   'o' is at index 8 → stop must be 9 (exclusive)

s = "PythonProgramming"
print(s[2:9])    # → thonPro ✅


# ──────────────────────────────────────────
# Q1(e) What does *args do?
# ──────────────────────────────────────────

# *args lets a function accept ANY NUMBER of positional arguments.
# Inside the function, they are stored as a TUPLE.
# The name 'args' is just a convention — the * is what matters.

def add(*args):
    print(type(args))    # → <class 'tuple'>
    return sum(args)

print(add(1, 2, 3, 4))     # → 10
print(add(10, 20))          # → 30
print(add())                # → 0  (empty tuple)


# ──────────────────────────────────────────
# Q2(a) sort() vs sorted()
# ──────────────────────────────────────────

# sort()   → LIST METHOD, modifies the list IN-PLACE, returns None
# sorted() → BUILT-IN FUNCTION, returns a NEW sorted list, original unchanged
# Both accept: reverse=True  and  key=function  parameters

a = [4, 1, 3]
a.sort()
print(a)              # → [1, 3, 4]  (original modified)

b = [4, 1, 3]
c = sorted(b)
print(c)              # → [1, 3, 4]  (new list)
print(b)              # → [4, 1, 3]  (original unchanged!)

# Descending
print(sorted([4, 1, 3], reverse=True))   # → [3, 4, 1]

# Custom key
print(sorted(["banana", "apple", "fig"], key=lambda x: len(x)))
# → ['fig', 'apple', 'banana']


# ──────────────────────────────────────────
# Q2(b) How to get a random number in Python?
# ──────────────────────────────────────────

# The 'random' module provides multiple functions:

print(random.random())              # float in [0.0, 1.0)
print(random.randint(1, 10))        # int, BOTH endpoints inclusive
print(random.uniform(1.0, 10.0))    # float in [1.0, 10.0]
print(random.choice([10, 20, 30]))  # random element from a list

# NumPy random (for arrays)
print(np.random.rand(3))            # 3 random floats in [0, 1)
print(np.random.randint(1, 10, 5))  # 5 random ints in [1, 10)


# ──────────────────────────────────────────
# Q2(c) map() and reduce() functions
# ──────────────────────────────────────────

# map(function, iterable)
#   → applies function to EVERY element
#   → returns a lazy iterator (wrap in list() to see values)

nums = [1, 2, 3]
squared = list(map(lambda x: x * x, nums))
print(squared)    # → [1, 4, 9]

# reduce(function, iterable)
#   → reduces all elements to a SINGLE value
#   → applies function cumulatively: f(f(f(a, b), c), d)...
#   → must import from functools

nums2 = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums2)
print(total)    # → 10
# How it works: ((1+2)+3)+4 = 10


# ──────────────────────────────────────────
# Q2(d) reshape() vs resize() (again — asked in multiple papers)
# ──────────────────────────────────────────

# Already covered above. Key one-line summary:
# reshape → new view, same size, original safe
# resize  → in-place change, size can change, 0-filled if larger

a = np.array([1, 2, 3, 4])
print(a.reshape(2, 2))    # [[1 2] [3 4]] — new array

a.resize(2, 3)             # 6 elements but only 4 exist → pads with 0
print(a)                   # [[1 2 3] [4 0 0]]


# ──────────────────────────────────────────
# Q2(e) pivot_table vs crosstab
# ──────────────────────────────────────────

# crosstab    → counts FREQUENCY of category COMBINATIONS (default = count)
# pivot_table → aggregates a NUMERIC column (mean, sum, max, etc.)
#
# Memory Aid:
#   crosstab    = "COUNT pairs"
#   pivot_table = "AGGREGATE values"

df = pd.DataFrame({
    'Gender':   ['M', 'F', 'M', 'F', 'M'],
    'Result':   ['Pass', 'Pass', 'Fail', 'Pass', 'Pass'],
    'Score':    [80, 90, 45, 85, 75]
})

# crosstab: how many Male/Female passed or failed
print(pd.crosstab(df['Gender'], df['Result']))
# Result  Fail  Pass
# Gender
# F          0     2
# M          1     2

# pivot_table: average score for each Gender × Result combination
print(df.pivot_table(values='Score', index='Gender', columns='Result', aggfunc='mean'))


# ╔══════════════════════════════════════════════════════════╗
# ║         FEBRUARY 2025 ESA — SECTION A                   ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# Q1(a) List vs Tuple
# ──────────────────────────────────────────

# List  → MUTABLE  (can add, remove, change elements), uses []
# Tuple → IMMUTABLE (fixed after creation), uses ()
# Tuples are faster and can be used as dict keys (hashable)

a = [1, 2, 3]
a[0] = 10         # ✅ allowed — lists are mutable
print(a)          # → [10, 2, 3]

b = (1, 2, 3)
# b[0] = 10       # ❌ TypeError — tuples are immutable


# ──────────────────────────────────────────
# Q1(b) break and continue statements
# ──────────────────────────────────────────

# break    → exits the ENTIRE loop immediately
# continue → skips the CURRENT iteration and moves to the next

# break example
for i in range(5):
    if i == 3:
        break       # stop loop entirely when i is 3
    print(i)        # prints 0, 1, 2  (3 and 4 never reached)

# continue example
for i in range(5):
    if i == 3:
        continue    # skip when i is 3, but keep looping
    print(i)        # prints 0, 1, 2, 4  (3 is skipped)


# ──────────────────────────────────────────
# Q1(c) What is a dictionary?
# ──────────────────────────────────────────

# A dictionary stores data as KEY → VALUE pairs.
# Keys must be unique and immutable (str, int, tuple).
# Values can be any type and can repeat.
# Lookups are O(1) — extremely fast.

student = {
    "name": "Ram",
    "age":  20
}
print(student["name"])      # → Ram
print(student.get("age"))   # → 20  (safe access — won't crash if key missing)

# Add / update / delete
student["city"] = "BLR"     # add new key
student["age"]  = 21        # update existing
del student["city"]          # delete key


# ──────────────────────────────────────────
# Q1(d) String slicing with example
# ──────────────────────────────────────────

# Syntax: string[start : end : step]
#   start → inclusive (defaults to 0)
#   end   → EXCLUSIVE (defaults to len)
#   step  → how many to jump (defaults to 1)

s = "PythonProgramming"
print(s[0:6])    # → Python   (chars 0,1,2,3,4,5)
print(s[:6])     # → Python   (same — start defaults to 0)
print(s[6:])     # → Programming  (from index 6 to end)
print(s[::-1])   # → gnimmargorPnohtyP  (REVERSED)
print(s[2:9])    # → thonPro  (exam favourite!)


# ──────────────────────────────────────────
# Q1(e) Difference between append() and extend()
# ──────────────────────────────────────────

# append(x) → adds x as a SINGLE element (even if x is a list)
# extend(x) → unpacks x and adds each element INDIVIDUALLY

a = [1, 2]
a.append([3, 4])   # adds the LIST [3,4] as one element
print(a)           # → [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])   # unpacks [3,4] and adds 3 and 4 separately
print(b)           # → [1, 2, 3, 4]

# Rule: append = "add one thing", extend = "add many things"


# ──────────────────────────────────────────
# Q2(a) What is NumPy?
# ──────────────────────────────────────────

# NumPy = Numerical Python
# Core data structure: ndarray (n-dimensional array)
# Key advantages over Python lists:
#   Homogeneous (same type) → more memory efficient
#   Vectorized operations → no loops needed
#   Much faster (implemented in C)
#   Foundation for pandas, scikit-learn, TensorFlow

a = np.array([1, 2, 3])
print(a)             # [1 2 3]
print(a * 2)         # [2 4 6]  — no loop needed!
print(a.mean())      # 2.0


# ──────────────────────────────────────────
# Q2(b) What is Pandas?
# ──────────────────────────────────────────

# Pandas = Python library for data analysis and manipulation
# Two main structures:
#   Series    → 1D labeled array (one column)
#   DataFrame → 2D table (like Excel / SQL table)
# Key features: read CSV/Excel, handle missing data, groupby, merge

data = {"Name": ["Ram", "Sam"], "Age": [20, 22]}
df = pd.DataFrame(data)
print(df)
#   Name  Age
# 0  Ram   20
# 1  Sam   22


# ──────────────────────────────────────────
# Q2(c) Difference between Series and DataFrame
# ──────────────────────────────────────────

# Series    → ONE-dimensional, one column of data with an index
# DataFrame → TWO-dimensional, multiple columns (collection of Series)

s = pd.Series([1, 2, 3])             # 1D
print(s)

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})   # 2D
print(df)

# A DataFrame column IS a Series:
print(type(df["A"]))    # → <class 'pandas.core.series.Series'>


# ──────────────────────────────────────────
# Q2(d) iloc[] and loc[] (recap)
# ──────────────────────────────────────────

# Already covered in Feb 2025 Q1(c) above.
# Quick recap:
df = pd.DataFrame({"A": [10, 20, 30]}, index=["x", "y", "z"])
print(df.iloc[0])      # → 10  (position 0)
print(df.loc["x"])     # → 10  (label "x")


# ──────────────────────────────────────────
# Q2(e) What is data visualization?
# ──────────────────────────────────────────

# Data visualization represents data graphically (charts/plots)
# so patterns, trends, and outliers are easier to understand.
# Main libraries:
#   matplotlib → low-level, full control
#   seaborn    → high-level, beautiful defaults, built on matplotlib

x = [1, 2, 3]
y = [4, 5, 6]
plt.plot(x, y, marker='o')
plt.title('Simple Line Plot')
plt.xlabel('X'); plt.ylabel('Y')
plt.tight_layout(); plt.show()


# ╔══════════════════════════════════════════════════════════╗
# ║         OCTOBER 2024 ESA                                ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# Q1(a) Generate a random float between 0 and 1
# ──────────────────────────────────────────

# random.random() returns a float in [0.0, 1.0)
# 0 is possible, 1.0 is NEVER returned (exclusive upper bound)

print(random.random())    # e.g. 0.7234...

# To get float in a custom range [a, b]:
print(random.uniform(5.0, 10.0))


# ──────────────────────────────────────────
# Q1(b) Difference between pop() and remove()
# ──────────────────────────────────────────

# pop(index)  → removes by INDEX, RETURNS the removed element
#               default: removes and returns the LAST element
# remove(val) → removes by VALUE (first occurrence), returns None
#               raises ValueError if value not found

a = [10, 20, 30]
removed = a.pop()       # removes last element (30), returns 30
print(removed)          # → 30
print(a)                # → [10, 20]

b = [10, 20, 30]
b.pop(0)                # removes element at index 0 (10)
print(b)                # → [20, 30]

c = [10, 20, 30]
c.remove(20)            # removes the value 20
print(c)                # → [10, 30]
# c.remove(99)          # ❌ ValueError — 99 not in list


# ──────────────────────────────────────────
# Q1(c) filter() function — filter even numbers
# ──────────────────────────────────────────

# filter(function, iterable)
#   → keeps only elements for which function returns True
#   → returns a lazy iterator (use list() to materialise)

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)    # → [2, 4, 6]

# Equivalent with list comprehension (often preferred for clarity)
evens2 = [x for x in nums if x % 2 == 0]
print(evens2)   # → [2, 4, 6]


# ──────────────────────────────────────────
# Q1(d) enumerate() function
# ──────────────────────────────────────────

# enumerate(iterable, start=0)
#   → adds a COUNTER to each element during iteration
#   → yields (index, value) tuples
#   → useful when you need both the position AND the value

fruits = ["apple", "banana", "mango"]

for index, value in enumerate(fruits):
    print(index, value)
# 0 apple
# 1 banana
# 2 mango

# Start counting from 1 instead of 0
for index, value in enumerate(fruits, 1):
    print(index, value)
# 1 apple
# 2 banana
# 3 mango


# ──────────────────────────────────────────
# Q1(e) arange() vs linspace() in NumPy
# ──────────────────────────────────────────

# arange(start, stop, step) → specifies the STEP SIZE
#                              stop is EXCLUDED
# linspace(start, stop, n)  → specifies NUMBER OF POINTS
#                              stop is INCLUDED

print(np.arange(0, 10, 2))      # → [0 2 4 6 8]       (step = 2)
print(np.linspace(0, 10, 5))    # → [0. 2.5 5. 7.5 10.] (5 points)

# Key difference:
#   arange(0, 1, 0.25) → [0. 0.25 0.5 0.75]    (1.0 excluded)
#   linspace(0, 1, 5)  → [0. 0.25 0.5 0.75 1.] (1.0 INCLUDED)


# ──────────────────────────────────────────
# Q2(a) Filter rows in pandas based on condition
# ──────────────────────────────────────────

# Use boolean indexing: df[condition]
# For multiple conditions: use & (AND), | (OR), each in parentheses

df = pd.DataFrame({
    "Name":  ["A", "B", "C"],
    "Marks": [80, 45, 90]
})

result = df[df["Marks"] > 50]    # single condition
print(result)
#   Name  Marks
# 0    A     80
# 2    C     90

# Multiple conditions
result2 = df[(df["Marks"] > 50) & (df["Name"] != "C")]
print(result2)


# ──────────────────────────────────────────
# Q2(b) groupby() in pandas
# ──────────────────────────────────────────

# groupby() = Split → Apply → Combine
# Splits DataFrame into groups based on a column's values,
# applies an aggregation function, then combines results.

df = pd.DataFrame({
    "Dept":   ["IT", "IT", "HR"],
    "Salary": [5000, 6000, 4000]
})

result = df.groupby("Dept")["Salary"].mean()
print(result)
# Dept
# HR    4000.0
# IT    5500.0

# Other aggregations: .sum(), .count(), .max(), .min(), .std()


# ──────────────────────────────────────────
# Q2(c) Remove missing data from a DataFrame
# ──────────────────────────────────────────

# dropna() removes rows (or columns) containing NaN values
# fillna() replaces NaN with a specified value

df = pd.DataFrame({
    "Name":  ["Alice", "Bob", None],
    "Score": [80, None, 90]
})

print(df.dropna())               # drop rows with ANY NaN
print(df.dropna(subset=["Score"]))  # drop only if 'Score' is NaN
print(df.fillna(0))              # replace NaN with 0
print(df["Score"].fillna(df["Score"].mean()))  # fill with column mean


# ──────────────────────────────────────────
# Q2(d) apply() vs map() in pandas
# ──────────────────────────────────────────

# apply()  → works on SERIES or ENTIRE DATAFRAME
#             used for row-wise (axis=1) or column-wise operations
# map()    → works on a SERIES only, element-wise transformation
#             best for simple element substitutions

df = pd.DataFrame({"Marks": [80, 45, 90]})

# map: simple element-wise transformation
df["Grade_map"] = df["Marks"].map(lambda x: "Pass" if x >= 50 else "Fail")

# apply: can use more complex logic, works on Series and DataFrames
df["Grade_apply"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")
print(df)

# apply with axis=1 (row-wise, uses multiple columns)
df["Total"] = df.apply(lambda row: row["Marks"] + 10, axis=1)


# ──────────────────────────────────────────
# Q2(e) reset_index()
# ──────────────────────────────────────────

# reset_index() resets the DataFrame index to the default 0, 1, 2, ...
# The old index becomes a regular column (unless drop=True is used)

df = pd.DataFrame({"A": [10, 20]}, index=[1, 2])
print(df.reset_index())
#    index   A
# 0      1  10
# 1      2  20

print(df.reset_index(drop=True))   # discard old index, don't keep as column
#     A
# 0  10
# 1  20


# ╔══════════════════════════════════════════════════════════╗
# ║         MARCH 2024 ESA                                  ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# Q1(a) What is type casting?
# ──────────────────────────────────────────

# Type casting = converting a value from one data type to another
# Implicit: Python does it automatically (int + float → float)
# Explicit: programmer uses int(), float(), str(), bool(), etc.

# Implicit
result = 10 + 5.5      # int + float → automatically becomes float
print(result)          # → 15.5
print(type(result))    # → <class 'float'>

# Explicit
a = "10"
b = int(a)             # manually convert str to int
print(b)               # → 10
print(type(b))         # → <class 'int'>

# Important: int() TRUNCATES decimals (does NOT round)
print(int(3.99))       # → 3 (not 4!)


# ──────────────────────────────────────────
# Q1(c) Lambda function + sum of list elements
# ──────────────────────────────────────────

# Lambda = anonymous one-line function
# Syntax: lambda arguments: expression

nums = [5, 8, 10, 20, 50, 100]

# Lambda that computes the sum of a list
result = lambda x: sum(x)
print(result(nums))     # → 193

# Immediate invocation (IIFE style)
print((lambda x: sum(x))([5, 8, 10, 20, 50, 100]))   # → 193


# ──────────────────────────────────────────
# Q1(e) *args and **kwargs
# ──────────────────────────────────────────

# *args   → accepts ANY NUMBER of positional arguments → stored as TUPLE
# **kwargs → accepts ANY NUMBER of keyword (name=value) arguments → stored as DICT

def demo(*args, **kwargs):
    print(type(args), args)       # <class 'tuple'> (1, 2, 3)
    print(type(kwargs), kwargs)   # <class 'dict'>  {'name': 'Ram'}

demo(1, 2, 3, name="Ram")
# (1, 2, 3)
# {'name': 'Ram'}


# ──────────────────────────────────────────
# Q2(a) pivot_table vs crosstab (March 2024)
# ──────────────────────────────────────────

# (Already explained above. Key one-liners:)
# pd.crosstab(df.A, df.B)                        → counts combinations
# df.pivot_table(values='V', index='A', columns='B', aggfunc='mean')
#                                                → aggregates numeric column


# ──────────────────────────────────────────
# Q2(c) Ranking methods for Series
# ──────────────────────────────────────────

# rank() assigns a rank to each element.
# When values are TIED, the method determines how to handle them.
#
# Method    Behavior                    Memory aid (AMFMD)
# average   tied positions get average  DEFAULT
# min       tied positions get minimum
# max       tied positions get maximum
# first     rank by order of appearance
# dense     like min but NO GAPS in ranks

s = pd.Series([100, 200, 200, 300])

print(s.rank(method='average'))  # [1.0, 2.5, 2.5, 4.0]  ← both 200s get avg of 2+3
print(s.rank(method='min'))      # [1.0, 2.0, 2.0, 4.0]
print(s.rank(method='max'))      # [1.0, 3.0, 3.0, 4.0]
print(s.rank(method='first'))    # [1.0, 2.0, 3.0, 4.0]  ← first 200 gets rank 2
print(s.rank(method='dense'))    # [1.0, 2.0, 2.0, 3.0]  ← no gap: 1,2,2,3 not 1,2,2,4


# ──────────────────────────────────────────
# Q2(d) GroupBy in Pandas (recap)
# ──────────────────────────────────────────

df = pd.DataFrame({
    "Dept":   ["IT", "IT", "HR"],
    "Salary": [5000, 6000, 4000]
})
print(df.groupby("Dept")["Salary"].mean())


# ──────────────────────────────────────────
# Q2(e) Plot for data distribution
# ──────────────────────────────────────────

# Histogram is the primary plot for DISTRIBUTION of a single numeric column.
# Other options: Box Plot (shows outliers + quartiles), KDE/Density Plot

data = [1, 2, 2, 3, 3, 3, 4]

plt.figure(figsize=(7, 4))
plt.hist(data, bins=10, color='steelblue', edgecolor='white')
plt.title('Data Distribution (Histogram)')
plt.xlabel('Value'); plt.ylabel('Frequency')
plt.tight_layout(); plt.show()

# Seaborn version with KDE curve (preferred)
# sns.histplot(data, bins=10, kde=True)


# ╔══════════════════════════════════════════════════════════╗
# ║         MARCH 2024 SCAN — SECTION A                     ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# Q1(a) Count occurrences of element in a list
# ──────────────────────────────────────────

# list.count(value) → returns how many times value appears
# Returns 0 if not found — NO error (unlike list.index())

a = ["a", "b", "a"]
print(a.count("a"))    # → 2
print(a.count("x"))    # → 0  (not found, no crash)


# ──────────────────────────────────────────
# Q1(b) Global keyword in Python
# ──────────────────────────────────────────

# By default, assigning a variable inside a function creates a LOCAL copy.
# The global keyword tells Python: "use the GLOBAL variable, not a local one."
# You only need 'global' when you want to WRITE/MODIFY a global variable.
# Reading a global variable works fine without the keyword.

x = 10

def demo():
    global x       # now x refers to the global x above
    x = 20         # modifies the global x

demo()
print(x)           # → 20  (global was changed)


# ──────────────────────────────────────────
# Q1(d) List and Dictionary comprehensions
# ──────────────────────────────────────────

# Comprehensions = compact one-line way to create lists or dicts
# Pattern: [expression  for variable in iterable  if condition]

# List comprehension
squares = [x * x for x in range(5)]
print(squares)    # → [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)      # → [0, 2, 4, 6, 8]

# Dictionary comprehension
d = {x: x * x for x in range(5)}
print(d)          # → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition in dict comprehension
d2 = {x: x**2 for x in range(10) if x % 2 == 0}
print(d2)


# ──────────────────────────────────────────
# Q1(e) Negative indexing in Python
# ──────────────────────────────────────────

# Negative indices count from the END of the sequence.
# -1 = last element, -2 = second last, -n = nth from end.
# Works on lists, strings, tuples, and NumPy arrays.

a = [10, 20, 30, 40]
print(a[-1])     # → 40  (last element)
print(a[-2])     # → 30  (second to last)
print(a[-4])     # → 10  (same as a[0])

s = "Python"
print(s[-1])     # → 'n'
print(s[-3:])    # → 'hon'  (last 3 characters)


# ──────────────────────────────────────────
# Q2(a) Remove duplicates from DataFrame
# ──────────────────────────────────────────

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Alice"],
    "Age":  [25, 30, 25]
})

print(df.drop_duplicates())           # keep first occurrence
print(df.drop_duplicates(keep='last'))  # keep last occurrence
print(df.duplicated().sum())          # count of duplicate rows


# ──────────────────────────────────────────
# Q2(b) Identify and handle missing values
# ──────────────────────────────────────────

df = pd.DataFrame({
    "A": [1, None, 3],
    "B": [4, 5, None]
})

# IDENTIFY
print(df.isnull())              # True where NaN
print(df.isnull().sum())        # count per column
print(df.isnull().sum().sum())  # total NaN count

# HANDLE — remove
print(df.dropna())              # drop rows with ANY NaN

# HANDLE — fill
print(df.fillna(0))             # fill with constant 0
print(df.fillna(df.mean()))     # fill each column with its mean


# ──────────────────────────────────────────
# Q2(d) vstack() vs hstack() in NumPy
# ──────────────────────────────────────────

# vstack (vertical stack)   → join arrays as new ROWS (more rows)
# hstack (horizontal stack) → join arrays as new COLUMNS (more cols)

a = np.array([1, 2])
b = np.array([3, 4])

print(np.vstack((a, b)))
# [[1 2]
#  [3 4]]

print(np.hstack((a, b)))
# [1 2 3 4]


# ╔══════════════════════════════════════════════════════════╗
# ║         NOVEMBER 2023 ESA                               ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# Q1(c) del, clear, remove, pop differences
# ──────────────────────────────────────────

# del       → remove by INDEX or delete entire variable
# clear()   → remove ALL elements, list becomes []
# remove(v) → remove FIRST occurrence of VALUE v (ValueError if missing)
# pop(i)    → remove by INDEX and RETURN the removed element

a = [1, 2, 3, 4, 5]

del a[0]          # removes element at index 0
print(a)          # → [2, 3, 4, 5]

a.remove(3)       # removes the VALUE 3
print(a)          # → [2, 4, 5]

popped = a.pop()  # removes and returns LAST element
print(popped)     # → 5
print(a)          # → [2, 4]

a.clear()         # empties the entire list
print(a)          # → []


# ──────────────────────────────────────────
# Q2(a) Combining DataFrames — concat, merge, join
# ──────────────────────────────────────────

# concat → STACK DataFrames (add rows or columns)
# merge  → SQL-style JOIN on a common column
# join   → JOIN on the INDEX

df1 = pd.DataFrame({"A": [1, 2]})
df2 = pd.DataFrame({"A": [3, 4]})

# Stack rows vertically
result = pd.concat([df1, df2], ignore_index=True)
print(result)
# A
# 0  1
# 1  2
# 2  3
# 3  4


# ──────────────────────────────────────────
# Q2(e) sort_values() vs sort_index()
# ──────────────────────────────────────────

# sort_values() → sort by the DATA values in the Series/column
# sort_index()  → sort by the INDEX LABELS (row labels)

s = pd.Series([30, 10, 20], index=['c', 'a', 'b'])

print(s.sort_values())
# a    10
# b    20
# c    30

print(s.sort_index())
# a    10
# b    20
# c    30
# (coincidentally same here since alphabetical = value order)

# Memory Aid:
#   sort_values → sort by DATA
#   sort_index  → sort by LABELS


# ╔══════════════════════════════════════════════════════════╗
# ║         AUGUST 2021 ESA                                 ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# Q1(a) Immutable built-in datatypes
# ──────────────────────────────────────────

# Immutable = content CANNOT be changed after creation.
# Any "modification" creates a NEW object.
# Immutable types: int, float, bool, str, tuple, frozenset, bytes
#
# Memory Aid (IFBSTFB): Int Float Bool Str Tuple Frozenset Bytes

s = "Python"
# s[0] = 'J'     # ❌ TypeError — string is immutable

s = "Jython"     # ✅ creates a NEW string — 'Python' still exists
print(s)         # → Jython

# Tuple also immutable
t = (1, 2, 3)
# t[0] = 99      # ❌ TypeError


# ──────────────────────────────────────────
# Q1(e) Is Python statically or dynamically typed?
# ──────────────────────────────────────────

# Python is DYNAMICALLY TYPED.
# Variable type is decided at RUNTIME, not at declaration.
# No need to declare types like int x; or String s;
# The same variable name can hold different types at different times.

x = 10
print(type(x))      # → <class 'int'>

x = "Python"        # same variable name, completely different type
print(type(x))      # → <class 'str'>

x = [1, 2, 3]
print(type(x))      # → <class 'list'>


# ──────────────────────────────────────────
# Q2(c) Matrices vs Arrays
# ──────────────────────────────────────────

# Array  → general n-dimensional structure, can be any shape
# Matrix → strictly 2D, special case of array
# In NumPy, np.matrix is deprecated — use 2D np.array instead.
# @ operator for matrix multiplication works on both.

a = np.array([[1, 2], [3, 4]])    # 2D array (used as matrix)
b = np.array([[5, 6], [7, 8]])

print(a @ b)    # matrix multiplication
# [[19 22]
#  [43 50]]

print(a * b)    # element-wise multiplication (NOT matrix multiply)
# [[ 5 12]
#  [21 32]]


# ──────────────────────────────────────────
# Q2(d) Create multi-dimensional array from 1D using reshape()
# ──────────────────────────────────────────

a = np.array([1, 2, 3, 4, 5, 6])   # 1D array with 6 elements

b = a.reshape(2, 3)    # reshape to 2 rows × 3 cols (2×3 = 6 ✅)
print(b)
# [[1 2 3]
#  [4 5 6]]

c = a.reshape(3, 2)    # reshape to 3 rows × 2 cols
print(c)
# [[1 2]
#  [3 4]
#  [5 6]]

# Use -1 to auto-compute one dimension
d = a.reshape(2, -1)   # 2 rows, NumPy calculates 3 cols
print(d.shape)         # (2, 3)


# ╔══════════════════════════════════════════════════════════╗
# ║         JULY 2021 ESA                                   ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# Q1(b) find() vs index() for strings
# ──────────────────────────────────────────

# find()  → returns the starting index of the substring if found
#            returns -1 if NOT found (SAFE — no crash)
# index() → returns the starting index if found
#            raises ValueError if NOT found (RISKY)

s = "Python"
print(s.find("t"))      # → 2   (found at index 2)
print(s.find("xyz"))    # → -1  (not found, no error!)

print(s.index("t"))     # → 2   (found at index 2)
# print(s.index("xyz")) # ❌ ValueError!

# Memory Aid:
#   find  = "Find or return -1"
#   index = "Index or Explode!"


# ──────────────────────────────────────────
# Q1(d) Change value associated with a key in a dictionary
# ──────────────────────────────────────────

# Use dictionary[key] = new_value to update an existing key's value.
# If the key doesn't exist, this ADDS a new key (same syntax for both!)

student = {"name": "Ram", "age": 20}
student["age"] = 25        # update existing key
print(student)             # → {'name': 'Ram', 'age': 25}

# Can also use .update() for multiple keys at once
student.update({"age": 26, "city": "BLR"})
print(student)


# ──────────────────────────────────────────
# Q1(e) Anonymous functions (lambda)
# ──────────────────────────────────────────

# Lambda = function without a name
# Syntax: lambda arguments: expression
# No 'def', no 'return', no name required.

square = lambda x: x * x
print(square(5))     # → 25

add = lambda a, b: a + b
print(add(3, 7))     # → 10

# Commonly used with map, filter, sorted
words = ["banana", "fig", "apple"]
print(sorted(words, key=lambda x: len(x)))  # → ['fig', 'apple', 'banana']


# ──────────────────────────────────────────
# Q2(a) Identity matrix using NumPy
# ──────────────────────────────────────────

# Identity matrix: square matrix with 1s on the DIAGONAL, 0s elsewhere
# Property: A × I = A  (multiplying by identity doesn't change the matrix)
# np.eye(n) or np.identity(n) both create an n×n identity matrix

print(np.eye(3))
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Verify A × I = A
A = np.array([[2, 3], [4, 5]])
I = np.eye(2)
print(A @ I)    # → same as A


# ──────────────────────────────────────────
# Q2(b) split() for arrays
# ──────────────────────────────────────────

# np.split(array, n) → splits into n EQUAL parts
# np.split(array, [i, j]) → splits AT indices i and j
# np.array_split() → allows UNEQUAL splits (no error for odd sizes)

a = np.array([1, 2, 3, 4, 5, 6])

print(np.split(a, 3))       # → [array([1,2]), array([3,4]), array([5,6])]
print(np.split(a, [2, 4]))  # → [array([1,2]), array([3,4]), array([5,6])]


# ──────────────────────────────────────────
# Q2(e) Plot for data distribution
# ──────────────────────────────────────────

# (Already shown above — same answer for all papers asking this)
# Histogram: plt.hist(data) or sns.histplot(data, kde=True)
# Box Plot:  sns.boxplot(data=df, y='col')
# KDE Plot:  sns.kdeplot(data)


# ╔══════════════════════════════════════════════════════════╗
# ║         MODEL SET ESA                                   ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────
# Q1(a) Python is case-sensitive — demonstration
# ──────────────────────────────────────────

# Python treats uppercase and lowercase as COMPLETELY DIFFERENT.
# 'name', 'Name', and 'NAME' are three separate variables.
# Keywords must also be lowercase: 'if', 'for', 'def' (not 'If' or 'FOR')

name = "Python"
Name = "Programming"

print(name)    # → Python
print(Name)    # → Programming  (different variable!)

# This also applies to function names, class names, module names, etc.


# ──────────────────────────────────────────
# Q1(b) Implicit type casting — 2 examples
# ──────────────────────────────────────────

# Python automatically promotes to a WIDER type when types are mixed.
# int → float → complex  (promotion hierarchy)

# Example 1: int + float → float
a = 10
b = 5.5
c = a + b
print(c)           # → 15.5
print(type(c))     # → <class 'float'>

# Example 2: bool + int → int (True = 1, False = 0)
x = True
y = 5
print(x + y)       # → 6  (True is treated as 1)
print(type(x + y)) # → <class 'int'>


# ──────────────────────────────────────────
# Q1(c) Complex data type in Python
# ──────────────────────────────────────────

# Complex numbers have a REAL part and an IMAGINARY part.
# Written as: a + bj  (Python uses 'j', not 'i')
# Used in signal processing, scientific computing.

x = 4 + 5j
print(x)           # → (4+5j)
print(type(x))     # → <class 'complex'>
print(x.real)      # → 4.0   (real part)
print(x.imag)      # → 5.0   (imaginary part)


# ──────────────────────────────────────────
# Q1(d) Default parameter in user-defined functions
# ──────────────────────────────────────────

# A default parameter has a value assigned in the def line.
# If the caller doesn't provide that argument, the default is used.
# ⚠️ RULE: default parameters MUST come AFTER non-default parameters!

def greet(name="Guest"):    # "Guest" is the default
    print("Hello", name)

greet()           # → Hello Guest  (uses default)
greet("Ram")      # → Hello Ram    (overrides default)


# ──────────────────────────────────────────
# Q1(e) Arithmetic operators with strings
# ──────────────────────────────────────────

# Strings support ONLY two arithmetic operators:
#   +  → concatenation (joins two strings)
#   *  → repetition (repeats string n times)
# All other operators (-, /, //, %, **) → TypeError on strings

a = "Python"
b = "Programming"

print(a + b)    # → PythonProgramming  (concatenation)
print(a * 3)    # → PythonPythonPython (repetition)

# These do NOT work on strings:
# a - b    ❌ TypeError
# a / 2    ❌ TypeError


# ──────────────────────────────────────────
# Q2(a) Features of NumPy
# ──────────────────────────────────────────

# (Covered in Day 7 notes. Key features:)
# ndarray, vectorized ops, broadcasting, C-speed, memory efficient,
# linear algebra, np.random, foundation for pandas/scikit-learn

a = np.array([1, 2, 3])
print(a * 2)         # [2 4 6]  — vectorized, no loop
print(a.mean())      # 2.0
print(np.eye(3))     # identity matrix


# ──────────────────────────────────────────
# Q2(c) NumPy random package
# ──────────────────────────────────────────

# np.random provides functions to generate random numbers in arrays.

print(np.random.rand(3))            # 3 random floats in [0, 1)
print(np.random.rand(2, 3))         # 2×3 matrix of random floats
print(np.random.randint(1, 10, 5))  # 5 random ints in [1, 10)
print(np.random.normal(0, 1, 100))  # 100 values from N(mean=0, std=1)
print(np.random.choice([10, 20, 30], 4))  # 4 random picks from the list

# Set seed for reproducibility
np.random.seed(42)
print(np.random.rand(3))   # same values every run with seed=42


# ──────────────────────────────────────────
# Q2(d) Delete rows and columns from a DataFrame
# ──────────────────────────────────────────

# df.drop(label, axis=0) → drop ROW by index label
# df.drop(label, axis=1) → drop COLUMN by name
# Use inplace=True to modify original, or reassign (df = df.drop(...))

df = pd.DataFrame({
    "Name":   ["Alice", "Bob", "Carol"],
    "Age":    [25, 30, 35],
    "Salary": [50000, 70000, 60000]
})

print(df.drop(0))                      # drop row with index 0
print(df.drop([0, 1]))                 # drop rows 0 and 1
print(df.drop("Age", axis=1))          # drop column 'Age'
print(df.drop(["Age", "Salary"], axis=1))  # drop multiple columns
print(df.drop(columns=["Age"]))        # cleaner syntax for columns


# ──────────────────────────────────────────
# Q2(e) Rank rows of a DataFrame
# ──────────────────────────────────────────

# df.rank() assigns a rank to each value in numeric columns.
# Default method='average' for ties.

df = pd.DataFrame({"Marks": [90, 70, 80]})
print(df.rank())
#    Marks
# 0    3.0   (90 is highest → rank 3)
# 1    1.0   (70 is lowest  → rank 1)
# 2    2.0   (80 is middle  → rank 2)

# Rank in descending order (highest value = rank 1)
print(df.rank(ascending=False))
#    Marks
# 0    1.0
# 1    3.0
# 2    2.0

# Apply to a Series
s = pd.Series([100, 200, 200, 300])
print(s.rank(method='dense'))   # [1.0, 2.0, 2.0, 3.0]  (no gaps)


# ============================================================
# MASTER QUICK REFERENCE — Most Repeated Questions
# ============================================================

# is vs ==          → is = same object, == = same value
# loc vs iloc       → loc = label (inclusive), iloc = position (exclusive)
# sort vs sorted    → sort() in-place+None, sorted() new list
# append vs extend  → append = one item, extend = unpack + add many
# find vs index     → find = -1 if missing, index = ValueError if missing
# pop vs remove     → pop(i) = by index+returns, remove(v) = by value
# any vs all        → any = at least one, all = every element
# reshape vs resize → reshape = new view, resize = in-place
# vstack vs hstack  → V = more rows, H = more cols
# arange vs linspace→ arange = step size, linspace = num points
# crosstab vs pivot → crosstab = count, pivot_table = aggregate
# map vs apply      → map = element-wise Series, apply = Series or DF
# *args vs **kwargs → *args = tuple of positionals, **kwargs = dict of keywords
# sort_values vs sort_index → values = data, index = labels

# ============================================================
# End of ESA Previous Year Notes — Good luck!
# ============================================================
