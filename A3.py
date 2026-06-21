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
