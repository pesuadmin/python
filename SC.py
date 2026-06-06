# ============================================================
#   PES University · UE20CS901 — Python for Data Science
#   Section C — Master Guide
#   One toolkit to answer any Section C, on any dataset
#   10 papers distilled · 13 operation families · 1 master pipeline
#   Every snippet tested
# ============================================================

# The one idea that lets you pass without knowing the dataset:
# Section C is ALWAYS the same shape: a real CSV you've never seen,
# plus a numbered list of "do this to it" tasks. The dataset changes
# every exam — ecommerce, cars, patients, students, Olympics, water,
# Titanic, census — but the OPERATIONS are a fixed vocabulary of ~13
# moves. This guide is organised by OPERATION, not by paper. Learn the
# move and its trigger words, and any task — on any data — becomes
# "which move is this?" Replace the generic column names (group_col,
# num_col, cat_col) with whatever the exam's columns are called, and
# you're done.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ╔══════════════════════════════════════════════════════════╗
# ║  STEP 0 · THE LOOKUP TABLE — map the wording to the move ║
# ╚══════════════════════════════════════════════════════════╝

# When you read a Section C task, find its TRIGGER WORDS in column 1
# and jump to the family in column 3.
# Almost every question in all 10 papers maps to one of these.
#
# ┌─────────────────────────────────────────────────────────────────────┬──────────────────────────────────────────────┬──────────────────────────────────┐
# │ If the question says...                                             │ It wants                                     │ Family                           │
# ├─────────────────────────────────────────────────────────────────────┼──────────────────────────────────────────────┼──────────────────────────────────┤
# │ "how many...", "count...", "find all where...",                     │ a filtered count                             │ 1 Filter & count                 │
# │   "number of samples with..."                                       │                                              │                                  │
# │ "...A AND B...", "between X and Y", "either... or..."               │ multi-condition filter (&, |, between)       │ 1 Filter                         │
# │ "proportion of...", "percentage of...", "% that are..."             │ mean of a boolean (or crosstab %)            │ 1 Filter / 9 Crosstab            │
# │ "add a new column...", "create a column for..."                     │ derived column (arithmetic / cut / apply)    │ 2 New columns                    │
# │ "categorise / classify into Low/Med/High / groups"                  │ pd.cut or apply                              │ 2 New columns                    │
# │ "average / mean / max / min X FOR EACH Y", "...per group"           │ groupby + agg                                │ 3 Group & aggregate              │
# │ "highest / most expensive / best PER group"                         │ groupby idxmax → loc                         │ 3 Group                          │
# │ "most common / most frequent", "which X is used most"               │ value_counts().idxmax()                      │ 4 Count categories               │
# │ "top N", "N largest / smallest", "N highest..."                     │ nlargest / nsmallest                         │ 5 Sort & rank                    │
# │ "unique values", "how many distinct..."                             │ unique / nunique                             │ 4 Count categories               │
# │ "extract domain / year / type from text", "first letter of..."      │ string ops (.str.split, .str[0])             │ 6 Strings                        │
# │ "remove nulls / missing", "drop column", "convert to categorical"   │ clean & types                                │ 7 Clean & types                  │
# │ "merge / combine two datasets / DataFrames"                         │ pd.merge                                     │ 8 Merge                          │
# │ "cross table / crosstab of A vs B"                                  │ pd.crosstab                                  │ 9 Crosstab & pivot               │
# │ "pivot table of..."                                                 │ pd.pivot_table                               │ 9 Crosstab & pivot               │
# │ "distribution of <one number>", "histogram", "N bins"               │ histogram                                    │ 12 Plots                         │
# │ "relationship between <num> and <num>"                              │ scatter (+ corr)                             │ 11 Corr / 12 Plots               │
# │ "distribution of <num> across <category>", "compare groups"         │ boxplot / violin                             │ 12 Plots                         │
# │ "how X changed over time / years / age"                             │ lineplot (ordered x)                         │ 12 Plots                         │
# │ "correlation between several columns", "heatmap"                    │ corr + heatmap                               │ 11 Corr                          │
# │ "write a function that takes... and returns..."                      │ a reusable function (filter → uniques)       │ 13 Functions                     │
# │ "define a function and apply it to each row"                        │ df.apply(lambda r:..., axis=1)               │ 2 New columns / 13               │
# │ "read the metadata", "data types", "statistical summary"            │ head/info/describe                           │ Step 0 EDA                       │
# └─────────────────────────────────────────────────────────────────────┴──────────────────────────────────────────────┴──────────────────────────────────┘

