"""
WHAT IS REGULARIZATION?
Regularization is a technique that adds a penalty term to the loss function of a
regression model to prevent overfitting.  Without regularization, a model may fit
training data perfectly but perform poorly on new data (high variance / overfitting).

FORMULAS:
  OLS Loss        = Σ(yᵢ - ŷᵢ)²
  Ridge Loss (L2) = Σ(yᵢ - ŷᵢ)² + λ·Σβⱼ²
  Lasso Loss (L1) = Σ(yᵢ - ŷᵢ)² + λ·Σ|βⱼ|

  λ (lambda) = regularization strength
  Higher λ → stronger penalty → smaller coefficients

# LaTeX equivalents:
#   OLS:   J(\\beta) = \\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2
#   Ridge: J(\\beta) = \\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2 + \\lambda\\sum_{j=1}^{k}\\beta_j^2
#   Lasso: J(\\beta) = \\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2 + \\lambda\\sum_{j=1}^{k}|\\beta_j|

5 KEY ROLES OF REGULARIZATION:
  1. Prevents Overfitting      → penalizes large coefficients; model generalizes better
  2. Handles Multicollinearity → Ridge stabilizes coefficients when predictors are correlated
  3. Feature Selection (Lasso) → L1 penalty can drive some coefficients exactly to ZERO
  4. Bias-Variance Tradeoff    → introduces small bias, dramatically reduces variance
  5. Controls Model Complexity → acts as a constraint on the hypothesis space

EXAM TIP — 4 points for full marks:
  (1) overfitting problem it solves
  (2) penalty term formula (Ridge vs Lasso)
  (3) Ridge vs Lasso key difference
  (4) role of λ hyperparameter
"""


# ─── Q1b (Feb 2025) ──────────────────────────────────────────────────────────
# Q: What is the difference between R² and Adjusted R², and when should each
#    be used?
# Marks: 5
# ─────────────────────────────────────────────────────────────────────────────

"""
FORMULAS:
  R²        = 1 - (SS_res / SS_tot)
  SS_res    = Σ(yᵢ - ŷᵢ)²        # Sum of Squared Residuals (model error)
  SS_tot    = Σ(yᵢ - ȳ)²         # Total Sum of Squares   (total variance)

  Adjusted R² = 1 - [ (1 - R²) · (n - 1) / (n - k - 1) ]
  n = number of observations | k = number of predictors

# LaTeX equivalents:
#   R^2 = 1 - \\frac{SS_{res}}{SS_{tot}}
#   \\bar{R}^2 = 1 - \\frac{(1 - R^2)(n-1)}{n - k - 1}

COMPARISON TABLE:
  Aspect                  R²                          Adjusted R²
  ─────────────────────── ─────────────────────────── ────────────────────────────
  Full Name               Coefficient of Determination  Adjusted Coeff. of Det.
  Range                   0 to 1 (rarely negative)      Can be lower than R²
  Adding a predictor      Always increases or stays same  Increases ONLY if useful
  Penalizes extra features  No                          Yes
  Use when                Single predictor / SLR        Multiple predictors / MLR
  Formula uses n, k?      No                            Yes

INTUITION EXAMPLE:
  Suppose R² = 0.80. You add a random noise variable (useless predictor).
  → R²         becomes 0.81  (increased, because it always does)
  → Adjusted R² drops to 0.78 (correctly flags the feature as unhelpful)

WHEN TO USE WHICH:
  Use R²          → only when models have the exact same number of predictors
  Use Adjusted R² → whenever comparing models with different numbers of predictors
"""


# ─── Q1c (Feb 2025) ──────────────────────────────────────────────────────────
# Q: What are Wrapper Methods in feature selection, and how are they applied
#    in Linear Regression?
# Marks: 5
# ─────────────────────────────────────────────────────────────────────────────

"""
THREE CATEGORIES OF FEATURE SELECTION:
  Category          How it Works                           Examples
  ──────────────── ────────────────────────────────────── ─────────────────────
  Filter Methods    Statistical tests; no model involved    Correlation, Chi², VIF
  Wrapper Methods   Uses a model to evaluate feature subsets  RFE, Forward/Backward
  Embedded Methods  Feature selection built into training   Lasso, Ridge, Trees

WRAPPER METHODS — DEFINITION:
  Treat feature selection as a search problem.  Evaluate subsets of features by
  training a model on each subset and measuring cross-validation performance.
  The subset giving the best model performance is selected.

THREE TYPES OF WRAPPER METHODS:
  1. Forward Selection   → Start with 0 features; add best one each step
  2. Backward Elimination → Start with ALL features; remove weakest one each step
  3. RFE (Recursive Feature Elimination):
       Train model → rank features by |βⱼ| → remove weakest → retrain → repeat
       until desired number of features remains

PYTHON EXAMPLE — RFE:
  from sklearn.feature_selection import RFE
  from sklearn.linear_model import LinearRegression

  model = LinearRegression()
  rfe   = RFE(estimator=model, n_features_to_select=3)   # keep top 3
  rfe.fit(X_train, y_train)
  print(rfe.support_)   # True/False for each feature
  print(rfe.ranking_)   # rank 1 = selected; higher = eliminated earlier

DISADVANTAGE:
  Computationally expensive — up to 2^p model fits needed for p features.
  That is why RFE (fixed step size) is preferred over exhaustive search.
"""


# ─── Q1d (Feb 2025) ──────────────────────────────────────────────────────────
# Q: How does Bayesian Optimization work, and how can it be used to tune
#    hyperparameters of a Linear Regression model?
# Marks: 5
# ─────────────────────────────────────────────────────────────────────────────

"""
WHY NOT GRID SEARCH OR RANDOM SEARCH?
  Grid Search   → Exhaustive; tries every combination; very slow
  Random Search → Faster but does NOT learn from past trials
  Bayesian Opt  → Learns from past evaluations; intelligently picks next hyperparameter

HOW BAYESIAN OPTIMIZATION WORKS (step-by-step):
  1. Define Objective Function:
       f(λ) = validation RMSE when training with hyperparameter λ
       Goal: minimize f

  2. Build a Surrogate Model:
       Use a Gaussian Process (GP) to model f(λ).
       GP gives a prediction AND uncertainty estimate for any untried λ.

  3. Acquisition Function:
       Decides where to sample next.
       Common choices: Expected Improvement (EI), Upper Confidence Bound (UCB)
       Balances EXPLORATION (uncertain regions) vs EXPLOITATION (promising regions)

  4. Evaluate and Update:
       Train model with chosen λ → get actual f(λ) → update GP with new point

  5. Repeat until budget exhausted; return best λ found.

FOR RIDGE REGRESSION — TUNING α (FORMULA):
  Objective:    α* = argmin  RMSE( Ridge(α) )
  Search space: α ∈ [0.001, 100]  (log scale)

# LaTeX:
#   \\alpha^* = \\arg\\min_{\\alpha} \\; \\text{RMSE}(\\text{Ridge}(\\alpha))

PYTHON EXAMPLE — scikit-optimize:
  from skopt import gp_minimize
  from skopt.space import Real
  from sklearn.linear_model import Ridge
  from sklearn.model_selection import cross_val_score

  def objective(params):
      alpha = params[0]
      model = Ridge(alpha=alpha)
      score = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_rmse')
      return -score.mean()

  result = gp_minimize(objective,
                       [Real(0.001, 100.0, prior='log-uniform')],
                       n_calls=20)
  print(f"Best alpha: {result.x[0]:.4f}")

KEY ADVANTAGE:
  Finds near-optimal hyperparameters in 10–50 iterations vs hundreds for Grid/Random Search.
"""


