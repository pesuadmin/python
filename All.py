
# ────────────────────────────────────────────────────────────
# 📦 SECTION 2 — VARIABLES
# ────────────────────────────────────────────────────────────


# ━━━ What is a Variable? ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A variable is a name that points to a value in memory . Think of it as a labeled box that holds
# something.

# Memory:        ┌─────────┐
#                │   42    │  ← actual value stored
#                └─────────┘
#                     ▲
#                     │  points to
#                   age          ← variable name (the label)


# ━━━ Naming Rules ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# [Rule]  [✅ Valid]  [❌ Invalid]
# Letters, digits, underscore only |  my_age, x1, _temp |  my-age, my age, my@age |
# Cannot start with digit |  name1 |  1name |
# Case-sensitive |  name and Name are different |  — |
# Cannot use Python keywords |  my_class |  class, if, for |


# ── 🔹 Examples ──────────────────────────────────────

#
# # ── Creating variables (assignment with =) ──
# age = 25                  # integer
# name = "Rajesh"            # string
# height = 5.9               # float (decimal)
# is_student = True          # boolean
#
# # ── Multiple assignment ──
# a, b, c = 1, 2, 3           # a=1, b=2, c=3
# x = y = z = 0               # all three set to 0
#
# # ── Reassignment ──
# age = 26                  # overwrite previous value
# age = age + 1              # now 27
# age += 1                   # shorthand: age = age + 1, now 28


# ────────────────────────────────────────────────────────────
# 🔢 SECTION 3 — DATA TYPES
# ────────────────────────────────────────────────────────────


# ━━━ Built-in Data Types — All 8 Categories ━━━━━━━━━━━━━━

# [Type]  [Example]  [What it stores]  [Mutable?]
# int |  42, -10, 0 |  Whole numbers |  ❌ Immutable |
# float |  3.14, -2.5 |  Decimal numbers |  ❌ Immutable |
# bool |  True, False |  Logical values |  ❌ Immutable |
# complex |  3 + 4j |  Complex numbers (real + imaginary) |  ❌ Immutable |
# str |  "hello" |  Text (sequence of characters) |  ❌ Immutable |
# list |  [1, 2, 3] |  Ordered, changeable collection |  ✅ Mutable |
# tuple |  (1, 2, 3) |  Ordered, fixed collection |  ❌ Immutable |
# dict |  {"a": 1, "b": 2} |  Key-value pairs |  ✅ Mutable |
# set |  {1, 2, 3} |  Unique, unordered collection |  ✅ Mutable |


# ── 🧠 Memory Aid — IFBSTFB ──────────────────────────
# Immutable types : I nt, F loat, B ool, S tr, T uple, F rozenset, B ytes
# Mutable types : list, dict, set

# ── 🔹 Mutable vs Immutable — Why It Matters ─────────
#   • Immutable = cannot be changed. Any "modification" creates a NEW object
#   • Mutable = can be changed in-place. Same object stays in memory
#   • Only immutable types can be used as dictionary keys or set elements

# ── 🔹 Demonstration ─────────────────────────────────


# ── IMMUTABLE: string cannot be modified ──
s = "hello"
# s[0] = "H"   ← ❌ TypeError!
s2 = "H" + s[1:]    # ✅ creates NEW string "Hello"
print(s)              # still "hello" (unchanged)

# ── IMMUTABLE: tuple cannot be modified ──
t = (1, 2, 3)
# t[0] = 99    ← ❌ TypeError!

# ── MUTABLE: list can be modified in-place ──
lst = [1, 2, 3]
lst[0] = 99          # ✅ allowed
lst.append(4)        # ✅ adds element
print(lst)            # → [99, 2, 3, 4]

# ── Tuple as dict key (works) ──
locations = {(10, 20): "Office"}    # ✅ tuple is hashable

# ── List as dict key (fails) ──
# bad = {[1,2]: "x"}   ← ❌ TypeError: list is unhashable


# ────────────────────────────────────────────────────────────
# 🔄 SECTION 4 — TYPE CASTING (CONVERSION)
# ────────────────────────────────────────────────────────────


# ━━━ What is Type Casting? ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Type casting = converting a value from one data type to another. Two kinds:
#   • Implicit: Python does it automatically (silent)
#   • Explicit: Programmer does it manually using built-in functions

# ── 🔹 IMPLICIT (Automatic) ──────────────────────────


# Python automatically promotes to wider type
result = 5 + 2.0         # int + float → float
print(result)             # → 7.0  (NOT 7!)
print(type(result))       # → 

# int + complex → complex
result2 = 3 + 2j
print(result2)            # → (3+2j)

# Promotion order: int → float → complex
# Python NEVER auto-converts str ↔ int (would lose data)


# ── 🔹 EXPLICIT (Manual) ─────────────────────────────

#
# # ── Convert TO int ──
# int("42")             # str → int: 42
# int(3.99)             # float → int: 3 (TRUNCATES, not rounds!)
# int(True)             # bool → int: 1
# int(False)            # bool → int: 0
#
# # ── Convert TO float ──
# float(10)             # int → float: 10.0
# float("3.14")         # str → float: 3.14
#
# # ── Convert TO str ──
# str(42)               # int → str: "42"
# str(3.14)             # float → str: "3.14"
#
# # ── Convert TO bool ──
# bool(0)               # → False (only 0 is falsy)
# bool(42)              # → True (any non-zero)
# bool("")              # → False (empty string)
# bool("hello")         # → True (non-empty)
# bool([])              # → False (empty list)
#
# # ── Convert TO list/tuple ──
# list((1,2,3))         # tuple → list: [1, 2, 3]
# tuple([1,2,3])         # list → tuple: (1, 2, 3)
# list("abc")            # str → list: ['a', 'b', 'c']


# ── ⚠️ Common Mistakes ──────────────────────────────
#   • int(3.99) = 3, not 4. Python TRUNCATES (cuts off decimals), does NOT round. Use round(3.99) = 4 if you need rounding.
#   • int("3.14") ❌ ValueError! Use int(float("3.14")) = 3
#   • Cannot add string to int directly: "5" + 3 ❌. Convert first: int("5") + 3 = 8

# ── 🧠 Memory Aid ────────────────────────────────────
# 🧠 Implicit = Invisible upgrade · Explicit = Enforced conversion
# Truncation rule : `int(any decimal)` = drop the decimal part, NEVER rounds
# Falsy values : 0, 0.0, "", [], {}, None, False

# ── 🔁 Reusable Pattern: Safe Type Casting ───────────


def safe_int(value, default=0):
    "Convert value to int, return default if fails."
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

# Usage: handles bad input safely
print(safe_int("42"))      # → 42
print(safe_int("abc"))     # → 0 (didn't crash)
print(safe_int(None))      # → 0


# ────────────────────────────────────────────────────────────
# ➕ SECTION 5 — OPERATORS
# ────────────────────────────────────────────────────────────


# ━━━ Categories of Operators ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ━━━ 1. Arithmetic Operators ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# [Operator]  [Name]  [Example]  [Result]
# + |  Addition |  5 + 3 |  8 |
# - |  Subtraction |  5 - 3 |  2 |
# * |  Multiplication |  5 * 3 |  15 |
# / |  True Division |  5 / 2 |  2.5 (always float) |
# // |  Floor Division |  5 // 2 |  2 (integer division) |
# % |  Modulus |  5 % 2 |  1 (remainder) |
# ** |  Exponent |  2 ** 3 |  8 (2 to power 3) |


# ━━━ 2. Comparison Operators (return True/False) ━━━━━━━━━

# [Operator]  [Meaning]  [Example]  [Result]
# == |  Equal to |  5 == 5 |  True |
# != |  Not equal |  5 != 3 |  True |
# > |  Greater than |  5 > 3 |  True |
# = |  Greater or equal |  5 >= 5 |  True |
# 0) and (x   5) |


# ━━━ 4. Identity & Membership ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# [Operator]  [Meaning]  [Example]
# is |  Same object in memory |  x is None |
# is not |  Different object |  x is not None |
# in |  Element exists in collection |  "a" in "apple" |
# not in |  Element does NOT exist |  5 not in [1,2,3] |


# ⚠️ WARN: ⚠️ == vs is: Use == for value comparison (5 == 5.0 is True). Use is only for None, True,
# False checks.


# ━━━ 5. String Operators (only 2!) ━━━━━━━━━━━━━━━━━━━━━━━

#
# # Only + (concatenation) and * (repetition) work on strings
# "Hello" + " World"     # → "Hello World"
# "Ha" * 3                # → "HaHaHa"
#
# # These do NOT work:
# # "Hello" - "lo"   ❌ TypeError
# # "Hello" / 2      ❌ TypeError


# ────────────────────────────────────────────────────────────
# ⌨️ SECTION 6 — INPUT / OUTPUT
# ────────────────────────────────────────────────────────────


# ━━━ input() — Read from User ━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# input() ALWAYS returns a string!
name = input("Enter your name: ")
print("Hello, " + name)

# For numbers, you MUST cast:
age = int(input("Enter age: "))     # cast to int
salary = float(input("Salary: "))    # cast to float

# Read multiple values (space-separated)
a, b = map(int, input("Two numbers: ").split())


# ━━━ print() — Display Output ━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# Basic print
print("Hello")                # → Hello

# Multiple values (space-separated by default)
print("Name:", name, "Age:", age)

# Custom separator
print("a","b","c", sep="-")        # → a-b-c

# Custom end (default is newline)
print("Hello", end=" ")            # no newline
print("World")                  # → Hello World

# f-strings (BEST way to format!)
name = "Alice"; age = 25
print(f"My name is {name} and I am {age}")

# Format numbers with f-strings
pi = 3.14159
print(f"{pi:.2f}")               # → 3.14 (2 decimals)
print(f"{1000000:,}")             # → 1,000,000 (with commas)


# ── 🔁 Reusable Pattern: Read N Numbers from User ────


def read_numbers(n):
    "Read n numbers from user, return as list."
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    return numbers

# Reuse for any "enter N numbers" question
nums = read_numbers(10)
print("You entered:", nums)


# ────────────────────────────────────────────────────────────
# 🎲 SECTION 7 — RANDOM NUMBERS
# ────────────────────────────────────────────────────────────

# Random numbers are tested in 4 papers . Master this.

# ── 🔹 Python's random module ────────────────────────


import random

# Float in [0.0, 1.0)
random.random()              # e.g. 0.7234

# Integer between a and b (BOTH inclusive)
random.randint(1, 100)        # e.g. 42

# Float between a and b
random.uniform(5, 10)         # e.g. 7.83

# Random element from list
random.choice(['a','b','c']) # e.g. 'b'

# Multiple random elements (with replacement)
random.choices([1,2,3], k=5)   # e.g. [1,3,1,2,3]

# Random sample (without replacement)
random.sample([1,2,3,4,5], 3) # e.g. [3,1,5]

# Shuffle a list in-place
lst = [1,2,3,4,5]
random.shuffle(lst)            # lst is now reordered

# Reproducibility (same random numbers each run)
random.seed(42)               # set seed BEFORE other random calls


# ────────────────────────────────────────────────────────────
# 🧠 SECTION 8 — MEMORY AIDS & EXAM TIPS
# ────────────────────────────────────────────────────────────


# ━━━ 🎯 Type Casting Mnemonics ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • int() truncates, doesn't round
#   • str() always works on any type
#   • bool(0) = False, anything else = True
#   • Falsy values: 0, 0.0, "", [], {}, None

# ━━━ 📋 Mutable vs Immutable ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • Immutable (IFBSTFB): Int, Float, Bool, Str, Tuple, Frozenset, Bytes
#   • Mutable: list, dict, set
#   • Only immutable can be dict keys

# ━━━ ⚡ Operator Precedence (high to low) ━━━━━━━━━━━━━━━━━
#   • ** (exponent)
#   • *, /, //, %
#   • +, -
#   • Comparisons: ==, <, >
#   • not
#   • and
#   • or

# ━━━ 🔤 String + Operator Reminder ━━━━━━━━━━━━━━━━━━━━━━━━
#   • Strings: ONLY + and * work
#   • + → concatenate
#   • * → repeat
#   • Any other arithmetic → TypeError

# ────────────────────────────────────────────────────────────
# 🏋️ SECTION 9 — PRACTICE PROBLEMS
# ────────────────────────────────────────────────────────────

# Try these in your notebook. Solutions are in matching topic files (5_STRINGS, 6_LISTS, etc.)
#   • Type casting: Read a number from input, multiply by 2, print result. Handle the case where user types non-number.
#   • Operators: Read 2 numbers, print sum, difference, product, quotient, remainder, and power.
#   • Mutability: Show that adding a tuple to a dict as key works; adding a list does not.
#   • Strings: Take a name, repeat it 5 times with separator " - " between each. (Hint: combine + and *)
#   • Random: Generate 10 random numbers between 1 and 100 with seed=42 (so result is reproducible).
# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ╔════════════════════════════════════════════════════════════╗
# ║  FILE 03 — Control Flow                                    ║
# ╚════════════════════════════════════════════════════════════╝


# ────────────────────────────────────────────────────────────
# 🚦 SECTION 1 — IF-ELSE (DECISIONS)
# ────────────────────────────────────────────────────────────


# ━━━ What is if-else? ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# It's how you tell Python: " If this is true, do X; otherwise, do Y ". The basis of all
# decision-making in code.

# ━━━ Basic Syntax ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


if condition:
    # do something (must be indented!)
    print("Yes")
elif another_condition:    # optional, can have many elif
    print("Maybe")
else:                       # optional fallback
    print("No")


# ⚠️ WARN: ⚠️ Indentation is MANDATORY in Python (unlike Java/C). Use 4 spaces. Mixing tabs and
# spaces causes errors.


# ━━━ Flowchart Visualization ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ┌─────────────┐
#                     │   START     │
#                     └─────┬───────┘
#                           ▼
#                 ┌───────────────────┐
#                 │   if condition?   │
#                 └─────┬─────────┬───┘
#                   Yes │         │ No
#                       ▼         ▼
#               ┌──────────┐  ┌──────────┐
#               │  do X    │  │ if elif? │
#               └────┬─────┘  └────┬─────┘
#                    │         Yes │  No
#                    │             ▼
#                    │       ┌──────────┐
#                    │       │   do Y   │
#                    │       └────┬─────┘
#                    │            ▼
#                    │       ┌──────────┐
#                    │       │ else: Z  │
#                    │       └────┬─────┘
#                    ▼            ▼
#                     ┌────────────┐
#                     │    END     │
#                     └────────────┘


# ━━━ Example: Grade Classification ━━━━━━━━━━━━━━━━━━━━━━━

# ── 🔹 Code ──────────────────────────────────────────


def get_grade(score):
    # Function returns the grade based on score
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test it
print(get_grade(95))   # → A
print(get_grade(75))   # → C
print(get_grade(45))   # → F


# ── 🔁 Pattern: Tier Classification ──────────────────
# When to use this pattern: Any problem that maps a number into ranges/categories.
# Where it appears in papers:
#   • Grade A/B/C/D/F (March 2024 Scan)
#   • Salary bonus tiers (May 2025)
#   • Hardness Low/Moderate/High (November 2023)
#   • Life expectancy High/Medium/Low (March 2024 Scan)
#   • Age groups Child/Teen/Adult/Senior (November 2023)
# Reusable template:


def classify(value):
    if value >= threshold_high:    return "High"
    elif value >= threshold_med:  return "Medium"
    else:                          return "Low"

# Use with apply() in pandas:
df['category'] = df['value'].apply(classify)


# ━━━ Compound Conditions ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# Use 'and', 'or', 'not' to combine conditions
age = 25
income = 50000

# AND: both must be true
if age >= 18 and income >= 30000:
    print("Eligible for loan")

# OR: any one must be true
if age < 18 or age > 65:
    print("Cannot apply")

# NOT: reverses
if not (age < 18):
    print("Adult")

# Range check (Python-specific shortcut)
if 18 <= age <= 65:        # same as: age >= 18 and age 
    print("Working age")


# ━━━ Ternary (One-line if) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# Format: value_if_true if condition else value_if_false
age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)             # → Minor

# Useful in apply() and lambda:
df['cat'] = df['age'].apply(lambda x: "adult" if x >= 18 else "minor")


# ── ⚠️ Common Mistakes ──────────────────────────────
#   • Using = (assignment) instead of == (comparison): if x = 5 ❌
#   • Missing colon at end of if line
#   • Wrong indentation under if block
#   • Writing If or IF (Python is case-sensitive — must be lowercase if)

# ────────────────────────────────────────────────────────────
# 🔁 SECTION 2 — FOR LOOPS
# ────────────────────────────────────────────────────────────


# ━━━ What is a for loop? ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A for loop repeats a block of code for each item in a collection . Use it when you know how many
# times to repeat OR when iterating over a sequence.

# ━━━ Basic Syntax ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


for variable in iterable:
    # do something with variable
    print(variable)


# ━━━ range() — The Most Common Iterable ━━━━━━━━━━━━━━━━━━


# range(stop): from 0 to stop-1
for i in range(5):
    print(i)              # prints 0, 1, 2, 3, 4

# range(start, stop): from start to stop-1
for i in range(2, 7):
    print(i)              # prints 2, 3, 4, 5, 6

# range(start, stop, step): with custom step
for i in range(0, 10, 2):
    print(i)              # prints 0, 2, 4, 6, 8

# Reverse: count down
for i in range(10, 0, -1):
    print(i)              # prints 10, 9, 8, ..., 1


# ━━━ Iterating over Different Types ━━━━━━━━━━━━━━━━━━━━━━


# ── List ──
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)

# ── String (each character) ──
for c in "hello":
    print(c)              # h, e, l, l, o

# ── Dictionary (keys by default) ──
prices = {"apple": 100, "banana": 50}
for key in prices:
    print(key, prices[key])

# ── Dictionary (key + value) ──
for key, val in prices.items():
    print(f"{key}: {val}")

# ── enumerate(): get index AND value ──
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")   # 0: apple, 1: banana, 2: cherry

# ── enumerate with start=1 ──
for i, fruit in enumerate(fruits, 1):
    print(f"{i}: {fruit}")   # 1: apple, 2: banana, 3: cherry

# ── zip(): iterate two lists in parallel ──
names = ["Alice", "Bob"]
ages  = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")


# ── 🔁 Pattern: Accumulator ──────────────────────────
# What it does: Build up a result while looping (sum, count, list).
# When to use: Any problem asking total/count/filtered list.


def sum_list(numbers):
    # Pattern: start with 0, add each item
    total = 0
    for num in numbers:
        total = total + num    # or: total += num
    return total

def count_evens(numbers):
    # Pattern: start with 0, increment when condition met
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count = count + 1
    return count

def filter_evens(numbers):
    # Pattern: start with empty list, append matches
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

# Test all three
nums = [1,2,3,4,5,6]
print(sum_list(nums))      # → 21
print(count_evens(nums))   # → 3
print(filter_evens(nums))  # → [2, 4, 6]


# ── 🔁 Pattern: Search (Find First Match) ────────────


def find_first_even(numbers):
    # Pattern: loop, check condition, return early
    for num in numbers:
        if num % 2 == 0:
            return num            # exit as soon as found
    return None                    # nothing found

print(find_first_even([1,3,4,7,8]))   # → 4
print(find_first_even([1,3,5,7]))     # → None


# ────────────────────────────────────────────────────────────
# ⏳ SECTION 3 — WHILE LOOPS
# ────────────────────────────────────────────────────────────


# ━━━ What is a while loop? ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A while loop keeps repeating as long as a condition is true . Use it when you don't know in advance
# how many times to repeat.

# ━━━ Basic Syntax ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


while condition:
    # do something
    # MUST update something inside or it loops forever!
    print("running")


# ━━━ Examples ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# Count from 1 to 5
i = 1
while i <= 5:
    print(i)
    i = i + 1              # MUST increment, else infinite loop!

# Count down from 10
n = 10
while n > 0:
    print(n)
    n -= 1

# Until user types something
text = ""
while text != "quit":
    text = input("Type something (quit to stop): ")
    print("You said:", text)


# ⚠️ WARN: ⚠️ Infinite loop danger! If condition never becomes False, the loop runs forever.
# Always make sure something inside the loop changes the condition.


# ── 🔁 Pattern: STOP-Loop (User-Controlled Repeat) ───
# Used in: Bookstore Billing (Feb 2025), Superstore Pricing (March 2024 Scan), Grocery Bill problems


def collect_items():
    # Pattern: while True + break on STOP
    items = []
    while True:
        entry = input("Enter item (or STOP to finish): ").strip().upper()
        if entry == "STOP":
            break            # exit loop
        items.append(entry)
    return items

print(collect_items())


# ━━━ while vs for — When to Use Which? ━━━━━━━━━━━━━━━━━━━

# [Use for]  [Use while]
# You know the count or have a sequence |  You don't know when to stop |
# Iterating over list, dict, string |  Until condition met (user input, sentinel) |
# Fixed number of repetitions |  Variable repetitions |
# for i in range(10): |  while user_input != "quit": |


# ────────────────────────────────────────────────────────────
# 🛑 SECTION 4 — BREAK & CONTINUE
# ────────────────────────────────────────────────────────────


# ━━━ break — Exit the Loop Immediately ━━━━━━━━━━━━━━━━━━━


# Find a target value, stop as soon as found
numbers = [10, 20, 30, 40, 50]
target = 30

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break                  # exit loop, stop checking rest
    print(f"Checked {num}")

# Output:
# Checked 10
# Checked 20
# Found 30!


# ━━━ continue — Skip This Iteration ━━━━━━━━━━━━━━━━━━━━━━


# Print only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue               # skip even, go to next iteration
    print(i)                  # prints only 1, 3, 5, 7, 9


# []  [break]  [continue]
# Effect |  Exits loop entirely |  Skips current iteration |
# Use case |  Found what you want, stop searching |  Don't process this item, but keep looping |
# Memory aid |  "Break out" |  "Continue to next" |


# ────────────────────────────────────────────────────────────
# 🪆 SECTION 5 — NESTED LOOPS
# ────────────────────────────────────────────────────────────

# A loop inside another loop. Outer loop runs once → inner loop runs completely → outer moves to next.


# Multiplication table 1-3 × 1-3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}", end="  ")
    print()                # newline after each row

# Output:
# 1 × 1 = 1   1 × 2 = 2   1 × 3 = 3
# 2 × 1 = 2   2 × 2 = 4   2 × 3 = 6
# 3 × 1 = 3   3 × 2 = 6   3 × 3 = 9

# Iterate over a list of lists
matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()


# ⚠️ WARN: 💡 Performance tip: Nested loops have O(n²) complexity. For 1000×1000, that's 1,000,000
# operations.
# Avoid 3+ levels of nesting if possible.


# ────────────────────────────────────────────────────────────
# 🧩 SECTION 6 — KEY PATTERNS FROM EXAM PAPERS
# ────────────────────────────────────────────────────────────


# ━━━ Pattern 1: Validation Loop (Re-prompt on Bad Input) ━


def get_valid_choice(options):
    # Pattern: while True + validate + break when good
    while True:
        choice = input(f"Choose ({options}): ").strip()
        if choice in options:
            return choice
        print("Invalid! Try again.")

# Reuse for any "ask user choice" question
size = get_valid_choice(["S", "M", "L"])


# ━━━ Pattern 2: Counting in Range Tiers ━━━━━━━━━━━━━━━━━━


def categorize_into_grades(scores):
    # Pattern: 5 buckets, append based on tier
    A, B, C, D, F = [], [], [], [], []
    for score in scores:
        if score >= 90:   A.append(score)
        elif score >= 80: B.append(score)
        elif score >= 70: C.append(score)
        elif score >= 60: D.append(score)
        else:             F.append(score)
    return [A, B, C, D, F]

# Used in: March 2024 Scan, Q3b


# ━━━ Pattern 3: Loop with Index using enumerate ━━━━━━━━━━


def print_with_position(items):
    # Pattern: enumerate when both index and value needed
    for position, item in enumerate(items, 1):
        print(f"  {position}. {item}")

print_with_position(["apple", "banana", "cherry"])
# Output:
#   1. apple
#   2. banana
#   3. cherry


# ━━━ Pattern 4: Cycle Detection (Set + while) ━━━━━━━━━━━━


def is_happy_number(n):
    # Pattern: track seen values to detect cycles
    seen = set()
    while n != 1:
        if n in seen:
            return False           # cycle = not happy
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return True

# Used in: March 2024 Scan, Q3a


# ────────────────────────────────────────────────────────────
# 🧠 SECTION 7 — MEMORY AIDS
# ────────────────────────────────────────────────────────────


# ━━━ 🔀 if-elif-else ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • Always end the line with colon (:)
#   • Indent the body (4 spaces)
#   • Order matters: put most specific conditions first
#   • Use elif, not else if (it's Python!)

# ━━━ 🔁 for vs while ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • for: known count, iterate over collection
#   • while: unknown count, condition-driven
#   • break: exit immediately
#   • continue: skip to next iteration

# ━━━ 📋 range() Quick Ref ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • range(5) → 0,1,2,3,4
#   • range(2,7) → 2,3,4,5,6
#   • range(0,10,2) → 0,2,4,6,8
#   • range(10,0,-1) → 10,9,...,1
#   • Stop value is ALWAYS excluded

# ━━━ ⚡ 4 Universal Loop Patterns ━━━━━━━━━━━━━━━━━━━━━━━━━
#   • Accumulator: total = 0; total += x
#   • Counter: count = 0; count += 1
#   • Filter: result = []; result.append(x)
#   • Search: if x: return x; else None