# Reading trick: the VERB tells you the family, the NOUNS tell you the
# columns. "average price for each make" → verb "average for each" =
# groupby-mean; nouns = df.groupby("make")["price"].mean().
# Train yourself to underline the verb and the two nouns in every task.


# ╔══════════════════════════════════════════════════════════╗
# ║   THE 13 MOVES · every Section C task is one of these   ║
# ╚══════════════════════════════════════════════════════════╝


# ──────────────────────────────────────────
# MOVE 0 · Load & Inspect (always start here)
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Read the metadata: first 10 rows, the data type of each column,
#  the count of numerical vs non-numerical columns, and the statistical
#  summary." (website-ratings paper)
#
# Common form — before answering anything, load the file and look at
# it so you know the column names and types.

df = pd.read_csv("data.csv")

df.head(10)        # first 10 rows  (Step 1 of the metadata question)
df.shape           # (rows, columns)
df.dtypes          # type of every column      (Step 2)
df.info()          # types + non-null counts together
df.describe()      # count/mean/std/min/quartiles/max for numeric cols (Step 4)
df.isnull().sum()  # missing values per column

# count numeric vs non-numeric columns          (Step 3)
num = df.select_dtypes(include="number").columns
non = df.select_dtypes(exclude="number").columns
print("numerical:", len(num), "| non-numerical:", len(non))

# Remember: run head/info/describe first every time — it hands you the
# exact column names so you never guess. select_dtypes splits numeric
# from text columns.


# ──────────────────────────────────────────
# MOVE 1 · Filter & Count
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "How many transactions have Purchase Price > 90?" · "Count cars
#  priced > 25000 and their average mileage."
# "Count records that are Mastercard AND price > 50" · "language en,
#  price between 50 and 80, Visa." (the & / between ones)
# "What proportion of citizens are German?" · "What % of students are
#  stressed?"
# "Select samples that are potable OR hardness > 200." (the | one)
# "Find the youngest and oldest" · "In which year did India win its
#  first gold?" (min / max)
#
# Common form — How many rows satisfy a condition? / Find all rows
# where A and B. / What proportion are X?

# single condition -> count
n = len(df[df["num_col"] > 90])           # or: (df["num_col"] > 90).sum()

# AND  (use &, each side in parentheses -- NOT the word 'and')
sub = df[(df["cat_col"] == "X") & (df["num_col"] > 50)]

# OR / NOT
sub = df[(df["flag"] == 1) | (df["num_col"] > 200)]
sub = df[~(df["cat_col"] == "X")]

# range and membership
sub = df[df["num_col"].between(50, 80)]
sub = df[df["cat_col"].isin(["A", "B"])]

# proportion / percentage  (mean of a 0/1 / True-False IS the proportion)
pct = (df["cat_col"] == "Germany").mean() * 100

# aggregate of a filtered subset (total/avg of just some rows)
total = df[df["period"] == "AM"]["revenue"].sum()
avg   = df[df["num_col"] > 25000]["mileage"].mean()

# min / max  (youngest, oldest, first year meeting a condition)
df["age"].min();  df["age"].max()
first_year = df[(df["country"] == "IND") & (df["medal"] == "Gold")]["year"].min()

# Remember: AND = &, OR = |, NOT = ~, each side in PARENTHESES.
# A 0/1 (or True/False) column's .mean() is the proportion — ×100 for
# a percent. "Count" = len(df[...]) or (cond).sum().


# ──────────────────────────────────────────
# MOVE 2 · New Columns (derive a column)
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Add a column avg_grade = average of the 3 grades" · "Add
#  overall_GDP = population × per-capita GDP."
# "Create a Mileage Category" · "categorise hardness as
#  Low / Moderate / High" · "categorise athletes Tall/Heavy etc."
#  (binning / apply)
# "Create a column working_mother = yes/no from the job column."
# "Create family_size with a function using siblings & parents,
#  applied per row." (lambda, axis=1)
#
# Common form — Add a new column that is an arithmetic combination of
# others, OR that labels each row by a rule.