# ─────────────────────────────────────────────────────────────────────────────
# PAPER 2 — MAY 2025  |  Section A Theory (20 Marks)
# 4 questions × 5 marks each
# Note: May 2025 uses a Laptop dataset (vs Fish in Feb 2025).
#       Questions 1b and 1c overlap with Feb 2025 — see cross-references below.
# ─────────────────────────────────────────────────────────────────────────────

# ─── Q1a (May 2025) ──────────────────────────────────────────────────────────
# Q: Describe the key assumptions of linear regression.  For each, explain the
#    verification technique and impact of violation.
# Marks: 5  |  MAY 2025 UNIQUE
# ─────────────────────────────────────────────────────────────────────────────

"""
MNEMONIC: L-I-N-E-R  (Linearity · Independence · Normality · Equal Variance · Reduced Collinearity)

  Assumption         What it Means                  How to Verify               Impact if Violated
  ──────────────── ──────────────────────────────── ─────────────────────────── ────────────────────────
  1. Linearity      Y has a linear relationship      Scatter plots Y vs each X;  Biased coefficients;
                    with each Xᵢ                     Residual vs Fitted plot      systematic under/over-predict
  2. Independence   Residuals are independent        Durbin-Watson stat ≈ 2       SE underestimated;
                    (no autocorrelation)              (residual sequence plot)     t-tests unreliable
  3. Normality      Residuals are normally           Q-Q plot (diagonal line);    Prediction intervals invalid;
                    distributed                      Shapiro-Wilk test p > 0.05   hypothesis tests unreliable
  4. Homoscedasticity Residuals have constant        Residual vs Fitted plot      SE incorrect; OLS no longer
                    variance (equal variance)        (no funnel shape);           BLUE (Best Linear Unbiased)
                                                     Breusch-Pagan test           Estimator
  5. No Multicollinearity Predictors not strongly    VIF (Variance Inflation      Unstable, unreliable
                    correlated with each other       Factor) — VIF > 5 or 10     coefficients; large SE
                                                     is problematic

VIF FORMULA:
  VIF_j = 1 / (1 - R²_j)
  R²_j  = R² from regressing feature j on all other features

  VIF = 1    → no multicollinearity
  VIF > 5    → moderate multicollinearity
  VIF > 10   → severe multicollinearity

# LaTeX:
#   \\text{VIF}_j = \\frac{1}{1 - R^2_j}
"""


# ─── Q1b (May 2025) ──────────────────────────────────────────────────────────
# Q: What is regularization?  Compare Lasso and Ridge — formulation,
#    coefficient impact, use cases.
# Marks: 5  |  SIMILAR TO FEB 2025 Q1a — see answer above
# ─────────────────────────────────────────────────────────────────────────────

"""
→ Refer to Feb 2025 Q1a for the full answer.

ADDITIONAL DETAIL — RIDGE VS LASSO DEEP COMPARISON:

  FORMULAS:
    OLS:         min  Σ(yᵢ - ŷᵢ)²
    Ridge (L2):  min  Σ(yᵢ - ŷᵢ)² + λ·Σβⱼ²      # squared penalty
    Lasso (L1):  min  Σ(yᵢ - ŷᵢ)² + λ·Σ|βⱼ|     # absolute value penalty
    ElasticNet:  min  Σ(yᵢ - ŷᵢ)² + λ₁·Σ|βⱼ| + λ₂·Σβⱼ²  # mix of both

  # LaTeX:
  #   \\text{Ridge}: \\min_\\beta \\sum(y_i-\\hat{y}_i)^2 + \\lambda\\sum_j \\beta_j^2
  #   \\text{Lasso}: \\min_\\beta \\sum(y_i-\\hat{y}_i)^2 + \\lambda\\sum_j |\\beta_j|

  Aspect                  Ridge (L2)                     Lasso (L1)
  ─────────────────────── ───────────────────────────── ─────────────────────────
  Penalty Term            λ·Σβⱼ²                         λ·Σ|βⱼ|
  Coefficient Behavior    Shrinks toward 0, never = 0    Can set exactly to 0
  Geometry                Circular (L2 ball)             Diamond (L1 ball; corners→zeros)
  Closed-form solution?   Yes: β̂ = (XᵀX + λI)⁻¹Xᵀy    No (coordinate descent)
  Best for                Multicollinearity; many small   Sparse models; auto feature
                          predictors                      selection
  Correlated features     Distributes weight equally      Picks one, ignores others
  When λ→∞               All βⱼ → 0 (never exactly 0)   All βⱼ = 0 exactly

  # LaTeX (Ridge closed form):
  #   \\hat{\\beta}_{ridge} = (X^\\top X + \\lambda I)^{-1} X^\\top y

KEY INSIGHT (Geometry):
  Lasso produces exactly-zero coefficients because the L1 constraint region
  (diamond shape) has corners at the axes.  When the OLS error ellipse meets the
  diamond, it most often hits a corner → βⱼ = 0.
"""


# ─── Q1c (May 2025) ──────────────────────────────────────────────────────────
# Q: What is Recursive Feature Elimination (RFE)?  How it works, advantages,
#    limitations, and use in linear regression.
# Marks: 5  |  MAY 2025 UNIQUE
# ─────────────────────────────────────────────────────────────────────────────

"""
RFE ALGORITHM — STEP BY STEP:
  1. Start:     Train a Linear Regression model using ALL features
  2. Rank:      Rank features by coefficient magnitude |βⱼ| (larger = more important)
  3. Eliminate: Remove the feature(s) with the smallest coefficient magnitude
  4. Retrain:   Train a new model on the remaining features
  5. Repeat:    Steps 2–4 until only k features remain (k = target number)
  6. Evaluate:  Use cross-validation to determine optimal k

ADVANTAGES vs LIMITATIONS:
  Advantages                                   Limitations
  ─────────────────────────────────────────── ─────────────────────────────────
  Considers feature interactions via training  Computationally expensive (many fits)
  Works with any model that has importances    Results depend on base estimator
  Provides feature ranking, not just selection Sensitive to correlated features
  RFECV for automatic optimal k selection      Not ideal for very high-d data

PYTHON EXAMPLE — RFECV:
  from sklearn.feature_selection import RFECV
  from sklearn.linear_model import LinearRegression

  model = LinearRegression()
  rfecv = RFECV(estimator=model,
                step=1,           # remove 1 feature per iteration
                cv=5,             # 5-fold cross-validation
                scoring='r2')     # metric to optimize
  rfecv.fit(X_train, y_train)
  print(f"Optimal features: {rfecv.n_features_}")
  print(f"Selected:         {X.columns[rfecv.support_]}")
"""


# ─── Q1d (May 2025) ──────────────────────────────────────────────────────────
# Q: Describe key steps in building a supervised ML pipeline from data
#    ingestion to model deployment.
# Marks: 5  |  MAY 2025 UNIQUE
# ─────────────────────────────────────────────────────────────────────────────

"""
END-TO-END ML PIPELINE:
  Stage               What Happens                          Tools / Techniques
  ─────────────────── ───────────────────────────────────── ─────────────────────────
  1  Data Ingestion   Load raw data from source             pandas, SQL, APIs, CSV, S3
  2  EDA              Understand distributions, outliers    matplotlib, seaborn, describe()
  3  Preprocessing    Missing values, encoding, scaling     SimpleImputer, LabelEncoder,
                                                            StandardScaler
  4  Feature Eng.     Create / remove features              VIF, RFE, domain knowledge
  5  Model Selection  Choose algorithm(s)                   Linear, Lasso, Ridge, ElasticNet
  6  Training         Fit model on training data            sklearn fit(), statsmodels OLS
  7  Evaluation       Assess on test data                   RMSE, MAPE, R², cross-validation
  8  Hyperparameter   Optimize model parameters             GridSearchCV, Bayesian Opt.
     Tuning
  9  Deployment       Serve model via API                   Flask, FastAPI, Docker, joblib
  10 Monitoring       Track production performance          MLflow, data drift detection

SKLEARN PIPELINE (BEST PRACTICE):
  from sklearn.pipeline import Pipeline
  from sklearn.preprocessing import StandardScaler
  from sklearn.linear_model import Ridge

  pipe = Pipeline([
      ('scaler', StandardScaler()),    # step 1: scale features
      ('model',  Ridge(alpha=1.0))     # step 2: train ridge model
  ])
  pipe.fit(X_train, y_train)
  predictions = pipe.predict(X_test)  # scaler + model applied automatically
"""