# ────────────────────────────────────────────────────────────
# 🏋️ SECTION 8 — PRACTICE PROBLEMS
# ────────────────────────────────────────────────────────────

#   • Sum 1 to N: Take N from user, print sum of 1+2+...+N
#   • Factorial: Take N, compute N! using a loop
#   • Reverse a number: Take 12345, output 54321 using % and //
#   • FizzBuzz: Print 1-30. Multiples of 3 → "Fizz", multiples of 5 → "Buzz", both → "FizzBuzz"
#   • Find max: Given a list, find the maximum (without using max())
#   • Pattern printing: Print a triangle of stars of height N
#   • Prime check: Is N prime? Loop from 2 to sqrt(N)
# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ╔════════════════════════════════════════════════════════════╗
# ║  FILE 04 — Functions                                       ║
# ╚════════════════════════════════════════════════════════════╝


# ────────────────────────────────────────────────────────────
# 📦 SECTION 1 — WHAT IS A FUNCTION?
# ────────────────────────────────────────────────────────────


# ━━━ Simple Definition ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A function is a reusable block of code that takes inputs (parameters), does something, and
# (optionally) returns an output.

# INPUT       FUNCTION         OUTPUT
#    ─────       ────────         ──────
#    x = 5  →  ┌──────────┐  →  result = 25
#             │ square() │
#             └──────────┘
#               code: x * x


# ━━━ Why use functions? ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • Reusability: Write once, use many times
#   • Readability: calculate_tax(income) reads like English
#   • Testing: Easy to verify each piece works
#   • Abstraction: Hide complexity behind a simple name

# ✅ NOTE: ✅ Exam rule: Wrap EVERY solution in a function. Graders give bonus marks for clean function
# design.


# ────────────────────────────────────────────────────────────
# ✏️ SECTION 2 — DEFINING FUNCTIONS (def)
# ────────────────────────────────────────────────────────────


# ━━━ Basic Syntax ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def function_name(parameter1, parameter2):
    # body — what the function does
    return result   # optional


# [Part]  [What it does]
# def |  Keyword that starts a function definition |
# function_name |  The name you'll use to call it (use snake_case) |
# parameters |  Variables that receive the input values |
# : |  Required colon at end of def line |
# indented body |  The actual code (4 spaces) |
# return |  Sends a value back. If omitted, function returns None |


# ━━━ Calling a Function ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def add(a, b):
    return a + b

result = add(3, 5)        # call function with inputs 3, 5
print(result)               # → 8


# ━━━ Multiple Returns / Multiple Values ━━━━━━━━━━━━━━━━━━


def min_max(numbers):
    # A function can return multiple values as a tuple
    return min(numbers), max(numbers)

low, high = min_max([3,1,4,5,9,2])
print(low, high)            # → 1 9


# ── ⚠️ Common Mistakes ──────────────────────────────
#   • Forgetting the colon at end of def line
#   • Forgetting to indent the body
#   • Using print() instead of return — print shows on screen, return gives value back
#   • Calling function_name without parentheses — that gets the function itself, not its result!

# ────────────────────────────────────────────────────────────
# ⚙️ SECTION 3 — PARAMETERS AND ARGUMENTS
# ────────────────────────────────────────────────────────────

# Parameter = the variable in the def line. Argument = the actual value passed when calling.

# ━━━ 1. Positional Arguments ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

# Order matters!
describe("Alice", 25, "Bengaluru")
# → Alice, 25, from Bengaluru

# Wrong order = wrong meaning
describe(25, "Alice", "Bengaluru")   # confusing!


# ━━━ 2. Keyword Arguments ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# # Use parameter names — order doesn't matter
# describe(age=25, city="Bengaluru", name="Alice")
# # → Alice, 25, from Bengaluru
#
# # Mix positional + keyword (positional must come first)
# describe("Alice", age=25, city="Bengaluru")   # ✅ OK
# # describe(name="Alice", 25, "Bengaluru") ← ❌ SyntaxError


# ━━━ 3. Default Parameters ⭐ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ── 🔹 Exam Question ─────────────────────────────────
# "What is the default parameter in user-defined function?" — Model Set


# Parameters can have default values
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")              # uses default → "Hello, Alice!"
greet("Bob", "Hi")          # overrides → "Hi, Bob!"

# Multiple defaults
def power(base, exponent=2):
    return base ** exponent

print(power(5))             # → 25 (5²)
print(power(5, 3))          # → 125 (5³)


# ⚠️ WARN: ⚠️ RULE: Default parameters MUST come AFTER non-default parameters.
# def fn(a=1, b): ❌ SyntaxError
# def fn(a, b=1): ✅ Correct


# ── 🧠 Memory Aid ────────────────────────────────────
# "Defaults go last, optionals come after required" — required first, optional with defaults at end.

# ────────────────────────────────────────────────────────────
# ⭐ SECTION 4 — *args and **kwargs (CRITICAL TOPIC)
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (asked in 3 papers!) ────────────
# "What are *args and **kwargs in Python functions?" — March 2024, November 2023, May 2025

# ━━━ *args — Variable Positional Arguments ━━━━━━━━━━━━━━━
# Use when you don't know how many positional arguments will be passed. Python collects them as a
# tuple .


def total(*args):
    # args is a tuple of all positional arguments
    print("args type:", type(args))
    print("args:", args)
    return sum(args)

print(total(1, 2, 3))           # args = (1,2,3) → 6
print(total(10, 20, 30, 40))    # args = (10,20,30,40) → 100
print(total())                  # args = () → 0


# ━━━ **kwargs — Variable Keyword Arguments ━━━━━━━━━━━━━━━
# Use when you don't know how many keyword (name=value) arguments will be passed. Python collects
# them as a dictionary .


def describe_person(**kwargs):
    # kwargs is a dict {name: value}
    print("kwargs type:", type(kwargs))
    print("kwargs:", kwargs)
    for key, val in kwargs.items():
        print(f"  {key}: {val}")

describe_person(name="Alice", age=25, city="Bengaluru")
# kwargs = {'name':'Alice', 'age':25, 'city':'Bengaluru'}


# ━━━ Combining All — The Right Order ━━━━━━━━━━━━━━━━━━━━━


# Order: positional, *args, default, **kwargs
def complete_function(required, *args, default=10, **kwargs):
    print(f"required = {required}")
    print(f"args     = {args}")
    print(f"default  = {default}")
    print(f"kwargs   = {kwargs}")

complete_function("hi", 1, 2, 3, default=99, x=10, y=20)
# required = hi
# args     = (1, 2, 3)
# default  = 99
# kwargs   = {'x': 10, 'y': 20}


# ── 🧠 Memory Aid ────────────────────────────────────
# 🧠 *args = "Accept any Positional → tuple"
# 🧠 **kwargs = "Accept any Key=Value → dict"
# Names `args` and `kwargs` are conventions — the `*` and `**` are what actually matter.

# ━━━ Practical Use: Print Statistics ━━━━━━━━━━━━━━━━━━━━━


def stats(*numbers):
    # Accept any number of numbers, compute statistics
    if not numbers:
        return None
    return {
        'count': len(numbers),
        'sum':   sum(numbers),
        'min':   min(numbers),
        'max':   max(numbers),
        'avg':   sum(numbers) / len(numbers)
    }

print(stats(10, 20, 30, 40, 50))
# {'count': 5, 'sum': 150, 'min': 10, 'max': 50, 'avg': 30.0}


# ────────────────────────────────────────────────────────────
# ⚡ SECTION 5 — LAMBDA (ANONYMOUS FUNCTIONS)
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (asked in many papers!) ─────────
# "What are anonymous functions in Python?" — July 2021, May 2025, March 2024

# ━━━ What is a Lambda? ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A lambda is a tiny, one-line, anonymous (no-name) function. Used for short throwaway operations.

# ━━━ Syntax ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


lambda arguments: expression

# Compared to regular function:

# [Regular function]  [Lambda equivalent]


def square(x):
    return x ** 2


square = lambda x: x ** 2


# ━━━ Common Uses ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 1. Quick math operations
square = lambda x: x ** 2
print(square(5))                   # → 25

add = lambda a, b: a + b
print(add(3, 7))                    # → 10

# 2. With map() — apply to every element
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)                     # → [1, 4, 9, 16, 25]

# 3. With filter() — keep only matching
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)                       # → [2, 4]

# 4. With sorted() — custom sort key
words = ["banana", "apple", "fig"]
by_len = sorted(words, key=lambda x: len(x))
print(by_len)                      # → ['fig', 'apple', 'banana']

# 5. With reduce() — combine all into one
from functools import reduce
total = reduce(lambda a, b: a + b, nums)
print(total)                       # → 15

# 6. With pandas apply()
# df['cat'] = df['age'].apply(lambda x: 'adult' if x >= 18 else 'minor')


# ── 🔹 Exam Question ─────────────────────────────────
# "Create a lambda function to print sum of all elements in [5, 8, 10, 20, 50, 100]" — March 2024
# (Q1c)


# Solution 1: lambda that takes a list
sum_lambda = lambda lst: sum(lst)
print(sum_lambda([5, 8, 10, 20, 50, 100]))   # → 193

# Solution 2: immediate invocation (IIFE)
result = (lambda lst: sum(lst))([5, 8, 10, 20, 50, 100])
print(result)                       # → 193


# ── 🧠 Memory Aid ────────────────────────────────────
# 🧠 L-I-E: Lambda · Inputs · Expression
# `lambda x: expression` — no `def`, no `return`, no name.
# Can ONLY have one expression (no statements like `if/else`... well, you can use ternary).

# ⚠️ WARN: 💡 When NOT to use lambda: If your function is more than one line, or you'll reuse it many
# times,
# use a normal def function instead. Lambdas are for throwaway use.


# ────────────────────────────────────────────────────────────
# 🌐 SECTION 6 — GLOBAL KEYWORD
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question ─────────────────────────────────
# "What is the Global Keyword in Python?" — March 2024 Scan (Q1b)

# ━━━ The LEGB Rule (Variable Scope) ━━━━━━━━━━━━━━━━━━━━━━
# When Python looks for a variable, it searches in this order:
#   • Local — inside current function
#   • Enclosing — inside outer functions (nested)
#   • Global — at module/file level
#   • Built-in — Python built-ins (print, len, etc.)

# ━━━ The Problem ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


count = 0             # GLOBAL variable

def increment_wrong():
    count = count + 1   # ❌ UnboundLocalError
    # Python sees assignment → thinks count is LOCAL
    # But local count not defined yet → error


# ━━━ The Solution: global Keyword ━━━━━━━━━━━━━━━━━━━━━━━━


count = 0

def increment():
    global count           # tell Python: use the global one
    count = count + 1      # now modifies global

increment()
increment()
print(count)               # → 2 ✅


# ⚠️ WARN: ⚠️ When do you need global? Only when you want to assign to a global variable inside a
# function.
# You can read globals freely without it.


# Reading global — NO need for global keyword
PI = 3.14159

def circle_area(r):
    return PI * r ** 2     # reading PI works fine

print(circle_area(5))         # → 78.54

# Writing global — NEED global keyword
counter = 0

def increment_counter():
    global counter
    counter += 1


# ── 🧠 Memory Aid ────────────────────────────────────
# 🧠 "Read freely, write needs global"
# LEGB : Local → Enclosing → Global → Built-in (search order)

# ────────────────────────────────────────────────────────────
# 🔁 SECTION 7 — RECURSION
# ────────────────────────────────────────────────────────────


# ━━━ What is Recursion? ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A function that calls itself . Useful for problems that can be broken into smaller versions of the
# same problem.

# ━━━ Recipe for Every Recursive Function ━━━━━━━━━━━━━━━━━
#   • Base case: When does it stop? (must have or infinite recursion!)
#   • Recursive case: Call self with smaller input

# ━━━ Classic Example: Factorial ━━━━━━━━━━━━━━━━━━━━━━━━━━


def factorial(n):
    # BASE CASE: stop the recursion
    if n <= 1:
        return 1
    # RECURSIVE CASE: smaller version of same problem
    return n * factorial(n - 1)

print(factorial(5))     # → 120
# How it works:
# factorial(5) = 5 × factorial(4)
# factorial(4) = 4 × factorial(3)
# factorial(3) = 3 × factorial(2)
# factorial(2) = 2 × factorial(1)
# factorial(1) = 1            ← base case
# Then unwinds: 1 → 2 → 6 → 24 → 120


# ━━━ Fibonacci (Recursive) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])
# → [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# ⚠️ WARN: ⚠️ Recursion limit: Python limits recursion depth (default 1000). For deep problems, use
# iteration (loops) instead.


# ────────────────────────────────────────────────────────────
# 📐 SECTION 8 — DOCSTRINGS & TYPE HINTS
# ────────────────────────────────────────────────────────────

# Make functions self-documenting:


def calculate_bmi(weight: float, height: float) -> float:
    "Compute BMI given weight (kg) and height (m)."
    # Type hints: weight and height are float, returns float
    # The string after def is a DOCSTRING - shows in help()
    return weight / (height ** 2)

print(calculate_bmi(70, 1.75))     # → 22.86
help(calculate_bmi)                # shows the docstring


# ✅ NOTE: ✅ Exam tip: Add a one-line docstring under every function. Graders love clean documentation.


# ────────────────────────────────────────────────────────────
# 🎯 SECTION 9 — REUSABLE FUNCTION TEMPLATES
# ────────────────────────────────────────────────────────────

# These templates appear repeatedly in exam papers. Memorize the structure.

# ━━━ Template 1: Validation Function ━━━━━━━━━━━━━━━━━━━━━


def is_valid_X(value):
    # Check rules one by one, return False on first failure
    if not rule1: return False
    if not rule2: return False
    if not rule3: return False
    return True

# Used in: Username, Password, Date validation


# ━━━ Template 2: Filter + Transform ━━━━━━━━━━━━━━━━━━━━━━


def process_list(items, condition_fn, transform_fn):
    # Generic: filter items, then transform each
    result = []
    for item in items:
        if condition_fn(item):
            result.append(transform_fn(item))
    return result

# Usage: squares of evens
nums = [1,2,3,4,5]
print(process_list(nums, lambda x: x%2==0, lambda x: x**2))
# → [4, 16]


# ━━━ Template 3: Aggregator (Sum/Count/Max) ━━━━━━━━━━━━━━


def aggregate(items, condition_fn):
    # Generic: count or sum items meeting condition
    matches = []
    for item in items:
        if condition_fn(item):
            matches.append(item)
    return {
        'count': len(matches),
        'sum':   sum(matches) if matches else 0,
        'list':  matches
    }


# ━━━ Template 4: Two-Stage Calculator (Math/Bill) ━━━━━━━━


def calculate_bill(items_dict, tax_rate=0.12):
    # Stage 1: subtotal
    subtotal = sum(items_dict.values())
    # Stage 2: tax + total
    tax = subtotal * tax_rate
    total = subtotal + tax
    return {'subtotal': subtotal, 'tax': tax, 'total': total}

# Used in: Computer Bill, Stock Profit, Bookstore Billing


# ────────────────────────────────────────────────────────────
# 🧠 SECTION 10 — MEMORY AIDS & CHEATSHEET
# ────────────────────────────────────────────────────────────


# ━━━ 📝 Function Anatomy ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def name(p1, p2=10, *args, **kwargs):
    "docstring"
    # body
    return result


# ━━━ ⚡ Lambda Quick Patterns ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


lambda x: x*2
lambda x: x % 2 == 0
lambda x: x[0]    # for sort key
lambda a,b: a+b
lambda x: 'A' if x>=90 else 'B'


# ━━━ 🌟 *args / **kwargs Rules ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • *args → tuple
#   • **kwargs → dict
#   • Order: positional, *args, defaults, **kwargs
#   • You can rename them (just need * and **)

# ━━━ 🌐 Global Rules ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • Read global → no keyword needed
#   • Write global → use global
#   • LEGB scope: Local → Enclosing → Global → Built-in

# ────────────────────────────────────────────────────────────
# 🏋️ SECTION 11 — PRACTICE PROBLEMS
# ────────────────────────────────────────────────────────────

#   • Write is_prime(n) that returns True if n is prime, False otherwise
#   • Write count_vowels(s) that counts vowels in a string
#   • Write reverse_string(s) using slicing
#   • Write a lambda that returns the square of a number
#   • Use *args to write multiply_all(*nums) that multiplies any number of args
#   • Use **kwargs to write format_card(**fields) that prints key-value pairs
#   • Write recursive sum_digits(n) — sum the digits of a number
#   • Write is_palindrome(s) using slicing
# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ╔════════════════════════════════════════════════════════════╗
# ║  FILE 05 — Strings                                         ║
# ╚════════════════════════════════════════════════════════════╝


# ────────────────────────────────────────────────────────────
# 📝 SECTION 1 — STRING BASICS
# ────────────────────────────────────────────────────────────


# ━━━ What is a String? ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A string is a sequence of characters . In Python, strings are immutable — once created, they cannot
# be changed.


# Three ways to create a string
s1 = "Hello"            # double quotes
s2 = 'World'            # single quotes (same thing)
s3 = "Multi-line via \\n newline"   # or use triple quotes

# Length
print(len(s1))         # → 5

# Concatenation with +
print(s1 + " " + s2)   # → "Hello World"

# Repetition with *
print(s1 * 3)          # → "HelloHelloHello"

# Membership with in
print("ell" in s1)     # → True


# ── ⚠️ Strings are Immutable ────────────────────────

#
# s = "hello"
# # s[0] = "H"   ← ❌ TypeError!
#
# # To "modify", create a new string:
# s = "H" + s[1:]      # → "Hello"
# # s now points to a NEW string in memory


# ────────────────────────────────────────────────────────────
# ✂️ SECTION 2 — STRING SLICING (CRITICAL)
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (5 papers!) ─────────────────────
# "What is string slicing? Slice 'PythonProgramming' to get 'thonPro'." — May 2025, August 2021,
# March 2024

# ━━━ Slicing Syntax ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# string[start : stop : step]
#
# # start = where to begin (inclusive, default 0)
# # stop  = where to end (EXCLUSIVE, default len)
# # step  = how many to skip (default 1)


# ━━━ Index Visualization ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# String:    P  y  t  h  o  n  P  r  o  g  r  a  m  m  i  n  g
# Index:     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
# Negative: -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1


# ━━━ Solving the Exam Question ━━━━━━━━━━━━━━━━━━━━━━━━━━━


s = "PythonProgramming"

# Goal: extract "thonPro"
# 't' is at index 2, last needed char 'o' is at index 8
# Slice should be [2 : 9] (stop is exclusive, so 9 to include 8)

result = s[2:9]
print(result)   # → "thonPro" ✅


# ━━━ All Slicing Patterns ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# s = "Hello World"
# # indices: 0=H, 1=e, 2=l, 3=l, 4=o, 5= , 6=W, 7=o, 8=r, 9=l, 10=d
#
# s[0]              # → 'H'  (single character)
# s[-1]             # → 'd'  (last character)
# s[0:5]            # → 'Hello' (chars 0,1,2,3,4)
# s[:5]             # → 'Hello' (start defaults to 0)
# s[6:]             # → 'World' (end defaults to len)
# s[:]              # → 'Hello World' (full copy)
# s[-5:]            # → 'World' (last 5 chars)
# s[:-6]            # → 'Hello' (all except last 6)
# s[::2]            # → 'HloWrd' (every 2nd char)
# s[::-1]           # → 'dlroW olleH' (REVERSED!)
# s[1:8:2]          # → 'el o' (every 2nd from 1 to 8)


# ── 🧠 Memory Aid ────────────────────────────────────
# 🧠 "Start In, End Out" — start is inclusive, stop is exclusive
# 🧠 s[::-1] = REVERSE TRICK — works on lists too
# 🧠 s[:n] = first n chars · s[-n:] = last n chars

# ────────────────────────────────────────────────────────────
# 🔍 SECTION 3 — find() vs index() (CRITICAL)
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question ─────────────────────────────────
# "What is the difference between index() and find() method with respect to string?" — July 2021

# [Behavior]  [find()]  [index()]
# If found |  Returns starting index |  Returns starting index |
# If NOT found |  Returns -1 |  Raises ValueError |
# Safe? |  ✅ Yes — won't crash |  ⚠️ No — must use try/except |


s = "Hello Python World"

# ── find() — safe ──
print(s.find("Python"))      # → 6  (found)
print(s.find("Java"))        # → -1 (NOT found, no crash)

# ── index() — risky ──
print(s.index("Python"))     # → 6  (found)
# s.index("Java")  ← ❌ ValueError!

# Safe pattern with index()
if "Java" in s:
    print(s.index("Java"))
else:
    print("Not found")


# ── 🧠 Memory Aid ────────────────────────────────────
# 🧠 find = "Find or return -1" · index = "Index or explode!"

# ────────────────────────────────────────────────────────────
# 🛠 SECTION 4 — STRING METHODS (TOP 30)
# ────────────────────────────────────────────────────────────


# ━━━ Case Manipulation ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# s = "Hello World"
# s.upper()           # → "HELLO WORLD"
# s.lower()           # → "hello world"
# s.title()           # → "Hello World"
# s.capitalize()      # → "Hello world"
# s.swapcase()        # → "hELLO wORLD"


# ━━━ Whitespace Trimming ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# s = "   Hello   "
# s.strip()           # → "Hello"  (both ends)
# s.lstrip()          # → "Hello   "  (left only)
# s.rstrip()          # → "   Hello"  (right only)
# s.strip("#@")       # strips specific chars


# ━━━ Search & Replace ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# s = "Hello World"
# s.find("World")             # → 6 (or -1)
# s.index("World")            # → 6 (or ValueError)
# s.count("l")                # → 3
# s.replace("World","Python") # → "Hello Python"
# s.startswith("Hello")       # → True
# s.endswith("World")         # → True


# ━━━ Type-Check Methods ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# All return True/False
"abc".isalpha()      # True (only letters)
"123".isdigit()      # True (only digits)
"abc123".isalnum()   # True (letters + digits, no spaces)
"hello".islower()    # True
"HELLO".isupper()    # True
"Hello".istitle()    # True (first letter caps)
"   ".isspace()      # True (only whitespace)


# ━━━ Split & Join ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# s = "apple,banana,cherry"
# parts = s.split(",")              # → ['apple', 'banana', 'cherry']
#
# s2 = "hello world python"
# words = s2.split()                  # → ['hello', 'world', 'python']
#
# # Join (reverse of split)
# joined = "-".join(["a","b","c"])    # → "a-b-c"


# ━━━ Padding & Alignment ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# "5".zfill(3)           # → "005" (zero-pad)
# "abc".center(7,"*")   # → "**abc**"
# "abc".ljust(7,".")    # → "abc...."
# "abc".rjust(7,".")    # → "....abc"


# ────────────────────────────────────────────────────────────
# 🎯 SECTION 5 — STRING VALIDATION PATTERNS
# ────────────────────────────────────────────────────────────


# ━━━ Pattern: Username Validation (Mar2024 + Nov2023) ━━━━


def UsernameValidation(s):
    # Rule 1: length 4-25
    if len(s) < 4 or len(s) > 25:
        return 'false'
    # Rule 2: starts with letter
    if not s[0].isalpha():
        return 'false'
    # Rule 3: only letters, digits, underscore
    for c in s:
        if not (c.isalnum() or c == '_'):
            return 'false'
    # Rule 4: cannot end with underscore
    if s[-1] == '_':
        return 'false'
    return 'true'

# Tests
print(UsernameValidation("alice_123"))  # true
print(UsernameValidation("alice_"))     # false
print(UsernameValidation("1alice"))     # false
print(UsernameValidation("ab"))         # false


# ━━━ Pattern: Password Strength (Nov 2023) ━━━━━━━━━━━━━━━


def password_strength(pwd):
    score = 0
    if len(pwd) >= 8:                            score += 2
    if any(c.isupper() for c in pwd):           score += 1
    if any(c.islower() for c in pwd):           score += 1
    if any(c.isdigit() for c in pwd):           score += 2
    if any(c in "!@#$%^&*" for c in pwd):       score += 2
    return score

print(password_strength("abc"))         # → 1 (only lower)
print(password_strength("Pass@123"))    # → 8 (all 5)


# ━━━ Pattern: Extract Alphanumeric (Mar 2024 PDF) ━━━━━━━━


def find_special_codes(message):
    # Return tokens that are pure alphanumeric (no special chars)
    tokens = message.split()
    result = []
    for token in tokens:
        if token.isalnum():
            result.append(token)
    return result

print(find_special_codes("abc 123 ab@c hello! ok99"))
# → ['abc', '123', 'ok99']


# ━━━ Pattern: Number Plate Extraction (Model Set) ━━━━━━━━


def classify_plates(plates):
    # Split each plate, take last numeric part, classify even/odd
    result = {'Even': [], 'Odd': []}
    for plate in plates:
        parts = plate.split()
        # Find the last part that is a number
        for part in reversed(parts):
            if part.isdigit():
                num = int(part)
                if num % 2 == 0:
                    result['Even'].append(plate)
                else:
                    result['Odd'].append(plate)
                break
    return result

plates = ["KA 02 4592", "DL 09 8765", "MH 14 1234"]
print(classify_plates(plates))


# ━━━ Pattern: Telephone Keypad Match (Nov 2023) ━━━━━━━━━━


