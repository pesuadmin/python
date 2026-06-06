# ============================================================
#   PES University · UE20CS901 — Python for Data Science
#   PDS ESA — The 90+ Beginner Strategy Pack
#   9 papers analysed · 2021 → 2025 · Pattern-first
#   Beginner-commented code
#
#   Built from: May 2025, Oct 2024, Aug 2021, July 2021,
#   Mar 2024 (ESA + scan), Nov 2023, Model Set.
#   Two papers were image-only and were recovered via OCR.
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import random
from functools import reduce


# ╔════════════════════════════════════════════════════════════╗
# ║  SECTION 1 · Section C — Verification & Pattern Analysis   ║
# ╚════════════════════════════════════════════════════════════╝

# The claim ("Section C is always the exact same task") is HALF TRUE.
# Section C is NOT always the same dataset or topic. But it IS the same
# type of task every single time, and the SET OF OPERATIONS tested barely
# changes. Memorise the operations, not a dataset.


# ──────────────────────────────────────────
# What Section C actually is, every paper
# ──────────────────────────────────────────

# Across all 9 papers, Section C is identical in SHAPE: you are given a
# real CSV dataset + a data dictionary, and asked to do Exploratory Data
# Analysis (EDA) — load it, filter/group/aggregate with pandas, engineer
# a category column, and produce a few plots with matplotlib/seaborn. It
# is NEVER machine-learning modelling (no train/test, no sklearn fit).
# It is always "pandas + plots + write your inference."


# ──────────────────────────────────────────
# Proof — the same 8 operations recur
# ──────────────────────────────────────────

# Recurring Section-C operation                       May25 Oct24 Nov23 Mar24 Aug21 Jul21 Model
# Load + filter rows by condition, report a stat        ✓     ✓     ✓     ✓     ✓     ✓     ✓
# groupby + mean/max aggregate                          ✓     ✓     ✓     ✓     ✓     ✓     ✓
# Create category column (Low/Mod/High via apply)       ✓     ✓     ✓     ✓     –     –     ✓
# Split into 2 sub-DataFrames by a category             ✓     ✓     ✓     –     ✓     ✓     –
# Handle / drop missing values                          ✓     ✓     –     –     –     –     –
# Boxplot / countplot / distribution (hist 20-30 bins)  ✓     –     ✓     ✓     ✓     ✓     ✓
# Correlation heatmap                                   –     –     –     –     –     ✓     ✓
# crosstab / pivot_table                                –     –     –     –     ✓     –     ✓

# Core objective of Section C (state this in your head before the exam):
# "Read a CSV with pandas → answer business questions using filter,
#  groupby, apply → add a categorical column → draw 2-4 plots → write a
#  one-line inference."  That is the whole game.
# Datasets seen: car_info, water, titanic, countries, adult, covid,
#   website-ratings, student-stress, olympics-athletes.
# The dataset changes; the verbs don't.


# ╔════════════════════════════════════════════════════════════╗
# ║  SECTION 2 · Universal Section-C Code Template             ║
# ╚════════════════════════════════════════════════════════════╝

# This single script handles EVERY Section-C operation in the table
# above. Paste it, set the path, and you have ~70% of Section C done
# before you read the questions. Every line is commented in plain
# English.
#
# How to use in the exam:
#   Run BLOCK 0 first. Then for each sub-question, copy only the
#   matching mini-block and change the column names. You do not need
#   all of it every time.


# ──────────────────────────────────────────
# BLOCK 0 — Setup & Load (always run first)
# ──────────────────────────────────────────

# Import the four libraries every Section C needs
import pandas as pd            # pandas = tables/DataFrames (the main tool)
import numpy  as np            # numpy = fast maths on numbers
import matplotlib.pyplot as plt  # basic plotting
import seaborn as sns          # prettier statistical plots

# Load the dataset. CHANGE ONLY THE PATH BELOW
df = pd.read_csv("INSERT_DATASET_PATH_HERE.csv")  # reads CSV file into a table called df