# ─────────────────────────────────────────────────────────────────────────────
# PAPER 3 — NOVEMBER 2021  |  Section A Theory (20 Marks)
# 5 questions × 4 marks each
# ─────────────────────────────────────────────────────────────────────────────

# ─── Q1a (Nov 2021) ──────────────────────────────────────────────────────────
# Q: Write the cost function for Linear Regression with RIDGE regularization
# Marks: 4
# ─────────────────────────────────────────────────────────────────────────────

"""
OLS COST FUNCTION (no regularization):
  J(β) = Σᵢ₌₁ⁿ (yᵢ − ŷᵢ)²
       = Σᵢ₌₁ⁿ (yᵢ − β₀ − β₁x₁ᵢ − ... − βₖxₖᵢ)²

# LaTeX:
#   J(\\beta) = \\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2

RIDGE (L2) COST FUNCTION:
  J_Ridge(β) = Σᵢ₌₁ⁿ (yᵢ − ŷᵢ)² + λ · Σⱼ₌₁ᵏ βⱼ²

  Matrix form:
  J_Ridge(β) = (y − Xβ)ᵀ(y − Xβ) + λ · βᵀβ

  Closed-form solution:
  β̂_ridge = (XᵀX + λI)⁻¹ Xᵀy

# LaTeX:
#   J_{ridge}(\\beta) = (y - X\\beta)^\\top(y - X\\beta) + \\lambda\\beta^\\top\\beta
#   \\hat{\\beta}_{ridge} = (X^\\top X + \\lambda I)^{-1} X^\\top y

KEY NOTES FOR 4 MARKS:
  (1) Full formula showing RSS + λ·Σβⱼ²
  (2) λ is the hyperparameter controlling penalty strength (λ ≥ 0)
  (3) β₀ (intercept) is typically NOT penalized
  (4) Closed-form solution — the λI term makes (XᵀX + λI) always invertible,
      solving the multicollinearity problem

  λ = 0    → reduces to OLS
  λ → ∞   → all βⱼ → 0  (but never exactly zero — that is Lasso's property)
"""


# ─── Q1b (Nov 2021) ──────────────────────────────────────────────────────────
# Q: How does Adjusted R² differ from R²? Role of Adjusted R² in feature
#    selection.
# Marks: 4  |  SIMILAR TO FEB 2025 Q1b — see above for full answer
# ─────────────────────────────────────────────────────────────────────────────

"""
→ Refer to Feb 2025 Q1b for the full answer.

COMPACT VERSION:
  R²      = 1 − SS_res / SS_tot  =  1 − Σ(y−ŷ)² / Σ(y−ȳ)²
  Adj R²  = 1 − (1 − R²) · (n−1) / (n−k−1)
  n = observations | k = predictors

ROLE IN FEATURE SELECTION:
  When adding feature X_new:
    Adj R² increases → feature is genuinely useful → keep it
    Adj R² decreases → feature adds no value       → remove it

  Used as selection criterion in forward selection and backward elimination.
  The model with the highest Adj R² among competing models is preferred.
"""


# ─── Q1c (Nov 2021) ──────────────────────────────────────────────────────────
# Q: p-value for 'advertisement cost' t-test = 0.02.  What is your inference?
# Marks: 4  |  APPLIED / INTERPRETATION QUESTION
# ─────────────────────────────────────────────────────────────────────────────

"""
MODEL CONTEXT:
  Sales = β₀ + β₁·price + β₂·adv_cost + β₃·promo_cost

HYPOTHESIS TEST FOR β₂ (advertisement cost):
  H₀: β₂ = 0   (advertisement cost has NO effect on sales)
  H₁: β₂ ≠ 0   (advertisement cost has a significant effect)

  t-statistic  = β̂₂ / SE(β̂₂)
  p-value      = P(|t| > |t_observed| | H₀ is true) = 0.02

INFERENCE:
  The p-value (0.02) < α = 0.05 (standard significance level)
  → REJECT H₀

  Conclusion: 'advertisement cost' is STATISTICALLY SIGNIFICANT at the 5% level.
  There is sufficient evidence that advertisement cost has a meaningful relationship
  with unit sales of mobile phones.

  Practical implication: advertisement cost should be RETAINED in the model.
  The coefficient β̂₂ tells us the expected change in unit sales for each 1-unit
  increase in advertisement cost, holding price and promo cost constant.

NOTE: At the 1% level (p < 0.01) it would NOT be significant.
      Result is significant at 5%, not at 1%.
"""


# ─── Q1d (Nov 2021) ──────────────────────────────────────────────────────────
# Q: RMSE(salary model) = 12,324 and RMSE(age model) = 55.
#    Comment on performance.
# Marks: 4  |  TRAP QUESTION — DIFFERENT SCALES
# ─────────────────────────────────────────────────────────────────────────────

"""
FORMULA:
  RMSE = sqrt[ (1/n) · Σ(yᵢ − ŷᵢ)² ]

# LaTeX:
#   \\text{RMSE} = \\sqrt{\\frac{1}{n}\\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2}

THE TRAP — YOU CANNOT COMPARE RMSE ACROSS DIFFERENT SCALES:
  Salary model RMSE = 12,324 → units are RUPEES (same as salary target)
  Age model    RMSE = 55     → units are YEARS  (same as age target)
  → These are INCOMPARABLE — different units, different scales!

COMMON WRONG ANSWER (avoid this):
  "RMSE = 55 means age model is better than salary model" — WRONG.
  You cannot compare RMSE values across models with different target variables.

CORRECT ANSWER:
  Salary model (RMSE = 12,324):
    Off by ~₹12,324 on average.
    If average salary = ₹5,00,000 → error is ~2.5% → EXCELLENT
    If average salary = ₹30,000   → error is ~41%  → POOR

  Age model (RMSE = 55):
    Off by ~55 years on average.
    Human age range ≈ 0–100 → RMSE of 55 ≈ 55% of range → VERY POOR

KEY TAKEAWAY:
  Use MAPE (Mean Absolute Percentage Error) or normalized RMSE (RMSE / mean(y))
  for fair comparison across models with different scales.
"""


# ─── Q1e (Nov 2021) ──────────────────────────────────────────────────────────
# Q: If we increase λ, what happens to Ridge coefficients?
# Marks: 4
# ─────────────────────────────────────────────────────────────────────────────

"""
RIDGE CLOSED-FORM:
  β̂_ridge = (XᵀX + λI)⁻¹ Xᵀy

# LaTeX:
#   \\hat{\\beta}_{ridge} = (X^\\top X + \\lambda I)^{-1} X^\\top y

AS λ INCREASES:
  (XᵀX + λI)⁻¹ becomes smaller in magnitude → β̂_ridge shrinks toward 0

  λ = 0    : β̂_ridge = β̂_OLS     (no regularization)
  λ → ∞   : β̂_ridge → 0          (all coefficients approach zero)
  0 < λ   : All βⱼ shrink proportionally — NEVER become exactly 0

EFFECTS:
  (1) All coefficients shrink toward zero (never reach exactly zero)
  (2) Model becomes simpler
  (3) Bias INCREASES (model no longer fits training data perfectly)
  (4) Variance DECREASES (more stable predictions on new data)
  (5) Test error may decrease up to the optimal λ, then increase (underfitting)

RIDGE vs LASSO KEY DISTINCTION:
  Ridge (L2): λ↑ → coefficients shrink toward 0, NEVER become exactly 0 (smooth shrinkage)
  Lasso (L1): λ↑ → some coefficients become EXACTLY 0 (sparse, automatic feature selection)
"""