def telephone_match(num, s):
    keypad = {'2':'ABC', '3':'DEF', '4':'GHI',
              '5':'JKL', '6':'MNO', '7':'PQRS',
              '8':'TUV', '9':'WXYZ'}
    if len(num) != len(s):
        return False
    for digit, letter in zip(num, s.upper()):
        if digit not in keypad:
            return False
        if letter not in keypad[digit]:
            return False
    return True

print(telephone_match("22426", "CABIN"))   # True


# ────────────────────────────────────────────────────────────
# 📊 SECTION 6 — STRING FORMATTING
# ────────────────────────────────────────────────────────────


# ━━━ f-strings (Best, Modern Way) ━━━━━━━━━━━━━━━━━━━━━━━━


name = "Alice"; age = 25; gpa = 3.847

print(f"{name} is {age} years old")
print(f"GPA: {gpa:.2f}")             # → "GPA: 3.85" (2 decimals)
print(f"{age:>5}")                  # → "   25" (right-align in 5 cols)
print(f"{age:<5}")                  # → "25   " (left-align)
print(f"{age:^5}")                  # → " 25  " (center)
print(f"{1234567:,}")               # → "1,234,567" (commas)
print(f"{0.85:.1%}")                # → "85.0%" (percentage)

# Expressions inside
print(f"Next year: {age + 1}")
print(f"Upper: {name.upper()}")


# ────────────────────────────────────────────────────────────
# 🧠 SECTION 7 — MEMORY AIDS
# ────────────────────────────────────────────────────────────


# ━━━ ✂️ Slicing Patterns ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# s[:n]      # first n chars
# s[-n:]     # last n chars
# s[::-1]    # reverse
# s[::2]     # every 2nd char
# s[a:b:c]   # start:stop:step


# ━━━ 🔍 Search Methods ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# s.find(x)   # index or -1
# s.index(x)  # index or ERROR
# s.count(x)  # # occurrences
# x in s      # True/False


# ━━━ 🔤 Type Checks ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • isalpha() — only letters
#   • isdigit() — only digits
#   • isalnum() — letters + digits, no spaces
#   • isspace() — only whitespace

# ━━━ ⚡ Universal Validation Pattern ━━━━━━━━━━━━━━━━━━━━━━
#   • Check length first
#   • Check first char
#   • Check each char in loop
#   • Check last char
#   • Return False on first failure

# ────────────────────────────────────────────────────────────
# 🏋️ SECTION 8 — PRACTICE PROBLEMS
# ────────────────────────────────────────────────────────────

#   • Slice "DataScience" to get "taSc"
#   • Reverse "hello world" using only slicing
#   • Count vowels in any string (use a function)
#   • Check if a string is palindrome using slicing
#   • Validate an email: must contain '@' and end with '.com'
#   • Extract all digits from "abc123def456" as a list
#   • Capitalize first letter of every word (without using .title())
# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ╔════════════════════════════════════════════════════════════╗
# ║  FILE 06 — Lists & Tuples                                  ║
# ╚════════════════════════════════════════════════════════════╝


# ────────────────────────────────────────────────────────────
# 📦 SECTION 1 — LIST vs TUPLE
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (3 papers!) ─────────────────────
# "What is the difference between List and Tuple?" — July 2021, March 2024, March 2024 Scan

# [Feature]  [List [ ]]  [Tuple ( )]
# Mutable? |  ✅ Yes — can change |  ❌ No — fixed |
# Speed |  Slower |  Faster |
# Memory |  More |  Less |
# As dict key? |  ❌ Not allowed (unhashable) |  ✅ Yes (hashable) |
# Methods |  Many: append, remove, pop, sort... |  Only count(), index() |
# Use when |  Data will change |  Data is fixed (coordinates, dates) |


# LIST — mutable
lst = [1, 2, 3]
lst[0] = 99            # ✅ allowed
lst.append(4)         # ✅ adds element
print(lst)             # → [99, 2, 3, 4]

# TUPLE — immutable
tup = (1, 2, 3)
# tup[0] = 99    ← ❌ TypeError
print(tup[0])         # ✅ reading is fine

# Tuple as dict key — works
locations = {(10, 20): "Office", (30, 40): "Home"}

# List as dict key — fails
# bad = {[1,2]: "x"}  ← ❌ TypeError


# ── 🧠 Memory Aid ────────────────────────────────────
# 🧠 List = Liquid (flexible) · Tuple = Stone (fixed)

# ────────────────────────────────────────────────────────────
# 📋 SECTION 2 — LIST CREATION & ACCESS
# ────────────────────────────────────────────────────────────


#
# # Creating lists
# empty = []                     # empty list
# nums = [1, 2, 3, 4, 5]
# mixed = [1, "hello", 3.14, True]   # can mix types
# nested = [[1,2], [3,4], [5,6]]   # list of lists
# zeros = [0] * 5                 # → [0, 0, 0, 0, 0]
# range_list = list(range(5))         # → [0, 1, 2, 3, 4]
#
# # Access by index (0-based)
# nums[0]                   # → 1 (first)
# nums[-1]                  # → 5 (last)
# nums[1:4]                 # → [2, 3, 4] (slice)
# nums[::-1]                # → [5, 4, 3, 2, 1] (reverse)
#
# # Length
# len(nums)                # → 5
#
# # Membership
# 3 in nums               # → True
# 99 not in nums         # → True


# ────────────────────────────────────────────────────────────
# 🛠 SECTION 3 — LIST METHODS (CRITICAL)
# ────────────────────────────────────────────────────────────


# ━━━ Adding Elements ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# lst = [1, 2, 3]
#
# lst.append(4)            # add to end → [1, 2, 3, 4]
# lst.insert(0, 0)         # insert at index → [0, 1, 2, 3, 4]
# lst.extend([5, 6])       # add multiple → [0, 1, 2, 3, 4, 5, 6]
# lst += [7, 8]             # same as extend → [0..8]


# ━━━ Removing Elements (4 ways!) ━━━━━━━━━━━━━━━━━━━━━━━━━

# ── 🔹 Exam Question (Nov 2023) ──────────────────────
# "What is the difference between del(), clear(), remove(), and pop()?"

# [Method]  [Removes by]  [Returns]  [Example]
# del lst[i] |  Index |  Nothing |  del lst[2] |
# lst.clear() |  ALL |  Nothing |  lst.clear() → [] |
# lst.remove(v) |  First match of value |  None |  lst.remove(20) |
# lst.pop(i) |  Index (default last) |  The removed item |  x = lst.pop() |


#
# lst = [10, 20, 30, 20, 40]
#
# # del — by index
# del lst[1]              # removes 20 → [10, 30, 20, 40]
#
# # pop — by index, RETURNS the value
# last = lst.pop()           # last=40, lst=[10, 30, 20]
# first = lst.pop(0)         # first=10, lst=[30, 20]
#
# # remove — by VALUE (first occurrence)
# lst = [10, 20, 30, 20]
# lst.remove(20)            # lst=[10, 30, 20] (only first 20 removed)
#
# # clear — empty entire list
# lst.clear()                # lst=[]


# ━━━ Counting & Searching ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ── 🔹 Exam Question (Mar 2024 Scan) ─────────────────
# 'How do you count the occurrences of a particular element in the list? a_list = ["a", "b", "a"]'


lst = ["a", "b", "a", "c", "a"]

lst.count("a")            # → 3 (occurrences)
lst.count("x")            # → 0 (not found, no error!)

lst.index("b")            # → 1 (first index)
# lst.index("x") ← ❌ ValueError

# Counter for all at once
from collections import Counter
print(Counter(lst))       # → Counter({'a':3, 'b':1, 'c':1})


# ━━━ Reversing & Copying ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# lst = [1, 2, 3]
#
# lst.reverse()              # in-place → [3, 2, 1]
# lst[::-1]                 # new reversed list (no in-place)
#
# copy1 = lst.copy()         # shallow copy
# copy2 = lst[:]             # slicing trick
# copy3 = list(lst)         # constructor


# ────────────────────────────────────────────────────────────
# ⚖️ SECTION 4 — sort() vs sorted()
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (2 papers!) ─────────────────────
# "How sorted() and sort() can be used with list in Python?" — May 2025, March 2024

# [Feature]  [sort()]  [sorted()]
# Type |  Method (lst.sort()) |  Built-in function (sorted(lst)) |
# Modifies original? |  ✅ Yes (in-place) |  ❌ No (returns new list) |
# Returns |  None |  The sorted list |
# Works on |  Lists only |  Any iterable (list, tuple, str, dict) |


nums = [3, 1, 4, 1, 5, 9, 2]

# sort() — in-place, returns None
nums.sort()
print(nums)            # → [1, 1, 2, 3, 4, 5, 9]

# sorted() — returns new list
nums = [3, 1, 4, 1, 5, 9, 2]
new_list = sorted(nums)
print(new_list)        # → [1, 1, 2, 3, 4, 5, 9]
print(nums)            # → [3, 1, 4, 1, 5, 9, 2]  ← unchanged!

# Descending order
sorted(nums, reverse=True)        # → [9, 5, 4, 3, 2, 1, 1]

# Custom key (sort by length)
words = ["banana", "apple", "fig"]
sorted(words, key=lambda x: len(x))
# → ['fig', 'apple', 'banana']

# Sort dicts by a key
people = [{"name":"Alice","age":30}, {"name":"Bob","age":25}]
sorted(people, key=lambda p: p["age"])
# → [{'name':'Bob','age':25}, {'name':'Alice','age':30}]


# ────────────────────────────────────────────────────────────
# ⚡ SECTION 5 — LIST COMPREHENSIONS
# ────────────────────────────────────────────────────────────

# One-line shortcut for creating a list using a loop. Cleaner and faster than equivalent for-loop.

# ━━━ Basic Pattern ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


[expression for item in iterable if condition]

# Equivalent to:
result = []
for item in iterable:
    if condition:
        result.append(expression)


# ━━━ Examples ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# Squares of 0-9
squares = [x**2 for x in range(10)]
# → [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Even numbers from 1-20
evens = [x for x in range(1, 21) if x % 2 == 0]
# → [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Lengths of words
words = ["apple", "banana", "fig"]
lengths = [len(w) for w in words]
# → [5, 6, 3]

# Conditional expression: classify
nums = [1, 2, 3, 4, 5]
parity = ["even" if x%2==0 else "odd" for x in nums]
# → ['odd', 'even', 'odd', 'even', 'odd']

# Nested: extract from list of lists
matrix = [[1,2,3], [4,5,6]]
flat = [val for row in matrix for val in row]
# → [1, 2, 3, 4, 5, 6]


# ⚠️ WARN: 💡 When NOT to use comprehensions: If logic is complex (multiple conditions, nested ifs,
# side-effects),
# use a regular for loop instead. Readability over cleverness!


# ────────────────────────────────────────────────────────────
# 🪆 SECTION 6 — TUPLES
# ────────────────────────────────────────────────────────────


# Create
empty_tup = ()
single = (5,)              # NOTE: comma needed for single-element!
tup = (1, 2, 3)
no_parens = 1, 2, 3        # also a tuple (parens optional)

# Access (same as lists)
tup[0]                       # → 1
tup[-1]                      # → 3
tup[0:2]                     # → (1, 2)

# Methods (only 2!)
tup.count(2)                 # → 1
tup.index(3)                 # → 2

# Tuple unpacking (very useful!)
point = (10, 20)
x, y = point                  # x=10, y=20

# Swap variables (Pythonic)
a, b = 5, 10
a, b = b, a                   # now a=10, b=5

# Multiple return values
def stats(lst):
    return min(lst), max(lst), sum(lst)/len(lst)

low, high, avg = stats([3,7,2,8,5])


# ────────────────────────────────────────────────────────────
# 🎯 SECTION 7 — REUSABLE LIST PATTERNS
# ────────────────────────────────────────────────────────────


# ━━━ Pattern: Find Min/Max/Sum/Average ━━━━━━━━━━━━━━━━━━━


def analyze_numbers(numbers):
    if not numbers:
        return None
    return {
        'min':   min(numbers),
        'max':   max(numbers),
        'sum':   sum(numbers),
        'avg':   sum(numbers)/len(numbers),
        'count': len(numbers)
    }

print(analyze_numbers([10, 20, 30, 40, 50]))


# ━━━ Pattern: Filter + Map ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def squares_of_evens(numbers):
    # Manual loop version (beginner-friendly)
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n ** 2)
    return result

# Same with map+filter (Q from Mar 2024)
def squares_of_evens_v2(numbers):
    evens = filter(lambda x: x % 2 == 0, numbers)
    return list(map(lambda x: x**2, evens))

print(squares_of_evens([1,2,3,4,5,6]))   # → [4, 16, 36]


# ━━━ Pattern: Flatten Nested List (Aug 2021) ━━━━━━━━━━━━━


def flatten(nested_list):
    # Convert [[1,2,3], 4, [5,6]] → [1,2,3,4,5,6]
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(item)        # extend with sub-list
        else:
            flat.append(item)        # single value
    return flat

data = [[20,25,30], 24, [56,8], 9, [7,5]]
print(flatten(data))             # [20,25,30,24,56,8,9,7,5]
print(min(flatten(data)))        # → 5
print(sum(flatten(data))/len(flatten(data)))  # avg


# ━━━ Pattern: Frequency Counter ━━━━━━━━━━━━━━━━━━━━━━━━━━


def count_frequencies(items):
    # Count how many times each item appears
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(count_frequencies(words))
# → {'apple':3, 'banana':2, 'cherry':1}

# Most frequent
freq = count_frequencies(words)
most = max(freq, key=freq.get)
print(f"Most frequent: {most}")


# ━━━ Pattern: Longest Consecutive Sequence (Oct 2024) ━━━━


def longest_consecutive(numbers):
    # Use set for O(1) lookup, find sequence starts
    num_set = set(numbers)
    longest = 0
    for n in num_set:
        # Only start counting if n is the start of a sequence
        if (n - 1) not in num_set:
            current = n
            length = 1
            while (current + 1) in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# → 4 (sequence: 1,2,3,4)


# ────────────────────────────────────────────────────────────
# 🧠 SECTION 8 — MEMORY AIDS
# ────────────────────────────────────────────────────────────


# ━━━ 📋 Method Quick Reference ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# # ADD
# lst.append(x)        # 1 to end
# lst.insert(i, x)     # at index
# lst.extend([x,y])    # multiple
#
# # REMOVE
# lst.pop()            # last (returns)
# lst.pop(i)           # by index
# lst.remove(x)        # by value
# lst.clear()          # all
# del lst[i]           # by index
#
# # SEARCH
# lst.count(x)         # # of x's
# lst.index(x)         # first idx
# x in lst           # T/F
#
# # SORT
# lst.sort()           # in-place
# sorted(lst)          # new list
# lst.reverse()        # in-place
# lst[::-1]            # new reversed


# ━━━ ⚡ Comprehension Patterns ━━━━━━━━━━━━━━━━━━━━━━━━━━━━


[x*2 for x in lst]
[x for x in lst if ...]
['A' if x>=90 else 'B' for x in lst]
[(i,x) for i,x in enumerate(lst)]


# ━━━ 🎯 List vs Tuple Decision ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • Will data change? → list
#   • Fixed forever? → tuple
#   • Need as dict key? → tuple
#   • Performance-critical reads? → tuple

# ━━━ ⚠️ Common Traps ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • (5) is int — use (5,) for single-element tuple
#   • lst.sort() returns None, not the sorted list
#   • list.remove() raises ValueError if not found
#   • Modifying a list while iterating can skip items

# ────────────────────────────────────────────────────────────
# 🏋️ SECTION 9 — PRACTICE PROBLEMS
# ────────────────────────────────────────────────────────────

#   • Find the second largest number in a list
#   • Remove duplicates from a list (preserve order)
#   • Rotate a list by k positions
#   • Find common elements between two lists
#   • Check if a list is sorted (ascending)
#   • Group consecutive duplicates: [1,1,2,3,3,3,4] → [[1,1],[2],[3,3,3],[4]]
#   • Use list comprehension to convert [1,2,3,4,5] to [1,4,9,16,25]
# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ╔════════════════════════════════════════════════════════════╗
# ║  FILE 07 — Dictionaries & Sets                             ║
# ╚════════════════════════════════════════════════════════════╝


# ────────────────────────────────────────────────────────────
# 🗂 SECTION 1 — DICTIONARIES
# ────────────────────────────────────────────────────────────


# ━━━ What is a Dictionary? ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A dictionary stores key → value pairs . Think of it as a phone book: name (key) maps to phone
# number (value).
# Lookups are extremely fast (O(1)).


# Creation
empty = {}
prices = {"apple": 100, "banana": 50, "cherry": 200}

# Or with dict()
prices2 = dict(apple=100, banana=50)

# Access
print(prices["apple"])         # → 100
# print(prices["mango"])     ← ❌ KeyError

# Safe access with .get()
print(prices.get("mango"))      # → None (no error)
print(prices.get("mango", 0))   # → 0 (default)

# Length, membership
len(prices)                    # → 3
"apple" in prices             # → True (checks KEYS only)


# ────────────────────────────────────────────────────────────
# 🛠 SECTION 2 — DICTIONARY OPERATIONS
# ────────────────────────────────────────────────────────────


# ━━━ Add / Update / Delete ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ── 🔹 Exam Question (July 2021) ─────────────────────
# "How to change the value associated with the key in dictionary?"


prices = {"apple": 100, "banana": 50}

# UPDATE existing or ADD new (same syntax!)
prices["apple"] = 120          # update existing
prices["mango"] = 80           # add new key

# Update multiple at once
prices.update({"apple": 150, "orange": 90})
prices.update(grape=75)         # keyword form

# DELETE
del prices["banana"]            # by key
val = prices.pop("apple")        # by key, RETURNS value
val = prices.pop("missing", 0)   # default if missing
prices.popitem()                  # remove last inserted
prices.clear()                    # empty all


# ━━━ Iterating Over a Dictionary ━━━━━━━━━━━━━━━━━━━━━━━━━


prices = {"apple": 100, "banana": 50, "cherry": 200}

# Iterate keys (default)
for key in prices:
    print(key)                # apple, banana, cherry

# Iterate values
for val in prices.values():
    print(val)                # 100, 50, 200

# Iterate key-value pairs (most common)
for key, val in prices.items():
    print(f"{key}: {val}")

# Useful aggregations
sum(prices.values())             # total = 350
max(prices, key=prices.get)      # most expensive: 'cherry'
min(prices, key=prices.get)      # cheapest: 'banana'

# Sort by value
sorted(prices.items(), key=lambda x: x[1])
# → [('banana', 50), ('apple', 100), ('cherry', 200)]


# ────────────────────────────────────────────────────────────
# 🪆 SECTION 3 — NESTED DICTIONARIES (BILLING PATTERN)
# ────────────────────────────────────────────────────────────

# Used heavily in billing/inventory questions (6+ papers).

# ━━━ Pattern: Computer Assembly Bill (July 2021) ━━━━━━━━━


# Nested dict: outer key = item, inner = type:price
price_list = {
    "HDD": {"1TB": 5000, "2TB": 7500, "4TB": 10000},
    "RAM": {"8GB": 4000, "16GB": 6000},
    "Processor": {"I5": 15000, "I7": 18000}
}

def calculate_bill(price_list, choices, gst_rate=0.12):
    # choices = {"HDD": "1TB", "RAM": "8GB", ...}
    subtotal = 0
    for item, choice in choices.items():
        if item in price_list and choice in price_list[item]:
            subtotal += price_list[item][choice]
    gst   = subtotal * gst_rate
    total = subtotal + gst
    return {'subtotal': subtotal, 'gst': gst, 'total': total}

choices = {"HDD": "1TB", "RAM": "16GB", "Processor": "I5"}
print(calculate_bill(price_list, choices))
# {'subtotal': 26000, 'gst': 3120.0, 'total': 29120.0}


# ━━━ Pattern: Inventory Management (Oct 2024) ━━━━━━━━━━━━


# Dict: name → {qty, price}
inventory = {
    "Pen":    {"qty": 100, "price": 10},
    "Pencil": {"qty": 200, "price": 5},
    "Eraser": {"qty": 50,  "price": 8}
}

def total_value(inventory):
    total = 0
    for name, details in inventory.items():
        total += details["qty"] * details["price"]
    return total

def add_item(inventory, name, qty, price):
    inventory[name] = {"qty": qty, "price": price}

def update_qty(inventory, name, new_qty):
    if name in inventory:
        inventory[name]["qty"] = new_qty

print(total_value(inventory))    # 100*10 + 200*5 + 50*8 = 2400


# ━━━ Pattern: Date Validation (Mar 2024 Scan) ━━━━━━━━━━━━


days_in_month = {
    "January":31, "February":28, "March":31,
    "April":30,   "May":31,      "June":30,
    "July":31,    "August":31,   "September":30,
    "October":31, "November":30, "December":31
}

def validate_date(month, day):
    if month not in days_in_month:
        return False
    return 1 <= day <= days_in_month[month]

print(validate_date("January", 15))   # True
print(validate_date("January", 32))   # False
print(validate_date("February", 30))  # False


# ━━━ Pattern: Telephone Keypad (Nov 2023) ━━━━━━━━━━━━━━━━


keypad = {
    '2':'ABC', '3':'DEF', '4':'GHI',
    '5':'JKL', '6':'MNO', '7':'PQRS',
    '8':'TUV', '9':'WXYZ'
}
# Reverse mapping for letter → digit
letter_to_digit = {}
for digit, letters in keypad.items():
    for ch in letters:
        letter_to_digit[ch] = digit

print(letter_to_digit['C'])   # → '2'


# ────────────────────────────────────────────────────────────
# ⚡ SECTION 4 — DICTIONARY COMPREHENSIONS
# ────────────────────────────────────────────────────────────


# Pattern: {key_expr: value_expr for item in iterable if condition}

# Word lengths
words = ["apple", "banana", "cherry"]
lens = {w: len(w) for w in words}
# → {'apple': 5, 'banana': 6, 'cherry': 6}

# Square map
squares = {x: x**2 for x in range(1, 6)}
# → {1:1, 2:4, 3:9, 4:16, 5:25}

# Filter: only short words
short = {w: len(w) for w in words if len(w) < 6}
# → {'apple': 5}

# Swap keys and values
prices = {"apple": 100, "banana": 50}
swapped = {v: k for k, v in prices.items()}
# → {100: 'apple', 50: 'banana'}


# ────────────────────────────────────────────────────────────
# 🔵 SECTION 5 — SETS
# ────────────────────────────────────────────────────────────


# ━━━ What is a Set? ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A set is an unordered collection of UNIQUE elements . Used for fast membership testing and removing
# duplicates.


# Create
empty = set()                    # NOT {} — that's a dict!
s = {1, 2, 3}                  # or use {}
s2 = set([1, 2, 2, 3, 3])      # → {1, 2, 3} (duplicates removed!)

# Add / remove
s.add(4)                       # → {1, 2, 3, 4}
s.remove(2)                    # raises error if missing
s.discard(99)                  # silently ignores if missing

# Membership (very fast — O(1))
3 in s                        # → True/False

# Length
len(s)


# ━━━ Set Operations (Math!) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# A | B          # Union: {1,2,3,4,5,6}
# A & B          # Intersection: {3, 4}
# A - B          # Difference: {1, 2}
# A ^ B          # Symmetric diff: {1, 2, 5, 6}
#
# A.union(B)
# A.intersection(B)
# A.difference(B)
# A.symmetric_difference(B)


# ━━━ Common Use Cases ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 1. Remove duplicates
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))     # → [1, 2, 3, 4]

# 2. Check if all elements unique
def all_unique(lst):
    return len(lst) == len(set(lst))

# 3. Find common elements between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))   # → [3, 4]


# ────────────────────────────────────────────────────────────
# 🎯 SECTION 6 — SET-BASED ALGORITHMS
# ────────────────────────────────────────────────────────────


# ━━━ Pattern: Cycle Detection — Happy Number ━━━━━━━━━━━━━

# ── 🔹 Exam Question (Mar 2024 Scan) ─────────────────
# "Write isHappy(n) — replace n by sum of squares of digits, repeat until 1 (happy) or cycles (not
# happy)."


def digit_squares_sum(n):
    # Helper: sum of squares of each digit
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 2
        n //= 10
    return total

def is_happy(n):
    # Use SET to track seen values — detect cycle
    seen = set()
    while n != 1:
        if n in seen:           # O(1) lookup — cycle!
            return False
        seen.add(n)
        n = digit_squares_sum(n)
    return True

print(is_happy(19))   # → True (19 → 82 → 68 → 100 → 1)
print(is_happy(4))    # → False (4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 [cycle!])


# ━━━ Pattern: Longest Consecutive Sequence (Oct 2024) ━━━━


def longest_consecutive(numbers):
    # Set lets us check (n-1) and (n+1) in O(1)
    num_set = set(numbers)
    longest = 0
    for n in num_set:
        if (n - 1) not in num_set:    # start of a sequence
            current = n
            length = 1
            while (current + 1) in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # → 4


# ────────────────────────────────────────────────────────────
# 🧠 SECTION 7 — MEMORY AIDS
# ────────────────────────────────────────────────────────────


# ━━━ 🗂 Dict Quick Reference ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# d[k] = v           # add/update
# d.get(k)           # safe access
# d.get(k, default)
# d.update({...})    # multiple
# del d[k]            # delete
# d.pop(k)           # delete + return
# d.keys()           # key view
# d.values()         # value view
# d.items()          # pair view
# k in d             # T/F (keys only)


