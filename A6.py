# ==============================================================================
# TOPIC 19: Most Important Topics
# ==============================================================================

"""
How to read this page
Section A — 1-mark questions
Section B — Q2/Q3 patterns
Section C — big questions
Topic frequency table
Hot-10 topics for ESA
Common traps & mistakes
3-day final revision plan
How to read this page
I went through every Section-A, Section-B, and Section-C question across 8 ESA papers (, ML-1 Sample, Nov 2021, Aug 2023, , Nov 2024, Feb 2025, ) and counted
how often each topic appeared. The result is a ranked list of topics that actually show up,
not just topics that look important in a textbook.
The big lesson — six topics dominate Section A. If you master them, you nearly
always score 4–5 out of 5 on Section A. The rest comes from Sections B and C, where everyone
loses marks on careful reading.
Section A — five 1-mark questions (5 marks total)
Section A is five short questions , often labelled 1a, 1b, 1c, 1d, 1e.
Each is 1 mark. They mostly test:
One-line definitions ("Define multicollinearity")
One-line "why" answers ("Why use VIF?")
Quick numerical readings of OLS output
True/False with one-line justification
What appeared in Section A across 8 papers
Topic
Times asked
Papers
LR Assumptions (LINER)
Mar21, Sample, Aug23, May25, Mar24
Multicollinearity / VIF
Sample, Aug23, Mar24, (Nov24)
Bias–Variance / Overfitting
Sample, Aug23, Mar24, May25
Cross-Validation
Aug23, Mar24, May25
Forward / Feature Selection
Aug23, Mar24, Feb25
Regularization (Ridge/Lasso/EN)
Nov21 (×2), Feb25, May25
Evaluation Metrics (R², RMSE, p-value)
Nov21 (×3), Feb25, May25
Hyperparameter Tuning (Grid/Random/Bayes)
Feb25, (other)
Numerical reading of regression coefficients
Mar21 (×3 — bwght, gpa, ceo)
Pattern — almost every paper has at least one Section A from each of these three
buckets: (1) an assumption / theory question , (2) a multicollinearity or
overfitting question , (3) a numerical or metric question .
Section B — Q2 and Q3 (15 marks total)
Q2 (8 marks) is almost always about DataFrame operations / pandas —
load data, drop columns, group-by, slice, head/tail, info, describe. You write small code
snippets or describe what each line does.
Q3 (7 marks) is EDA — Exploratory Data Analysis : plot the data,
boxplots, pairplots, correlation heatmap, identify outliers, comment on skewness.
Question
Marks
Almost always asks for…
Q2
pandas operations on a CSV — read_csv, head, info, describe, drop, group-by, value_counts
Q3
EDA — visualisations, missing values, outliers, comment on distribution
Strategy: learn the 10 most common pandas one-liners (see File 20: Python Pipeline ) and you can answer Q2 confidently.
For Q3, remember the EDA recipe: SHAPE → HEAD → INFO → DESCRIBE → MISSING → BOX → CORR .
Section C — Q4, Q5, Q6 (60 marks total — the bulk of the paper)
Section C is where most marks live, and it has a very predictable structure.
Question
Marks
Theme
Q4
Pre-modelling pipeline : missing values, outliers, encoding, scaling, train/test split, multicollinearity check (VIF), feature transformations, feature selection
Q5
OLS / linear regression model building : fit OLS, read summary, check assumptions, residual diagnostics, interpret coefficients
Q6
Model comparison and tuning : build multiple models (Linear, Ridge, Lasso, ElasticNet, Polynomial), compare with R²/RMSE, hyperparameter tuning (GridSearch / RandomSearch / Bayesian), final business interpretation
Q4 sub-parts that appear almost every paper
4j: feature scaling (StandardScaler / MinMaxScaler)
4k: train/test split
Q5 sub-parts
Fit OLS using statsmodels, print summary
Identify significant variables (p-value < 0.05)
Check assumptions: linearity, normality of residuals, homoscedasticity, independence
Compute and interpret R², Adjusted R², F-statistic
Residual plots — Q-Q plot, residuals vs fitted
Q6 sub-parts
Compare Linear vs Ridge vs Lasso vs ElasticNet
Use cross-validation (k-fold, k=5 or 10) to evaluate
Apply GridSearchCV / RandomizedSearchCV for tuning alpha
Interpret final model in business terms
The 70% rule — if you can confidently do Q4 (preprocessing) and Q5 (OLS + assumptions),
you have already secured 40+ marks out of 60 in Section C. That's the difference between failing and
a B grade.
Topic frequency table — overall
Across all 8 papers, all sections combined, here is how often each topic was tested:
Rank
Topic
Approx times asked
Total marks across papers
Pandas / DataFrame operations
8 (every paper)
~64 marks
OLS Regression + Summary interpretation
~120 marks
Multicollinearity & VIF
~30 marks
Assumptions of LR (LINER)
~25 marks
Regularization (Ridge / Lasso / ElasticNet)
~80 marks
Cross-validation
~20 marks
EDA & data visualisations
~56 marks
Bias-Variance / Overfitting
~15 marks
Feature engineering / transformations
~30 marks
Feature selection (Forward / RFE / Wrapper)
~15 marks
Hyperparameter tuning (Grid/Random/Bayes)
~30 marks
Evaluation metrics (R², RMSE, MAPE, MAE)
~25 marks
Outlier detection (IQR / boxplot)
~20 marks
Encoding (one-hot, label, ordinal)
~20 marks
Numerical reading of regression coefficients
~16 marks
Polynomial regression
~15 marks
Gradient descent
~5 marks
The Hot-10 — concepts you must NOT skip
If you have only a few days, master these ten topics. Together they cover ~80% of all marks.
Topic
Why it's hot
Where to study
OLS regression + statsmodels summary
Q5 every paper, 20 marks; you must read p-values, R², coefficients
File 02 , File 13
Multicollinearity & VIF
File 08
LINER assumptions
1-mark Section A almost every paper + appears in Q5
File 07
Ridge / Lasso / Elastic Net
20 marks in Q6 every paper; 1-mark in Section A repeatedly
File 10
Cross-validation (k-fold)
Section A + appears in Q6 tuning
File 11
Pandas one-liners
Q2 every paper; 8 marks each
File 20
EDA recipe
Q3 every paper; 7 marks each
File 20
Outlier handling + Encoding + Scaling
Q4 every paper; 10–15 marks each
File 15
R², Adjusted R², RMSE, p-value reading
1-mark and Section C interpretation
File 12
Hyperparameter tuning (GridSearchCV)
Q6 part of Section C
File 16
Hot-10 mnemonic — "OMLR-CPE-OEH":
O LS · M ulticollinearity · L INER · R egularization · C V · P andas · E DA · O utliers/Encoding/Scaling · E valuation metrics · H yperparameters
Common traps that lose marks
Several mistakes appear again and again in how students answer ESA questions. Avoid these and
you'll score noticeably higher with the same knowledge.
Trap
What goes wrong
The fix
Comparing RMSEs across different targets
Says "model A is better because RMSE 55 < RMSE 12324" when the targets are age vs CTC
RMSE has same units as target. Different targets → not comparable. Use %RMSE / mean target instead.
Dummy-variable trap
One-hot encodes a 3-level category and creates 3 columns → causes multicollinearity
Always use drop_first=True in pd.get_dummies or drop="first" in OneHotEncoder
Treating ordinal as nominal
One-hot encodes "Low/Medium/High" instead of mapping 1/2/3
Use OrdinalEncoder when an order exists; one-hot when it doesn't
Scaling before train/test split
Fits scaler on full data → information leak from test set
Split first, then fit_transform on train only, transform on test
Imputing on whole dataset
Same data leak as above
Fit imputer on train only
R² always means "good model"
High R² on training is meaningless if test R² is much lower (overfit)
Always report Adjusted R² and a held-out / CV score, not just train R²
p-value > 0.05 means "no relationship"
Says "x has no effect on y"
Better: "with this data, we fail to reject H₀; we don't have evidence of a non-zero effect"
Confusing VIF threshold
Uses VIF > 0.05 (mixing it up with p-value)
VIF > 5 is a warning, > 10 is serious. Range starts at 1, no upper limit.
Ridge "selects features"
Says Ridge does feature selection like Lasso
Ridge shrinks coefficients toward zero but rarely to zero. Lasso can. Elastic Net does both.
Forgetting to scale before Ridge/Lasso
Penalty is dominated by features with large units (e.g. salary in lakhs vs age in years)
Always StandardScale features before any regularised regression
Using R² to compare different-sized feature sets
R² always increases when you add features
Use Adjusted R² or held-out RMSE for comparison
"Linear regression assumes the data is linear"
Vague phrasing
It assumes a linear relationship between predictors and target , in the chosen form. You can include polynomial or log terms and still call it "linear regression".
3-day final revision plan
If you have only 3 days before the ESA, here is a tight schedule:
Morning: File 01 + File 02 + File 03
Afternoon: File 07 (LINER) + File 08 (VIF) + File 09
Evening: File 10 (Ridge/Lasso/EN) + File 11 + File 12
Last hour: re-read File 18 Section-A questions only — do them on paper.
Morning: File 17 — work through every numerical with pen on paper
Afternoon: File 13 + File 14 + File 15 + File 16
Evening: File 20 — write out the full pandas + sklearn pipeline 2 times from memory
Morning: pick the latest paper () from File 18 and attempt it timed (3 hours)
Afternoon: review answers, list weaknesses
Night before: re-read File 21 (Cheatsheet) only — high-yield mnemonics, formulas, one-liners
The night before — DO NOT learn anything new. Just re-read File 21 (cheatsheet),
sleep 7+ hours. Tired brains forget things faster than well-rested ones.
"""


