# =============================================================================
#   UE20CS905 · SUPERVISED MACHINE LEARNING – REGRESSION (SMLR)
#   COMPLETE STUDY GUIDE: SESSIONS 1 through 6
#   PES University · M.Tech Data Science & AI
# =============================================================================
#
#  HOW TO READ THIS FILE
#  ---------------------
#  Each SESSION is a clearly marked block.
#  Formulas appear in two styles:
#    • Plain text  — when the formula is readable as-is  (e.g.  R² = SSR/SST)
#    • LaTeX block — when a symbol-heavy formula needs it (delimited by  $$ ... $$)
#
#  Navigate with: Ctrl+G → line number, or search for  "SESSION N"  or  "##"
#
#  QUICK-JUMP TABLE
#  ----------------
#  SESSION 1  – Data Preprocessing & SLR Foundations .............. line ~60
#  SESSION 2  – Linear Regression (SLR + OLS + MLR) ............... line ~420
#  SESSION 3  – Assumptions & Model Evaluation ..................... line ~780
#  SESSION 4  – Feature Engineering & Selection ................... line ~1330
#  SESSION 5  – Model Optimization ................................ line ~1750
#  SESSION 6  – Model Deployment (Pickle + Flask) ................. line ~2170
#  MASTER FORMULA SHEET ............................................ line ~2530
# =============================================================================


# ─────────────────────────────────────────────────────────────────────────────
# SESSION 1  ·  DATA PREPROCESSING & SIMPLE LINEAR REGRESSION FOUNDATIONS
# Dataset   : BigMart Sales (preprocessing) · Car Premium (SLR)
# ─────────────────────────────────────────────────────────────────────────────

## 1.1  WHAT IS DATA PREPROCESSING?
# ------------------------------------------------------------------------------
# Formal  : Transforming raw, real-world data into a clean, structured, and
#           model-ready format before feeding it to a machine learning algorithm.
#
# Simple  : Like cleaning survey forms — blank answers, inconsistent units,
#           prankster outliers — must all be fixed before counting or modelling.
#
# Why necessary?
#   • Most ML algorithms work only on NUMBERS → text must be encoded.
#   • Missing values cause computation errors in sklearn.
#   • Different scales (age 0–100 vs income 0–1 000 000) skew gradient-based
#     and distance-based algorithms.
#   • Outliers distort OLS regression coefficients significantly.
#
# Preprocessing Pipeline (dependency chain):
#   Raw Data
#     → Missing Value Treatment
#     → Categorical Encoding
#     → Outlier Treatment
#     → Feature Scaling / Transformation
#     → Feature Engineering
#     → Train-Test Split
#     → Model Ready ✓

## BigMart Dataset — Key Columns
# Column                     Type          Description
# Item_Identifier            Categorical   Unique product ID
# Item_Weight                Numeric       Weight (kg)
# Item_Fat_Content           Categorical   Low Fat / Regular
# Item_Visibility            Numeric       % display area (0–1)
# Item_MRP                   Numeric       Maximum Retail Price
# Outlet_Identifier          Categorical   Unique store ID
# Outlet_Establishment_Year  Numeric       Year store opened
# Outlet_Size                Categorical   Small / Medium / High
# Outlet_Location_Type       Categorical   Tier 1 / Tier 2 / Tier 3
# Outlet_Type                Categorical   Grocery Store / Supermarket Type1/2/3
# Item_Outlet_Sales          Numeric       ★ TARGET — Sales of the product
# Profit                     Numeric       Profit % of the item sold


## 1.2  MISSING VALUES
# ------------------------------------------------------------------------------
# A missing value is an absent data point. Causes: data corruption, sensor
# failure, survey non-response, data entry errors.
# sklearn throws an error if NaN values exist during model fitting.
#
# TWO TYPES:
#   ① Standard Missing   : NaN / None / np.NaN — auto-detected by pandas isnull()
#   ② Non-Standard Missing: Human-entered placeholders — "?", "--", "-", "na",
#                           "NAN" — look like valid data but represent absence.
#                           Must be found with  df.col.value_counts()  then
#                           replaced:  df['col'].replace("?", np.NaN, inplace=True)
#
# BigMart missing counts:
#   Item_Weight             749 missing
#   Outlet_Size            2410 missing
#   Outlet_Location_Type   2050 missing (grows to 2410 after replacing non-standard)

## Decision Tree for Missing Value Treatment:
#
#   Is column missing > 60-70%?
#       YES  → Drop the entire column
#       NO   ↓
#   Is the column NUMERIC?
#       YES → Are there outliers?
#           YES → Fill with MEDIAN
#           NO  → Fill with MEAN
#       NO  (Categorical) → Fill with MODE (most frequent)

# Treatment Options:
# Strategy            When to Use                   Code
# Drop Row            Very few rows missing (<1-2%)  df.dropna()
# Drop Column         Column > 60-70% missing        df.drop('col', axis=1)
# Fill with Mean      Numeric, no outliers           df['col'].fillna(df['col'].mean(), inplace=True)
# Fill with Median    Numeric, outliers present      df['col'].fillna(df['col'].median(), inplace=True)
# Fill with Mode      Categorical                    df['col'].replace(np.NaN, df['col'].mode()[0], inplace=True)
#
# Mnemonic: "MFD" — Mean for numbers, Frequency (Mode) for categories,
#           Drop when too many missing.


## 1.3  CATEGORICAL ENCODING
# ------------------------------------------------------------------------------
# ML algorithms need numbers. Categorical text must be converted.
#
# ① N-1 Dummy Encoding  (pd.get_dummies, drop_first=True)
#    For k categories → k-1 binary columns.
#    Dropped category = inferred when all others = 0.
#    Avoids DUMMY VARIABLE TRAP (perfect multicollinearity).
#    Best for: Linear Regression.
#    Example: Products {Vegetables, Dairy, Fruits} → 2 cols: Dairy_flag, Fruits_flag
#             When both=0 → it's Vegetables (reference category).
#
# ② One-Hot Encoding  (pd.get_dummies, no drop_first)
#    For k categories → exactly k binary columns.
#    Each row has exactly one "1", rest are "0".
#    Best for: Tree models, Neural Networks.
#
# ③ Label Encoding
#    Assigns integer 0 to n-1 alphabetically.
#    Implies ordering — use only for genuinely ordered categories or tree-based models.
#    Example: High=0, Low=1, Medium=2  (alphabetical — may not match real order!)
#
# ④ Ordinal Encoding
#    Like Label Encoding but USER specifies the order explicitly.
#    Best for: Small < Medium < High (user-defined ordering).
#
# ⑤ Frequency Encoding
#    Replaces each category with its proportion of total observations.
#    Useful for HIGH CARDINALITY variables (many unique categories).
#    ⚠ Risk: Two categories with same frequency get same code → model cannot distinguish.
#
# ⑥ Target / Mean Encoding
#    Replaces each category with the MEAN of the TARGET variable for that category.
#    Example: Smoker=Yes rows have mean heart-attack-rate = 0.5 → replace "Yes" with 0.5
#    ⚠ Risk: DATA LEAKAGE (target info leaks into features). Use cross-validation encoding.
#
# Quick Rule — "NOLF·T":
#   Nominal → OHE
#   Ordinal → Label/Ordinal Encoding
#   Large cardinality → Frequency/Target Encoding

# Comparison Table:
# Method           Output Cols  Preserves Order?  MC Risk  Best For
# N-1 Dummy        k-1          No                No       Linear Regression
# One-Hot          k            No                Yes      Trees, Neural Nets
# Label Encoding   1            Alphabetical      No       Tree-based only
# Ordinal Encoding 1            Yes (user-defined) No      Ordered categories
# Frequency        1            By frequency      No       High cardinality
# Target / Mean    1            By target mean    No       Classification/regression


## 1.4  FEATURE SCALING
# ------------------------------------------------------------------------------
# Why scale? Variables with different magnitudes (age 0-100 vs salary 0-100 000)
# cause gradient-based and distance-based algorithms to give undue weight to
# the larger-scale feature.
#
# Algorithms that NEED scaling:
#   Linear/Logistic Regression, k-NN, SVM, Neural Networks, PCA, Gradient Descent
# Tree-based models (Decision Tree, Random Forest) do NOT need scaling.
#
# ── Method 1 · Standardization (Z-score) ──────────────────────────────────────
#
#   x_new = (x − μ) / σ
#
#   LaTeX: $$x_{\text{new}} = \frac{x - \mu}{\sigma}$$
#
#   μ = mean of the column, σ = standard deviation
#   Result: every column gets mean=0 and std=1.
#   Shape of distribution is preserved (just re-centred).
#   Handles outliers BETTER than Min-Max.
#   Best for: algorithms assuming normality (Linear Regression, PCA).
#
# Worked Example — Z-score:
#   Values: [10, 20, 30, 40, 50]
#   Step 1: μ = (10+20+30+40+50)/5 = 30
#   Step 2: Variance = [(10-30)² + (20-30)² + (30-30)² + (40-30)² + (50-30)²] / 5
#                    = [400+100+0+100+400] / 5 = 200
#   Step 3: σ = √200 ≈ 14.14
#   Step 4: z(30) = (30 − 30) / 14.14 = 0.0   ← 30 is exactly at the mean
#
# ── Method 2 · Min-Max Normalization ──────────────────────────────────────────
#
#   X_norm = (X − X_min) / (X_max − X_min)
#
#   LaTeX: $$X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$$
#
#   Squeezes all values into [0, 1].
#   Sensitive to outliers (one extreme value compresses all others).
#   ★ IMPORTANT: Min-Max preserves linear relationships →
#     Pearson's R does NOT change after Min-Max scaling.
#
# Comparison:
# Feature              Standardization          Min-Max
# Output range         (−∞, +∞), centred at 0   [0, 1]
# Outlier sensitivity  Less sensitive            Very sensitive
# When to use          Normality assumed (LR)    Neural nets, bounded needed


## 1.5  DATA TRANSFORMATION
# ------------------------------------------------------------------------------
# Applied to correct skewness and satisfy regression assumptions.
#
# LOG TRANSFORMATION:
#   x_new = log(x)      [use log(x+1) if x contains zeros]
#   Applied to right-skewed data to reduce skewness.
#   Properties:
#     1. Reduces positive skewness.
#     2. Arithmetic mean of log(x) = geometric mean of original x.
#     3. Converts exponential growth into linear growth:  log(e^x) = x
#     4. Cannot be applied to zero or negative values.
#   Use when: skewness > 0.5
#
# EXPONENTIAL (Inverse of log):
#   Used to reverse log transformation — convert log-space predictions back
#   to original units.