# "Read the meta-data" (asked verbatim in July'21)
print(df.head(10))    # first 10 rows — see what the data looks like
print(df.shape)       # (rows, columns) — how big is it
print(df.dtypes)      # data type of each column (number? text?)
print(df.info())      # types + how many missing values per column
print(df.describe())  # count/mean/std/min/max for numeric columns
print(df.isnull().sum())  # count of missing values in each column


# ──────────────────────────────────────────
# MINI-BLOCK A — Filter rows + report a statistic
# ──────────────────────────────────────────

# "Find number of cars with price > $25000 and their average mileage"
# "samples with TDS > 500" · "passengers older than X"

# Keep only rows where a condition is true. CHANGE column + number.
subset = df[df["Price"] > 25000]   # df[ condition ] = filtered rows
print("How many rows match:", len(subset))      # len() counts the rows
print("Average of another column:", subset["Mileage"].mean())  # .mean() = average
# INFERENCE: write 1 line, e.g. "Expensive cars tend to have lower mileage."


# ──────────────────────────────────────────
# MINI-BLOCK B — groupby aggregate (the single most-tested op)
# ──────────────────────────────────────────

# "average price and max mileage for each Make"
# "average hemoglobin by gender" · "avg fare by Embarked"

# Group rows that share a category, then summarise each group.
result = df.groupby("Make").agg(
    avg_price   = ("Price",   "mean"),   # new col = (source col, function)
    max_mileage = ("Mileage", "max")
)
print(result)
# Quick version if you only need one number:
# df.groupby("Make")["Price"].mean()


# ──────────────────────────────────────────
# MINI-BLOCK C — Create a category column with apply (high-frequency!)
# ──────────────────────────────────────────

# "classify Mileage as Low/Moderate/High"
# "categorize hardness" · "categorize life expectancy"

# Step 1: write a plain function that decides the label for ONE value.
def categorize(value):              # 'value' is one cell, e.g. one mileage
    if value < 30000:
        return "Low"
    elif value < 100000:           # between 30k and 100k
        return "Moderate"
    else:
        return "High"

# Step 2: apply that function to every row of the column -> new column.
df["Mileage_Category"] = df["Mileage"].apply(categorize)
print(df[["Mileage", "Mileage_Category"]].head())


# ──────────────────────────────────────────
# MINI-BLOCK D — Split into two sub-DataFrames
# ──────────────────────────────────────────

# "separate Petrol and Diesel" · "potable vs non-potable water"

petrol = df[df["Fuel_Type"] == "Petrol"]   # rows where fuel is Petrol
diesel = df[df["Fuel_Type"] == "Diesel"]
print("Petrol avg price:", petrol["Price"].mean())
print("Diesel avg price:", diesel["Price"].mean())


# ──────────────────────────────────────────
# MINI-BLOCK E — Missing values
# ──────────────────────────────────────────

# "calculate average price filtering out missing Price or Mileage"
# "deal with missing values"

# Drop rows missing EITHER of the named columns, then compute.
clean = df.dropna(subset=["Price", "Mileage"])  # dropna = remove missing rows
print(clean.groupby("Make")["Price"].mean())
# Alternative — fill instead of drop: df["Price"].fillna(df["Price"].mean())


# ──────────────────────────────────────────
# MINI-BLOCK F — The 4 plots that cover every paper
# ──────────────────────────────────────────

# 1) BOXPLOT (distribution of a number across a category)
sns.boxplot(data=df, x="Make", y="Price", hue="Fuel_Type")
plt.title("Price distribution by Make and Fuel"); plt.xticks(rotation=45); plt.show()

# 2) COUNTPLOT (how many rows in each category)
sns.countplot(data=df, x="assigned_rating"); plt.title("Counts"); plt.show()

# 3) HISTOGRAM / distribution (note: papers often say "use 20 or 30 bins")
sns.histplot(df["avg_rating"], bins=30, kde=True)
plt.title("Distribution of avg_rating"); plt.show()