# ==============================================================================
# TOPIC 20: Python Pipeline
# ==============================================================================

"""
Step 0 — Imports
Step 1 — Load data (Q2)
Step 2 — EDA (Q3)
Step 3 — Missing values (Q4)
Step 4 — Outlier handling (Q4)
Step 5 — Encoding (Q4)
Step 6 — Scaling (Q4)
Step 7 — Train/test split (Q4)
Step 8 — Multicollinearity / VIF (Q4)
Step 9 — Feature selection (Q4)
Step 10 — OLS / statsmodels (Q5)
Step 11 — Assumption checks (Q5)
Step 12 — Model comparison (Q6)
Step 13 — Hyperparameter tuning (Q6)
Step 14 — Final interpretation (Q6)
Quick snippets cheatsheet
How to use this file
This is the full pipeline for any regression Section C question. The order
matches how Q4 → Q5 → Q6 are structured in the ESA. You can literally read this top-to-bottom
during the exam and answer most questions.
Every section has:
What this step does (one paragraph in plain English)
The code with comments on every line
What the output looks like
How to read it for the exam
Memorize the order, not the syntax. If you remember the 14 steps in sequence,
you'll never blank during a Section C question. The exact pandas function name can be looked up.
Step 0 — Imports (always at the top)
Standard imports for every regression task. Memorize these — they appear in every Section C answer.
Step 1 — Load data (Q2 territory)
Goal: read the CSV, get a feel for size and types, look at a few rows.
This is exactly what Q2 (8 marks) tests.
EDA recipe (Q3, 7 marks) — the standard 7-step exploratory approach is SHAPE → HEAD → INFO → DESCRIBE → MISSING → BOX → CORR .
Step 2 — Exploratory Data Analysis (Q3, 7 marks)
Goal: visually understand the data. Find skewness, outliers, relationships.
Step 3 — Missing values (Q4 sub-part)
Goal: find missing entries and decide how to handle them.
Trap: if you fill missing values before train/test split, you leak info
from the test set into the train set. Always split first, then impute on train, then apply the
same imputer to test.
Step 4 — Outlier detection & treatment (Q4 sub-part)
Goal: find rows whose values lie way outside the normal range. Decide whether
to drop, cap, or transform.
Step 5 — Encoding categoricals (Q4 sub-part)
Goal: ML models need numbers. Convert text categories into numeric form.
Trap (dummy-variable trap): if a category has k levels and you create k dummies, they sum to 1 → perfect multicollinearity. Always drop one level.
Step 6 — Feature scaling (Q4 sub-part)
Goal: bring all features onto a comparable range. Required before
Ridge/Lasso/ElasticNet, KNN, gradient descent. Not strictly required for plain OLS.
Order matters! Always: (1) split → (2) fit scaler on train → (3) transform train,
(4) transform test. Never fit_transform on test data.
Step 7 — Train/test split (Q4 sub-part)
Step 8 — Multicollinearity / VIF (Q4 sub-part)
Goal: detect features that are too correlated with each other.
VIF > 5 is a warning, > 10 is serious. Drop or combine those features.
How to read the output:
VIF value
Meaning
No correlation with other predictors
Moderate, usually OK
High — investigate / drop
> 10
Serious multicollinearity — drop
Step 9 — Feature selection (Q4 sub-part)
Step 10 — OLS / statsmodels (Q5, 20 marks!)
This is the most important step in Section C. The summary table is the source
of half the marks in Q5.
How to read the OLS summary table (this is gold for the exam)
Field
Means
What's "good"
R-squared
% of variance in y explained
Higher is better; 0–1
Adj. R-squared
R² penalised for #features
Use this when comparing models with different feature counts
F-statistic / Prob (F)
Joint significance of all predictors
Prob < 0.05 → at least one predictor matters
coef
How much y changes per unit increase in x
Sign and magnitude tell direction and strength
std err
Uncertainty around the coefficient
Smaller is better
t
coef / std err
|t| > 2 ≈ significant
P>|t|
p-value of that coefficient
< 0.05 → significant
[0.025, 0.975]
95% confidence interval for the coef
Doesn't include 0 → significant
Durbin-Watson
Autocorrelation in residuals
~ 2 ideal; < 1.5 or > 2.5 = trouble
Jarque-Bera (JB)
Normality of residuals
Prob > 0.05 → residuals look normal
Cond. No.
Multicollinearity indicator
> 30 = warning
Step 11 — Assumption checks (Q5 sub-part)
Step 12 — Model comparison (Q6 part)
Goal: build several models, compare them with the same metric, pick the best.
Step 13 — Hyperparameter tuning (Q6 part)
Step 14 — Final business interpretation (Q6 part)
The last sub-part of Q6 typically asks for business interpretation . Use this template:
Template answer (adapt to the dataset):
State the chosen model and its CV-RMSE / R² on the test set.
Pick the 2–3 features with the largest standardised coefficients. State the direction (sign).
Translate the coefficient into a one-sentence business statement : "A 1-unit increase in area is associated with an expected ₹X change in price, holding other features constant."
Mention which features the model dropped (if Lasso) or de-emphasised (Ridge) — these are
candidates the business can de-prioritise.
State a caveat: "These are associations under the LR assumptions; not causal claims."
Quick snippets cheatsheet
Pandas one-liners
Numpy quick
Sklearn essentials
Metrics one-liners
Full pipeline in one go (paste-and-go)
If a Section C question says "build a complete regression pipeline for this dataset", here is the full skeleton in 50 lines:
You can quote-paste this 50-line skeleton in any Section C answer that says
"build a regression model end-to-end". Adjust the column names and you have all 60 marks of
Section C in front of you.
"""