## 1.6  OUTLIER DETECTION & TREATMENT
# ------------------------------------------------------------------------------
# An outlier is a data point abnormally far from other observations.
# Outliers distort OLS regression coefficients (slope + intercept).
#
# ── Method 1 · Z-Score ────────────────────────────────────────────────────────
#
#   z = (x − μ) / σ
#
#   Threshold: |z| > 3  (99.7% rule of normal distribution)
#   Z-score rules:
#     Small samples (n < 100)  : |z| > 2  (95%)
#     Medium samples            : |z| > 3  (standard)
#     Large samples (n > 1000) : |z| > 4  (99.9%)
#   ⚠ ONLY valid when data is roughly NORMAL (Gaussian).
#
# ── Method 2 · IQR (Interquartile Range) ─────────────────────────────────────
#
#   IQR = Q3 − Q1
#   Lower fence = Q1 − 1.5 × IQR
#   Upper fence = Q3 + 1.5 × IQR
#   Values outside these fences = outliers.
#   More ROBUST than Z-score — does NOT assume normality.
#
# Worked Example — IQR:
#   Data: [2, 4, 5, 7, 8, 10, 55]
#   Q1 = 4,  Q3 = 10,  IQR = 6
#   Lower fence = 4 − 1.5×6 = −5
#   Upper fence = 10 + 1.5×6 = 19
#   55 > 19 → OUTLIER ✓
#
# Method Comparison:
# Method    Assumes Normal?  Threshold                    Best When
# Z-Score   Yes              |z| > 3                      Bell-shaped data
# IQR       No               Outside Q1-1.5IQR, Q3+1.5IQR Skewed / unknown dist.


## 1.7  FEATURE ENGINEERING
# ------------------------------------------------------------------------------
# Creating new, more informative features from existing ones using domain knowledge.
# "A simple model with great features will often outperform a complex model
#  with raw features."
#
# BigMart Example:
#   Raw Feature: Outlet_Establishment_Year
#   Engineered:  Outlet_Age = current_year − Outlet_Establishment_Year
#   Impact:      Better correlation with sales → higher R²


## 1.8  TRAIN-TEST SPLIT
# ------------------------------------------------------------------------------
# Never test on the same data you trained on.
#
# Standard splits:
#   70% Train / 30% Test  — most common
#   80% Train / 20% Test  — for smaller datasets
#   75% Train / 25% Test  — sklearn default (if test_size not specified)
#
# Code:
#   X_train, X_test, y_train, y_test = train_test_split(
#       X, y, test_size=0.25, random_state=42)
#
# random_state:
#   Seeds the random number generator.
#   Same integer → same split every run → REPRODUCIBILITY.
#   Without it: different splits each run → non-comparable results.
#
# ⚠ Risk of NO split: Testing on training data gives optimistically
#   inflated (biased) performance metrics.


## 1.9  SIMPLE LINEAR REGRESSION (SLR) — FOUNDATIONS
# ------------------------------------------------------------------------------
# Regression Analysis models the relationship between a continuous dependent
# variable (target) and one or more independent variables (features).
#
# SLR equation:
#
#   Y = β₀ + β₁X + ε
#
#   LaTeX: $$Y = \beta_0 + \beta_1 X + \varepsilon$$
#
#   Y   = dependent variable (target)
#   X   = independent variable
#   β₀  = intercept (value of Y when X = 0)
#   β₁  = slope (change in Y per unit change in X)
#   ε   = error term (residual — what the model could not explain)
#
# Car Premium Dataset context:
#   Y = Insurance Premium,  X = Mileage
#   Model: Premium = 327.0860 − 11.6905 × Mileage
#   Interpretation of β₁ = −11.6905:
#     Every 1-unit increase in Mileage → Premium decreases by $11.69
#   Prediction:  Mileage = 17
#     Premium = 327.0860 − 11.6905 × 17 = $128.35
#
# Hypotheses:
#   H₀: β₁ = 0  (no linear relationship between X and Y)
#   H₁: β₁ ≠ 0  (linear relationship exists)


## 1.10  OLS METHOD
# ------------------------------------------------------------------------------
# OLS finds β₀ and β₁ that minimise SSE = Σ(yᵢ − ŷᵢ)².
#
#   Closed-form OLS formulas:
#
#   β₁ = Cov(X, Y) / Var(X)  =  Σ[(xᵢ − x̄)(yᵢ − ȳ)] / Σ[(xᵢ − x̄)²]
#   β₀ = ȳ − β₁ · x̄
#
#   LaTeX:
#   $$\hat{\beta}_1 = \frac{\text{Cov}(X,Y)}{\text{Var}(X)}$$
#   $$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$
#
# ★ Key Property: The OLS regression line always passes through (x̄, ȳ).


## 1.11  MEASURES OF VARIATION
# ------------------------------------------------------------------------------
#
#   SST = Σ(ȳ − yᵢ)²   Total variation in Y around its mean
#   SSR = Σ(ȳ − ŷᵢ)²   Variation explained by the regression line
#   SSE = Σ(yᵢ − ŷᵢ)²  Unexplained variation (residuals)
#
#   GOLDEN RULE:  SST = SSR + SSE
#
# R-Squared (Coefficient of Determination):
#
#   R² = SSR / SST = 1 − (SSE / SST)
#
#   LaTeX: $$R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}$$
#
#   Range: 0 ≤ R² ≤ 1.
#   R² = 1 → perfect fit.  R² = 0 → model explains nothing.
#   Example: R² = 0.72 means 72% of variation in Premium is explained by Mileage.
#
# Standard Error of Estimate (SEE):
#   SEE = √[SSE / (n − 2)]    [n−2: two parameters β₀, β₁ estimated]
#
#   LaTeX: $$SEE = \sqrt{\frac{SSE}{n-2}}$$
#
# Worked Example — SST, SSR, SSE, R²:
#   Actual Y  = [5, 10, 15],  ȳ = 10
#   Predicted = [6,  9, 15]
#   SST = (10-5)² + (10-10)² + (10-15)² = 25+0+25 = 50
#   SSE = (5-6)²  + (10-9)²  + (15-15)² = 1+1+0   = 2
#   SSR = SST − SSE = 48
#   R²  = 48/50 = 0.96  → model explains 96% of variance.

# Memory Aid: "Total pie = slice model ate (SSR) + slice left over (SSE)"


## 1.12  t-TEST AND CONFIDENCE INTERVALS FOR SLR
# ------------------------------------------------------------------------------
# Why test the slope? β₁ is estimated from sample data.
# We need to check it is SIGNIFICANTLY different from zero.
#
#   t = β₁ / SE(β₁)     degrees of freedom = n − 2
#
#   LaTeX: $$t = \frac{\hat{\beta}_1}{SE(\hat{\beta}_1)}, \quad df = n-2$$
#
#   H₀: β₁ = 0  |  H₁: β₁ ≠ 0
#   Decision: p-value < α (0.05) → Reject H₀ → slope is significant.
#
# Confidence Interval:
#   CI = β̂ ± t_critical × SE(β̂)
#   If CI for slope does NOT contain 0 → slope is significant at that α.
#
# Worked Numerical Example:
#   Slope = −11.6905,  SE(slope) = 2.85,  n = 15,  α = 0.05
#   t_calculated = −11.6905 / 2.85 = −4.10
#   df = n−2 = 13
#   t_critical (α=0.05, two-tail, df=13) = ±2.160
#   |t_calc| = 4.10 > 2.160  → Reject H₀
#   Conclusion: Mileage significantly predicts Premium.


## 1.13  ANOVA FOR SLR
# ------------------------------------------------------------------------------
# Tests whether the OVERALL regression model is statistically significant.
# For SLR: equivalent to t-test for slope; generalises to MLR.
#
#   F = MSR / MSE = (SSR / df_R) / (SSE / df_E)
#   For SLR: df_R = 1,  df_E = n − 2
#
#   LaTeX: $$F = \frac{MSR}{MSE} = \frac{SSR/1}{SSE/(n-2)}$$
#
#   H₀: β₁ = 0  |  H₁: β₁ ≠ 0
#
# ANOVA Table for SLR:
# Source      SS    df       MS          F
# Regression  SSR   1        MSR=SSR/1   MSR/MSE
# Error       SSE   n−2      MSE=SSE/(n-2)
# Total       SST   n−1
#
# ★ For SLR:  F = t²
#   If t = −4.10  →  F = 4.10² = 16.81


## 1.14  SESSION 1 EXAM Q&A
# ------------------------------------------------------------------------------
# 2-Mark Q: What is the dummy variable trap?
#   When using one-hot encoding in linear regression, including all k dummy
#   variables for a k-category variable creates perfect multicollinearity
#   (one column is a linear combination of the others).
#   Solution: use N−1 dummy encoding (drop_first=True).
#
# 2-Mark Q: When should you use median instead of mean for imputation?
#   When the numeric variable contains outliers. The mean is pulled by extremes;
#   the median is the middle value and is robust to extreme values.
#
# 2-Mark Q: What is the formula for Z-score normalization?
#   x_new = (x − μ) / σ,  result: mean=0, std=1.
#
# 2-Mark Q: What does R² = 0.85 mean?
#   85% of the variation in Y is explained by the regression model.
#
# 5-Mark Q: Explain Target Encoding with a numerical example.
#   Replace each category value with the mean of the target for that category.
#   Example: Smoker="Yes" rows: targets = [1,0,0,1,0,1] → mean = 3/6 = 0.5
#            Smoker="No"  rows: targets = [1,0,0,0]     → mean = 1/4 = 0.25
#   Replace "Yes" → 0.5, "No" → 0.25.
#   Risk: Data leakage. Use cross-validation or holdout encoding to mitigate.
#
# 5-Mark Q: Conduct a t-test for slope. (Same example as §1.12 above.)


## 1.15  SESSION 1 FORMULA SHEET
# ------------------------------------------------------------------------------
# Z-score         : z = (x − μ) / σ
# Min-Max         : X_norm = (X − X_min) / (X_max − X_min)
# SLR Equation    : Y = β₀ + β₁X + ε
# OLS Slope       : β₁ = Cov(X,Y) / Var(X)
# OLS Intercept   : β₀ = ȳ − β₁ · x̄
# SST             : Σ(ȳ − yᵢ)²
# SSR             : Σ(ȳ − ŷᵢ)²
# SSE             : Σ(yᵢ − ŷᵢ)²
# R²              : SSR / SST = 1 − SSE/SST
# SEE             : √[SSE / (n−2)]
# t for slope     : t = β₁ / SE(β₁),  df = n−2
# IQR             : Q3 − Q1
# Outlier fences  : Q1 − 1.5·IQR   to   Q3 + 1.5·IQR
# F-statistic     : F = (SSR/1) / (SSE/(n−2))
# CI for β        : β̂ ± t_crit × SE(β̂)
# SST = SSR + SSE


# ─────────────────────────────────────────────────────────────────────────────
# SESSION 2  ·  LINEAR REGRESSION — DEEP DIVE (SLR + MLR)
# Dataset   : Vehicle Insurance Premium (carpremium.csv)
# ─────────────────────────────────────────────────────────────────────────────

## 2.1  MACHINE LEARNING OVERVIEW
# ------------------------------------------------------------------------------
# Formal: ML is the science of making computers learn from data without
#         programming them explicitly, improving over time autonomously.
#
# Traditional Programming: Data + Rules → Output
# Machine Learning:        Data + Output → Rules (Model)
#
# AI ⊃ ML ⊃ Deep Learning
# Mnemonic: "All My Dogs"  →  AI contains ML contains Deep Learning
#
# Types of ML:
# Type                   Key Idea                              Examples
# Supervised Learning    Labelled data (features + target)     Linear Regression, SVM, Random Forest
# Unsupervised Learning  Patterns in unlabelled data           K-Means, PCA, DBSCAN
# Reinforcement Learning Agent rewarded for correct actions    Q-Learning, Policy Gradient
#
# Supervised: Regression vs Classification:
#   Regression     → continuous target  (predict salary, predict premium)
#   Classification → discrete target    (spam/not-spam, healthy/infected)
#
# ML Steps:
#   Data → EDA → Preprocessing → Feature Engineering → Feature Selection
#   → Model Building → Model Validation & Tuning → Model Testing → Deployment