# 4) CORRELATION HEATMAP (only on numeric columns)
sns.heatmap(df[["colA","colB","colC"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation"); plt.show()


# ──────────────────────────────────────────
# MINI-BLOCK G — crosstab & pivot_table
# ──────────────────────────────────────────

# "cross table of diabetes type vs survival"
# "pivot of stressed-student count by family size"

# crosstab = counts at the intersection of two categories
ct = pd.crosstab(df["Diabetestype"], df["Survive_status"])
print(ct)
# turn counts into row-wise % (the "survival ratio" ask):
print(ct.div(ct.sum(axis=1), axis=0) * 100)

# pivot_table = groupby in grid form with an aggregate
pt = pd.pivot_table(df, index="famsize", columns="famsup",
                    values="Stress", aggfunc="sum")
print(pt)


# ──────────────────────────────────────────
# MINI-BLOCK H — merge two datasets
# ──────────────────────────────────────────

# "merge athletes and regions" (Mar'24 Olympics)

merged = pd.merge(df1, df2, on="region_id", how="left")  # join on a shared key column


# ╔════════════════════════════════════════════════════════════╗
# ║  SECTION 3 · Consolidated Worksheet — Sections A & B       ║
# ╚════════════════════════════════════════════════════════════╝


# ──────────────────────────────────────────
# Section A — Theory (handwritten, 20 marks, 10 × 2)
# ──────────────────────────────────────────

# Section A is PURE RECALL of definitions. The same ~20 questions rotate.
# Group them and memorise the bullets. ★ = appeared in 3+ papers


# ──────────────────────────────────────────
# list vs tuple ★★★
# ──────────────────────────────────────────

# List = mutable, []; Tuple = immutable, (), faster, hashable (usable as
# dict key).


# ──────────────────────────────────────────
# dict vs list ★★
# ──────────────────────────────────────────

# List = ordered, index-accessed. Dict = key→value pairs, unordered (3.7+
# insertion-ordered), key lookup O(1).


# ──────────────────────────────────────────
# lambda / anonymous fn ★★★
# ──────────────────────────────────────────

# One-line nameless function: f = lambda x: x+1. No def/name, single
# expression, no statements. Sum a list: sum([5,8,10,20]) or reduce(lambda
# a,b:a+b, lst).

f = lambda x: x + 1
print(f(4))   # 5


# ──────────────────────────────────────────
# *args / **kwargs ★★★
# ──────────────────────────────────────────

# *args = tuple of extra positional args; **kwargs = dict of extra keyword
# args.

def f(*a, **k): ...
# a is a tuple, k is a dict


# ──────────────────────────────────────────
# map / reduce / filter ★★★
# ──────────────────────────────────────────

# map(fn,seq) transforms each item; filter(fn,seq) keeps where True;
# reduce(fn,seq) folds to one value (from functools).

list(map(lambda x: x*2, [1,2,3]))        # [2,4,6]
list(filter(lambda x: x%2==0, [1,2,3,4]))  # [2,4]
reduce(lambda a,b: a+b, [1,2,3])           # 6


# ──────────────────────────────────────────
# type casting / conversion ★★★
# ──────────────────────────────────────────

# Converting type explicitly: int("5"), str(5), float(). Implicit = Python
# auto-promotes (int+float→float).

int("5") + 1    # 6
float(3)        # 3.0
str(99)         # "99"
x = 2 + 3.0     # implicit -> 5.0 (float)


# ──────────────────────────────────────────
# string immutability + slicing ★★★
# ──────────────────────────────────────────

# Strings can't be changed in place. Slice s[start:stop:step].
# 'PythonProgramming'[2:9] → 'thonPro'. Negative index counts from end
# (s[-1]=last).

s = 'PythonProgramming'
print(s[2:9])   # thonPro
print(s[-1])    # g
# s[0]='X'  -> TypeError (immutable)


# ──────────────────────────────────────────
# sorted() vs sort() ★★
# ──────────────────────────────────────────

# sort() = list method, in-place, returns None. sorted() = function,
# returns new list, works on any iterable.

a = [3,1,2]
a.sort()            # a is now [1,2,3], returns None
b = sorted([3,1,2]) # b=[1,2,3], original kept


# ──────────────────────────────────────────
# list/dict comprehension ★★
# ──────────────────────────────────────────

# Concise one-line construction. List: [x*2 for x in lst]. Dict: {k:len(k)
# for k in lst}.

[x*2 for x in [1,2,3]]           # [2,4,6]
{k:len(k) for k in ["hi","hello"]}  # {"hi":2,"hello":5}


# ──────────────────────────────────────────
# random number ★★
# ──────────────────────────────────────────

# random.random() = float 0–1; random.randint(a,b) = int; numpy:
# np.random.rand().

import random
random.random()       # float in [0.0, 1.0)
random.randint(1,6)   # int 1..6
np.random.rand()      # float in [0.0, 1.0)


# ──────────────────────────────────────────
# reshape vs resize ★★
# ──────────────────────────────────────────

# reshape returns new shape (size must match), doesn't modify original;
# resize modifies in place, can change total size (pads/repeats).

a = np.arange(6)
b = a.reshape(2,3)   # new view; a unchanged -> [1 2 3 4 5 6]
a.resize(3,3)        # a modified in place (pads with 0s)


# ──────────────────────────────────────────
# arange vs linspace ★
# ──────────────────────────────────────────

# arange(start,stop,step) = by step size; linspace(start,stop,n) = n
# evenly-spaced points incl. endpoint.

np.arange(0,1,0.25)   # [0, 0.25, 0.5, 0.75]        (stop exclusive)
np.linspace(0,1,5)    # [0, 0.25, 0.5, 0.75, 1.0]    (stop inclusive)


# ──────────────────────────────────────────
# vstack vs hstack ★
# ──────────────────────────────────────────

# vstack stacks rows (vertically); hstack joins columns (horizontally).

a = np.array([1,2]); b = np.array([3,4])
np.vstack([a,b])   # [[1,2],[3,4]]
np.hstack([a,b])   # [1,2,3,4]


# ──────────────────────────────────────────
# pivot table vs cross table ★★★
# ──────────────────────────────────────────

# pivot_table aggregates a value column over row/col categories (any
# aggfunc). crosstab = frequency count of two categoricals (special case).

pd.crosstab(df["A"], df["B"])          # counts
pd.pivot_table(df, index="A",
    columns="B", values="V",
    aggfunc="mean")                # aggregated values


# ──────────────────────────────────────────
# groupby ★★
# ──────────────────────────────────────────

# Split rows by category → apply aggregate → combine.

df.groupby('col')['v'].mean()


# ──────────────────────────────────────────
# apply vs map ★
# ──────────────────────────────────────────

# map = element-wise on a Series only. apply = works on Series or whole
# DataFrame rows/cols, more flexible.

df['c'].map(str.upper)                         # element-wise on Series
df.apply(lambda row: row['a']+row['b'], axis=1) # row-wise on DataFrame


# ──────────────────────────────────────────
# missing values ★★
# ──────────────────────────────────────────

# Find: df.isnull().sum(). Handle: dropna() (remove) or fillna(value)
# (impute mean/median/mode).

df.isnull().sum()                  # count NaN per column
df.dropna()                        # remove all rows with any NaN
df["Age"].fillna(df["Age"].mean())  # fill NaN with column mean


# ──────────────────────────────────────────
# remove duplicates / reset index ★
# ──────────────────────────────────────────

# df.drop_duplicates() removes duplicate rows; df.reset_index(drop=True)
# renumbers rows 0..n.

df = df.drop_duplicates()
df = df.reset_index(drop=True)


# ──────────────────────────────────────────
# pop vs remove vs del vs clear ★
# ──────────────────────────────────────────

# pop(i)=remove by index+return; remove(v)=remove by value; del=statement
# removes by index/slice; clear()=empty the list.

a = [10,20,30,40]
print(a.pop(1))  # 20 (removed by index, returned)
a.remove(30)     # removes first occurrence of value 30
del a[0]         # removes element at index 0 (no return)
a.clear()        # empties the list -> []


# ──────────────────────────────────────────
# ranking / sort_values vs sort_index ★
# ──────────────────────────────────────────

# sort_values sorts by the data; sort_index sorts by the index labels.
# rank() methods: average, min, max, first, dense.

s = pd.Series([30,10,20], index=["c","a","b"])
s.sort_values()         # 10,20,30
s.sort_index()          # a:10,b:20,c:30
s.rank()                # dense rank
s.rank(method="dense")  # no gaps in ties


# ──────────────────────────────────────────
# static vs dynamic typing ★
# ──────────────────────────────────────────

# Python is DYNAMICALLY typed: variable types decided at runtime, no
# declaration needed.

x = 5           # x is int
x = "now str"   # perfectly legal — type changes at runtime


# ──────────────────────────────────────────
# identity matrix ★
# ──────────────────────────────────────────

# Square, 1s on diagonal, 0 elsewhere: np.eye(n) or np.identity(n).

np.eye(3)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


# ──────────────────────────────────────────
# Section B — Programming (40 marks, ~5 × 8)
# ──────────────────────────────────────────

# Section B mixes REPEATING ARCHETYPES. Learn the "common logic" core of
# each — the 3-5 lines you must be able to write from memory — and you
# can adapt to any wording.


# ──────────────────────────────────────────
# B-1 · Prime / Palindrome / Happy number — number-property filters ★★★
# ──────────────────────────────────────────

# "primes that are palindromes" (May'25),
# "primes from a list" (Oct'24), "happy number" (Mar'24)
#
# Common logic — the prime test you MUST memorise:

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):  # only check up to sqrt(n)
        if n % i == 0: return False     # divisible -> not prime
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]    # reads same backwards

nums = [7, 11, 12, 131, 23, 101]
result = [x for x in nums if is_prime(x) and is_palindrome(x)]
print(result)   # [7, 11, 131, 101]

# Happy number variant:
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))  # sum of squares of digits
    return n == 1