# --- Code ---

# Data handling
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# sklearn — preprocessing
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer

# sklearn — models
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import RFE, SequentialFeatureSelector

# sklearn — metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_absolute_percentage_error

# statsmodels for OLS summary tables
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Set figure defaults
plt.rcParams["figure.figsize"] = (8, 5)
sns.set_style("whitegrid")

# Read the data
df = pd.read_csv("housing.csv")

# 1. Shape — how many rows × columns?
print("Shape:", df.shape)

# 2. First / last few rows
df.head()        # first 5 rows
df.tail()        # last 5 rows
df.sample(5)    # 5 random rows

# 3. Data types and non-null counts
df.info()

# 4. Numerical summary — count, mean, std, min, 25/50/75%, max
df.describe()

# 5. Categorical summary
df.describe(include="object")

# 6. Column names
df.columns.tolist()

# 7. Selecting
df["price"]                                  # single column → Series
df[["price", "area"]]                       # two columns → DataFrame
df.iloc[0:5, 0:3]                          # by position
df.loc[df["price"] > 100000]                # by condition

# 8. Group-by
df.groupby("city")["price"].mean()

# 9. Value counts (categorical)
df["city"].value_counts()

# Histogram for one feature — see the distribution shape
df["price"].hist(bins=30)
plt.title("Distribution of Price")
plt.xlabel("Price"); plt.ylabel("Frequency")
plt.show()