# ━━━ 🔵 Set Quick Reference ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# s.add(x)           # add
# s.remove(x)        # raises error
# s.discard(x)       # silent
# A | B   union
# A & B   intersect
# A - B   difference
# A ^ B   symmetric
# len(s)             # count


# ━━━ ⚡ When to Use Each ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • Dict: key → value lookup, billing, frequency counting
#   • Set: uniqueness, fast membership, remove duplicates, cycle detection
#   • List: ordered, allows duplicates, indexed access

# ━━━ ⚠️ Common Traps ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • {} creates an empty dict, not set! Use set()
#   • Sets are unordered — don't rely on iteration order
#   • k in d checks keys, not values
#   • Dict keys must be hashable (immutable)

# ────────────────────────────────────────────────────────────
# 🏋️ SECTION 8 — PRACTICE PROBLEMS
# ────────────────────────────────────────────────────────────

#   • Build a frequency counter for words in a sentence
#   • Merge two dictionaries (later values win on conflict)
#   • Invert a dictionary: swap keys and values
#   • Find the most common element in a list using dict
#   • Build a phone book add/lookup/delete system using dict
#   • Find duplicates in a list using a set
#   • Implement a simple set-based cycle detector for any function
# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ╔════════════════════════════════════════════════════════════╗
# ║  FILE 08 — NumPy                                           ║
# ╚════════════════════════════════════════════════════════════╝


# ────────────────────────────────────────────────────────────
# 🚀 SECTION 1 — INTRO TO NUMPY
# ────────────────────────────────────────────────────────────


# ━━━ What is NumPy? ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# NumPy = "Numerical Python". It provides the `ndarray` (n-dimensional array) — much faster than
# Python lists for numerical operations.

# ── 🔹 Exam Question ─────────────────────────────────
# "Define significant features of NumPy library." — Model Set

# ━━━ Key Features (for theory questions) ━━━━━━━━━━━━━━━━━
#   • ndarray: Multi-dimensional homogeneous arrays
#   • Vectorized operations: Apply ops on entire arrays without loops
#   • Broadcasting: Operate on arrays of different shapes
#   • Speed: Implemented in C, much faster than Python lists
#   • Memory efficient: Stores raw numeric data without Python object overhead
#   • Linear algebra functions: Matrix operations, decomposition, eigenvalues
#   • Random number generation: np.random module
#   • Integration: Foundation for pandas, SciPy, scikit-learn, TensorFlow

# ━━━ Array vs List ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# [Feature]  [Python List]  [NumPy Array]
# Element types |  Mixed |  Same (homogeneous) |
# Speed |  Slow |  Fast |
# Memory |  More |  Less |
# Math ops |  Element-by-element loop needed |  Vectorized (no loops) |


import numpy as np

# Create from list
a = np.array([1, 2, 3, 4, 5])
print(a)              # [1 2 3 4 5]
print(type(a))        # 

# Vectorized math (no loops needed!)
print(a * 2)          # [2 4 6 8 10]
print(a + a)          # [2 4 6 8 10]
print(a ** 2)         # [1 4 9 16 25]


# ────────────────────────────────────────────────────────────
# 🏗 SECTION 2 — CREATING ARRAYS
# ────────────────────────────────────────────────────────────


import numpy as np

# From Python list
np.array([1,2,3])              # 1D
np.array([[1,2],[3,4]])        # 2D matrix

# Special arrays
np.zeros((3, 4))               # 3x4 of zeros
np.ones((2, 3))                # 2x3 of ones
np.full((3, 3), 7)              # 3x3 all 7s
np.eye(3)                       # 3x3 identity matrix
np.identity(4)                  # same
np.diag([1,2,3])                  # diagonal matrix

# Range arrays
np.arange(10)                    # [0 1 2 ... 9]
np.arange(2, 10, 2)                # [2 4 6 8]
np.linspace(0, 1, 5)              # [0., 0.25, 0.5, 0.75, 1.] (5 points)

# Random
np.random.rand(3, 3)             # 3x3 in [0,1)
np.random.randint(1, 100, 5)        # 5 ints in [1,100)
np.random.normal(0, 1, 100)         # 100 from N(0,1)

# Properties
a = np.array([[1,2,3],[4,5,6]])
a.shape         # (2, 3)
a.ndim          # 2 (number of dimensions)
a.size          # 6 (total elements)
a.dtype         # int64


# ── 🔹 Exam Question ─────────────────────────────────
# "Differentiate between np.arange() and np.linspace()." — October 2024

# [Function]  [Specifies]  [Example]  [Result]
# np.arange(start, stop, step) |  STEP size |  np.arange(0, 1, 0.25) |  [0, 0.25, 0.5, 0.75] |
# np.linspace(start, stop, num) |  NUMBER of points |  np.linspace(0, 1, 5) |  [0, 0.25, 0.5, 0.75, 1.0] |

# Key difference: arange is exclusive of stop, linspace is inclusive.

# ────────────────────────────────────────────────────────────
# 🆔 SECTION 3 — IDENTITY MATRIX (np.eye)
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (July 2021) ─────────────────────
# "What is an identity matrix? How to create it using numpy library?"
#
#
# Identity matrix : Square matrix with 1s on the main diagonal and 0s elsewhere. Property: A × I = A
# (like multiplying a number by 1).


import numpy as np

I3 = np.eye(3)
print(I3)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Same as np.identity(n)
np.identity(4)

# Integer dtype
np.eye(3, dtype=int)
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

# Verify: A × I = A
A = np.array([[2,3],[4,5]])
I = np.eye(2)
print(A @ I)        # same as A


# ── 🧠 Memory Aid ────────────────────────────────────
# 🧠 np.eye = "Eye on the diagonal" — looks like the letter I

# ────────────────────────────────────────────────────────────
# 🔄 SECTION 4 — reshape() vs resize()
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (3 papers!) ─────────────────────
# "Difference between reshape() and resize() methods?" — May 2025, Feb 2025, November 2023

# [Feature]  [reshape()]  [resize()]
# Returns |  NEW array (view) |  None (modifies in-place) |
# Original array |  Unchanged |  Modified |
# Total elements |  Must stay same |  Can change (fills with 0 or repeats) |


import numpy as np

a = np.array([1,2,3,4,5,6])

# reshape — new shape, total = 6 must remain
b = a.reshape(2, 3)
print(b)
# [[1 2 3]
#  [4 5 6]]
print(a)              # [1 2 3 4 5 6] - UNCHANGED

# Use -1 to auto-compute one dimension
c = a.reshape(3, -1)     # 3 rows, 6/3=2 cols

# resize — modifies original
a.resize(3, 2)
print(a)
# [[1 2]
#  [3 4]
#  [5 6]]  - a was modified

# resize can also add elements
a = np.array([1,2,3])
a.resize(2, 3)         # 6 elements but only 3 → fills 0s
print(a)
# [[1 2 3]
#  [0 0 0]]


# ── 🧠 Memory Aid ────────────────────────────────────
# 🧠 reshape = "show me Reshape" (new view) · resize = "Resize me" (in-place change)

# ────────────────────────────────────────────────────────────
# 📚 SECTION 5 — vstack & hstack & split
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (Mar 2024 PDF) ──────────────────
# "How is vstack() different from hstack() in NumPy?"

# [Function]  [Purpose]  [Memory Aid]
# np.vstack |  Stack VERTICALLY (more rows) |  V = Vertical = adds rows |
# np.hstack |  Stack HORIZONTALLY (more cols) |  H = Horizontal = adds cols |
# np.concatenate |  General version (specify axis) |  axis=0 vertical, axis=1 horizontal |


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# vstack — stack vertically (more rows)
np.vstack((a, b))
# [[1 2 3]
#  [4 5 6]]

# hstack — stack horizontally (extends row)
np.hstack((a, b))
# [1 2 3 4 5 6]

# 2D example
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

np.vstack((A,B))   # 4x2 (more rows)
np.hstack((A,B))   # 2x4 (more cols)


# ━━━ Split (Inverse Operation) ━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ── 🔹 Exam Question (July 2021) ─────────────────────
# "Explain split() method for arrays."


arr = np.array([1,2,3,4,5,6])

# Equal split
np.split(arr, 3)
# [array([1,2]), array([3,4]), array([5,6])]

# Split at specific indices
np.split(arr, [2, 4])
# [array([1,2]), array([3,4]), array([5,6])]

# Split into UNEQUAL parts (allows uneven)
np.array_split(arr, 4)        # 6 elements / 4 parts

# 2D split
mat = np.arange(12).reshape(3, 4)
np.hsplit(mat, 2)              # split by columns (horizontal)
np.vsplit(mat, 3)              # split by rows (vertical)


# ────────────────────────────────────────────────────────────
# 📡 SECTION 6 — BROADCASTING
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (Feb 2025) ──────────────────────
# "Explain NumPy broadcasting with example."
#
#
# Broadcasting : NumPy auto-stretches smaller arrays to match shapes for operations. Avoids manual
# loops.

# ━━━ 3 Broadcasting Rules ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • If shapes differ, prepend 1s to the smaller shape
#   • Two dimensions are compatible if they're equal OR one of them is 1
#   • Size 1 is "stretched" to match the larger size


import numpy as np

# Scalar + array (scalar broadcast to all elements)
a = np.array([1, 2, 3])
print(a + 10)          # [11 12 13] - scalar 10 added to each

# 1D + 2D (1D broadcast to each row)
mat = np.array([[1,2,3],[4,5,6]])
row = np.array([10, 20, 30])
print(mat + row)
# [[11 22 33]
#  [14 25 36]]

# Column vector + row vector (creates matrix)
col = np.array([[1],[2],[3]])     # shape (3,1)
row = np.array([10, 20])         # shape (2,)
print(col + row)
# [[11 21]
#  [12 22]
#  [13 23]]


# ────────────────────────────────────────────────────────────
# ⚡ SECTION 7 — INDEXING & SLICING
# ────────────────────────────────────────────────────────────


arr = np.array([10, 20, 30, 40, 50])

# 1D slicing (same as Python list)
arr[0]              # 10
arr[-1]             # 50
arr[1:4]            # [20, 30, 40]
arr[::2]            # [10, 30, 50]

# 2D slicing
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
mat[0, 1]           # 2 (row 0, col 1)
mat[0]              # [1 2 3] (entire row 0)
mat[:, 1]           # [2 5 8] (entire col 1)
mat[0:2, 1:3]       # top-right 2x2 subset

# Boolean indexing (very powerful!)
arr = np.array([10, 25, 8, 42, 17])
mask = arr > 20             # [False True False True False]
print(arr[mask])           # [25 42]

# One-liner
print(arr[arr > 20])      # [25 42]

# Multiple conditions
print(arr[(arr > 10) & (arr < 40)])   # [25 17]


# ────────────────────────────────────────────────────────────
# 📊 SECTION 8 — STATISTICAL FUNCTIONS
# ────────────────────────────────────────────────────────────


arr = np.array([3, 7, 1, 9, 5, 2])

print(arr.sum())            # 27
print(arr.mean())           # 4.5
print(arr.min(), arr.max()) # 1 9
print(arr.std())            # standard deviation
print(arr.var())            # variance
print(arr.argmin())         # 2 (index of min)
print(arr.argmax())         # 3 (index of max)
print(np.median(arr))       # 4.0

# 2D — axis matters!
mat = np.array([[1,2,3],[4,5,6]])
mat.sum()                # 21 (all)
mat.sum(axis=0)          # [5 7 9]   (column sums)
mat.sum(axis=1)          # [6 15]    (row sums)


# ━━━ any() and all() (Feb 2025) ━━━━━━━━━━━━━━━━━━━━━━━━━━


arr = np.array([True, False, True, True])

print(arr.any())           # True (at least one True)
print(arr.all())           # False (NOT all True)

# Useful with conditions
nums = np.array([5, 10, 15])
print((nums > 0).all())   # True - all positive
print((nums > 7).any())   # True - some > 7


# ────────────────────────────────────────────────────────────
# 🧠 SECTION 9 — MEMORY AIDS
# ────────────────────────────────────────────────────────────


# ━━━ 🏗 Array Creation ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


np.zeros((3,4))
np.ones((2,3))
np.eye(3)         # identity
np.arange(10)    # 0..9
np.linspace(0,1,5)
np.random.rand(3,3)


# ━━━ 🔄 Shape Manipulation ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


arr.reshape(r,c)   # new view
arr.resize(r,c)    # in-place
arr.flatten()      # 1D copy
arr.T              # transpose
np.vstack          # stack rows
np.hstack          # stack cols
np.split           # equal split


# ━━━ 📊 Stats Methods ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


arr.sum()
arr.mean()
arr.min(), arr.max()
arr.std(), arr.var()
arr.argmin(), arr.argmax()
np.median(arr)
arr.any(), arr.all()


# ━━━ 🎯 Axis Direction ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • axis=0 = collapse rows → COLUMN result (down)
#   • axis=1 = collapse columns → ROW result (across)
#   • Memory: "axis=0 keeps the columns"

# ────────────────────────────────────────────────────────────
# 🏋️ SECTION 10 — PRACTICE PROBLEMS
# ────────────────────────────────────────────────────────────

#   • Create a 5x5 matrix with values 1 to 25
#   • Reverse all elements of a 1D array (use slicing)
#   • Replace all values > 50 in an array with -1
#   • Compute row-wise and column-wise sum of a 3x3 matrix
#   • Generate 100 random numbers and find their mean and std
#   • Create a checkerboard 8x8 matrix (0s and 1s alternating)
#   • Verify A * I = A using np.eye() for any 3x3 matrix A
# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ╔════════════════════════════════════════════════════════════╗
# ║  FILE 09 — Pandas Basics                                   ║
# ╚════════════════════════════════════════════════════════════╝


# ────────────────────────────────────────────────────────────
# 🐼 SECTION 1 — INTRO TO PANDAS
# ────────────────────────────────────────────────────────────


# ━━━ Two Main Data Structures ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# [Structure]  [Description]  [Like]
# Series |  1D labeled array (single column) |  List with named indices |
# DataFrame |  2D labeled table (multiple columns) |  Excel sheet / SQL table |


# ── 🔹 Exam Question ─────────────────────────────────
# "Define significant features of pandas library." — August 2021

# ━━━ Key Features ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • DataFrame: Tabular structure with labeled rows and columns
#   • Read/Write: CSV, Excel, JSON, SQL, etc.
#   • Missing data handling: dropna(), fillna()
#   • Group by + aggregations: split-apply-combine
#   • Merging/Joining: SQL-style operations
#   • Time series: Date/time indexing
#   • Built on NumPy: Fast vectorized operations


import pandas as pd
import numpy  as np

# Create a Series
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
# a    10
# b    20
# c    30

# Create a DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age':  [25, 30, 35],
    'City': ['BLR', 'DEL', 'MUM']
})
print(df)


# ────────────────────────────────────────────────────────────
# 📁 SECTION 2 — READING DATA
# ────────────────────────────────────────────────────────────


import pandas as pd

# From CSV (most common)
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", index_col=0)        # first column as index
df = pd.read_csv("data.csv", na_values=["?","NA"]) # custom NA

# Other formats
df = pd.read_excel("data.xlsx")
df = pd.read_json("data.json")


# ────────────────────────────────────────────────────────────
# 🔍 SECTION 3 — EXPLORING DATA (FIRST STEPS)
# ────────────────────────────────────────────────────────────


# ━━━ Standard Inspection (Use for EVERY dataset) ━━━━━━━━━


# Shape: (rows, columns)
df.shape

# First/last rows
df.head()        # first 5 rows
df.head(10)      # first 10
df.tail()        # last 5

# Column names
df.columns
df.columns.tolist()

# Data types per column
df.dtypes

# Summary info: dtypes + non-null counts
df.info()

# Statistical summary (numeric columns)
df.describe()
df.describe(include='all')        # include non-numeric

# Number of rows
len(df)


# ━━━ Numerical vs Categorical Columns (July 2021) ━━━━━━━━


# Get only numerical columns
numerical = df.select_dtypes(include=['number']).columns.tolist()

# Get only non-numerical columns
non_numerical = df.select_dtypes(exclude=['number']).columns.tolist()

print(f"Numerical: {numerical}")
print(f"Non-numerical: {non_numerical}")


# ────────────────────────────────────────────────────────────
# 📍 SECTION 4 — INDEXING (loc & iloc)
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (Feb 2025) ──────────────────────
# "Explain loc and iloc indexing with examples."

# []  [loc]  [iloc]
# Type |  LABEL-based |  POSITION-based (integer) |
# Range |  Inclusive on both ends |  Exclusive on stop (like Python lists) |
# Example |  df.loc[0:2, 'Name'] |  df.iloc[0:2, 0] |


# Sample df with custom index
df = pd.DataFrame({
    'A': [1,2,3,4],
    'B': [5,6,7,8]
}, index=['w','x','y','z'])

# ── loc: by LABEL ──
df.loc['x']              # row labeled 'x'
df.loc['x', 'A']         # single cell
df.loc['w':'y']           # INCLUSIVE: w, x, y
df.loc[:, 'A']           # all rows, column A
df.loc[df['A'] > 2]     # BOOLEAN indexing

# ── iloc: by POSITION ──
df.iloc[0]              # first row
df.iloc[0, 1]           # row 0, col 1
df.iloc[0:2]            # EXCLUSIVE: rows 0,1
df.iloc[:, 0]           # first column
df.iloc[-1]             # last row

# Column access (no loc/iloc needed)
df['A']                # single column → Series
df[['A', 'B']]         # multiple columns → DataFrame


# ────────────────────────────────────────────────────────────
# 🔧 SECTION 5 — FILTERING ROWS
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (Oct 2024) ──────────────────────
# "How to filter rows in pandas based on condition?"


# Single condition
df[df['Age'] > 25]

# Multiple conditions (use & for AND, | for OR)
df[(df['Age'] > 25) & (df['City'] == 'BLR')]
df[(df['Age'] < 20) | (df['Age'] > 60)]
# NOTE: parentheses around each condition are required!

# Membership filter
df[df['City'].isin(['BLR', 'DEL'])]

# NOT membership
df[~df['City'].isin(['BLR'])]    # ~ = NOT

# String-based filter
df[df['Name'].str.startswith('A')]
df[df['Name'].str.contains('lice')]
df[df['Email'].str.endswith('.com')]

# between (inclusive)
df[df['Age'].between(25, 35)]

# query() — alternative readable syntax
df.query("Age > 25 and City == 'BLR'")


# ────────────────────────────────────────────────────────────
# ❓ SECTION 6 — MISSING VALUES
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (2 papers!) ─────────────────────
# "How do you identify missing values and deal with missing values in DataFrame?" — Mar 2024 Scan,
# Nov 2023

# ━━━ IDENTIFY Missing Values ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


df.isnull()              # True where NaN, False otherwise
df.isnull().sum()        # count of NaN per column
df.isnull().sum().sum()  # total NaN count
df.isnull().mean() * 100 # % missing per column

df.notna()               # inverse: True where NOT NaN
df.info()                # shows non-null counts


# ━━━ HANDLE Missing Values ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# Drop rows with ANY NaN
df.dropna()

# Drop only if specific column has NaN
df.dropna(subset=['Age'])

# Drop columns where ALL values are NaN
df.dropna(axis=1, how='all')

# Fill with constant
df.fillna(0)
df.fillna("Unknown")

# Fill with column mean (numeric only)
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Forward fill (use previous value)
df.fillna(method='ffill')

# Backward fill
df.fillna(method='bfill')

# Different fill per column
df.fillna({'Age': 0, 'Name': 'Unknown'})


# ── 🔹 Exam Question (Oct 2024) ──────────────────────
# "Difference between dropna() with axis=0 and axis=1."

# [Parameter]  [Effect]  [Use when]
# axis=0 (default) |  Drop ROWS with NaN |  Few rows have NaN |
# axis=1 |  Drop COLUMNS with NaN |  An entire column is mostly empty |


# ────────────────────────────────────────────────────────────
# 🔁 SECTION 7 — REMOVING DUPLICATES
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (Mar 2024 Scan) ─────────────────
# "Which function can be used to remove duplicates in DataFrames?"


# Identify duplicates
df.duplicated()              # True for duplicate rows
df.duplicated().sum()        # count duplicates

# Remove duplicates
df.drop_duplicates()         # keep first by default
df.drop_duplicates(keep='last')
df.drop_duplicates(keep=False)        # drop ALL copies

# Based on specific columns
df.drop_duplicates(subset=['Name'])
df.drop_duplicates(subset=['Name', 'City'])

# In-place
df.drop_duplicates(inplace=True)


# ────────────────────────────────────────────────────────────
# 🗑 SECTION 8 — DROPPING ROWS/COLUMNS
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (Model Set) ─────────────────────
# "How to delete rows and columns from a DataFrame?"


# Drop rows by index
df.drop(0)                      # drop row with index 0
df.drop([0, 1, 2])                # multiple

# Drop columns
df.drop('Age', axis=1)             # drop column 'Age'
df.drop(['Age', 'City'], axis=1)    # multiple columns

# Equivalent (uses 'columns' or 'index')
df.drop(columns=['Age', 'City'])
df.drop(index=[0, 1])

# In-place
df.drop('Age', axis=1, inplace=True)


# ────────────────────────────────────────────────────────────
# 📊 SECTION 9 — ADDING COLUMNS
# ────────────────────────────────────────────────────────────


# Add new column with constant
df['Country'] = 'India'

# Add new column from existing
df['AgePlusOne'] = df['Age'] + 1

# Add column from another DataFrame's series
df['Score'] = scores_series

# Add row-wise mean
df['avg_rating'] = df[['A','B','C']].mean(axis=1).round(1)

# Add column based on condition (apply with lambda)
df['Senior'] = df['Age'].apply(lambda x: 'Yes' if x >= 60 else 'No')

# Add column using assign() (chainable)
df = df.assign(NewCol=df['Age'] * 2)


# ────────────────────────────────────────────────────────────
# 🔢 SECTION 10 — VALUE COUNTS & UNIQUE
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question (Feb 2025) ──────────────────────
# "Difference between value_counts() and count()."

# [Method]  [What it does]
# df['col'].count() |  Count NON-NULL entries (single number) |
# df['col'].value_counts() |  Count occurrences of EACH unique value (Series) |
# df['col'].unique() |  List of unique values (array) |
# df['col'].nunique() |  Count of unique values (single number) |


# Sample data
df = pd.DataFrame({'City': ['BLR', 'DEL', 'BLR', 'MUM', 'BLR', None]})

df['City'].count()        # → 5 (excludes None)

df['City'].value_counts()
# BLR    3
# DEL    1
# MUM    1

df['City'].value_counts(normalize=True)   # proportions instead of counts

df['City'].unique()       # → ['BLR', 'DEL', 'MUM', None]
df['City'].nunique()      # → 3 (unique non-null count)


# ────────────────────────────────────────────────────────────
# 🏷 SECTION 11 — CATEGORICAL DATA
# ────────────────────────────────────────────────────────────


# ── 🔹 Exam Question ─────────────────────────────────
# "Explain categorical data in pandas. How to convert?" — August 2021, May 2025
#
#
# Categorical data = data that has a fixed set of possible values (like Gender: M/F or Grade: A/B/C).
# Storing as `category` dtype saves memory and enables ordering.


# Convert to categorical
df['Grade'] = df['Grade'].astype('category')

# Check dtype
print(df['Grade'].dtype)        # category

# Get unique categories
print(df['Grade'].cat.categories)

# Set ordered categories
from pandas.api.types import CategoricalDtype
ordered = CategoricalDtype(['F','D','C','B','A'], ordered=True)
df['Grade'] = df['Grade'].astype(ordered)
# Now A > B > C > D > F


# ────────────────────────────────────────────────────────────
# 🧠 SECTION 12 — MEMORY AIDS
# ────────────────────────────────────────────────────────────


# ━━━ 🔍 Inspection Cheatsheet ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


df.shape       # (rows, cols)
df.head()      # first 5
df.tail()      # last 5
df.info()      # dtypes + nulls
df.describe()  # stats
df.dtypes      # col types
df.columns     # col names


# ━━━ 📍 loc vs iloc ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • loc: by LABEL, INCLUSIVE end
#   • iloc: by POSITION, EXCLUSIVE end
#   • df['col'] → no loc/iloc needed
#   • Boolean: df[df['x']>5]

# ━━━ ❓ Missing Value Workflow ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • Find: df.isnull().sum()
#   • Drop: df.dropna()
#   • Fill: df.fillna(value)
#   • Forward fill: method='ffill'

# ━━━ 🔁 Filter Patterns ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


df[df['A'] > 5]
df[df['A'].isin([1,2])]
df[(df['A']>5) & (df['B']<10)]
df[df['col'].str.contains('x')]
df[df['A'].between(5,10)]


# ────────────────────────────────────────────────────────────
# 🏋️ SECTION 13 — PRACTICE PROBLEMS
# ────────────────────────────────────────────────────────────

#   • Read a CSV, show first 10 rows, dtypes, and stats
#   • Find columns with missing values and their percentages
#   • Drop duplicate rows and rows with any NaN
#   • Filter rows where age > 30 AND salary < 100000
#   • Add a new column 'AgeGroup' classifying ages into Young/Middle/Senior
#   • Count occurrences of each city, show top 3
#   • Convert all string columns to categorical
# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ╔════════════════════════════════════════════════════════════╗
# ║  FILE 10 — Pandas Advanced                                 ║
# ╚════════════════════════════════════════════════════════════╝