print(is_happy(19))  # True


# ──────────────────────────────────────────
# B-2 · "Manage a system" dict CRUD — students / inventory ★★★
# ──────────────────────────────────────────

# "student marks system" (May'25), "inventory system" (Oct'24),
# "product_inventory" (Mar'24)
#
# Common logic — a dict + 4 tiny functions. Same skeleton every time:

data = {}                              # the store: name -> value
def add_item(name, value):    data[name] = value          # add/insert
def update_item(name, value): data[name] = value          # overwrite
def average():                return sum(data.values()) / len(data)
def display():
    for k, v in data.items(): print(k, v)   # show all

# Student marks example:
students = {}
def add_student(name, marks):   students[name] = marks
def update_marks(name, marks):
    if name in students: students[name] = marks
def average_marks():
    return sum(students.values()) / len(students) if students else 0

add_student('Asha', 88); add_student('Ravi', 72)
update_marks('Ravi', 80)
print(average_marks()); display()


# ──────────────────────────────────────────
# B-3 · Bonus / salary adjustment by tiered rules ★★★
# ──────────────────────────────────────────

# Appears almost verbatim in May'25 & Oct'24 — only the % numbers change.
#
# Common logic — loop the dict, branch on experience, build a NEW dict:

def adjust(emps):                # emps: name -> (years, base, rating)
    out = {}
    for name, (yrs, base, rating) in emps.items():
        if yrs > 10:
            out[name] = base*1.20 + 0.03*base*rating
        elif yrs >= 5:
            out[name] = base*1.15 + 0.02*base*rating
        else:
            out[name] = base*1.10 + 0.01*base*rating
    return out