# All numeric features at once
df.hist(bins=30, figsize=(12,8))
plt.tight_layout(); plt.show()

# Boxplot — see outliers and quartiles
sns.boxplot(x=df["price"])
plt.show()

# Pairplot — relationships between every pair (use only when small # of features)
sns.pairplot(df[["price", "area", "bedrooms", "bathrooms"]])
plt.show()

# Correlation heatmap — find multicollinearity hints + relationships with target
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.show()

# Scatter — relationship between one feature and target
sns.scatterplot(x="area", y="price", data=df)
plt.show()

# Skewness — is the column heavily skewed (> 1 or < -1 is a flag)?
df["price"].skew()

# Count of categorical values
sns.countplot(x="city", data=df); plt.xticks(rotation=45); plt.show()

# 1. Count missing values per column
df.isnull().sum()

# Same as percentage
(df.isnull().sum() / len(df) * 100).round(2)

# 2. Visual — heatmap of missing
sns.heatmap(df.isnull(), cbar=False)

# 3. Strategies (apply ONLY to training data; never on test)

# a) Drop rows with any missing — only if very few are missing
df_clean = df.dropna()

# b) Drop columns where most values are missing (e.g. > 50%)
df = df.drop(columns=["too_many_missing_col"])

# c) Numeric — fill with median (robust to outliers)
df["area"] = df["area"].fillna(df["area"].median())