# ─────────────────────────────────────────────────────────────────────────────
# PAPER 4 — AUGUST 2023  |  Section A Theory (20 Marks)
# 5 questions × 4 marks each
# NOTE: Aug 2023 Section A ≈ near-identical to March 2024 Section A.
#       Unique question is Q1c (Assumptions) — below.
#       All others: see March 2024 answers.
# ─────────────────────────────────────────────────────────────────────────────

# ─── Q1a/b/d/e (Aug 2023) ────────────────────────────────────────────────────
# Q1a: Multicollinearity       → see March 2024 Q1a
# Q1b: k-fold Cross Validation → see March 2024 Q1b
# Q1d: Forward Feature Selection → see June 2024 Q1d
# Q1e: Overfitting / Bias-Variance → see June 2024 Q1e / March 2024 Q1e

# ─── Q1c (Aug 2023) ──────────────────────────────────────────────────────────
# Q: Explain the assumptions of Linear Regression.
# Marks: 4  |  ALSO ASKED IN JUN 2024 Q1a — SAME TOPIC
# ─────────────────────────────────────────────────────────────────────────────

"""
L-I-N-E-R MNEMONIC — FULL TABLE:

  Assumption         Formal Statement                  Visual Test           Statistical Test      Violation Impact
  ──────────────── ──────────────────────────────── ─────────────────────── ─────────────────── ─────────────────────
  Linearity         E[y|X] = Xβ                       Residuals vs Fitted     Rainbow test          Biased predictions
                    (linear in parameters)             → random around 0
  Independence      Cov(εᵢ, εⱼ) = 0  for i≠j         Residual sequence plot  Durbin-Watson ≈ 2     Underestimated SE
  Normality         ε ~ N(0, σ²)                       Q-Q Plot (diagonal)    Shapiro-Wilk p>0.05   Invalid t/F tests
  Equal Variance    Var(εᵢ) = σ²  (homoscedasticity)  Scale-Location flat    Breusch-Pagan p>0.05  Incorrect SE; not BLUE
  Reduced Collin.   No perfect linear dependence       Correlation heatmap    VIF < 5–10             Unstable coefficients
                    among predictors

# LaTeX (Independence):
#   \\text{Cov}(\\varepsilon_i, \\varepsilon_j) = 0 \\quad \\forall i \\neq j

# LaTeX (Normality):
#   \\varepsilon \\sim \\mathcal{N}(0, \\sigma^2)
"""


# ─── Q1e (Aug 2023) ──────────────────────────────────────────────────────────
# Q: How to reduce overfitting in Linear Regression? What is bias-variance
#    tradeoff?
# Marks: 4
# ─────────────────────────────────────────────────────────────────────────────

"""
BIAS-VARIANCE DECOMPOSITION:
  Total Error = Bias² + Variance + Irreducible Noise (σ²)

  Bias(ŷ)    = E[ŷ] − y         # systematic error — how wrong on average
  Variance   = E[(ŷ − E[ŷ])²]  # how much predictions vary across datasets
  σ²         = inherent data noise (cannot be reduced)

# LaTeX:
#   E[(y - \\hat{y})^2] = \\text{Bias}(\\hat{y})^2 + \\text{Var}(\\hat{y}) + \\sigma^2
#   \\text{Bias}(\\hat{y}) = E[\\hat{y}] - y
#   \\text{Var}(\\hat{y})  = E[(\\hat{y} - E[\\hat{y}])^2]

  Underfitting: High Bias + Low Variance  (too simple model)
  Overfitting:  Low Bias  + High Variance  (too complex model)
  Optimal:      Low Bias  + Low Variance   (regularization achieves this)

METHODS TO REDUCE OVERFITTING:
  Method                   Mechanism
  ─────────────────────── ────────────────────────────────────────────────────
  Ridge (L2)               Add λΣβⱼ² penalty → shrinks coefficients → ↓variance
  Lasso (L1)               Add λΣ|βⱼ| penalty → zeros features → sparse model
  Cross-validation         Detect gap between train vs validation performance
  Feature selection        Remove irrelevant features (VIF, p-values, RFE)
  More training data       More examples → ↓variance (model can't memorize)
"""


# ─────────────────────────────────────────────────────────────────────────────
# PAPER 5 — MARCH 2024  |  Section A Theory (20 Marks)
# 5 questions × 4 marks each
# ─────────────────────────────────────────────────────────────────────────────

# ─── Q1a (Mar 2024) ──────────────────────────────────────────────────────────
# Q: What is Multicollinearity? How to detect it and which variables are involved?
# Marks: 4
# ─────────────────────────────────────────────────────────────────────────────

"""
DEFINITION:
  Multicollinearity occurs when two or more independent variables (predictors) in
  a regression model are highly linearly correlated with each other.
  This makes it difficult for OLS to isolate the individual effect of each predictor.

FORMAL STATEMENT:
  If X_j ≈ c₀ + c₁X₁ + c₂X₂ + ...  (linear combination of other predictors)
  then:
    Var(β̂_j) = σ² / (Σxᵢⱼ² · (1 − R²_j))  → becomes very large
    VIF_j    = 1 / (1 − R²_j)

# LaTeX:
#   \\text{VIF}_j = \\frac{1}{1-R^2_j}
#   \\text{where } R^2_j \\text{ = } R^2 \\text{ from regressing } X_j \\text{ on all other predictors}

DETECTION METHODS:
  Method                  How                                        Threshold
  ───────────────────── ─────────────────────────────────────────── ──────────────────
  VIF                    Regress each X_j on all others; VIF_j=1/(1-R²_j)  VIF>5=moderate; VIF>10=severe
  Correlation Matrix     Pairwise Pearson correlations               |r| > 0.8 = suspect
  Condition Number       Ratio of largest to smallest eigenvalue of XᵀX  >30=moderate; >100=severe
  Eigenvalue Analysis    Near-zero eigenvalues of XᵀX               eigenvalue < 0.01 = problematic

WHICH VARIABLES ARE INVOLVED:
  Multicollinearity is between the PREDICTOR variables (X), NOT between X and y.

  Real examples:
    Fish dataset:    V_length, D_length, C_length — all measure fish length → VIF > 50
    Admission:       Percent_SSC, Percent_HSC, Percent_Degree — academic %s correlate
    Insurance:       age and charges interact indirectly through smoker status

REMEDIES:
  1. Remove one of the correlated variables (iterative VIF-based removal)
  2. Ridge Regression → β̂ = (XᵀX + λI)⁻¹Xᵀy  (λI makes matrix always invertible)
  3. PCA             → decorrelates predictors into orthogonal components
  4. Collect more data → increases statistical power
"""


# ─── Q1b (Mar 2024) ──────────────────────────────────────────────────────────
# Q: Explain the procedure involved in k-fold Cross Validation.
# Marks: 4  |  ALSO ASKED JUN 2024 (implicit)
# ─────────────────────────────────────────────────────────────────────────────

"""
PURPOSE:
  Estimate how well a model generalizes to unseen data, using ONLY training data.
  More reliable than a single train-validation split.  Combats overfitting.

PROCEDURE (k steps):
  1. Partition: shuffle data; split into k equal folds.  Common: k=5 or k=10.
  2. Loop k times:
       Fold i = validation set
       Remaining k−1 folds = training set
  3. Train & Evaluate: fit model on k−1 folds; compute metric on fold i.
  4. Aggregate: compute mean and std of k scores.

FORMULAS:
  CV_score       = (1/k) · Σᵢ₌₁ᵏ Score(fold_i)
  Bias_error     = 1 − mean(R²_folds)   # systematic underfitting
  Variance_error = std(R²_folds)         # inconsistency across folds

# LaTeX:
#   CV_{score} = \\frac{1}{k}\\sum_{i=1}^{k} \\text{Score}(\\text{fold}_i)

k-VALUE TRADEOFFS:
  k value         Bias      Variance    Computation
  ────────────── ───────── ─────────── ────────────
  k = 2           High      Low         Fast
  k = 5 (standard) Moderate Moderate   Moderate
  k = 10          Low       Moderate+  Slower
  k = n (LOOCV)   Very Low  High        Very slow
"""


