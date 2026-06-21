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

===================================================

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


# ==============================================================================
# TOPIC 21: Cheatsheet and Mnemonics
# ==============================================================================

"""
Mnemonics master list
Every formula on one page
Concept one-liners
Model one-liners
When to use what
Red-flag values to memorize
Common traps
How to read OLS / numbers
Pipeline steps you must remember
Answer templates
Mnemonics master list
Mnemonic
Stands for
Used in
LINER
L inearity · I ndependence · N ormality of residuals · E qual variance (homoscedasticity) · R esiduals uncorrelated with predictors (≈ no multicollinearity)
5 assumptions of Linear Regression
LECESSTE
L oad · E DA · C lean · E ncode · S cale · S plit · T rain · E valuate
ML pipeline steps
SHID-BC
S hape · H ead · I nfo · D escribe · B oxplot · C orrelation
EDA recipe (Q3, 7 marks)
R-MAE-MAPE-MSE-RMSE
R² · MAE · MAPE · MSE · RMSE
Five regression metrics (in increasing penalty for big errors)
OMLR-CPE-OEH
O LS · M ulticollinearity · L INER · R egularization · C V · P andas · E DA · O utliers · E ncoding · H yperparameters
Hot-10 exam topics
"Lasso = Less" "Ridge = Reduce"
Lasso eliminates features (coefs to zero), Ridge reduces them but keeps all
Telling Lasso vs Ridge apart
"VIF over 5? Drive feature alive." (i.e. drop it)
VIF > 5 → warning, > 10 → drop
Multicollinearity threshold
"R² always grows; Adj R² won't snow"
R² never decreases when you add features; Adj R² can
Comparing models with different #features
"Bias is big-picture wrong; Variance is bouncy along"
High bias = model too simple (consistently off); high variance = model too complex (jumps with data)
Bias-variance tradeoff
"Train low, test high → overfit cry"
Training error tiny but test error big = overfitting
Diagnosing overfit vs underfit
"DROP-first to avoid the trap"
Use drop_first=True in get_dummies to avoid dummy-variable trap
One-hot encoding
"Split-Fit-Transform"
Split first, fit scaler/imputer on train, transform test
Avoiding data leakage
"DW close to 2 → independence is true"
Durbin-Watson ≈ 2 means no autocorrelation
Reading OLS summary
"p < 0.05 → keep alive"
p-value < 0.05 → coefficient significant, keep variable
Reading OLS summary
"Grid is greedy, Random is rapid, Bayes is brainy"
GridSearch tries everything (slow), RandomSearch samples (faster), Bayesian models the search space (smartest)
Hyperparameter tuning methods
"K-fold shuffles trust"
k-fold CV gives a more trustworthy estimate than a single train/test split
Why use cross-validation
Every formula on one page
Regression form
Simple LR: y = β₀ + β₁x + ε
Multiple LR: y = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ + ε
Polynomial: y = β₀ + β₁x + β₂x² + ... + βₖxᵏ + ε
Matrix form: Y = Xβ + ε
OLS estimation
Normal equation: β̂ = (XᵀX)⁻¹Xᵀy
Slope (SLR): β₁ = Σ(xᵢ−x̄)(yᵢ−ȳ) / Σ(xᵢ−x̄)²
Intercept (SLR): β₀ = ȳ − β₁x̄
Cost functions
MSE: (1/n) · Σ(yᵢ − ŷᵢ)²
RMSE: √MSE — same units as the target
MAE: (1/n) · Σ|yᵢ − ŷᵢ|
MAPE: (100/n) · Σ|yᵢ − ŷᵢ| / |yᵢ|
Evaluation
R²: 1 − (SS res / SS tot ) = 1 − (Σ(y−ŷ)² / Σ(y−ȳ)²)
Adjusted R²: 1 − [(1−R²)(n−1) / (n−p−1)]
where n = #samples, p = #predictors
Gradient descent
Update rule: β j := β j − α · ∂J/∂β j
α = learning rate
Regularization (with shrinkage penalty)
Ridge (L2): minimize Σ(y − ŷ)² + λ·Σβⱼ²
Lasso (L1): minimize Σ(y − ŷ)² + λ·Σ|βⱼ|
ElasticNet: minimize Σ(y − ŷ)² + λ·[α·Σ|βⱼ| + (1−α)·Σβⱼ²]
Multicollinearity
VIF for feature j: VIF j = 1 / (1 − R j ²)
where R j ² = R² of regressing x j on all other predictors
Tolerance: 1 / VIF (alternative form)
Inference
t-statistic: t = β̂ / SE(β̂)
F-statistic: F = [(SS tot − SS res )/p] / [SS res /(n−p−1)]
95% CI for coef: β̂ ± 1.96·SE(β̂) (large n)
Bias-Variance from cross-validation
Operational bias: 1 − mean(R² across folds)
Operational variance: std(R² across folds)
Train/test split & CV
k-fold CV: split into k parts; train on k−1, test on 1; rotate; average score
Concept one-liners
Concept
One-line definition
Supervised learning
Learning a function from input → output using labeled data.
Regression
Supervised learning where the target is continuous (e.g. price, salary).
Linear regression
Fit a straight line (or hyperplane) that minimises sum of squared residuals.
OLS
Ordinary Least Squares — the classic method that gives a closed-form β̂ = (XᵀX)⁻¹Xᵀy.
Polynomial regression
Linear regression on polynomial-transformed features; still linear in coefficients.
Cost function
Number that measures how wrong the model's predictions are; we minimise it.
MSE
Average squared error — penalises big mistakes more.
RMSE
Square root of MSE — same units as the target, easier to interpret.
MAE
Average absolute error — robust to outliers, easier to read.
R²
Proportion of variance in y explained by the model. 1 = perfect, 0 = useless.
Adjusted R²
R² penalised for adding more predictors. Use this to compare different-sized models.
Residual
y true − y pred . The error the model makes on each point.
Gradient descent
Iteratively update parameters in the direction that reduces the cost.
Learning rate (α)
Step size in gradient descent. Too big → diverge; too small → slow.
Linearity
Relationship between predictors and target is approximately a straight line.
Independence (of errors)
Errors at different observations are uncorrelated.
Normality (of residuals)
Residuals follow a normal (bell-curve) distribution.
Homoscedasticity
Variance of residuals is constant across all fitted values.
Heteroscedasticity
Variance of residuals changes with fitted value (funnel shape).
Multicollinearity
Two or more predictors are highly correlated; coefficients become unstable.
VIF
Variance Inflation Factor — measures how much a coefficient variance is inflated by multicollinearity.
Underfitting (high bias)
Model too simple; misses the pattern. Train and test error both high.
Overfitting (high variance)
Model too complex; memorises noise. Train low, test high.
Bias-variance tradeoff
Reducing one tends to raise the other; we seek the sweet spot.
Regularization
Add a penalty on coefficient size to fight overfitting.
Ridge (L2)
Penalty = λ·Σβ². Shrinks coefficients toward zero but keeps them all.
Lasso (L1)
Penalty = λ·Σ|β|. Can shrink coefficients exactly to zero → does feature selection.
ElasticNet
Mix of L1 and L2; useful when many features are correlated.
α (alpha) in Ridge/Lasso
Strength of penalty. α = 0 → no penalty. Higher α → more shrinkage.
Cross-validation
Split data into k folds; train on k−1, test on 1; rotate; average.
Hyperparameter
A parameter you set before training (like alpha or k) — not learned.
Q-Q plot
Plot of residual quantiles vs theoretical normal quantiles. Straight line → normal.
p-value
Probability of seeing such a result if the true coefficient were 0. < 0.05 → significant.
Feature engineering
Transforming or creating features (log, polynomial, interaction) to help the model.
Feature selection
Picking the most useful subset of features (forward, backward, RFE).
StandardScaler
Subtract mean, divide by std. Brings each feature to mean 0, std 1.
One-hot encoding
Convert a k-level category into k−1 binary columns (drop one level).
Dummy-variable trap
Keeping all k dummies → perfect multicollinearity with the intercept.
Model one-liners — when each shines
Model
Best for
Watch out for
Linear Regression (OLS)
Interpretable baseline; small to medium n; LINER assumptions roughly hold
Multicollinearity, non-linearity
Ridge
Many correlated features; you want to keep all features in the model
Doesn't do feature selection
Lasso
Many features, suspect most are useless; want a sparse model
Among correlated features it picks one randomly
ElasticNet
Many correlated features AND want some selection
Two hyperparameters (alpha, l1_ratio)
Polynomial Regression
Clearly non-linear pattern; one or two key features
Easy to overfit at high degree; explodes feature count
When to use what — quick decisions
Situation
What to use
Continuous target (price, salary)
Regression
Categorical target (yes/no, class)
Classification (out of scope for this exam)
Many features, > 100, suspect lots of irrelevant ones
Lasso
Many correlated features, want them all
Ridge
Mixed — many correlated, also want sparsity
ElasticNet
Visible curved pattern
Polynomial regression
Compare 2 models with different #features
Adjusted R² (not R²)
Compare 2 models predicting same target
RMSE / MAE / R² on test set
Compare 2 models predicting different targets (e.g. age vs CTC)
Cannot compare RMSE directly. Use %RMSE / mean target, or R².
Outliers heavily affect results
MAE (more robust than MSE/RMSE)
Errors of large magnitude must be punished
MSE / RMSE
Need to interpret coefficients
statsmodels OLS (gives full summary)
Need to predict only
sklearn LinearRegression / Ridge / Lasso
Small dataset (n < 100)
k-fold CV with k=5; avoid deep models
Want robust estimate of generalisation
Cross-validation, not single train/test split
Tuning 1–2 hyperparameters with small ranges
GridSearchCV
Tuning many hyperparameters or large ranges
RandomizedSearchCV / Bayesian
Heavy-tailed target distribution
Try log(y) transformation
Funnel-shaped residuals
Heteroscedasticity → log-transform y or use weighted LS
Red-flag values to memorize
Quantity
Healthy
Warning
Action
p-value
< 0.05
> 0.05 → not significant
VIF
> 10 → drop / combine feature
Durbin-Watson
1.5 – 2.5 (≈2)
1.0 – 1.5 or 2.5 – 3.0
< 1 or > 3 → autocorrelation
R²
Higher (context dependent)
Always pair with Adjusted R²
Skewness
−1 to 1
±1 to ±2
Beyond ±2 → consider log/Box-Cox
Condition number (in OLS)
< 30
> 100 → severe multicollinearity
Train R² vs Test R²
Close
Test ~ 5–10% lower
Big gap → overfitting
k for k-fold CV
5 or 10
Standard choices; avoid k=2
α (Ridge/Lasso)
Tuned via CV
Try {0.001, 0.01, 0.1, 1, 10, 100}
Test set size
20–30%
Below 10% → unreliable estimates
Common traps
Don't compare RMSE across different targets. RMSE has the units of the target. RMSE 55 (age in years) is not better than RMSE 12,324 (CTC in ₹). Use %RMSE relative to mean(y), or use R².
Always drop_first=True for one-hot. Otherwise you get the dummy-variable trap (perfect multicollinearity).
Scale and impute on TRAIN only. Splitting after scaling/imputing leaks info from test → over-optimistic scores.
Ridge does not do feature selection. It shrinks coefficients toward zero but rarely to zero. Lasso can. Elastic Net does both.
Regularised models need scaled features. Without scaling, the penalty unfairly punishes features measured on larger scales (e.g., salary in lakhs vs age in years).
R² always increases with more features. So R² is bad for comparing models with different numbers of predictors. Use Adjusted R² or held-out RMSE.
"Linear" in Linear Regression refers to the coefficients, not x. y = β₀ + β₁x + β₂x² is still called "linear regression" (linear in β).
p-value > 0.05 ≠ "no relationship". It means we don't have enough evidence to reject the null. Underpowered samples can hide real effects.
VIF threshold is 5/10, not 0.05. Don't confuse VIF with p-value.
k-fold CV with shuffle is essential when the data is ordered (e.g. by date or by class). Otherwise folds become biased.
GridSearchCV's best_score_ is on the validation folds, not the held-out test set. Always score the final tuned model on a separate test set.
Feature scaling does not change the fit of plain OLS. The coefficients change but R²/RMSE don't. Scaling matters for Ridge/Lasso/EN/SGD.
Don't use only training error to choose models. Always evaluate on held-out data or via cross-validation.
Outlier removal must be justified. "Just delete points outside 1.5·IQR" can throw away genuine signal. Investigate first.
Imputing with mean for skewed data is a bad idea. Use median for skewed numeric columns; mode for categorical.
How to read OLS / numbers in 60 seconds
Reading a coefficient
If area has coefficient +125.3 and y is price (₹) :
"Holding all other features constant, a one-unit increase in area is associated with an
expected increase of ₹125.3 in price."
Reading a p-value
p = 0.02 (less than 0.05): "reject the null hypothesis that this coefficient is zero — the
variable is statistically significant at the 5% level."
p = 0.30 (more than 0.05): "fail to reject the null — we don't have enough evidence to claim
this variable has a non-zero effect."
Reading R²
R² = 0.78: "about 78% of the variance in y is explained by this model."
Reading Adjusted R²
If R² = 0.81 but Adj R² = 0.62 → many features added with little real value.
Closer Adj R² to R² → features are pulling their weight.
Reading the F-statistic
Prob(F) < 0.05 → at least one predictor is significant. Prob(F) > 0.05 → none are; the model
overall is no better than just predicting the mean of y.
Reading VIF
VIF = 8.4 for x : "the variance of x's coefficient is inflated 8.4× compared to a
no-multicollinearity scenario. Strong multicollinearity — investigate or drop."
Reading log-coefficients
If model is log(salary) = α + β·log(sales) and β = 0.28:
"a 1% increase in sales is associated with a 0.28% increase in salary."
If model is log(salary) = α + β·roe and β = 0.0174:
"a 1-unit increase in roe is associated with a (approximately) 1.74% increase in salary."
Pipeline steps you must remember (LECESSTE)
L oad — pd.read_csv → df.shape, df.head, df.info, df.describe
E DA — histograms, boxplots, pairplot, correlation heatmap
C lean — handle missing (drop / median / mode), handle outliers (IQR / clip)
E ncode — one-hot for nominal (drop_first=True), ordinal for ordered, label for target
S cale — StandardScaler (fit on train only)
S plit — train_test_split (test_size=0.2, random_state=42)
T rain — fit model(s); compare Linear / Ridge / Lasso / EN / Polynomial; tune via CV
E valuate — R², Adjusted R², RMSE, MAE; residual plots; assumption checks
Answer templates for common ESA prompts
Template 1 — "Define X and explain why it is used"
Definition: X is <one sentence>.
Why used: It addresses <problem> by <mechanism>.
Example: e.g. predicting house prices, X helps because...
Caveat: X assumes / can fail when ...
Template 2 — "Differentiate between A and B"
Two-column comparison covering: definition · math form · effect on coefficients · feature
selection? · scaling required? · best for
Template 3 — "Comment on this OLS summary"
Fit quality: R² = X, Adj R² = Y → model explains X% of variance.
Joint significance: Prob(F) = Z → at least one predictor significant.
Significant variables: <list features with p < 0.05> with sign and rough magnitude.
Insignificant variables: <list with p > 0.05> — candidates to drop.
Diagnostics: DW = ?, JB p-value = ?, Cond. No. = ? — flag any concerns.
Business read: One sentence translating the biggest coefficient into plain English.
Template 4 — "Build a regression model end-to-end"
1. Load + EDA (head, info, describe, corr heatmap).
2. Handle missing (median for numeric, mode for categorical).
3. Outlier check (IQR; cap or drop).
4. Encode categoricals (get_dummies, drop_first=True).
5. Train/test split (test_size=0.2, random_state=42).
6. Scale (StandardScaler, fit on train).
7. Check VIF; drop features with VIF > 10.
8. Fit OLS; read summary; check assumptions via residuals + Q-Q.
9. Compare Linear / Ridge / Lasso / EN with 5-fold CV.
10. GridSearchCV to tune the chosen model's α.
11. Report final test R², RMSE, MAE.
12. Interpret top 3 coefficients in business terms.
Template 5 — "How would you handle multicollinearity?"
1. Detect: pairwise correlations + VIF (> 5 warning, > 10 serious).
2. Diagnose: identify the offending pair / cluster.
3. Fix:
Drop one of the highly-correlated pair
Combine: average or PCA the cluster
Use Ridge regression — handles multicollinearity gracefully
Re-collect data if a structural duplicate exists
4. Verify: recompute VIF; ensure all < 5.
Template 6 — "Detect and treat overfitting"
Detect: training R² >> test R² (or low CV score with high variance across folds).
Treat:
Add regularization (Ridge / Lasso)
Reduce model complexity (lower polynomial degree)
Reduce feature count (Lasso, RFE, forward selection)
Get more training data
Use cross-validation for honest evaluation
The night-before mantra
LINER — five LR assumptions.
VIF > 10 = drop ; alpha tuned by CV; scale before regularizing.
Lasso = Less features; Ridge = Reduce sizes; ElasticNet = both.
R² always grows; Adj R² wins for fair comparisons.
RMSE only compares same target; otherwise use R².
Bias = simple-wrong; Variance = bouncy.
p < 0.05 → keep alive; DW ≈ 2 → independence true.
Split → fit → transform. No leakage.
LECESSTE — full pipeline order.
Q4 = Preprocess. Q5 = OLS. Q6 = Compare + tune.
Read this list once before sleep. Sleep 7+ hours. You're ready.
All the best, Rajesh!
← Previous 20. Python Pipeline
"""