# d) Numeric — fill with mean
df["area"] = df["area"].fillna(df["area"].mean())

# e) Categorical — fill with mode (most common)
df["city"] = df["city"].fillna(df["city"].mode()[0])

# f) Use sklearn SimpleImputer (cleaner, fits on train only)
imputer = SimpleImputer(strategy="median")
df[["area", "price"]] = imputer.fit_transform(df[["area", "price"]])

# Method 1: IQR (Interquartile Range) — most common for ESA
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Boolean mask of outliers
mask_outlier = (df["price"] < lower) | (df["price"] > upper)
print("Outlier count:", mask_outlier.sum())

# Strategy A: drop them
df_no_out = df[~mask_outlier]

# Strategy B: cap (winsorize) — keep the row but clip extreme value
df["price"] = df["price"].clip(lower=lower, upper=upper)

# Method 2: Z-score (assumes near-normal distribution)
from scipy.stats import zscore
z = np.abs(zscore(df["price"]))
mask = z > 3          # > 3 sigma

# Method 3: just look — boxplot
sns.boxplot(x=df["price"])

# A) One-hot encoding — for nominal (no order) categories
# IMPORTANT: drop_first=True avoids the dummy variable trap
df = pd.get_dummies(df, columns=["city", "furnishing"],
                    drop_first=True, dtype=int)

# sklearn version (preferred in pipelines)
ohe = OneHotEncoder(drop="first", sparse_output=False)
encoded = ohe.fit_transform(df[["city"]])

# B) Ordinal encoding — when categories have a natural order (Low < Medium < High)
order = [["Low", "Medium", "High"]]
oe = OrdinalEncoder(categories=order)
df["quality_enc"] = oe.fit_transform(df[["quality"]])

# C) Manual mapping (when you know the levels)
mp = {{"yes": 1, "no": 0}}
df["has_garage"] = df["has_garage"].map(mp)

# D) Label encoding — typically for the target column only
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["target_enc"] = le.fit_transform(df["target"])

# StandardScaler — mean 0, std 1 (most common)
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)   # fit only on TRAIN
X_test_sc  = scaler.transform(X_test)        # reuse same scaler on TEST

# MinMaxScaler — squeeze into [0, 1]
mm = MinMaxScaler()
X_train_mm = mm.fit_transform(X_train)
X_test_mm  = mm.transform(X_test)

X = df.drop(columns=["price"])     # features
y = df["price"]                     # target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,        # 80% train / 20% test
    random_state=42      # reproducibility — same split every time
)

print(X_train.shape, X_test.shape)

# Add a constant column (statsmodels needs it)
X_const = sm.add_constant(X_train)

# Compute VIF for each column
vif = pd.DataFrame()
vif["feature"] = X_const.columns
vif["VIF"] = [variance_inflation_factor(X_const.values, i)
               for i in range(X_const.shape[1])]
print(vif.sort_values("VIF", ascending=False))

# Strategy: drop the column with highest VIF, recompute, repeat until all < 5
X_train = X_train.drop(columns=["highest_vif_col"])

# A) Forward Selection — add one variable at a time
sfs = SequentialFeatureSelector(
    LinearRegression(),
    n_features_to_select=5,
    direction="forward",
    scoring="r2", cv=5
)
sfs.fit(X_train, y_train)
selected = X_train.columns[sfs.get_support()].tolist()