# ─── Q1c (Mar 2024) ──────────────────────────────────────────────────────────
# Q: Discuss the need for data transformations in linear regression + techniques
# Marks: 4  |  UNIQUE TO MARCH 2024
# ─────────────────────────────────────────────────────────────────────────────

"""
WHY TRANSFORM DATA?
  OLS assumes: linearity, normality of residuals, homoscedasticity.
  Real data often violates these.  Transformations fix the violation WITHOUT
  changing the model class.

  Problem                  Transformation    Formula                    Use Case
  ──────────────────────── ──────────────── ─────────────────────────── ─────────────────────
  Right-skewed target      Log Transform     y* = log(y)                Salary, price, count data
  Skewed target (general)  BoxCox            y* = (yᵅ − 1) / λ         Any positive skewed variable
  Square-root relationship Square Root       y* = sqrt(y)               Count data, Poisson-like
  Features on diff. scales StandardScaler    x* = (x − μ) / σ          Ridge / Lasso (scale-sensitive)
  Features on diff. scales MinMaxScaler      x* = (x−min)/(max−min)    When bounded [0,1] range needed
  Non-linear X–y relation  Polynomial        Add X², X³, X₁·X₂         Curved scatter plots
  Multiplicative relation  Log-Log           log(y) = β·log(x)          Elasticity models, economics
  Binary categorical       Dummy Encoding    n−1 binary columns         All categorical features

# LaTeX (StandardScaler):
#   x^* = \\frac{x - \\mu}{\\sigma}
# LaTeX (MinMaxScaler):
#   x^* = \\frac{x - x_{min}}{x_{max} - x_{min}}
# LaTeX (BoxCox):
#   y^* = \\frac{y^\\lambda - 1}{\\lambda}

KEY INTERPRETATION CHANGE AFTER LOG TRANSFORM:
  If y* = log(y):  β means "a 1-unit increase in X changes log(y) by β"
  Percentage interpretation: %ΔY ≈ β × ΔX × 100  (for small ΔX)
  Always back-transform: ŷ = exp(ŷ*)  when reporting results
"""


# ─── Q1d (Mar 2024) ──────────────────────────────────────────────────────────
# Q: Explain the procedure involved in Forward Feature Selection.
# Marks: 4  |  SAME AS JUN 2024 Q1d — see below
# ─────────────────────────────────────────────────────────────────────────────

# → See June 2024 Q1d for the full detailed answer.

"""
COMPACT VERSION:
  0. Start:  M₀ = empty model (intercept only)
  1. Candidate evaluation: for each feature X_j NOT yet in model,
     compute performance of model + X_j
  2. Best addition: add X_j* with maximum improvement
  3. Stop when: no remaining feature provides significant improvement

Backward Elimination (reverse):
  Start with ALL features → remove least useful one at a time
  SFS from mlxtend: SequentialFeatureSelector(lr, k_features='best', forward=False)
"""


# ─── Q1e (Mar 2024) ──────────────────────────────────────────────────────────
# Q: Strategies to mitigate overfitting + forms of Linear Regression addressing it
# Marks: 4  |  ALSO JUN 2024 Q1e — see below
# ─────────────────────────────────────────────────────────────────────────────

"""
  Strategy                     How it Reduces Overfitting
  ─────────────────────────── ────────────────────────────────────────────────
  Ridge (L2 regularization)    Penalizes β² → shrinks coefficients → ↓variance
  Lasso (L1 regularization)    Zeros out irrelevant features → auto feature sel.
  ElasticNet                   L1 + L2 combined → best of both worlds
  Feature selection            VIF, RFE, SFS → removes redundant features
  Cross-validation             Detects overfitting during training
  More training data           ↓variance (model can't memorize with more examples)
"""


# ─────────────────────────────────────────────────────────────────────────────
# PAPER 6 — JUNE 2024  |  Section A Theory (20 Marks)
# 5 questions × 4 marks each
# ─────────────────────────────────────────────────────────────────────────────

# ─── Q1a (Jun 2024) ──────────────────────────────────────────────────────────
# Q: Explain the relation between Bias and Variance in a linear regression model
# Marks: 4
# ─────────────────────────────────────────────────────────────────────────────

"""
MATHEMATICAL DECOMPOSITION:
  For any estimator ŷ:
  E[(y − ŷ)²] = Bias(ŷ)² + Variance(ŷ) + Irreducible Noise (σ²)

  Bias(ŷ)    = E[ŷ] − y              # systematic error
  Variance   = E[(ŷ − E[ŷ])²]        # variability across datasets
  σ²         = inherent data noise    (cannot be reduced)

# LaTeX:
#   E[(y-\\hat{y})^2] = \\left(E[\\hat{y}] - y\\right)^2 +
#                       E\\left[(\\hat{y} - E[\\hat{y}])^2\\right] + \\sigma^2

TRADEOFF:
  Model Complexity    Bias    Variance    Result
  ─────────────────── ─────── ─────────── ─────────────────────────────────
  Too simple          HIGH    LOW         Underfitting — bad on train + test
  Just right          LOW     LOW         Good generalization ← GOAL
  Too complex         LOW     HIGH        Overfitting — great train, bad test

IN LINEAR REGRESSION SPECIFICALLY:
  OLS (no regularization): Low bias, but correlated features → high variance
  Ridge (L2):              Small bias (shrinks β) + ↓variance → better generalization
  Lasso (L1):              More bias than Ridge (zeros β) + lowest variance (sparse)

MEASURING WITH CV:
  Bias     ≈ 1 − mean(R²_folds)   (how far mean performance is from perfect)
  Variance ≈ std(R²_folds)         (how much performance fluctuates across folds)
"""


# ─── Q1b (Jun 2024) ──────────────────────────────────────────────────────────
# Q: How can regularization help in tackling overfitting?
# Marks: 4  |  ALSO FEB 2025 Q1a, MAY 2025 Q1b — see above
# ─────────────────────────────────────────────────────────────────────────────

"""
→ Refer to Feb 2025 Q1a for the full answer.

COMPACT SUMMARY:
  Overfitting: model memorizes training noise → high variance, low bias

  Ridge: L = RSS + λ·Σβⱼ²    → shrinks all coefficients toward 0
  Lasso: L = RSS + λ·Σ|βⱼ|  → zeros out unimportant coefficients

  Effect: forces simpler model → ↑bias slightly, ↓variance significantly
  Net result: better generalization (lower test error)

FOUR MARKS REQUIRE:
  (1) Define overfitting
  (2) Explain how penalty term works
  (3) Effect on bias-variance tradeoff
  (4) Role of λ — larger λ = more regularization = simpler model
"""


# ─── Q1c (Jun 2024) ──────────────────────────────────────────────────────────
# Q: n=21, 5 predictors, SS(Total)=1500, SS(Residual)=375 — Calculate R²
# Marks: 4  |  NUMERICAL
# ─────────────────────────────────────────────────────────────────────────────