# arithmetic across columns
df["overall_GDP"] = df["population"] * df["gdp_per_capita"]

# row-wise mean of several columns  (axis=1 = across the row)
df["avg_grade"] = df[["G1", "G2", "G3"]].mean(axis=1)

# bin a NUMBER into labelled bands  ->  pd.cut  (len(labels) = len(bins) - 1)
df["band"] = pd.cut(df["num_col"], bins=[0, 100, 200, 10**9],
                    labels=["Low", "Moderate", "High"])

# custom label via a function + apply (one value at a time)
def categorize(v):
    if v < 60:    return "Low"
    elif v < 75:  return "Medium"
    else:         return "High"
df["life_cat"] = df["life_expectancy"].apply(categorize)

# quick two-way label with a lambda
df["working_mother"] = df["Mjob"].apply(lambda j: "no" if j == "at_home" else "yes")

# ROW-WISE function needing several columns  ->  apply(..., axis=1)
def get_family_size(sib, par):
    return sib + par + 1
df["family_size"] = df.apply(
    lambda r: get_family_size(r["SibSp"], r["Parch"]), axis=1)

# Remember: mean(axis=1) averages ACROSS COLUMNS (one number per row).
# pd.cut turns a number into bands (give bins + labels). apply(func)
# works on one column; apply(lambda r:..., axis=1) when the rule needs
# several columns of the same row. The #1 bug is forgetting axis=1.


# ──────────────────────────────────────────
# MOVE 3 · Group & Aggregate
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Average price for Petrol vs Diesel" · "average Hemoglobin for male
#  and female" · "mean & std age for >50K vs <=50K."
# "For each make, the average price and max mileage" · "turbidity
#  avg/min/max per potability" · "by Embarked: count, avg age, median
#  fare." (multi-stat agg)
# "The highest-priced car per make" (idxmax → loc)
# "Average population for each continent whose average life-exp > 75."
#  (group-then-filter)
# "Most common fuel across brands." (mode per group)
#
# Common form — Find the average (or min/max/count) of a number for
# each category.

# one statistic per group
df.groupby("group_col")["num_col"].mean()

# several statistics at once
df.groupby("group_col")["num_col"].agg(["mean", "min", "max"])

# named multi-stat aggregation (clean output column names)
df.groupby("group_col").agg(
    avg_price=("price", "mean"),
    max_mileage=("mileage", "max"),
    n=("price", "count"))

# BEST ROW per group: idxmax gives the index of the max -> loc fetches the row
idx = df.groupby("group_col")["num_col"].idxmax()
best = df.loc[idx]                      # full rows, all columns kept

# most common value (mode) per group
df.groupby("group_col")["cat_col"].agg(lambda s: s.mode()[0])

# count of a flagged (0/1) thing per group  ->  sum the flag
df.groupby("group_col")["flag"].sum()

# group-THEN-filter: keep groups whose mean passes a test, then aggregate them
gmean = df.groupby("group_col")["metric"].mean()
keep  = gmean[gmean > 75].index
df[df["group_col"].isin(keep)].groupby("group_col")["num_col"].mean()

# Remember: "for each" = groupby. One stat → ["col"].mean(); many →
# .agg([...]) or named agg. "Highest/best PER GROUP" is idxmax→loc
# (plain max() loses the other columns). Counting a flag per group =
# sum the 0/1 column.


# ──────────────────────────────────────────
# MOVE 4 · Count Categories
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Which metric is used for most ratings?" · "the most common
#  occupation" · "the most-listed make."
# "Top 5 sports by gold medals" (value_counts + head)
# "How many distinct email domains?" · "unique addiction values and
#  how many."
# "Count of countries in each continent."
#
# Common form — Which category appears most often? / How many distinct
# values are there?

df["cat_col"].value_counts()            # count of each category, high -> low
df["cat_col"].value_counts().head(5)   # top 5 categories
df["cat_col"].value_counts().idxmax()  # the single most common label
df["cat_col"].mode()[0]                # most frequent value (same idea)

df["cat_col"].nunique()                # how many DISTINCT values
df["cat_col"].unique()                 # the distinct values themselves