# B) Backward Elimination — start with all, drop the worst at each step
sfs_b = SequentialFeatureSelector(
    LinearRegression(),
    n_features_to_select=5,
    direction="backward",
    scoring="r2", cv=5
)

# C) RFE — Recursive Feature Elimination
rfe = RFE(LinearRegression(), n_features_to_select=5)
rfe.fit(X_train, y_train)
selected_rfe = X_train.columns[rfe.support_].tolist()

# D) Filter — correlation with target
corr_with_target = X_train.corrwith(y_train).abs().sort_values(ascending=False)

# statsmodels — gives you a full summary table
X_const = sm.add_constant(X_train)            # add intercept column
model = sm.OLS(y_train, X_const).fit()
print(model.summary())

# Pull out individual values
model.params           # coefficients
model.pvalues          # p-values
model.rsquared         # R²
model.rsquared_adj     # Adjusted R²
model.fvalue           # F-statistic
model.f_pvalue         # p-value of F-statistic

# Predict on test
X_test_const = sm.add_constant(X_test)
y_pred = model.predict(X_test_const)

# Residuals (errors)
resid = model.resid
fitted = model.fittedvalues

# 1. Linearity & Homoscedasticity — residuals vs fitted should look random
plt.scatter(fitted, resid, alpha=0.5)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Fitted"); plt.ylabel("Residuals")
plt.title("Residuals vs Fitted")
plt.show()

# 2. Normality — Q-Q plot
sm.qqplot(resid, line="45")
plt.title("Q-Q Plot"); plt.show()

# Statistical normality test — Shapiro-Wilk
from scipy.stats import shapiro
stat, p = shapiro(resid)
# p > 0.05 → residuals look normal

# 3. Homoscedasticity formal test — Breusch-Pagan
from statsmodels.stats.diagnostic import het_breuschpagan
bp = het_breuschpagan(resid, X_const)
# bp[1] is the p-value; > 0.05 → no heteroscedasticity

# 4. Independence — Durbin-Watson
from statsmodels.stats.stattools import durbin_watson
dw = durbin_watson(resid)
# dw ≈ 2 → no autocorrelation

# 1. Linear Regression — baseline
lr = LinearRegression().fit(X_train_sc, y_train)
pred_lr = lr.predict(X_test_sc)

# 2. Ridge — L2 penalty
ridge = Ridge(alpha=1.0).fit(X_train_sc, y_train)
pred_ridge = ridge.predict(X_test_sc)

# 3. Lasso — L1 penalty (does feature selection)
lasso = Lasso(alpha=0.1).fit(X_train_sc, y_train)
pred_lasso = lasso.predict(X_test_sc)

# 4. ElasticNet — mix of L1 and L2
en = ElasticNet(alpha=0.1, l1_ratio=0.5).fit(X_train_sc, y_train)
pred_en = en.predict(X_test_sc)

# 5. Polynomial — for non-linear patterns
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train_sc)
X_test_poly  = poly.transform(X_test_sc)
poly_lr = LinearRegression().fit(X_train_poly, y_train)
pred_poly = poly_lr.predict(X_test_poly)

# Compare
def evaluate(y_true, y_pred, name):
    print(f"{{name}}")
    print(f"  R²    : {{r2_score(y_true, y_pred):.4f}}")
    print(f"  RMSE  : {{np.sqrt(mean_squared_error(y_true, y_pred)):.2f}}")
    print(f"  MAE   : {{mean_absolute_error(y_true, y_pred):.2f}}")
    print()

evaluate(y_test, pred_lr,    "Linear")
evaluate(y_test, pred_ridge, "Ridge")
evaluate(y_test, pred_lasso, "Lasso")
evaluate(y_test, pred_en,    "ElasticNet")
evaluate(y_test, pred_poly,  "Polynomial-2")

# A) GridSearchCV — exhaustive search over a grid
param_grid = {{"alpha": [0.001, 0.01, 0.1, 1, 10, 100]}}
grid = GridSearchCV(Ridge(), param_grid,
                    cv=5, scoring="neg_mean_squared_error")
grid.fit(X_train_sc, y_train)
print("Best alpha:", grid.best_params_)
print("Best CV RMSE:", np.sqrt(-grid.best_score_))
best_ridge = grid.best_estimator_