"""
GIVEN:
  n = 21     (number of observations)
  k = 5      (number of predictors)
  SS(Total)   = 1500
  SS(Residual) = 375

STEP 1: SS(Regression)
  SS(Regression) = SS(Total) − SS(Residual)
                 = 1500 − 375
                 = 1125

STEP 2: R²
  R² = 1 − SS(Residual) / SS(Total)
     = 1 − 375 / 1500
     = 1 − 0.25
     = 0.75

STEP 3: Adjusted R²
  Adj R² = 1 − (1 − R²) × (n−1) / (n−k−1)
         = 1 − (1 − 0.75) × (21−1) / (21−5−1)
         = 1 − 0.25 × 20 / 15
         = 1 − 0.25 × 1.3333
         = 1 − 0.3333
         = 0.6667

# LaTeX:
#   R^2 = 1 - \\frac{SS_{res}}{SS_{tot}} = 1 - \\frac{375}{1500} = 0.75
#   \\bar{R}^2 = 1 - \\frac{(1-R^2)(n-1)}{n-k-1}
#             = 1 - \\frac{0.25 \\times 20}{15} = 0.6667

CONCLUSION:
  R² = 0.75 → model explains 75% of total variance.
  Adj R² = 0.667 → after penalizing for 5 predictors on 21 observations.
  Gap of 0.083 suggests some predictors may not be contributing meaningfully.
  With n=21 and k=5, the model uses many degrees of freedom → always report Adj R².
"""


# ─── Q1d (Jun 2024) ──────────────────────────────────────────────────────────
# Q: Explain the procedure involved in Forward Feature Selection.
# Marks: 4  |  UNIQUE TO JUN 2024 (full version)
# ─────────────────────────────────────────────────────────────────────────────

"""
ALGORITHM:
  0. Start:            M₀ = empty model (intercept only, no predictors)
  1. Candidate Addition: for each feature Xⱼ not yet in model:
       fit model with (current features + Xⱼ)
       record performance (R², AIC, p-value, or CV score)
  2. Best Addition:    add Xⱼ* giving the biggest improvement
  3. Stopping Criterion:
       (a) all remaining features are statistically non-significant (p > threshold), OR
       (b) adding more features doesn't improve CV score
  4. Final Model:      model at the stopping point

EXAMPLE WITH 3 FEATURES {X1, X2, X3}:
  Step 0: M₀ = {intercept only}
  Step 1: try M{X1}, M{X2}, M{X3}    → best is M{X2}  (R²=0.60) → add X2
  Step 2: try M{X2,X1}, M{X2,X3}     → best is M{X2,X1} (R²=0.72) → add X1
  Step 3: try M{X1,X2,X3}            → R²=0.73, tiny improvement → STOP
  Final: M = {X2, X1}

FORWARD SELECTION vs BACKWARD ELIMINATION:
  Aspect          Forward Selection        Backward Elimination
  ─────────────── ───────────────────────  ────────────────────────────
  Start           Empty model              Full model (all features)
  Action          Add best feature/step    Remove worst feature/step
  Stops when      No significant improve.  All remaining features significant
  Preferred when  p >> n (many features)   Fewer features, moderate n
  Limitation      Can't remove once added  Can't re-add once removed
"""


# ─── Q1e (Jun 2024) ──────────────────────────────────────────────────────────
# Q: Strategies to mitigate overfitting in Linear Regression + forms that
#    address it.
# Marks: 4
# ─────────────────────────────────────────────────────────────────────────────

"""
5 STRATEGIES:
  1. Regularization (Ridge/Lasso/ElasticNet):
       Add penalty to limit coefficient size — most direct approach.
  2. Feature Selection:
       Remove irrelevant features via VIF, p-values, RFE, Forward/Backward selection.
  3. Cross-Validation:
       Use k-fold CV during training to detect overfitting early.
       High CV variance → overfitting signal.
  4. Get More Data:
       More training samples → ↓variance.  Overfitting is worse with small datasets.
  5. Dimensionality Reduction (PCA):
       Reduces number of features while preserving variance.

FORMS OF LINEAR REGRESSION ADDRESSING OVERFITTING:
  Method          Penalty         Key Feature                         Formula
  ─────────────── ─────────────── ─────────────────────────────────── ──────────────────────────────
  Ridge (L2)      λΣβⱼ²           Shrinks all; never zeros out        β̂=(XᵀX+λI)⁻¹Xᵀy
  Lasso (L1)      λΣ|βⱼ|          Zeros out irrelevant → sparse model  (no closed form; coord descent)
  ElasticNet      λ₁Σ|βⱼ|+λ₂Σβⱼ²  Combines both; handles correlated groups

# LaTeX (ElasticNet):
#   J(\\beta) = \\sum(y_i-\\hat{y}_i)^2 + \\lambda_1\\sum|\\beta_j| + \\lambda_2\\sum\\beta_j^2
"""


# ─────────────────────────────────────────────────────────────────────────────
# PAPER 7 — MARCH 2021  |  Theory Questions (Q1 + Q2 = 20 Marks)
# ─────────────────────────────────────────────────────────────────────────────

# ─── Q1a (Mar 2021) ──────────────────────────────────────────────────────────
# Q: Explain Heteroscedasticity and Multicollinearity in Linear Regression
# Marks: 2
# ─────────────────────────────────────────────────────────────────────────────

"""
HETEROSCEDASTICITY:
  OLS assumes homoscedasticity: Var(εᵢ) = σ² (constant for all i).
  When variance is NOT constant → heteroscedasticity.

  Homoscedastic:    Var(εᵢ) = σ²   (constant for all i)     ← GOOD
  Heteroscedastic:  Var(εᵢ) = σᵢ²  (varies with i)          ← BAD

  Aspect                    Homoscedastic (GOOD)      Heteroscedastic (BAD)
  ───────────────────────── ─────────────────────── ─────────────────────────────
  Residual vs Fitted plot   Random scatter            Funnel/cone/expanding shape
  OLS estimates             BLUE                      Unbiased, but NOT efficient
  Standard Errors           Correct                   Underestimated → t-tests invalid
  Detection test            —                         Breusch-Pagan, White's test
  Fix                       —                         Log transform Y, WLS, robust SE

MULTICOLLINEARITY:
  VIF_j = 1 / (1 − R²_j)
  R²_j  = R² from regressing X_j on all other predictors

  VIF = 1: no collinearity | VIF > 5: moderate | VIF > 10: severe

  Aspect              Effect
  ─────────────────── ────────────────────────────────────────────────────────
  Coefficient estimates  Unstable — small data changes → huge swings in β
  Standard errors        Inflated → hard to determine which variable matters
  p-values               Unreliable
  R² overall             Still high — model fits well globally

KEY EXAM DISTINCTION:
  Heteroscedasticity → about the ERROR TERM (ε) — its variance changes
  Multicollinearity  → about the PREDICTORS (X) — they correlate with each other
"""


# ─── Q1b (Mar 2021) ──────────────────────────────────────────────────────────
# Q: Birth Weight Prediction:
#    pred_bwght = 119.77 − 0.514 × cigs
#    (i) Predicted birth weight when cigs = 0
#    (ii) Predicted birth weight when cigs = 20
# Marks: 2  |  NUMERICAL
# ─────────────────────────────────────────────────────────────────────────────

"""
MODEL:
  pred_bwght = 119.77 − 0.514 × cigs
  β₀ = 119.77   (predicted weight when cigs = 0)
  β₁ = −0.514   (each additional cigarette/day → weight drops 0.514 oz)

PART 1 — cigs = 0:
  pred_bwght = 119.77 − 0.514 × 0
             = 119.77 − 0
             = 119.77 ounces  (≈ 7.49 pounds)

PART 2 — cigs = 20:
  pred_bwght = 119.77 − 0.514 × 20
             = 119.77 − 10.28
             = 109.49 ounces  (≈ 6.84 pounds)

DIFFERENCE:
  119.77 − 109.49 = 10.28 ounces (≈ 0.643 pounds)

COMMENT:
  Babies born to mothers who smoke one pack/day are predicted to weigh about
  10.28 oz LESS — a ~8.6% reduction.  Practically significant.
  Caveat: simple regression — confounders (nutrition, maternal age) not controlled.
"""