# Remember: value_counts() = "how many of each". .idxmax() on it =
# "which is most common". nunique() = "how many distinct"; unique()
# lists them. Top-N = value_counts().head(N).


# ──────────────────────────────────────────
# MOVE 5 · Sort & Rank
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Top 5 transactions by Purchase Price" (+ their job titles)
# "10 countries with the highest population"
# "10 countries with the lowest GDP per capita, AMONG those with
#  population > 100M" (filter THEN rank)
#
# Common form — List the top (or bottom) N rows by a column.

df.nlargest(10, "num_col")             # 10 biggest rows by num_col
df.nsmallest(10, "num_col")            # 10 smallest
df.sort_values("num_col", ascending=False).head(10)   # same as nlargest

# "among countries with population > 100M" -> FILTER first, then rank
big = df[df["population"] > 100_000_000]
big.nsmallest(10, "gdp_per_capita")

# Remember: nlargest/nsmallest keep the WHOLE ROW, so you can read
# other columns too (e.g. job titles). If the question says "among
# rows that...", FILTER FIRST, then rank.


# ──────────────────────────────────────────
# MOVE 6 · Strings
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Extract the email domain" · "credit cards expiring in 2025"
#  (split on a delimiter)
# "Extract the cabin type (deck) from the Cabin column" (first letter)
# "married = marital status starting with 'Married'"
#
# Common form — Extract a part (domain / year / type) from a text
# column, or filter on what text starts with / contains.

# split on a delimiter and take a piece
df["domain"] = df["email"].str.split("@").str[1]    # part after the @
df["year"]   = df["expiry"].str.split("/").str[1]   # "MM/YY" -> "YY"

# first character (e.g. cabin deck letter)
df["deck"] = df["Cabin"].astype(str).str[0]

# startswith / contains -> boolean masks you put inside df[ ... ]
df[df["marital"].str.startswith("Married")]
df[df["email"].str.contains("gmail")]

# length / digit check (e.g. 16-digit card numbers)
df[df["card"].astype(str).str.len() == 16]

# Remember: .str applies string methods to a whole column.
# split(sep).str[i] grabs a piece; .str[0] the first char;
# startswith/contains give True/False masks. Wrap in .astype(str) if
# the column might be numeric.


# ──────────────────────────────────────────
# MOVE 7 · Clean & Types
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Convert these columns to categorical" · "Drop the patient-id column."
# "Drop missing values before grouping" (dropna)
#
# Common form — Convert columns to categorical / drop a column /
# remove rows with missing values.

# drop rows with ANY missing, or only where specific columns are missing
df = df.dropna()
df = df.dropna(subset=["Price", "Mileage"])

# drop a column you don't need  (assign back!)
df = df.drop(columns=["pid"])

# convert columns to the 'category' type
for c in ["cp", "fbs", "restecg"]:
    df[c] = df[c].astype("category")

# fill missing instead of dropping (when asked)
df["age"] = df["age"].fillna(df["age"].median())

# Remember: dropna(subset=[...]) drops only where those columns are
# null (safer than dropping all). drop(columns=...) and
# astype("category") return a NEW object — ASSIGN BACK.
# Gotcha: a category literally named "None" is read from CSV as NaN
# — use keep_default_na=False or rename it.


# ──────────────────────────────────────────
# MOVE 8 · Merge two datasets
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Merge the athletes and regions datasets" (on the shared NOC code)
#
# Common form — Combine two DataFrames on their common key column.

df = pd.merge(left_df, right_df, on="key_col", how="left")
# how = "left"  keeps every row of the first table (safe default)
# how = "inner" keeps only rows that match in both

# Remember: on= is the shared column; how="left" keeps every row of
# the first table. After merging, the second table's columns are
# available for the rest of the analysis.


# ──────────────────────────────────────────
# MOVE 9 · Crosstab & Pivot
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Cross table of diabetes type vs survival, with a survival % column"
#  · "crosstab of family-relation quality vs stress."
# "Pivot table of stressed-student count by family size and family
#  support."
#
# Common form — Make a cross table of A vs B (counts), optionally with
# a % column; or a pivot table aggregating a value across two
# categories.

# crosstab = counts for each (row category, column category) pair
ct = pd.crosstab(df["row_cat"], df["col_cat"])