emps = {'A': (12, 1000, 5), 'B': (7, 1000, 3), 'C': (2, 1000, 4)}
print(adjust(emps))


# ──────────────────────────────────────────
# B-4 · Word-count from sentences (>=4 chars, case-insensitive) ★★
# ──────────────────────────────────────────

# May'25 & Oct'24 (Oct adds a word-length histogram).

import re
sentences = ['The quick brown Fox', 'the lazy dog runs fast']
counts = {}
for s in sentences:
    for w in re.findall(r"[a-zA-Z]+", s.lower()):  # letters only, lowercase
        if len(w) >= 4:
            counts[w] = counts.get(w, 0) + 1     # the count-up idiom
print(counts)

# Oct'24 variant — also plot histogram of word lengths:
lengths = [len(w) for w in counts]
import matplotlib.pyplot as plt
plt.hist(lengths, bins=range(4, max(lengths)+2)); plt.title('Word lengths'); plt.show()


# ──────────────────────────────────────────
# B-5 · map() / filter() one-liners — squares of evens, replace >10, even-check ★★
# ──────────────────────────────────────────

# Mar'24 (square of evens), Mar'24 (replace >10 with 10),
# Aug'21 (all-even via map-reduce).

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squares of even numbers
sq_even = list(map(lambda x: x*x, filter(lambda x: x%2==0, nums)))
print(sq_even)   # [4, 16, 36, 64, 100]