# ─── Q1c (Mar 2021) ──────────────────────────────────────────────────────────
# Q: College GPA:
#    colgpa = 1.392 − 0.0135 × hsperc + 0.00148 × sat
#    (i) Why is the coefficient on hsperc negative?
#    (ii) SAT 140 points higher → predicted GPA difference?
#    (iii) SAT points needed for colgpa difference of 0.50?
# Marks: 3  |  NUMERICAL + INTERPRETATION
# ─────────────────────────────────────────────────────────────────────────────

"""
MODEL:
  colgpa = 1.392 − 0.0135 × hsperc + 0.00148 × sat
  β₀ = 1.392     (intercept)
  β₁ = −0.0135   (coefficient on hsperc)
  β₂ = +0.00148  (coefficient on sat)

PART 1 — Why is β₁ NEGATIVE?
  'hsperc' is the percentile rank in the graduating class where:
    lower value = better rank  (e.g., hsperc = 5 → top 5% = excellent)
  Therefore: higher hsperc → worse rank → lower college GPA → negative coefficient
  β₁ = −0.0135 correctly captures: as rank worsens (hsperc↑), colgpa decreases.

PART 2 — ΔSAT = 140, same hsperc (hsperc term cancels out):
  Δcolgpa = β₂ × ΔSAT
           = 0.00148 × 140
           = 0.2072 GPA points

  A 140-point SAT advantage → ~0.207 grade point increase.
  Moderately meaningful (≈5.2% of 4-point scale); going from 2.8 → 3.0 matters.

PART 3 — What ΔSAT gives Δcolgpa = 0.50?
  0.50  = 0.00148 × ΔSAT
  ΔSAT  = 0.50 / 0.00148
        = 337.84 ≈ 338 SAT points

  Conclusion: a 0.5 GPA improvement requires ~338 extra SAT points (~2.4 std deviations).
  SAT's individual effect is relatively modest.
"""


# ─── Q1d (Mar 2021) ──────────────────────────────────────────────────────────
# Q: How can you deal with autocorrelation of errors?
# Marks: 2
# ─────────────────────────────────────────────────────────────────────────────

"""
WHAT IS AUTOCORRELATION?
  Residuals εᵢ are correlated with residuals at previous time points εᵢ₋₁.
  Violates OLS independence assumption.

  Detection: Durbin-Watson statistic
    DW ≈ 2     → no autocorrelation
    DW < 1.5   → positive autocorrelation
    DW > 2.5   → negative autocorrelation

5 SOLUTIONS:
  1. GLS (Generalized Least Squares):
       Transforms model to account for correlation structure.
       AR(1): εᵢ = ρεᵢ₋₁ + uᵢ → estimate ρ, transform variables.

  2. Cochrane-Orcutt / Prais-Winsten:
       Iteratively estimates ρ, transforms variables, re-estimates until convergence.

  3. Newey-West HAC Standard Errors:
       Doesn't fix autocorrelation but produces CORRECT (robust) standard errors.
       Most common in practice.

  4. Include Lag Variables:
       If autocorrelation is due to omitted dynamics, add Yᵢ₋₁ as a predictor.

  5. Differencing:
       Replace Yᵢ with ΔYᵢ = Yᵢ − Yᵢ₋₁.  Common in time-series econometrics.
"""


# ─── Q1e (Mar 2021) ──────────────────────────────────────────────────────────
# Q: Difference between Classification and Regression
# Marks: 1
# ─────────────────────────────────────────────────────────────────────────────

"""
  Aspect          Regression                          Classification
  ─────────────── ─────────────────────────────────── ──────────────────────────────────
  Output Type     Continuous numeric value             Discrete category / label
  Examples        Salary, house price, weight          Spam/not-spam, disease/healthy
  Algorithms      Linear Regression, Ridge, Lasso      Logistic Regression, SVM, Decision Tree
  Loss Function   MSE, RMSE, MAE                       Cross-Entropy, Accuracy, F1
  Output Range    −∞ to +∞  (any real number)          Finite set of classes {0,1} or {A,B,C}
"""


# ─── Q2a (Mar 2021) ──────────────────────────────────────────────────────────
# Q: CEO Salary: log(Salary) = 4.32 + 0.280·log(sales) + 0.0174·roe + 0.00024·ros
#    SE(intercept) = 0.32 | SE(log sales) = 0.035 | SE(roe) = 0.0041 | SE(ros) = 0.00054
#    n = 209 | R² = 0.283 | t-critical (10%, one-tail) = 1.282
#    (i) % increase in Salary when ros increases by 50 points
#    (ii) H₀: β_ros = 0 — test and conclude
#    (iii) Would you include ros in the final model?
# Marks: 6  |  NUMERICAL
# ─────────────────────────────────────────────────────────────────────────────

"""
MODEL (log-level):
  log(Salary) = 4.32 + 0.280·log(sales) + 0.0174·roe + 0.00024·ros

PART 1 — % increase in Salary when Δros = 50:
  For a log-level model: %ΔSalary ≈ β_ros × Δros × 100

  %ΔSalary = 0.00024 × 50 × 100
           = 0.00024 × 5000
           = 1.2%

  A 50-point increase in ros → salary increases by approximately 1.2%.
  Not a practically large effect; ros is not a dominant driver of CEO pay.

PART 2 — Hypothesis test: H₀: β_ros = 0  vs  H₁: β_ros > 0

  Test Statistic:
    t = β̂_ros / SE(β̂_ros)
      = 0.00024 / 0.00054
      = 0.444

  Decision Rule: Reject H₀ if t > t_critical (10%, one-tail) = 1.282
  Since 0.444 < 1.282 → FAIL TO REJECT H₀

  Conclusion: At the 10% level, we CANNOT reject β_ros = 0.
              Insufficient evidence that ros has a positive effect on salary.

PART 3 — Include ros in final model?
  Likely NO.  Reasons:
    Statistical significance: t = 0.444, not significant even at 10%
    Practical significance:   only 1.2% salary increase per 50-point ros gain
    R² = 0.283 — only 28.3% variance explained even with ros included
    Including an insignificant variable inflates complexity; Adj R² may decrease
  However, theoretically ros should matter → could retain with caveat about weakness.
"""


# ─── Q2b (Mar 2021) ──────────────────────────────────────────────────────────
# Q: y = 2x₁ + 12x₂ + 3x₃ + 5 — How do coefficients of x₂ and x₃ affect y?
# Marks: 2  |  SAME AS SAMPLE PAPER Q1d (x₁ and x₂)
# ─────────────────────────────────────────────────────────────────────────────

"""
MODEL:
  y = 5 + 2x₁ + 12x₂ + 3x₃
  β₀ = 5  (intercept — value of y when all predictors = 0)
  β₁ = 2  (coefficient of x₁)
  β₂ = 12 (coefficient of x₂)
  β₃ = 3  (coefficient of x₃)

COEFFICIENT OF x₂ (β₂ = 12):
  Holding x₁ and x₃ constant, a 1-unit increase in x₂ → y increases by 12 units.
  x₂ has the LARGEST coefficient → most influential predictor.
  Example: x₂ goes from 2 to 3 → y increases by exactly 12.

COEFFICIENT OF x₃ (β₃ = 3):
  Holding x₁ and x₂ constant, a 1-unit increase in x₃ → y increases by 3 units.
  Positive but smaller effect than x₂.
  Example: x₃ goes from 5 to 6 → y increases by 3.

COMPARISON:
  x₂ is 4× more influential than x₃  (12 vs 3).
  CAVEAT: only meaningful if x₂ and x₃ are on the SAME SCALE.
  Use standardized (beta) coefficients for fair comparison when units differ.
"""