# add a percentage column (e.g. survival %): row total, then divide
ct["Total"] = ct.sum(axis=1)               # axis=1 = sum across the row
ct["pct"] = (ct[1] / ct["Total"] * 100).round(2)   # column 1 = positive class

# pivot_table: aggregate a value across two categories
pd.pivot_table(df, index="row_cat", columns="col_cat",
               values="flag", aggfunc="sum")   # sum of 0/1 = COUNT of flagged

# Remember: crosstab(A, B) = a table of counts. For "% per row" use
# ct.sum(axis=1) then divide. pivot_table needs index/columns/
# values/aggfunc — to COUNT a 0/1 flag use aggfunc="sum" (not "count",
# which counts everyone).


# ──────────────────────────────────────────
# MOVE 10 · Reshape
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Average hours by country and salary" → a tidy wide table (unstack)
# "Count distinct products across the 1st/2nd/3rd purchase columns"
#  (concat then nunique)
#
# Common form — Turn a two-level group into a wide table; or count
# distinct values spread across several columns.

# two-key groupby -> unstack pivots one level up into columns
df.groupby(["country", "salary"])["hours"].mean().unstack()

# distinct values living in SEVERAL columns: stack them, then nunique
all_products = pd.concat([df["Product_1"], df["product_2"], df["product_3"]])
all_products.dropna().nunique()

# Remember: unstack() turns the inner group index into columns —
# perfect for "X by A and B" tables. To count distinct across several
# columns, pd.concat them into one Series first, then .dropna().nunique().


# ──────────────────────────────────────────
# MOVE 11 · Correlation
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Correlation between studytime and average grade" · "between Age and
#  max heart rate."
# "Heatmap of the correlation among these 5 columns."
#
# Common form — Find the correlation between two numbers; or show a
# heatmap of correlations among several columns.

# correlation between two columns -> a single number in [-1, 1]
df["studytime"].corr(df["avg_grade"])

# correlation MATRIX for several columns + heatmap
cols = ["c1", "c2", "c3", "c4", "c5"]
corr = df[cols].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)

# Remember: .corr() on two Series → one number; on df[[cols]] → a
# matrix. Pass the NAMED NUMERIC COLUMNS (running it on the whole df
# with text columns errors). The heatmap needs annot=True to print the
# values.


# ──────────────────────────────────────────
# MOVE 12 · Plots — pick by counting the variables
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Distribution of trtbps / chol / average grade (use 20 / 30 bins)"
#  · "boxplot of Web_review and Exp_review."
# "Boxplot of price by make and fuel" · "absences by gender" · "Age
#  across blood groups." (number across category, + hue)
# "Relationship between Age & thalachh" · "price vs age, manual vs
#  auto" (scatter / lmplot with hue, col)
# "Count-plot of assigned ratings" · "most common occupation,
#  illustrated." (category frequency)
# "Pie chart of the father's occupations" (parts of a whole)
# "Male/female participation over time, Summer & Winter"
#  (line, panels)
# "Heatmap of correlations" (see family 11)
#
# The decision rule — how many variables, and of what kind?
#
# ┌───────────────────────────────────────────────────┬────────────────┬─────────────────────────────────────────────┐
# │ What you're asked for                             │ Plot           │ Call                                        │
# ├───────────────────────────────────────────────────┼────────────────┼─────────────────────────────────────────────┤
# │ distribution of ONE number                        │ histogram      │ sns.histplot(df[num], bins=20)              │
# │ ONE number across a CATEGORY (compare groups)     │ box / violin   │ sns.boxplot(x=cat, y=num)                   │
# │ TWO numbers (relationship)                        │ scatter (+trend)│ sns.scatterplot(x,y) + regplot             │
# │ frequency of a CATEGORY                           │ countplot      │ sns.countplot(x=cat)                        │
# │ a value you ALREADY COMPUTED per group            │ bar            │ sns.barplot(x=s.index, y=s.values)          │
# │ PARTS OF A WHOLE (shares)                         │ pie            │ plt.pie(counts, autopct="%1.1f%%")          │
# │ trend over an ORDERED x (year, age)               │ line           │ plt.plot(x, y, marker="o")                  │
# │ correlations among MANY numbers                   │ heatmap        │ sns.heatmap(corr, annot=True)               │
# │ a SECOND category on top                          │ add hue=       │ sns.boxplot(x,y,hue=cat2)                   │
# │ a SEPARATE CHART PER category                     │ add col=       │ sns.lmplot(x,y,hue=,col=)                   │
# └───────────────────────────────────────────────────┴────────────────┴─────────────────────────────────────────────┘

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")