## 2.2  DESCRIPTIVE STATISTICS RECAP
# ------------------------------------------------------------------------------
# Category               Measures
# Central Tendency       Mean, Median, Mode
# Dispersion             Variance, Standard Deviation, Range
# Shape                  Skewness, Kurtosis
# Statistical Dependence Pearson Correlation
# Visualisation tools    Box plots (outliers), Histograms (distribution shape)


## 2.3  KEY VARIABLES IN REGRESSION
# ------------------------------------------------------------------------------
# Dependent Variable Y:   What we predict. Also called Response / Target Variable.
#   Insurance example: Insurance Premium = Y
#
# Independent Variable X: Inputs used to predict. Also called Predictor / Feature.
#   Insurance example: Mileage, Age, Engine Capacity, Condition, Manufacturer
#
# COVARIANCE:
#
#   COV(X, Y) = Σᵢ (Xᵢ − X̄)(Yᵢ − Ȳ) / (n − 1)
#
#   LaTeX: $$\text{Cov}(X,Y) = \frac{\sum_{i=1}^{n}(X_i - \bar{X})(Y_i - \bar{Y})}{n-1}$$
#
#   Direction only — no standard scale. Positive cov: X↑ → Y↑.
#
# PEARSON'S CORRELATION COEFFICIENT R:
#
#   R = COV(X, Y) / (σₓ · σᵧ)
#
#   LaTeX: $$R = \frac{\text{Cov}(X,Y)}{\sigma_X \cdot \sigma_Y}$$
#
#   R ∈ [−1, +1]
#   R = +1: perfect positive | R = 0: no linear relationship | R = −1: perfect negative
#
# Mnemonic: "Covariance = Raw, Correlation = Refined"


## 2.4  SIMPLE LINEAR REGRESSION (SLR)
# ------------------------------------------------------------------------------
# One independent variable X, one dependent variable Y.
#
#   y = β₀ + β₁x + ε
#
# Error term (Residual ε):
#   εᵢ = yᵢ(actual) − ŷᵢ(predicted)
#   SSE = Σ εᵢ² = Σ(yᵢ − ŷᵢ)²
#
# Why square errors?
#   Raw residuals can cancel (+ and −). Squaring:
#   (1) makes all errors positive, (2) penalises large errors more.

## 2.5  OLS — FULL DERIVATION
# ------------------------------------------------------------------------------
# Minimise SSE:
#   E = Σ(yᵢ − β₀ − β₁xᵢ)²
#
# Derivation steps:
#   1. ∂E/∂β₀ = Σ 2(y − β₀ − β₁x)(−1) = 0   → Normal Equation 1
#   2. ∂E/∂β₁ = Σ 2(y − β₀ − β₁x)(−x) = 0   → Normal Equation 2
#   3. Solve simultaneously to get:
#
#   β̂₁ = COV(X,Y) / Var(X)
#   β̂₀ = Ȳ − β̂₁ · X̄
#
#   LaTeX:
#   $$\hat{\beta}_1 = \frac{\text{Cov}(X,Y)}{\text{Var}(X)}$$
#   $$\hat{\beta}_0 = \bar{Y} - \hat{\beta}_1 \bar{X}$$
#
# ★ The OLS line always passes through (X̄, Ȳ).
#
# OLS Worked Example (Insurance Dataset, n=15):
#   β̂₀ = 327.0860   β̂₁ = −11.6905
#   Premium = 327.0860 − 11.6905 × Mileage
#   Predict Mileage=17: ŷ = 327.086 − 11.6905×17 = $128.35

## Advantages of OLS:
#   ✓ Simple closed-form solution
#   ✓ Computationally efficient (moderate datasets)
#   ✓ Interpretable coefficients
#   ✓ BLUE estimator under Gauss-Markov assumptions
#   ✓ Well-established inference framework
#
## Limitations of OLS:
#   ✗ Sensitive to outliers (squared errors amplify outlier impact)
#   ✗ Assumes linear relationship
#   ✗ Assumes homoscedasticity
#   ✗ Sensitive to multicollinearity in MLR
#   ✗ Matrix inversion can be unstable for large/correlated features


## 2.6  MEASURES OF VARIATION
# ------------------------------------------------------------------------------
# (See also Session 1 §1.11)
#
# SST = SSR + SSE   (GOLDEN RELATIONSHIP)
#
# R²: (Coefficient of Determination)
#   R² = SSR/SST = 1 − SSE/SST
#
#   Insurance Model: R² = 0.226 → Mileage explains only 22.6% of variation
#   in premium. Need more variables → motivates MLR.
#
# ⚠ DEMERIT of R²: Always INCREASES when more variables are added, even useless ones.
#   Solution: Use Adjusted R² for MLR.
#
# SEE (Standard Error of Estimate):
#   Sxy = √[ SSE / (n − k) ]
#   where k = number of parameters estimated (k=2 for SLR)


## 2.7  INFERENCES ABOUT SLOPE
# ------------------------------------------------------------------------------
# t-test for Slope (β₁):
#   H₀: β₁ = 0  (no linear relationship)
#   H₁: β₁ ≠ 0
#
#   t₁ = β̂₁ / SE(β̂₁)  ~  t(n−2)
#   Reject H₀ if |t₁| > t(n−2, α/2)  OR  p-value < α
#
# t-test for Intercept (β₀):
#   H₀: β₀ = 0  |  H₁: β₀ ≠ 0
#   t₀ = β̂₀ / SE(β̂₀)  ~  t(n−2)
#
# Confidence Intervals:
#   CI for β₁: β̂₁ ± t(n−2, α/2) × SE(β̂₁)
#   CI for β₀: β̂₀ ± t(n−2, α/2) × SE(β̂₀)
#
# Insurance Model (α = 0.05):
#   β₁ (Mileage): CI = (−24.665, 1.284)  — contains 0 → may NOT be significant
#   β₀ (Intercept): CI = (139.057, 515.115) — does NOT contain 0 → IS significant
#
# t-test for Pearson's R:
#   H₀: ρ = 0  |  H₁: ρ ≠ 0
#
#   t = R · √(n−2) / √(1 − R²)  ~  t(n−2)
#
#   LaTeX: $$t = \frac{R\sqrt{n-2}}{\sqrt{1-R^2}}$$
#
# ANOVA for Bivariate Regression:
#   F₀ = MRSS / MESS = (SSR/k) / (SSE/(n−k−1))
#   H₀: β₁ = 0  |  H₁: β₁ ≠ 0
#   Reject H₀ if F₀ > F(k, n−k−1, α)  OR  p-value < α


## 2.8  MULTIPLE LINEAR REGRESSION (MLR)
# ------------------------------------------------------------------------------
# Extends SLR to multiple independent variables.
#
#   y = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ + ε
#
#   LaTeX: $$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p + \varepsilon$$
#
# Matrix Form (OLS for MLR):
#   Y = Xβ + ε
#
#   β̂ = (XᵀX)⁻¹ · Xᵀ · Y
#
#   LaTeX: $$\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \mathbf{Y}$$
#
#   Y = n×1 response vector
#   X = n×(p+1) design matrix (first column = 1s for intercept)
#   β = (p+1)×1 parameter vector
#
# Adjusted R²:
#   Penalises adding variables that don't improve the model.
#
#   R²_adj = 1 − [(1 − R²)(n − 1) / (n − p − 1)]
#
#   LaTeX: $$R^2_{\text{adj}} = 1 - \frac{(1-R^2)(n-1)}{n-p-1}$$
#
#   n = sample size,  p = number of predictors.
#   Adj. R² can DECREASE if an added variable doesn't help.
#   ALWAYS use Adj. R² for comparing MLR models.
#
# ANOVA Table for MLR:
# Source      SS    df        MS                  F
# Regression  SSR   k         MSR = SSR/k         F = MSR/MSE
# Error       SSE   n−k−1     MSE = SSE/(n−k−1)
# Total       SST   n−1


## 2.9  SESSION 2 EXAM Q&A
# ------------------------------------------------------------------------------
# 2-Mark Q: What is R² = 0.226 mean?
#   22.6% of the variation in Y is explained by the predictor.
#   The remaining 77.4% is not explained by this model.
#
# 2-Mark Q: Difference between SSR and SSE?
#   SSR = variation in Y explained by the model (larger = better).
#   SSE = unexplained variation (smaller = better).  SST = SSR + SSE.
#
# 5-Mark Q: Derive the OLS formulas for β₀ and β₁.
#   Minimise SSE = Σ(y − β₀ − β₁x)².
#   Take ∂SSE/∂β₀ = 0 and ∂SSE/∂β₁ = 0.
#   Solve the Normal Equations to get:
#     β̂₁ = COV(X,Y)/Var(X)  and  β̂₀ = Ȳ − β̂₁X̄.
#
# 5-Mark Q: Why is Adjusted R² preferred over R² in MLR?
#   R² always increases when variables are added.
#   Adj. R² penalises extra variables via n and p.
#   It can DECREASE when a useless variable is added.
#   Always use Adj. R² for comparing MLR models.


## 2.10  SESSION 2 FORMULA SHEET
# ------------------------------------------------------------------------------
# SLR            : y = β₀ + β₁x + ε
# Covariance     : COV(X,Y) = Σ(Xᵢ−X̄)(Yᵢ−Ȳ)/(n−1)
# Pearson's R    : R = COV(X,Y) / (σₓ·σᵧ)
# OLS slope      : β̂₁ = COV(X,Y) / Var(X)
# OLS intercept  : β̂₀ = Ȳ − β̂₁X̄
# SST=SSR+SSE    : Fundamental decomposition
# R²             : SSR/SST = 1 − SSE/SST
# Adj. R²        : 1 − [(1−R²)(n−1)/(n−p−1)]
# SEE            : √[SSE/(n−k)]
# t for slope    : β̂₁/SE(β̂₁) ~ t(n−2)
# t for Pearson  : R·√(n−2)/√(1−R²) ~ t(n−2)
# F (ANOVA)      : (SSR/k) / (SSE/(n−k−1))
# MLR Matrix     : β̂ = (XᵀX)⁻¹XᵀY


# ─────────────────────────────────────────────────────────────────────────────
# SESSION 3  ·  ASSUMPTIONS OF REGRESSION & MODEL EVALUATION
# Dataset   : NYC Employee Compensation · Auto Insurance Premium
# ─────────────────────────────────────────────────────────────────────────────