# ━━━ 📋 TABLE OF CONTENTS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • 1. groupby() — The Power Tool
#   • 2. agg() — Multiple Aggregations
#   • 3. concat / merge / join
#   • 4. pivot vs crosstab
#   • 5. apply() with lambda (axis=1)
#   • 6. rank() — 5 Methods
#   • 7. sort_values vs sort_index
#   • 8. value_counts() and unique()
#   • 9. nlargest / nsmallest
#   • 10. isin() Filtering
#   • 11. Multi-level GroupBy + unstack
#   • 🧩 Reusable Patterns
#   • 📌 Cheatsheet
#   • 🧠 Memory Aids

# ────────────────────────────────────────────────────────────
# 1️⃣ groupby() — The Most Important Pandas Tool
# ────────────────────────────────────────────────────────────


# ────────────────────────────────────────────
# CONCEPTgroupby = Split → Apply → Combine
# ────────────────────────────────────────────


# ── 🔹 What & Why ────────────────────────────────────
# groupby divides your DataFrame into groups based on column values, then lets you
# compute statistics for each group. It's the SQL equivalent of `GROUP BY`.
# Real-world examples:
#   • Average salary per department (titanic, adult datasets)
#   • Count of passengers per embarked port (Nov 2023 Titanic)
#   • Survival rate per cabin type (Nov 2023 Titanic)
#   • Avg population per continent (Mar 2024 Countries)

# ── 🔹 Basic Syntax (Memorise This) ──────────────────


import pandas as pd

df = pd.DataFrame({
    'Dept':   ['IT', 'HR', 'IT', 'HR', 'Finance'],
    'Salary': [70000, 50000, 80000, 55000, 60000],
    'Age':    [28, 32, 45, 29, 38]
})

# ── Step 1: SPLIT into groups by 'Dept' ──
# ── Step 2: APPLY function (mean) to each group ──
# ── Step 3: COMBINE results ──
df.groupby('Dept')['Salary'].mean()
# Output:
#   Finance    60000.0
#   HR         52500.0
#   IT         75000.0

# ── Common aggregations ──
df.groupby('Dept')['Salary'].sum()       # total per group
df.groupby('Dept')['Salary'].count()     # count per group
df.groupby('Dept')['Salary'].max()       # max per group
df.groupby('Dept')['Salary'].min()       # min per group
df.groupby('Dept')['Salary'].median()    # median per group
df.groupby('Dept')['Salary'].std()       # std deviation


# ── 🔹 Reusable Pattern ──────────────────────────────


def group_summary(df, group_col, value_col, agg_func='mean'):
    "Generic grouping helper.
    Args: df=DataFrame, group_col=str, value_col=str, agg_func='mean'/'sum'/etc.
    Returns: Series with group_col as index."
    return df.groupby(group_col)[value_col].agg(agg_func)

# Use for ANY question like "average X per Y"
group_summary(titanic, 'Embarked', 'Survived', 'mean')   # survival per port
group_summary(adult, 'occupation', 'age', 'mean')         # avg age per job
group_summary(water, 'Potability', 'Turbidity', 'max')     # max turbidity per status


# ── 🔹 Used in Every Section C ───────────────────────
# Aug 2021, Oct 2024, Feb 2025, May 2025, Mar 2024 (both), Nov 2023, Model Set, Jul 2021 — every
# dataset paper has 2–4 groupby questions.

# ────────────────────────────────────────────────────────────
# 2️⃣ agg() — Multiple Aggregations at Once
# ────────────────────────────────────────────────────────────


# ── 🔹 Three Ways to Use agg() ───────────────────────


# ── Method 1: List of functions (same on all columns) ──
df.groupby('Dept').agg(['mean', 'min', 'max'])
# Returns DataFrame with mean, min, max for ALL numeric columns

# ── Method 2: Different functions per column (DICT) ──
df.groupby('Dept').agg({
    'Salary': ['mean', 'max'],   # two stats for Salary
    'Age':    'mean'             # one stat for Age
})

# ── Method 3: Named aggregation (CLEANEST OUTPUT) ──
df.groupby('Dept').agg(
    Avg_Salary = ('Salary', 'mean'),
    Max_Salary = ('Salary', 'max'),
    Avg_Age    = ('Age',    'mean'),
    Count      = ('Age',    'count')
).round(2)
# Output: clean column names — recommended for exams


# ── 🔹 Pattern: Multi-Stat Summary ───────────────────


def multi_stat_summary(df, group_col, stats_dict):
    "Compute multiple stats per group.
    stats_dict: {output_name: (column, function)}"
    return df.groupby(group_col).agg(**{
        name: spec for name, spec in stats_dict.items()
    }).round(2)

# Example use (Nov 2023 Titanic Q4b.4)
stats = {
    'Passenger_Count': ('PassengerId', 'count'),
    'Avg_Age':         ('Age',         'mean'),
    'Median_Fare':     ('Fare',        'median')
}
multi_stat_summary(titanic, 'Embarked', stats)


# ────────────────────────────────────────────────────────────
# 3️⃣ Combining DataFrames — concat / merge / join
# ────────────────────────────────────────────────────────────


# ── 🔹 Three Methods Compared ────────────────────────

# [Method]  [What it does]  [When to use]
# pd.concat() |  Stack rows or columns |  Same columns, different rows (or vice versa) |
# pd.merge() |  SQL-style join on column |  Combining tables with a common key |
# df.join() |  Join on index |  Quick join when index is the key |


# ── 🔹 Examples ──────────────────────────────────────


import pandas as pd

df1 = pd.DataFrame({'ID':[1,2,3], 'Name':['A','B','C']})
df2 = pd.DataFrame({'ID':[2,3,4], 'Score':[88,75,92]})
df3 = pd.DataFrame({'ID':[4,5],   'Name':['D','E']})

# ── concat: stack rows (axis=0, default) ──
pd.concat([df1, df3], ignore_index=True)
#    ID Name
# 0   1    A
# 1   2    B
# 2   3    C
# 3   4    D
# 4   5    E

# ── concat: stack columns (axis=1) ──
pd.concat([df1, df2], axis=1)
# Places df2 columns BESIDE df1 (matches by row position)

# ── merge: inner join (DEFAULT) — only matching keys ──
pd.merge(df1, df2, on='ID')
#    ID Name  Score
# 0   2    B     88
# 1   3    C     75

# ── merge: left join — keep all of df1 ──
pd.merge(df1, df2, on='ID', how='left')
#    ID Name  Score
# 0   1    A    NaN  ← unmatched, NaN
# 1   2    B   88.0
# 2   3    C   75.0

# ── merge: outer join — keep ALL keys from both ──
pd.merge(df1, df2, on='ID', how='outer')

# ── join: works on index ──
df1_idx = df1.set_index('ID')
df2_idx = df2.set_index('ID')
df1_idx.join(df2_idx, how='inner')


# ── 🔹 Pattern: Safe Combiner ────────────────────────


def combine_dfs(df1, df2, mode='merge', key=None, how='inner'):
    "Generic combiner: works for concat, merge, or join."
    if mode == 'concat_rows':
        return pd.concat([df1, df2], ignore_index=True)
    elif mode == 'concat_cols':
        return pd.concat([df1, df2], axis=1)
    elif mode == 'merge':
        return pd.merge(df1, df2, on=key, how=how)
    elif mode == 'join':
        return df1.join(df2, how=how)


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 concat = stack · merge = SQL JOIN on column · join = JOIN on index
# Default merge = inner join (only matching rows kept)
# Mar 2024 Olympics paper : merge athletes_df with countries_df on `'NOC'`

# ────────────────────────────────────────────────────────────
# 4️⃣ pivot_table vs crosstab — Cross-Categorical Summaries
# ────────────────────────────────────────────────────────────


# ── 🔹 Concept — Why You Need Both ───────────────────
# Both create 2-way summary tables . The difference is small but exam-critical:
#   • crosstab: counts frequencies (default = count). Best for "how many in each category".
#   • pivot_table: aggregates a value column. Best for "average X per category × category".

# ── 🔹 Examples ──────────────────────────────────────


import pandas as pd

# Sample: Covid patient data (Aug 2021 paper Section C)
df = pd.DataFrame({
    'Diabetes': ['Yes','No','Yes','No','Yes','No'],
    'Survived': ['Y','Y','N','Y','N','N'],
    'Age':      [45,50,60,35,70,55]
})

# ── crosstab: count combinations ──
pd.crosstab(df['Diabetes'], df['Survived'])
# Survived   N   Y
# Diabetes
# No         1   2
# Yes        2   1

# ── crosstab with percentages (normalize='index') ──
pd.crosstab(df['Diabetes'], df['Survived'], normalize='index')
# Each ROW sums to 1.0 → "of diabetic patients, what % survived?"

# ── crosstab with margins (totals) ──
pd.crosstab(df['Diabetes'], df['Survived'], margins=True)
# Adds 'All' row and column with totals

# ── pivot_table: aggregate a numeric column ──
df.pivot_table(values='Age', index='Diabetes',
               columns='Survived', aggfunc='mean')
# Shows AVERAGE AGE for each Diabetes × Survived combination


# ── 🔹 Pattern: 2-Way Categorical Summary ────────────


def two_way_summary(df, row, col, value=None,
                     mode='count', normalize=None):
    "Generic 2-way summary table.
    mode='count' → uses crosstab.
    mode='mean'/'sum' → uses pivot_table on `value` column."
    if mode == 'count':
        return pd.crosstab(df[row], df[col], normalize=normalize)
    else:
        return df.pivot_table(values=value, index=row,
                              columns=col, aggfunc=mode)

# Reuse for any "X by category vs category" question
two_way_summary(df, 'Diabetes', 'Survived')               # count
two_way_summary(df, 'Diabetes', 'Survived', normalize='index') # row %
two_way_summary(df, 'Diabetes', 'Survived', value='Age', mode='mean')


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 crosstab = COUNT pairs · pivot_table = AGGREGATE values
# `normalize='index'` = row %s · `normalize='columns'` = column %s · `margins=True` = add totals

# ────────────────────────────────────────────────────────────
# 5️⃣ apply() with lambda — The Most-Used Pattern in Section C
# ────────────────────────────────────────────────────────────


# ── 🔹 Why apply() Matters ───────────────────────────
# Almost every Section C question asks you to create a new column based on existing columns.
# That's exactly what `apply()` does. Two flavours:
#   • df['col'].apply(fn) — apply to a single column
#   • df.apply(fn, axis=1) — apply across each ROW (multiple columns)

# ── 🔹 Single-Column apply ───────────────────────────


# ── Categorise a numeric column (Mar 2024 Countries paper) ──
def life_category(le):
    if   le >= 75: return 'High'
    elif le >= 60: return 'Medium'
    else:          return 'Low'

countries['life_exp_cat'] = countries['lifeExpectancy'].apply(life_category)

# ── Or with a lambda for short logic ──
df['is_adult'] = df['age'].apply(lambda x: 'Yes' if x >= 18 else 'No')


# ── 🔹 Multi-Column apply (axis=1) — CRITICAL PATTERN 


# ── Use case: family_size needs SibSp AND Parch (Nov 2023 Titanic) ──
def get_family_size(sibsp, parch):
    return sibsp + parch + 1     # +1 for the passenger

titanic['family_size'] = titanic.apply(
    lambda row: get_family_size(row['SibSp'], row['Parch']),
    axis=1                          # axis=1 means "go row by row"
)

# ── Cabin type extraction (Nov 2023) ──
titanic['Cabin_Type'] = titanic['Cabin'].apply(
    lambda x: x[0] if pd.notna(x) else 'Unknown'
)

# ── BMI from height and weight ──
df['BMI'] = df.apply(lambda r: r['weight'] / (r['height']/100)**2, axis=1)


# ── 🔹 The Universal Apply Template ──────────────────


def add_categorical_column(df, source_col, new_col, classify_fn):
    "Generic: classify values from one column into a new column."
    df[new_col] = df[source_col].apply(classify_fn)
    return df

def add_derived_column(df, new_col, derive_fn):
    "Generic: compute a new column from multiple existing columns."
    df[new_col] = df.apply(derive_fn, axis=1)
    return df

# ── Uses ──
add_categorical_column(countries, 'lifeExpectancy', 'le_cat', life_category)
add_derived_column(titanic, 'family_size',
                   lambda r: r['SibSp'] + r['Parch'] + 1)


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 apply() on Series → applies to each value · apply(axis=1) on DF → applies to each row
# axis=1 = "across columns" = "row by row" (think: row spans across columns)
# Always handle `pd.notna(x)` when source can have NaN

# ────────────────────────────────────────────────────────────
# 6️⃣ rank() — 5 Methods for Tied Values
# ────────────────────────────────────────────────────────────


# ── 🔹 All 5 Methods Side-by-Side ────────────────────


import pandas as pd
s = pd.Series([30, 10, 30, 50, 10])
# Position:    0    1    2    3    4
# Two ties: value 10 (pos 1,4) and value 30 (pos 0,2)

s.rank(method='average')   # DEFAULT
# [3.5, 1.5, 3.5, 5.0, 1.5]  ties get AVERAGE of tied positions

s.rank(method='min')
# [3.0, 1.0, 3.0, 5.0, 1.0]  ties get MINIMUM rank

s.rank(method='max')
# [4.0, 2.0, 4.0, 5.0, 2.0]  ties get MAXIMUM rank

s.rank(method='first')
# [3.0, 1.0, 4.0, 5.0, 2.0]  first occurrence gets lower rank

s.rank(method='dense')
# [2.0, 1.0, 2.0, 3.0, 1.0]  like min but NO GAPS in ranks

# Reverse order (largest=1)
s.rank(ascending=False)


# ── 🔹 Memory Aid (AMFMD) ────────────────────────────
# 🧠 A-M-F-M-D: Average · Min · First · Max · Dense
# Default = average (most common in stats)
# dense = "no gaps" (rank 1, 2, 3, 4 — never skips)
# first = "by order of appearance"

# ────────────────────────────────────────────────────────────
# 7️⃣ sort_values vs sort_index
# ────────────────────────────────────────────────────────────


# ── 🔹 Quick Reference ───────────────────────────────


df.sort_values('Salary')                 # sort by DATA in 'Salary' column
df.sort_values('Salary', ascending=False) # descending
df.sort_values(['Dept', 'Salary'])         # sort by multiple columns
df.sort_values(['Dept', 'Salary'],
               ascending=[True, False])     # Dept asc, Salary desc

df.sort_index()                       # sort by row LABELS (index)
df.sort_index(axis=1)                 # sort COLUMN names


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 sort_values = sort by DATA · sort_index = sort by LABELS

# ────────────────────────────────────────────────────────────
# 8️⃣ value_counts() and unique() — Frequency Operations
# ────────────────────────────────────────────────────────────


# ── 🔹 Examples ──────────────────────────────────────


# ── value_counts: frequency of each unique value (sorted DESC) ──
df['occupation'].value_counts()
# Tech-support    1234
# Craft-repair    1100
# Sales            980
# ...

# Top occupation (Mar 2024 Adult dataset Q4b.2)
top_occ = df['occupation'].value_counts().index[0]

# Top 5 only
df['occupation'].value_counts().head(5)

# As percentages
df['occupation'].value_counts(normalize=True) * 100

# ── unique values ──
df['continent'].unique()       # array of distinct values
df['continent'].nunique()      # count of distinct values

# ── distinct across MULTIPLE columns (Jul 2021 Q4a.3) ──
all_products = pd.concat([df['P1'], df['P2'], df['P3']]).dropna()
print(f"Distinct products: {all_products.nunique()}")


# ────────────────────────────────────────────────────────────
# 9️⃣ nlargest / nsmallest — Top-N Without Sort
# ────────────────────────────────────────────────────────────


# ── 🔹 Faster Than sort + head ───────────────────────

#
# # ── Top 10 most populated countries (Mar 2024 Q4a.2) ──
# top10 = countries.nlargest(10, 'population')
#
# # ── 10 lowest GDP per capita (where pop > 100M) ──
# big = countries[countries['population'] > 100_000_000]
# poorest = big.nsmallest(10, 'gdpPerCapita')
#
# # Equivalent (slower):
# # countries.sort_values('population', ascending=False).head(10)


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 nlargest = "give me top N" · nsmallest = "give me bottom N"
# Faster than sort_values().head(N) · Cleaner code

# ────────────────────────────────────────────────────────────
# 🔟 isin() — Filter by Multiple Values
# ────────────────────────────────────────────────────────────


# ── 🔹 Multi-Value Filtering ─────────────────────────


# ── Filter by list (Mar 2024 Adult Q4b.4) ──
high_edu = ['Bachelors', 'Prof-school', 'Assoc-acdm',
            'Assoc-voc', 'Masters', 'Doctorate']

# Rows where education is in the list
educated = df[df['education'].isin(high_edu)]

# NOT in list (using ~)
not_educated = df[~df['education'].isin(high_edu)]

# Combine with other conditions
target = df[
    (df['salary'] == '>50K') &
    (df['education'].isin(high_edu))
]


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 isin = "is value in this list?" · ~ = NOT
# Cleaner than multiple `(df.col == 'A') | (df.col == 'B') | ...`

# ────────────────────────────────────────────────────────────
# 1️⃣1️⃣ Multi-Level GroupBy + unstack()
# ────────────────────────────────────────────────────────────


# ── 🔹 Concept ───────────────────────────────────────
# Group by 2+ columns to create a hierarchical Series. Use `unstack()` to pivot the inner level into
# columns — produces a clean 2-D table.

# ── 🔹 Mar 2024 Adult Q4b.7 Pattern ──────────────────


# ── Avg hours-per-week by country AND salary ──
result = adult.groupby(['native-country', 'salary'])['hours-per-week'].mean()

# Result is a Series with multi-level index:
# native-country     salary
# Cambodia           
#                    >50K        50.0
# Canada             
#                    >50K        45.2

# ── unstack: turn inner level into columns ──
table = result.unstack('salary')
#                  50K
# native-country
# Cambodia          40.0    50.0
# Canada            38.5    45.2

# ── Top 5 countries with most hours for >50K earners ──
top5 = table['>50K'].nlargest(5)


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 groupby([col1, col2]) → multi-index · .unstack() → flatten to table
# stack() = opposite (wide → long) · Use for ANY "by X and Y" question

# ────────────────────────────────────────────────────────────
# 🧩 REUSABLE PATTERNS — Section C Survival Kit
# ────────────────────────────────────────────────────────────


# ── 📋 Pattern 1: Filter-and-Aggregate ───────────────


# Use for: "Among rows matching condition X, find avg/max/min Y"
def filter_and_aggregate(df, condition, value_col, agg='mean'):
    filtered = df[condition]
    return filtered[value_col].agg(agg)

# Examples:
# Mar 2024: avg pop where life_exp > 75
# Nov 2023: avg hardness where TDS > 500
# Mar 2024: avg Ureview where consecutive_usage > 4


# ── 📋 Pattern 2: Add Categorical Column from Numeric 


def categorise_numeric(value, bins, labels):
    "Classify a numeric value into named bin."
    for i, threshold in enumerate(bins):
        if value return labels[i]
    return labels[-1]

df['category'] = df['numeric_col'].apply(
    lambda x: categorise_numeric(x, [100, 200], ['Low','Mid','High'])
)


# ── 📋 Pattern 3: Survival/Success Rate per Group ────


def success_rate_per_group(df, group_col, target_col, success_value):
    "Compute success rate for each group.
    Useful for: survival rate per port/cabin, %>50K per education, etc."
    return df.groupby(group_col)[target_col].apply(
        lambda s: (s == success_value).mean()
    )

# Or simpler when target is already 0/1:
df.groupby('Embarked')['Survived'].mean()


# ── 📋 Pattern 4: Multi-Aggregate Summary (Named) ────


def summary_table(df, group_by_col):
    return df.groupby(group_by_col).agg(
        Count    = ('id',    'count'),
        Avg_Age  = ('age',   'mean'),
        Med_Fare = ('fare',  'median'),
        Max_Sal  = ('salary', 'max')
    ).round(2)


# ── 📋 Pattern 5: 2-Way Cross with Percentages ───────


# For "what % of X are Y" questions
pct_table = pd.crosstab(df['gender'], df['survived'],
                        normalize='index') * 100
# Each row sums to 100% — interpretation: "of all males, X% survived"


# ────────────────────────────────────────────────────────────
# 📌 ULTIMATE PANDAS ADVANCED CHEATSHEET
# ────────────────────────────────────────────────────────────


# ━━━ 🎯 GroupBy Quick Reference ━━━━━━━━━━━━━━━━━━━━━━━━━━━


df.groupby('col')['val'].mean()
df.groupby(['a','b'])['val'].sum()
df.groupby('col').agg(['mean','min','max'])
df.groupby('col').agg(
    Avg = ('val', 'mean'),
    Cnt = ('val', 'count')
)
df.groupby('col')['val'].apply(custom_fn)


# ━━━ 🔗 Combine Quick Reference ━━━━━━━━━━━━━━━━━━━━━━━━━━━


pd.concat([df1,df2])              # rows
pd.concat([df1,df2], axis=1)      # cols
pd.merge(df1, df2, on='id')
pd.merge(df1, df2, on='id',
         how='inner|left|right|outer')
df1.join(df2)                     # on index


# ━━━ 🔄 Pivot/Crosstab ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


pd.crosstab(df.A, df.B)
pd.crosstab(df.A, df.B,
            normalize='index')
pd.crosstab(df.A, df.B, margins=True)
df.pivot_table(values='V',
               index='A', columns='B',
               aggfunc='mean')


# ━━━ ⚡ Apply Patterns ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


df['col'].apply(fn)              # 1 col
df.apply(fn, axis=1)               # row
df['col'].apply(lambda x:
    'A' if x>=10 else 'B')
df.apply(lambda r: r.A+r.B, axis=1)


# ━━━ 📊 Top-N / Filter ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


df.nlargest(10, 'col')
df.nsmallest(5, 'col')
df[df['col'].isin(['A','B'])]
df[~df['col'].isin(['A'])]   # NOT
df['col'].value_counts()
df['col'].value_counts(normalize=True)


# ━━━ 📈 Multi-Level Tricks ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


g = df.groupby(['A','B'])['V'].mean()
g.unstack('B')            # inner→cols
g.unstack(level=-1)
df.set_index(['A','B'])
df.reset_index()        # flatten


# ────────────────────────────────────────────────────────────
# 🧠 MEMORY AIDS — Pandas Advanced
# ────────────────────────────────────────────────────────────

#   • groupby = SAC: Split → Apply → Combine
#   • concat / merge / join: stack / SQL-on-column / on-index
#   • crosstab vs pivot_table: COUNT pairs vs AGGREGATE values
#   • apply axis=1: "across columns" = "row by row"
#   • rank methods (AMFMD): Average · Min · First · Max · Dense
#   • sort_values / sort_index: by DATA / by LABELS
#   • isin() + ~ = filter in / not-in a list
#   • nlargest / nsmallest = fast top-N/bottom-N
#   • unstack turns inner index → columns
#   • normalize='index' → row %s · 'columns' → col %s
# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ╔════════════════════════════════════════════════════════════╗
# ║  FILE 11 — Visualization                                   ║
# ╚════════════════════════════════════════════════════════════╝


# ━━━ 📋 TABLE OF CONTENTS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • 🎯 Plot Decision Map
#   • 1. Histogram (distribution)
#   • 2. Boxplot (compare distributions)
#   • 3. Scatter + Regplot (correlation)
#   • 4. Bar / Countplot (categories)
#   • 5. Pie chart (proportions)
#   • 6. Line plot (trend over time)
#   • 7. Violin plot (shape + box)
#   • 8. Heatmap (correlation matrix)
#   • 9. axhline / axvline / annotations
#   • 🧩 Reusable Templates
#   • 📌 Cheatsheet

# ────────────────────────────────────────────────────────────
# 🎯 Plot Decision Map — From Question Keyword to Plot Type
# ────────────────────────────────────────────────────────────


# [Keyword in Question]  [Plot Type]  [Method]
# "distribution of", "spread" |  Histogram + KDE |  sns.histplot(x, bins=30, kde=True) |
# "compare distributions", "across categories" |  Boxplot |  sns.boxplot(data=df, x='cat', y='val') |
# "relationship", "correlation" (2 numeric) |  Scatter + regplot |  sns.regplot(data=df, x='A', y='B') |
# "correlation matrix" |  Heatmap |  sns.heatmap(df.corr(), annot=True, cmap='coolwarm') |
# "count of", "frequency" |  Countplot / bar |  sns.countplot(data=df, x='col') |
# "proportion", "percentage" (few categories) |  Pie |  df['col'].value_counts().plot(kind='pie', autopct='%1.1f%%') |
# "over time", "trend" |  Line plot |  plt.plot(x, y) or df.plot(kind='line') |
# "distribution + median" |  Violin plot |  sns.violinplot(data=df, x='cat', y='val') |


# ────────────────────────────────────────────────────────────
# 1️⃣ Histogram — Distribution of a Single Numeric Column
# ────────────────────────────────────────────────────────────


# ── 🔹 What & When ───────────────────────────────────
# Shows how values of ONE numeric column are spread. X-axis = value bins; Y-axis = frequency.
# Used for : age distribution, fare distribution, hardness levels, BP/cholesterol patterns.