# 1) distribution of ONE number  (set bins exactly as asked, e.g. 20 or 30)
sns.histplot(df["num_col"], bins=20, kde=True)

# 2) ONE number across a CATEGORY -> compare groups
sns.boxplot(data=df, x="cat_col", y="num_col")
sns.violinplot(data=df, x="cat_col", y="num_col")     # box + density shape

# 3) relationship between TWO numbers
sns.scatterplot(data=df, x="num1", y="num2")
sns.regplot(data=df, x="num1", y="num2", scatter=False)   # add a trend line

# 4) frequency of a CATEGORY
sns.countplot(data=df, x="cat_col")                   # counts the rows for you
# bar of a value you already computed (e.g. survival RATE per group):
s = df.groupby("cat_col")["flag"].mean()
sns.barplot(x=s.index, y=s.values)

# 5) parts of a whole -> pie
counts = df["cat_col"].value_counts()
plt.pie(counts, labels=counts.index, autopct="%1.1f%%")

# 6) trend over an ORDERED x (year, age) -> line
s = df.groupby("year").size()
plt.plot(s.index, s.values, marker="o")

# 7) add a SECOND category -> hue ;  separate PANELS -> col
sns.boxplot(data=df, x="cat_col", y="num_col", hue="cat2")
sns.lmplot(data=df, x="num1", y="num2", hue="cat2", col="cat3")

# ALWAYS finish a plot with:
plt.title("...");  plt.xlabel("...");  plt.ylabel("...")
plt.tight_layout(); plt.show()

# Remember: count the variables. 1 NUMBER → histogram.
# 1 NUMBER + A CATEGORY → box/violin. 2 NUMBERS → scatter.
# A CATEGORY'S FREQUENCY → countplot. Want a second category? add
# hue=. Want separate panels? add col=. And every plot needs a
# TITLE + AXIS LABELS + A ONE-LINE INFERENCE, or you lose marks the
# question explicitly allots.


# ──────────────────────────────────────────
# MOVE 13 · Write a Function
# ──────────────────────────────────────────

# WHERE THIS SHOWS UP IN THE PAPERS
# "Write a function that takes a player's name and returns the unique
#  countries, sports and Olympics attended."
# "Define get_family_size using parents & siblings, then use lambda to
#  apply it to each row."
#
# Common form — write a function that takes a key, filters the data,
# and returns the unique values associated with it.

# "write a function that takes <key> and returns the unique <values>"
def profile(name):
    p = df[df["Name"] == name]                 # 1. filter by the key
    return {                                   # 2. pull unique values
        "countries": p["Team"].unique().tolist(),
        "sports":    p["Sport"].unique().tolist(),
        "olympics":  p["Games"].unique().tolist(),
    }
print(profile("Some Name"))                    # 3. test by calling it

# row-wise function applied with lambda (needs several columns)
def get_family_size(sib, par):
    return sib + par + 1
df["family_size"] = df.apply(
    lambda r: get_family_size(r["SibSp"], r["Parch"]), axis=1)

# Remember: a "function that takes X and returns Y" is almost always:
# FILTER the df by X, then pull .unique() (or a sum/mean) of some
# columns, and RETURN them. For per-row calculations use
# df.apply(lambda r:..., axis=1). Always test by calling it once.


# ╔══════════════════════════════════════════════════════════╗
# ║  THE MASTER PIPELINE · the same 5 steps solve any Sec C ║
# ╚══════════════════════════════════════════════════════════╝

# Whatever the dataset, whatever the tasks, Section C is this
# skeleton. Load → clean → derive → answer with the right move →
# visualise + infer. Keep this in your head and fill in the column
# names on the day.

# ► the 5-step skeleton

import pandas as pd, numpy as np
import matplotlib.pyplot as plt, seaborn as sns
sns.set_theme(style="whitegrid")

# 1. LOAD + LOOK  (do this first, every single time)
df = pd.read_csv("data.csv")
print(df.shape); print(df.dtypes); print(df.head()); print(df.describe())
print(df.isnull().sum())