## 3.0  BIG PICTURE
# ------------------------------------------------------------------------------
# Regression only produces BLUE estimates (Best Linear Unbiased Estimator)
# when six assumptions hold. Violations lead to:
#   - Unstable or biased coefficients
#   - Unreliable t-tests and p-values
#   - Invalid confidence intervals
#
# The 6 assumptions at a glance:
# #  Assumption                 When to Check   Test Used                      What Breaks If Violated
# 1  Numeric Dependent Variable Before Model    dtype check                    Regression is meaningless
# 2  No Multicollinearity       Before Model    Det, CN, Corr Matrix, VIF      Unstable coefficients, wide CIs
# 3  Linear Relationship        After Model     Residual vs Predictor plot      Model misspecified
# 4  No Autocorrelation         After Model     Durbin-Watson                  p-values too small, false significance
# 5  Homoscedasticity           After Model     Goldfeld-Quandt, Breusch-Pagan Inefficient estimates
# 6  Normality of Errors        After Model     QQ Plot, Jarque-Bera, Shapiro-Wilk Invalid t/F-tests
#
# Mnemonic: "NUM LAHN"
#   N umeric target · U ncorrelated predictors · M odel fit
#   → L inearity · A utocorrelation absent · H omoscedasticity · N ormality


## 3.1  ASSUMPTION 1 — NUMERIC DEPENDENT VARIABLE
# ------------------------------------------------------------------------------
# Y must be continuous and numeric.
# Check: df.dtypes — Y must be int64 or float64.
# If violated: Use classification models instead.
# Example: 0/1 disease labels look numeric but are categories → use Logistic Regression.


## 3.2  ASSUMPTION 2 — NO MULTICOLLINEARITY
# ------------------------------------------------------------------------------
# Independent variables should NOT be highly correlated with each other.
# Analogy: Two court witnesses giving identical testimony — judge cannot determine
#          how much weight to assign each one.
#
# Consequences:
#   • OLS is no longer BLUE
#   • SE(β) inflated → wider confidence intervals
#   • Coefficients become unstable
#   • Individual t-tests become unreliable
#
# Chain:  High Corr → Multicollinearity → Large SE(β) → Wide CI → Unreliable t-tests
#
# TEST 1 — Determinant of Correlation Matrix:
#   D = det(Correlation Matrix)
#   D = 0 → Severe multicollinearity
#   D = 1 → No multicollinearity
#
# TEST 2 — Condition Number (CN):
#   CN = √(λ_max / λ_min)    [eigenvalues of correlation matrix]
#
#   LaTeX: $$CN = \sqrt{\frac{\lambda_{\max}}{\lambda_{\min}}}$$
#
#   CN > 1000 : Severe multicollinearity
#   100 < CN < 1000 : Moderate
#   CN < 100 : None
#
# TEST 3 — Correlation Matrix:
#   Off-diagonal values near ±1 → which variable pair is correlated.
#   ⚠ Limitation: Only captures pairwise relationships. Use VIF for precision.
#
# TEST 4 — Variance Inflation Factor (VIF):
#   For each predictor Xᵢ, regress it against ALL OTHER predictors.
#   R²ᵢ = R² from that regression.
#
#   VIF = 1 / (1 − R²ᵢ)
#
#   LaTeX: $$VIF_j = \frac{1}{1 - R^2_j}$$
#
#   VIF = 1   → No correlation         Keep
#   1 < VIF < 5 → Moderate              Monitor
#   VIF > 5   → High correlation        Remove or combine
#   VIF > 10  → Severe multicollinearity Must remove
#
# VIF Worked Example:
#   Predictor X₁ regressed on X₂, X₃. R² = 0.80.
#   VIF = 1/(1−0.80) = 1/0.20 = 5.0  → High correlation. Investigate.
#
# Remedies:
#   1. Drop one of the correlated variables
#   2. Combine variables into a composite (e.g., salary+bonus → income)
#   3. Ridge Regression (L2) — shrinks collinear coefficients
#   4. PCA — transform into uncorrelated principal components
#
# Mnemonic: "D C C V" — Determinant → CN → Correlation Matrix → VIF


## 3.3  ASSUMPTION 3 — LINEARITY
# ------------------------------------------------------------------------------
# Each predictor must have a linear relationship with Y.
# "Linear in Parameters" — β must appear as simple multipliers.
#
# Linear in parameters?
#   y = β₀ + β₁x₁ + β₂x₂²       YES  (x₂² is a transform of X, not β)
#   y = β₀ + β₁log(x₁) + β₂x₂   YES  (log is transform of X)
#   y = β₀ + e^(β₁x₁)            NO   (β₁ is inside exponential)
#
# How to check:
#   1. Residuals vs. Predictors Plot — random scatter = linearity OK
#   2. Residuals vs. Fitted Values   — random scatter = linearity + homoscedasticity OK
#   U-shaped/curved pattern → nonlinear → add X² term.
#
# Mnemonic: "If residuals have NO PATTERN, relationship is LINEAR."


## 3.4  ASSUMPTION 4 — NO AUTOCORRELATION
# ------------------------------------------------------------------------------
# Error terms εᵢ must be independent. "Auto" = self.
# Autocorrelation = errors that copy previous errors.
# Common in: time series, monthly/weekly data.
#
# Impact: β values UNCHANGED → BUT SE(β) REDUCED → p-values too small → FALSE SIGNIFICANCE.
# ⚠ Tricky: autocorrelation does NOT change β, only inflates significance.
#
# DURBIN-WATSON TEST:
#   Tests first-order serial correlation.
#
#   d = Σ(êₜ − êₜ₋₁)² / Σêₜ²
#
#   LaTeX: $$d = \frac{\sum_{t=2}^{n}(\hat{e}_t - \hat{e}_{t-1})^2}{\sum_{t=1}^{n}\hat{e}_t^2}$$
#
#   d ∈ [0, 4]
#   d ≈ 2  → No autocorrelation ✓
#   d < 2  → Positive autocorrelation
#   d > 2  → Negative autocorrelation
#   d ≈ 0  → Strong positive autocorrelation
#   d ≈ 4  → Strong negative autocorrelation
#
# DW Worked Example:
#   Residuals: ê₁=2, ê₂=5, ê₃=−1, ê₄=3, ê₅=−4
#   Numerator:   (5−2)²+(−1−5)²+(3−(−1))²+(−4−3)² = 9+36+16+49 = 110
#   Denominator: 2²+5²+1²+3²+4² = 4+25+1+9+16 = 55
#   d = 110/55 = 2.0  → No autocorrelation ✓
#
# Mnemonic: "DW = 2 is the Sweet Spot"


## 3.5  ASSUMPTION 5 — HOMOSCEDASTICITY
# ------------------------------------------------------------------------------
# Variance of error terms must be CONSTANT across all levels of predictors.
# HOMO = Same.  HETERO = Different.
#
# Visual: Residual vs. Fitted Plot
#   Random scatter         → homoscedastic ✓
#   Funnel shape (widens)  → heteroscedastic ✗
#   Funnel inversed        → heteroscedastic ✗
#
# TEST 1 — GOLDFELD-QUANDT (GQ):
#   Splits data into two groups (low X, high X).
#   Compares residual variances using F-ratio.
#   H₀: σ₁² = σ₂²  (homoscedastic)
#   H₁: σ₁² ≠ σ₂²  (heteroscedastic)
#   Reject H₀ if p-value < α.
#
# TEST 2 — BREUSCH-PAGAN (BP):
#   Regresses squared residuals on predictors.
#   BP = n × R²(e²)  ~  χ²(k)
#
#   LaTeX: $$BP = n \cdot R^2_{e^2} \sim \chi^2(k)$$
#
#   H₀: Homoscedastic.  Reject H₀ if p-value < α.
#
# GQ vs BP:
# Feature        GQ                         BP
# Approach       Splits data into 2 groups   Regresses squared residuals on predictors
# Best for       Single predictor            Multiple predictors
# Distribution   F                           Chi-squared
#
# Remedies: Log-transform Y | WLS | Remove outliers | Box-Cox transform
# Mnemonic: "GB Tests for Same Variance"


## 3.6  ASSUMPTION 6 — NORMALITY OF ERRORS
# ------------------------------------------------------------------------------
# Residuals must follow Normal(0, σ²).
# Required for t-tests and F-tests to be valid.
#
# TEST 1 — QQ PLOT (Quantile-Quantile):
#   Plots sorted residuals vs theoretical normal quantiles.
#   Points on 45° line → normal ✓
#   S-curve → heavy tails.  Skewed off-line → non-normal.
#
# TEST 2 — JARQUE-BERA (JB):
#   H₀: S = 0 AND K = 3  (data is normal)
#   H₁: S ≠ 0 OR K ≠ 3
#
#   JB = (n/6) × [S² + (1/4)(K − 3)²]    ~  χ²(2)
#
#   LaTeX: $$JB = \frac{n}{6}\left[S^2 + \frac{(K-3)^2}{4}\right] \sim \chi^2(2)$$
#
#   n = observations, S = skewness, K = kurtosis
#
# JB Worked Example:
#   n=100, S=0.5, K=4.0
#   S² = 0.25
#   (K−3)²/4 = (1.0)²/4 = 0.25
#   JB = (100/6) × (0.25+0.25) = 16.67 × 0.50 = 8.33
#   χ²(2) critical at α=0.05 = 5.99
#   8.33 > 5.99 → Reject H₀ → Residuals NOT normally distributed ✗
#
# TEST 3 — SHAPIRO-WILK (SW):
#   W = (Σ aᵢxᵢ)² / Σ(xᵢ − x̄)²
#
#   LaTeX: $$W = \frac{\left(\sum_i a_i x_{(i)}\right)^2}{\sum_i (x_i-\bar{x})^2}$$
#
#   W ∈ (0, 1].  W ≈ 1 → Normal.  W → 0 → Not normal.
#   H₀: Data is normally distributed.  p < α → reject → Not normal.
#   Best for: small to medium samples (n < 2000).
#
# Test Comparison:
# Method       Type         Best For           H₀
# QQ Plot      Visual       Any sample size     —  (subjective)
# Jarque-Bera  Statistical  Large samples       S=0, K=3
# Shapiro-Wilk Statistical  Small-medium (n<2000) Data is normal
#
# Mnemonic: "QJS" — QQ Plot → Jarque-Bera → Shapiro-Wilk


## 3.7  MODEL EVALUATION METRICS
# ------------------------------------------------------------------------------
# MSE   = (1/n) × Σ(yᵢ − ŷᵢ)²          [Y² units, penalises outliers]
# RMSE  = √MSE                           [Y units, most common]
# MAE   = (1/n) × Σ|yᵢ − ŷᵢ|           [Y units, robust to outliers]
# MAPE  = (1/n) × Σ|(yᵢ−ŷᵢ)/yᵢ| × 100% [%, undefined when yᵢ=0]
#
# LaTeX for MSE and RMSE:
#   $$MSE = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$$
#   $$RMSE = \sqrt{MSE}$$
#   $$MAE = \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|$$
#   $$MAPE = \frac{1}{n}\sum_{i=1}^n \left|\frac{y_i - \hat{y}_i}{y_i}\right| \times 100\%$$
#
# R²:
#   R² = SSR/SST     Range: 0 ≤ R² ≤ 1
#
# Adjusted R²:
#   R²_adj = 1 − [(1 − R²)(n − 1) / (n − k − 1)]
#
# R² vs Adj. R² Worked Example:
#   n=100, k=5, R²=0.80
#   R²_adj = 1 − (0.20 × 99/94) = 1 − 0.2106 = 0.789
#
# F-Test for Overall Model Significance:
#   H₀: β₁ = β₂ = ... = βₖ = 0   |   H₁: at least one βᵢ ≠ 0
#   F = (SSR/k) / (SSE/(n−k−1)) = MSR/MSE
#   Reject H₀ if F > F(k, n−k−1, α) or p < α.
#
# F-Test Worked Example:
#   n=50, k=3, SSR=1200, SSE=300
#   MSR = 1200/3 = 400
#   MSE = 300/(50−3−1) = 300/46 ≈ 6.52
#   F   = 400/6.52 ≈ 61.35
#   F(3,46) critical at 5% ≈ 2.81  →  61.35 ≫ 2.81 → Reject H₀ ✓ model is significant
#
# t-test for Individual Coefficients:
#   t = β̂ᵢ / SE(β̂ᵢ)  ~  t(n−k−1)
#   CI: β̂ᵢ ± t(α/2, n−k−1) × SE(β̂ᵢ)
#   CI contains 0 → predictor NOT significant at that α level.
#
# Mnemonic: "RRAM" — R-squared · R-adjusted · ANOVA F-test · MSE/RMSE/MAE/MAPE