# cap all values at 10 (replace >10 with 10)
capped = list(map(lambda x: 10 if x > 10 else x, [3,12,7,15,9,11,2]))
print(capped)    # [3, 10, 7, 10, 9, 10, 2]

# verify every number is even using map + reduce (Aug'21)
def is_even(x): return x % 2 == 0
def all_even(lst): return reduce(lambda a, b: a and b, map(is_even, lst), True)
print(all_even([2, 4, 6]))   # True
print(all_even([2, 3, 6]))   # False


# ──────────────────────────────────────────
# B-6 · String / username validation, date validation, billing with GST ★★
# ──────────────────────────────────────────

# username rules (Mar'24, Nov'23), GST bill (July'21),
# tiered discount store (Mar'24).
#
# Validation common logic — check length, first char, allowed chars:

def UsernameValidation(s):
    return (4 <= len(s) <= 25            # length window
            and s[0].isalpha()           # starts with a letter
            and s.replace("_","").isalnum()  # only letters/digits/_
            and not s.endswith("_"))     # no trailing _

print(UsernameValidation("user_1"))   # True
print(UsernameValidation("_bad"))     # False

# GST/billing logic:
# Build a price dict -> look up choices -> total*0.12 for GST -> total+gst
prices = {'HDD':{'1TB':5000,'2TB':7500}, 'RAM':{'8GB':4000,'16GB':6000}}
chosen = {'HDD':'1TB', 'RAM':'16GB'}
total = sum(prices[item][typ] for item, typ in chosen.items()) + 4000  # + motherboard
gst = total * 0.12
print('Total with GST:', total + gst)


# ──────────────────────────────────────────
# B-7 · Fibonacci / triangular series / consecutive sequence ★★
# ──────────────────────────────────────────

# Fibonacci (Mar'24), series 0,1,3,6,10... (July'21),
# longest consecutive (Oct'24).

# Fibonacci (iterative — safest):
def fib(n):
    a, b = 0, 1; seq = []
    for _ in range(n): seq.append(a); a, b = b, a+b
    return seq
print(','.join(map(str, fib(10))))  # 0,1,1,2,3,5,8,13,21,34