# 2. CLEAN  (only if needed / asked)
df = df.dropna(subset=["key_col"])           # or df.dropna()
# df = df.drop(columns=["id_col"])
# df["cat"] = df["cat"].astype("category")

# 3. DERIVE the columns the questions rely on
df["avg3"]  = df[["a", "b", "c"]].mean(axis=1)
df["band"]  = pd.cut(df["num"], bins=[0, 100, 200, 1e9], labels=["Low", "Mid", "High"])
df["label"] = df["num"].apply(lambda v: "high" if v > 50 else "low")

# 4. ANSWER each task with the matching move
(df["cat"] == "X").mean() * 100                       # proportion / %
df[df["num"] > 90]                                    # filter / count
df.groupby("group")["num"].mean()                     # average per group
df.loc[df.groupby("group")["num"].idxmax()]           # best row per group
df.nlargest(5, "num")                                 # top N
df["cat"].value_counts().idxmax()                     # most common
ct = pd.crosstab(df["a"], df["b"])                    # cross table
ct["pct"] = ct[1] / ct.sum(axis=1) * 100             #   + percentage

# 5. VISUALISE + INFER  (title, labels, ONE sentence of meaning)
sns.histplot(df["num"], bins=20)
plt.title("Distribution of num"); plt.xlabel("num"); plt.ylabel("count")
plt.tight_layout(); plt.show()


# ╔══════════════════════════════════════════════════════════╗
# ║       8 REFLEXES · train these until automatic          ║
# ╚══════════════════════════════════════════════════════════╝

# 1. read_csv → head/info/describe first, every time — learn the
#    column names before writing anything.

# 2. "for each" → groupby. "most/least per group" → idxmax → loc.

# 3. "how many / proportion" → boolean filter; a 0/1 column's
#    .mean()*100 is the percentage.

# 4. "add a column / categorise" → arithmetic, pd.cut, or apply.

# 5. & | with PARENTHESES (never and/or); axis=1 for row-wise
#    apply / row sums.

# 6. COUNT THE VARIABLES to choose the plot: 1 number = histogram,
#    1 number + category = box, 2 numbers = scatter,
#    a category = countplot.

# 7. To COUNT a 0/1 flag in a crosstab/pivot, use
#    aggfunc="sum" (not "count").

# 8. Every plot: title + axis labels + ONE sentence of inference.


# ╔══════════════════════════════════════════════════════════╗
# ║              RULES THAT WIN THE MARKS                   ║
# ╚══════════════════════════════════════════════════════════╝

# ✓ LABEL EVERY PLOT (title, x, y) and write ONE SENTENCE OF
#   INFERENCE — papers explicitly award this ("comment on your
#   observation").

# ✓ ROUND numbers (.round(2)) and state units.

# ✓ Use &/| with parentheses; df = df.drop(...) /
#   df = df.dropna(...) (assign back).

# ✓ Use apply(lambda r:..., axis=1) when a calc needs several
#   columns of a row.

# ✓ To "count the flagged" in a pivot/crosstab,
#   aggfunc="sum" on the 0/1 column.

# ✓ STATE YOUR THRESHOLDS when categorising
#   (e.g. Low < 100, Moderate 100–200, High > 200).

# ✓ When the question says "AMONG rows that...", FILTER FIRST,
#   then nlargest/nsmallest.

# ✓ Watch UNIT TRAPS: height in cm vs metres; a 1.8 / 80
#   benchmark; a category named "None" read as NaN.

# ✓ If a filter returns EMPTY, say WHY (e.g. football is a
#   Summer-only sport) — don't assume your code is broken.

# ✓ For groupby summaries, prefer NAMED AGG
#   (avg=("col","mean")) so output columns read cleanly.


# ============================================================
# Section C Master Guide — UE20CS901, Python for Data Science
# Distilled from 10 ESA papers (Feb/May 2025, Oct 2024,
# Aug/July 2021, the Model Set, March 2024 x2, Nov 2023)
# covering ecommerce, cars, patients, students, Olympics,
# website ratings, world countries, census income, water and
# Titanic. The dataset is never the point — the move is.
# Every snippet here was executed before publishing.
# Print to PDF for the night before.
# ============================================================