## 3.8  CATEGORICAL VARIABLES (DUMMY ENCODING)
# ------------------------------------------------------------------------------
# k categories → k−1 dummy (binary 0/1) variables.
# Dropped category = reference / baseline.
#
# Example: Manufacturer (Ford / Honda / Tata), k=3
#   Mfr_Honda  Mfr_Tata  → Reference (both=0) = Ford
#
# Intercept Shift Effect:
#   Premium = β₀ + β₁·Mileage + β₂·Mfr_Honda + β₃·Mfr_Tata
#
#   Manufacturer   Effective Intercept    Regression Line
#   Ford           β₀                     β₀ + β₁·Mileage
#   Honda          β₀ + β₂               (β₀+β₂) + β₁·Mileage
#   Tata           β₀ + β₃               (β₀+β₃) + β₁·Mileage
#
# Estimated Model:
#   Premium = 368.93 − 9.117·Mileage − 95.174·Mfr_Honda − 129.216·Mfr_Tata
#   β₂ = −95.174: Honda cars cost $95.17 LESS premium than Ford (on average).
#
# ⚠ DUMMY VARIABLE TRAP: Never use k dummies for k categories → perfect multicollinearity.
# Mnemonic: "k minus 1 saves the day"


## 3.9  INTERACTION EFFECTS
# ------------------------------------------------------------------------------
# An interaction effect occurs when the effect of X₁ on Y CHANGES depending
# on the value of X₂.
# Analogy: "1 + 1 ≠ 2 in interactions." Salt + Sugar + Lemon = Lemonade.
#
# Interaction term:
#   Int_EC_Mil = Engine_Capacity × Mileage
#   Premium = β₀ + β₁·Mileage + β₂·Engine_Capacity + β₃·Age + β₄·(EC×Mileage) + ε
#
#   β₄ = how much Mileage's effect on Premium changes per unit of Engine_Capacity
#
# ⚠ Interaction ≠ Multicollinearity.
#   Multicollinearity = predictors share information independently.
#   Interaction = new effect that arises when they work TOGETHER.
#
# When to include:
#   • Domain knowledge suggests joint effect
#   • Interaction term has significant p-value (< α)
#   • Adj. R² improves after adding interaction term
#
# Mnemonic: "Lemonade Effect" — Two ingredients together create something different.


## 3.10  SESSION 3 EXAM Q&A
# ------------------------------------------------------------------------------
# 2-Mark Q: What is multicollinearity?
#   Two or more independent variables are highly correlated.
#   Problem: OLS no longer BLUE; SE(β) inflated; t-tests unreliable.
#
# 2-Mark Q: DW statistic = 2 means?
#   No autocorrelation. d=2 is the sweet spot in [0,4].
#
# 2-Mark Q: What is VIF = 8?
#   High multicollinearity (> 5). 80% of the variable's variance is explained
#   by other predictors. Should investigate for removal.
#
# 5-Mark Q: Explain multicollinearity detection and treatment.
#   (1) Det of Corr Matrix: D near 0 = severe.
#   (2) CN: > 1000 = severe, 100-1000 = moderate.
#   (3) Correlation Matrix: which pair is correlated.
#   (4) VIF = 1/(1−R²ᵢ): > 5 = high.
#   Treatment: Drop redundant, combine, Ridge Regression, PCA.
#
# 5-Mark Q: Explain F-test for overall significance. (See §3.7 above.)
#
# 5-Mark Q: Dummy encoding with 3 categories. (See §3.8 above.)


## 3.11  SESSION 3 FORMULA SHEET
# ------------------------------------------------------------------------------
# VIF                : VIF = 1/(1−R²ᵢ)
# CN                 : CN = √(λmax/λmin)
# Durbin-Watson      : d = Σ(êₜ−êₜ₋₁)²/Σêₜ²   [0–4; d=2 = no AC]
# Breusch-Pagan      : BP = n·R²(e²) ~ χ²(k)
# Jarque-Bera        : JB = (n/6)[S² + (K−3)²/4] ~ χ²(2)
# Shapiro-Wilk       : W = (Σaᵢxᵢ)²/Σ(xᵢ−x̄)²    [W ∈ (0,1]; W≈1 = normal]
# MSE                : (1/n)Σ(yᵢ−ŷᵢ)²
# RMSE               : √MSE
# MAE                : (1/n)Σ|yᵢ−ŷᵢ|
# MAPE               : (1/n)Σ|(yᵢ−ŷᵢ)/yᵢ|×100%
# F-test             : (SSR/k) / (SSE/(n−k−1))
# R²_adj             : 1 − [(1−R²)(n−1)/(n−k−1)]
# Interaction term   : y = β₀ + β₁X₁ + β₂X₂ + β₃(X₁×X₂) + ε
# Dummy coefficients : y = (β₀ + βⱼ) + β₁x₁   [βⱼ = intercept shift]


# ─────────────────────────────────────────────────────────────────────────────
# SESSION 4  ·  FEATURE ENGINEERING & FEATURE SELECTION
# Dataset   : Appliances Energy Prediction (1000 obs, 25 vars)
# ─────────────────────────────────────────────────────────────────────────────

## 4.0  THE ML PIPELINE — BIG PICTURE
# ------------------------------------------------------------------------------
# Session 4 focuses on Step 2 — Feature Extraction:
#
# Pipeline Step        Sub-Activities                            Session 4?
# Step 1 — Processing  Collection, Formatting, Labelling         No  (Sessions 1–3)
# Step 2 — Extraction  Transformation, Engineering, Selection    YES — THIS SESSION
# Step 3 — Modelling   Model Building, Evaluation                No
# Step 4 — Optimization Validation, Fine Tuning                  No
# Step 5 — Deployment  Serving predictions via web               No
#
# Three Types of Feature Extraction:
#   Feature Transformation : Replace existing features with a math function
#                            (e.g., log(Income) to reduce skew)
#   Feature Engineering    : Create new features from domain knowledge
#                            (e.g., Age × Income interaction term)
#   Feature Selection      : Keep only significant features; drop the rest
#
# Dataset: Appliances Energy Prediction
#   Sensor readings from a smart home. Target: Appliances (Wh).
#   1000 observations, 25 variables.
#   Data prep: IQR outlier treatment; "lights" dropped (zero variance).


## 4.1  FEATURE TRANSFORMATION
# ------------------------------------------------------------------------------
# Replaces existing features with a mathematical function to:
#   - Correct skewness
#   - Satisfy normality assumption
#   - Reduce outlier influence
#
# ── Log Transformation ────────────────────────────────────────────────────────
#   x_new = log(x)    [use log(x+1) if x contains zeros]
#   Use when: right-skewed (skewness > 0), multiplicative relationships.
#
# ── Square Root Transformation ────────────────────────────────────────────────
#   x_new = √x
#   Use when: moderate right skew, count data.
#   Milder than log.
#
# ── Reciprocal Transformation ─────────────────────────────────────────────────
#   x_new = 1/x
#   Use when: rate data, very strong right skew.
#   Cannot use if x = 0.
#
# ── Exponential / Power Transformation ───────────────────────────────────────
#   x_new = x²  or  xⁿ
#   Use when: left-skewed data.
#   ⚠ Can amplify outliers.
#
# ── Box-Cox Transformation ────────────────────────────────────────────────────
#   A family of power transformations that finds optimal λ via max-likelihood.
#
#   Y(λ) = (xᵀ − 1) / λ    if λ ≠ 0
#   Y(λ) = log(x)           if λ = 0
#
#   LaTeX:
#   $$Y(\lambda) = \begin{cases} \dfrac{x^\lambda - 1}{\lambda} & \lambda \neq 0 \\ \log(x) & \lambda = 0 \end{cases}$$
#
#   λ = 1 → No transformation
#   λ = 0 → Log transformation
#   λ = 0.5 → Square root
#   λ = −1 → Reciprocal
#   ⚠ Requires all x > 0.
#
# Transformation Comparison:
# Method       Formula       Best Used When
# Log          log(x)        Strong right skew, multiplicative relationships
# Square Root  √x            Moderate right skew, count data
# Reciprocal   1/x           Rate data, very strong right skew
# Power (x²)   x^n           Left-skewed data
# Box-Cox      (xᵀ−1)/λ      Any skew — finds optimal λ automatically


## 4.2  FEATURE SCALING
# ------------------------------------------------------------------------------
# Ensures all features are on a comparable scale.
# OLS is scale-invariant, but regularization, kNN, SVM are NOT.
#
# Normalization (Min-Max):
#   X_scaled = (X − X_min) / (X_max − X_min)    → range [0, 1]
#   Use: Neural Networks, kNN, SVM.
#   ⚠ Very sensitive to outliers.
#
# Standardization (Z-Score):
#   X_scaled = (X − μ) / σ    → mean=0, std=1
#   Use: Linear/Ridge/Lasso Regression, PCA, regularization.
#   Better handling of outliers.
#
# Mnemonic: "S for Standard — Standardization is the Standard (default choice)"


## 4.3  FEATURE SELECTION
# ------------------------------------------------------------------------------
# Identifies most important predictors; removes irrelevant/redundant features.
# Benefits: simpler model, less overfitting, faster training.
#
# ── Forward Selection ─────────────────────────────────────────────────────────
#   Starts with NO variables. Adds one at a time.
#   Steps:
#   1. Start with intercept-only model.
#   2. Fit all one-variable models; add predictor with lowest p-value (or highest F).
#   3. Fit all two-variable models including the selected; add best new predictor.
#   4. Continue until no remaining variable has p-value < α (typically 0.05).
#
# ── Backward Elimination ──────────────────────────────────────────────────────
#   Starts with ALL variables. Removes one at a time.
#   Steps:
#   1. Start with all predictors.
#   2. Remove predictor with highest p-value IF p > α.
#   3. Refit without that variable.
#   4. Repeat until all remaining predictors have p < α.
#
# ── Stepwise Regression (Bidirectional) ──────────────────────────────────────
#   Combination of forward + backward.
#   After each addition, checks if any previously added variable became insignificant.
#   Uses α_entry AND α_exit thresholds.
#
# ── Recursive Feature Elimination (RFE) ──────────────────────────────────────
#   Model-based iterative removal.
#   Steps:
#   1. Fit model on all features.
#   2. Compute feature importance (|coefficient| for linear models).
#   3. Remove feature with lowest importance.
#   4. Refit and repeat until desired number of features reached.
#   Use RFECV to find optimal feature count via cross-validation.
#
# Comparison:
# Method     Description                                Trade-offs
# Forward    Starts empty, adds one at a time           Fast for large p; may miss interactions
# Backward   Starts full, removes one at a time         Better when p < n; can be slow
# Stepwise   Bidirectional add/remove                   More thorough; two thresholds
# RFE        Model-based ranking, iterative removal     Needs importance scores; any model
#
# Master Mnemonic — Session 4: "Transform → Scale → Select → Perform"