# ─── Q2c (Mar 2021) ──────────────────────────────────────────────────────────
# Q: Explain Gradient Descent in brief
# Marks: 2
# ─────────────────────────────────────────────────────────────────────────────

"""
CORE IDEA:
  Gradient Descent is an iterative optimization algorithm to find the MINIMUM of a
  cost/loss function.  Used when the normal equation (XᵀX)⁻¹Xᵀy is too expensive
  for large datasets.

MATHEMATICAL FOUNDATION:
  Cost Function:  J(β) = (1/2n) · Σ(yᵢ − ŷᵢ)²
  Gradient:       ∂J/∂βⱼ = (1/n) · Σ(ŷᵢ − yᵢ) · xᵢⱼ
  Update Rule:    βⱼ := βⱼ − α · ∂J/∂βⱼ

  α = learning rate (step size)  |  := means "update"

# LaTeX:
#   J(\\beta) = \\frac{1}{2n}\\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2
#   \\frac{\\partial J}{\\partial \\beta_j} = \\frac{1}{n}\\sum_{i=1}^{n}(\\hat{y}_i - y_i)x_{ij}
#   \\beta_j := \\beta_j - \\alpha \\cdot \\frac{\\partial J}{\\partial \\beta_j}

ALGORITHM STEPS:
  1. Initialize: set all β = 0 (or small random values)
  2. Compute Predictions: ŷ = Xβ
  3. Compute Error: residuals = ŷ − y
  4. Compute Gradient: ∂J/∂β = (1/n) · Xᵀ(ŷ − y)
  5. Update β: β := β − α · gradient  (move downhill)
  6. Repeat steps 2–5 until convergence (ΔJ very small)

THREE VARIANTS:
  Type             Uses               Speed       Stability
  ──────────────── ────────────────── ─────────── ──────────────────
  Batch GD         All n samples      Slow (large n)  Stable convergence
  Stochastic GD    1 sample           Fast        Noisy, may oscillate
  Mini-Batch GD    Batch of k samples Balanced    Most common in practice

LEARNING RATE α:
  Too large → overshoots minimum, may diverge
  Too small → very slow convergence
  Fix: learning rate schedules or Adam optimizer
"""


# ─────────────────────────────────────────────────────────────────────────────
# PAPER 8 — ML-1 SAMPLE PAPER  |  Section A Theory (20 Marks)
# 5 questions × 4 marks each
# ─────────────────────────────────────────────────────────────────────────────

# ─── Q1a (Sample) ────────────────────────────────────────────────────────────
# Q: What is Machine Learning? State any two types.
# Marks: 4  |  UNIQUE TO SAMPLE PAPER
# ─────────────────────────────────────────────────────────────────────────────

"""
DEFINITION:
  Machine Learning (ML) is a subfield of Artificial Intelligence (AI) that enables
  systems to LEARN PATTERNS FROM DATA and improve performance WITHOUT being explicitly
  programmed for each task.

  Formal Definition (Tom Mitchell, 1997):
  "A computer program is said to learn from Experience E with respect to some class of  Tasks T and Performance Measure P, if its performance at T, as measured by P,
   improves with experience E."

TWO TYPES OF MACHINE LEARNING:
  Type                  Description                               Examples
  ───────────────────── ───────────────────────────────────────── ───────────────────────────────
  Supervised Learning   Model learns from labeled data (X + y).   Linear Regression (price),
                        Goal: learn mapping from X to y.          Logistic Regression (spam)
  Unsupervised Learning Model finds patterns in unlabeled data    K-Means Clustering,
                        (only X, no y). Goal: discover structure. PCA, Autoencoders

  (Also: Reinforcement Learning — agent learns via rewards/penalties, e.g., game playing)
"""


# ─── Q1b (Sample) ────────────────────────────────────────────────────────────
# Q: How can you handle overfitting and underfitting?
# Marks: 4
# ─────────────────────────────────────────────────────────────────────────────

"""
DEFINITIONS:
  Underfitting: model too simple → High Bias + Low Variance
  Overfitting:  model too complex → Low Bias  + High Variance
  Goal: Low Bias + Low Variance (the sweet spot)

  Problem       Symptom                                  Solutions
  ──────────── ──────────────────────────────────────── ─────────────────────────────────────────
  Underfitting  High training AND test error;            1. Increase model complexity
                model misses patterns                    2. Reduce regularization (↓λ)
                                                         3. Train longer / more iterations
                                                         4. Add relevant features
  Overfitting   Low training error but HIGH test error;  1. Add regularization (Ridge, Lasso)
                model memorizes training data            2. Feature selection (VIF, RFE)
                                                         3. Get more training data
                                                         4. Cross-validation to detect early
                                                         5. Simpler model
"""


# ─── Q1c (Sample) ────────────────────────────────────────────────────────────
# Q: State the assumptions of linear regression.
# Marks: 4  |  ALSO AUG 2023, JUN 2024 — see Q1c Aug 2023 above
# ─────────────────────────────────────────────────────────────────────────────

"""
L-I-N-E-R (5 Assumptions):
  L  Linearity:         E[y|X] = Xβ  (linear relationship between X and y)
  I  Independence:      residuals εᵢ are independent (no autocorrelation) — DW ≈ 2
  N  Normality:         εᵢ ~ N(0, σ²) — residuals normally distributed — Q-Q plot
  E  Equal Variance:    Var(εᵢ) = σ² constant (homoscedasticity) — Breusch-Pagan
  R  Reduced Collin.:   no perfect linear dependence among X — VIF < 5

→ See Aug 2023 Q1c for the full detailed table with statistical tests and violation impacts.
"""


# ─── Q1d (Sample) ────────────────────────────────────────────────────────────
# Q: y = 2x₁ + 12x₂ + 3x₃ + 5 — Effect of x₁ and x₂ coefficients
# Marks: 4  |  SAME AS MAR 2021 Q2b
# ─────────────────────────────────────────────────────────────────────────────

"""
→ See March 2021 Q2b for the full answer.

COEFFICIENTS:
  y = 5 + 2x₁ + 12x₂ + 3x₃

EFFECT OF x₁ (β₁ = 2):
  Holding x₂, x₃ constant → 1-unit increase in x₁ → y increases by 2 units.
  Positive but relatively small effect.

EFFECT OF x₂ (β₂ = 12):
  Holding x₁, x₃ constant → 1-unit increase in x₂ → y increases by 12 units.
  x₂ is the DOMINANT predictor — 6× more influential than x₁ (12 vs 2).

CAVEAT: comparison valid only if x₁ and x₂ are on the SAME SCALE.
"""


# ─── Q1e (Sample) ────────────────────────────────────────────────────────────
# Q: Explain any two data preprocessing steps.
# Marks: 4
# ─────────────────────────────────────────────────────────────────────────────

"""
PREPROCESSING STEP 1 — MISSING VALUE TREATMENT:
  Missing values occur when data is not recorded.  Most ML algorithms cannot process NaN.

  Strategy            When to Use                         Code
  ─────────────────── ─────────────────────────────────── ────────────────────────────────────
  Drop rows           Few missing values in target        df.dropna(subset=['y'])
  Mean imputation     Numeric column, low skewness        df['col'].fillna(df['col'].mean())
  Median imputation   Numeric column with outliers        df['col'].fillna(df['col'].median())
  Mode imputation     Categorical columns                 df['col'].fillna(df['col'].mode()[0])
  Constant fill       When absence is meaningful          df['col'].fillna('missing')

PREPROCESSING STEP 2 — FEATURE SCALING:
  Features on different scales cause regularized models (Ridge, Lasso) to unfairly
  penalize features with larger magnitudes.

  StandardScaler:  z = (x − μ) / σ
    Result: mean = 0, std = 1 for each feature
    Preferred when features follow approximately normal distributions

  MinMaxScaler:    z = (x − min) / (max − min)
    Result: all values in range [0, 1]
    Use when bounded range is needed

"""