# Triangular series: term i = i*(i+1)//2  ->  0,1,3,6,10,15...
def triangular(n): return [i*(i+1)//2 for i in range(n)]
def sum_range(n, k, l):
    s = triangular(n); return sum(s[k:l+1])
print(triangular(11))         # [0,1,3,6,10,15,21,28,36,45,55]
print(sum_range(11, 2, 5))    # 3+6+10+15 = 34

# Longest consecutive sequence (Oct'24):
def longest_consecutive_sequence(nums):
    s = set(nums); best = 0
    for x in s:
        if x-1 not in s:           # start of a run
            y = x
            while y+1 in s: y += 1
            best = max(best, y-x+1)
    return best
print(longest_consecutive_sequence([100,4,200,1,3,2]))  # 4

# Optimisation problems (knapsack, job-fair, farmer-truck) appear only
# in older 80-mark papers (2021) and the Model Set — LOW PRIORITY for
# the current 100-mark format. Skip unless you have spare time.


# ╔════════════════════════════════════════════════════════════╗
# ║  SECTION 4 · The 90-Mark Beginner Roadmap                  ║
# ╚════════════════════════════════════════════════════════════╝

# MARKS BREAKDOWN:
#   Section A (20) + Section B (40) + Section C (40) = 100.
#   To hit 90 you can afford to drop ~10 marks. The smart drop is the
#   HARDEST single Section-B program, not scattered points everywhere.


# ──────────────────────────────────────────
# Study order — do these in sequence
# ──────────────────────────────────────────

# ── PRIORITY 1 — Section C template (40 marks · highest ROI) ──────────────
# It is the SAME TASK every time and you have a ready template above.
# This is your biggest, safest block.
# Drill BLOCK B (groupby) and BLOCK C (apply category) until automatic
# — they appear in every paper.
# Practice on 1 car dataset + 1 titanic dataset. If you can do those
# two, you can do any Section C.
# ALWAYS add a one-line inference after each answer — papers explicitly
# award marks for it ("write your inference").
# TARGET: 36/40.

# ── PRIORITY 2 — Section A theory (20 marks · pure memory, easiest win) ──
# Memorise the worksheet table. ~21 definitions cover EVERY question
# ever asked.
# These are 2-mark recall items — no coding, no thinking.
# HIGHEST marks-per-minute in the exam.
# Focus first on the ★★★ rows (list/tuple, lambda, *args, map/reduce,
# type casting, slicing, pivot vs crosstab).
# TARGET: 18/20.

# ── PRIORITY 3 — Section B, the 3 guaranteed archetypes (24 of 40 marks) ──
# Learn cold: B-1 (prime/palindrome), B-2 (dict system), B-3 (bonus tiers).
# These three appear in nearly every recent paper and are worth ~24 marks.
# Then add B-4 (word count) and B-5 (map/filter) — short and formulaic.
# TARGET: 28-32/40.

# ── SKIP / LAST — low-frequency hard items ──────────────────────────────────
# Knapsack, job-scheduling, farmer-truck optimisation, regex telephone,
# Collatz — rare and time-expensive.
# If short on time, DELIBERATELY SACRIFICE one 8-mark Section-B program
# here. That single drop still leaves you at ~92.


# ──────────────────────────────────────────
# "Easy wins" that appear almost every paper
# ──────────────────────────────────────────

# Easy win                             Where         Why it's easy
# Meta-data / df.head, dtypes, describe  Section C(1)  5 marks for 4 one-line calls
# groupby mean/max                       Section C     One memorised line, 7/7 papers
# Low/Mod/High category column           Section C     Copy Block C, change 2 numbers
# list vs tuple / lambda / *args         Section A     2 marks each, pure recall
# prime number filter                    Section B     Same 6 lines, reused across papers
# boxplot / histogram with bins          Section C     One seaborn line + title


# ──────────────────────────────────────────
# Three exam-floor mistakes that cost beginners marks
# ──────────────────────────────────────────

# 1. FORGETTING plt.show() / TITLES
#    Plot questions explicitly say "add an appropriate title."

# 2. NOT WRITING THE INFERENCE LINE
#    It's separately marked.

# 3. HARD-CODING COLUMN NAMES THAT DON'T EXIST
#    Always run df.columns first and match spelling/case exactly.


# ──────────────────────────────────────────
# The whole plan in one breath
# ──────────────────────────────────────────

# Memorise Section A (18) + nail the Section C template (36) + the three
# Section-B archetypes (28) = ~82 guaranteed, with B-4/B-5 and inference
# lines pushing you over 90.
# Spend your last revision hour only on:
#   groupby, apply-category, prime + dict-system snippets.

# ============================================================
# Generated from 9 PDS ESA papers · pattern-frequency analysis
# UE20CS901 · Study aid for exam prep based on past-paper
# patterns — verify column names against the actual exam
# dataset, since those change.
# ============================================================