# B) RandomizedSearchCV — random sample of the grid (faster for big grids)
from scipy.stats import uniform
rs = RandomizedSearchCV(
    ElasticNet(),
    {{"alpha": uniform(0.001, 10),
     "l1_ratio": uniform(0, 1)}},
    n_iter=50, cv=5,
    scoring="r2", random_state=42
)
rs.fit(X_train_sc, y_train)
print("Best params:", rs.best_params_)

# C) Bayesian Search — smart, builds a probabilistic model of the search space
# pip install scikit-optimize
from skopt import BayesSearchCV
bayes = BayesSearchCV(
    Ridge(),
    {{"alpha": (1e-3, 1e2, "log-uniform")}},
    n_iter=30, cv=5
)
bayes.fit(X_train_sc, y_train)

# Save coefficients with feature names for interpretation
coef_df = pd.DataFrame({{
    "feature": X_train.columns,
    "coef":    best_ridge.coef_
}}).sort_values("coef", key=abs, ascending=False)
print(coef_df.head(10))

df.shape                              # (rows, cols)
df.head(); df.tail(); df.sample(5)
df.info(); df.describe()
df.isnull().sum()                     # missing per col
df.dropna(); df.fillna(0)
df["col"].mean(), .median(), .std(), .skew()
df.groupby("city")["price"].mean()
df["city"].value_counts()
df.corr(numeric_only=True)
df.sort_values("price", ascending=False)
df.drop(columns=["id"])
df.rename(columns={{"old": "new"}})
pd.get_dummies(df, drop_first=True)

np.mean(arr); np.median(arr); np.std(arr)
np.sqrt(x); np.log(x); np.log1p(x)
np.where(cond, a, b)
np.percentile(arr, [25, 50, 75])

# Fit pattern is the SAME for every estimator
model = SomeEstimator(...)
model.fit(X_train, y_train)
preds = model.predict(X_test)
score = model.score(X_test, y_test)

# CV one-liner
scores = cross_val_score(LinearRegression(), X, y, cv=5, scoring="r2")
print("Mean R²:", scores.mean(), "+/-", scores.std())

r2_score(y_true, y_pred)
mean_squared_error(y_true, y_pred)
np.sqrt(mean_squared_error(y_true, y_pred))   # RMSE
mean_absolute_error(y_true, y_pred)
mean_absolute_percentage_error(y_true, y_pred)

import pandas as pd, numpy as np
import matplotlib.pyplot as plt, seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import r2_score, mean_squared_error
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 1. Load
df = pd.read_csv("data.csv")
print(df.shape); df.head()

# 2. Quick EDA
df.info(); df.describe()
sns.heatmap(df.corr(numeric_only=True), annot=True); plt.show()

# 3. Missing
df = df.dropna()                          # or impute

# 4. Encode
df = pd.get_dummies(df, drop_first=True, dtype=int)

# 5. Split
X = df.drop(columns=["target"]); y = df["target"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Scale
sc = StandardScaler()
X_tr_s = sc.fit_transform(X_tr); X_te_s = sc.transform(X_te)

# 7. VIF check
vif = pd.DataFrame({{"f": X_tr.columns,
                    "v": [variance_inflation_factor(X_tr.values, i)
                          for i in range(X_tr.shape[1])]}})
print(vif.sort_values("v", ascending=False))

# 8. OLS for interpretation
ols = sm.OLS(y_tr, sm.add_constant(X_tr)).fit()
print(ols.summary())

# 9. Models
models = {{"Linear": LinearRegression(),
          "Ridge":  Ridge(),
          "Lasso":  Lasso(),
          "EN":     ElasticNet()}}
for name, m in models.items():
    m.fit(X_tr_s, y_tr)
    pred = m.predict(X_te_s)
    print(name, "R²", r2_score(y_te, pred),
          "RMSE", np.sqrt(mean_squared_error(y_te, pred)))

# 10. Tune Ridge
gs = GridSearchCV(Ridge(),
                  {{"alpha": [0.01, 0.1, 1, 10, 100]}},
                  cv=5, scoring="r2")
gs.fit(X_tr_s, y_tr)
print("Best alpha:", gs.best_params_)
print("Test R²:", gs.score(X_te_s, y_te))