# ── 🔹 Three Ways to Plot ────────────────────────────


import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. matplotlib basic ──
plt.hist(df['age'], bins=30, color='steelblue', edgecolor='white')
plt.title('Age Distribution')
plt.xlabel('Age'); plt.ylabel('Frequency')
plt.show()

# ── 2. seaborn (BEST: includes KDE smooth curve) ──
sns.histplot(df['age'], bins=30, kde=True, color='steelblue')
plt.title('Age Distribution'); plt.show()

# ── 3. pandas one-liner ──
df['age'].plot(kind='hist', bins=30)

# ── Bonus: add mean line (Jul 2021 distribution paper) ──
sns.histplot(df['avg_rating'], bins=30, kde=True)
plt.axvline(df['avg_rating'].mean(), color='red', linestyle='--',
            label=f'Mean={df["avg_rating"].mean():.2f}')
plt.legend(); plt.show()


# ── 🔹 Reusable Template ─────────────────────────────


def plot_distribution(df, col, bins=30, title=None):
    "Plot histogram with KDE and mean reference line."
    plt.figure(figsize=(9, 5))
    sns.histplot(df[col], bins=bins, kde=True, color='steelblue')
    plt.axvline(df[col].mean(), color='red', linestyle='--',
                label=f'Mean={df[col].mean():.2f}')
    plt.title(title or f'Distribution of {col}')
    plt.xlabel(col); plt.ylabel('Frequency')
    plt.legend(); plt.tight_layout(); plt.show()

# Reuse for ANY "show distribution of X" question
plot_distribution(titanic, 'Age')
plot_distribution(adult, 'hours-per-week')
plot_distribution(water, 'Hardness', bins=20)


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 histplot(bins=30, kde=True) — bins of 20-30 are standard. KDE adds a smooth bell curve.
# Used in: Jul 2021 Q4b.5 , Aug 2021 Covid Q4 (BP, cholesterol)

# ────────────────────────────────────────────────────────────
# 2️⃣ Boxplot — Compare Distributions Across Categories
# ────────────────────────────────────────────────────────────


# ── 🔹 Boxplot Anatomy ───────────────────────────────
#   • Box: middle 50% of data (Q1 to Q3)
#   • Line in box: median (50th percentile)
#   • Whiskers: extend to non-outlier min/max
#   • Dots beyond whiskers: outliers
# Best for : comparing how a numeric column varies across groups (e.g., salary by department).

# ── 🔹 Code Examples ─────────────────────────────────


# ── Two columns side-by-side (Jul 2021 Q4a.4) ──
df[['Web_review', 'Exp_review']].boxplot()
plt.title('Web vs Experience Reviews'); plt.show()

# ── Numeric column grouped by category (Mar 2024 Countries Q4a.6) ──
sns.boxplot(data=countries, x='continent', y='population', palette='Set2')
plt.xticks(rotation=30)   # rotate long category labels
plt.title('Population by Continent'); plt.show()

# ── With hue (3-way comparison) ──
sns.boxplot(data=titanic, x='Sex', y='Age', hue='Survived')


# ── 🔹 Template ──────────────────────────────────────


def plot_box_by_group(df, group_col, value_col, rotate=30):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=group_col, y=value_col, palette='Set2')
    plt.xticks(rotation=rotate)
    plt.title(f'{value_col} by {group_col}')
    plt.tight_layout(); plt.show()

plot_box_by_group(adult, 'occupation', 'hours-per-week')


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 Boxplot = "5-number summary in a picture" : min, Q1, median, Q3, max + outliers

# ────────────────────────────────────────────────────────────
# 3️⃣ Scatter + Regplot — Show Relationships Between 2 Numeric Variables
# ────────────────────────────────────────────────────────────


# ── 🔹 Code ──────────────────────────────────────────


# ── Basic scatter ──
plt.scatter(df['Age'], df['Fare'], alpha=0.5)
plt.xlabel('Age'); plt.ylabel('Fare')
plt.title('Age vs Fare'); plt.show()

# ── Seaborn scatter with category coloring ──
sns.scatterplot(data=titanic, x='Age', y='Fare', hue='Survived')

# ── regplot: scatter + regression line ──
sns.regplot(data=df, x='Age', y='Fare', scatter_kws={'alpha':0.5})
plt.title('Age vs Fare with Trendline'); plt.show()

# ── lmplot: regplot with category facets ──
sns.lmplot(data=titanic, x='Age', y='Fare', hue='Sex', height=5)


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 Scatter = "are these two numerics related?" · regplot adds the trend line for you
# `alpha=0.5` useful for dense overlapping points (transparency)

# ────────────────────────────────────────────────────────────
# 4️⃣ Bar Plot / Countplot — Compare Categories
# ────────────────────────────────────────────────────────────


# ── 🔹 Code ──────────────────────────────────────────


# ── countplot: counts of each category (Jul 2021 Q4b.4) ──
sns.countplot(data=df, x='assigned_rating', palette='viridis',
              order=sorted(df['assigned_rating'].unique()))
plt.title('Count of each Rating'); plt.show()

# ── horizontal bar (long category names) ──
df['occupation'].value_counts().plot(kind='barh', color='#58a6ff')
plt.title('Occupation Counts'); plt.show()

# ── Grouped bar (compare values per category) ──
group_data = df.groupby('Embarked')['Survived'].mean()
group_data.plot(kind='bar', color=['#5ccfe6','#3fb950','#f0883e'])
plt.title('Survival Rate by Port'); plt.show()


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 countplot = automatic counting · bar = you provide values
# Use `order=sorted(df.col.unique())` for consistent x-axis ordering

# ────────────────────────────────────────────────────────────
# 5️⃣ Pie Chart — Proportions of Few Categories
# ────────────────────────────────────────────────────────────


# ── 🔹 Code ──────────────────────────────────────────


# ── Pie of value counts (Jul 2021 Q4b.1: most-used metric) ──
counts = df['assigned_metric'].value_counts()

plt.figure(figsize=(7, 7))
counts.plot(
    kind='pie',
    autopct='%1.1f%%',        # show percentage on each slice
    startangle=90,             # start from top
    colors=sns.color_palette('Set2', len(counts))
)
plt.title('Distribution of Metrics')
plt.ylabel('')                   # hide default ylabel
plt.tight_layout(); plt.show()


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 Use pie only for ≤6 categories. More than that → use a bar plot for readability.
# `autopct='%1.1f%%'` = show "12.5%" labels on each slice

# ────────────────────────────────────────────────────────────
# 6️⃣ Line Plot — Trend Over Time / Ordered Index
# ────────────────────────────────────────────────────────────


# ── 🔹 Code ──────────────────────────────────────────


# ── Basic line ──
plt.plot(years, sales, marker='o', color='steelblue')
plt.title('Annual Sales'); plt.xlabel('Year'); plt.ylabel('Sales')
plt.grid(True, alpha=0.3); plt.show()

# ── Multiple lines ──
plt.plot(years, sales_a, label='Product A', marker='o')
plt.plot(years, sales_b, label='Product B', marker='s')
plt.legend(); plt.show()

# ── Pandas one-liner ──
df.set_index('date')['value'].plot(figsize=(10,5))


# ────────────────────────────────────────────────────────────
# 7️⃣ Violin Plot — Box + Distribution Shape
# ────────────────────────────────────────────────────────────


# ── 🔹 What is It? ───────────────────────────────────
# Combines boxplot (median, quartiles) with KDE (distribution shape) on each side. Best when you want
# to see both central tendency AND distribution shape in one plot.

# ── 🔹 Code ──────────────────────────────────────────


# ── Violin per category ──
sns.violinplot(data=titanic, x='Pclass', y='Age', palette='Set3')
plt.title('Age Distribution by Class'); plt.show()

# ── Split violin (compare groups within categories) ──
sns.violinplot(data=titanic, x='Pclass', y='Age',
               hue='Survived', split=True)


# ────────────────────────────────────────────────────────────
# 8️⃣ Heatmap — Correlation Matrix
# ────────────────────────────────────────────────────────────


# ── 🔹 What & When ───────────────────────────────────
# Shows correlation values (between -1 and +1) for every pair of numeric columns as a coloured grid.
#   • +1 = perfect positive correlation (red)
#   • 0 = no correlation (white)
#   • -1 = perfect negative correlation (blue)
# Used in : Jul 2021 Q4b.3 (Web rating dataset), almost every dataset paper

# ── 🔹 The Heatmap Recipe (Memorise) ─────────────────


import seaborn as sns

# ── Step 1: Compute correlation matrix ──
cols = ['Ucredit', 'Ureview', 'Web_review',
        'consecutive_usage', 'Exp_review']
corr_matrix = df[cols].corr()

# ── Step 2: Plot heatmap ──
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    annot=True,         # show numbers in cells
    fmt=".2f",          # 2 decimal places
    cmap="coolwarm",    # red = positive, blue = negative
    vmin=-1, vmax=1,    # lock scale to full range
    linewidths=0.5,    # cell separators
    square=True          # square cells
)
plt.title('Correlation Heatmap')
plt.tight_layout(); plt.show()


# ── 🔹 Reusable Template ─────────────────────────────


def plot_corr_heatmap(df, cols=None, title='Correlation Heatmap'):
    "Plot correlation heatmap. If cols=None, uses all numeric columns."
    if cols is None:
        cols = df.select_dtypes(include=['number']).columns.tolist()
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[cols].corr(), annot=True, fmt='.2f',
                cmap='coolwarm', vmin=-1, vmax=1, square=True)
    plt.title(title); plt.tight_layout(); plt.show()

plot_corr_heatmap(titanic, ['Age','Fare','SibSp','Parch','Survived'])


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 HEATMAP RECIPE: corr() → heatmap(annot=True, cmap='coolwarm')
# Always use `annot=True` and `cmap='coolwarm'` — the gold standard

# ────────────────────────────────────────────────────────────
# 9️⃣ Plot Extras — axhline, axvline, annotations, save
# ────────────────────────────────────────────────────────────


# ── 🔹 Reference Lines & Annotations ─────────────────


# ── Horizontal/vertical reference lines ──
plt.axhline(y=50, color='red', linestyle='--', label='Threshold')
plt.axvline(x=df['col'].mean(), color='green',
            linestyle='-.', label='Mean')

# ── Annotations on points ──
plt.annotate('Outlier!',
             xy=(10, 95),                  # point to annotate
             xytext=(12, 90),               # text position
             arrowprops=dict(arrowstyle='->'))

# ── Save figure ──
plt.savefig('plot.png', dpi=150, bbox_inches='tight')

# ── Multiple subplots ──
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].hist(df['A'], bins=20); axes[0].set_title('A')
axes[1].hist(df['B'], bins=20); axes[1].set_title('B')
plt.tight_layout(); plt.show()


# ────────────────────────────────────────────────────────────
# 🧩 ALL-IN-ONE PLOT TEMPLATES — Copy-Paste Ready
# ────────────────────────────────────────────────────────────


# ── 📋 Universal Plot Helper ─────────────────────────


import matplotlib.pyplot as plt
import seaborn as sns

def quick_plot(df, kind, x=None, y=None, hue=None, title=''):
    "One-call wrapper for the 6 most common plot types."
    plt.figure(figsize=(10, 6))

    if   kind == 'hist':    sns.histplot(df[x], bins=30, kde=True)
    elif kind == 'box':     sns.boxplot(data=df, x=x, y=y, hue=hue)
    elif kind == 'scatter': sns.scatterplot(data=df, x=x, y=y, hue=hue)
    elif kind == 'count':   sns.countplot(data=df, x=x, hue=hue)
    elif kind == 'bar':     sns.barplot(data=df, x=x, y=y, hue=hue)
    elif kind == 'violin':  sns.violinplot(data=df, x=x, y=y, hue=hue)

    plt.title(title); plt.xticks(rotation=30)
    plt.tight_layout(); plt.show()

# Usage
quick_plot(titanic, 'hist', x='Age', title='Age Distribution')
quick_plot(adult,   'box',  x='occupation', y='hours-per-week')
quick_plot(titanic, 'count', x='Embarked', hue='Survived')


# ── 📋 Plot Saver Helper ─────────────────────────────


def save_current_plot(filename, dpi=150):
    plt.savefig(filename, dpi=dpi, bbox_inches='tight')
    plt.close()
    print(f'Saved {filename}')


# ────────────────────────────────────────────────────────────
# 📌 VISUALIZATION CHEATSHEET
# ────────────────────────────────────────────────────────────


# ━━━ 📊 Standard Imports ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style('whitegrid')   # nicer default
plt.rcParams['figure.figsize'] = (10,6)


# ━━━ 🎨 Color Palettes ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


sns.color_palette('viridis', n=5)
sns.color_palette('Set2')
# Built-in: Set1, Set2, Set3, viridis,
# coolwarm, magma, plasma, husl

# Heatmap: cmap='coolwarm' (always)


# ━━━ ⚡ Always-Add Lines ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


plt.title('...')
plt.xlabel('...'); plt.ylabel('...')
plt.xticks(rotation=30)   # long labels
plt.legend()                # if multiple series
plt.tight_layout()          # avoid clipping
plt.show()


# ━━━ 🔄 Plot Decision Quick ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#
# # 1 numeric → histplot
# # 1 numeric × 1 cat → boxplot
# # 2 numeric → regplot
# # 2 cat → crosstab → heatmap
# # 1 cat counts → countplot
# # proportions (≤6) → pie
# # corr matrix → heatmap
# # time series → line


# ━━━ 🌡️ Heatmap Recipe ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


sns.heatmap(
    df[cols].corr(),
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    vmin=-1, vmax=1,
    linewidths=0.5,
    square=True
)


# ━━━ 📌 Reference Lines ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


plt.axhline(y=0, color='r',
            linestyle='--')
plt.axvline(x=df['c'].mean(),
            color='g')

# Useful for showing means/medians/
# thresholds on histograms

# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ╔════════════════════════════════════════════════════════════╗
# ║  FILE 12 — Coding Patterns                                 ║
# ╚════════════════════════════════════════════════════════════╝


# ━━━ 📋 15 PATTERNS — Click to Jump ━━━━━━━━━━━━━━━━━━━━━━━
#   • P1: Validation with Multiple Rules
#   • P2: Billing / Invoice with GST
#   • P3: Greedy — Sort by Ratio
#   • P4: Word / Element Frequency
#   • P5: Tier Classification (Grade-Like)
#   • P6: Date Validation with Dict
#   • P7: Cycle Detection (Set-Based)
#   • P8: Conditional Sequence (Collatz)
#   • P9: Mapping/Lookup Table
#   • P10: Multi-Criterion Scoring
#   • P11: STOP-Loop with Accumulator
#   • P12: Sequence Generator (Fibonacci-Like)
#   • P13: Knapsack/Optimisation
#   • P14: Prime Check (sqrt+1)
#   • P15: Longest Consecutive (Set O(n))
#   • 🎯 Pattern Decision Tree

# ────────────────────────────────────────────────────────────
# P1 · Validation with Multiple Rules
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Check if input is valid against rules X, Y, Z" — return True/False (or 'true'/'false').
# Examples : Username (Mar 2024 Scan, Nov 2023), Password rules, Email validation.

# ── 🔹 Template ──────────────────────────────────────


def validate(s):
    "Check input against multiple rules. Return True/False."
    # Rule 1: length
    if len(s) 4 or len(s) > 25:
        return False

    # Rule 2: must start with letter
    if not s[0].isalpha():
        return False

    # Rule 3: only allowed chars
    for ch in s:
        if not (ch.isalnum() or ch == '_'):
            return False

    # Rule 4: cannot end with underscore
    if s[-1] == '_':
        return False

    return True

# Tests
print(validate('alice_123'))   # True
print(validate('1alice'))      # False (starts with digit)
print(validate('alice_'))      # False (ends with _)


# ── 🔹 Reuse Notes ───────────────────────────────────
# Change the rules — same skeleton handles email, phone, password, ID validation.
# Pattern : check rules in order, return False at first failure, return True at end.

# ────────────────────────────────────────────────────────────
# P2 · Billing / Invoice with GST or Discount
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Calculate a bill given prices and quantities; add tax/discount; print formatted bill."
# Examples : Computer Assembly (Jul 2021), Bookstore (Feb 2025), Superstore (Mar 2024 Scan).

# ── 🔹 Template (nested dict for catalogue) ──────────


def generate_bill(catalogue, selections, tax_rate=0.12, fixed_charges=0):
    "Generate a bill with subtotal, tax, and total.
    catalogue : {item: {type: price}}
    selections: {item: type}"

    line_items = []
    subtotal = 0

    for item, choice in selections.items():
        price = catalogue[item][choice]
        line_items.append((item, choice, price))
        subtotal += price

    subtotal += fixed_charges
    tax     = subtotal * tax_rate
    total   = subtotal + tax

    # Print formatted bill
    print('=' * 40)
    print(f"{'Item':10}")
    print('-' * 40)
    for item, choice, price in line_items:
        print(f"{item+' '+choice:10}")
    if fixed_charges:
        print(f"{'Other':10}")
    print(f"{'Tax':10.2f}")
    print('-' * 40)
    print(f"{'TOTAL':10.2f}")
    return total

# Example: Computer Assembly Bill (Jul 2021)
catalogue = {
    'HDD'      : {'1TB': 5000,    '2TB': 7500},
    'RAM'      : {'8GB': 4000,    '16GB': 6000},
    'Processor': {'I5': 15000,    'I7': 18000}
}
selections = {'HDD': '1TB', 'RAM': '16GB', 'Processor': 'I5'}
generate_bill(catalogue, selections, tax_rate=0.12, fixed_charges=4000)


# ────────────────────────────────────────────────────────────
# P3 · Greedy Algorithm — Sort by Ratio/Value
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Maximise/minimise something subject to a constraint, by always picking the best item next."
# Examples : Job Fair (Aug 2021), Fractional Knapsack (Jul 2021, Model Set), Activity Selection.

# ── 🔹 Template ──────────────────────────────────────


def greedy_select(items, key_fn, capacity, weight_fn, value_fn):
    "Generic fractional greedy selector.
    items: list of items
    key_fn(i): score to sort by, e.g. value/weight
    capacity: total capacity
    weight_fn(i), value_fn(i): item weight and value"

    # Step 1: Sort items by key (descending)
    sorted_items = sorted(items, key=key_fn, reverse=True)

    # Step 2: Greedy fill
    portions     = []
    total_value  = 0
    remaining    = capacity

    for item in sorted_items:
        w = weight_fn(item)
        v = value_fn(item)
        if remaining 0:
            portions.append((item, 0))
            continue
        if w 1))
            total_value += v
            remaining   -= w
        else:
            frac = remaining / w
            portions.append((item, frac))
            total_value += v * frac
            remaining = 0

    return portions, total_value

# Example: Fractional Knapsack (Jul 2021)
profit = [1, 2, 3, 4]
weight = [6, 3, 8, 10]
items  = list(range(len(profit)))

portions, total = greedy_select(
    items,
    key_fn    = lambda i: profit[i] / weight[i],   # profit/weight ratio
    capacity  = 15,
    weight_fn = lambda i: weight[i],
    value_fn  = lambda i: profit[i]
)
# Output: portions sorted, total profit = 8.625


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 Greedy = "Best bang per kg first" : Sort by ratio DESC → take fully if fits → take fraction →
# stop when full

# ────────────────────────────────────────────────────────────
# P4 · Word / Element Frequency Counter
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Count how many times each X appears in Y." Examples : word count (May 2025),
# product purchase frequency (Jul 2021), top occupation (Mar 2024 Scan), element occurrences.

# ── 🔹 Template ──────────────────────────────────────


from collections import Counter

def count_frequencies(items, top_n=None):
    "Count occurrences. Returns {item: count} sorted desc.
    If top_n given, returns only top N items."
    counts = Counter(items)
    if top_n:
        return dict(counts.most_common(top_n))
    return dict(counts)

# Word frequency from a sentence (May 2025)
text = "the quick brown fox jumps over the lazy dog the fox is quick"
words = text.lower().split()
freq = count_frequencies(words)
print(freq)   # {'the': 3, 'quick': 2, 'fox': 2, ...}

# Most common 5
print(count_frequencies(words, top_n=5))