## 4.4  SESSION 4 EXAM Q&A
# ------------------------------------------------------------------------------
# 2-Mark Q: Difference between Feature Transformation and Feature Selection?
#   Transformation creates a new version of an existing feature (e.g., log(X)).
#   Selection decides which features to keep and which to drop.
#
# 2-Mark Q: Why is Standardization preferred over Normalization for Linear Regression?
#   Normalization is sensitive to outliers and bounded [0,1].
#   Standardization handles outliers better and is the standard for regression
#   and regularization methods.
#
# 5-Mark Q: Explain Backward Elimination step by step.
#   (1) Start with all p predictors.
#   (2) Find predictor with highest p-value. If p > α, remove it.
#   (3) Refit model.
#   (4) Repeat until all remaining predictors have p-value < α.
#
# 5-Mark Q: What is Box-Cox transformation? When to use?
#   Y(λ) = (xᵀ−1)/λ for λ≠0; log(x) for λ=0.
#   λ found by max-likelihood to make data as normal as possible.
#   Use when: distribution is skewed and optimal transformation is unknown.
#   Constraint: all values must be > 0.


## 4.5  SESSION 4 FORMULA SHEET
# ------------------------------------------------------------------------------
# Log Transform       : x_new = log(x)  or  log(x+1) if zeros present
# Square Root         : x_new = √x
# Reciprocal          : x_new = 1/x
# Box-Cox             : Y(λ) = (xᵀ−1)/λ for λ≠0;  log(x) for λ=0
# Normalization       : X_scaled = (X−X_min)/(X_max−X_min)
# Standardization     : X_scaled = (X−μ)/σ
# Exam Checklist:
#   Log can't handle zeros; Square Root can; Reciprocal can't handle zeros.
#   Box-Cox = generalised log (λ=0 gives log); only for positive values.
#   Forward: starts null, adds. Backward: starts full, removes. Stepwise: does both.
#   RFE = automated backward with model-based rankings; needs target feature count.
#   Always back-transform predictions before comparing RMSE/R².


# ─────────────────────────────────────────────────────────────────────────────
# SESSION 5  ·  MODEL OPTIMIZATION
# Dataset   : IPL Auction Data (130 obs, 22 vars)
# ─────────────────────────────────────────────────────────────────────────────

## 5.0  OVERVIEW
# ------------------------------------------------------------------------------
# Model Optimization improves predictive efficacy by:
#   Prediction Evaluation → Model Validation → Fine Tuning
# Mnemonic: "EVF — Evaluate → Validate → Fine-Tune"
#
# Three Pillars:
# Pillar                Description                            Tools
# Prediction Evaluation How well does it predict?              RMSE, MAPE, R², Adj-R²
# Model Validation      Does it generalise?                    k-Fold CV, LOOCV
# Fine Tuning           Maximise performance                   GridSearchCV, Randomized, Bayesian


## 5.1  BIAS & VARIANCE
# ------------------------------------------------------------------------------
# Two competing sources of error in any ML model.
#
# BIAS:
#   Bias = E[ŷ] − y_true
#
#   LaTeX: $$\text{Bias} = E[\hat{y}] - y_{\text{true}}$$
#
#   High bias → underfitting (model too simple; misses real pattern).
#   Dart analogy: Bias = how far your average throw is from bullseye.
#   "Bias = Bad Assumptions → Bulldozer through data, won't bend"
#
# VARIANCE:
#   Variance = E[ŷ²] − (E[ŷ])²
#
#   LaTeX: $$\text{Variance} = E[\hat{y}^2] - (E[\hat{y}])^2$$
#
#   High variance → overfitting (model memorises training data).
#   Dart analogy: Variance = how scattered your throws are around where they land.
#
# BIAS-VARIANCE TRADEOFF:
#
#   Total Error = Bias² + Variance + Irreducible Noise
#
#   LaTeX: $$\text{Total Error} = \text{Bias}^2 + \text{Variance} + \sigma^2_\varepsilon$$
#
#   Scenario              What It Means                     Remedy
#   High Bias, Low Var    Underfitting; consistent but wrong More complex model
#   Low Bias, High Var    Overfitting; great on train, bad on test Simplify / regularise
#   Low Bias, Low Var     IDEAL — generalises well           Correct complexity
#   High Bias, High Var   Worst case; wrong model type       Change model type
#
# ★ Sweet Spot: Optimal complexity minimises Total Error.
#   As complexity increases: Bias decreases, Variance increases.


## 5.2  OVERFITTING & UNDERFITTING
# ------------------------------------------------------------------------------
# Underfitting (High Bias):
#   High training error AND high test error.
#   Training R² is low.
#   Remedy: Add features, increase model complexity.
#
# Good Fit:
#   Low training error AND low test error (both similar).
#   This is the GOAL.
#
# Overfitting (High Variance):
#   Very low training error but high test error.
#   Training R² ≫ Test R².
#   Red flag: Training R²=0.98, Test R²=0.62 → severe overfitting.
#   Remedy: Regularisation, reduce features, cross-validation.


## 5.3  CROSS-VALIDATION
# ------------------------------------------------------------------------------
# Provides reliable estimate of how a model generalises.
# Helps detect overfitting.
#
# k-FOLD CROSS-VALIDATION:
#   1. Split dataset into k equal folds (typically k=5 or 10).
#   2. For each fold i: train on all other k−1 folds; test on fold i.
#   3. Final CV score = mean of k scores.
#
#   CV Score = (1/k) × Σᵢ₌₁ᵏ Score(fold i)
#
#   LaTeX: $$CV = \frac{1}{k}\sum_{i=1}^{k}\text{Score}_i$$
#
#   Every observation is used for testing exactly once.
#   k=10 is the most common choice.
#
# LOOCV (Leave-One-Out Cross-Validation):
#   Special case: k = n.
#   Each iteration uses n−1 observations for training, 1 for testing.
#   ✓ Maximum training data used.
#   ✗ Computationally expensive (n model fits).
#   In practice: k-fold (k=10) is preferred over LOOCV.


## 5.4  GRADIENT DESCENT
# ------------------------------------------------------------------------------
# Iterative optimization to find β that minimises cost function J(β).
# Used when OLS matrix inversion is too expensive (very large datasets).
#
# Cost Function (MSE):
#   J(β) = (1/n) × Σᵢ (yᵢ − ŷᵢ)²
#
#   LaTeX: $$J(\boldsymbol{\beta}) = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$$
#
# Parameter Update Rule:
#   βⱼ(new) = βⱼ(old) − α × ∂J(β)/∂βⱼ
#
#   LaTeX: $$\beta_j \leftarrow \beta_j - \alpha \frac{\partial J}{\partial \beta_j}$$
#
#   For regression: ∂J/∂βⱼ = (2/n) × Σ(ŷᵢ − yᵢ) × xᵢⱼ
#
# Learning Rate α:
#   Too large → overshoots minimum; may diverge.
#   Too small → very slow convergence; will converge eventually.
#   Just right → smooth convergence in reasonable iterations.
#
# Types of Gradient Descent:
# Type            Description                                    Best When
# Batch GD        Uses ALL n examples per update. Stable, slow.  Small datasets
# Stochastic GD   Uses ONE random example per update. Fast, noisy. Very large datasets
# Mini-Batch GD   Uses batch of 32–256 examples. Balanced.        Most practical; deep learning
#
# GD vs OLS:
#   OLS: β̂ = (XᵀX)⁻¹XᵀY — exact solution in one step.
#   Use OLS for small/moderate n and p.
#   Use Gradient Descent when n and p are very large (matrix inversion infeasible).


## 5.5  REGULARIZATION
# ------------------------------------------------------------------------------
# Adds a penalty term to the cost function to prevent overfitting.
# Shrinks coefficients toward zero.
#
# General form:
#   Regularised Cost = Loss Function + λ × Penalty Term
#   λ = 0 → standard OLS.  Large λ → heavy shrinkage.
#
# RIDGE REGRESSION (L2):
#
#   J_Ridge(β) = Σ(yᵢ − ŷᵢ)² + λ × Σⱼ βⱼ²
#
#   LaTeX: $$J_{\text{Ridge}}(\boldsymbol{\beta}) = \sum_i (y_i-\hat{y}_i)^2 + \lambda\sum_j \beta_j^2$$
#
#   Closed-form: β̂_Ridge = (XᵀX + λI)⁻¹ XᵀY
#
#   LaTeX: $$\hat{\boldsymbol{\beta}}_{\text{Ridge}} = (\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{Y}$$
#
#   ★ Ridge NEVER sets coefficients to exactly zero.
#   Keeps all features but reduces their impact.
#   Handles multicollinearity (λI stabilises XᵀX inversion).
#
# LASSO REGRESSION (L1):
#
#   J_Lasso(β) = Σ(yᵢ − ŷᵢ)² + λ × Σⱼ |βⱼ|
#
#   LaTeX: $$J_{\text{Lasso}}(\boldsymbol{\beta}) = \sum_i (y_i-\hat{y}_i)^2 + \lambda\sum_j |\beta_j|$$
#
#   No closed form — solved with coordinate descent.
#   ★ Lasso CAN set coefficients to exactly zero → automatic feature selection.
#   Best for sparse models (many predictors suspected irrelevant).
#
# ELASTIC NET:
#
#   J_EN(β) = Σ(yᵢ − ŷᵢ)² + λ [α × Σ|βⱼ| + (1−α)/2 × Σβⱼ²]
#
#   LaTeX:
#   $$J_{\text{EN}}(\boldsymbol{\beta}) = \sum_i (y_i-\hat{y}_i)^2 + \lambda\left[\alpha\sum_j|\beta_j| + \frac{1-\alpha}{2}\sum_j\beta_j^2\right]$$
#
#   α = 1 → Pure Lasso.  α = 0 → Pure Ridge.  0 < α < 1 → mix.
#   Best for: p > n (more predictors than observations), correlated groups.
#
# Regularization Comparison:
# Method       Penalty         Coefficients → 0?  Best For
# Ridge (L2)   Σβⱼ²            Never              Multicollinearity, all features matter
# Lasso (L1)   Σ|βⱼ|           Yes (sparse)        Feature selection, many irrelevant features
# Elastic Net  mix of L1+L2    Some                p > n, correlated feature groups
#
# Decision Guide:
#   All features matter?     → Ridge
#   Many features irrelevant? → Lasso
#   Features in correlated groups or p > n? → Elastic Net


## 5.6  HYPERPARAMETER TUNING
# ------------------------------------------------------------------------------
# Hyperparameters are set BEFORE training (e.g., λ, k).
# Not learned from data — found through search.
#
# GRIDSEARCHCV:
#   Exhaustively tries every combination of specified values.
#   Uses cross-validation to evaluate each combination.
#   Example: λ ∈ {0.01, 0.1, 1, 10, 100}, α ∈ {0.1, 0.5, 0.9} = 15 combinations × k-folds.
#   ✓ Guaranteed best in grid.
#   ✗ Computationally expensive; scales poorly.
#
# RANDOMIZEDSEARCHCV:
#   Randomly samples a fixed number of combinations.
#   ✓ Much faster. Often finds near-optimal solutions.
#   ✗ No guarantee of finding absolute best.
#
# BAYESIAN OPTIMIZATION:
#   Intelligent sequential search. Learns from previous evaluations.
#   Uses a Gaussian Process surrogate model and an acquisition function (Expected Improvement).
#   Steps:
#   1. Evaluate a few initial random combinations.
#   2. Fit a Gaussian Process surrogate model to results so far.
#   3. Use acquisition function to select next hyperparameter to try.
#   4. Evaluate actual model at that point.
#   5. Update surrogate model. Repeat until budget exhausted.
#
# Comparison:
# Method          Speed     Guarantee  Best For
# GridSearchCV    Slow      Best in grid  Small grids; known search space
# Randomized      Fast      Near-optimal  Large search spaces
# Bayesian        Smart     Most efficient Expensive model evaluations
#
# Master Mnemonic — Session 5:
# "Big Overfit? Cross-validate. Got Descent? Regularize with Ridge, Lasso, or Elastic-net.
#  Tune Hyperparams with Grid, Random, or Bayes."


## 5.7  MODEL SCORE CARD
# ------------------------------------------------------------------------------
# Metric              What to Check
# Training RMSE       Should be low (fits training data)
# Test RMSE           Should be close to Training RMSE (generalises)
# Training R²         Should be high
# Test R²             If much lower → overfitting
# CV Score (Mean±Std) Low std → stable model
# Adj. R²             Use for MLR model comparison
#
# Red Flags:
#   Training R² = 0.97, Test R² = 0.63 → Severe overfitting
#   CV Score std > 0.1 → Unstable model
#   Adj. R² drops when adding variable → That variable is not useful


## 5.8  SESSION 5 EXAM Q&A
# ------------------------------------------------------------------------------
# 2-Mark Q: Bias-variance tradeoff?
#   Total Error = Bias² + Variance + Irreducible Noise.
#   Bias = oversimplification (underfitting).
#   Variance = oversensitivity to training data (overfitting).
#   Increasing complexity: Bias↓, Variance↑. Sweet spot minimises total error.
#
# 2-Mark Q: Ridge vs Lasso?
#   Ridge: L2 penalty (Σβⱼ²) — shrinks toward zero but keeps all features.
#   Lasso: L1 penalty (Σ|βⱼ|) — sets some to exactly zero → feature selection.
#
# 5-Mark Q: Explain k-fold CV and why it is better than a simple train-test split.
#   k-fold: split into k folds; use k−1 for train, 1 for test; repeat k times.
#   Every observation used for testing exactly once.
#   More reliable estimate; reduces dependency on which observations are in train vs test.
#
# 5-Mark Q: Explain Gradient Descent and its types. (See §5.4 above.)
#
# 5-Mark Q: Explain Bayesian Optimization. (See §5.6 above.)


## 5.9  SESSION 5 FORMULA SHEET
# ------------------------------------------------------------------------------
# Total Error  : Bias² + Variance + Irreducible Noise
# Bias         : E[ŷ] − y_true
# Variance     : E[ŷ²] − (E[ŷ])²
# k-Fold CV    : (1/k) × Σ Score(fold i)
# GD Update    : βⱼ = βⱼ − α × ∂J/∂βⱼ
# Ridge cost   : Σ(yᵢ−ŷᵢ)² + λΣβⱼ²
# Ridge soln   : β̂ = (XᵀX + λI)⁻¹ XᵀY
# Lasso cost   : Σ(yᵢ−ŷᵢ)² + λΣ|βⱼ|
# Elastic Net  : Σ(yᵢ−ŷᵢ)² + λ[α·Σ|βⱼ| + (1−α)/2·Σβⱼ²]


# ─────────────────────────────────────────────────────────────────────────────
# SESSION 6  ·  MODEL DEPLOYMENT (PICKLE + SKLEARN PIPELINE + FLASK)
# Dataset   : Loan Status (Loan_data_ver2.csv)
# ─────────────────────────────────────────────────────────────────────────────

## 6.0  WHAT IS MODEL DEPLOYMENT?
# ------------------------------------------------------------------------------
# Formal: Integrating a trained ML model into a production environment where it
#         can receive real-world inputs and return predictions to end users.
#
# Bakery Analogy:
#   You've baked a cake (trained a model).
#   Deployment = opening a bakery (web app) so customers can walk in,
#   tell you their order, and get their cake slice (prediction)
#   — without needing to know how the cake was baked.
#
# Why Deployment is Necessary:
#   • Model in Jupyter notebook cannot be used by anyone else.
#   • Deployment turns a model into a service via web browser or API.
#   • End users (loan officers, bankers) just fill a form — no Python needed.
#   • Enables real-time prediction on new, unseen data.


## 6.1  ML LIFECYCLE OVERVIEW
# ------------------------------------------------------------------------------
# Phase         What Happens                                       File
# 1. Collection Fetch raw dataset (pd.read_csv(url))               Train_Deploy.ipynb
# 2. Preprocess Imputation, encoding, scaling                      Train_Deploy.ipynb
# 3. Training   Fit model on training data                         Train_Deploy.ipynb
# 4. Serialize  Save model to disk (pickle.dump())                 → full_pipeline file
# 5. Validate   Test saved model on sample input (pickle.load())   Test_Deploy.ipynb
# 6. Deploy     Serve predictions via web interface                app.py + main.html
#
# Mnemonic: "Build a Pipeline, Pickle it, Prove it, Put it on Flask, Point a browser at it"
# B uild → P ickle.dump() → P rove (Test_Deploy) → P ut on Flask → P oint browser


## 6.2  SERIALIZATION — PICKLE
# ------------------------------------------------------------------------------
# Pickle converts a Python object (model, pipeline, scaler) to a binary file.
# Memory Trick: "Pickle = Freeze-dry the model for storage"
#
# Saving a Model:
#   import pickle
#   with open("full_pipeline", "wb") as f:    # 'wb' = write binary
#       pickle.dump(pipeline, f)
#
# Loading a Model:
#   with open("full_pipeline", "rb") as f:    # 'rb' = read binary
#       my_model = pickle.load(f)
#
# Making Predictions:
#   predictions = my_model.predict(new_data_df)
#   (new_data_df must have same column structure as training data)


## 6.3  SKLEARN PIPELINE
# ------------------------------------------------------------------------------
# Chains multiple preprocessing steps + model into a SINGLE object.
#
# Why Pipeline?
#   Without Pipeline: must manually apply scalers/encoders to new data in order.
#   With Pipeline:    call .predict(raw_data) — Pipeline handles all transformations.
#   Prevents DATA LEAKAGE (scalers fit only on training data, not test data).
#
# Numeric Sub-Pipeline:
#   numeric_transformer = Pipeline(steps=[
#       ("imputer", SimpleImputer(strategy="mean")),
#       ("scaler", StandardScaler())
#   ])
#
# Categorical Sub-Pipeline:
#   categorical_transformer = Pipeline(steps=[
#       ("imputer", SimpleImputer(strategy="most_frequent")),
#       ("onehot", OneHotEncoder(handle_unknown="ignore"))
#   ])
#
# ColumnTransformer (applies different pipelines to different columns):
#   ct = ColumnTransformer(transformers=[
#       ("num", numeric_transformer, numeric_cols),
#       ("cat", categorical_transformer, categorical_cols)
#   ])
#
# Full Pipeline:
#   full_pipeline = Pipeline(steps=[
#       ("preprocessor", ct),
#       ("model", RandomForestClassifier())
#   ])
#   full_pipeline.fit(X_train, y_train)
#   predictions = full_pipeline.predict(X_test)
#
# Key sklearn Objects:
# Object                 What It Does                      Memory Trick
# SimpleImputer(mean)    Fills numeric NaNs with column mean   "Ask the class average"
# KNNImputer             Fills NaNs using nearest neighbour    "Ask your neighbors"
# StandardScaler         Z-score normalization (mean=0, std=1) "Center and squeeze"
# SimpleImputer(constant) Fills categorical NaNs with 'Missing' "Label the gap"
# OneHotEncoder          Binary encodes categorical variables  "One column per category"
# ColumnTransformer      Routes columns to different pipelines "Sorting office"


## 6.4  LOAN DATASET WALKTHROUGH
# ------------------------------------------------------------------------------
# Dataset: Loan_data_ver2.csv
# Task: Binary classification — predict Loan_Status (Approved Y / Rejected N).
#
# TRAIN_DEPLOY.IPYNB — Training Phase:
#   1. Load data:  pd.read_csv(github_url)
#   2. Split:  X = all features (drop Loan_Status),  y = Loan_Status
#             X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#   3. Build numeric sub-pipeline (SimpleImputer + StandardScaler)
#   4. Build categorical sub-pipeline (SimpleImputer + OneHotEncoder)
#   5. Build ColumnTransformer combining both
#   6. Build full Pipeline: ColumnTransformer + RandomForestClassifier
#   7. Fit: full_pipeline.fit(X_train, y_train)
#   8. Evaluate: full_pipeline.score(X_test, y_test)
#   9. Save: pickle.dump(full_pipeline, open("full_pipeline", "wb"))
#
# TEST_DEPLOY.IPYNB — Validation Phase:
#   1. Create one test observation as a dictionary with all features.
#   2. Convert to DataFrame: test_df = pd.DataFrame([test_dict])
#   3. Load: my_model = pickle.load(open("full_pipeline", "rb"))
#   4. Predict: my_model.predict(test_df) → "Y" (Approved) or "N" (Rejected)
#   5. Verify prediction matches manual expectation.


## 6.5  FLASK WEB FRAMEWORK
# ------------------------------------------------------------------------------
# Flask is a lightweight Python web framework.
# Serves as the interface between the model and end users.
# Analogy: "Flask = Hotel receptionist — takes orders, returns results"
#
# Key Flask Concepts:
# Concept          Description
# @app.route       Maps a URL path to a Python function
# HTTP GET         Serves blank HTML form (user browsing/navigating)
# HTTP POST        Receives filled form data, runs prediction, returns result
# request.form     Dict-like object with all form field values from POST
# render_template  Renders HTML template from templates/ folder
#
# app.py Structure:
#
#   from flask import Flask, request, render_template
#   import pickle, pandas as pd
#
#   app = Flask(__name__)
#   my_model = pickle.load(open("full_pipeline", "rb"))
#
#   @app.route("/", methods=["GET", "POST"])
#   def index():
#       if request.method == "POST":
#           data = {col: request.form[col] for col in feature_cols}
#           df   = pd.DataFrame([data])
#           prediction = my_model.predict(df)[0]
#           return render_template("main.html", prediction=prediction)
#       return render_template("main.html")
#
#   if __name__ == "__main__":
#       app.run(debug=True)
#
# HTML Template (templates/main.html):
#   <form action="/" method="POST">
#       <input name="Gender" ...>
#       <input name="ApplicantIncome" ...>
#       ... one input per feature ...
#       <button type="submit">Predict</button>
#   </form>
#   {% if prediction %}
#       <p>Loan Status: {{ prediction }}</p>
#   {% endif %}
#
# Jinja2: {{ prediction }} injects the Python variable into HTML at runtime.