# Manual version (without Counter)
def count_manual(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


# ────────────────────────────────────────────────────────────
# P5 · Tier Classification (Grade-Like Buckets)
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Classify a numeric value into a named tier (Grade A/B/C, Low/Medium/High, etc.)."
# Examples : Grades (Mar 2024 Scan), Hardness category (Nov 2023),
# Life expectancy (Mar 2024 Scan), Tall/Short (Mar 2024 PDF Olympics).

# ── 🔹 Template ──────────────────────────────────────


def classify_tier(value, thresholds, labels):
    "Classify value into a tier.
    thresholds: sorted ascending [t1, t2, t3]
    labels    : [label_below_t1, label_below_t2, ..., label_above_last]
    len(labels) must be len(thresholds)+1"
    for i, t in enumerate(thresholds):
        if value return labels[i]
    return labels[-1]

# Example: Grade classifier (Mar 2024 Scan)
def grade(score):
    return classify_tier(score,
                          thresholds=[60, 70, 80, 90],
                          labels    =['F', 'D', 'C', 'B', 'A'])

#   
#   60-69 → D
#   70-79 → C
#   80-89 → B
#   >=90 → A

# Example: Hardness category (Nov 2023)
hardness_cat = lambda h: classify_tier(h, [100, 200], ['Low', 'Moderate', 'High'])

# Use with pandas apply
df['category'] = df['value_col'].apply(lambda x: classify_tier(x, [10,20,30],
                                                              ['A','B','C','D']))


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 n thresholds → n+1 labels . Sort thresholds ascending. Walk through and return at first match.

# ────────────────────────────────────────────────────────────
# P6 · Date Validation with Dictionary
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Validate a date — check month is real and day is within month limit."
# Used in : Mar 2024 Scan Q3c (calendar validation).

# ── 🔹 Template ──────────────────────────────────────


def validate_date(month, day, leap=False):
    "Check if a (month, day) combo is real."
    days_per_month = {
        'January': 31, 'February': 29 if leap else 28,
        'March': 31,   'April': 30,
        'May': 31,     'June': 30,
        'July': 31,    'August': 31,
        'September': 30, 'October': 31,
        'November': 30,  'December': 31
    }
    if month not in days_per_month:
        return False, f"'{month}' is not a valid month."
    max_d = days_per_month[month]
    if day 1 or day > max_d:
        return False, f"{month} only has {max_d} days."
    return True, f"{month} {day} is valid."

print(validate_date('February', 30))   # False, "February only has 28 days"
print(validate_date('January', 31))    # True, "January 31 is valid."


# ────────────────────────────────────────────────────────────
# P7 · Cycle Detection with Set
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Sequence may loop forever — detect when we revisit a value."
# Used in : Happy Number (Mar 2024 Scan), can also apply to graph traversal, function-iteration loops.

# ── 🔹 Template ──────────────────────────────────────


def runs_to_target(start, next_fn, target, max_iter=10000):
    "Iterate next_fn until we reach target or repeat (cycle).
    Returns True if reaches target, False if cycle detected."
    seen = set()
    n = start
    while n != target:
        if n in seen or len(seen) > max_iter:
            return False     # cycle / runaway
        seen.add(n)
        n = next_fn(n)
    return True

# Example: Happy Number
def digit_sq_sum(n):
    return sum(int(d)**2 for d in str(n))

def is_happy(n):
    return runs_to_target(n, digit_sq_sum, 1)

print(is_happy(19))     # True  (19→82→68→100→1)
print(is_happy(4))      # False (cycle: 4→16→37→58→89→145→42→20→4)


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 Sets → O(1) membership check → perfect for cycle detection . Lists would be O(n) per check.

# ────────────────────────────────────────────────────────────
# P8 · Conditional Sequence (Collatz-Style)
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Generate a sequence where the next value depends on a condition on the current value."
# Used in : Collatz Conjecture (Nov 2023), can apply to many recursive sequences.

# ── 🔹 Template ──────────────────────────────────────


def generate_sequence(start, next_fn, stop_value=1, max_terms=30):
    "Build a sequence using next_fn until stop_value or max_terms."
    seq = [start]
    n = start
    while n != stop_value and len(seq) return seq

# Example: Collatz (Nov 2023)
def collatz_step(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

seq = generate_sequence(6, collatz_step)
print(' '.join(map(str, seq)))
# 6 3 10 5 16 8 4 2 1


# ────────────────────────────────────────────────────────────
# P9 · Mapping/Lookup Table (Telephone Keypad)
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Translate or match items between two systems via a mapping."
# Used in : Telephone keypad (Nov 2023), morse code, encoding/decoding tasks.

# ── 🔹 Template ──────────────────────────────────────


def match_via_mapping(seq1, seq2, mapping):
    "Check if every (a, b) in zip(seq1, seq2) satisfies mapping[a]∋b."
    if len(seq1) != len(seq2):
        return False
    for a, b in zip(seq1, seq2):
        if a not in mapping or b not in mapping[a]:
            return False
    return True

# Example: telephone match (Nov 2023)
KEYPAD = {'2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL',
          '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}

def telephone_match(num, s):
    return match_via_mapping(num, s.upper(), KEYPAD)

print(telephone_match('22426', 'CABIN'))    # True
print(telephone_match('22426', 'ABCDE'))    # False (E not in keypad[6]='MNO')


# ────────────────────────────────────────────────────────────
# P10 · Multi-Criterion Scoring (Password Strength)
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Score input based on multiple criteria, then classify by total score."
# Used in : Password strength (Nov 2023), profile completeness, quality scoring.

# ── 🔹 Template ──────────────────────────────────────


def multi_criterion_score(value, criteria, classifier):
    "Score value against criteria.
    criteria  : list of (check_fn, points_if_passes)
    classifier: function (score → label)"
    score = 0
    feedback = []
    for check_fn, points, name in criteria:
        if check_fn(value):
            score += points
            feedback.append(f'✅ {name}')
        else:
            feedback.append(f'❌ {name}')
    return score, classifier(score), feedback

# Example: Password strength
import re
PWD_CRITERIA = [
    (lambda p: len(p) >= 8,                          2, 'Length >= 8'),
    (lambda p: any(c.isupper() for c in p),         2, 'Has uppercase'),
    (lambda p: any(c.islower() for c in p),         2, 'Has lowercase'),
    (lambda p: any(c.isdigit() for c in p),         2, 'Has digit'),
    (lambda p: bool(re.search(r'[!@#$%]', p)),       2, 'Has special char')
]

def classify_pwd(s):
    if s >= 9: return 'VERY STRONG'
    if s >= 7: return 'STRONG'
    if s >= 4: return 'MEDIUM'
    return 'WEAK'

score, label, fb = multi_criterion_score('Hello@123', PWD_CRITERIA, classify_pwd)
print(f'Score: {score}/10, Strength: {label}')


# ────────────────────────────────────────────────────────────
# P11 · STOP-Loop with Accumulator
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Repeatedly ask user for input until they type STOP, accumulate values, print totals."
# Used in : Bookstore billing (Feb 2025), Superstore (Mar 2024 Scan), interactive billing systems.

# ── 🔹 Template ──────────────────────────────────────


def stop_loop_collect(prompt, parse_fn, stop_word='STOP'):
    "Repeatedly read input, parse, and collect items.
    Stops when user types stop_word."
    items = []
    while True:
        entry = input(prompt).strip()
        if entry.upper() == stop_word:
            break
        try:
            items.append(parse_fn(entry))
        except Exception as e:
            print(f'  Invalid input: {e}')
    return items

# Example: Superstore — read "qty category" until STOP
def parse_qty_category(s):
    parts = s.split()
    return int(parts[0]), parts[1].upper()

orders = stop_loop_collect(
    "Enter qty category (or STOP): ",
    parse_qty_category
)
print(f'You entered {len(orders)} orders')


# ────────────────────────────────────────────────────────────
# P12 · Sequence Generator (Fibonacci, Triangular, …)
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Generate the first N terms of a number sequence." Used in : Fibonacci (Mar 2024 PDF),
# Triangular numbers (Jul 2021), prime sequences, geometric progressions.

# ── 🔹 Template ──────────────────────────────────────


def generate_n_terms(n, term_fn):
    "Generate sequence using term_fn(i) for i = 0 to n-1."
    return [term_fn(i) for i in range(n)]

# Example 1: Triangular numbers (Jul 2021)
triangular = generate_n_terms(11, lambda i: i * (i + 1) // 2)
# [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

# Example 2: Fibonacci (Mar 2024 PDF)
def fib(i):
    a, b = 0, 1
    for _ in range(i): a, b = b, a + b
    return a

fibs = generate_n_terms(10, fib)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Example 3: Squares
squares = generate_n_terms(5, lambda i: i**2)
# [0, 1, 4, 9, 16]

# Bonus: Sum of terms in a range [k, l]
def sum_range(seq, k, l):
    return sum(seq[k : l + 1])


# ────────────────────────────────────────────────────────────
# P13 · Knapsack / Optimisation (specific case of P3)
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Given items with weights and values, maximise value within a weight limit."
# Used in : Jul 2021 Q3b, Model Set Q3 (Farmer's Fractional Knapsack).

# ── 🔹 Standalone Template ───────────────────────────


def fractional_knapsack(profit, weight, capacity):
    "Solve fractional knapsack. Return (portions_in_original_order, total_profit)."
    n = len(profit)
    # Sort indices by profit/weight ratio DESC
    indices = sorted(range(n),
                      key=lambda i: profit[i] / weight[i],
                      reverse=True)

    portions     = [0] * n
    total        = 0
    remaining    = capacity

    for i in indices:
        if remaining 0: break
        if weight[i] 1
            total       += profit[i]
            remaining   -= weight[i]
        else:
            frac        = remaining / weight[i]
            portions[i] = frac
            total       += profit[i] * frac
            remaining   = 0

    return portions, round(total, 3)

# Jul 2021 sample
print(fractional_knapsack([1,2,3,4], [6,3,8,10], 15))
# ([0, 1, 0.875, 1], 8.625)


# ────────────────────────────────────────────────────────────
# P14 · Prime Check + Prime List (sqrt+1 trick)
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Find primes / palindrome primes / count primes in a range."
# Used in : Prime palindromes (May 2025), prime filter (Oct 2024).

# ── 🔹 Template ──────────────────────────────────────


def is_prime(n):
    "Return True if n is prime."
    if n 2:                return False
    if n == 2:               return True
    if n % 2 == 0:           return False
    for i in range(3, int(n**0.5) + 1, 2):   # step by 2 (odds only)
        if n % i == 0:        return False
    return True

def primes_in_range(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def prime_palindromes(start, end):
    return [n for n in primes_in_range(start, end) if is_palindrome(n)]


# ── 🔹 Memory Aid ────────────────────────────────────
# 🧠 Why sqrt+1? If n=ab and a≤b, then a≤√n. So we only need to test factors up to √n.

# ────────────────────────────────────────────────────────────
# P15 · Longest Consecutive Sequence (Set O(n))
# ────────────────────────────────────────────────────────────


# ── 🔹 When to use ───────────────────────────────────
# "Find the longest run of consecutive integers in an unsorted list."
# Used in : Oct 2024 Q3b. Naive sort = O(n log n); set-based = O(n).

# ── 🔹 Template ──────────────────────────────────────


def longest_consecutive(nums):
    "Return length of longest run of consecutive integers."
    num_set = set(nums)
    longest = 0

    for n in num_set:
        # Only start counting from sequence beginnings
        if (n - 1) not in num_set:
            current = n
            length  = 1
            while (current + 1) in num_set:
                current += 1
                length  += 1
            longest = max(longest, length)

    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))   # 4 (1,2,3,4)
print(longest_consecutive([10, 5, 12, 11, 6]))     # 3 (10,11,12)


# ────────────────────────────────────────────────────────────
# 🎯 PATTERN DECISION TREE — From Question to Pattern
# ────────────────────────────────────────────────────────────


# [Keywords in Question]  [Pattern]
# "validate", "rules", "true/false" |  P1 — Validation |
# "bill", "invoice", "GST", "discount" |  P2 — Billing |
# "maximise", "optimise", "select items" |  P3 / P13 — Greedy / Knapsack |
# "count", "frequency", "most common" |  P4 — Frequency Counter |
# "classify", "category", "grade" |  P5 — Tier Classification |
# "date", "month", "day", "valid" |  P6 — Date Validation |
# "happy number", "loop forever" |  P7 — Cycle Detection |
# "sequence", "Collatz", "rule" |  P8 — Conditional Sequence |
# "keypad", "match", "decode" |  P9 — Mapping/Lookup |
# "strength", "score from criteria" |  P10 — Multi-Criterion Scoring |
# "STOP", "until done" |  P11 — STOP-Loop |
# "Fibonacci", "n terms", "series" |  P12 — Sequence Generator |
# "prime", "palindrome" |  P14 — Prime + sqrt |
# "longest consecutive" |  P15 — Set Trick |


# ✅ NOTE: ✅ Master strategy: When you see a coding question, identify which 1-2 patterns it matches.
# Combine if needed (e.g., bill calculation INSIDE a STOP-loop). Adapt the template's variable names
# to match
# the problem. Most questions = 80-90% pattern + 10-20% problem-specific tweak.

# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ╔════════════════════════════════════════════════════════════╗
# ║  FILE 13 — Dataset Playbook                                ║
# ╚════════════════════════════════════════════════════════════╝


# ━━━ 📋 PLAYBOOK CONTENTS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • 🎬 Standard Setup (every Section C)
#   • 📄 Step 1: Metadata Recipe
#   • 🔍 Step 2: Filtering Rows
#   • ➕ Step 3: New Column with apply()
#   • 📊 Step 4: GroupBy + Aggregate
#   • 🔀 Step 5: Crosstab vs Pivot
#   • 🎨 Step 6: Choosing the Right Plot
#   • 🎯 Plot Picker (by keyword)
#   • 📚 12 Datasets — Quick Reference
#   • ⚠️ Tricky Patterns Across Papers
#   • 📜 Full Reusable Template
#   • 🧠 Memory Aids
#   • ⚡ Section C Workflow (7-Step)

# ────────────────────────────────────────────────────────────
# 🎬 STANDARD SETUP — EVERY SECTION C STARTS HERE
# ────────────────────────────────────────────────────────────


# ── 📦 Imports + Load ────────────────────────────────
# Always start with this exact 6-line block. Memorise it.

import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")   # load CSV into DataFrame
print(df.head())                # peek at first 5 rows


# ── 🧠 Mnemonic ──────────────────────────────────────
# "PNMP-S" — Pandas, Numpy, Matplotlib, Plot, Seaborn. Always import in this order.

# ────────────────────────────────────────────────────────────
# 📄 STEP 1 — METADATA RECIPE (asked in 6 of 9 papers)
# ────────────────────────────────────────────────────────────


# ────────────────────────────────────────────
# Step 1Read the meta-data of the datasetJul21, Aug21, Mar24P, Mar24S, Feb25
# ────────────────────────────────────────────


# ── 🔹 Question Pattern ──────────────────────────────
# "Read the meta-data: first 10 rows, data types, count of numerical/non-numerical columns,
# statistical summary."

# ── 🔹 Reusable Function ─────────────────────────────

def explore_dataset(df, n=10):
    "Standard metadata recipe — prints head/dtypes/describe/nulls."
    print("=== FIRST {} ROWS ===".format(n))
    print(df.head(n))                    # step 1: peek at data

    print("\n=== DATA TYPES PER COLUMN ===")
    print(df.dtypes)                     # step 2: show int/float/object types

    print("\n=== SHAPE ===")
    print(f"Rows: {df.shape[0]}, Cols: {df.shape[1]}")

    # step 3: count numerical vs non-numerical
    num_cols = df.select_dtypes(include=['number']).columns
    cat_cols = df.select_dtypes(exclude=['number']).columns
    print(f"\nNumerical columns ({len(num_cols)}): {list(num_cols)}")
    print(f"Non-numerical columns ({len(cat_cols)}): {list(cat_cols)}")

    # step 4: statistical summary (numerical only by default)
    print("\n=== STATISTICAL SUMMARY ===")
    print(df.describe())

    # bonus: missing values count
    print("\n=== MISSING VALUES ===")
    print(df.isnull().sum())

# Usage:
explore_dataset(df, n=10)            # works for ANY dataset


# ── ♻️ Reusability ──────────────────────────────────
# Pass any DataFrame — Car, Titanic, Water, Adult — and you'll get the same metadata report.
# Change `n` for more/fewer rows.

# ── 🧠 Memory Aid ────────────────────────────────────
# "HD-NSI" — Head, Dtypes, Numeric/non-numeric Split, Info, Sum-of-nulls.
# Five lines = 5 marks (every Section C opener).

# ────────────────────────────────────────────────────────────
# 🔍 STEP 2 — FILTERING ROWS (asked in ALL 9 papers)
# ────────────────────────────────────────────────────────────


# ────────────────────────────────────────────
# Step 2Filter rows by conditionAll 9 papers
# ────────────────────────────────────────────


# ── 🔹 Question Patterns Seen ────────────────────────
#   • "Find samples with TDS > 500" (Nov23)
#   • "Users with consecutive_usage > 4" (Jul21)
#   • "Countries with population > 100 million" (Mar24S)
#   • "Patients with Age > 60 AND Diabetes = 1" (Aug21)
#   • "Indian athletes who won Gold" (Mar24P)

# ── 🎯 The 5 Filter Patterns ─────────────────────────

# PATTERN 1: Single condition
df[df['TDS'] > 500]

# PATTERN 2: AND (use & with parentheses)
df[(df['Age'] > 60) & (df['Diabetes'] == 1)]

# PATTERN 3: OR (use | with parentheses)
df[(df['Potability'] == 1) | (df['Hardness'] > 200)]

# PATTERN 4: NOT (use ~)
df[~(df['Country'] == 'India')]

# PATTERN 5: Multiple values with isin()
df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]


# ── 🔹 Reusable Function ─────────────────────────────

def filter_rows(df, column, op, value):
    "Filter dataframe by single condition. op: >, =, 
    if   op == '>':  return df[df[column] >  value]
    elif op == ':  return df[df[column] elif op == '>=': return df[df[column] >= value]
    elif op == ': return df[df[column] elif op == '==': return df[df[column] == value]
    elif op == '!=': return df[df[column] != value]
    else: raise ValueError("Unknown operator")

# Usage:
high_tds = filter_rows(df, 'TDS', '>', 500)
print(f"Found {len(high_tds)} samples with TDS > 500")


# ── ⚠️ Common Mistakes ──────────────────────────────
#   • Using and / or / not instead of & / | / ~ — pandas requires bitwise operators
#   • Forgetting parentheses around each condition: df[df.A > 5 & df.B < 10] ❌ → df[(df.A > 5) & (df.B < 10)] ✅
#   • Using = instead of == for equality check

# ── 🧠 Mnemonic ──────────────────────────────────────
# "&|~ with ()" — In pandas, & = and, | = or, ~ = not. Always wrap each side in parentheses.

# ────────────────────────────────────────────────────────────
# ➕ STEP 3 — CREATING A CONDITIONAL COLUMN (asked in ALL 9 papers)
# ────────────────────────────────────────────────────────────


# ────────────────────────────────────────────
# Step 3Add new categorical column based on conditionAll 9 papers
# ────────────────────────────────────────────


# ── 🔹 Question Patterns Seen ────────────────────────
#   • "Categorise life expectancy as High/Medium/Low" (Mar24S)
#   • "Create Hardness_Category column: Low/Moderate/High" (Nov23)
#   • "Movie age limit: U/UA/A/S" (Nov23)
#   • "family_size = SibSp + Parch + 1" (Nov23)
#   • "Cabin_Type from Cabin column first letter" (Nov23)
#   • "Tall+Heavy classify athletes" (Mar24P)
#   • "Age groups: Child/Teen/Adult/Senior" (Nov23)

# ── 🎯 The 3 apply() Patterns ────────────────────────

# ─── PATTERN A: apply on ONE column ───
def categorise_age(age):
    if   age 13: return 'Child'
    elif age 20: return 'Teen'
    elif age 60: return 'Adult'
    else:           return 'Senior'

df['Age_Group'] = df['Age'].apply(categorise_age)

# ─── PATTERN B: apply on MULTIPLE columns (axis=1) ───
def family_size(row):
    return row['SibSp'] + row['Parch'] + 1   # +1 for self

df['family_size'] = df.apply(family_size, axis=1)

# ─── PATTERN C: apply with lambda for short logic ───
df['Cabin_Type'] = df['Cabin'].apply(lambda x: x[0] if pd.notna(x) else 'Unknown')

# Or with axis=1 + lambda
df['family_size'] = df.apply(lambda r: r['SibSp'] + r['Parch'] + 1, axis=1)


# ── 🔹 Generic Categoriser Template ──────────────────

def make_category_column(df, source_col, new_col, rules):
    "Create new categorical column from list of (condition_fn, label) tuples."
    def apply_rules(value):
        for condition, label in rules:
            if condition(value):
                return label
        return 'Unknown'

    df[new_col] = df[source_col].apply(apply_rules)
    return df

# Usage example: hardness categorisation
rules = [
    (lambda x: x 100, 'Low'),
    (lambda x: x 200, 'Moderate'),
    (lambda x: True,    'High'),  # catch-all
]
df = make_category_column(df, 'Hardness', 'Hardness_Category', rules)


# ── ♻️ Reusability ──────────────────────────────────
# The `make_category_column` function works for ANY classification task — just change the
# `rules` list. Apply this to: age groups, salary brackets, score grades, water quality,
# movie ratings, BMI categories, etc.

# ── 🧠 Mnemonic ──────────────────────────────────────
# "axis=1 reads ACROSS" — when your function needs multiple columns from each row,
# `axis=1`. When you only need one column, `df['col'].apply()` is enough.

# ────────────────────────────────────────────────────────────
# 📊 STEP 4 — GROUPBY + AGGREGATE (asked in ALL 9 papers)
# ────────────────────────────────────────────────────────────


# ────────────────────────────────────────────
# Step 4GroupBy + Aggregation — split-apply-combineAll 9 papers
# ────────────────────────────────────────────


# ── 🔹 Question Patterns Seen ────────────────────────
#   • "Average price per brand" (Oct24, May25)
#   • "Count of countries per continent" (Mar24S)
#   • "Survival rate by Embarked port" (Nov23)
#   • "Avg hours-per-week by salary class and country" (Mar24S — multi-level)
#   • "Total deaths per year per country" (Feb25)
#   • "Average rating per metric" (Jul21)

# ── 🎯 The 4 GroupBy Patterns ────────────────────────

# ─── PATTERN 1: Single column, single agg ───
df.groupby('Continent')['Population'].mean()

# ─── PATTERN 2: Single column, MULTIPLE aggs ───
df.groupby('Embarked')['Fare'].agg(['mean', 'min', 'max', 'count'])

# ─── PATTERN 3: Named aggregations (cleaner output) ───
df.groupby('Embarked').agg(
    Passenger_Count = ('PassengerId', 'count'),
    Avg_Age         = ('Age',         'mean'),
    Median_Fare     = ('Fare',        'median')
).round(2)

# ─── PATTERN 4: Multi-level groupby + unstack ───
df.groupby(['native-country', 'salary'])['hours-per-week'].mean() \
  .unstack('salary')   # makes salary into columns instead of nested rows


# ── 🔹 Reusable Function ─────────────────────────────

def summarize_by_group(df, group_col, value_col, aggs=None):
    "Generic group-summary function. aggs default: mean,min,max,count."
    if aggs is None:
        aggs = ['mean', 'min', 'max', 'count']
    result = df.groupby(group_col)[value_col].agg(aggs).round(2)
    return result.sort_values(by=aggs[0], ascending=False)

# Usage:
summary = summarize_by_group(df, 'Continent', 'Population')
print(summary)


# ── 🧠 Mnemonic ──────────────────────────────────────
# "SAC: Split, Apply, Combine" — groupby splits data into groups, agg applies a function
# to each group, then pandas combines the results. Use `.unstack()` to convert nested
# multi-index into wide-format columns.

# ────────────────────────────────────────────────────────────
# 🔀 STEP 5 — CROSSTAB vs PIVOT_TABLE (asked in 4 papers)
# ────────────────────────────────────────────────────────────


# ────────────────────────────────────────────
# Step 5Cross-tabulation: 2 categorical variablesAug21, Mar24P, Feb25, May25
# ────────────────────────────────────────────


# ── 🔹 Question Patterns Seen ────────────────────────
#   • "Crosstab of Diabetes × Survival" (Aug21)
#   • "Survival by Pclass × Sex" (often)
#   • "Salary class proportion by education" (Mar24S)

# ── 🔹 Concept ───────────────────────────────────────
# Both produce 2-D tables. Crosstab is for counting frequency . Pivot
# is for aggregating a numeric value .

# ── 🔹 Examples ──────────────────────────────────────

# ─── CROSSTAB: counts by default ───
pd.crosstab(df['Diabetes'], df['Survived'])
# Shows COUNT of each (Diabetes, Survived) combination

# With percentages: normalize='index' = each row sums to 1
pd.crosstab(df['Diabetes'], df['Survived'], normalize='index') * 100

# With margins (row/col totals)
pd.crosstab(df['Diabetes'], df['Survived'], margins=True)

# ─── PIVOT_TABLE: any aggregation ───
df.pivot_table(values='Fare',
               index='Pclass',
               columns='Sex',
               aggfunc='mean').round(2)

# Multiple aggregations
df.pivot_table(values='Fare',
               index='Pclass',
               columns='Sex',
               aggfunc=['mean', 'count'])


# ── 🔹 Decision Rule ─────────────────────────────────

# [Question Asks…]  [Use]
# "How many in each combination?" |  pd.crosstab(df['A'], df['B']) |
# "Average X by category combo?" |  df.pivot_table(values='X', index='A', columns='B', aggfunc='mean') |
# "Percentage in each row?" |  pd.crosstab(...,normalize='index')*100 |


# ── 🧠 Mnemonic ──────────────────────────────────────
# "Crosstab Counts · Pivot Calculates" — crosstab default is count of rows;
# pivot_table needs a `values` column and an `aggfunc`.

# ────────────────────────────────────────────────────────────
# 🎨 STEP 6 — VISUALISATION (asked in ALL 9 papers)
# ────────────────────────────────────────────────────────────


# ────────────────────────────────────────────
# Step 6Plotting Patterns by Question TypeAll papers
# ────────────────────────────────────────────


# ── 🎯 The Universal Plotting Template ───────────────

def plot_chart(df, plot_type, x=None, y=None, title=""):
    "Generic chart maker - plug in any plot type."
    plt.figure(figsize=(9, 5))                # consistent size

    if   plot_type == 'hist':
        plt.hist(df[x], bins=30, edgecolor='white')
    elif plot_type == 'box':
        sns.boxplot(data=df, x=x, y=y)
    elif plot_type == 'scatter':
        sns.scatterplot(data=df, x=x, y=y)
    elif plot_type == 'count':
        sns.countplot(data=df, x=x)
    elif plot_type == 'heatmap':
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

    plt.title(title)
    plt.xlabel(x or "")
    plt.ylabel(y or "")
    plt.tight_layout()
    plt.show()


# ── ⚡ Quick Recipes ─────────────────────────────────

# Distribution of one variable
sns.histplot(df['Age'], bins=30, kde=True)

# Comparison across categories
sns.boxplot(data=df, x='Continent', y='Population')

# Correlation matrix
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')

# Category counts
sns.countplot(data=df, x='occupation')
plt.xticks(rotation=45)   # rotate long labels

# Pie chart for proportions
df['class'].value_counts().plot(kind='pie', autopct='%1.1f%%')


# ────────────────────────────────────────────────────────────
# 🎯 PLOT PICKER — CHOOSE BY QUESTION KEYWORD
# ────────────────────────────────────────────────────────────


# [Question Keyword]  [Use This Plot]  [Code Snippet]
# distribution / spread / how values are distributed |  histogram |  plt.hist(data, bins=30) | sns.histplot(data, kde=True, bins=30) |
# outliers / IQR / median comparison across groups |  boxplot |  sns.boxplot(data=df, x='cat', y='val') |
# distribution shape + summary by group |  violinplot |  sns.violinplot(data=df, x='cat', y='val') |
# relationship between two numeric variables |  scatter |  sns.scatterplot(data=df, x='X', y='Y') |
# relationship + best-fit line |  regplot |  sns.regplot(data=df, x='X', y='Y') |
# count / frequency of categories |  countplot |  sns.countplot(data=df, x='category') |
# aggregated value (mean/sum) per category |  barplot |  sns.barplot(data=df, x='cat', y='val') |
# share / proportion of a whole |  pie |  df['col'].value_counts().plot(kind='pie', autopct='%1.1f%%') |
# correlation matrix / 2-D intensity |  heatmap |  sns.heatmap(df.corr(), annot=True, cmap='coolwarm') |
# trend over time / sequence |  line |  df.plot(x='year', y='value', kind='line') |
# distribution with smooth curve |  hist+kde |  sns.histplot(data, kde=True, bins=30) |
# 2-categorical cross-frequency |  crosstab heat |  sns.heatmap(pd.crosstab(df['A'], df['B']), annot=True) |


# ── 🧠 The Master Decision Rule ──────────────────────
# "What is the question really asking?"
#   • "How are values spread?" → histogram or boxplot
#   • "Is X related to Y?" → scatter (numeric) or boxplot (cat vs num)
#   • "How many in each category?" → countplot or barplot
#   • "What's the correlation pattern?" → heatmap
#   • "How does X change over Y?" → line plot
#   • "What share/proportion?" → pie chart

# ────────────────────────────────────────────────────────────
# 📚 12 DATASETS SEEN — QUICK REFERENCE
# ────────────────────────────────────────────────────────────


# [Dataset]  [Papers]  [Key Columns]  [Style]
# Car Dataset |  Oct24, May25 |  Brand/Model/Year/Price/KM |  regression-style |
# Ecommerce Dataset |  Feb25 |  Order_ID/Date/Product/Qty |  9 sub-questions |
# Suicide Dataset |  Feb25 |  Country/Year/Sex/Age/Deaths |  visualization-heavy |
# Olympics Dataset |  Mar24P |  Athlete/NOC/Year/Sport/Medal |  9 sub-Q + merge |
# Adult Census |  Mar24S |  Age/Education/Occupation/Salary |  7 sub-questions |
# Countries Dataset |  Mar24S |  Name/Continent/Pop/Life Exp/GDP |  8 sub-questions |
# Water Quality |  Nov23 |  Solids/Hardness/Turbidity/Potability |  5 sub-questions |
# Titanic Dataset |  Nov23 |  Age/SibSp/Parch/Fare/Cabin/Survived |  6 sub-questions |
# Covid Patient |  Aug21 |  Age/Gender/Hb/BP/Cholesterol/Diabetes/Survival |  histograms+crosstab |
# Website Rating |  Jul21 |  userid/Ucredit/Ureview/Web_review/products |  heatmap+countplot |
# Student Stress |  Model Set |  Age/Gender/AcademicLevel/Stress/Hours |  general analysis |
# Bookstore |  Feb25 |  Title/Author/Price/Genre |  filtering |


# ────────────────────────────────────────────────────────────
# ⚠️ TRICKY PATTERNS THAT TRIP STUDENTS UP
# ────────────────────────────────────────────────────────────


# ── ⚠️ Trap 1: pd.notna() in apply() ────────────────

# Cabin column has many NaN — extracting first letter requires guard

# ❌ WRONG: crashes on NaN
df['Cabin_Type'] = df['Cabin'].apply(lambda x: x[0])  # TypeError on NaN

# ✅ CORRECT: check pd.notna() first
df['Cabin_Type'] = df['Cabin'].apply(
    lambda x: x[0] if pd.notna(x) else 'Unknown'
)


# ── ⚠️ Trap 2: Distinct values across multiple columns 

# Jul21 Q4: distinct products in Product_1 + Product_2 + Product_3

# ❌ WRONG: only counts within one column
df['Product_1'].nunique()

# ✅ CORRECT: concat all 3 columns, then unique
all_products = pd.concat([df['Product_1'], df['Product_2'], df['Product_3']])
distinct_count = all_products.dropna().nunique()


# ── ⚠️ Trap 3: Row-wise mean across columns ─────────

# Jul21: avg_rating = mean of Ucredit, Ureview, Web_review for each row

# ❌ WRONG: this gives column means (single number per col)
df['avg_rating'] = df[['A', 'B', 'C']].mean()

# ✅ CORRECT: axis=1 means "across columns, per row"
df['avg_rating'] = df[['A', 'B', 'C']].mean(axis=1).round(1)


# ── ⚠️ Trap 4: Boolean indexing with multiple conditions 

# Wants: rows where Age > 30 AND Salary == '>50K'

# ❌ WRONG: 'and' fails on Series
df[df['Age'] > 30 and df['Salary'] == '>50K']

# ✅ CORRECT: use & with parens
df[(df['Age'] > 30) & (df['Salary'] == '>50K')]


# ── ⚠️ Trap 5: groupby on multiple columns ──────────

# Mar24S: avg hours by country and salary class

# groupby returns multi-index Series
df.groupby(['native-country', 'salary'])['hours-per-week'].mean()

# Use unstack() to flatten into a 2-D table
df.groupby(['native-country', 'salary'])['hours-per-week'].mean() \
  .unstack('salary')


# ────────────────────────────────────────────────────────────
# 📜 FULL REUSABLE SECTION-C TEMPLATE
# ────────────────────────────────────────────────────────────


# ── 🔹 Copy-Paste This Template for Any Section C ────

# ════════════════════════════════════════════════════════════
# SECTION C — UNIVERSAL TEMPLATE
# Adapt the parts marked with 
# ════════════════════════════════════════════════════════════

# ─── 1. IMPORTS ───
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns

# ─── 2. LOAD ───
df = pd.read_csv("data.csv")            # <-- CHANGE filename -->

# ─── 3. METADATA RECIPE (5 marks!) ───
print(df.head(10))                       # first 10 rows
print(df.dtypes)                          # data types
print(df.select_dtypes('number').columns) # numerical cols
print(df.select_dtypes(exclude='number').columns)
print(df.describe())                      # statistical summary
print(df.isnull().sum())                  # missing values

# ─── 4. FILTER ROWS ───
filtered = df[df['col'] > 100]               # <-- CHANGE condition -->

# ─── 5. NEW CONDITIONAL COLUMN ───
def categorise(value):
    if   value 100: return 'Low'      # <-- CHANGE thresholds -->
    elif value 200: return 'Medium'
    else:             return 'High'

df['category'] = df['col'].apply(categorise)

# ─── 6. GROUPBY + AGGREGATE ───
summary = df.groupby('group_col').agg(
    Avg_Value = ('value_col', 'mean'),
    Count     = ('value_col', 'count')
).round(2)
print(summary)

# ─── 7. CROSSTAB / PIVOT ───
ct = pd.crosstab(df['A'], df['B'], normalize='index') * 100
print(ct.round(2))

# ─── 8. PLOT ───
plt.figure(figsize=(9, 5))
sns.histplot(df['col'], bins=30, kde=True)   # <-- CHANGE plot type -->
plt.title('Distribution of col')
plt.xlabel('col'); plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ─── 9. WRITE INFERENCE (ALWAYS!) ───
# Inference: most values fall between X and Y, with Z observable...


# ── ♻️ How to use this template ─────────────────────
#   • Read the dataset description in the question
#   • Identify column names mentioned
#   • Replace <-- CHANGE --> spots with actual column names + thresholds
#   • Re-arrange sections to match the order of sub-questions
#   • Always end with a 1-line written inference for full marks

# ────────────────────────────────────────────────────────────
# 🧠 MEMORY AIDS — REVISE 2 MINUTES BEFORE EXAM
# ────────────────────────────────────────────────────────────


# ━━━ 🔤 Mnemonics ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • PNMP-S — Pandas, Numpy, Matplotlib, Plot, Seaborn (import order)
#   • HD-NSI — Head, Dtypes, Numeric/non-numeric Split, Info, Sum-of-nulls
#   • SAC — Split, Apply, Combine (groupby workflow)
#   • "&|~ with ()" — pandas boolean operators always need parentheses
#   • "axis=1 reads ACROSS" — for row-wise operations
#   • "Crosstab Counts · Pivot Calculates"

# ━━━ 🎯 One-Line Summaries ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • df.head() = peek at data
#   • df.describe() = numeric summary
#   • df.dtypes = column types
#   • df['col'].apply(fn) = transform one column
#   • df.apply(fn, axis=1) = transform per row using multiple cols
#   • df.groupby('col').agg(...) = summarize per group
#   • pd.crosstab(A,B) = count combinations
#   • df.pivot_table(...) = aggregate combinations
#   • sns.heatmap(df.corr(), annot=True) = correlation chart

# ━━━ 💡 Quick Wins (always do these) ━━━━━━━━━━━━━━━━━━━━━━
#   • Add plt.tight_layout() before plt.show() — prevents label clipping
#   • Add annot=True, cmap='coolwarm' to heatmaps — examiners love it
#   • Round floats with .round(2) — looks professional
#   • Always write 1-line inference after a chart — easy 1-2 marks
#   • Use numeric_only=True in df.corr() for newer pandas versions

# ━━━ 🚫 Top 5 Avoidable Errors ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • Using and/or instead of &/| on Series
#   • Forgetting parentheses around boolean conditions
#   • Not handling NaN in .apply() with pd.notna()
#   • Using axis=0 when you need axis=1 (or vice versa)
#   • Forgetting .round() — can lose neatness marks

# ────────────────────────────────────────────────────────────
# ⚡ SECTION C 7-STEP WORKFLOW
# ────────────────────────────────────────────────────────────


# ── 🎯 Follow This Order Every Time ──────────────────
#   • Read all sub-questions first — they often share columns/operations.
 Time: 2 minutes.
#   • Imports + Load — paste the standard 5-line block. Time: 30 seconds.
#   • Metadata block — head/dtypes/describe (often worth 5 marks!). Time: 2 minutes.
#   • Solve sub-questions in order — each in its own clearly-labelled cell.
 Add a comment showing the question number.
#   • Write 1-line inference after every plot or aggregation.
 "Inference: the data shows X is highest in Y." Easy 1 mark each.
#   • Round + format outputs — .round(2), sort by relevant column.
#   • Final review — check all sub-questions answered, all plots have title/labels.
 Time: 2 minutes.

# ── 🧠 Time Budget for Section C (40 marks) ──────────
# Total ~80 minutes. Allocate as: 5 min planning + 5 min metadata + 60 min sub-questions
# (~10 min per 5-mark question) + 10 min review/inferences. Don't get stuck — if a sub-question takes
# >15 min, write what you can and move on.

# ── ♻️ Cross-Reference ──────────────────────────────
# For deeper coverage of the underlying tools, see:
#   • 09 · Pandas Basics — DataFrames, indexing, missing values
#   • 10 · Pandas Advanced — groupby, merge, pivot details
#   • 11 · Visualization — every plot type with examples
#   • 12 · Coding Patterns — reusable function templates
#   • 14 · Exam Strategy — full time management plan
# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ╔════════════════════════════════════════════════════════════╗
# ║  FILE 14 — Exam Strategy                                   ║
# ╚════════════════════════════════════════════════════════════╝


# ━━━ 📋 STRATEGY CONTENTS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   • ⏰ Time Management — 3 Hours, 100 Marks
#   • 🎯 Question Order — Don't Solve in Sequence!
#   • ⚡ Fast-Write Tactics for Section A
#   • 💻 Section B — Coding Workflow
#   • 📊 Section C — Dataset Workflow
#   • 📋 Cheat-Block Library (memorise these!)
#   • ⚠️ Top 18 Common Traps
#   • 🧠 All Mnemonics in One Place
#   • 🔧 Debugging Tips
#   • ✅ Last-Minute Exam Checklist

# ────────────────────────────────────────────────────────────
# ⏰ TIME MANAGEMENT — 3 Hours, 100 Marks
# ────────────────────────────────────────────────────────────


# ── 🎯 The 180-Minute Plan ───────────────────────────

# [Phase]  [Time]  [Activity]  [Marks]
# 1. Read all questions |  0–10 min |  Skim entire paper, note unfamiliar items |  — |
# 2. Section A (theory) |  10–35 min |  10 short answers, 2 marks each |  20 |
# 3. Section B (coding) |  35–115 min |  5 coding problems, ~16 min each |  40 |
# 4. Section C (datasets) |  115–170 min |  2 datasets with 5–9 sub-Q each |  40 |
# 5. Review & cleanup |  170–180 min |  Check answers, add inferences |  — |


# ── 🧠 Time Budget Per Question Type ─────────────────
#   • Section A (2-mark Q): Max 2.5 minutes each. If stuck after 1 min, move on.
#   • Section B (5-mark Q): Max 8 minutes. Plan 1 min, code 5 min, test 2 min.
#   • Section B (10-mark Q): Max 16 minutes. Plan 2 min, code 10 min, test 4 min.
#   • Section C (per sub-Q): ~10 minutes per 5 marks. Inference adds 1-2 marks easily.

# ── ⚠️ The 50% Rule ─────────────────────────────────
# If you've spent 50% of allocated time and aren't halfway through, stop and move on.
# Come back later. A perfect solution to one question is worse than partial solutions to three.

# ────────────────────────────────────────────────────────────
# 🎯 QUESTION ORDER — DON'T SOLVE SEQUENTIALLY
# ────────────────────────────────────────────────────────────


# ── 🎯 The Best Order ────────────────────────────────
#   • Section A first — fastest marks per minute. Builds confidence.
#   • Within Section A: answer EASY ones first (definitions you know cold), come back to harder ones.
#   • Section C metadata sub-Q — get the 5 easy marks for head/dtypes/describe.
#   • Section B coding — start with the one whose pattern matches a known template (validation, billing, classification).
#   • Section C remaining sub-Q — work through one dataset at a time.
#   • Section B hardest — leave for last (knapsack, dynamic algorithms).
#   • Final review — fill in skipped Section A items, add inferences to Section C plots.

# ── ✅ Why This Order Works ──────────────────────────
#   • Section A is highest mark/minute ratio — guarantee these.
#   • Metadata in Section C is template-able — write once, get 5 marks.
#   • Pattern-matching Section B questions are fast wins.
#   • Hardest items last means if you run out of time, you've lost the least.

# ────────────────────────────────────────────────────────────
# ⚡ FAST-WRITE TACTICS FOR SECTION A
# ────────────────────────────────────────────────────────────


# ── 🎯 The 4-Line Answer Template ────────────────────
# For any "What is X?" or "Difference between X and Y?" question, use this template:
#   • Line 1: One-sentence definition
#   • Line 2: One short syntax/code example
#   • Line 3: Difference/key point (if comparison)
#   • Line 4: Use case or memory aid (optional)

# ── 🔹 Examples ──────────────────────────────────────

# [Question]  [4-Line Answer]
# What is type casting? |
# 1. Converting one type to another.
# 2. int("5") → 5; float(3) → 3.0
# 3. Implicit (auto) vs Explicit (programmer)
# 4. int(3.99) = 3 truncates, not rounds! |
# find() vs index()? |
# 1. Both find substring index.
# 2. "abc".find("z") → -1; "abc".index("z") → ValueError
# 3. find() is safe, index() raises exception.
# 4. Use find() if substring may be missing. |
# What are *args and **kwargs? |
# 1. Variable-length arguments to functions.
# 2. def f(*args, **kwargs): args=tuple, kwargs=dict
# 3. *args = positional, **kwargs = keyword.
# 4. Used when count of args is unknown. |


# ── 🧠 Speed-Writing Rules ───────────────────────────
#   • Definitions = 1 line. Don't expand unless 5+ marks.
#   • Code examples = single line. Don't write full programs.
#   • Use bullet points / arrows (→) instead of prose.
#   • Skip preamble like "There are several ways to..."

# ────────────────────────────────────────────────────────────
# 💻 SECTION B WORKFLOW (CODING)
# ────────────────────────────────────────────────────────────


# ── 🎯 The 5-Step Coding Process ─────────────────────
#   • Read carefully (1 min): Note inputs, expected outputs, edge cases. Underline key requirements.
#   • Identify pattern (30 sec): Match to one of the 15 patterns from file 12.
#   • Write function shell (1 min): def name(params): pass with clear docstring.
#   • Code main logic (5–10 min): Add line-by-line comments as you write.
#   • Test mentally (1–2 min): Walk through with sample input from question.

# ── ✅ Mark-Maximising Tips ──────────────────────────
#   • Always wrap in a function — even if not asked. Shows good design.
#   • Add comments — Examiners give partial marks for logic even if code has bugs.
#   • Print sample output — show test cases at the bottom.
#   • Validate inputs when relevant (length checks, type checks).
#   • Use meaningful variable names — total_sum not t.
#   • Match exact output format from the question (spacing, decimals, labels).

# ── 🔹 Standard Section B Code Skeleton ──────────────

def solve_problem(input_data):
    # Step 1: Validate / parse input
    if not input_data:
        return None

    # Step 2: Initialize variables
    result = []

    # Step 3: Main logic (loop / conditions / aggregation)
    for item in input_data:
        # process each item
        result.append(item)

    # Step 4: Return / print output
    return result

# ─── TEST ───
if __name__ == "__main__":
    sample = [1, 2, 3]   # or input() call
    output = solve_problem(sample)
    print(output)


# ────────────────────────────────────────────────────────────
# 📊 SECTION C WORKFLOW (DATASETS)
# ────────────────────────────────────────────────────────────


# ── 🎯 The 7-Step Dataset Process ────────────────────
# Detailed full walkthrough is in file 13 — Dataset Playbook .
# Quick summary:
#   • Read ALL sub-questions before writing any code (2 min)
#   • Imports + load (30 sec)
#   • Metadata block (head, dtypes, describe) — almost always 5 marks!
#   • Solve sub-questions in order, label each clearly
#   • Add 1-line inference after every plot/aggregation
#   • Round outputs with .round(2), sort sensibly
#   • Final review — every sub-Q answered, every plot has title/labels

# ── ✅ Marks-You-Often-Lose ──────────────────────────
#   • Forgetting to write inference after a plot — easy 1 mark each
#   • Not rounding floats — looks unprofessional
#   • Plot without title or axis labels — examiners deduct
#   • Wrong axis (axis=0 vs axis=1) — gives wrong answer
#   • Using and instead of & in pandas filters — runtime error

# ────────────────────────────────────────────────────────────
# 📋 CHEAT-BLOCK LIBRARY — MEMORISE THESE 10
# ────────────────────────────────────────────────────────────

# 📌 Goal: Memorise these 10 code blocks cold. They cover ~80% of all coding tasks
# across Sections B and C. Type them from memory daily until automatic.

# ── 🔹 BLOCK 1: IMPORTS ──────────────────────────────

import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns


# ── 🔹 BLOCK 2: LOAD + EXPLORE ───────────────────────

df = pd.read_csv("data.csv")
df.head(10); df.dtypes; df.describe()
df.isnull().sum()    # count NaN per col


# ── 🔹 BLOCK 3: FILTER ROWS ──────────────────────────

df[df['col'] > 100]
df[(df['A'] > 5) & (df['B'] == 1)]
df[df['col'].isin(['X', 'Y'])]


# ── 🔹 BLOCK 4: NEW COLUMN with apply ────────────────

df['cat'] = df['val'].apply(lambda x: 'High' if x>=75 else 'Low')
df['fs']  = df.apply(lambda r: r['A']+r['B'], axis=1)


# ── 🔹 BLOCK 5: GROUPBY ──────────────────────────────

df.groupby('col')['val'].mean()
df.groupby('A').agg({'B':'mean', 'C':'count'})


# ── 🔹 BLOCK 6: PLOT ─────────────────────────────────

plt.figure(figsize=(9,5))
sns.histplot(df['col'], bins=30, kde=True)
plt.title('Title'); plt.tight_layout(); plt.show()


# ── 🔹 BLOCK 7: FUNCTION TEMPLATE ────────────────────

def solve(data):
    # step 1: validate input
    # step 2: process
    # step 3: return result
    return result


# ── 🔹 BLOCK 8: STRING VALIDATION ────────────────────

def validate(s):
    if len(s) 4:           return False
    if not s[0].isalpha(): return False
    if s[-1] == '_':        return False
    return True


# ── 🔹 BLOCK 9: READ INPUT (numbers) ─────────────────

n = int(input("Enter n: "))
nums = list(map(int, input().split()))
data = [int(x) for x in input().split(',')]


# ── 🔹 BLOCK 10: FREQUENCY COUNT ─────────────────────

from collections import Counter
counts = Counter(words)         # dict-like
counts.most_common(3)            # top 3


# ────────────────────────────────────────────────────────────
# ⚠️ TOP 18 COMMON TRAPS — KNOW EVERY ONE
# ────────────────────────────────────────────────────────────


# [#]  [Trap]  [Explanation]  [Topic]
# 1 |  int(3.99) returns 3 |  int() truncates, NEVER rounds. Use round(3.99) = 4 instead. |  Type casting |
# 2 |  find() vs index() |  find() returns -1 if missing | index() raises ValueError. Use find() to be safe. |  Strings |
# 3 |  == vs is |  == checks values | is checks identity. Use == for value comparison, is only for None. |  Operators |
# 4 |  Mutable default args |  def f(x, lst=[]): is dangerous - lst is shared! Use lst=None then init. |  Functions |
# 5 |  List vs Tuple |  List = mutable [] | Tuple = immutable () | Tuple is hashable, list is not. |  Data structures |
# 6 |  and/or vs &/| |  Python uses and/or for booleans. Pandas Series need & / | with parentheses. |  Pandas |
# 7 |  axis=0 vs axis=1 |  axis=0 = down columns (per column) | axis=1 = across rows (per row). |  Pandas |
# 8 |  range(n) is 0 to n-1 |  range(5) gives 0,1,2,3,4 NOT 1,2,3,4,5. Use range(1, n+1) for 1..n. |  Loops |
# 9 |  Slice end is exclusive |  lst[2:5] returns indices 2,3,4. NOT 5. lst[k:l+1] for inclusive l. |  Lists |
# 10 |  Strings are immutable |  s[0]='X' fails. Use s = 'X' + s[1:] to 'modify'. |  Strings |
# 11 |  Lambda single expression |  Lambda can't have if-elif-else statements. Use ternary or full def. |  Functions |
# 12 |  Empty list [] is falsy |  if lst: is True for non-empty list, False for empty. Same for dict, str. |  Booleans |
# 13 |  dict iteration order |  Dicts preserve INSERTION order in Python 3.7+. Don't rely on alphabetical. |  Dictionaries |
# 14 |  NaN != NaN |  np.nan == np.nan is False. Use pd.isna(x) or pd.notna(x) instead. |  Pandas |
# 15 |  groupby return type |  groupby().sum() returns DataFrame; groupby()['col'].sum() returns Series. |  Pandas |
# 16 |  Reset index after groupby |  Use .reset_index() to convert groupby Series back to DataFrame. |  Pandas |
# 17 |  seaborn vs matplotlib |  sns plots use data=df, x='col'. plt expects raw lists/arrays. |  Visualization |
# 18 |  plt.show() at end |  Forgetting plt.show() means no plot displayed in some environments. |  Visualization |


# ────────────────────────────────────────────────────────────
# 🧠 ALL MNEMONICS IN ONE PLACE
# ────────────────────────────────────────────────────────────


# [Mnemonic]  [Stands For]  [Topic]
# IFBSTFB |  Immutable: Int, Float, Bool, String, Tuple, Frozenset, Bytes |  Data types |
# L-I-N-E-N |  Linear regression assumptions: Linearity, Independence, Normality, Equal variance, No multicollinearity |  Stats |
# PNMP-S |  Pandas, Numpy, Matplotlib, Plot, Seaborn — import order |  Pandas |
# HD-NSI |  Head, Dtypes, Numeric/non-numeric Split, Info, Sum-of-nulls |  Pandas metadata |
# SAC |  Split, Apply, Combine — groupby workflow |  Pandas |
# LEGB |  Local, Enclosing, Global, Built-in — variable lookup order |  Functions |
# CAP-V |  Center (mean), Average, Position (median, percentile), Variance/spread |  Stats |
# STOP |  while STOP marker pattern for input loops |  Loops |
# U-UA-A-S |  Movie ratings: Universal, Universal/Adult, Adult, Special |  Section B |
# AMFMD |  Rank methods: Average, Min, First, Max, Dense |  Pandas |


# ────────────────────────────────────────────────────────────
# 🔧 DEBUGGING TIPS — WHEN CODE DOESN'T WORK
# ────────────────────────────────────────────────────────────


# ── ⚠️ 5 Most Common Errors ─────────────────────────

# [Error]  [Cause]  [Fix]
# NameError |  Variable used before defined OR typo |  Check spelling, scope, import statement |
# TypeError |  Wrong type passed (e.g., int() on None) |  Add type check, handle None/NaN |
# IndexError |  Index out of range |  Check len(lst) before accessing |
# KeyError |  Dict key doesn't exist |  Use dict.get(k, default) |
# ValueError |  Right type, wrong value (e.g., int("abc")) |  Wrap in try/except or validate first |


# ── ✅ Debug Workflow ────────────────────────────────
#   • Read the error message — it usually points to the exact line.
#   • Add print statements — print intermediate values: print(f"x = {x}")
#   • Check types — print(type(x)) when output is unexpected.
#   • Check shape — for DataFrames/arrays: print(df.shape)
#   • Reduce to smaller input — does it work with [1, 2, 3]? Then scale up.

# ── 🧠 In-Exam Debug Mantra ──────────────────────────
# "Print, Print, Print" — when stuck, add `print()` after every step
# to see what's happening. Don't try to read code in your head.

# ────────────────────────────────────────────────────────────
# ✅ LAST-MINUTE EXAM CHECKLIST
# ────────────────────────────────────────────────────────────


# ── ✅ The Night Before ──────────────────────────────
#   • ☐ Read this entire file (20 min)
#   • ☐ Skim 12 · Coding Patterns — recognise each pattern
#   • ☐ Skim 13 · Dataset Playbook — recall the 7-step workflow
#   • ☐ Memorise the 10 cheat-blocks above
#   • ☐ Sleep early — tired brain ≠ working brain

# ── ✅ The Morning Of ────────────────────────────────
#   • ☐ Eat a proper breakfast — energy lasts 3 hours
#   • ☐ Re-read the 18 traps list (5 min)
#   • ☐ Re-read the mnemonics table (3 min)
#   • ☐ Bring 2 working pens, ID, allowed materials
#   • ☐ Reach venue 15 min early — settle nerves

# ── ✅ During the Exam ───────────────────────────────
#   • ☐ Read all questions first (10 min) — note difficulty per question
#   • ☐ Allocate time per section (use the 180-min plan)
#   • ☐ Section A first — fastest marks
#   • ☐ Always check: did I include test/sample output?
#   • ☐ Always check: did I write inference after each plot?
#   • ☐ Always check: are all 4 sub-questions answered?
#   • ☐ Last 10 min: quick review of all answers

# ── 🧠 Final Pep Talk ────────────────────────────────
# You've solved 9 past papers. Every pattern in this exam has appeared before. You know
# the templates. You know the traps. You know the mnemonics. Trust your prep, work
# methodically, manage time strictly. Partial credit beats blank pages — write
# something for every question.
#
#
#
#
#
#
# UE20CS901 — Python for Data Science · Complete Learning System · PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates
#
#
#
#
# UE20CS901 — Python for Data Science · Complete Consolidated Learning System · PES University,
# Bengaluru
# 15 files · Beginner-Friendly · Pattern-Based · Exam-Optimised · Reusable Templates


# ==============================================================
# End of UE20CS901 Complete Learning System
# PES University, Bengaluru
# Beginner-Friendly · Pattern-Based · Exam-Optimised
# ==============================================================