## 6.6  END-TO-END DEPLOYMENT FLOW
# ------------------------------------------------------------------------------
# Step  What Happens                                    Technical Detail
# 1     User opens http://127.0.0.1:5000/              Flask serves blank main.html form
# 2     User fills form (income, loan amount, etc.)     Input values stored in HTML fields
# 3     User clicks Submit                              Browser sends HTTP POST to /
# 4     Flask reads request.form, builds DataFrame      data = {col: request.form[col] for col}
# 5     Pipeline transforms → model predicts            my_model.predict(df)[0]
# 6     Flask renders result                            render_template("main.html", prediction=result)
# 7     User sees "Approved" or "Rejected"              Jinja2 {{ prediction }} displayed


## 6.7  KEY CONCEPTS COMPARED
# ------------------------------------------------------------------------------
# Concept            What It Does
# pickle.dump()      Saves trained Python object to binary file (serialization)
# pickle.load()      Reconstructs Python object from binary file (deserialization)
# Pipeline.fit()     Trains pipeline — fits all transformers + model on training data
# Pipeline.predict() Applies all transformations to new data; returns prediction
# ColumnTransformer  Routes different feature subsets to different sub-pipelines
# GET request        Serves the empty prediction form to the user
# POST request       Receives filled form, runs prediction, returns result
# render_template()  Renders HTML file with optional Python variable injection


## 6.8  SESSION 6 EXAM Q&A
# ------------------------------------------------------------------------------
# 2-Mark Q: What is model serialization and why is it necessary?
#   Pickle saves a trained model object to disk as a binary file.
#   Necessary because: training is expensive; the web app (Flask) needs to
#   access the model at runtime without retraining each time.
#
# 2-Mark Q: What is a sklearn Pipeline and why use it?
#   Chains preprocessing steps + model into one object.
#   Prevents data leakage (transformers fit only on training data).
#   Ensures same transformations applied consistently to any new data.
#
# 5-Mark Q: Describe Train_Deploy and Test_Deploy for the Loan dataset.
#   (See §6.4 above — all 9 Train_Deploy steps and 5 Test_Deploy steps.)
#
# 5-Mark Q: How is Flask used for ML deployment?
#   (See §6.5 above — app.py walkthrough, routes, GET/POST, render_template.)


## 6.9  SESSION 6 QUICK REFERENCE
# ------------------------------------------------------------------------------
# Task                  Code
# Save model            pickle.dump(pipeline, open("full_pipeline","wb"))
# Load model            model = pickle.load(open("full_pipeline","rb"))
# Predict               model.predict(pd.DataFrame([input_dict]))
# Flask app             app = Flask(__name__)
# Route decorator       @app.route("/", methods=["GET","POST"])
# Read form data        request.form["field_name"]
# Render HTML           render_template("main.html", prediction=result)
# Run app               app.run(debug=True)  →  http://127.0.0.1:5000/
# Numeric pipeline      Pipeline([("imp",SimpleImputer()),("sc",StandardScaler())])
# Cat pipeline          Pipeline([("imp",SimpleImputer()),("ohe",OneHotEncoder())])
# ColumnTransformer     ColumnTransformer([("num",np,num_cols),("cat",cp,cat_cols)])
# Full pipeline         Pipeline([("pre",ct),("model",RandomForestClassifier())])


# ─────────────────────────────────────────────────────────────────────────────
# MASTER FORMULA SHEET  ·  ALL SESSIONS 1 – 6
# ─────────────────────────────────────────────────────────────────────────────

## SESSION 1 — DATA PREPROCESSING & SLR FOUNDATIONS
# ──────────────────────────────────────────────────
# Z-score            : z = (x − μ) / σ
#   LaTeX            : $$z = \frac{x-\mu}{\sigma}$$
# Min-Max            : X_norm = (X − X_min) / (X_max − X_min)
#   LaTeX            : $$X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max}-X_{\min}}$$
# SLR Equation       : Y = β₀ + β₁X + ε
# OLS Slope          : β₁ = Cov(X,Y) / Var(X)
# OLS Intercept      : β₀ = ȳ − β₁ · x̄
# SST                : Σ(ȳ − yᵢ)²
# SSR                : Σ(ȳ − ŷᵢ)²
# SSE                : Σ(yᵢ − ŷᵢ)²
# Golden Rule        : SST = SSR + SSE
# R²                 : SSR / SST = 1 − SSE/SST
# SEE                : √[SSE / (n−2)]
# t for slope        : t = β₁/SE(β₁), df=n−2
# IQR                : Q3 − Q1
# Outlier Fences     : Q1 − 1.5·IQR  and  Q3 + 1.5·IQR
# F-statistic (SLR)  : F = (SSR/1) / (SSE/(n−2))
# CI for β           : β̂ ± t_crit × SE(β̂)

## SESSION 2 — LINEAR REGRESSION
# ──────────────────────────────────────────────────
# Covariance         : Cov(X,Y) = Σ(Xᵢ−X̄)(Yᵢ−Ȳ)/(n−1)
# Pearson R          : R = Cov(X,Y) / (σₓ·σᵧ)
# Adj. R²            : 1 − [(1−R²)(n−1)/(n−p−1)]
#   LaTeX            : $$R^2_{\text{adj}}=1-\frac{(1-R^2)(n-1)}{n-p-1}$$
# t for Pearson      : t = R·√(n−2)/√(1−R²)  ~  t(n−2)
# MLR Matrix OLS     : β̂ = (XᵀX)⁻¹XᵀY
#   LaTeX            : $$\hat{\boldsymbol{\beta}}=(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{Y}$$
# F (MLR ANOVA)      : (SSR/k) / (SSE/(n−k−1))

## SESSION 3 — ASSUMPTIONS & MODEL EVALUATION
# ──────────────────────────────────────────────────
# VIF                : VIF = 1/(1−R²ᵢ)
#   LaTeX            : $$VIF_j = \frac{1}{1-R_j^2}$$
# Condition Number   : CN = √(λ_max / λ_min)
#   LaTeX            : $$CN = \sqrt{\lambda_{\max}/\lambda_{\min}}$$
# Durbin-Watson      : d = Σ(êₜ−êₜ₋₁)² / Σêₜ²     [d=2 → no AC]
#   LaTeX            : $$d = \frac{\sum_{t=2}^n(\hat{e}_t-\hat{e}_{t-1})^2}{\sum_{t=1}^n\hat{e}_t^2}$$
# Breusch-Pagan      : BP = n·R²(e²) ~ χ²(k)
#   LaTeX            : $$BP = n\cdot R^2_{e^2} \sim \chi^2(k)$$
# Jarque-Bera        : JB = (n/6)[S² + (K−3)²/4]  ~  χ²(2)
#   LaTeX            : $$JB=\frac{n}{6}\!\left[S^2+\frac{(K-3)^2}{4}\right]\sim\chi^2(2)$$
# Shapiro-Wilk       : W = (Σaᵢxᵢ)²/Σ(xᵢ−x̄)²    [W ∈ (0,1]; W≈1 = normal]
#   LaTeX            : $$W = \frac{(\sum_i a_i x_{(i)})^2}{\sum_i(x_i-\bar{x})^2}$$
# MSE                : (1/n)Σ(yᵢ−ŷᵢ)²
# RMSE               : √MSE
# MAE                : (1/n)Σ|yᵢ−ŷᵢ|
# MAPE               : (1/n)Σ|(yᵢ−ŷᵢ)/yᵢ|×100%
# Dummy Rule         : k categories → k−1 dummy variables
# Interaction Model  : y = β₀ + β₁X₁ + β₂X₂ + β₃(X₁×X₂) + ε
# Intercept Shift    : y = (β₀ + βⱼ) + β₁x₁

## SESSION 4 — FEATURE ENGINEERING
# ──────────────────────────────────────────────────
# Log Transform      : log(x)  or  log(x+1) if zeros
# Square Root        : √x
# Reciprocal         : 1/x
# Box-Cox            : Y(λ) = (xᵀ−1)/λ for λ≠0;  log(x) for λ=0
#   LaTeX            : $$Y(\lambda)=\begin{cases}\frac{x^\lambda-1}{\lambda}&\lambda\neq0\\\log x&\lambda=0\end{cases}$$
# Normalization      : (X−X_min)/(X_max−X_min)
# Standardization    : (X−μ)/σ

## SESSION 5 — MODEL OPTIMIZATION
# ──────────────────────────────────────────────────
# Total Error        : Bias² + Variance + Irreducible Noise
#   LaTeX            : $$\text{Total Error}=\text{Bias}^2+\text{Var}+\sigma^2_\varepsilon$$
# Bias               : E[ŷ] − y_true
# Variance           : E[ŷ²] − (E[ŷ])²
# k-Fold CV          : (1/k) Σᵢ Score(fold i)
# GD Update          : βⱼ = βⱼ − α·∂J/∂βⱼ
#   LaTeX            : $$\beta_j \leftarrow \beta_j - \alpha\frac{\partial J}{\partial\beta_j}$$
# Ridge cost         : Σ(yᵢ−ŷᵢ)² + λΣβⱼ²
#   LaTeX            : $$J_R=\sum(y_i-\hat y_i)^2+\lambda\sum\beta_j^2$$
# Ridge solution     : (XᵀX + λI)⁻¹ XᵀY
#   LaTeX            : $$\hat\beta_R=(\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{Y}$$
# Lasso cost         : Σ(yᵢ−ŷᵢ)² + λΣ|βⱼ|
#   LaTeX            : $$J_L=\sum(y_i-\hat y_i)^2+\lambda\sum|\beta_j|$$
# Elastic Net        : Σ(yᵢ−ŷᵢ)² + λ[α·Σ|βⱼ| + (1−α)/2·Σβⱼ²]
#   LaTeX            : $$J_{EN}=\sum(y_i-\hat y_i)^2+\lambda\!\left[\alpha\sum|\beta_j|+\tfrac{1-\alpha}{2}\sum\beta_j^2\right]$$

## SESSION 6 — DEPLOYMENT QUICK REFERENCE
# ──────────────────────────────────────────────────
# Save              : pickle.dump(pipeline, open("full_pipeline","wb"))
# Load              : model = pickle.load(open("full_pipeline","rb"))
# Predict           : model.predict(pd.DataFrame([input_dict]))
# Flask route       : @app.route("/", methods=["GET","POST"])
# Read form         : request.form["field_name"]
# Render HTML       : render_template("main.html", prediction=result)
# Full pipeline     : Pipeline([("pre",ColumnTransformer(...)),("model",Estimator())])

