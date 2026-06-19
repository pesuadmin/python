"""
SMLR - Supervised Machine Learning (Regression)
PES University M.Tech Data Science and AI - UE20CS905
Complete Study Guide - All Topics in Index Order
"""

#==============================================================================
# TOPIC 08: Multicollinearity and VIF
#==============================================================================

# What is Multicollinearity?
# Multicollinearity happens when two or more predictor features are strongly correlated with each other. Examples from the Fish dataset: Length1 , Length2 , Length3 are all measurements of the same fish in different directions — they correlate ~0.99. The model can't tell which one is "really" doing the work.
#  Why it's a problem
# Coefficients become unstable. Small changes in the data cause big swings in β values, even sign flips.
# Standard errors balloon. p-values become large; you may wrongly conclude "this feature isn't significant" when it actually is.
# Interpretation breaks. "Holding everything else constant" doesn't make sense if features always move together.
# Predictions usually still fine. Multicollinearity hurts interpretation more than prediction accuracy .
#  Perfect multicollinearity = math breaks
# If two features are exactly linearly related (e.g., one is a copy or sum of others), the matrix XᵀX cannot be inverted and the OLS formula fails outright. Real datasets rarely hit this — but watch out after dummy encoding (the "dummy variable trap" — drop one category!).
# How to detect multicollinearity
# 1. Correlation matrix
# Compute pairwise correlations between all features. Pairs with |r| > 0.8 are suspicious. Visualize with a heatmap ( seaborn.heatmap ).
# 2. Variance Inflation Factor (VIF) — the gold standard
# VIF formula
# VIF_j = 1 / (1 − R²_j)
# where R²_j is the R² obtained by regressing feature j on all other features.
# Intuition: if you can predict feature j very well from the other features (R²_j close to 1), then feature j carries no new information — pure multicollinearity. VIF spikes to infinity.
# VIF value Interpretation Action
# VIF = 1 No multicollinearity Feature is independent — keep
# 1 < VIF < 5 Mild — usually fine Keep, monitor
# 5 ≤ VIF < 10 Moderate — caution Consider dropping or combining
# VIF ≥ 10 Severe Drop one of the correlated features
# 3. Condition Number
# Reported in the statsmodels OLS summary. Cond. No. > 30 = caution; > 100 = severe multicollinearity.
#  How to fix multicollinearity
# Drop one of the correlated features. Simplest. If Length1, Length2, Length3 all correlate > 0.99, keep one (typically the most interpretable, e.g., Length3 = total length).
# Combine into a single feature. e.g., average of correlated features, or PCA on them.
# Use Ridge Regression. Ridge's L2 penalty stabilizes coefficients even under multicollinearity.
# Apply Principal Component Analysis (PCA). Transform correlated features into uncorrelated principal components.
# Increase sample size if feasible — more data → tighter estimates → less sensitivity.
# Python code — computing VIF
# from statsmodels.stats.outliers_influence import variance_inflation_factor import pandas as pd # Compute VIF for each feature in your X matrix vif_df = pd.DataFrame()
vif_df[ 'feature' ] = X.columns
vif_df[ 'VIF' ] = [variance_inflation_factor(X.values, i) for i in range(X.shape[ 1 ])] print (vif_df.sort_values( 'VIF' , ascending= False )) # Iteratively drop the feature with highest VIF until all VIFs are below 5 while True : vifs = [variance_inflation_factor(X.values, i) for i in range(X.shape[ 1 ])] max_vif = max(vifs) if max_vif < 5 : break drop_idx = vifs.index(max_vif) print ( f"Dropping {X.columns[drop_idx]} (VIF={max_vif:.2f})" ) X = X.drop(columns=[X.columns[drop_idx]])
#  Worked example: VIF calculation
# Say feature x₁ has R² = 0.9 when regressed on x₂, x₃, x₄. Then:
# VIF_x₁ = 1 / (1 − 0.9) = 1 / 0.1 = 10
# VIF = 10 means the variance of β̂_x₁ is 10× larger than it would be if x₁ were uncorrelated with the others. Severe — drop x₁ or merge it with a correlated feature.
# Exam questions on this topic

# What is Multicollinearity? How to detect the presence of multicollinearity and which variables are involved in it?
# Answer
# Multicollinearity = strong linear correlation between two or more predictor features in a regression model. It makes coefficient estimates unstable and standard errors inflated, harming interpretability.
# Detection methods:
# Correlation matrix — compute pairwise correlations between features. Pairs with |r| > 0.8 are suspicious. Use df.corr() + heatmap.
# Variance Inflation Factor (VIF) = 1 / (1 − R²_j), where R²_j is from regressing feature j on all others.
# VIF < 5 → safe
# 5 ≤ VIF < 10 → moderate; consider dropping
# VIF ≥ 10 → severe; drop one
# Condition Number from OLS summary > 30 indicates trouble.
# Tolerance = 1/VIF; values < 0.1 → severe.
# Identifying the involved variables: features with VIF ≥ 10 are the culprits. The correlation matrix tells you which pairs are most strongly tied (e.g., in Fish data, Length1, Length2, Length3 will all show high VIF together because they measure overlapping geometry).
# Fixes: drop redundant features (keep the most interpretable), combine into one (mean / first principal component), use Ridge regression (stabilizes via L2 penalty), or apply PCA.
# 4f / 4i / 4h Feb 2025 / / Mar 2024 / Nov 2024 each
# check and reduce multicollinearity using VIF.
# Answer (template code)
# from statsmodels.stats.outliers_influence import variance_inflation_factor import pandas as pd def compute_vif (X): vif = pd.DataFrame() vif[ 'feature' ] = X.columns vif[ 'VIF' ] = [variance_inflation_factor(X.values, i) for i in range(X.shape[ 1 ])] return vif.sort_values( 'VIF' , ascending= False ) # Iteratively drop highest VIF until all < 5 while compute_vif(X)[ 'VIF' ].max() > 5 : drop_feat = compute_vif(X).iloc[ 0 ][ 'feature' ] print ( f'Dropping {drop_feat}' ) X = X.drop(columns=[drop_feat]) print (compute_vif(X))
# Reasoning to write in the inference: "Length1, Length2, Length3 all measure overlapping geometry of the fish, hence high VIF. We retain Length3 (most representative) and drop Length1 and Length2. Final VIFs all below 5 — multicollinearity resolved."
# Multicollinearity in 3 lines
# What: predictors correlate with each other.
# Detect: VIF = 1/(1−R²); VIF > 5 = warning, > 10 = severe.
# Fix: drop one, combine, Ridge, or PCA.
# Multicollinearity = correlated predictors. Hurts interpretability, not always prediction.
# Detect with VIF (gold standard): VIF = 1/(1−R²_j). VIF < 5 OK, ≥ 10 fix it.
# Fix: drop, combine, Ridge, or PCA.
# The dummy variable trap (perfect multicollinearity after one-hot encoding) — always drop one category.

#==============================================================================
# TOPIC 09: Bias-Variance Tradeoff and Overfitting
#==============================================================================

# Underfitting vs Overfitting
# Bias-Variance Tradeoff
# Bias/variance from CV
# Strategies to reduce overfit
#  Underfitting and Overfitting
# Two ways a model can be bad:
# Underfitting Overfitting
# What Model too simple to capture the pattern Model too complex — fits noise as if it were signal
# Symptom on train High error Very low error
# Symptom on test High error (similar to train) Much higher error than train
# Cause Too few features, low-degree polynomial, too much regularization Too many features, high-degree polynomial, no regularization
# Fix Add features, increase model complexity, reduce regularization Reduce features, regularize (Ridge/Lasso), add data, cross-validate
# UNDERFIT (high bias) JUST RIGHT OVERFIT (high variance)
# Underfit ignores the curve. Overfit chases every data point including noise. Just right captures the underlying signal.
# The Bias-Variance Tradeoff
# Total expected error of a model can be decomposed into three parts:
# Bias-Variance Decomposition
# Expected Error = Bias² + Variance + Irreducible Error
# Term Definition Cause Reduce by
# Bias How far off the model's average prediction is from truth Model too simple — assumptions don't fit reality More features, complex model, less regularization
# Variance How much predictions jump around for different training sets Model too complex — too sensitive to specific training data Fewer features, regularization, more training data
# Irreducible Random noise inherent in y Real-world randomness, measurement error Cannot be removed
# model complexity → error bias² variance total ↑ sweet spot
# As model complexity grows, bias falls but variance rises. Total error is U-shaped — minimize at the sweet spot (green dot).
# Bias and variance from cross-validation
# The Feb/papers ask: "calculate the bias error (1 − mean R²) and variance error (standard deviation of R²) by performing 5-fold cross-validation."
# This is an operational definition (different from the statistical decomposition above):
# Operational definitions used in your paper
# Bias error = 1 − mean(R² scores across folds)
# Variance error = standard deviation of R² scores across folds
# Interpretation:
# High mean(1 − R²) → model under-explains variance → underfitting → bias issue.
# High std(R²) → model behaviour swings wildly across folds → overfitting → variance issue.
# from sklearn.model_selection import cross_val_score from sklearn.linear_model import LinearRegression import numpy as np model = LinearRegression()
scores = cross_val_score(model, X_train, y_train, cv= 5 , scoring= 'r2' ) bias_error = 1 - scores.mean() # operational bias variance_error = scores.std() # operational variance print ( f"Bias error: {bias_error:.4f}" ) print ( f"Variance error: {variance_error:.4f}" )
#  Strategies to reduce overfitting
# Regularization — add penalty for large coefficients (Ridge, Lasso, ElasticNet). See chapter 10.
# Cross-validation — pick hyperparameters that generalize, not those that memorize. See chapter 11.
# More training data — more data dilutes the impact of noise.
# Reduce model complexity — drop features, lower polynomial degree, simpler model.
# Feature selection — keep only the most useful features (Forward, RFE, Lasso). See chapter 14.
# Early stopping — for iterative models, stop training when validation error starts rising.
# Ensemble methods — bagging averages out variance (Random Forests).
# Exam questions on this topic
# How the problem of overfitting can be reduced in Linear regression? What is bias variance trade off?
# Answer
# Reducing overfitting in Linear Regression:
# Regularization — Ridge (L2 penalty), Lasso (L1 penalty), or ElasticNet shrink coefficients toward zero, reducing model variance.
# Cross-validation — k-fold CV picks hyperparameters that generalize.
# Feature selection — Forward selection, Backward elimination, RFE remove uninformative predictors.
# More training data — dilutes noise; harder to fit specific samples.
# Reduce polynomial degree if using polynomial features.
# Drop multicollinear features using VIF.
# Bias-Variance Tradeoff:
# Bias = how far model's average prediction is from truth → high when model too simple → underfitting.
# Variance = how much predictions vary across training sets → high when model too complex → overfitting.
# Tradeoff: reducing bias (add complexity) often raises variance, and vice versa.
# Total error decomposition: Error = Bias² + Variance + Irreducible Noise
# Goal: minimize total error → find the sweet spot where bias and variance are balanced.
# What strategies can be employed to mitigate overfitting in Linear Regression? Provide an explanation of various forms of Linear Regression that address the issue of overfitting.
# Answer
# Strategies to mitigate overfitting:
# Regularization (Ridge, Lasso, ElasticNet)
# Cross-validation (k-fold CV) for hyperparameter tuning
# Feature selection (Forward, Backward, RFE)
# Reducing model complexity
# Increasing training data size
# Removing multicollinearity (VIF)
# Forms of Linear Regression that address overfitting:
# Variant Penalty Effect
# Ridge (L2) α · Σβⱼ² Shrinks all coefficients toward zero (none exactly zero). Best for many small effects.
# Lasso (L1) α · Σ|βⱼ| Sets some coefficients exactly to zero → automatic feature selection.
# ElasticNet α₁·Σβⱼ² + α₂·Σ|βⱼ| Combines L1 and L2. Good when features are correlated.
# All three add a penalty to the cost function: J(β) = MSE + penalty. The hyperparameter α controls the strength — bigger α → more shrinkage → less overfitting (but more bias).
# How can you handle overfitting and underfitting?
# Answer
# To handle Overfitting (low train error, high test error):
# Use regularization (Ridge / Lasso / ElasticNet)
# Reduce model complexity (fewer features, lower polynomial degree)
# Use cross-validation
# Get more training data
# Apply feature selection / dimensionality reduction (PCA)
# Early stopping (for iterative models)
# To handle Underfitting (high train error, high test error):
# Add more features (or polynomial features)
# Use a more complex model
# Reduce regularization strength (lower α)
# Train longer / more iterations
# Improve feature engineering
#  Bias vs Variance — one liners
# Bias = systematic wrongness (model too simple).
# Variance = jumpiness (model too sensitive to data).
# Underfit = high bias, low variance. Overfit = low bias, high variance.
# Tradeoff = lowering one usually raises the other; find the U-curve minimum.
# Underfitting = too simple. Overfitting = too complex.
# Total error = Bias² + Variance + Noise.
# Operational measures from CV: bias = 1 − mean(R²), variance = std(R²).
# Fixes: regularization, CV, feature selection, more data, simpler model.

#==============================================================================
# TOPIC 10: Regularization (Ridge, Lasso, ElasticNet)
#==============================================================================

# Why regularize?
# Ridge
# Lasso
# ElasticNet
# Side-by-side
# Role of α
# Tuning α with CV
#  Why Regularization?
# Plain OLS minimizes squared residuals: J(β) = Σ(y − ŷ)² . With many features (or correlated ones), some β values can become huge — the model overfits, predictions on new data are unstable.
# Regularization adds a penalty term to the cost function that grows when β values get large. The model now has to balance: fit the data well (low residuals) and keep coefficients small (low penalty). This shrinks coefficients and reduces overfitting.
# General regularized cost function
# J(β) = Σ(yᵢ − ŷᵢ)² + α · Penalty(β)
# Three popular penalties → three regression variants: Ridge , Lasso , ElasticNet .
# Ridge Regression (L2 penalty)
# Ridge cost function
# J(β) = Σᵢ(yᵢ − ŷᵢ)² + α · Σⱼ βⱼ²
# The penalty is the sum of squared coefficients (L2 norm). Big βs cost a lot; small ones cost little.
# Effect on coefficients
# Shrinks all coefficients toward zero, but never exactly to zero .
# Stable under multicollinearity — splits the effect across correlated predictors instead of going wild on one.
# When to use Ridge
# You believe all features are at least somewhat useful .
# Multicollinearity is present.
# You want stability, not feature selection.
# Lasso Regression (L1 penalty)
# Lasso cost function
# J(β) = Σᵢ(yᵢ − ŷᵢ)² + α · Σⱼ |βⱼ|
# Penalty is the sum of absolute coefficient values (L1 norm).
# Effect on coefficients
# Shrinks coefficients toward zero, and can drive some exactly to zero . This is automatic feature selection .
# For correlated features, Lasso tends to keep one and zero out the others (sometimes arbitrarily).
# When to use Lasso
# You suspect many features are useless and want them removed.
# You want a sparse, interpretable model.
# ElasticNet (L1 + L2)
# ElasticNet cost function
# J(β) = Σᵢ(yᵢ − ŷᵢ)² + α · [ρ · Σ|βⱼ| + (1−ρ) · Σβⱼ²]
# ρ ("rho", or l1_ratio in sklearn) controls the L1/L2 mix. ρ=1 → Lasso, ρ=0 → Ridge, ρ=0.5 → equal blend.
# When to use ElasticNet
# You want feature selection (like Lasso) and stability under multicollinearity (like Ridge).
# Common with high-dimensional, correlated data (genomics, text features).
# Side-by-side comparison
# Aspect Ridge (L2) Lasso (L1) ElasticNet
# Penalty α·Σβⱼ² α·Σ|βⱼ| α·[ρ·L1 + (1-ρ)·L2]
# Sets β to 0? No Yes (some) Yes (some)
# Feature selection? No Yes (built-in) Yes
# Handles multicollinearity? Excellent Poor (picks one) Good
# Interpretable? Less (all features kept) More (sparse) Medium
# sklearn class Ridge Lasso ElasticNet
#  The role of α (lambda)
# α (sometimes written λ in textbooks) is the regularization strength. It's a hyperparameter you choose, typically via cross-validation.
# α value Effect
# α = 0 No penalty → identical to plain OLS
# α small (e.g. 0.01) Mild shrinkage; close to OLS
# α moderate (e.g. 1.0) Substantial shrinkage; strong regularization
# α very large (e.g. 1000) All coefficients ≈ 0 → severe underfitting
#  Always scale features before regularizing
# The penalty Σβⱼ² treats all coefficients equally. If your features have different scales (RAM in GB vs storage in MB), the bigger-scale features will have unfairly tiny βs and escape penalty. Always StandardScaler your X before Ridge/Lasso/ElasticNet.
# Tuning α with cross-validation
# The exam papers ask you to use Grid/Random search to tune α. Here's the template:
# from sklearn.model_selection import GridSearchCV from sklearn.linear_model import Ridge param_grid = { 'alpha' : [ 0.001 , 0.01 , 0.1 , 1 , 10 , 100 ]}
grid = GridSearchCV(Ridge(max_iter= 500 ), param_grid, cv= 5 , scoring= 'neg_root_mean_squared_error' )
grid.fit(X_train_scaled, y_train) print ( "Best alpha:" , grid.best_params_[ 'alpha' ])
y_pred = grid.predict(X_test_scaled)
rmse = np.sqrt(mean_squared_error(y_test, y_pred)) print ( "Test RMSE:" , rmse)
# Exam questions on this topic
# Write the expression for the cost function, which need to be minimized in Linear regression with RIDGE regularization.
# Answer
# J(β) = Σᵢ(yᵢ − ŷᵢ)² + α · Σⱼ βⱼ²
# Equivalently: J(β) = ||y − Xβ||²₂ + α · ||β||²₂
# The first term is the residual sum of squares (RSS); the second is the L2 penalty. α ≥ 0 is the regularization strength — when α = 0 it reduces to OLS; as α → ∞ all βs are forced to zero.
# If we increase the value of lambda, what will happen to the estimated coefficients in RIDGE model?
# Answer
# As λ (lambda) increases , the penalty for having large coefficients grows. To minimize total cost, the model is forced to shrink all coefficients toward zero :
# λ = 0: no penalty → coefficients = OLS estimates.
# λ small: mild shrinkage; coefficients close to OLS but slightly smaller in magnitude.
# λ large: all coefficients shrink substantially. Bias increases, variance decreases.
# λ → ∞: all coefficients → 0. The model predicts only the mean of y → severe underfitting.
# Important: Ridge shrinks coefficients but never sets them exactly to zero . (For exact-zero behaviour, use Lasso instead.) Picking the right λ is a bias-variance tradeoff — typically tuned via cross-validation.
# What is regularization in linear regression? Compare and contrast Lasso and Ridge regression in terms of mathematical formulation, impact on coefficients, and use cases.
# Answer
# Regularization = adding a penalty term to the OLS cost function to discourage large coefficients. This reduces overfitting and improves model generalization, especially when features are many or multicollinear.
# Aspect Ridge (L2) Lasso (L1)
# Cost function RSS + α·Σβⱼ² RSS + α·Σ|βⱼ|
# Penalty type Squared coefficients Absolute coefficients
# Solution Closed-form: β̂ = (XᵀX + αI)⁻¹ Xᵀy No closed form; coordinate descent
# Impact on coefs Shrinks all βs toward 0; never exactly 0 Shrinks and sets some βs exactly to 0
# Feature selection? No Yes (sparse solution)
# Multicollinearity Handles well — distributes effect Picks one feature, zeros others (arbitrary)
# Use case All features moderately useful; multicollinearity present Few features actually useful; sparse interpretable model needed
# Common ground: both add a penalty controlled by α; both reduce variance at the cost of slightly higher bias; both require feature scaling beforehand.
# What role does regularization play in improving Linear Regression models?
# Answer
# Regularization plays multiple roles:
# Reduces overfitting — by penalizing large coefficients, the model becomes simpler and generalizes better to unseen data.
# Stabilizes coefficients under multicollinearity — Ridge in particular handles correlated predictors gracefully.
# Performs feature selection — Lasso (and ElasticNet) drive uninformative coefficients to exactly zero, automatically removing them from the model.
# Improves test-set performance — by trading a small amount of bias for a large reduction in variance.
# Enables modeling with p > n — when there are more features than observations, OLS can't run; regularization makes the problem solvable.
# Improves interpretability — sparse models (from Lasso) are easier to explain.
# The strength is controlled by α, tuned via cross-validation. The 3 main forms are Ridge (L2), Lasso (L1), and ElasticNet (L1+L2 blend).
# The 3 Rs: Ridge, Restraint, Removal
# Ridge uses squared β (L 2 ) — R educes everyone equally.
# Lasso uses absolute β (L 1 ) — L obs uninformative features off entirely.
# ElasticNet mixes both — best of both worlds.
# Regularization = penalty added to cost function to fight overfitting.
# Ridge (L2): shrinks all βs, never zero; great for multicollinearity.
# Lasso (L1): can zero out βs; built-in feature selection.
# ElasticNet: blends L1+L2; balances stability and sparsity.
# α controls strength; tune with cross-validation.
# Always scale features before regularizing.

#==============================================================================
# TOPIC 11: Cross-Validation
#==============================================================================

# Why CV?
# k-Fold procedure
# Bias/Variance from CV
# Other CV variants
# Memory aid
# Why Cross-Validation?
# A single train/test split has a problem: the test-set score depends on which 20% of the data happened to land in the test set. With unlucky luck, your model might look great or terrible just because of the split.
# Cross-validation (CV) averages performance across multiple splits, giving you a more reliable estimate of how the model will generalize.
# k-Fold Cross-Validation — the standard recipe
# Shuffle the training data.
# Split it into k equal-sized chunks ("folds"). Common: k = 5 or k = 10.
# For each fold i (1 to k):
# Treat fold i as the validation set.
# Train the model on the other k-1 folds.
# Score it on fold i.
# Average the k scores → that's your CV score.
# 5-Fold Cross-Validation Fold 1 → score₁ Fold 2 → score₂ Fold 3 → score₃ Fold 4 → score₄ Fold 5 → score₅ Train Validation CV Score = mean(score₁, …, score₅)
# Each fold takes a turn as the validation set. The model is trained 5 separate times. Average the 5 scores.
#  Bias error and Variance error from CV
# The Feb/ + + Nov 2024 papers ask for these operational definitions:
# Operational definitions
# Bias error = 1 − mean(R² across folds)
# Variance error = standard deviation of R² across folds
# Interpretation
# Combination Diagnosis
# Low bias error, low variance error Excellent — well-fit, stable model
# High bias error, low variance error Underfitting — model is consistent but bad
# Low bias error, high variance error Overfitting — performance depends on which fold
# High bias error, high variance error Bad model — both poor and unstable
# from sklearn.model_selection import KFold, cross_val_score, cross_validate from sklearn.linear_model import LinearRegression import numpy as np # Quick way: cross_val_score model = LinearRegression()
r2_scores = cross_val_score(model, X_train, y_train, cv= 5 , scoring= 'r2' ) print ( f"R² per fold: {r2_scores}" ) print ( f"Mean R²: {r2_scores.mean():.4f}" ) print ( f"Bias error (1 - mean R²): {1 - r2_scores.mean():.4f}" ) print ( f"Variance error (std R²): {r2_scores.std():.4f}" ) # If you want RMSE per fold instead of R² neg_mse = cross_val_score(model, X_train, y_train, cv= 5 , scoring= 'neg_mean_squared_error' )
rmse_per_fold = np.sqrt(-neg_mse) print ( f"RMSE per fold: {rmse_per_fold}" )
# Other CV variants
# Variant What it does When to use
# k-Fold (k=5 or 10) Standard k splits General purpose; default choice
# Stratified k-Fold Preserves class balance per fold Classification with imbalanced classes
# Leave-One-Out (LOOCV) k = n; each sample is its own fold Very small datasets; extremely expensive
# Time-Series Split Train always precedes test in time Time-series data — never shuffle the time axis
# Shuffle Split Random repeated train/val splits When you want more iterations than k allows
# Exam questions on this topic

# Explain the procedure involved in k-fold cross validation.
# Answer
# k-Fold Cross-Validation is a model-validation technique that gives a more reliable estimate of test performance than a single train/test split.
# Procedure:
# Shuffle the training data randomly (unless time-ordered).
# Split the data into k equal-sized parts called folds. Common values: k = 5 or k = 10.
# For each fold i = 1 to k:
# Treat fold i as the validation set.
# Combine the remaining k-1 folds into a training set.
# Train the model on the training folds.
# Evaluate it on fold i — record the score (e.g., R² or RMSE).
# After all k iterations, you have k scores. Compute the mean of the scores → that's the CV estimate of model performance.
# Optionally compute the standard deviation → measures stability across folds.
# Why it's better than a single split:
# Every observation gets used for both training and validation (each one exactly once for validation).
# The averaged score has lower variance than a single split's score.
# You get a sense of model stability via the std-dev of fold scores.
# Tradeoffs: CV is k× more computationally expensive than a single fit. Larger k → less bias, more variance, more cost.
# Memory aid
# 5-fold CV in 5 words
# "Split, rotate, score, average, report."
# CV averages performance across multiple train/val splits → more reliable than one split.
# k-fold CV: split into k chunks, each takes a turn as validation, average k scores.
# Common: k = 5 (default in your papers); k = 10 for more reliable estimates.
# Operational measures: bias error = 1 − mean(R²) , variance error = std(R²) .
# Use Stratified k-Fold for imbalanced classification; TimeSeriesSplit for time data.

#==============================================================================
# TOPIC 12: Evaluation Metrics
#==============================================================================

# Why multiple metrics?
# R²
# Adjusted R²
# RMSE
# MAE
# MAPE
# Comparison table
# Why we need multiple metrics
# "How good is my model?" is a question with several valid answers depending on what you care about: variance explained, average error size, big-error sensitivity, percentage error. Each metric tells a different story.
# R² — the coefficient of determination
# R-squared
# R² = 1 − (SS_res / SS_tot)
# SS_res = Σᵢ(yᵢ − ŷᵢ)² SS_tot = Σᵢ(yᵢ − ȳ)²
# Term Meaning
# SS_res Residual sum of squares — how badly the model fits
# SS_tot Total variance in y — how spread out y is around its mean
# R² Fraction of variance the model explains. Closer to 1 = better.
# R² value Interpretation
# R² = 1 Model explains 100% of variance — perfect predictions
# R² = 0 Model is no better than predicting the mean of y
# R² < 0 Model is worse than predicting the mean (yes, possible on test set)
# R² ≈ 0.7 Decent — explains ~70% of variance; common in real data
#  The trap with R²
# R² always increases (or stays the same) when you add features , even useless ones. So "higher R² = better model" only works if you compare models with the same number of features.
# Adjusted R² — fair comparison across feature counts
# Adjusted R²
# Adj R² = 1 − (1 − R²) · [(n − 1) / (n − k − 1)]
# n = number of samples, k = number of predictors (features)
# Adjusted R² penalizes models with more features. Useless features hurt Adj R² but not R². So Adj R² goes up when added features genuinely help, and goes down when they don't.
# R² vs Adj R²
# Use R² — when reporting variance explained on a single model.
# Use Adj R² — when comparing models with different numbers of features.
# Big gap (R² much higher than Adj R²) → too many useless features.
# RMSE — Root Mean Squared Error
# RMSE = √[(1/n) · Σᵢ(yᵢ − ŷᵢ)²]
# "Average size of prediction error, in the same units as y." If you predicted house prices and RMSE = 5L, then on average you're off by about 5L. Large errors hurt more due to squaring.
# MAE — Mean Absolute Error
# MAE = (1/n) · Σᵢ |yᵢ − ŷᵢ|
# Same units as y. Treats all errors equally (no squaring). More robust to outliers than RMSE.
# MAPE — Mean Absolute Percentage Error
# MAPE = (100/n) · Σᵢ |yᵢ − ŷᵢ| / |yᵢ|
# Average percentage error. Same percentage scale across different problems — a MAPE of 8% means "off by 8% on average."
#  MAPE pitfall
# MAPE blows up when any yᵢ is close to 0. Don't use MAPE if your target can be near zero.
# Comparing the metrics
# Metric Range Units Outlier-sensitive? Best when
# R² (−∞, 1] Unitless Yes Reporting variance explained
# Adj R² (−∞, 1] Unitless Yes Comparing models with different feature counts
# RMSE [0, ∞) Same as y Yes (squared) You care about big errors
# MSE [0, ∞) y² Yes (squared) Internal optimization (training)
# MAE [0, ∞) Same as y Less Robust to outliers; equal weight to all errors
# MAPE [0, ∞) % Less Comparing across scales; y >> 0
# from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error import numpy as np y_pred = model.predict(X_test) r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred) * 100 # sklearn returns fraction # Adjusted R² — sklearn doesn't have it, but it's a one-liner n = len(y_test)
k = X_test.shape[ 1 ]
adj_r2 = 1 - ( 1 - r2) * (n - 1 ) / (n - k - 1 ) print ( f"R²: {r2:.4f}" ) print ( f"AdjR²: {adj_r2:.4f}" ) print ( f"RMSE: {rmse:.2f}" ) print ( f"MAE: {mae:.2f}" ) print ( f"MAPE: {mape:.2f}%" )
# Exam questions on this topic
# What is the difference between R² and Adjusted R², and when should each be used?
# Answer
# R² = fraction of variance in y explained by the model. Formula:
# R² = 1 − SS_res / SS_tot
# Adjusted R² = R² penalized for the number of features:
# Adj R² = 1 − (1 − R²) · (n − 1) / (n − k − 1)
# Aspect R² Adjusted R²
# Behaviour when adding any feature Always ↑ or stays same ↑ only if feature genuinely helps; else ↓
# Range (−∞, 1] Can be lower than R²
# Penalizes model complexity? No Yes (penalizes k)
# When to use which:
# R² — for a single model, or to report variance explained.
# Adjusted R² — when comparing models with different numbers of features ; for feature selection.
# Diagnostic: if R² is much higher than Adj R², your model has redundant or useless features.
# How adjusted R-square is differing from R-square? Brief the role of adjusted R-square in feature selection process.
# Answer
# Difference:
# R² always increases (or stays the same) when you add a feature, regardless of whether the feature is useful.
# Adjusted R² = 1 − (1 − R²)·(n−1)/(n−k−1) accounts for the number of predictors k. It increases only when a new feature improves the model more than expected by chance ; otherwise it decreases.
# Role in feature selection:
# When comparing two models with different feature counts, Adjusted R² gives a fair comparison — R² alone would always favour the bigger model.
# Used in stepwise selection (forward / backward): at each step, a candidate feature is added/removed only if Adj R² improves.
# If adding a feature drops Adj R², the feature is rejected as not contributing genuine information.
# Helps prevent overfitting that would result from blindly adding features to chase higher R².
# 1c · Mobile-phone sales numerical
# A linear regression model is build with three independent variable price, advertisement cost and promotion cost to predict unit sales of mobile phone. Say the p value for the t-test of the variable 'advertisement cost' is 0.02. What is your inference on this?
# Answer
# p-value = 0.02 → reject H₀ at the 5% significance level.
# Hypothesis setup for the t-test on β_advertisement:
# H₀: β_advertisement = 0 (advertisement cost has no effect on sales)
# H₁: β_advertisement ≠ 0 (advertisement cost has a significant effect)
# The p-value 0.02 is the probability of observing a coefficient at least as extreme as the one we got, if H₀ were true . Since 0.02 < 0.05 (the conventional 5% significance threshold):
# We reject H₀ .
# The coefficient on advertisement cost is statistically significant .
# Inference: advertisement cost is a meaningful predictor of mobile phone sales — keep this feature in the model.
# (At the 1% level, p = 0.02 would not be significant since 0.02 > 0.01. So conclude: significant at 5% but not at 1%.)
# 1d · RMSE comparison numerical
# The RMSE of the regression model which predicting the CTC salary is 12324 and the RMSE of the other regression model which predicting the age of the person is 55. Comment on the performance of these two models. [output column is not scaled or transformed]
# Answer
# You cannot compare these RMSE values directly. RMSE has the same units as y, and the two ys are on completely different scales:
# CTC salary is typically in lakhs of rupees — values commonly between 100,000 and 5,000,000+. An RMSE of 12,324 is roughly 12K — a tiny error in this context.
# Age is in years — values between roughly 18 and 80. An RMSE of 55 years is enormous — bigger than the entire reasonable range of ages.
# To compare fairly, use a scale-free metric such as:
# Relative RMSE (% RMSE) = RMSE / mean(y) × 100. If average salary ≈ 500,000, then %RMSE ≈ 12,324/500,000 × 100 ≈ 2.5% — excellent. If average age ≈ 35, then %RMSE ≈ 55/35 × 100 ≈ 157% — disastrous.
# R² — measures variance explained, unit-less, comparable across models.
# MAPE — already a percentage; directly comparable.
# Inference: the salary model is performing well (low relative error). The age model is failing badly — RMSE is larger than the entire range of plausible ages, suggesting the model is essentially useless. Always interpret RMSE relative to the scale of y.
# Metric one-liners
# R² → "variance explained" (closer to 1 = better)
# Adj R² → "R² minus the bullshit features" — comparable across feature counts
# RMSE → "average mistake size in original units" — outlier-aware
# MAE → "average absolute mistake" — outlier-tough
# MAPE → "average percentage off" — comparable across scales
# R² = fraction of variance explained. Range (−∞, 1]; 1 = perfect.
# Adj R² penalizes for number of features → use when comparing models.
# RMSE = average error size in y's units; sensitive to outliers (squared).
# MAE = average absolute error; robust to outliers.
# MAPE = average percentage error; only valid if y is well above zero.
# Never compare RMSE across different ys — use scale-free metrics (R², MAPE).

#==============================================================================
# TOPIC 13: Model Diagnostics
#==============================================================================

# Why diagnose?
# 4 residual plots
# Statistical tests
# Exam template answer
# Why diagnose your model?
# A high R² doesn't guarantee a good model. The OLS assumptions (chapter 7) might be silently violated, making your p-values lies and your predictions unreliable. Diagnostics are the visual + statistical checks that tell you which assumption is broken and where to look.
# The Section C question 5b in nearly every paper says: "Check assumptions of linear regression. Write your inferences." — these diagnostics are exactly what you need.
# The 4 residual plots you must know
# 1. Residuals vs Fitted plot
# What it shows: residuals (yᵢ − ŷᵢ) on the y-axis, fitted values ŷᵢ on the x-axis.
# What you want: a random horizontal cloud around zero, with no pattern.
# Detects: Linearity (curve = non-linear) and Homoscedasticity (fan = heteroscedastic).
# 2. Q-Q (Quantile-Quantile) Plot
# What it shows: quantiles of standardized residuals (y-axis) vs quantiles of a normal distribution (x-axis).
# What you want: points hugging the diagonal y=x line.
# Detects: Normality of errors.
# Reading the deviations:
# Points form a straight line on the diagonal → normal
# S-shape (curves above-then-below or below-then-above) → heavy tails (more outliers than normal)
# Points curving up at the top, down at the bottom → light tails
# Skewed shape → distribution isn't symmetric
# 3. Scale-Location plot (a.k.a. Spread-Location)
# What it shows: √|standardized residuals| vs fitted values.
# What you want: a horizontal line with random scatter.
# Detects: Homoscedasticity. A rising line means variance increases with prediction.
# 4. Residuals vs Leverage plot
# What it shows: standardized residuals vs leverage (how unusual the X values are).
# What you want: no point in the top-right or bottom-right corner with high Cook's distance.
# Detects: Influential points — single observations that disproportionately tilt the model.
# Residuals vs Fitted Q-Q Plot Scale-Location Residuals vs Leverage outlier
# The four diagnostic plots. Top-left: random scatter = linearity & homoscedasticity OK. Top-middle: points on diagonal = normal residuals. Top-right: flat line = constant variance. Bottom: lone point in corner = influential outlier.
# Statistical tests for assumptions
# Assumption Test Null hypothesis Reject if
# Normality of residuals Shapiro-Wilk Residuals are normal p < 0.05 → not normal
# Normality of residuals Jarque-Bera Residuals are normal (skew & kurt = normal) p < 0.05 → not normal
# Homoscedasticity Breusch-Pagan Variance is constant p < 0.05 → heteroscedastic
# Homoscedasticity White test Variance is constant p < 0.05 → heteroscedastic
# Independence (autocorr.) Durbin-Watson No autocorrelation Statistic far from 2.0
# Linearity Rainbow test Relationship is linear p < 0.05 → non-linear
# Multicollinearity VIF (Not a hypothesis test) VIF > 5–10 → problematic
# import matplotlib.pyplot as plt import statsmodels.api as sm import scipy.stats as stats from statsmodels.stats.diagnostic import het_breuschpagan from statsmodels.stats.stattools import durbin_watson # Suppose you've already fit: ols_model = sm.OLS(y_train, X_const).fit() residuals = ols_model.resid
fitted = ols_model.fittedvalues # 1. Residuals vs Fitted plot plt.figure(figsize=( 10 , 8 ))
plt.subplot( 2 , 2 , 1 )
plt.scatter(fitted, residuals, alpha= 0.5 )
plt.axhline( 0 , color= 'red' , linestyle= '--' )
plt.xlabel( 'Fitted' ); plt.ylabel( 'Residuals' )
plt.title( 'Residuals vs Fitted' ) # 2. Q-Q plot plt.subplot( 2 , 2 , 2 )
sm.qqplot(residuals, line= '45' , ax=plt.gca())
plt.title( 'Normal Q-Q Plot' ) # 3. Histogram of residuals plt.subplot( 2 , 2 , 3 )
plt.hist(residuals, bins= 30 , edgecolor= 'black' )
plt.xlabel( 'Residual' ); plt.title( 'Residual distribution' ) # 4. Statistical tests shapiro_stat, shapiro_p = stats.shapiro(residuals)
bp_stat, bp_p, _, _ = het_breuschpagan(residuals, X_const)
dw = durbin_watson(residuals) print ( f"Shapiro-Wilk normality: p={shapiro_p:.4f}" ) print ( f"Breusch-Pagan homoscedast.: p={bp_p:.4f}" ) print ( f"Durbin-Watson autocorr.: {dw:.3f}" )
plt.tight_layout(); plt.show()
# Exam guidance — what to write for "Check assumptions"
# Template inference (Section C 5b)
# For each assumption, write ONE sentence with: (a) the test/plot used, (b) the result, (c) the conclusion. Example:
# Linearity — Residuals vs Fitted plot shows random scatter around 0; no clear pattern. Linearity holds.
# Independence — Durbin-Watson statistic = 1.92, close to 2.0. No autocorrelation.
# Normality — Q-Q plot points fall on the diagonal; Shapiro-Wilk p = 0.18 (> 0.05). Residuals approximately normal.
# Homoscedasticity — Breusch-Pagan p = 0.08 (> 0.05); residuals show constant spread. Homoscedastic.
# No multicollinearity — All VIFs < 5 after dropping Length1 and Length2. Multicollinearity resolved.
# If any test fails, suggest the fix (log-transform y, polynomial features, drop feature, etc.).
# Four residual plots: Residuals-vs-Fitted, Q-Q, Scale-Location, Residuals-vs-Leverage.
# Statistical tests: Shapiro-Wilk (normality), Breusch-Pagan (homoscedasticity), Durbin-Watson (autocorrelation).
# For Section C 5b answers: 5 assumptions × (test + result + conclusion) = full marks.

#==============================================================================
# TOPIC 14: Feature Engineering and Selection
#==============================================================================

# Engineering vs Selection
# Engineering techniques
# Selection methods
# Feature Engineering vs Feature Selection
# Term Goal Examples
# Feature Engineering Create new, more informative features log-transform, polynomial features, interaction terms, datetime parts
# Feature Selection Pick the most useful features from existing ones Forward selection, RFE, Lasso, VIF-based dropping
#  Feature Engineering techniques
# 1. Log Transformation
# Use when: y or a feature is right-skewed (lots of small values, few huge ones — common in prices, salaries, counts).
# Effect: compresses the range, makes the distribution more symmetric / closer to normal, often makes a non-linear relationship more linear.
# df[ 'log_price' ] = np.log1p(df[ 'price' ]) # log(1+x) handles zeros
# 2. Box-Cox / Yeo-Johnson Transformation
# Generalization of log: tries to find the best power transformation. Box-Cox needs y > 0; Yeo-Johnson works for any y.
# from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer(method= 'yeo-johnson' )
X_transformed = pt.fit_transform(X)
# 3. Polynomial Features & Interactions
# Add x², x·z, x³ etc. to capture non-linear and interaction effects.
# from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree= 2 , interaction_only= False )
X_poly = poly.fit_transform(X)
# 4. Binning / Discretization
# Convert a continuous feature into bins (e.g., age → "young/middle/senior"). Useful when relationship is non-monotonic.
# 5. Datetime feature extraction
# From a single datetime column, extract: year, month, day, day-of-week, hour, is_weekend, days_since_event. Hugely useful for time-aware predictions (e.g., metro traffic in Nov 2021 paper).
#  Feature Selection methods
# Method family Examples How it picks features
# Filter methods Correlation, VIF, mutual information, ANOVA F-test Score features in isolation; doesn't use the model
# Wrapper methods Forward, Backward, Recursive Feature Elimination (RFE) Try subsets, score with the actual model
# Embedded methods Lasso, ElasticNet, Tree feature importance Selection happens during model training
# Forward Selection (Wrapper)
# Start with no features.
# For each remaining feature, fit a model with the current set + that feature; record the score (R², Adj R², or AIC).
# Add the single feature that improved the score the most.
# Stop when no further addition improves the score.
# Backward Elimination (Wrapper)
# Start with all features.
# Fit the model. Find the feature with the highest p-value (or smallest contribution).
# Remove that feature if its p-value > 0.05 (or threshold).
# Repeat until all remaining features are significant.
# Recursive Feature Elimination (RFE)
# Train a model with all features.
# Rank features by importance (e.g., absolute coefficient size or feature_importance_).
# Remove the least important feature.
# Repeat until a target number of features remains.
# from sklearn.feature_selection import RFE from sklearn.linear_model import LinearRegression
selector = RFE(LinearRegression(), n_features_to_select= 5 )
selector.fit(X_train, y_train)
selected = X.columns[selector.support_] print ( "Selected features:" , list(selected))
# SequentialFeatureSelector (mlxtend / sklearn)
# from mlxtend.feature_selection import SequentialFeatureSelector
sfs = SequentialFeatureSelector(LinearRegression(), k_features= 'best' , forward= False , # False = backward elimination scoring= 'r2' , cv= 5 )
sfs.fit(X_train, y_train) print ( "Best features:" , sfs.k_feature_names_)
# Exam questions on this topic

# Explain the procedure involved in Forward Feature Selection.
# Answer
# Forward Feature Selection is a stepwise (wrapper) feature-selection technique that starts with no features and adds one at a time, picking the most useful at each step.
# Procedure:
# Start with an empty feature set .
# For each candidate feature not yet in the model:
# Fit the regression model using {current set} + {candidate}.
# Record the score (R² / Adjusted R² / AIC / cross-validation score).
# Add the candidate that improved the score the most to the model.
# Repeat steps 2-3 until either: (a) no remaining candidate improves the score, or (b) you reach a desired number of features, or (c) all features are added.
# The final feature set is the chosen subset.
# Pros: simple, interpretable, gives a small model.
# Cons: greedy — can miss feature combinations that only help when chosen together; computationally expensive when k is large.
# What are Wrapper Methods in feature selection, and how are they applied in Linear Regression?
# Answer
# Wrapper methods are feature selection techniques that "wrap around" a learning algorithm — they evaluate feature subsets by training the actual model and measuring its performance, choosing the subset that gives the best score.
# Three main wrapper methods:
# Forward Selection — start empty, add the most-useful feature one at a time.
# Backward Elimination — start with all features, drop the least-significant one at a time.
# Recursive Feature Elimination (RFE) — start with all, repeatedly drop the lowest-ranked feature based on coefficient importance.
# Applied to Linear Regression:
# Use the linear model (e.g., LinearRegression ) as the base estimator.
# Score subsets via Adjusted R², AIC/BIC, or cross-validated RMSE.
# Implementations: SequentialFeatureSelector from mlxtend or sklearn; RFE / RFECV from sklearn.
# Pros: often find better subsets than filter methods; capture feature interactions in the model context.
# Cons: computationally expensive (model fit per subset); risk of overfitting to validation set.
# What is Recursive Feature Elimination (RFE)? Explain how it works, its advantages and limitations, and how it can be used to improve model performance in linear regression.
# Answer
# RFE is a wrapper feature-selection method that ranks features by importance and removes them one at a time (or in batches) using the trained model itself.
# How it works:
# Train the linear regression model with all features.
# Rank features by importance — typically the absolute value of the coefficients (or coefficients on standardized features).
# Remove the feature with the lowest rank.
# Re-train the model on the remaining features.
# Repeat steps 2–4 until you reach the target number of features (or use RFECV to let CV pick the optimal count).
# Advantages:
# Considers multivariate feature importance (uses the actual model's coefficients).
# Often outperforms simple filter methods.
# Can be combined with cross-validation (RFECV) to auto-pick the best feature count.
# Limitations:
# Computationally expensive — fits the model many times.
# Sensitive to feature scaling — must standardize before applying with linear models.
# Coefficient-based ranking unreliable when features are highly correlated.
# Greedy — doesn't explore all subsets.
# How it improves linear regression: reduces overfitting, eliminates noise features, makes the model more interpretable, and often gives better test-set performance.
# Discuss the need for data transformations in a linear regression model. Also write about various techniques employed.
# Answer
# Why data transformations are needed:
# Fix non-linearity — straighten curved relationships so a linear model fits well.
# Reduce skewness — bring features/target closer to normal distribution.
# Stabilize variance — fix heteroscedasticity (residual variance varying with ŷ).
# Bring features to comparable scales — required for regularization and for fair coefficient comparison.
# Handle outliers — log/sqrt compress extreme values without dropping them.
# Improve normality of residuals — makes p-values reliable.
# Techniques:
# Technique Use case
# Log / log1p Right-skewed positive data (prices, salaries, counts)
# Square root / Cube root Mildly skewed positive data
# Box-Cox Auto-pick best power transformation; needs y > 0
# Yeo-Johnson Generalisation of Box-Cox for any y
# Reciprocal (1/x) Heavy right tail
# StandardScaler (x − μ) / σ — for distance-based or regularized models
# MinMaxScaler (x − min) / (max − min) → [0, 1]
# RobustScaler (x − median) / IQR — outlier-robust
# Polynomial features Capture x², x³, x·z relationships
# Encoding (label, one-hot) Convert categorical features to numeric
# Binning Convert continuous to categorical when relationship is non-monotonic
# Engineering creates new features. Selection picks the best of existing ones.
# Filter methods score features alone; Wrapper methods use the model; Embedded methods (Lasso) do both.
# Forward / Backward / RFE are the three core wrapper methods.
# Always scale features before RFE with linear models.

#==============================================================================
# TOPIC 15: Data Preprocessing
#==============================================================================

# Why preprocess?
# Missing Values
# Outliers
# Encoding
# Scaling
# Train-Test Split
# Why preprocess data?
# Real datasets are messy. They have missing values, outliers, mixed types, wrong scales, text categories. Models can't directly digest any of that. Preprocessing is the cleanup step that gets your data into a model-friendly state.
# Section B Q4 of nearly every ML-1 paper is dedicated to this — typically worth 25 marks . The five subtasks recur identically across papers: missing values, outliers, encoding, scaling, splitting .
# 1. Missing Values
# Detect
# df.isnull().sum() # count of NaNs per column df.isnull().sum() / len(df) * 100 # % missing per column import seaborn as sns
sns.heatmap(df.isnull(), cbar= False ) # visual map of NaNs
# Treat
# Strategy When to use Code
# Drop rows Few rows have NaN; data is plentiful df.dropna()
# Drop column Column is > 50% missing df.drop(columns=['col'])
# Fill with mean Numeric, roughly normal distribution df['col'].fillna(df['col'].mean())
# Fill with median Numeric, skewed or has outliers df['col'].fillna(df['col'].median())
# Fill with mode Categorical features df['col'].fillna(df['col'].mode()[0])
# Forward / backward fill Time-series data df.ffill() / df.bfill()
# Constant value "missing" itself is meaningful df.fillna('missing') or df.fillna(0)
# KNN imputation Missing-at-random patterns sklearn.impute.KNNImputer()
# Iterative imputer Multivariate dependencies sklearn.impute.IterativeImputer()
# 2. Outliers
# Detect
# Visual: boxplot — points outside the whiskers; histogram with extreme tails; scatter plot vs y.
# Statistical:
# IQR method: Q1 − 1.5·IQR < outlier > Q3 + 1.5·IQR (where IQR = Q3 − Q1).
# Z-score method: |z| > 3 → outlier.
# Treat (in order of preference)
# Investigate first. Are they real values or data-entry errors?
# Cap (winsorize) — clip values to the IQR boundary or a percentile (e.g., 1st-99th).
# Transform — log or square-root often pulls outliers in.
# Drop — only when you're sure they're errors. Used by every Section B Q4 in your papers ("treat with dropping").
# Use a robust model — Huber regression, RANSAC.
# # IQR-based dropping (the standard exam approach) Q1 = df[ 'col' ].quantile( 0.25 )
Q3 = df[ 'col' ].quantile( 0.75 )
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df = df[(df[ 'col' ] >= lower) & (df[ 'col' ] <= upper)]
# 3. Encoding categorical features
# Method How it works Pros Cons
# Label Encoding Map categories to integers (0, 1, 2, …) Compact; one column Implies ordering — wrong for nominal data!
# One-Hot Encoding One binary column per category No false ordering Many columns if high cardinality
# Dummy Encoding (n−1) Like one-hot but drop one column Avoids dummy variable trap One category becomes the "reference"
# Ordinal Encoding Map to integers in a meaningful order Captures real ordering Need to specify the order
# Target Encoding Replace category with mean(y) for that category Captures relationship to y Risk of leakage; needs CV
#  The Dummy Variable Trap
# If you have a categorical feature with k categories and create k one-hot columns, the columns sum to 1 — perfectly collinear with the intercept. OLS fails. Always drop one category (use n-1 dummies) or use drop_first=True in pandas.
# Code
# # Label encoding (use only for ordinal categories) from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df[ 'gender_encoded' ] = le.fit_transform(df[ 'gender' ]) # One-hot encoding (n columns) df_encoded = pd.get_dummies(df, columns=[ 'category' ], drop_first= False ) # n-1 dummy encoding (avoids the trap) — used in Feb 2025, Mar 2024, Nov 2024 df_encoded = pd.get_dummies(df, columns=[ 'category' ], drop_first= True )
# 4. Feature Scaling
# Scaler Formula Output range Use when
# StandardScaler (x − μ) / σ Mean 0, Std 1 Default; data roughly normal; required before regularization
# MinMaxScaler (x − min) / (max − min) [0, 1] You need a bounded range (e.g., neural nets)
# RobustScaler (x − median) / IQR Centered around 0 Data has outliers
# MaxAbsScaler x / max(|x|) [−1, 1] Sparse data
#  The cardinal scaling rule
# fit on training data only. Then transform both train and test using the same scaler — never re-fit on test data. Fitting on full data leaks test info into training.
# from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) # learn μ, σ from train X_test_scaled = scaler.transform(X_test) # apply same μ, σ to test
# 5. Train-Test Split
# from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size= 0.2 , # 80:20 (Feb 2025, Mar 2024, Nov 2024); use 0.3 for 70:30 random_state= 42 # for reproducibility )
# Exam questions on this topic
# Explain any two of the data preprocessing steps.
# Answer (pick any two)
# 1. Handling missing values — replace NaNs with mean (numeric), median (skewed numeric), or mode (categorical); or drop rows/columns when too many are missing. Visualize first with df.isnull().sum() or a heatmap. Choice depends on % missing and the distribution.
# 2. Encoding categorical features — convert text categories to numeric so the model can use them. Use Label Encoding for ordinal data (e.g., 'low/medium/high' → 0/1/2) and One-Hot or n-1 Dummy Encoding for nominal data (e.g., 'red'/'green'/'blue' → three or two binary columns). Always drop one category to avoid the dummy variable trap.
# 3. Outlier treatment — detect via boxplots, IQR rule (1.5×IQR boundary), or Z-scores (|z| > 3). Treat by capping (winsorize), dropping, or log-transformation. Outliers can dominate OLS regression if untreated.
# 4. Feature scaling — bring features to comparable magnitudes. Use StandardScaler (mean 0, std 1) for most cases; MinMaxScaler for [0,1] range; RobustScaler when outliers exist. Required before regularization (Ridge/Lasso) and most distance-based algorithms.
# Five core preprocessing steps: missing values, outliers, encoding, scaling, splitting.
# Section B Q4 of every paper tests these — worth ~25 marks.
# Always fit scalers/encoders on training data only; transform test using the fitted version.
# Use n-1 dummy encoding to avoid the dummy variable trap.

#==============================================================================
# TOPIC 16: Hyperparameter Tuning
#==============================================================================

# Parameters vs Hyperparameters
# Grid Search
# Random Search
# Bayesian Optimization
# Comparison
#  Parameters vs Hyperparameters
# Parameters Hyperparameters
# Learned from data during training Set by you before training
# Examples: β₀, β₁, …, βₖ in linear regression Examples: alpha in Ridge, l1_ratio in ElasticNet, k in k-fold CV, max_iter
# Found via OLS or gradient descent Found via Grid Search, Random Search, Bayesian Optimization
# Grid Search
# Try every combination of hyperparameters from a predefined list. Pick the one that gives the best cross-validation score.
# from sklearn.model_selection import GridSearchCV from sklearn.linear_model import Ridge param_grid = { 'alpha' : [ 0.001 , 0.01 , 0.1 , 1 , 10 , 100 ]}
grid = GridSearchCV(Ridge(max_iter= 500 ), param_grid, cv= 5 , # 5-fold CV scoring= 'neg_root_mean_squared_error' , n_jobs=- 1 ) # parallel across cores grid.fit(X_train_scaled, y_train) print ( f"Best alpha: {grid.best_params_['alpha']}" ) print ( f"Best CV score: {-grid.best_score_:.3f}" )
y_pred = grid.predict(X_test_scaled)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred)) print ( f"Test RMSE: {test_rmse:.3f}" )
# Pros: exhaustive — guaranteed to find the best in your grid.
# Cons: exponential cost. With 4 hyperparameters of 5 values each = 5⁴ = 625 fits × 5 folds = 3,125 model trainings. Slow.
# Random Search
# Sample random combinations from a distribution. Often finds nearly-best results in a fraction of the time.
# from sklearn.model_selection import RandomizedSearchCV from scipy.stats import loguniform param_dist = { 'alpha' : loguniform( 0.001 , 100 )}
rnd = RandomizedSearchCV(Lasso(max_iter= 500 ), param_dist, n_iter= 20 , # try 20 random alphas cv= 5 , scoring= 'neg_root_mean_squared_error' , random_state= 42 )
rnd.fit(X_train_scaled, y_train) print ( f"Best alpha: {rnd.best_params_['alpha']}" )
# Pros: faster than grid; explores continuous ranges; often finds good combos quickly.
# Cons: not exhaustive — you might miss the global optimum (though usually not by much).
# Bayesian Optimization
# Smarter still: build a probabilistic model (typically a Gaussian Process) of "score as a function of hyperparameters" , and use it to pick the next promising point to try.
# How it works
# Initialize by trying a few random points; record their scores.
# Fit a surrogate model (e.g., Gaussian Process) that predicts the score at any unseen hyperparameter point, plus uncertainty.
# Acquisition function (Expected Improvement / Upper Confidence Bound) decides where to evaluate next — balancing exploration (uncertain regions) and exploitation (regions with predicted high score).
# Train and score the model at that point; update the surrogate.
# Repeat until budget exhausted.
# Tools: scikit-optimize ( BayesSearchCV ), Optuna , Hyperopt .
# from skopt import BayesSearchCV from sklearn.linear_model import Ridge
opt = BayesSearchCV(Ridge(), { 'alpha' : ( 1e-4 , 1e2 , 'log-uniform' )}, n_iter= 25 , cv= 5 )
opt.fit(X_train_scaled, y_train) print ( f"Best alpha: {opt.best_params_['alpha']:.4f}" )
# Pros: finds excellent hyperparameters with few evaluations; great when each model fit is expensive.
# Cons: more complex setup; the surrogate model itself takes a moment per iteration.
# Comparison
# Method How it explores Best for Cost
# Grid Search Every combination Few hyperparameters with discrete values Exponential in #params
# Random Search Random sampling Many hyperparameters, large ranges Linear in #iterations
# Bayesian Optimization Smart sampling, learns from past trials Expensive-to-train models, want best result with minimum cost Linear, but each step has surrogate-fitting overhead
# Exam questions on this topic
# How does Bayesian Optimization work, and how can it be used to tune the hyperparameters of a Linear Regression model?
# Answer
# Bayesian Optimization is an intelligent hyperparameter tuning technique that uses a probabilistic surrogate model to choose the next set of hyperparameters to try, balancing exploration and exploitation.
# How it works:
# Initialize with a few random hyperparameter samples; train and score each via cross-validation.
# Build a surrogate model (typically a Gaussian Process) that maps hyperparameters → CV score, with uncertainty estimates at every point in the search space.
# Use an acquisition function — such as Expected Improvement (EI) or Upper Confidence Bound (UCB) — to choose the next hyperparameter point. The acquisition function trades off:
# Exploitation — points where the surrogate predicts a high score.
# Exploration — points where the surrogate is uncertain.
# Train the model at the chosen point and record the actual CV score.
# Update the surrogate with this new observation.
# Repeat steps 3–5 until the evaluation budget is exhausted.
# Applied to Linear Regression hyperparameter tuning:
# For Ridge: tune alpha over a log-uniform range like (1e-4, 1e2).
# For ElasticNet: tune alpha AND l1_ratio simultaneously.
# For polynomial regression: tune degree .
# Use BayesSearchCV from scikit-optimize , or Optuna , or Hyperopt .
# Advantages over Grid/Random Search:
# Reaches near-optimal hyperparameters in many fewer trials — important when each fit is expensive.
# Handles continuous, log-scale, and discrete hyperparameters together.
# Provides uncertainty estimates of the score landscape.
# Hyperparameters are settings you choose; parameters are learned from data.
# Grid Search: exhaustive, slow.
# Random Search: sample randomly, faster.
# Bayesian Optimization: smart sampling using a surrogate model — best for expensive models.
# All use cross-validation to score each candidate setting.

#==============================================================================
# TOPIC 17: Numerical Problems Solved
#==============================================================================

# Index of problems
# P1: Birth Weight
# P2: College GPA
# P3: CEO Salary
# P4: Coefficient interpretation
# P5: Mobile p-value
# P6: RMSE comparison
# Practice 1: VIF
# Practice 2: Manual β
# Practice 3: Bias/Variance
# Solving checklist
# What's in this chapter
# Every numerical problem from your past papers, solved step-by-step . Read each one twice — first to follow the answer, second to internalize the method so you can adapt it to a new problem.
# Numerical problems index
# Birth Weight Prediction — Mar 2021 1b
# College GPA from SAT and HS percentile — Mar 2021 1c
# CEO Salary log model — Mar 2021 2a
# Coefficient interpretation y = 2x₁ + 12x₂ + 3x₃ + 5 — Mar 2021 2b / Sample 1d · 2-4 marks
# Mobile sales p-value interpretation — Nov 2021 1c
# RMSE comparison: salary vs age — Nov 2021 1d
# VIF calculation — practice problem
# Manual β computation — practice problem
# Problem 1: Birth Weight Prediction
# 1b · Birth Weight dataset (n = 1,388 births)
# Below is the equation of the births given by women in the United States. Two variables of interest are the dependent variable, infant birth weight in ounces (bwght), and an explanatory variable, average number of cigarettes the mother smoked per day during pregnancy (cigs). The following simple regression was estimated using data on n = 1,388 births: pred_bwght = 119.77 - 0.514*cigs What is the predicted birth weight when cigs = 0? What about when cigs = 20 (one pack per day)? Comment on the difference.
# Step 1 — Identify the model
# This is a simple linear regression with form ŷ = β₀ + β₁·x where:
# x = cigs (cigarettes per day)
# ŷ = pred_bwght (predicted birth weight in ounces)
# β₀ = 119.77 (intercept)
# β₁ = −0.514 (slope)
# Step 2 — Predict at cigs = 0
# Substitute x = 0:
# pred_bwght = 119.77 − 0.514 × 0 = 119.77 ounces
# So a non-smoking mother is predicted to have a baby weighing 119.77 oz ≈ 7.49 lbs ≈ 3.40 kg.
# Step 3 — Predict at cigs = 20
# pred_bwght = 119.77 − 0.514 × 20 = 119.77 − 10.28 = 109.49 ounces
# A mother smoking a pack/day is predicted to have a baby weighing 109.49 oz ≈ 6.84 lbs ≈ 3.10 kg.
# Step 4 — Comment on the difference
# Difference = 119.77 − 109.49 = 10.28 ounces .
# That's roughly 8.6% of the non-smoking baseline weight.
# Babies of pack-a-day smokers are predicted to weigh about 10 ounces less on average — a practically significant reduction.
# This is consistent with public-health findings linking maternal smoking to lower birth weight.
# Caveat: this is a simple regression — other variables (nutrition, prenatal care, alcohol) are not controlled for. Causation cannot be established from a single regression.
# Problem 2: College GPA from SAT and High School Percentile
# 1c · College GPA dataset
# The following equation has been obtained for college Grade Point Average (colgpa) at a US university, colgpa = 1.392 - 0.0135*hsperc + 0.00148*sat where hsperc is percentile in the high school graduating class (defined so that, for example, hsperc=5 means the top 5% of the class) and sat is the combined SAT score.
(a) Why does it make sense for the coefficient on hsperc to be negative?
(b) What is the predicted change in colgpa for a difference in SAT of 140 points (about one standard deviation)?
(c) What change in SAT score would be required to produce a 0.50 increase in colgpa?
# Part (a) — Why is hsperc coefficient negative?
# The variable hsperc is inverted compared to academic performance:
# hsperc = 5 means top 5% of the class — a strong student.
# hsperc = 95 means bottom 5% of the class — a weak student.
# So lower hsperc → better student → higher college GPA. Mathematically, the coefficient on hsperc must be negative to reflect: as percentile rank goes up (worse rank), predicted college GPA goes down. The β = −0.0135 says: each one-unit drop in class rank reduces predicted college GPA by about 0.0135 points .
# Part (b) — Predicted change in colgpa for ΔSAT = 140
# Coefficient on SAT is β_sat = 0.00148. Holding hsperc constant:
# Δcolgpa = β_sat × ΔSAT = 0.00148 × 140 = 0.2072
# Inference: a 140-point higher SAT (about one standard deviation) is associated with an increase of about 0.21 GPA points — meaningful but not huge.
# Part (c) — ΔSAT needed for Δcolgpa = 0.50
# Solve 0.50 = 0.00148 × ΔSAT for ΔSAT:
# ΔSAT = 0.50 / 0.00148 ≈ 337.84 points
# Inference: to gain 0.5 GPA units, a student would need to raise their SAT by roughly 338 points — that's about 2.4 standard deviations, a very large change. SAT alone has a relatively modest effect on college GPA in this model.
# Problem 3: CEO Salary log model — most important problem
# 2a · CEO compensation dataset (n = 209)
# Following equation has been obtained using a CEO Salary database for 209 CEOs of US companies: log(Salary) = 4.32 + 0.280*log(sales) + 0.0174*roe + 0.00024*ros SE values: (0.32) (0.035) (0.0041) (0.00054) where Salary in 1000s of dollars, sales in millions of dollars, return on the firm's equity (roe) in percent, and ros is return on the firm's stock (in percent).
(a) For this regression, what is the predicted percentage increase in salary if the ros increases by 50 points?
(b) Test the null hypothesis that ros has no effect on salary against the alternative that ros has a positive effect. Carry out the test at the 10% significance level. (Reject if t > 1.282)
(c) Would you include ros in a final model explaining CEO compensation in terms of firm performance? Explain.
# Part (a) — % salary change for Δros = 50
# Note: this is a log-linear model — the dependent variable is log(Salary) but ros enters in levels , not log. Because of the log-linear form, the coefficient β_ros = 0.00024 has the interpretation: "a 1-unit increase in ros leads to approximately a 100·β_ros = 0.024% increase in salary."
# For a 50-unit change:
# % Δ Salary ≈ 100 × β_ros × Δros = 100 × 0.00024 × 50 = 1.2%
# So a 50-point increase in ros is associated with about a 1.2% increase in CEO salary . (For exact percentages with larger Δ, use 100·(e^(β·Δros) − 1), but for small β, the linear approximation is fine.)
# Part (b) — Hypothesis test on β_ros (one-tailed at 10%)
# Hypotheses:
# H₀: β_ros = 0 (ros has no effect on salary)
# H₁: β_ros > 0 (ros has a positive effect)
# Test statistic:
# t = β̂_ros / SE(β̂_ros) = 0.00024 / 0.00054 ≈ 0.444
# Decision rule: reject H₀ if t > 1.282 (the critical value at α = 0.10 for a one-tailed test).
# Comparison: 0.444 < 1.282 → fail to reject H₀ .
# Conclusion: at the 10% significance level, there is insufficient evidence to conclude that ros has a positive effect on CEO salary. The coefficient on ros is not statistically distinguishable from zero.
# Part (c) — Should ros be in the final model?
# Reasons to drop ros:
# The hypothesis test (part b) shows the coefficient is not statistically significant even at the lenient 10% level.
# The economic effect is very small — a 50-point change in ros gives only a 1.2% salary change.
# Keeping a noisy non-significant predictor wastes a degree of freedom and inflates uncertainty in the other coefficients.
# Reasons to keep ros:
# If it's of theoretical interest (does stock return affect CEO pay?), reporting "no significant effect" is itself a finding.
# Adjusted R² and out-of-sample MSE could decide empirically.
# Conclusion: based purely on this regression, I would not include ros in the final model — it's not statistically significant and the effect size is small. log(sales) and roe are the meaningful predictors of CEO salary here.
# Problem 4: Coefficient interpretation
# 2b / 1d · ML-1 Sample · 2-4 marks · Generic regression equation
# If y = 2x1 + 12x2 + 3x3 + 5 is the linear regression equation, then explain how the coefficients of x1, x2, x3 affect the value of y.
# Step 1 — Rewrite in standard form
# y = 5 + 2·x₁ + 12·x₂ + 3·x₃
# So β₀ = 5, β₁ = 2, β₂ = 12, β₃ = 3.
# Step 2 — Apply the universal interpretation rule
# "Holding all other features constant, a 1-unit increase in xⱼ is associated with a βⱼ-unit change in y."
# Coefficient Sign & magnitude Interpretation
# β₁ = 2 Positive, smallest 1 unit ↑ in x₁ → 2 units ↑ in y (smallest positive effect)
# β₂ = 12 Positive, largest 1 unit ↑ in x₂ → 12 units ↑ in y (most influential predictor)
# β₃ = 3 Positive, medium 1 unit ↑ in x₃ → 3 units ↑ in y (modest positive effect)
# Step 3 — Comparison & caveats
# Order of influence (raw): x₂ > x₃ > x₁ (12 vs 3 vs 2).
# x₂ is 6× more influential than x₁ (12/2 = 6) and 4× more than x₃ (12/3 = 4).
# The intercept β₀ = 5 is the predicted y when all x's = 0. May or may not be physically meaningful.
# Caveat: coefficient comparisons are only valid if x₁, x₂, x₃ are on the same scale (e.g., all in standardized form). If features have different units, use standardized coefficients .
# Problem 5: p-value interpretation (Mobile phone sales)
# 1c · Mobile phone sales regression
# A linear regression model is build with three independent variable price, advertisement cost and promotion cost to predict unit sales of mobile phone. Say the p value for the t-test of the variable 'advertisement cost' is 0.02. What is your inference on this?
# Step 1 — State the hypotheses
# For each coefficient in a regression, the t-test asks whether that coefficient is statistically distinguishable from zero:
# H₀: β_ad = 0 — advertisement cost has no effect on unit sales.
# H₁: β_ad ≠ 0 — advertisement cost has a (non-zero) effect.
# Step 2 — Interpret the p-value
# The p-value is the probability of seeing a coefficient at least as extreme as the observed one, if H₀ were true . Here p = 0.02 = 2%.
# Step 3 — Compare against significance levels
# Significance level α Threshold Decision
# 10% 0.10 0.02 < 0.10 → reject H₀
# 5% (most common) 0.05 0.02 < 0.05 → reject H₀
# 1% 0.01 0.02 > 0.01 → fail to reject H₀
# Step 4 — Stated inference
# At the conventional 5% significance level, we reject H₀ . Advertisement cost is a statistically significant predictor of mobile phone unit sales. The probability of observing this β value by chance alone (if advertising truly had no effect) is only 2%.
# At the stricter 1% level, the result would not be significant. So we'd say: "significant at the 5% level but not at the 1% level."
# Practical implication: keep advertisement cost in the model. The t-test alone doesn't tell you the magnitude of the effect — you'd want to look at the coefficient value and its confidence interval too.
# Problem 6: RMSE comparison (CTC vs Age)
# 1d · Two unrelated regression models
# The RMSE of the regression model which predicting the CTC salary is 12324 and the RMSE of the other regression model which predicting the age of the person is 55. Comment on the performance of these two models. [output column is not scaled or transformed]
# Step 1 — Recognize the trap
# RMSE has the same units as the target variable y . The two models predict completely different things on completely different scales. Direct comparison of raw RMSEs is meaningless.
# Step 2 — Evaluate each in context
# Model 1: CTC salary, RMSE = 12,324
# Indian CTC values typically range from 3,00,000 to 50,00,000+.
# Suppose mean CTC ≈ 6,00,000.
# %RMSE = 12,324 / 6,00,000 × 100 ≈ 2.05%
# An average error of 2% on salary predictions is very good .
# Model 2: Age, RMSE = 55
# Human ages typically range from 18 to 80.
# Suppose mean age ≈ 35.
# %RMSE = 55 / 35 × 100 ≈ 157%
# An RMSE of 55 is larger than the entire reasonable range of ages . The model is essentially useless — it might as well predict random numbers.
# Step 3 — Use scale-free metrics for fair comparison
# For comparing models predicting different ys, use:
# R² (coefficient of determination) — fraction of variance explained, range (−∞, 1]. A salary model with R² = 0.9 is comparable to an age model with R² = 0.9.
# MAPE — mean absolute percentage error, in %. Already scale-free.
# %RMSE = RMSE / mean(y) × 100 — quick rule of thumb.
# Step 4 — Final inference
# The CTC model performs excellently (relative error ≈ 2%). The age model performs terribly (relative error far exceeds the data range). The raw RMSE numbers (12,324 vs 55) are misleading — without converting to a scale-free metric, you'd wrongly think the age model is better. Always interpret RMSE relative to the magnitude of y.
# Practice Problem 1: VIF Calculation
# Practice problem
# In a regression with 5 features (x₁, …, x₅), suppose when you regress x₁ on the other four features you get R²₁ = 0.85. Compute VIF for x₁ and interpret.
# Solution
# VIF₁ = 1 / (1 − R²₁) = 1 / (1 − 0.85) = 1 / 0.15 ≈ 6.67
# Interpretation: the variance of β̂₁ is about 6.67× larger than it would be if x₁ were uncorrelated with x₂…x₅. Since 6.67 > 5, this is moderate-to-severe multicollinearity . Recommendation: drop x₁ if redundant, or merge with the most correlated companion feature, or use Ridge regression.
# Practice Problem 2: Manual β computation
# Practice problem
# You have 5 data points: (1, 2), (2, 4), (3, 5), (4, 4), (5, 5). Fit a simple linear regression by hand and compute β₀, β₁.
# Solution
# Step 1: means. x̄ = (1+2+3+4+5)/5 = 3, ȳ = (2+4+5+4+5)/5 = 4.
# Step 2: deviations.
# x y x − x̄ y − ȳ (x−x̄)(y−ȳ) (x−x̄)²
# 1 2 −2 −2 4 4
# 2 4 −1 0 0 1
# Sum 6 10
# Step 3: β₁. β₁ = 6 / 10 = 0.6
# Step 4: β₀. β₀ = ȳ − β₁·x̄ = 4 − 0.6·3 = 4 − 1.8 = 2.2
# Final equation: ŷ = 2.2 + 0.6·x
# Verify: predict for x = 3 → ŷ = 2.2 + 1.8 = 4.0 (passes through the centroid (3, 4) as expected).
# Practice Problem 3: Bias/Variance from CV
# Practice problem
# 5-fold CV gives R² scores of [0.82, 0.78, 0.85, 0.80, 0.79]. Compute bias and variance errors, and interpret.
# Solution
# Mean R² = (0.82 + 0.78 + 0.85 + 0.80 + 0.79) / 5 = 4.04 / 5 = 0.808
# Bias error = 1 − 0.808 = 0.192
# Standard deviation = √[((0.82−0.808)² + (0.78−0.808)² + (0.85−0.808)² + (0.80−0.808)² + (0.79−0.808)²) / 5] ≈ √(0.000688) ≈ 0.026
# Variance error = 0.026.
# Interpretation: the model explains about 80.8% of variance — decent but improvable. The low std-dev (0.026) indicates stable performance across folds — no overfitting concern. Bias (1−R²) is moderate at 0.192 — could try richer features or polynomial terms to reduce it.
# Quick numerical-problem checklist
# Solving recipe
# Identify the equation form — linear, log-linear, log-log, polynomial.
# Identify what's asked — predict y, compute Δy, find Δx, test a hypothesis.
# Substitute the given numbers carefully.
# Show every step — calculation by calculation. Examiners give partial marks.
# State units — ounces, %, GPA points, .
# Interpret — translate the number back into plain English.
# State caveats — "this is correlation, not causation"; "valid only if assumptions hold."
# Simple linear regression questions: substitute in ŷ = β₀ + β₁x.
# Log-linear questions: 100·β gives the % effect per unit change.
# Hypothesis tests: t = β̂ / SE; reject H₀ if |t| > critical value (or p < α).
# RMSE comparisons across different ys are meaningless — use R² or MAPE.
# VIF = 1/(1−R²_j); show every digit of the calculation.

#==============================================================================
# TOPIC 18: Exam Questions by Topic
#==============================================================================

# Machine Learning Fundamentals & Pipelines
# Linear Regression Assumptions
# Multicollinearity & VIF
# Bias-Variance Tradeoff & Cross-Validation
# Regularization (Ridge/Lasso/ElasticNet)
# Gradient Descent
# Evaluation Metrics (R²/Adj R²/RMSE/MAPE)
# Feature Selection
# Data Transformation & Feature Engineering
# Hyperparameter Tuning & Optimization
# Numerical Problems on Regression Models
# OLS Linear Regression & Model Building
# Data Preprocessing (Missing Values, Outliers, Encoding, Scaling)
# DataFrame Operations (Pandas)
# Exploratory Data Analysis (EDA)
# Open-ended Modeling & Business Interpretation
# Problem Statement / Context
# How to use
# Index of all 138 unique exam questions
# Every distinct question from your 8 ESA papers, grouped by topic. Each card shows the verbatim question, its source, dataset, and marks. Click the topic header to jump to the corresponding learning chapter for the full theory.
# Topic Question count Linked chapter
# Machine Learning Fundamentals & Pipelines 3 → Chapter
# Linear Regression Assumptions 10 → Chapter
# Multicollinearity & VIF 6 → Chapter
# Bias-Variance Tradeoff & Cross-Validation 9 → Chapter
# Regularization (Ridge/Lasso/ElasticNet) 14 → Chapter
# Gradient Descent 1 → Chapter
# Evaluation Metrics (R²/Adj R²/RMSE/MAPE) 7 → Chapter
# Feature Selection 5 → Chapter
# Data Transformation & Feature Engineering 5 → Chapter
# Hyperparameter Tuning & Optimization 6 → Chapter
# Numerical Problems on Regression Models 6 → Chapter
# OLS Linear Regression & Model Building 14 → Chapter
# Data Preprocessing (Missing Values, Outliers, Encoding, Scaling) 42 → Chapter
# DataFrame Operations (Pandas) 28 → Chapter
# Exploratory Data Analysis (EDA) 24 → Chapter
# Open-ended Modeling & Business Interpretation 5 → Chapter
# Problem Statement / Context 6 —
# Total 191
# Machine Learning Fundamentals & Pipelines → Open chapter
# Topic basics: definition of ML, supervised vs unsupervised vs reinforcement, regression vs classification, the LECESSTE pipeline. Full answers in chapter 01.
# 1d (UE20CS905)
# Describe the key steps in building a supervised machine learning pipeline from data ingestion to model deployment. Include tools or techniques relevant at each stage.
# 1e (UE20CS905)
# What is the difference between the Classification and Regression problem?
# 1a (UE20CS905)
# What is Machine learning? State any two types of machine learning.
# Linear Regression Assumptions → Open chapter
# Topic basics: LINER (Linearity, Independence, Normality, Equal variance, no multicollinearity). Each verified visually + statistically (Breusch-Pagan, Durbin-Watson, Shapiro-Wilk). Full answers in chapter 07.
# 5b Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check assumptions of linear regression. Write your inferences.
# 1a (UE20CS905)
# Describe the key assumptions of linear regression. For each assumption, explain how it can be verified using visual or statistical techniques, and the potential impact if the assumption is violated.
# 5b (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Check assumptions of linear regression. Write your inferences.
# 1c (UE20CS905)
# Explain the assumptions of linear regression.
# 5b (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Use OLS statsmodels package to build the Linear Regression model (Without multicollinearity feature) on the train set. Generate the summary report. check assumptions of linear regression. Write your inferences.
# 1a (UE20CS905)
# Explain Heteroscedasticity and Multicollinearity in Linear Regression.
# 1d (UE20CS905)
# How can you deal with autocorrelation of errors?
# 1c (UE20CS905)
# State the assumptions of linear regression algorithm.
# 3(ii) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Explore the statistical significance of the model build and comment about all the assumptions.
# 5b (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Use OLS statsmodels package to build the Linear Regression model (Without multicollinearity feature) on the train set. Generate the summary report. check assumptions of linear regression. Write your inferences.
# Multicollinearity & VIF → Open chapter
# Topic basics: VIF = 1/(1−R²_j); < 5 OK, > 10 severe. Detect via correlation matrix and VIF. Fix by dropping, combining, Ridge, or PCA. Full answers in chapter 08.
# 4f Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# check and reduce multicollinearity using VIF.
# 4f (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# check and reduce multicollinearity using VIF.
# 1a (UE20CS905)
# What is Multicollinearity? How to detect the presence of multicollinearity and which variables are involved in it?
# 1a (UE20CS905)
# What is Multicollinearity? How to detect the presence of multicollinearity and which variables are involved in it?
# 4i (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check and reduce multicollinearity using VIF.
# 4h (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Drop columns that are not needed, then evaluate multicollinearity with VIF and reduce it where possible.
# Bias-Variance Tradeoff & Cross-Validation → Open chapter
# Topic basics: Error = Bias² + Variance + Noise. Operationally: bias = 1 − mean(R²), variance = std(R²) from k-fold CV. Full answers in chapters 09 and 11.
# 6a Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Train a Linear Regression model using sklearn on the training data and calculate the bias error (1 - mean R²) and variance error (standard deviation of R²) by performing 5-fold cross-validation.
# 6a (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Train a Linear Regression model using sklearn on the training data and calculate the bias error (1 - mean R²) and variance error (standard deviation of R²) by performing 5-fold cross-validation.
# 1b (UE20CS905)
# Explain the procedure involved in k-fold cross validation.
# 1e (UE20CS905)
# How the problem of overfitting can be reduced in Linear regression? What is bias variance trade off?
# 1b (UE20CS905)
# Explain the procedure involved in k-fold cross validation.
# 1e (UE20CS905)
# What strategies can be employed to mitigate overfitting in Linear Regression? Provide an explanation of various forms of Linear Regression that address the issue of overfitting.
# 6a (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Using sklearn's linear regression model train model on the train set compute bias error (mean r2) and variance error (standard deviation r2) across 5 fold cross validation.
# 1b (UE20CS905)
# How can you handle overfitting and underfitting?
# 6b (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Using sklearn's linear regression model train model on the train set compute bias error (mean r2) and variance error (standard deviation r2) across 5 fold cross validation.
# Regularization (Ridge/Lasso/ElasticNet) → Open chapter
# Topic basics: Ridge L2 (shrinks all), Lasso L1 (zeros some), ElasticNet (mix). All add α·penalty to MSE. Tune α via CV. Full answers in chapter 10.
# 1a Feb 2025 ESA (UE20CS905)
# What role does regularization play in improving Linear Regression models?
# 6 Feb 2025 ESA (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Model Comparisons and Hyperparameter tuning
# 6b Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Train below models and obtain values using 5 fold cross validation on train data and 'rmse' metric. Find the metric score in the test set and suggest the best model. - ElasticNet(alpha=0.1, l1_ratio=0.5) (5 marks) - Lasso(alpha=0.01, max_iter=500) (5 marks)
# 1b (UE20CS905)
# What is regularization in linear regression? Compare and contrast Lasso and Ridge regression in terms of mathematical formulation, impact on coefficients, and use cases.
# 6 (UE20CS905) · — marks · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Model Comparisons and Hyperparameter tuning
# 6b (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Train below models and obtain values using 5 fold cross validation on train data and 'rmse' metric. Find the metric score in the test set and suggest the best model. - ElasticNet(alpha=0.1, l1_ratio=0.5) (5 marks) - Lasso(alpha=0.01, max_iter=500) (5 marks)
# 3(ii) (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Model Comparisons and Hyperparameter tuning
# 3(ii).1 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Train below models and obtain values using 5 fold cross validation on train data and 'RMSE' metric. Find the metric (RMSE) score in test set and suggest the best model. - Ridge(alpha=1, max_iter=500) (5 marks) - Lasso(alpha=0.01, max_iter=500) (5 marks) - ElasticNet(alpha=0.1, l1_ratio=0.01, max_iter=500) (5 marks)
# 6 (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Model Comparisons and Hyperparameter tuning
# 6b (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Train below models and obtain values using 5 fold cross validation on train data and 'rmse' metric. Find the metric score in the test set and suggest the best model. - Ridge(alpha=1, max_iter=500) - Lasso(alpha=0.01, max_iter=500)
# 1a (UE20CS905)
# Write the expression for the cost function, which need to be minimized in Linear regression with RIDGE regularization.
# 1e (UE20CS905)
# If we increase the value of lambda, what will happen to the estimated coefficients in RIDGE model?
# 6 (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Model Comparisons and Hyperparameter tuning
# 6c (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Train below models and obtain values using 5 fold cross validation on train data and 'rmse' metric. Find the metric score in test set and suggest the best model. - Ridge(alpha=1, max_iter=500) (5 marks) - Lasso(alpha=0.01, max_iter=500) (5 marks)
# Gradient Descent → Open chapter
# Topic basics: iterative minimization, β := β − α·∂J/∂β. Variants: Batch, SGD, Mini-Batch. Full answer in chapter 06.
# 2c (UE20CS905)
# Explain Gradient Descent in brief.
# Evaluation Metrics (R²/Adj R²/RMSE/MAPE) → Open chapter
# Topic basics: R² explains variance; Adj R² penalizes feature count; RMSE in y units (outlier-sensitive); MAPE is %. Full answers in chapter 12.
# 1b Feb 2025 ESA (UE20CS905)
# What is the difference between R² and Adjusted R², and when should each be used?
# 5c Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Predict the values using test set, Compute measures of RMSE, MAPE, R-square for test set.
# 5c (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Predict the values using test set, Compute measures of RMSE, MAPE, R-square for test set.
# 5d (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Compute measures of RMSE, MAPE, R-square for test set.
# 1b (UE20CS905)
# How adjusted R-square is differing from R-square? Brief the role of adjusted R-square in feature selection process.
# 1d (UE20CS905) · RMSE comparison numerical example
# The RMSE of the regression model which predicting the CTC salary is 12324 and the RMSE of the other regression model which predicting the age of the person is 55. Comment on the performance of these two models. [output column is not scaled or transformed]
# 5d (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Compute measures of RMSE, MAPE, R-square for test set.
# Feature Selection → Open chapter
# Topic basics: Filter (correlation, VIF), Wrapper (Forward/Backward/RFE), Embedded (Lasso). Full answers in chapter 14.
# 1c Feb 2025 ESA (UE20CS905)
# What are Wrapper Methods in feature selection, and how are they applied in Linear Regression?
# 1c (UE20CS905)
# What is Recursive Feature Elimination (RFE)? Explain how it works, its advantages and limitations, and how it can be used to improve model performance in linear regression.
# 1d (UE20CS905)
# Explain the procedure involved in Forward Feature Selection.
# 1d (UE20CS905)
# Explain the procedure involved in Forward Feature Selection.
# 6a (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Perform backward elimination for selecting the "best" features, you can use SequentialFeatureSelector (SFS) from mlxtend.
# Data Transformation & Feature Engineering → Open chapter
# Topic basics: log, Box-Cox, Yeo-Johnson, polynomial features, interactions, datetime extraction, binning. Full answers in chapter 14.
# 2(iii).5 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Convert the feature 'size' to int by removing alphabetic content and keep only numeric content. In case of missing/null content replace by constant numeric value 2.
# 2(iii).6 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Convert the feature 'total_sqft' to numerical using 'to_numeric' method. Also, replace all its missing entries by mean.
# 1c (UE20CS905)
# Discuss the need for data transformations in a linear regression model. Also write about various techniques employed.
# 3(iii) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Make the model more reliable by performing appropriate feature engineering techniques.
# 3(iv) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Explore the possibility of improving the model performance by introducing new interactive features.
# Hyperparameter Tuning & Optimization → Open chapter
# Topic basics: Grid (exhaustive), Random (sampled), Bayesian (smart-sampled). All score via CV. Full answers in chapter 16.
# 1d Feb 2025 ESA (UE20CS905)
# How does Bayesian Optimization work, and how can it be used to tune the hyperparameters of a Linear Regression model?
# 6c Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Using Grid search on the ridge model, find the best value of alpha and corresponding rmse value on the test set.
# 6c (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Using Grid search on the ridge model, find the best value of alpha and corresponding rmse value on the test set.
# 3(ii).2 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Using Random search on Lasso model find the best value of alpha and corresponding RMSE value on test set.
# 6c (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Using Grid search on Lasso model find the best value of alpha and corresponding rmse value on test set.
# 6d (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Using Grid serach on Lasso model find the best value of alpha and corresponding rmse value on test set.
# Numerical Problems on Regression Models → Open chapter
# These appear primarily in the paper. Step-by-step solutions for every numerical in chapter 17.
# 1b (UE20CS905) · Birth Weight regression — n=1,388 births (textbook example)
# Below is the equation of the births given by women in the United States. Two variables of interest are the dependent variable, infant birth weight in ounces (bwght), and an explanatory variable, average number of cigarettes the mother smoked per day during pregnancy (cigs). The following simple regression was estimated using data on n = 1,388 births: pred_bwght = 119.77 - 0.514*cigs What is the predicted birth weight when cigs = 0? What about when cigs = 20 (one pack per day)? Comment on the difference.
# 1c (UE20CS905) · GPA2 college students dataset — n=4,137 (textbook example)
# Using the data in GPA2 on 4,137 college students, the following equation was estimated by OLS: colgpa = 1.392 - 0.0135*hsperc + 0.00148*sat where colgpa is measured on a four-point scale, hsperc is the percentile in the high school graduating class (defined so that, for example, hsperc = 5 means the top 5% of the class), and sat is the combined math and verbal scores on the student achievement test. • Why does it make sense for the coefficient on hsperc to be negative? • Suppose that two high school graduates, A and B, graduated in the same percentile from high school, but Student A's SAT score was 140 points higher (about one standard deviation in the sample). What is the predicted difference in college GPA for these two students? Is the difference large? • Holding hsperc fixed, what difference in SAT scores leads to a predicted colgpa difference of .50, or one-half of a grade point? Comment on your answer.
# 2a (UE20CS905) · CEO salary regression — n=209 firms (textbook example)
# 2b (UE20CS905) · Numerical example (coefficients given)
# If y = 2x1 + 12x2 + 3x3 + 5 is the linear regression equation, then explain how the coefficients of x2 and x3 affect the value of y.
# 1d (UE20CS905) · Numerical example (coefficients given)
# If y = 2x1 + 12x2 + 3x3 + 5 is the linear regression equation, then explain how the coefficients of x1 and x2 affect the value of y.
# 1c (UE20CS905) · Mobile-phone sales numerical example
# A linear regression model is build with three independent variable price, advertisement cost and promotion cost to predict unit sales of mobile phone. Say the p value for the t-test of the variable 'advertisement cost' is 0.02. What is your inference on this?
# OLS Linear Regression & Model Building → Open chapter
# Topic basics: ŷ = β₀ + Σβⱼxⱼ; OLS normal equation β̂ = (XᵀX)⁻¹Xᵀy; statsmodels.OLS for full report. See chapters 02, 03, 13.
# 5 Feb 2025 ESA (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Perform Below Modeling Tasks
# 5a Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Use OLS statsmodels package to build the Linear Regression model (Without multicollinearity feature) on the train set to ensure feature 'Weight' as target(y). Generate the summary report.
# 5 (UE20CS905) · — marks · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Perform Below Modeling Tasks
# 5a (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Use OLS statsmodels package to build the Linear Regression model (Without multicollinearity feature) on the train set to ensure feature 'Weight' as target(y). Generate the summary report. (Note: question text says 'Weight' as target — paper appears to be re-using the Feb 2025 wording; in context the target is laptop Price.)
# 3(i) (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Perform Below Modeling Tasks
# 3(i).2 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Use OLS statsmodels package to build the Linear Regression model on the train set. Also, generate the summary report.
# 3(i).3 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Using sklearn's linear regression model train model on the train set and interpret the coefficients.
# 5 (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Perform Below Modeling Tasks
# 5c (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Predict the values using test set.
# 3b (UE20CS905) · Admission / Student Placement dataset — SlNo, Gender, Percent_SSC/HSC/Degree/MBA, Boards, Streams, Course, Experience_Yrs, Entrance_Test, Percentile_ET, Specialization_MBA, Marks Communication, Marks_Projectwork, Placement, Salary
# Fit a base model. Please write your key observations. i. What is the overall R²? Please comment on whether it is good or not. ii. What is the adjusted R²? Is it different from R²? Why? iii. Which variables are significant. Explain the Feature Selection Technique used? iv. Is there multicollinearity, Suggest ways to remove it. v. Which other key model output parameters do you want to look at?
# 2b (UE20CS905) · Airbnb NYC dataset — id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365
# Fit a base model. Please write your key observations. i. What is the overall R²? Please comment on whether it is good or not. (2 marks) ii. What is the adjusted R²? Is it different from R²? Why? (3 marks) iii. Which variables are significant? (4 marks) iv. Is there multicollinearity? (4 marks) v. Which other key model output parameters do you want to look at? (2 marks)
# 3(i) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Build the linear regression to predict the 'traffic_volume'. Evaluate the base model performance using appropriate measures.
# 5 (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Perform Below Modeling Tasks
# 5c (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Use sklearn library to Predict the values using test set.
# Data Preprocessing (Missing Values, Outliers, Encoding, Scaling) → Open chapter
# Topic basics: 5 sub-steps — handle missing (mean/median/mode/drop), outliers (IQR/Z-score/clip/drop), encoding (label/dummy n-1), scaling (StandardScaler), splitting. Full answers in chapter 15.
# 4 Feb 2025 ESA (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Perform Data pre-processing as Mentioned Below.
# 4a Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check for the presence of missing values across features and represent them visually also treat it
# 4b Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Examine the numerical features for any outliers and provide visual evidence and also treat it with dropping.
# 4c Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Perform n-1 dummy encoding to convert categorical features into numerical, followed by StandardScaler transformation on the numerical data.
# 4d Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Split the pre-processed dataframe into 2 parts y (output), x (input) features.
# 4e Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Plot output feature and print skewness. Describe your observations.
# 4 (UE20CS905) · — marks · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Perform Data pre-processing as Mentioned Below.
# 4a (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Check for the presence of missing values across features and represent them visually also treat it
# 4b (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Examine the numerical features for any outliers and provide visual evidence and also treat it with dropping.
# 4c (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Perform label encoding to convert categorical features into numerical, followed by StandardScaler transformation on the numerical data.
# 4d (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Split the pre-processed dataframe into 2 parts y (output), x (input) features.
# 4e (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Plot output feature and print skewness. Describe your observations.
# 2(iii) (UE20CS905) · — marks · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Pre-process the Dataframe as Mentioned Below.
# 2(iii).1 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Replace missing values of the feature 'balcony' with numerical value 0 and convert its feature type to int.
# 2(iii).2 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Replace missing values of the feature 'bath' missing values with numerical 1 and convert feature type to int.
# 2(iii).3 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Replace missing values of the feature 'location' with a constant "missing".
# 2(iii).4 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Replace missing values of the feature 'society' with a constant "missing".
# 2(iii).7 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Eliminate all the outlies records/rows from Dataframe with respect to feature 'bath'.
# 2(iii).8 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# convert 3 categorical features i.e. 'availability', 'location' and 'society' into numerical using label encoding.
# 2(iii).9 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Perform one hot encoding on feature 'area_type', also ensure output columns are of type int.
# 3(i).1 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Split the processed Dataframe into 2 parts train and test with ratio as 70:30. Ensure feature 'price' as target(y).
# 4 (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Perform Data pre-processing as Mentioned Below.
# 4a (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check and visualize if there are any missing values feature wise.
# 4b (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Implement a strategy to deal with the missing values with reason.
# 4c (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check and visualize if there are any outliers present in the numerical features.
# 4d (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Treat the outlies records/rows from Dataframe, Use IQR and Drop the outliers in the feature.
# 4e (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Convert the categorical features into numerical using n-1 dummy encoding techniques.
# 4f (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Perform standardscaler on numerical data.
# 4g (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Split the pre-processed data frame into 2 parts y (output), x (input) features.
# 4h (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Plot output feature, input feature and print skewness.
# 5a (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Split the pre-processed data frame into 2 parts train and test with a ratio as 80:20. Ensure feature 'Weight' as target(y).
# 1e (UE20CS905)
# Explain any two of the data preprocessing steps.
# 2(ii) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Perform required pre-processing techniques on the dataset, which are required for building the Machine Learning model. Justify the approaches/techniques used for pre-processing. Explain/type the clear reason for the choice of your techniques for the different pre-processing techniques.
# 4 (UE20CS905) · — marks · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Perform Data pre-processing as Mentioned Below.
# 4a (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Examine the presence of missing values across features, visualize them, and handle accordingly.
# 4b (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Analyze each numerical feature for potential outliers and visualize the findings.
# 4c (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Treat the outlies records/rows from Dataframe, Use IQR and Drop the outliers in the feature.
# 4d (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Convert the categorical features into numerical using n-1 dummy encoding techniques.
# 4e (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Perform StandardScaler on numerical data.
# 4f (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Split the pre-processed dataframe into 2 parts y (output), x (input) features.
# 4g (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Plot output, input feature and print skewness.
# 5a (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Split the pre-processed dataframe into 2 parts train and test with ratio as 80:20. Ensure feature 'totlngth' as target(y).
# DataFrame Operations (Pandas) → Open chapter
# Topic basics: read_csv, head/info/describe, dtype changes, groupby, value_counts, isnull, dropna, fillna, get_dummies, indexing. Code patterns in chapter 20.
# 2a Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print the dimensions of the dataset i.e. no of rows and columns.
# 2b Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print the data types of all the features.
# 2c Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Does any feature need type casting? if yes, perform it.
# 2d Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print statistical summary of all the numeric as well as categorical features and drop unnecessary features.
# 2e Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Find out how many unique categories are available and number of instances in each of the categorical features.
# 2a (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Print the dimensions of the dataset i.e. no of rows and columns.
# 2b (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Print the data types of all the features.
# 2c (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Does any feature need type casting? if yes, perform it.
# 2d (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Print statistical summary of all the numeric as well as categorical features and drop unnecessary features.
# 2e (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Find out how many unique categories are available and number of instances in each of the categorical features.
# 2(i).1 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Read/load the dataset as a pandas Dataframe.
# 2(i).2 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Print/show the dimensions of Dataframe i.e., no of rows and columns.
# 2(i).3 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Print/show the data types of all the features/columns.
# 2(i).4 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Print/show statistical summary of all the numeric features.
# 2(i).5 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Print/show statistical summary for all the categorical variable.
# 2(i).6 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Find out Feature wise Missing value counts.
# 2a (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Read/load the dataset.
# 2b (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print the dimensions of the dataset i.e. no of rows and columns.
# 2c (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print the data types of all the features.
# 2d (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Does any feature need type casting? if yes, perform the same and change the datatype to the correct type.
# 2e (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print statistical summary of all the numeric as well as categorical features and drop unnecessary features.
# 2f (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Find out how many unique categories are available and number of instances in each of the categorical features.
# 2a (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Read/load the dataset.
# 2b (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Print the dimensions of the dataset i.e. no of rows and columns.
# 2c (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Print the data types of all the features.
# 2d (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Does any feature need type casting? if yes, perform the same and change the datatype to the correct type.
# 2e (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Print statistical summary of all the numeric as well as categorical features and drop unnecessary features.
# 2f (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Determine the number of distinct categories in each categorical feature and the instance count for each category.
# Exploratory Data Analysis (EDA) → Open chapter
# Topic basics: histograms, boxplots, scatterplots, correlation heatmap, value counts, descriptive stats. Code patterns in chapter 20.
# 3 Feb 2025 ESA (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# EDA (Exploratory data Analysis)
# 3a Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Explore the associations between the numerical predictors and the target feature using visualizations. Describe your observations.
# 3b Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Examine how the categorical features are associated with the target variable. Use visualizations and provide your interpretations.
# 3 (UE20CS905) · — marks · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# EDA (Exploratory data Analysis)
# 3a (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Explore the associations between the numerical predictors and the target feature using visualizations. Describe your observations.
# 3b (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Examine how the categorical features are associated with the target variable. Use visualizations and provide your interpretations.
# 2(ii) (UE20CS905) · — marks · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Perform Below Exploratory Data Analysis(EDA) Tasks.
# 2(ii).1 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Show/Visualize the relationship between features 'bath' and 'price' using scattered plot.
# 2(ii).2 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Show/Visualize the relationship between features 'balcony' and 'price' using scattered plot.
# 2(ii).3 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# show/Visualize the relationship between features 'bath','balcony' and 'price' using 3D Scatterplot.
# 2(ii).4 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Show outliers distribution of variable 'bath' by drawing Boxplot.
# 3 (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# EDA (Exploratory data Analysis)
# 3a (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check/Visualize the relationship between the numerical features with the target feature. State the inferences.
# 3b (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Visualize the relationship between 'target' and 'V_length'.
# 3c (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check/Visualize the relationships between categorical features and the target feature. State the inferences.
# 3d (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print skewness of numerical feature.
# 3a (UE20CS905) · Admission / Student Placement dataset — SlNo, Gender, Percent_SSC/HSC/Degree/MBA, Boards, Streams, Course, Experience_Yrs, Entrance_Test, Percentile_ET, Specialization_MBA, Marks Communication, Marks_Projectwork, Placement, Salary
# DATA DESCRIPTION: The data set consists of complete educational details of students right from their schooling to MBA and previous work experience. Our main objective is to predict the Salary of the students based on the info available.
ATTRIBUTES: SlNo, Gender, Percent_SSC, Board_SSC, Percent_HSC, Board_HSC, Stream_HSC, Percent Degree, Course_Degree, Experience_Yrs, Entrance_Test, Percentile_ET, Percent_MBA, Specialization_MBA, Marks Communication, Marks_Projectwork, Placement, Salary. Perform Exploratory data analysis and summarize important observations from the data set. Some pointers which would help you, but don't be limited by these: i. What are the number of rows; no. & types of variables (continuous, categorical etc.) ii. Calculate five-point summary for numerical variables iii. Summarize observations for categorical variables — no. of categories, % observations in each category iv. Check for defects in the data. Perform necessary actions to 'fix' these defects. check for numerical/categorical variable (wrong representation), missing values, outlier treatment, skewness, encoding v. Summarize relationships among variables. vi. Split dataset into train and test (70:30)
# 2a (UE20CS905) · Airbnb NYC dataset — id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365
# 2(i) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Understand the relation between each input and output variables. Support the finding with abstract tables and graphs. Summarize 5 important key findings (understanding) about the dataset.
# 3 (UE20CS905) · — marks · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# EDA (Exploratory data Analysis)
# 3a (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Explore the relationships between numerical features and the target feature through visualization, and provide your observations.
# 3b (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Visualize the relationship between 'belly' and 'totlngth'.
# 3c (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Check/Visualize the relationships between categorical features and the target feature using violinplot. State the inferences.
# 3d (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Print skewness of numerical feature.
# Open-ended Modeling & Business Interpretation → Open chapter
# These typically end Section C. Apply: build model → evaluate → interpret coefficients → check assumptions → recommend. Pipeline template in chapter 20.
# 4a (UE20CS905) · Admission / Student Placement dataset — SlNo, Gender, Percent_SSC/HSC/Degree/MBA, Boards, Streams, Course, Experience_Yrs, Entrance_Test, Percentile_ET, Specialization_MBA, Marks Communication, Marks_Projectwork, Placement, Salary
# How do you improve the accuracy of the model? Write clearly the changes that you will make before re-fitting the model. Fit the final model. Please feel free to have any number of iterations to get to the final answer. Marks are awarded based on the quality of the final model you are able to achieve.
# 4b (UE20CS905) · Admission / Student Placement dataset — SlNo, Gender, Percent_SSC/HSC/Degree/MBA, Boards, Streams, Course, Experience_Yrs, Entrance_Test, Percentile_ET, Specialization_MBA, Marks Communication, Marks_Projectwork, Placement, Salary
# Summarize as follows: i. Summarize the overall fit of the model and list down the measures to prove that it is a good model. ii. Write down a business interpretation/explanation of the model — which variables are affecting the target the most and explain the relationship. Feel free to use charts or graphs to explain. iii. What changes from the base model had the most effect on model performance? iv. What are the key risks to your results and interpretation?
# 3a (UE20CS905) · Airbnb NYC dataset — id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365
# How do you improve the accuracy of the model? Write clearly the changes that you will make before re-fitting the model. Fit the final model. • Feature Engineering / Feature Selection • Regularization • Cross Validation
Please feel free to have any number of iterations to get to the final answer. Marks are awarded based on the quality of the final model you are able to achieve.
# 3b (UE20CS905) · Airbnb NYC dataset — id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365
# Summarize as follows: i. Summarize the overall fit of the model and list down the measures to prove that it is a good model. ii. Write down a business interpretation/explanation of the model — which variables are affecting the target the most and explain the relationship. Feel free to use charts or graphs to explain. iii. What changes from the base model had the most effect on model performance? iv. What are the key risks to your results and interpretation? • Justification for selecting a model.
# 3(v) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Write the business inferences through the model parameters.
# Problem Statement / Context
# These are dataset descriptions, not standalone questions. They tell you which dataset Section B/C uses. Refer to the dataset notes in the index.
# 2 Feb 2025 ESA (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Problem Statement: Fish Weight Prediction. With a dataset of fish species, with some of its characteristics like vertical, diagonal, length, height, and width. Try to predict the weight of the fish based on their characteristics. We will use the Linear Regression Method to see whether the weight of the fish is related to their characteristic. Basic Perform below Pandas DataFrame Operations to understand the data.
# 2 (UE20CS905) · — marks · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Problem Statement: The objective here is to build a regression model that can accurately predict the price of a laptop based on its key features such as brand, processor type, RAM size, storage configuration, graphics card, display specifications, and operating system. This model can assist consumers in making informed purchase decisions and help retailers in dynamic pricing.
# 2 (UE20CS905) · — marks · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Problem Statement: Housing price dataset of Bengaluru city is provided. Based on the given details predict the price of the house.
Features: area_type, availability, location, size (BHK), society (encrypted), total_sqft, bath, balcony, price (target, in Lakhs).
# 2 (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Problem Statement: Fish Weight Prediction. With a dataset of fish species, with some of its characteristics like vertical, diagonal, length, height, and width. Try to predict the weight of the fish based on their characteristics. We will use the Linear Regression Method to see whether the weight of the fish is related to their characteristic. Basic Perform below Pandas DataFrame Operations to understand the data.
# 2 (UE20CS905) · — marks · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# 2 (UE20CS905) · — marks · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Problem Statement: Predicting a Possum's total length using Linear Regression. you use your regression skills to predict the total length of a possum, its head length, whether it is male or female? etc. This classic practice regression dataset. The possum data frame consists of morphometric measurements on each of 104 mountain brushtail possums, trapped at seven sites from Southern Victoria to central Queensland. Basic Pandas DataFrame Operations to understand the data.
# How to use this index
# Get familiar with the breadth. Scroll through every topic — note which appear most often.
# For each topic that appears 5+ times (Assumptions, Regularization, OLS, Preprocessing) — make sure you can answer ANY of those questions cold.
# For each topic that appears 1-2 times — read the corresponding chapter once, but don't over-invest.
# Click "Open chapter" to read full theory, formulas, code, and worked examples.

#==============================================================================
# TOPIC 19: Most Important Topics
#==============================================================================

# How to read this page
# Section A — 1-mark questions
# Section B — Q2/Q3 patterns
# Section C — big questions
# Topic frequency table
# Hot-10 topics for ESA
# Common traps & mistakes
# 3-day final revision plan
# How to read this page
# I went through every Section-A, Section-B, and Section-C question across 8 ESA papers (, ML-1 Sample, Nov 2021, Aug 2023, , Nov 2024, Feb 2025, ) and counted
how often each topic appeared. The result is a ranked list of topics that actually show up,
not just topics that look important in a textbook.
# The big lesson — six topics dominate Section A. If you master them, you nearly
always score 4–5 out of 5 on Section A. The rest comes from Sections B and C, where everyone
loses marks on careful reading.
#  Section A — five 1-mark questions (5 marks total)
# Section A is five short questions , often labelled 1a, 1b, 1c, 1d, 1e.
Each is 1 mark. They mostly test:
# One-line definitions ("Define multicollinearity")
# One-line "why" answers ("Why use VIF?")
# Quick numerical readings of OLS output
# True/False with one-line justification
# What appeared in Section A across 8 papers
# Topic Times asked Papers
# LR Assumptions (LINER) 5 Mar21, Sample, Aug23, May25, Mar24
# Multicollinearity / VIF 4 Sample, Aug23, Mar24, (Nov24)
# Bias–Variance / Overfitting 4 Sample, Aug23, Mar24, May25
# Cross-Validation 3 Aug23, Mar24, May25
# Forward / Feature Selection 3 Aug23, Mar24, Feb25
# Regularization (Ridge/Lasso/EN) 4 Nov21 (×2), Feb25, May25
# Evaluation Metrics (R², RMSE, p-value) 5 Nov21 (×3), Feb25, May25
# Hyperparameter Tuning (Grid/Random/Bayes) 2 Feb25, (other)
# Numerical reading of regression coefficients 3 Mar21 (×3 — bwght, gpa, ceo)
# Pattern — almost every paper has at least one Section A from each of these three
buckets: (1) an assumption / theory question , (2) a multicollinearity or
overfitting question , (3) a numerical or metric question .
#  Section B — Q2 and Q3 (15 marks total)
# Q2 (8 marks) is almost always about DataFrame operations / pandas —
load data, drop columns, group-by, slice, head/tail, info, describe. You write small code
snippets or describe what each line does.
# Q3 (7 marks) is EDA — Exploratory Data Analysis : plot the data,
boxplots, pairplots, correlation heatmap, identify outliers, comment on skewness.
# Question Marks Almost always asks for…
# Q2 8 pandas operations on a CSV — read_csv, head, info, describe, drop, group-by, value_counts
# Q3 7 EDA — visualisations, missing values, outliers, comment on distribution
# Strategy: learn the 10 most common pandas one-liners (see File 20: Python Pipeline ) and you can answer Q2 confidently.
For Q3, remember the EDA recipe: SHAPE → HEAD → INFO → DESCRIBE → MISSING → BOX → CORR .
# Section C — Q4, Q5, Q6 (60 marks total — the bulk of the paper)
# Section C is where most marks live, and it has a very predictable structure.
# Question Marks Theme
# Q4 20–25 Pre-modelling pipeline : missing values, outliers, encoding, scaling, train/test split, multicollinearity check (VIF), feature transformations, feature selection
# Q5 20 OLS / linear regression model building : fit OLS, read summary, check assumptions, residual diagnostics, interpret coefficients
# Q6 20 Model comparison and tuning : build multiple models (Linear, Ridge, Lasso, ElasticNet, Polynomial), compare with R²/RMSE, hyperparameter tuning (GridSearch / RandomSearch / Bayesian), final business interpretation
# Q4 sub-parts that appear almost every paper
# 4a/4b/4c: read & describe data, handle missing values
# 4d/4e: outlier detection (IQR / boxplot / Z-score)
# 4f/4g: encoding categorical variables (one-hot, label, ordinal)
# 4h/4i: multicollinearity check using VIF, drop or transform
# 4j: feature scaling (StandardScaler / MinMaxScaler)
# 4k: train/test split
# Q5 sub-parts
# Fit OLS using statsmodels, print summary
# Identify significant variables (p-value < 0.05)
# Check assumptions: linearity, normality of residuals, homoscedasticity, independence
# Compute and interpret R², Adjusted R², F-statistic
# Residual plots — Q-Q plot, residuals vs fitted
# Q6 sub-parts
# Compare Linear vs Ridge vs Lasso vs ElasticNet
# Use cross-validation (k-fold, k=5 or 10) to evaluate
# Apply GridSearchCV / RandomizedSearchCV for tuning alpha
# Interpret final model in business terms
# The 70% rule — if you can confidently do Q4 (preprocessing) and Q5 (OLS + assumptions),
you have already secured 40+ marks out of 60 in Section C. That's the difference between failing and
a B grade.
# Topic frequency table — overall
# Across all 8 papers, all sections combined, here is how often each topic was tested:
# Rank Topic Approx times asked Total marks across papers
# 1 Pandas / DataFrame operations 8 (every paper) ~64 marks
# 2 OLS Regression + Summary interpretation 8 ~120 marks
# 3 Multicollinearity & VIF 7 ~30 marks
# 4 Assumptions of LR (LINER) 6 ~25 marks
# 5 Regularization (Ridge / Lasso / ElasticNet) 6 ~80 marks
# 6 Cross-validation 5 ~20 marks
# 7 EDA & data visualisations 8 ~56 marks
# 8 Bias-Variance / Overfitting 5 ~15 marks
# 9 Feature engineering / transformations 5 ~30 marks
# 10 Feature selection (Forward / RFE / Wrapper) 4 ~15 marks
# 11 Hyperparameter tuning (Grid/Random/Bayes) 4 ~30 marks
# 12 Evaluation metrics (R², RMSE, MAPE, MAE) 6 ~25 marks
# 13 Outlier detection (IQR / boxplot) 5 ~20 marks
# 14 Encoding (one-hot, label, ordinal) 5 ~20 marks
# 15 Numerical reading of regression coefficients 4 ~16 marks
# 16 Polynomial regression 3 ~15 marks
# 17 Gradient descent 2 ~5 marks
# The Hot-10 — concepts you must NOT skip
# If you have only a few days, master these ten topics. Together they cover ~80% of all marks.
# # Topic Why it's hot Where to study
# 1 OLS regression + statsmodels summary Q5 every paper, 20 marks; you must read p-values, R², coefficients File 02 , File 13
# 2 Multicollinearity & VIF 4f/4h/4i in Q4 every paper; also a 1-mark Section A File 08
# 3 LINER assumptions 1-mark Section A almost every paper + appears in Q5 File 07
# 4 Ridge / Lasso / Elastic Net 20 marks in Q6 every paper; 1-mark in Section A repeatedly File 10
# 5 Cross-validation (k-fold) Section A + appears in Q6 tuning File 11
# 6 Pandas one-liners Q2 every paper; 8 marks each File 20
# 7 EDA recipe Q3 every paper; 7 marks each File 20
# 8 Outlier handling + Encoding + Scaling Q4 every paper; 10–15 marks each File 15
# 9 R², Adjusted R², RMSE, p-value reading 1-mark and Section C interpretation File 12
# 10 Hyperparameter tuning (GridSearchCV) Q6 part of Section C File 16
# Hot-10 mnemonic — "OMLR-CPE-OEH":
# O LS · M ulticollinearity · L INER · R egularization · C V · P andas · E DA · O utliers/Encoding/Scaling · E valuation metrics · H yperparameters
#  Common traps that lose marks
# Several mistakes appear again and again in how students answer ESA questions. Avoid these and
you'll score noticeably higher with the same knowledge.
# Trap What goes wrong The fix
# Comparing RMSEs across different targets Says "model A is better because RMSE 55 < RMSE 12324" when the targets are age vs CTC RMSE has same units as target. Different targets → not comparable. Use %RMSE / mean target instead.
# Dummy-variable trap One-hot encodes a 3-level category and creates 3 columns → causes multicollinearity Always use drop_first=True in pd.get_dummies or drop="first" in OneHotEncoder
# Treating ordinal as nominal One-hot encodes "Low/Medium/High" instead of mapping 1/2/3 Use OrdinalEncoder when an order exists; one-hot when it doesn't
# Scaling before train/test split Fits scaler on full data → information leak from test set Split first, then fit_transform on train only, transform on test
# Imputing on whole dataset Same data leak as above Fit imputer on train only
# R² always means "good model" High R² on training is meaningless if test R² is much lower (overfit) Always report Adjusted R² and a held-out / CV score, not just train R²
# p-value > 0.05 means "no relationship" Says "x has no effect on y" Better: "with this data, we fail to reject H₀; we don't have evidence of a non-zero effect"
# Confusing VIF threshold Uses VIF > 0.05 (mixing it up with p-value) VIF > 5 is a warning, > 10 is serious. Range starts at 1, no upper limit.
# Ridge "selects features" Says Ridge does feature selection like Lasso Ridge shrinks coefficients toward zero but rarely to zero. Lasso can. Elastic Net does both.
# Forgetting to scale before Ridge/Lasso Penalty is dominated by features with large units (e.g. salary in lakhs vs age in years) Always StandardScale features before any regularised regression
# Using R² to compare different-sized feature sets R² always increases when you add features Use Adjusted R² or held-out RMSE for comparison
# "Linear regression assumes the data is linear" Vague phrasing It assumes a linear relationship between predictors and target , in the chosen form. You can include polynomial or log terms and still call it "linear regression".
# 3-day final revision plan
# If you have only 3 days before the ESA, here is a tight schedule:
# Morning: File 01 + File 02 + File 03
# Afternoon: File 07 (LINER) + File 08 (VIF) + File 09
# Evening: File 10 (Ridge/Lasso/EN) + File 11 + File 12
# Last hour: re-read File 18 Section-A questions only — do them on paper.
# Morning: File 17 — work through every numerical with pen on paper
# Afternoon: File 13 + File 14 + File 15 + File 16
# Evening: File 20 — write out the full pandas + sklearn pipeline 2 times from memory
# Morning: pick the latest paper () from File 18 and attempt it timed (3 hours)
# Afternoon: review answers, list weaknesses
# Night before: re-read File 21 (Cheatsheet) only — high-yield mnemonics, formulas, one-liners
# The night before — DO NOT learn anything new. Just re-read File 21 (cheatsheet),
sleep 7+ hours. Tired brains forget things faster than well-rested ones.

#==============================================================================
# TOPIC 20: Python Pipeline
#==============================================================================

# Step 0 — Imports
# Step 1 — Load data (Q2)
# Step 2 — EDA (Q3)
# Step 3 — Missing values (Q4)
# Step 4 — Outlier handling (Q4)
# Step 5 — Encoding (Q4)
# Step 6 — Scaling (Q4)
# Step 7 — Train/test split (Q4)
# Step 8 — Multicollinearity / VIF (Q4)
# Step 9 — Feature selection (Q4)
# Step 10 — OLS / statsmodels (Q5)
# Step 11 — Assumption checks (Q5)
# Step 12 — Model comparison (Q6)
# Step 13 — Hyperparameter tuning (Q6)
# Step 14 — Final interpretation (Q6)
# Quick snippets cheatsheet
# How to use this file
# This is the full pipeline for any regression Section C question. The order
matches how Q4 → Q5 → Q6 are structured in the ESA. You can literally read this top-to-bottom
during the exam and answer most questions.
# Every section has:
# What this step does (one paragraph in plain English)
# The code with comments on every line
# What the output looks like
# How to read it for the exam
# Memorize the order, not the syntax. If you remember the 14 steps in sequence,
you'll never blank during a Section C question. The exact pandas function name can be looked up.
# Step 0 — Imports (always at the top)
# Standard imports for every regression task. Memorize these — they appear in every Section C answer.
# # Data handling import pandas as pd import numpy as np # Visualization import matplotlib.pyplot as plt import seaborn as sns # sklearn — preprocessing from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV, RandomizedSearchCV from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, OrdinalEncoder from sklearn.impute import SimpleImputer # sklearn — models from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet from sklearn.preprocessing import PolynomialFeatures from sklearn.feature_selection import RFE, SequentialFeatureSelector # sklearn — metrics from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_absolute_percentage_error # statsmodels for OLS summary tables import statsmodels.api as sm from statsmodels.stats.outliers_influence import variance_inflation_factor # Set figure defaults plt.rcParams[ "figure.figsize" ] = ( 8 , 5 )
sns.set_style( "whitegrid" )
# Step 1 — Load data (Q2 territory)
# Goal: read the CSV, get a feel for size and types, look at a few rows.
This is exactly what Q2 (8 marks) tests.
# EDA recipe (Q3, 7 marks) — the standard 7-step exploratory approach is SHAPE → HEAD → INFO → DESCRIBE → MISSING → BOX → CORR .
# Step 2 — Exploratory Data Analysis (Q3, 7 marks)
# Goal: visually understand the data. Find skewness, outliers, relationships.
# # Histogram for one feature — see the distribution shape df[ "price" ].hist(bins= 30 )
plt.title( "Distribution of Price" )
plt.xlabel( "Price" ); plt.ylabel( "Frequency" )
plt.show() # All numeric features at once df.hist(bins= 30 , figsize=( 12 , 8 ))
plt.tight_layout(); plt.show() # Boxplot — see outliers and quartiles sns.boxplot(x=df[ "price" ])
plt.show() # Pairplot — relationships between every pair (use only when small # of features) sns.pairplot(df[[ "price" , "area" , "bedrooms" , "bathrooms" ]])
plt.show() # Correlation heatmap — find multicollinearity hints + relationships with target corr = df.corr(numeric_only= True )
sns.heatmap(corr, annot= True , cmap= "coolwarm" , fmt= ".2f" )
plt.show() # Scatter — relationship between one feature and target sns.scatterplot(x= "area" , y= "price" , data=df)
plt.show() # Skewness — is the column heavily skewed (> 1 or < -1 is a flag)? df[ "price" ].skew() # Count of categorical values sns.countplot(x= "city" , data=df); plt.xticks(rotation= 45 ); plt.show()
# Step 3 — Missing values (Q4 sub-part)
# Goal: find missing entries and decide how to handle them.
# Trap: if you fill missing values before train/test split, you leak info
from the test set into the train set. Always split first, then impute on train, then apply the
same imputer to test.
# Step 4 — Outlier detection & treatment (Q4 sub-part)
# Goal: find rows whose values lie way outside the normal range. Decide whether
to drop, cap, or transform.
# # Method 1: IQR (Interquartile Range) — most common for ESA Q1 = df[ "price" ].quantile( 0.25 )
Q3 = df[ "price" ].quantile( 0.75 )
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR # Boolean mask of outliers mask_outlier = (df[ "price" ] < lower) | (df[ "price" ] > upper)
print( "Outlier count:" , mask_outlier.sum()) # Strategy A: drop them df_no_out = df[~mask_outlier] # Strategy B: cap (winsorize) — keep the row but clip extreme value df[ "price" ] = df[ "price" ].clip(lower=lower, upper=upper) # Method 2: Z-score (assumes near-normal distribution) from scipy.stats import zscore
z = np.abs(zscore(df[ "price" ]))
mask = z > 3 # > 3 sigma # Method 3: just look — boxplot sns.boxplot(x=df[ "price" ])
#  Step 5 — Encoding categoricals (Q4 sub-part)
# Goal: ML models need numbers. Convert text categories into numeric form.
# # A) One-hot encoding — for nominal (no order) categories # IMPORTANT: drop_first=True avoids the dummy variable trap df = pd.get_dummies(df, columns=[ "city" , "furnishing" ], drop_first= True , dtype= int ) # sklearn version (preferred in pipelines) ohe = OneHotEncoder(drop= "first" , sparse_output= False )
encoded = ohe.fit_transform(df[[ "city" ]]) # B) Ordinal encoding — when categories have a natural order (Low < Medium < High) order = [[ "Low" , "Medium" , "High" ]]
oe = OrdinalEncoder(categories=order)
df[ "quality_enc" ] = oe.fit_transform(df[[ "quality" ]]) # C) Manual mapping (when you know the levels) mp = {{ "yes" : 1 , "no" : 0 }}
df[ "has_garage" ] = df[ "has_garage" ].map(mp) # D) Label encoding — typically for the target column only from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df[ "target_enc" ] = le.fit_transform(df[ "target" ])
# Trap (dummy-variable trap): if a category has k levels and you create k dummies, they sum to 1 → perfect multicollinearity. Always drop one level.
#  Step 6 — Feature scaling (Q4 sub-part)
# Goal: bring all features onto a comparable range. Required before
Ridge/Lasso/ElasticNet, KNN, gradient descent. Not strictly required for plain OLS.
# # StandardScaler — mean 0, std 1 (most common) scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train) # fit only on TRAIN X_test_sc = scaler.transform(X_test) # reuse same scaler on TEST # MinMaxScaler — squeeze into [0, 1] mm = MinMaxScaler()
X_train_mm = mm.fit_transform(X_train)
X_test_mm = mm.transform(X_test)
# Order matters! Always: (1) split → (2) fit scaler on train → (3) transform train,
(4) transform test. Never fit_transform on test data.
#  Step 7 — Train/test split (Q4 sub-part)
# X = df.drop(columns=[ "price" ]) # features y = df[ "price" ] # target X_train, X_test, y_train, y_test = train_test_split( X, y, test_size= 0.2 , # 80% train / 20% test random_state= 42 # reproducibility — same split every time ) print(X_train.shape, X_test.shape)
# Step 8 — Multicollinearity / VIF (Q4 sub-part)
# Goal: detect features that are too correlated with each other.
VIF > 5 is a warning, > 10 is serious. Drop or combine those features.
# # Add a constant column (statsmodels needs it) X_const = sm.add_constant(X_train) # Compute VIF for each column vif = pd.DataFrame()
vif[ "feature" ] = X_const.columns
vif[ "VIF" ] = [variance_inflation_factor(X_const.values, i) for i in range(X_const.shape[ 1 ])]
print(vif.sort_values( "VIF" , ascending= False )) # Strategy: drop the column with highest VIF, recompute, repeat until all < 5 X_train = X_train.drop(columns=[ "highest_vif_col" ])
# How to read the output:
# VIF value Meaning
# 1 No correlation with other predictors
# 1–5 Moderate, usually OK
# 5–10 High — investigate / drop
# > 10 Serious multicollinearity — drop
# Step 9 — Feature selection (Q4 sub-part)
# # A) Forward Selection — add one variable at a time sfs = SequentialFeatureSelector( LinearRegression(), n_features_to_select= 5 , direction= "forward" , scoring= "r2" , cv= 5 )
sfs.fit(X_train, y_train)
selected = X_train.columns[sfs.get_support()].tolist() # B) Backward Elimination — start with all, drop the worst at each step sfs_b = SequentialFeatureSelector( LinearRegression(), n_features_to_select= 5 , direction= "backward" , scoring= "r2" , cv= 5 ) # C) RFE — Recursive Feature Elimination rfe = RFE(LinearRegression(), n_features_to_select= 5 )
rfe.fit(X_train, y_train)
selected_rfe = X_train.columns[rfe.support_].tolist() # D) Filter — correlation with target corr_with_target = X_train.corrwith(y_train).abs().sort_values(ascending= False )
# Step 10 — OLS / statsmodels (Q5, 20 marks!)
# This is the most important step in Section C. The summary table is the source
of half the marks in Q5.
# # statsmodels — gives you a full summary table X_const = sm.add_constant(X_train) # add intercept column model = sm.OLS(y_train, X_const).fit()
print(model.summary()) # Pull out individual values model.params # coefficients model.pvalues # p-values model.rsquared # R² model.rsquared_adj # Adjusted R² model.fvalue # F-statistic model.f_pvalue # p-value of F-statistic # Predict on test X_test_const = sm.add_constant(X_test)
y_pred = model.predict(X_test_const)
# How to read the OLS summary table (this is gold for the exam)
# Field Means What's "good"
# R-squared % of variance in y explained Higher is better; 0–1
# Adj. R-squared R² penalised for #features Use this when comparing models with different feature counts
# F-statistic / Prob (F) Joint significance of all predictors Prob < 0.05 → at least one predictor matters
# coef How much y changes per unit increase in x Sign and magnitude tell direction and strength
# std err Uncertainty around the coefficient Smaller is better
# t coef / std err |t| > 2 ≈ significant
# P>|t| p-value of that coefficient < 0.05 → significant
# [0.025, 0.975] 95% confidence interval for the coef Doesn't include 0 → significant
# Durbin-Watson Autocorrelation in residuals ~ 2 ideal; < 1.5 or > 2.5 = trouble
# Jarque-Bera (JB) Normality of residuals Prob > 0.05 → residuals look normal
# Cond. No. Multicollinearity indicator > 30 = warning
# Step 11 — Assumption checks (Q5 sub-part)
# # Residuals (errors) resid = model.resid
fitted = model.fittedvalues # 1. Linearity & Homoscedasticity — residuals vs fitted should look random plt.scatter(fitted, resid, alpha= 0.5 )
plt.axhline( 0 , color= "red" , linestyle= "--" )
plt.xlabel( "Fitted" ); plt.ylabel( "Residuals" )
plt.title( "Residuals vs Fitted" )
plt.show() # 2. Normality — Q-Q plot sm.qqplot(resid, line= "45" )
plt.title( "Q-Q Plot" ); plt.show() # Statistical normality test — Shapiro-Wilk from scipy.stats import shapiro
stat, p = shapiro(resid) # p > 0.05 → residuals look normal # 3. Homoscedasticity formal test — Breusch-Pagan from statsmodels.stats.diagnostic import het_breuschpagan
bp = het_breuschpagan(resid, X_const) # bp[1] is the p-value; > 0.05 → no heteroscedasticity # 4. Independence — Durbin-Watson from statsmodels.stats.stattools import durbin_watson
dw = durbin_watson(resid) # dw ≈ 2 → no autocorrelation
# Step 12 — Model comparison (Q6 part)
# Goal: build several models, compare them with the same metric, pick the best.
# # 1. Linear Regression — baseline lr = LinearRegression().fit(X_train_sc, y_train)
pred_lr = lr.predict(X_test_sc) # 2. Ridge — L2 penalty ridge = Ridge(alpha= 1.0 ).fit(X_train_sc, y_train)
pred_ridge = ridge.predict(X_test_sc) # 3. Lasso — L1 penalty (does feature selection) lasso = Lasso(alpha= 0.1 ).fit(X_train_sc, y_train)
pred_lasso = lasso.predict(X_test_sc) # 4. ElasticNet — mix of L1 and L2 en = ElasticNet(alpha= 0.1 , l1_ratio= 0.5 ).fit(X_train_sc, y_train)
pred_en = en.predict(X_test_sc) # 5. Polynomial — for non-linear patterns poly = PolynomialFeatures(degree= 2 , include_bias= False )
X_train_poly = poly.fit_transform(X_train_sc)
X_test_poly = poly.transform(X_test_sc)
poly_lr = LinearRegression().fit(X_train_poly, y_train)
pred_poly = poly_lr.predict(X_test_poly) # Compare def evaluate(y_true, y_pred, name): print(f "{{name}}" ) print(f " R² : {{r2_score(y_true, y_pred):.4f}}" ) print(f " RMSE : {{np.sqrt(mean_squared_error(y_true, y_pred)):.2f}}" ) print(f " MAE : {{mean_absolute_error(y_true, y_pred):.2f}}" ) print() evaluate(y_test, pred_lr, "Linear" )
evaluate(y_test, pred_ridge, "Ridge" )
evaluate(y_test, pred_lasso, "Lasso" )
evaluate(y_test, pred_en, "ElasticNet" )
evaluate(y_test, pred_poly, "Polynomial-2" )
#  Step 13 — Hyperparameter tuning (Q6 part)
# # A) GridSearchCV — exhaustive search over a grid param_grid = {{ "alpha" : [ 0.001 , 0.01 , 0.1 , 1 , 10 , 100 ]}}
grid = GridSearchCV(Ridge(), param_grid, cv= 5 , scoring= "neg_mean_squared_error" )
grid.fit(X_train_sc, y_train)
print( "Best alpha:" , grid.best_params_)
print( "Best CV RMSE:" , np.sqrt(-grid.best_score_))
best_ridge = grid.best_estimator_ # B) RandomizedSearchCV — random sample of the grid (faster for big grids) from scipy.stats import uniform
rs = RandomizedSearchCV( ElasticNet(), {{ "alpha" : uniform( 0.001 , 10 ), "l1_ratio" : uniform( 0 , 1 )}}, n_iter= 50 , cv= 5 , scoring= "r2" , random_state= 42 )
rs.fit(X_train_sc, y_train)
print( "Best params:" , rs.best_params_) # C) Bayesian Search — smart, builds a probabilistic model of the search space # pip install scikit-optimize from skopt import BayesSearchCV
bayes = BayesSearchCV( Ridge(), {{ "alpha" : ( 1e-3 , 1e2 , "log-uniform" )}}, n_iter= 30 , cv= 5 )
bayes.fit(X_train_sc, y_train)
# Step 14 — Final business interpretation (Q6 part)
# The last sub-part of Q6 typically asks for business interpretation . Use this template:
# Template answer (adapt to the dataset):
# State the chosen model and its CV-RMSE / R² on the test set.
# Pick the 2–3 features with the largest standardised coefficients. State the direction (sign).
# Translate the coefficient into a one-sentence business statement : "A 1-unit increase in area is associated with an expected X change in price, holding other features constant."
# Mention which features the model dropped (if Lasso) or de-emphasised (Ridge) — these are
candidates the business can de-prioritise.
# State a caveat: "These are associations under the LR assumptions; not causal claims."
# # Save coefficients with feature names for interpretation coef_df = pd.DataFrame({{ "feature" : X_train.columns, "coef" : best_ridge.coef_
}}).sort_values( "coef" , key=abs, ascending= False )
print(coef_df.head( 10 ))
# Quick snippets cheatsheet
# Pandas one-liners
# df.shape # (rows, cols) df.head(); df.tail(); df.sample( 5 )
df.info(); df.describe()
df.isnull().sum() # missing per col df.dropna(); df.fillna( 0 )
df[ "col" ].mean(), .median(), .std(), .skew()
df.groupby( "city" )[ "price" ].mean()
df[ "city" ].value_counts()
df.corr(numeric_only= True )
df.sort_values( "price" , ascending= False )
df.drop(columns=[ "id" ])
df.rename(columns={{ "old" : "new" }})
pd.get_dummies(df, drop_first= True )
# Numpy quick
# np.mean(arr); np.median(arr); np.std(arr)
np.sqrt(x); np.log(x); np.log1p(x)
np.where(cond, a, b)
np.percentile(arr, [ 25 , 50 , 75 ])
# Sklearn essentials
# # Fit pattern is the SAME for every estimator model = SomeEstimator(...)
model.fit(X_train, y_train)
preds = model.predict(X_test)
score = model.score(X_test, y_test) # CV one-liner scores = cross_val_score(LinearRegression(), X, y, cv= 5 , scoring= "r2" )
print( "Mean R²:" , scores.mean(), "+/-" , scores.std())
# Metrics one-liners
# r2_score(y_true, y_pred)
mean_squared_error(y_true, y_pred)
np.sqrt(mean_squared_error(y_true, y_pred)) # RMSE mean_absolute_error(y_true, y_pred)
mean_absolute_percentage_error(y_true, y_pred)
# Full pipeline in one go (paste-and-go)
# If a Section C question says "build a complete regression pipeline for this dataset", here is the full skeleton in 50 lines:
# You can quote-paste this 50-line skeleton in any Section C answer that says
"build a regression model end-to-end". Adjust the column names and you have all 60 marks of
Section C in front of you.

#==============================================================================
# TOPIC 21: Cheatsheet and Mnemonics
#==============================================================================

# Mnemonics master list
# Every formula on one page
# Concept one-liners
# Model one-liners
# When to use what
# Red-flag values to memorize
#  Common traps
# How to read OLS / numbers
#  Pipeline steps you must remember
# Answer templates
# Mnemonics master list
# Mnemonic Stands for Used in
# LINER L inearity · I ndependence · N ormality of residuals · E qual variance (homoscedasticity) · R esiduals uncorrelated with predictors (≈ no multicollinearity) 5 assumptions of Linear Regression
# LECESSTE L oad · E DA · C lean · E ncode · S cale · S plit · T rain · E valuate ML pipeline steps
# SHID-BC S hape · H ead · I nfo · D escribe · B oxplot · C orrelation EDA recipe (Q3, 7 marks)
# R-MAE-MAPE-MSE-RMSE R² · MAE · MAPE · MSE · RMSE Five regression metrics (in increasing penalty for big errors)
# OMLR-CPE-OEH O LS · M ulticollinearity · L INER · R egularization · C V · P andas · E DA · O utliers · E ncoding · H yperparameters Hot-10 exam topics
# "Lasso = Less" "Ridge = Reduce" Lasso eliminates features (coefs to zero), Ridge reduces them but keeps all Telling Lasso vs Ridge apart
# "VIF over 5? Drive feature alive." (i.e. drop it) VIF > 5 → warning, > 10 → drop Multicollinearity threshold
# "R² always grows; Adj R² won't snow" R² never decreases when you add features; Adj R² can Comparing models with different #features
# "Bias is big-picture wrong; Variance is bouncy along" High bias = model too simple (consistently off); high variance = model too complex (jumps with data) Bias-variance tradeoff
# "Train low, test high → overfit cry" Training error tiny but test error big = overfitting Diagnosing overfit vs underfit
# "DROP-first to avoid the trap" Use drop_first=True in get_dummies to avoid dummy-variable trap One-hot encoding
# "Split-Fit-Transform" Split first, fit scaler/imputer on train, transform test Avoiding data leakage
# "DW close to 2 → independence is true" Durbin-Watson ≈ 2 means no autocorrelation Reading OLS summary
# "p < 0.05 → keep alive" p-value < 0.05 → coefficient significant, keep variable Reading OLS summary
# "Grid is greedy, Random is rapid, Bayes is brainy" GridSearch tries everything (slow), RandomSearch samples (faster), Bayesian models the search space (smartest) Hyperparameter tuning methods
# "K-fold shuffles trust" k-fold CV gives a more trustworthy estimate than a single train/test split Why use cross-validation
# Every formula on one page
# Regression form
# Simple LR: y = β₀ + β₁x + ε
# Multiple LR: y = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ + ε
# Polynomial: y = β₀ + β₁x + β₂x² + ... + βₖxᵏ + ε
# Matrix form: Y = Xβ + ε
# OLS estimation
# Normal equation: β̂ = (XᵀX)⁻¹Xᵀy
# Slope (SLR): β₁ = Σ(xᵢ−x̄)(yᵢ−ȳ) / Σ(xᵢ−x̄)²
# Intercept (SLR): β₀ = ȳ − β₁x̄
# Cost functions
# MSE: (1/n) · Σ(yᵢ − ŷᵢ)²
# RMSE: √MSE — same units as the target
# MAE: (1/n) · Σ|yᵢ − ŷᵢ|
# MAPE: (100/n) · Σ|yᵢ − ŷᵢ| / |yᵢ|
# Evaluation
# R²: 1 − (SS res / SS tot ) = 1 − (Σ(y−ŷ)² / Σ(y−ȳ)²)
# Adjusted R²: 1 − [(1−R²)(n−1) / (n−p−1)]
# where n = #samples, p = #predictors
# Gradient descent
# Update rule: β j := β j − α · ∂J/∂β j
# α = learning rate
# Regularization (with shrinkage penalty)
# Ridge (L2): minimize Σ(y − ŷ)² + λ·Σβⱼ²
# Lasso (L1): minimize Σ(y − ŷ)² + λ·Σ|βⱼ|
# ElasticNet: minimize Σ(y − ŷ)² + λ·[α·Σ|βⱼ| + (1−α)·Σβⱼ²]
# Multicollinearity
# VIF for feature j: VIF j = 1 / (1 − R j ²)
# where R j ² = R² of regressing x j on all other predictors
# Tolerance: 1 / VIF (alternative form)
# Inference
# t-statistic: t = β̂ / SE(β̂)
# F-statistic: F = [(SS tot − SS res )/p] / [SS res /(n−p−1)]
# 95% CI for coef: β̂ ± 1.96·SE(β̂) (large n)
# Bias-Variance from cross-validation
# Operational bias: 1 − mean(R² across folds)
# Operational variance: std(R² across folds)
# Train/test split & CV
# k-fold CV: split into k parts; train on k−1, test on 1; rotate; average score
# Concept one-liners
# Concept One-line definition
# Supervised learning Learning a function from input → output using labeled data.
# Regression Supervised learning where the target is continuous (e.g. price, salary).
# Linear regression Fit a straight line (or hyperplane) that minimises sum of squared residuals.
# OLS Ordinary Least Squares — the classic method that gives a closed-form β̂ = (XᵀX)⁻¹Xᵀy.
# Polynomial regression Linear regression on polynomial-transformed features; still linear in coefficients.
# Cost function Number that measures how wrong the model's predictions are; we minimise it.
# MSE Average squared error — penalises big mistakes more.
# RMSE Square root of MSE — same units as the target, easier to interpret.
# MAE Average absolute error — robust to outliers, easier to read.
# R² Proportion of variance in y explained by the model. 1 = perfect, 0 = useless.
# Adjusted R² R² penalised for adding more predictors. Use this to compare different-sized models.
# Residual y true − y pred . The error the model makes on each point.
# Gradient descent Iteratively update parameters in the direction that reduces the cost.
# Learning rate (α) Step size in gradient descent. Too big → diverge; too small → slow.
# Linearity Relationship between predictors and target is approximately a straight line.
# Independence (of errors) Errors at different observations are uncorrelated.
# Normality (of residuals) Residuals follow a normal (bell-curve) distribution.
# Homoscedasticity Variance of residuals is constant across all fitted values.
# Heteroscedasticity Variance of residuals changes with fitted value (funnel shape).
# Multicollinearity Two or more predictors are highly correlated; coefficients become unstable.
# VIF Variance Inflation Factor — measures how much a coefficient variance is inflated by multicollinearity.
# Underfitting (high bias) Model too simple; misses the pattern. Train and test error both high.
# Overfitting (high variance) Model too complex; memorises noise. Train low, test high.
# Bias-variance tradeoff Reducing one tends to raise the other; we seek the sweet spot.
# Regularization Add a penalty on coefficient size to fight overfitting.
# Ridge (L2) Penalty = λ·Σβ². Shrinks coefficients toward zero but keeps them all.
# Lasso (L1) Penalty = λ·Σ|β|. Can shrink coefficients exactly to zero → does feature selection.
# ElasticNet Mix of L1 and L2; useful when many features are correlated.
# α (alpha) in Ridge/Lasso Strength of penalty. α = 0 → no penalty. Higher α → more shrinkage.
# Cross-validation Split data into k folds; train on k−1, test on 1; rotate; average.
# Hyperparameter A parameter you set before training (like alpha or k) — not learned.
# Q-Q plot Plot of residual quantiles vs theoretical normal quantiles. Straight line → normal.
# p-value Probability of seeing such a result if the true coefficient were 0. < 0.05 → significant.
# Feature engineering Transforming or creating features (log, polynomial, interaction) to help the model.
# Feature selection Picking the most useful subset of features (forward, backward, RFE).
# StandardScaler Subtract mean, divide by std. Brings each feature to mean 0, std 1.
# One-hot encoding Convert a k-level category into k−1 binary columns (drop one level).
# Dummy-variable trap Keeping all k dummies → perfect multicollinearity with the intercept.
# Model one-liners — when each shines
# Model Best for Watch out for
# Linear Regression (OLS) Interpretable baseline; small to medium n; LINER assumptions roughly hold Multicollinearity, non-linearity
# Ridge Many correlated features; you want to keep all features in the model Doesn't do feature selection
# Lasso Many features, suspect most are useless; want a sparse model Among correlated features it picks one randomly
# ElasticNet Many correlated features AND want some selection Two hyperparameters (alpha, l1_ratio)
# Polynomial Regression Clearly non-linear pattern; one or two key features Easy to overfit at high degree; explodes feature count
# When to use what — quick decisions
# Situation What to use
# Continuous target (price, salary) Regression
# Categorical target (yes/no, class) Classification (out of scope for this exam)
# Many features, > 100, suspect lots of irrelevant ones Lasso
# Many correlated features, want them all Ridge
# Mixed — many correlated, also want sparsity ElasticNet
# Visible curved pattern Polynomial regression
# Compare 2 models with different #features Adjusted R² (not R²)
# Compare 2 models predicting same target RMSE / MAE / R² on test set
# Compare 2 models predicting different targets (e.g. age vs CTC) Cannot compare RMSE directly. Use %RMSE / mean target, or R².
# Outliers heavily affect results MAE (more robust than MSE/RMSE)
# Errors of large magnitude must be punished MSE / RMSE
# Need to interpret coefficients statsmodels OLS (gives full summary)
# Need to predict only sklearn LinearRegression / Ridge / Lasso
# Small dataset (n < 100) k-fold CV with k=5; avoid deep models
# Want robust estimate of generalisation Cross-validation, not single train/test split
# Tuning 1–2 hyperparameters with small ranges GridSearchCV
# Tuning many hyperparameters or large ranges RandomizedSearchCV / Bayesian
# Heavy-tailed target distribution Try log(y) transformation
# Funnel-shaped residuals Heteroscedasticity → log-transform y or use weighted LS
# Red-flag values to memorize
# Quantity Healthy Warning Action
# p-value < 0.05 0.05 – 0.10 > 0.05 → not significant
# VIF 1 – 5 5 – 10 > 10 → drop / combine feature
# Durbin-Watson 1.5 – 2.5 (≈2) 1.0 – 1.5 or 2.5 – 3.0 < 1 or > 3 → autocorrelation
# R² Higher (context dependent) — Always pair with Adjusted R²
# Skewness −1 to 1 ±1 to ±2 Beyond ±2 → consider log/Box-Cox
# Condition number (in OLS) < 30 30 – 100 > 100 → severe multicollinearity
# Train R² vs Test R² Close Test ~ 5–10% lower Big gap → overfitting
# k for k-fold CV 5 or 10 — Standard choices; avoid k=2
# α (Ridge/Lasso) Tuned via CV — Try {0.001, 0.01, 0.1, 1, 10, 100}
# Test set size 20–30% — Below 10% → unreliable estimates
#  Common traps
# Don't compare RMSE across different targets. RMSE has the units of the target. RMSE 55 (age in years) is not better than RMSE 12,324 (CTC in ). Use %RMSE relative to mean(y), or use R².
# Always drop_first=True for one-hot. Otherwise you get the dummy-variable trap (perfect multicollinearity).
# Scale and impute on TRAIN only. Splitting after scaling/imputing leaks info from test → over-optimistic scores.
# Ridge does not do feature selection. It shrinks coefficients toward zero but rarely to zero. Lasso can. Elastic Net does both.
# Regularised models need scaled features. Without scaling, the penalty unfairly punishes features measured on larger scales (e.g., salary in lakhs vs age in years).
# R² always increases with more features. So R² is bad for comparing models with different numbers of predictors. Use Adjusted R² or held-out RMSE.
# "Linear" in Linear Regression refers to the coefficients, not x. y = β₀ + β₁x + β₂x² is still called "linear regression" (linear in β).
# p-value > 0.05 ≠ "no relationship". It means we don't have enough evidence to reject the null. Underpowered samples can hide real effects.
# VIF threshold is 5/10, not 0.05. Don't confuse VIF with p-value.
# k-fold CV with shuffle is essential when the data is ordered (e.g. by date or by class). Otherwise folds become biased.
# GridSearchCV's best_score_ is on the validation folds, not the held-out test set. Always score the final tuned model on a separate test set.
# Feature scaling does not change the fit of plain OLS. The coefficients change but R²/RMSE don't. Scaling matters for Ridge/Lasso/EN/SGD.
# Don't use only training error to choose models. Always evaluate on held-out data or via cross-validation.
# Outlier removal must be justified. "Just delete points outside 1.5·IQR" can throw away genuine signal. Investigate first.
# Imputing with mean for skewed data is a bad idea. Use median for skewed numeric columns; mode for categorical.
# How to read OLS / numbers in 60 seconds
# Reading a coefficient
# If area has coefficient +125.3 and y is price () :
# "Holding all other features constant, a one-unit increase in area is associated with an
expected increase of 125.3 in price."
# Reading a p-value
# p = 0.02 (less than 0.05): "reject the null hypothesis that this coefficient is zero — the
variable is statistically significant at the 5% level."
# p = 0.30 (more than 0.05): "fail to reject the null — we don't have enough evidence to claim
this variable has a non-zero effect."
# Reading R²
# R² = 0.78: "about 78% of the variance in y is explained by this model."
# Reading Adjusted R²
# If R² = 0.81 but Adj R² = 0.62 → many features added with little real value.
# Closer Adj R² to R² → features are pulling their weight.
# Reading the F-statistic
# Prob(F) < 0.05 → at least one predictor is significant. Prob(F) > 0.05 → none are; the model
overall is no better than just predicting the mean of y.
# Reading VIF
# VIF = 8.4 for x : "the variance of x's coefficient is inflated 8.4× compared to a
no-multicollinearity scenario. Strong multicollinearity — investigate or drop."
# Reading log-coefficients
# If model is log(salary) = α + β·log(sales) and β = 0.28:
# "a 1% increase in sales is associated with a 0.28% increase in salary."
# If model is log(salary) = α + β·roe and β = 0.0174:
# "a 1-unit increase in roe is associated with a (approximately) 1.74% increase in salary."
#  Pipeline steps you must remember (LECESSTE)
# L oad — pd.read_csv → df.shape, df.head, df.info, df.describe
# E DA — histograms, boxplots, pairplot, correlation heatmap
# C lean — handle missing (drop / median / mode), handle outliers (IQR / clip)
# E ncode — one-hot for nominal (drop_first=True), ordinal for ordered, label for target
# S cale — StandardScaler (fit on train only)
# S plit — train_test_split (test_size=0.2, random_state=42)
# T rain — fit model(s); compare Linear / Ridge / Lasso / EN / Polynomial; tune via CV
# E valuate — R², Adjusted R², RMSE, MAE; residual plots; assumption checks
# Answer templates for common ESA prompts
# Template 1 — "Define X and explain why it is used"
# Definition: X is <one sentence>.
# Why used: It addresses <problem> by <mechanism>.
# Example: e.g. predicting house prices, X helps because...
# Caveat: X assumes / can fail when ...
# Template 2 — "Differentiate between A and B"
# Two-column comparison covering: definition · math form · effect on coefficients · feature
selection? · scaling required? · best for
# Template 3 — "Comment on this OLS summary"
# Fit quality: R² = X, Adj R² = Y → model explains X% of variance.
# Joint significance: Prob(F) = Z → at least one predictor significant.
# Significant variables: <list features with p < 0.05> with sign and rough magnitude.
# Insignificant variables: <list with p > 0.05> — candidates to drop.
# Diagnostics: DW = ?, JB p-value = ?, Cond. No. = ? — flag any concerns.
# Business read: One sentence translating the biggest coefficient into plain English.
# Template 4 — "Build a regression model end-to-end"
# 1. Load + EDA (head, info, describe, corr heatmap).
# 2. Handle missing (median for numeric, mode for categorical).
# 3. Outlier check (IQR; cap or drop).
# 4. Encode categoricals (get_dummies, drop_first=True).
# 5. Train/test split (test_size=0.2, random_state=42).
# 6. Scale (StandardScaler, fit on train).
# 7. Check VIF; drop features with VIF > 10.
# 8. Fit OLS; read summary; check assumptions via residuals + Q-Q.
# 9. Compare Linear / Ridge / Lasso / EN with 5-fold CV.
# 10. GridSearchCV to tune the chosen model's α.
# 11. Report final test R², RMSE, MAE.
# 12. Interpret top 3 coefficients in business terms.
# Template 5 — "How would you handle multicollinearity?"
# 1. Detect: pairwise correlations + VIF (> 5 warning, > 10 serious).
# 2. Diagnose: identify the offending pair / cluster.
# 3. Fix:
# Drop one of the highly-correlated pair
# Combine: average or PCA the cluster
# Use Ridge regression — handles multicollinearity gracefully
# Re-collect data if a structural duplicate exists
# 4. Verify: recompute VIF; ensure all < 5.
# Template 6 — "Detect and treat overfitting"
# Detect: training R² >> test R² (or low CV score with high variance across folds).
# Treat:
# Add regularization (Ridge / Lasso)
# Reduce model complexity (lower polynomial degree)
# Reduce feature count (Lasso, RFE, forward selection)
# Get more training data
# Use cross-validation for honest evaluation
# The night-before mantra
# LINER — five LR assumptions.
# VIF > 10 = drop ; alpha tuned by CV; scale before regularizing.
# Lasso = Less features; Ridge = Reduce sizes; ElasticNet = both.
# R² always grows; Adj R² wins for fair comparisons.
# RMSE only compares same target; otherwise use R².
# Bias = simple-wrong; Variance = bouncy.
# p < 0.05 → keep alive; DW ≈ 2 → independence true.
# Split → fit → transform. No leakage.
# LECESSTE — full pipeline order.
# Q4 = Preprocess. Q5 = OLS. Q6 = Compare + tune.
# Read this list once before sleep. Sleep 7+ hours. You're ready.
# All the best, Rajesh!
# ← Previous 20. Python Pipeline"""
SMLR - Supervised Machine Learning (Regression)
PES University M.Tech Data Science and AI - UE20CS905
Complete Study Guide - All Topics in Index Order
"""

#==============================================================================
# TOPIC 08: Multicollinearity and VIF
#==============================================================================

# What is Multicollinearity?
# Multicollinearity happens when two or more predictor features are strongly correlated with each other. Examples from the Fish dataset: Length1 , Length2 , Length3 are all measurements of the same fish in different directions — they correlate ~0.99. The model can't tell which one is "really" doing the work.
#  Why it's a problem
# Coefficients become unstable. Small changes in the data cause big swings in β values, even sign flips.
# Standard errors balloon. p-values become large; you may wrongly conclude "this feature isn't significant" when it actually is.
# Interpretation breaks. "Holding everything else constant" doesn't make sense if features always move together.
# Predictions usually still fine. Multicollinearity hurts interpretation more than prediction accuracy .
#  Perfect multicollinearity = math breaks
# If two features are exactly linearly related (e.g., one is a copy or sum of others), the matrix XᵀX cannot be inverted and the OLS formula fails outright. Real datasets rarely hit this — but watch out after dummy encoding (the "dummy variable trap" — drop one category!).
# How to detect multicollinearity
# 1. Correlation matrix
# Compute pairwise correlations between all features. Pairs with |r| > 0.8 are suspicious. Visualize with a heatmap ( seaborn.heatmap ).
# 2. Variance Inflation Factor (VIF) — the gold standard
# VIF formula
# VIF_j = 1 / (1 − R²_j)
# where R²_j is the R² obtained by regressing feature j on all other features.
# Intuition: if you can predict feature j very well from the other features (R²_j close to 1), then feature j carries no new information — pure multicollinearity. VIF spikes to infinity.
# VIF value Interpretation Action
# VIF = 1 No multicollinearity Feature is independent — keep
# 1 < VIF < 5 Mild — usually fine Keep, monitor
# 5 ≤ VIF < 10 Moderate — caution Consider dropping or combining
# VIF ≥ 10 Severe Drop one of the correlated features
# 3. Condition Number
# Reported in the statsmodels OLS summary. Cond. No. > 30 = caution; > 100 = severe multicollinearity.
#  How to fix multicollinearity
# Drop one of the correlated features. Simplest. If Length1, Length2, Length3 all correlate > 0.99, keep one (typically the most interpretable, e.g., Length3 = total length).
# Combine into a single feature. e.g., average of correlated features, or PCA on them.
# Use Ridge Regression. Ridge's L2 penalty stabilizes coefficients even under multicollinearity.
# Apply Principal Component Analysis (PCA). Transform correlated features into uncorrelated principal components.
# Increase sample size if feasible — more data → tighter estimates → less sensitivity.
# Python code — computing VIF
# from statsmodels.stats.outliers_influence import variance_inflation_factor import pandas as pd # Compute VIF for each feature in your X matrix vif_df = pd.DataFrame()
vif_df[ 'feature' ] = X.columns
vif_df[ 'VIF' ] = [variance_inflation_factor(X.values, i) for i in range(X.shape[ 1 ])] print (vif_df.sort_values( 'VIF' , ascending= False )) # Iteratively drop the feature with highest VIF until all VIFs are below 5 while True : vifs = [variance_inflation_factor(X.values, i) for i in range(X.shape[ 1 ])] max_vif = max(vifs) if max_vif < 5 : break drop_idx = vifs.index(max_vif) print ( f"Dropping {X.columns[drop_idx]} (VIF={max_vif:.2f})" ) X = X.drop(columns=[X.columns[drop_idx]])
#  Worked example: VIF calculation
# Say feature x₁ has R² = 0.9 when regressed on x₂, x₃, x₄. Then:
# VIF_x₁ = 1 / (1 − 0.9) = 1 / 0.1 = 10
# VIF = 10 means the variance of β̂_x₁ is 10× larger than it would be if x₁ were uncorrelated with the others. Severe — drop x₁ or merge it with a correlated feature.
# Exam questions on this topic

# What is Multicollinearity? How to detect the presence of multicollinearity and which variables are involved in it?
# Answer
# Multicollinearity = strong linear correlation between two or more predictor features in a regression model. It makes coefficient estimates unstable and standard errors inflated, harming interpretability.
# Detection methods:
# Correlation matrix — compute pairwise correlations between features. Pairs with |r| > 0.8 are suspicious. Use df.corr() + heatmap.
# Variance Inflation Factor (VIF) = 1 / (1 − R²_j), where R²_j is from regressing feature j on all others.
# VIF < 5 → safe
# 5 ≤ VIF < 10 → moderate; consider dropping
# VIF ≥ 10 → severe; drop one
# Condition Number from OLS summary > 30 indicates trouble.
# Tolerance = 1/VIF; values < 0.1 → severe.
# Identifying the involved variables: features with VIF ≥ 10 are the culprits. The correlation matrix tells you which pairs are most strongly tied (e.g., in Fish data, Length1, Length2, Length3 will all show high VIF together because they measure overlapping geometry).
# Fixes: drop redundant features (keep the most interpretable), combine into one (mean / first principal component), use Ridge regression (stabilizes via L2 penalty), or apply PCA.
# 4f / 4i / 4h Feb 2025 / / Mar 2024 / Nov 2024 each
# check and reduce multicollinearity using VIF.
# Answer (template code)
# from statsmodels.stats.outliers_influence import variance_inflation_factor import pandas as pd def compute_vif (X): vif = pd.DataFrame() vif[ 'feature' ] = X.columns vif[ 'VIF' ] = [variance_inflation_factor(X.values, i) for i in range(X.shape[ 1 ])] return vif.sort_values( 'VIF' , ascending= False ) # Iteratively drop highest VIF until all < 5 while compute_vif(X)[ 'VIF' ].max() > 5 : drop_feat = compute_vif(X).iloc[ 0 ][ 'feature' ] print ( f'Dropping {drop_feat}' ) X = X.drop(columns=[drop_feat]) print (compute_vif(X))
# Reasoning to write in the inference: "Length1, Length2, Length3 all measure overlapping geometry of the fish, hence high VIF. We retain Length3 (most representative) and drop Length1 and Length2. Final VIFs all below 5 — multicollinearity resolved."
# Multicollinearity in 3 lines
# What: predictors correlate with each other.
# Detect: VIF = 1/(1−R²); VIF > 5 = warning, > 10 = severe.
# Fix: drop one, combine, Ridge, or PCA.
# Multicollinearity = correlated predictors. Hurts interpretability, not always prediction.
# Detect with VIF (gold standard): VIF = 1/(1−R²_j). VIF < 5 OK, ≥ 10 fix it.
# Fix: drop, combine, Ridge, or PCA.
# The dummy variable trap (perfect multicollinearity after one-hot encoding) — always drop one category.

#==============================================================================
# TOPIC 09: Bias-Variance Tradeoff and Overfitting
#==============================================================================

# Underfitting vs Overfitting
# Bias-Variance Tradeoff
# Bias/variance from CV
# Strategies to reduce overfit
#  Underfitting and Overfitting
# Two ways a model can be bad:
# Underfitting Overfitting
# What Model too simple to capture the pattern Model too complex — fits noise as if it were signal
# Symptom on train High error Very low error
# Symptom on test High error (similar to train) Much higher error than train
# Cause Too few features, low-degree polynomial, too much regularization Too many features, high-degree polynomial, no regularization
# Fix Add features, increase model complexity, reduce regularization Reduce features, regularize (Ridge/Lasso), add data, cross-validate
# UNDERFIT (high bias) JUST RIGHT OVERFIT (high variance)
# Underfit ignores the curve. Overfit chases every data point including noise. Just right captures the underlying signal.
# The Bias-Variance Tradeoff
# Total expected error of a model can be decomposed into three parts:
# Bias-Variance Decomposition
# Expected Error = Bias² + Variance + Irreducible Error
# Term Definition Cause Reduce by
# Bias How far off the model's average prediction is from truth Model too simple — assumptions don't fit reality More features, complex model, less regularization
# Variance How much predictions jump around for different training sets Model too complex — too sensitive to specific training data Fewer features, regularization, more training data
# Irreducible Random noise inherent in y Real-world randomness, measurement error Cannot be removed
# model complexity → error bias² variance total ↑ sweet spot
# As model complexity grows, bias falls but variance rises. Total error is U-shaped — minimize at the sweet spot (green dot).
# Bias and variance from cross-validation
# The Feb/papers ask: "calculate the bias error (1 − mean R²) and variance error (standard deviation of R²) by performing 5-fold cross-validation."
# This is an operational definition (different from the statistical decomposition above):
# Operational definitions used in your paper
# Bias error = 1 − mean(R² scores across folds)
# Variance error = standard deviation of R² scores across folds
# Interpretation:
# High mean(1 − R²) → model under-explains variance → underfitting → bias issue.
# High std(R²) → model behaviour swings wildly across folds → overfitting → variance issue.
# from sklearn.model_selection import cross_val_score from sklearn.linear_model import LinearRegression import numpy as np model = LinearRegression()
scores = cross_val_score(model, X_train, y_train, cv= 5 , scoring= 'r2' ) bias_error = 1 - scores.mean() # operational bias variance_error = scores.std() # operational variance print ( f"Bias error: {bias_error:.4f}" ) print ( f"Variance error: {variance_error:.4f}" )
#  Strategies to reduce overfitting
# Regularization — add penalty for large coefficients (Ridge, Lasso, ElasticNet). See chapter 10.
# Cross-validation — pick hyperparameters that generalize, not those that memorize. See chapter 11.
# More training data — more data dilutes the impact of noise.
# Reduce model complexity — drop features, lower polynomial degree, simpler model.
# Feature selection — keep only the most useful features (Forward, RFE, Lasso). See chapter 14.
# Early stopping — for iterative models, stop training when validation error starts rising.
# Ensemble methods — bagging averages out variance (Random Forests).
# Exam questions on this topic
# How the problem of overfitting can be reduced in Linear regression? What is bias variance trade off?
# Answer
# Reducing overfitting in Linear Regression:
# Regularization — Ridge (L2 penalty), Lasso (L1 penalty), or ElasticNet shrink coefficients toward zero, reducing model variance.
# Cross-validation — k-fold CV picks hyperparameters that generalize.
# Feature selection — Forward selection, Backward elimination, RFE remove uninformative predictors.
# More training data — dilutes noise; harder to fit specific samples.
# Reduce polynomial degree if using polynomial features.
# Drop multicollinear features using VIF.
# Bias-Variance Tradeoff:
# Bias = how far model's average prediction is from truth → high when model too simple → underfitting.
# Variance = how much predictions vary across training sets → high when model too complex → overfitting.
# Tradeoff: reducing bias (add complexity) often raises variance, and vice versa.
# Total error decomposition: Error = Bias² + Variance + Irreducible Noise
# Goal: minimize total error → find the sweet spot where bias and variance are balanced.
# What strategies can be employed to mitigate overfitting in Linear Regression? Provide an explanation of various forms of Linear Regression that address the issue of overfitting.
# Answer
# Strategies to mitigate overfitting:
# Regularization (Ridge, Lasso, ElasticNet)
# Cross-validation (k-fold CV) for hyperparameter tuning
# Feature selection (Forward, Backward, RFE)
# Reducing model complexity
# Increasing training data size
# Removing multicollinearity (VIF)
# Forms of Linear Regression that address overfitting:
# Variant Penalty Effect
# Ridge (L2) α · Σβⱼ² Shrinks all coefficients toward zero (none exactly zero). Best for many small effects.
# Lasso (L1) α · Σ|βⱼ| Sets some coefficients exactly to zero → automatic feature selection.
# ElasticNet α₁·Σβⱼ² + α₂·Σ|βⱼ| Combines L1 and L2. Good when features are correlated.
# All three add a penalty to the cost function: J(β) = MSE + penalty. The hyperparameter α controls the strength — bigger α → more shrinkage → less overfitting (but more bias).
# How can you handle overfitting and underfitting?
# Answer
# To handle Overfitting (low train error, high test error):
# Use regularization (Ridge / Lasso / ElasticNet)
# Reduce model complexity (fewer features, lower polynomial degree)
# Use cross-validation
# Get more training data
# Apply feature selection / dimensionality reduction (PCA)
# Early stopping (for iterative models)
# To handle Underfitting (high train error, high test error):
# Add more features (or polynomial features)
# Use a more complex model
# Reduce regularization strength (lower α)
# Train longer / more iterations
# Improve feature engineering
#  Bias vs Variance — one liners
# Bias = systematic wrongness (model too simple).
# Variance = jumpiness (model too sensitive to data).
# Underfit = high bias, low variance. Overfit = low bias, high variance.
# Tradeoff = lowering one usually raises the other; find the U-curve minimum.
# Underfitting = too simple. Overfitting = too complex.
# Total error = Bias² + Variance + Noise.
# Operational measures from CV: bias = 1 − mean(R²), variance = std(R²).
# Fixes: regularization, CV, feature selection, more data, simpler model.

#==============================================================================
# TOPIC 10: Regularization (Ridge, Lasso, ElasticNet)
#==============================================================================

# Why regularize?
# Ridge
# Lasso
# ElasticNet
# Side-by-side
# Role of α
# Tuning α with CV
#  Why Regularization?
# Plain OLS minimizes squared residuals: J(β) = Σ(y − ŷ)² . With many features (or correlated ones), some β values can become huge — the model overfits, predictions on new data are unstable.
# Regularization adds a penalty term to the cost function that grows when β values get large. The model now has to balance: fit the data well (low residuals) and keep coefficients small (low penalty). This shrinks coefficients and reduces overfitting.
# General regularized cost function
# J(β) = Σ(yᵢ − ŷᵢ)² + α · Penalty(β)
# Three popular penalties → three regression variants: Ridge , Lasso , ElasticNet .
# Ridge Regression (L2 penalty)
# Ridge cost function
# J(β) = Σᵢ(yᵢ − ŷᵢ)² + α · Σⱼ βⱼ²
# The penalty is the sum of squared coefficients (L2 norm). Big βs cost a lot; small ones cost little.
# Effect on coefficients
# Shrinks all coefficients toward zero, but never exactly to zero .
# Stable under multicollinearity — splits the effect across correlated predictors instead of going wild on one.
# When to use Ridge
# You believe all features are at least somewhat useful .
# Multicollinearity is present.
# You want stability, not feature selection.
# Lasso Regression (L1 penalty)
# Lasso cost function
# J(β) = Σᵢ(yᵢ − ŷᵢ)² + α · Σⱼ |βⱼ|
# Penalty is the sum of absolute coefficient values (L1 norm).
# Effect on coefficients
# Shrinks coefficients toward zero, and can drive some exactly to zero . This is automatic feature selection .
# For correlated features, Lasso tends to keep one and zero out the others (sometimes arbitrarily).
# When to use Lasso
# You suspect many features are useless and want them removed.
# You want a sparse, interpretable model.
# ElasticNet (L1 + L2)
# ElasticNet cost function
# J(β) = Σᵢ(yᵢ − ŷᵢ)² + α · [ρ · Σ|βⱼ| + (1−ρ) · Σβⱼ²]
# ρ ("rho", or l1_ratio in sklearn) controls the L1/L2 mix. ρ=1 → Lasso, ρ=0 → Ridge, ρ=0.5 → equal blend.
# When to use ElasticNet
# You want feature selection (like Lasso) and stability under multicollinearity (like Ridge).
# Common with high-dimensional, correlated data (genomics, text features).
# Side-by-side comparison
# Aspect Ridge (L2) Lasso (L1) ElasticNet
# Penalty α·Σβⱼ² α·Σ|βⱼ| α·[ρ·L1 + (1-ρ)·L2]
# Sets β to 0? No Yes (some) Yes (some)
# Feature selection? No Yes (built-in) Yes
# Handles multicollinearity? Excellent Poor (picks one) Good
# Interpretable? Less (all features kept) More (sparse) Medium
# sklearn class Ridge Lasso ElasticNet
#  The role of α (lambda)
# α (sometimes written λ in textbooks) is the regularization strength. It's a hyperparameter you choose, typically via cross-validation.
# α value Effect
# α = 0 No penalty → identical to plain OLS
# α small (e.g. 0.01) Mild shrinkage; close to OLS
# α moderate (e.g. 1.0) Substantial shrinkage; strong regularization
# α very large (e.g. 1000) All coefficients ≈ 0 → severe underfitting
#  Always scale features before regularizing
# The penalty Σβⱼ² treats all coefficients equally. If your features have different scales (RAM in GB vs storage in MB), the bigger-scale features will have unfairly tiny βs and escape penalty. Always StandardScaler your X before Ridge/Lasso/ElasticNet.
# Tuning α with cross-validation
# The exam papers ask you to use Grid/Random search to tune α. Here's the template:
# from sklearn.model_selection import GridSearchCV from sklearn.linear_model import Ridge param_grid = { 'alpha' : [ 0.001 , 0.01 , 0.1 , 1 , 10 , 100 ]}
grid = GridSearchCV(Ridge(max_iter= 500 ), param_grid, cv= 5 , scoring= 'neg_root_mean_squared_error' )
grid.fit(X_train_scaled, y_train) print ( "Best alpha:" , grid.best_params_[ 'alpha' ])
y_pred = grid.predict(X_test_scaled)
rmse = np.sqrt(mean_squared_error(y_test, y_pred)) print ( "Test RMSE:" , rmse)
# Exam questions on this topic
# Write the expression for the cost function, which need to be minimized in Linear regression with RIDGE regularization.
# Answer
# J(β) = Σᵢ(yᵢ − ŷᵢ)² + α · Σⱼ βⱼ²
# Equivalently: J(β) = ||y − Xβ||²₂ + α · ||β||²₂
# The first term is the residual sum of squares (RSS); the second is the L2 penalty. α ≥ 0 is the regularization strength — when α = 0 it reduces to OLS; as α → ∞ all βs are forced to zero.
# If we increase the value of lambda, what will happen to the estimated coefficients in RIDGE model?
# Answer
# As λ (lambda) increases , the penalty for having large coefficients grows. To minimize total cost, the model is forced to shrink all coefficients toward zero :
# λ = 0: no penalty → coefficients = OLS estimates.
# λ small: mild shrinkage; coefficients close to OLS but slightly smaller in magnitude.
# λ large: all coefficients shrink substantially. Bias increases, variance decreases.
# λ → ∞: all coefficients → 0. The model predicts only the mean of y → severe underfitting.
# Important: Ridge shrinks coefficients but never sets them exactly to zero . (For exact-zero behaviour, use Lasso instead.) Picking the right λ is a bias-variance tradeoff — typically tuned via cross-validation.
# What is regularization in linear regression? Compare and contrast Lasso and Ridge regression in terms of mathematical formulation, impact on coefficients, and use cases.
# Answer
# Regularization = adding a penalty term to the OLS cost function to discourage large coefficients. This reduces overfitting and improves model generalization, especially when features are many or multicollinear.
# Aspect Ridge (L2) Lasso (L1)
# Cost function RSS + α·Σβⱼ² RSS + α·Σ|βⱼ|
# Penalty type Squared coefficients Absolute coefficients
# Solution Closed-form: β̂ = (XᵀX + αI)⁻¹ Xᵀy No closed form; coordinate descent
# Impact on coefs Shrinks all βs toward 0; never exactly 0 Shrinks and sets some βs exactly to 0
# Feature selection? No Yes (sparse solution)
# Multicollinearity Handles well — distributes effect Picks one feature, zeros others (arbitrary)
# Use case All features moderately useful; multicollinearity present Few features actually useful; sparse interpretable model needed
# Common ground: both add a penalty controlled by α; both reduce variance at the cost of slightly higher bias; both require feature scaling beforehand.
# What role does regularization play in improving Linear Regression models?
# Answer
# Regularization plays multiple roles:
# Reduces overfitting — by penalizing large coefficients, the model becomes simpler and generalizes better to unseen data.
# Stabilizes coefficients under multicollinearity — Ridge in particular handles correlated predictors gracefully.
# Performs feature selection — Lasso (and ElasticNet) drive uninformative coefficients to exactly zero, automatically removing them from the model.
# Improves test-set performance — by trading a small amount of bias for a large reduction in variance.
# Enables modeling with p > n — when there are more features than observations, OLS can't run; regularization makes the problem solvable.
# Improves interpretability — sparse models (from Lasso) are easier to explain.
# The strength is controlled by α, tuned via cross-validation. The 3 main forms are Ridge (L2), Lasso (L1), and ElasticNet (L1+L2 blend).
# The 3 Rs: Ridge, Restraint, Removal
# Ridge uses squared β (L 2 ) — R educes everyone equally.
# Lasso uses absolute β (L 1 ) — L obs uninformative features off entirely.
# ElasticNet mixes both — best of both worlds.
# Regularization = penalty added to cost function to fight overfitting.
# Ridge (L2): shrinks all βs, never zero; great for multicollinearity.
# Lasso (L1): can zero out βs; built-in feature selection.
# ElasticNet: blends L1+L2; balances stability and sparsity.
# α controls strength; tune with cross-validation.
# Always scale features before regularizing.

#==============================================================================
# TOPIC 11: Cross-Validation
#==============================================================================

# Why CV?
# k-Fold procedure
# Bias/Variance from CV
# Other CV variants
# Memory aid
# Why Cross-Validation?
# A single train/test split has a problem: the test-set score depends on which 20% of the data happened to land in the test set. With unlucky luck, your model might look great or terrible just because of the split.
# Cross-validation (CV) averages performance across multiple splits, giving you a more reliable estimate of how the model will generalize.
# k-Fold Cross-Validation — the standard recipe
# Shuffle the training data.
# Split it into k equal-sized chunks ("folds"). Common: k = 5 or k = 10.
# For each fold i (1 to k):
# Treat fold i as the validation set.
# Train the model on the other k-1 folds.
# Score it on fold i.
# Average the k scores → that's your CV score.
# 5-Fold Cross-Validation Fold 1 → score₁ Fold 2 → score₂ Fold 3 → score₃ Fold 4 → score₄ Fold 5 → score₅ Train Validation CV Score = mean(score₁, …, score₅)
# Each fold takes a turn as the validation set. The model is trained 5 separate times. Average the 5 scores.
#  Bias error and Variance error from CV
# The Feb/ + + Nov 2024 papers ask for these operational definitions:
# Operational definitions
# Bias error = 1 − mean(R² across folds)
# Variance error = standard deviation of R² across folds
# Interpretation
# Combination Diagnosis
# Low bias error, low variance error Excellent — well-fit, stable model
# High bias error, low variance error Underfitting — model is consistent but bad
# Low bias error, high variance error Overfitting — performance depends on which fold
# High bias error, high variance error Bad model — both poor and unstable
# from sklearn.model_selection import KFold, cross_val_score, cross_validate from sklearn.linear_model import LinearRegression import numpy as np # Quick way: cross_val_score model = LinearRegression()
r2_scores = cross_val_score(model, X_train, y_train, cv= 5 , scoring= 'r2' ) print ( f"R² per fold: {r2_scores}" ) print ( f"Mean R²: {r2_scores.mean():.4f}" ) print ( f"Bias error (1 - mean R²): {1 - r2_scores.mean():.4f}" ) print ( f"Variance error (std R²): {r2_scores.std():.4f}" ) # If you want RMSE per fold instead of R² neg_mse = cross_val_score(model, X_train, y_train, cv= 5 , scoring= 'neg_mean_squared_error' )
rmse_per_fold = np.sqrt(-neg_mse) print ( f"RMSE per fold: {rmse_per_fold}" )
# Other CV variants
# Variant What it does When to use
# k-Fold (k=5 or 10) Standard k splits General purpose; default choice
# Stratified k-Fold Preserves class balance per fold Classification with imbalanced classes
# Leave-One-Out (LOOCV) k = n; each sample is its own fold Very small datasets; extremely expensive
# Time-Series Split Train always precedes test in time Time-series data — never shuffle the time axis
# Shuffle Split Random repeated train/val splits When you want more iterations than k allows
# Exam questions on this topic

# Explain the procedure involved in k-fold cross validation.
# Answer
# k-Fold Cross-Validation is a model-validation technique that gives a more reliable estimate of test performance than a single train/test split.
# Procedure:
# Shuffle the training data randomly (unless time-ordered).
# Split the data into k equal-sized parts called folds. Common values: k = 5 or k = 10.
# For each fold i = 1 to k:
# Treat fold i as the validation set.
# Combine the remaining k-1 folds into a training set.
# Train the model on the training folds.
# Evaluate it on fold i — record the score (e.g., R² or RMSE).
# After all k iterations, you have k scores. Compute the mean of the scores → that's the CV estimate of model performance.
# Optionally compute the standard deviation → measures stability across folds.
# Why it's better than a single split:
# Every observation gets used for both training and validation (each one exactly once for validation).
# The averaged score has lower variance than a single split's score.
# You get a sense of model stability via the std-dev of fold scores.
# Tradeoffs: CV is k× more computationally expensive than a single fit. Larger k → less bias, more variance, more cost.
# Memory aid
# 5-fold CV in 5 words
# "Split, rotate, score, average, report."
# CV averages performance across multiple train/val splits → more reliable than one split.
# k-fold CV: split into k chunks, each takes a turn as validation, average k scores.
# Common: k = 5 (default in your papers); k = 10 for more reliable estimates.
# Operational measures: bias error = 1 − mean(R²) , variance error = std(R²) .
# Use Stratified k-Fold for imbalanced classification; TimeSeriesSplit for time data.

#==============================================================================
# TOPIC 12: Evaluation Metrics
#==============================================================================

# Why multiple metrics?
# R²
# Adjusted R²
# RMSE
# MAE
# MAPE
# Comparison table
# Why we need multiple metrics
# "How good is my model?" is a question with several valid answers depending on what you care about: variance explained, average error size, big-error sensitivity, percentage error. Each metric tells a different story.
# R² — the coefficient of determination
# R-squared
# R² = 1 − (SS_res / SS_tot)
# SS_res = Σᵢ(yᵢ − ŷᵢ)² SS_tot = Σᵢ(yᵢ − ȳ)²
# Term Meaning
# SS_res Residual sum of squares — how badly the model fits
# SS_tot Total variance in y — how spread out y is around its mean
# R² Fraction of variance the model explains. Closer to 1 = better.
# R² value Interpretation
# R² = 1 Model explains 100% of variance — perfect predictions
# R² = 0 Model is no better than predicting the mean of y
# R² < 0 Model is worse than predicting the mean (yes, possible on test set)
# R² ≈ 0.7 Decent — explains ~70% of variance; common in real data
#  The trap with R²
# R² always increases (or stays the same) when you add features , even useless ones. So "higher R² = better model" only works if you compare models with the same number of features.
# Adjusted R² — fair comparison across feature counts
# Adjusted R²
# Adj R² = 1 − (1 − R²) · [(n − 1) / (n − k − 1)]
# n = number of samples, k = number of predictors (features)
# Adjusted R² penalizes models with more features. Useless features hurt Adj R² but not R². So Adj R² goes up when added features genuinely help, and goes down when they don't.
# R² vs Adj R²
# Use R² — when reporting variance explained on a single model.
# Use Adj R² — when comparing models with different numbers of features.
# Big gap (R² much higher than Adj R²) → too many useless features.
# RMSE — Root Mean Squared Error
# RMSE = √[(1/n) · Σᵢ(yᵢ − ŷᵢ)²]
# "Average size of prediction error, in the same units as y." If you predicted house prices and RMSE = 5L, then on average you're off by about 5L. Large errors hurt more due to squaring.
# MAE — Mean Absolute Error
# MAE = (1/n) · Σᵢ |yᵢ − ŷᵢ|
# Same units as y. Treats all errors equally (no squaring). More robust to outliers than RMSE.
# MAPE — Mean Absolute Percentage Error
# MAPE = (100/n) · Σᵢ |yᵢ − ŷᵢ| / |yᵢ|
# Average percentage error. Same percentage scale across different problems — a MAPE of 8% means "off by 8% on average."
#  MAPE pitfall
# MAPE blows up when any yᵢ is close to 0. Don't use MAPE if your target can be near zero.
# Comparing the metrics
# Metric Range Units Outlier-sensitive? Best when
# R² (−∞, 1] Unitless Yes Reporting variance explained
# Adj R² (−∞, 1] Unitless Yes Comparing models with different feature counts
# RMSE [0, ∞) Same as y Yes (squared) You care about big errors
# MSE [0, ∞) y² Yes (squared) Internal optimization (training)
# MAE [0, ∞) Same as y Less Robust to outliers; equal weight to all errors
# MAPE [0, ∞) % Less Comparing across scales; y >> 0
# from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error import numpy as np y_pred = model.predict(X_test) r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred) * 100 # sklearn returns fraction # Adjusted R² — sklearn doesn't have it, but it's a one-liner n = len(y_test)
k = X_test.shape[ 1 ]
adj_r2 = 1 - ( 1 - r2) * (n - 1 ) / (n - k - 1 ) print ( f"R²: {r2:.4f}" ) print ( f"AdjR²: {adj_r2:.4f}" ) print ( f"RMSE: {rmse:.2f}" ) print ( f"MAE: {mae:.2f}" ) print ( f"MAPE: {mape:.2f}%" )
# Exam questions on this topic
# What is the difference between R² and Adjusted R², and when should each be used?
# Answer
# R² = fraction of variance in y explained by the model. Formula:
# R² = 1 − SS_res / SS_tot
# Adjusted R² = R² penalized for the number of features:
# Adj R² = 1 − (1 − R²) · (n − 1) / (n − k − 1)
# Aspect R² Adjusted R²
# Behaviour when adding any feature Always ↑ or stays same ↑ only if feature genuinely helps; else ↓
# Range (−∞, 1] Can be lower than R²
# Penalizes model complexity? No Yes (penalizes k)
# When to use which:
# R² — for a single model, or to report variance explained.
# Adjusted R² — when comparing models with different numbers of features ; for feature selection.
# Diagnostic: if R² is much higher than Adj R², your model has redundant or useless features.
# How adjusted R-square is differing from R-square? Brief the role of adjusted R-square in feature selection process.
# Answer
# Difference:
# R² always increases (or stays the same) when you add a feature, regardless of whether the feature is useful.
# Adjusted R² = 1 − (1 − R²)·(n−1)/(n−k−1) accounts for the number of predictors k. It increases only when a new feature improves the model more than expected by chance ; otherwise it decreases.
# Role in feature selection:
# When comparing two models with different feature counts, Adjusted R² gives a fair comparison — R² alone would always favour the bigger model.
# Used in stepwise selection (forward / backward): at each step, a candidate feature is added/removed only if Adj R² improves.
# If adding a feature drops Adj R², the feature is rejected as not contributing genuine information.
# Helps prevent overfitting that would result from blindly adding features to chase higher R².
# 1c · Mobile-phone sales numerical
# A linear regression model is build with three independent variable price, advertisement cost and promotion cost to predict unit sales of mobile phone. Say the p value for the t-test of the variable 'advertisement cost' is 0.02. What is your inference on this?
# Answer
# p-value = 0.02 → reject H₀ at the 5% significance level.
# Hypothesis setup for the t-test on β_advertisement:
# H₀: β_advertisement = 0 (advertisement cost has no effect on sales)
# H₁: β_advertisement ≠ 0 (advertisement cost has a significant effect)
# The p-value 0.02 is the probability of observing a coefficient at least as extreme as the one we got, if H₀ were true . Since 0.02 < 0.05 (the conventional 5% significance threshold):
# We reject H₀ .
# The coefficient on advertisement cost is statistically significant .
# Inference: advertisement cost is a meaningful predictor of mobile phone sales — keep this feature in the model.
# (At the 1% level, p = 0.02 would not be significant since 0.02 > 0.01. So conclude: significant at 5% but not at 1%.)
# 1d · RMSE comparison numerical
# The RMSE of the regression model which predicting the CTC salary is 12324 and the RMSE of the other regression model which predicting the age of the person is 55. Comment on the performance of these two models. [output column is not scaled or transformed]
# Answer
# You cannot compare these RMSE values directly. RMSE has the same units as y, and the two ys are on completely different scales:
# CTC salary is typically in lakhs of rupees — values commonly between 100,000 and 5,000,000+. An RMSE of 12,324 is roughly 12K — a tiny error in this context.
# Age is in years — values between roughly 18 and 80. An RMSE of 55 years is enormous — bigger than the entire reasonable range of ages.
# To compare fairly, use a scale-free metric such as:
# Relative RMSE (% RMSE) = RMSE / mean(y) × 100. If average salary ≈ 500,000, then %RMSE ≈ 12,324/500,000 × 100 ≈ 2.5% — excellent. If average age ≈ 35, then %RMSE ≈ 55/35 × 100 ≈ 157% — disastrous.
# R² — measures variance explained, unit-less, comparable across models.
# MAPE — already a percentage; directly comparable.
# Inference: the salary model is performing well (low relative error). The age model is failing badly — RMSE is larger than the entire range of plausible ages, suggesting the model is essentially useless. Always interpret RMSE relative to the scale of y.
# Metric one-liners
# R² → "variance explained" (closer to 1 = better)
# Adj R² → "R² minus the bullshit features" — comparable across feature counts
# RMSE → "average mistake size in original units" — outlier-aware
# MAE → "average absolute mistake" — outlier-tough
# MAPE → "average percentage off" — comparable across scales
# R² = fraction of variance explained. Range (−∞, 1]; 1 = perfect.
# Adj R² penalizes for number of features → use when comparing models.
# RMSE = average error size in y's units; sensitive to outliers (squared).
# MAE = average absolute error; robust to outliers.
# MAPE = average percentage error; only valid if y is well above zero.
# Never compare RMSE across different ys — use scale-free metrics (R², MAPE).

#==============================================================================
# TOPIC 13: Model Diagnostics
#==============================================================================

# Why diagnose?
# 4 residual plots
# Statistical tests
# Exam template answer
# Why diagnose your model?
# A high R² doesn't guarantee a good model. The OLS assumptions (chapter 7) might be silently violated, making your p-values lies and your predictions unreliable. Diagnostics are the visual + statistical checks that tell you which assumption is broken and where to look.
# The Section C question 5b in nearly every paper says: "Check assumptions of linear regression. Write your inferences." — these diagnostics are exactly what you need.
# The 4 residual plots you must know
# 1. Residuals vs Fitted plot
# What it shows: residuals (yᵢ − ŷᵢ) on the y-axis, fitted values ŷᵢ on the x-axis.
# What you want: a random horizontal cloud around zero, with no pattern.
# Detects: Linearity (curve = non-linear) and Homoscedasticity (fan = heteroscedastic).
# 2. Q-Q (Quantile-Quantile) Plot
# What it shows: quantiles of standardized residuals (y-axis) vs quantiles of a normal distribution (x-axis).
# What you want: points hugging the diagonal y=x line.
# Detects: Normality of errors.
# Reading the deviations:
# Points form a straight line on the diagonal → normal
# S-shape (curves above-then-below or below-then-above) → heavy tails (more outliers than normal)
# Points curving up at the top, down at the bottom → light tails
# Skewed shape → distribution isn't symmetric
# 3. Scale-Location plot (a.k.a. Spread-Location)
# What it shows: √|standardized residuals| vs fitted values.
# What you want: a horizontal line with random scatter.
# Detects: Homoscedasticity. A rising line means variance increases with prediction.
# 4. Residuals vs Leverage plot
# What it shows: standardized residuals vs leverage (how unusual the X values are).
# What you want: no point in the top-right or bottom-right corner with high Cook's distance.
# Detects: Influential points — single observations that disproportionately tilt the model.
# Residuals vs Fitted Q-Q Plot Scale-Location Residuals vs Leverage outlier
# The four diagnostic plots. Top-left: random scatter = linearity & homoscedasticity OK. Top-middle: points on diagonal = normal residuals. Top-right: flat line = constant variance. Bottom: lone point in corner = influential outlier.
# Statistical tests for assumptions
# Assumption Test Null hypothesis Reject if
# Normality of residuals Shapiro-Wilk Residuals are normal p < 0.05 → not normal
# Normality of residuals Jarque-Bera Residuals are normal (skew & kurt = normal) p < 0.05 → not normal
# Homoscedasticity Breusch-Pagan Variance is constant p < 0.05 → heteroscedastic
# Homoscedasticity White test Variance is constant p < 0.05 → heteroscedastic
# Independence (autocorr.) Durbin-Watson No autocorrelation Statistic far from 2.0
# Linearity Rainbow test Relationship is linear p < 0.05 → non-linear
# Multicollinearity VIF (Not a hypothesis test) VIF > 5–10 → problematic
# import matplotlib.pyplot as plt import statsmodels.api as sm import scipy.stats as stats from statsmodels.stats.diagnostic import het_breuschpagan from statsmodels.stats.stattools import durbin_watson # Suppose you've already fit: ols_model = sm.OLS(y_train, X_const).fit() residuals = ols_model.resid
fitted = ols_model.fittedvalues # 1. Residuals vs Fitted plot plt.figure(figsize=( 10 , 8 ))
plt.subplot( 2 , 2 , 1 )
plt.scatter(fitted, residuals, alpha= 0.5 )
plt.axhline( 0 , color= 'red' , linestyle= '--' )
plt.xlabel( 'Fitted' ); plt.ylabel( 'Residuals' )
plt.title( 'Residuals vs Fitted' ) # 2. Q-Q plot plt.subplot( 2 , 2 , 2 )
sm.qqplot(residuals, line= '45' , ax=plt.gca())
plt.title( 'Normal Q-Q Plot' ) # 3. Histogram of residuals plt.subplot( 2 , 2 , 3 )
plt.hist(residuals, bins= 30 , edgecolor= 'black' )
plt.xlabel( 'Residual' ); plt.title( 'Residual distribution' ) # 4. Statistical tests shapiro_stat, shapiro_p = stats.shapiro(residuals)
bp_stat, bp_p, _, _ = het_breuschpagan(residuals, X_const)
dw = durbin_watson(residuals) print ( f"Shapiro-Wilk normality: p={shapiro_p:.4f}" ) print ( f"Breusch-Pagan homoscedast.: p={bp_p:.4f}" ) print ( f"Durbin-Watson autocorr.: {dw:.3f}" )
plt.tight_layout(); plt.show()
# Exam guidance — what to write for "Check assumptions"
# Template inference (Section C 5b)
# For each assumption, write ONE sentence with: (a) the test/plot used, (b) the result, (c) the conclusion. Example:
# Linearity — Residuals vs Fitted plot shows random scatter around 0; no clear pattern. Linearity holds.
# Independence — Durbin-Watson statistic = 1.92, close to 2.0. No autocorrelation.
# Normality — Q-Q plot points fall on the diagonal; Shapiro-Wilk p = 0.18 (> 0.05). Residuals approximately normal.
# Homoscedasticity — Breusch-Pagan p = 0.08 (> 0.05); residuals show constant spread. Homoscedastic.
# No multicollinearity — All VIFs < 5 after dropping Length1 and Length2. Multicollinearity resolved.
# If any test fails, suggest the fix (log-transform y, polynomial features, drop feature, etc.).
# Four residual plots: Residuals-vs-Fitted, Q-Q, Scale-Location, Residuals-vs-Leverage.
# Statistical tests: Shapiro-Wilk (normality), Breusch-Pagan (homoscedasticity), Durbin-Watson (autocorrelation).
# For Section C 5b answers: 5 assumptions × (test + result + conclusion) = full marks.

#==============================================================================
# TOPIC 14: Feature Engineering and Selection
#==============================================================================

# Engineering vs Selection
# Engineering techniques
# Selection methods
# Feature Engineering vs Feature Selection
# Term Goal Examples
# Feature Engineering Create new, more informative features log-transform, polynomial features, interaction terms, datetime parts
# Feature Selection Pick the most useful features from existing ones Forward selection, RFE, Lasso, VIF-based dropping
#  Feature Engineering techniques
# 1. Log Transformation
# Use when: y or a feature is right-skewed (lots of small values, few huge ones — common in prices, salaries, counts).
# Effect: compresses the range, makes the distribution more symmetric / closer to normal, often makes a non-linear relationship more linear.
# df[ 'log_price' ] = np.log1p(df[ 'price' ]) # log(1+x) handles zeros
# 2. Box-Cox / Yeo-Johnson Transformation
# Generalization of log: tries to find the best power transformation. Box-Cox needs y > 0; Yeo-Johnson works for any y.
# from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer(method= 'yeo-johnson' )
X_transformed = pt.fit_transform(X)
# 3. Polynomial Features & Interactions
# Add x², x·z, x³ etc. to capture non-linear and interaction effects.
# from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree= 2 , interaction_only= False )
X_poly = poly.fit_transform(X)
# 4. Binning / Discretization
# Convert a continuous feature into bins (e.g., age → "young/middle/senior"). Useful when relationship is non-monotonic.
# 5. Datetime feature extraction
# From a single datetime column, extract: year, month, day, day-of-week, hour, is_weekend, days_since_event. Hugely useful for time-aware predictions (e.g., metro traffic in Nov 2021 paper).
#  Feature Selection methods
# Method family Examples How it picks features
# Filter methods Correlation, VIF, mutual information, ANOVA F-test Score features in isolation; doesn't use the model
# Wrapper methods Forward, Backward, Recursive Feature Elimination (RFE) Try subsets, score with the actual model
# Embedded methods Lasso, ElasticNet, Tree feature importance Selection happens during model training
# Forward Selection (Wrapper)
# Start with no features.
# For each remaining feature, fit a model with the current set + that feature; record the score (R², Adj R², or AIC).
# Add the single feature that improved the score the most.
# Stop when no further addition improves the score.
# Backward Elimination (Wrapper)
# Start with all features.
# Fit the model. Find the feature with the highest p-value (or smallest contribution).
# Remove that feature if its p-value > 0.05 (or threshold).
# Repeat until all remaining features are significant.
# Recursive Feature Elimination (RFE)
# Train a model with all features.
# Rank features by importance (e.g., absolute coefficient size or feature_importance_).
# Remove the least important feature.
# Repeat until a target number of features remains.
# from sklearn.feature_selection import RFE from sklearn.linear_model import LinearRegression
selector = RFE(LinearRegression(), n_features_to_select= 5 )
selector.fit(X_train, y_train)
selected = X.columns[selector.support_] print ( "Selected features:" , list(selected))
# SequentialFeatureSelector (mlxtend / sklearn)
# from mlxtend.feature_selection import SequentialFeatureSelector
sfs = SequentialFeatureSelector(LinearRegression(), k_features= 'best' , forward= False , # False = backward elimination scoring= 'r2' , cv= 5 )
sfs.fit(X_train, y_train) print ( "Best features:" , sfs.k_feature_names_)
# Exam questions on this topic

# Explain the procedure involved in Forward Feature Selection.
# Answer
# Forward Feature Selection is a stepwise (wrapper) feature-selection technique that starts with no features and adds one at a time, picking the most useful at each step.
# Procedure:
# Start with an empty feature set .
# For each candidate feature not yet in the model:
# Fit the regression model using {current set} + {candidate}.
# Record the score (R² / Adjusted R² / AIC / cross-validation score).
# Add the candidate that improved the score the most to the model.
# Repeat steps 2-3 until either: (a) no remaining candidate improves the score, or (b) you reach a desired number of features, or (c) all features are added.
# The final feature set is the chosen subset.
# Pros: simple, interpretable, gives a small model.
# Cons: greedy — can miss feature combinations that only help when chosen together; computationally expensive when k is large.
# What are Wrapper Methods in feature selection, and how are they applied in Linear Regression?
# Answer
# Wrapper methods are feature selection techniques that "wrap around" a learning algorithm — they evaluate feature subsets by training the actual model and measuring its performance, choosing the subset that gives the best score.
# Three main wrapper methods:
# Forward Selection — start empty, add the most-useful feature one at a time.
# Backward Elimination — start with all features, drop the least-significant one at a time.
# Recursive Feature Elimination (RFE) — start with all, repeatedly drop the lowest-ranked feature based on coefficient importance.
# Applied to Linear Regression:
# Use the linear model (e.g., LinearRegression ) as the base estimator.
# Score subsets via Adjusted R², AIC/BIC, or cross-validated RMSE.
# Implementations: SequentialFeatureSelector from mlxtend or sklearn; RFE / RFECV from sklearn.
# Pros: often find better subsets than filter methods; capture feature interactions in the model context.
# Cons: computationally expensive (model fit per subset); risk of overfitting to validation set.
# What is Recursive Feature Elimination (RFE)? Explain how it works, its advantages and limitations, and how it can be used to improve model performance in linear regression.
# Answer
# RFE is a wrapper feature-selection method that ranks features by importance and removes them one at a time (or in batches) using the trained model itself.
# How it works:
# Train the linear regression model with all features.
# Rank features by importance — typically the absolute value of the coefficients (or coefficients on standardized features).
# Remove the feature with the lowest rank.
# Re-train the model on the remaining features.
# Repeat steps 2–4 until you reach the target number of features (or use RFECV to let CV pick the optimal count).
# Advantages:
# Considers multivariate feature importance (uses the actual model's coefficients).
# Often outperforms simple filter methods.
# Can be combined with cross-validation (RFECV) to auto-pick the best feature count.
# Limitations:
# Computationally expensive — fits the model many times.
# Sensitive to feature scaling — must standardize before applying with linear models.
# Coefficient-based ranking unreliable when features are highly correlated.
# Greedy — doesn't explore all subsets.
# How it improves linear regression: reduces overfitting, eliminates noise features, makes the model more interpretable, and often gives better test-set performance.
# Discuss the need for data transformations in a linear regression model. Also write about various techniques employed.
# Answer
# Why data transformations are needed:
# Fix non-linearity — straighten curved relationships so a linear model fits well.
# Reduce skewness — bring features/target closer to normal distribution.
# Stabilize variance — fix heteroscedasticity (residual variance varying with ŷ).
# Bring features to comparable scales — required for regularization and for fair coefficient comparison.
# Handle outliers — log/sqrt compress extreme values without dropping them.
# Improve normality of residuals — makes p-values reliable.
# Techniques:
# Technique Use case
# Log / log1p Right-skewed positive data (prices, salaries, counts)
# Square root / Cube root Mildly skewed positive data
# Box-Cox Auto-pick best power transformation; needs y > 0
# Yeo-Johnson Generalisation of Box-Cox for any y
# Reciprocal (1/x) Heavy right tail
# StandardScaler (x − μ) / σ — for distance-based or regularized models
# MinMaxScaler (x − min) / (max − min) → [0, 1]
# RobustScaler (x − median) / IQR — outlier-robust
# Polynomial features Capture x², x³, x·z relationships
# Encoding (label, one-hot) Convert categorical features to numeric
# Binning Convert continuous to categorical when relationship is non-monotonic
# Engineering creates new features. Selection picks the best of existing ones.
# Filter methods score features alone; Wrapper methods use the model; Embedded methods (Lasso) do both.
# Forward / Backward / RFE are the three core wrapper methods.
# Always scale features before RFE with linear models.

#==============================================================================
# TOPIC 15: Data Preprocessing
#==============================================================================

# Why preprocess?
# Missing Values
# Outliers
# Encoding
# Scaling
# Train-Test Split
# Why preprocess data?
# Real datasets are messy. They have missing values, outliers, mixed types, wrong scales, text categories. Models can't directly digest any of that. Preprocessing is the cleanup step that gets your data into a model-friendly state.
# Section B Q4 of nearly every ML-1 paper is dedicated to this — typically worth 25 marks . The five subtasks recur identically across papers: missing values, outliers, encoding, scaling, splitting .
# 1. Missing Values
# Detect
# df.isnull().sum() # count of NaNs per column df.isnull().sum() / len(df) * 100 # % missing per column import seaborn as sns
sns.heatmap(df.isnull(), cbar= False ) # visual map of NaNs
# Treat
# Strategy When to use Code
# Drop rows Few rows have NaN; data is plentiful df.dropna()
# Drop column Column is > 50% missing df.drop(columns=['col'])
# Fill with mean Numeric, roughly normal distribution df['col'].fillna(df['col'].mean())
# Fill with median Numeric, skewed or has outliers df['col'].fillna(df['col'].median())
# Fill with mode Categorical features df['col'].fillna(df['col'].mode()[0])
# Forward / backward fill Time-series data df.ffill() / df.bfill()
# Constant value "missing" itself is meaningful df.fillna('missing') or df.fillna(0)
# KNN imputation Missing-at-random patterns sklearn.impute.KNNImputer()
# Iterative imputer Multivariate dependencies sklearn.impute.IterativeImputer()
# 2. Outliers
# Detect
# Visual: boxplot — points outside the whiskers; histogram with extreme tails; scatter plot vs y.
# Statistical:
# IQR method: Q1 − 1.5·IQR < outlier > Q3 + 1.5·IQR (where IQR = Q3 − Q1).
# Z-score method: |z| > 3 → outlier.
# Treat (in order of preference)
# Investigate first. Are they real values or data-entry errors?
# Cap (winsorize) — clip values to the IQR boundary or a percentile (e.g., 1st-99th).
# Transform — log or square-root often pulls outliers in.
# Drop — only when you're sure they're errors. Used by every Section B Q4 in your papers ("treat with dropping").
# Use a robust model — Huber regression, RANSAC.
# # IQR-based dropping (the standard exam approach) Q1 = df[ 'col' ].quantile( 0.25 )
Q3 = df[ 'col' ].quantile( 0.75 )
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df = df[(df[ 'col' ] >= lower) & (df[ 'col' ] <= upper)]
# 3. Encoding categorical features
# Method How it works Pros Cons
# Label Encoding Map categories to integers (0, 1, 2, …) Compact; one column Implies ordering — wrong for nominal data!
# One-Hot Encoding One binary column per category No false ordering Many columns if high cardinality
# Dummy Encoding (n−1) Like one-hot but drop one column Avoids dummy variable trap One category becomes the "reference"
# Ordinal Encoding Map to integers in a meaningful order Captures real ordering Need to specify the order
# Target Encoding Replace category with mean(y) for that category Captures relationship to y Risk of leakage; needs CV
#  The Dummy Variable Trap
# If you have a categorical feature with k categories and create k one-hot columns, the columns sum to 1 — perfectly collinear with the intercept. OLS fails. Always drop one category (use n-1 dummies) or use drop_first=True in pandas.
# Code
# # Label encoding (use only for ordinal categories) from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df[ 'gender_encoded' ] = le.fit_transform(df[ 'gender' ]) # One-hot encoding (n columns) df_encoded = pd.get_dummies(df, columns=[ 'category' ], drop_first= False ) # n-1 dummy encoding (avoids the trap) — used in Feb 2025, Mar 2024, Nov 2024 df_encoded = pd.get_dummies(df, columns=[ 'category' ], drop_first= True )
# 4. Feature Scaling
# Scaler Formula Output range Use when
# StandardScaler (x − μ) / σ Mean 0, Std 1 Default; data roughly normal; required before regularization
# MinMaxScaler (x − min) / (max − min) [0, 1] You need a bounded range (e.g., neural nets)
# RobustScaler (x − median) / IQR Centered around 0 Data has outliers
# MaxAbsScaler x / max(|x|) [−1, 1] Sparse data
#  The cardinal scaling rule
# fit on training data only. Then transform both train and test using the same scaler — never re-fit on test data. Fitting on full data leaks test info into training.
# from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) # learn μ, σ from train X_test_scaled = scaler.transform(X_test) # apply same μ, σ to test
# 5. Train-Test Split
# from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size= 0.2 , # 80:20 (Feb 2025, Mar 2024, Nov 2024); use 0.3 for 70:30 random_state= 42 # for reproducibility )
# Exam questions on this topic
# Explain any two of the data preprocessing steps.
# Answer (pick any two)
# 1. Handling missing values — replace NaNs with mean (numeric), median (skewed numeric), or mode (categorical); or drop rows/columns when too many are missing. Visualize first with df.isnull().sum() or a heatmap. Choice depends on % missing and the distribution.
# 2. Encoding categorical features — convert text categories to numeric so the model can use them. Use Label Encoding for ordinal data (e.g., 'low/medium/high' → 0/1/2) and One-Hot or n-1 Dummy Encoding for nominal data (e.g., 'red'/'green'/'blue' → three or two binary columns). Always drop one category to avoid the dummy variable trap.
# 3. Outlier treatment — detect via boxplots, IQR rule (1.5×IQR boundary), or Z-scores (|z| > 3). Treat by capping (winsorize), dropping, or log-transformation. Outliers can dominate OLS regression if untreated.
# 4. Feature scaling — bring features to comparable magnitudes. Use StandardScaler (mean 0, std 1) for most cases; MinMaxScaler for [0,1] range; RobustScaler when outliers exist. Required before regularization (Ridge/Lasso) and most distance-based algorithms.
# Five core preprocessing steps: missing values, outliers, encoding, scaling, splitting.
# Section B Q4 of every paper tests these — worth ~25 marks.
# Always fit scalers/encoders on training data only; transform test using the fitted version.
# Use n-1 dummy encoding to avoid the dummy variable trap.

#==============================================================================
# TOPIC 16: Hyperparameter Tuning
#==============================================================================

# Parameters vs Hyperparameters
# Grid Search
# Random Search
# Bayesian Optimization
# Comparison
#  Parameters vs Hyperparameters
# Parameters Hyperparameters
# Learned from data during training Set by you before training
# Examples: β₀, β₁, …, βₖ in linear regression Examples: alpha in Ridge, l1_ratio in ElasticNet, k in k-fold CV, max_iter
# Found via OLS or gradient descent Found via Grid Search, Random Search, Bayesian Optimization
# Grid Search
# Try every combination of hyperparameters from a predefined list. Pick the one that gives the best cross-validation score.
# from sklearn.model_selection import GridSearchCV from sklearn.linear_model import Ridge param_grid = { 'alpha' : [ 0.001 , 0.01 , 0.1 , 1 , 10 , 100 ]}
grid = GridSearchCV(Ridge(max_iter= 500 ), param_grid, cv= 5 , # 5-fold CV scoring= 'neg_root_mean_squared_error' , n_jobs=- 1 ) # parallel across cores grid.fit(X_train_scaled, y_train) print ( f"Best alpha: {grid.best_params_['alpha']}" ) print ( f"Best CV score: {-grid.best_score_:.3f}" )
y_pred = grid.predict(X_test_scaled)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred)) print ( f"Test RMSE: {test_rmse:.3f}" )
# Pros: exhaustive — guaranteed to find the best in your grid.
# Cons: exponential cost. With 4 hyperparameters of 5 values each = 5⁴ = 625 fits × 5 folds = 3,125 model trainings. Slow.
# Random Search
# Sample random combinations from a distribution. Often finds nearly-best results in a fraction of the time.
# from sklearn.model_selection import RandomizedSearchCV from scipy.stats import loguniform param_dist = { 'alpha' : loguniform( 0.001 , 100 )}
rnd = RandomizedSearchCV(Lasso(max_iter= 500 ), param_dist, n_iter= 20 , # try 20 random alphas cv= 5 , scoring= 'neg_root_mean_squared_error' , random_state= 42 )
rnd.fit(X_train_scaled, y_train) print ( f"Best alpha: {rnd.best_params_['alpha']}" )
# Pros: faster than grid; explores continuous ranges; often finds good combos quickly.
# Cons: not exhaustive — you might miss the global optimum (though usually not by much).
# Bayesian Optimization
# Smarter still: build a probabilistic model (typically a Gaussian Process) of "score as a function of hyperparameters" , and use it to pick the next promising point to try.
# How it works
# Initialize by trying a few random points; record their scores.
# Fit a surrogate model (e.g., Gaussian Process) that predicts the score at any unseen hyperparameter point, plus uncertainty.
# Acquisition function (Expected Improvement / Upper Confidence Bound) decides where to evaluate next — balancing exploration (uncertain regions) and exploitation (regions with predicted high score).
# Train and score the model at that point; update the surrogate.
# Repeat until budget exhausted.
# Tools: scikit-optimize ( BayesSearchCV ), Optuna , Hyperopt .
# from skopt import BayesSearchCV from sklearn.linear_model import Ridge
opt = BayesSearchCV(Ridge(), { 'alpha' : ( 1e-4 , 1e2 , 'log-uniform' )}, n_iter= 25 , cv= 5 )
opt.fit(X_train_scaled, y_train) print ( f"Best alpha: {opt.best_params_['alpha']:.4f}" )
# Pros: finds excellent hyperparameters with few evaluations; great when each model fit is expensive.
# Cons: more complex setup; the surrogate model itself takes a moment per iteration.
# Comparison
# Method How it explores Best for Cost
# Grid Search Every combination Few hyperparameters with discrete values Exponential in #params
# Random Search Random sampling Many hyperparameters, large ranges Linear in #iterations
# Bayesian Optimization Smart sampling, learns from past trials Expensive-to-train models, want best result with minimum cost Linear, but each step has surrogate-fitting overhead
# Exam questions on this topic
# How does Bayesian Optimization work, and how can it be used to tune the hyperparameters of a Linear Regression model?
# Answer
# Bayesian Optimization is an intelligent hyperparameter tuning technique that uses a probabilistic surrogate model to choose the next set of hyperparameters to try, balancing exploration and exploitation.
# How it works:
# Initialize with a few random hyperparameter samples; train and score each via cross-validation.
# Build a surrogate model (typically a Gaussian Process) that maps hyperparameters → CV score, with uncertainty estimates at every point in the search space.
# Use an acquisition function — such as Expected Improvement (EI) or Upper Confidence Bound (UCB) — to choose the next hyperparameter point. The acquisition function trades off:
# Exploitation — points where the surrogate predicts a high score.
# Exploration — points where the surrogate is uncertain.
# Train the model at the chosen point and record the actual CV score.
# Update the surrogate with this new observation.
# Repeat steps 3–5 until the evaluation budget is exhausted.
# Applied to Linear Regression hyperparameter tuning:
# For Ridge: tune alpha over a log-uniform range like (1e-4, 1e2).
# For ElasticNet: tune alpha AND l1_ratio simultaneously.
# For polynomial regression: tune degree .
# Use BayesSearchCV from scikit-optimize , or Optuna , or Hyperopt .
# Advantages over Grid/Random Search:
# Reaches near-optimal hyperparameters in many fewer trials — important when each fit is expensive.
# Handles continuous, log-scale, and discrete hyperparameters together.
# Provides uncertainty estimates of the score landscape.
# Hyperparameters are settings you choose; parameters are learned from data.
# Grid Search: exhaustive, slow.
# Random Search: sample randomly, faster.
# Bayesian Optimization: smart sampling using a surrogate model — best for expensive models.
# All use cross-validation to score each candidate setting.

#==============================================================================
# TOPIC 17: Numerical Problems Solved
#==============================================================================

# Index of problems
# P1: Birth Weight
# P2: College GPA
# P3: CEO Salary
# P4: Coefficient interpretation
# P5: Mobile p-value
# P6: RMSE comparison
# Practice 1: VIF
# Practice 2: Manual β
# Practice 3: Bias/Variance
# Solving checklist
# What's in this chapter
# Every numerical problem from your past papers, solved step-by-step . Read each one twice — first to follow the answer, second to internalize the method so you can adapt it to a new problem.
# Numerical problems index
# Birth Weight Prediction — Mar 2021 1b
# College GPA from SAT and HS percentile — Mar 2021 1c
# CEO Salary log model — Mar 2021 2a
# Coefficient interpretation y = 2x₁ + 12x₂ + 3x₃ + 5 — Mar 2021 2b / Sample 1d · 2-4 marks
# Mobile sales p-value interpretation — Nov 2021 1c
# RMSE comparison: salary vs age — Nov 2021 1d
# VIF calculation — practice problem
# Manual β computation — practice problem
# Problem 1: Birth Weight Prediction
# 1b · Birth Weight dataset (n = 1,388 births)
# Below is the equation of the births given by women in the United States. Two variables of interest are the dependent variable, infant birth weight in ounces (bwght), and an explanatory variable, average number of cigarettes the mother smoked per day during pregnancy (cigs). The following simple regression was estimated using data on n = 1,388 births: pred_bwght = 119.77 - 0.514*cigs What is the predicted birth weight when cigs = 0? What about when cigs = 20 (one pack per day)? Comment on the difference.
# Step 1 — Identify the model
# This is a simple linear regression with form ŷ = β₀ + β₁·x where:
# x = cigs (cigarettes per day)
# ŷ = pred_bwght (predicted birth weight in ounces)
# β₀ = 119.77 (intercept)
# β₁ = −0.514 (slope)
# Step 2 — Predict at cigs = 0
# Substitute x = 0:
# pred_bwght = 119.77 − 0.514 × 0 = 119.77 ounces
# So a non-smoking mother is predicted to have a baby weighing 119.77 oz ≈ 7.49 lbs ≈ 3.40 kg.
# Step 3 — Predict at cigs = 20
# pred_bwght = 119.77 − 0.514 × 20 = 119.77 − 10.28 = 109.49 ounces
# A mother smoking a pack/day is predicted to have a baby weighing 109.49 oz ≈ 6.84 lbs ≈ 3.10 kg.
# Step 4 — Comment on the difference
# Difference = 119.77 − 109.49 = 10.28 ounces .
# That's roughly 8.6% of the non-smoking baseline weight.
# Babies of pack-a-day smokers are predicted to weigh about 10 ounces less on average — a practically significant reduction.
# This is consistent with public-health findings linking maternal smoking to lower birth weight.
# Caveat: this is a simple regression — other variables (nutrition, prenatal care, alcohol) are not controlled for. Causation cannot be established from a single regression.
# Problem 2: College GPA from SAT and High School Percentile
# 1c · College GPA dataset
# The following equation has been obtained for college Grade Point Average (colgpa) at a US university, colgpa = 1.392 - 0.0135*hsperc + 0.00148*sat where hsperc is percentile in the high school graduating class (defined so that, for example, hsperc=5 means the top 5% of the class) and sat is the combined SAT score.
(a) Why does it make sense for the coefficient on hsperc to be negative?
(b) What is the predicted change in colgpa for a difference in SAT of 140 points (about one standard deviation)?
(c) What change in SAT score would be required to produce a 0.50 increase in colgpa?
# Part (a) — Why is hsperc coefficient negative?
# The variable hsperc is inverted compared to academic performance:
# hsperc = 5 means top 5% of the class — a strong student.
# hsperc = 95 means bottom 5% of the class — a weak student.
# So lower hsperc → better student → higher college GPA. Mathematically, the coefficient on hsperc must be negative to reflect: as percentile rank goes up (worse rank), predicted college GPA goes down. The β = −0.0135 says: each one-unit drop in class rank reduces predicted college GPA by about 0.0135 points .
# Part (b) — Predicted change in colgpa for ΔSAT = 140
# Coefficient on SAT is β_sat = 0.00148. Holding hsperc constant:
# Δcolgpa = β_sat × ΔSAT = 0.00148 × 140 = 0.2072
# Inference: a 140-point higher SAT (about one standard deviation) is associated with an increase of about 0.21 GPA points — meaningful but not huge.
# Part (c) — ΔSAT needed for Δcolgpa = 0.50
# Solve 0.50 = 0.00148 × ΔSAT for ΔSAT:
# ΔSAT = 0.50 / 0.00148 ≈ 337.84 points
# Inference: to gain 0.5 GPA units, a student would need to raise their SAT by roughly 338 points — that's about 2.4 standard deviations, a very large change. SAT alone has a relatively modest effect on college GPA in this model.
# Problem 3: CEO Salary log model — most important problem
# 2a · CEO compensation dataset (n = 209)
# Following equation has been obtained using a CEO Salary database for 209 CEOs of US companies: log(Salary) = 4.32 + 0.280*log(sales) + 0.0174*roe + 0.00024*ros SE values: (0.32) (0.035) (0.0041) (0.00054) where Salary in 1000s of dollars, sales in millions of dollars, return on the firm's equity (roe) in percent, and ros is return on the firm's stock (in percent).
(a) For this regression, what is the predicted percentage increase in salary if the ros increases by 50 points?
(b) Test the null hypothesis that ros has no effect on salary against the alternative that ros has a positive effect. Carry out the test at the 10% significance level. (Reject if t > 1.282)
(c) Would you include ros in a final model explaining CEO compensation in terms of firm performance? Explain.
# Part (a) — % salary change for Δros = 50
# Note: this is a log-linear model — the dependent variable is log(Salary) but ros enters in levels , not log. Because of the log-linear form, the coefficient β_ros = 0.00024 has the interpretation: "a 1-unit increase in ros leads to approximately a 100·β_ros = 0.024% increase in salary."
# For a 50-unit change:
# % Δ Salary ≈ 100 × β_ros × Δros = 100 × 0.00024 × 50 = 1.2%
# So a 50-point increase in ros is associated with about a 1.2% increase in CEO salary . (For exact percentages with larger Δ, use 100·(e^(β·Δros) − 1), but for small β, the linear approximation is fine.)
# Part (b) — Hypothesis test on β_ros (one-tailed at 10%)
# Hypotheses:
# H₀: β_ros = 0 (ros has no effect on salary)
# H₁: β_ros > 0 (ros has a positive effect)
# Test statistic:
# t = β̂_ros / SE(β̂_ros) = 0.00024 / 0.00054 ≈ 0.444
# Decision rule: reject H₀ if t > 1.282 (the critical value at α = 0.10 for a one-tailed test).
# Comparison: 0.444 < 1.282 → fail to reject H₀ .
# Conclusion: at the 10% significance level, there is insufficient evidence to conclude that ros has a positive effect on CEO salary. The coefficient on ros is not statistically distinguishable from zero.
# Part (c) — Should ros be in the final model?
# Reasons to drop ros:
# The hypothesis test (part b) shows the coefficient is not statistically significant even at the lenient 10% level.
# The economic effect is very small — a 50-point change in ros gives only a 1.2% salary change.
# Keeping a noisy non-significant predictor wastes a degree of freedom and inflates uncertainty in the other coefficients.
# Reasons to keep ros:
# If it's of theoretical interest (does stock return affect CEO pay?), reporting "no significant effect" is itself a finding.
# Adjusted R² and out-of-sample MSE could decide empirically.
# Conclusion: based purely on this regression, I would not include ros in the final model — it's not statistically significant and the effect size is small. log(sales) and roe are the meaningful predictors of CEO salary here.
# Problem 4: Coefficient interpretation
# 2b / 1d · ML-1 Sample · 2-4 marks · Generic regression equation
# If y = 2x1 + 12x2 + 3x3 + 5 is the linear regression equation, then explain how the coefficients of x1, x2, x3 affect the value of y.
# Step 1 — Rewrite in standard form
# y = 5 + 2·x₁ + 12·x₂ + 3·x₃
# So β₀ = 5, β₁ = 2, β₂ = 12, β₃ = 3.
# Step 2 — Apply the universal interpretation rule
# "Holding all other features constant, a 1-unit increase in xⱼ is associated with a βⱼ-unit change in y."
# Coefficient Sign & magnitude Interpretation
# β₁ = 2 Positive, smallest 1 unit ↑ in x₁ → 2 units ↑ in y (smallest positive effect)
# β₂ = 12 Positive, largest 1 unit ↑ in x₂ → 12 units ↑ in y (most influential predictor)
# β₃ = 3 Positive, medium 1 unit ↑ in x₃ → 3 units ↑ in y (modest positive effect)
# Step 3 — Comparison & caveats
# Order of influence (raw): x₂ > x₃ > x₁ (12 vs 3 vs 2).
# x₂ is 6× more influential than x₁ (12/2 = 6) and 4× more than x₃ (12/3 = 4).
# The intercept β₀ = 5 is the predicted y when all x's = 0. May or may not be physically meaningful.
# Caveat: coefficient comparisons are only valid if x₁, x₂, x₃ are on the same scale (e.g., all in standardized form). If features have different units, use standardized coefficients .
# Problem 5: p-value interpretation (Mobile phone sales)
# 1c · Mobile phone sales regression
# A linear regression model is build with three independent variable price, advertisement cost and promotion cost to predict unit sales of mobile phone. Say the p value for the t-test of the variable 'advertisement cost' is 0.02. What is your inference on this?
# Step 1 — State the hypotheses
# For each coefficient in a regression, the t-test asks whether that coefficient is statistically distinguishable from zero:
# H₀: β_ad = 0 — advertisement cost has no effect on unit sales.
# H₁: β_ad ≠ 0 — advertisement cost has a (non-zero) effect.
# Step 2 — Interpret the p-value
# The p-value is the probability of seeing a coefficient at least as extreme as the observed one, if H₀ were true . Here p = 0.02 = 2%.
# Step 3 — Compare against significance levels
# Significance level α Threshold Decision
# 10% 0.10 0.02 < 0.10 → reject H₀
# 5% (most common) 0.05 0.02 < 0.05 → reject H₀
# 1% 0.01 0.02 > 0.01 → fail to reject H₀
# Step 4 — Stated inference
# At the conventional 5% significance level, we reject H₀ . Advertisement cost is a statistically significant predictor of mobile phone unit sales. The probability of observing this β value by chance alone (if advertising truly had no effect) is only 2%.
# At the stricter 1% level, the result would not be significant. So we'd say: "significant at the 5% level but not at the 1% level."
# Practical implication: keep advertisement cost in the model. The t-test alone doesn't tell you the magnitude of the effect — you'd want to look at the coefficient value and its confidence interval too.
# Problem 6: RMSE comparison (CTC vs Age)
# 1d · Two unrelated regression models
# The RMSE of the regression model which predicting the CTC salary is 12324 and the RMSE of the other regression model which predicting the age of the person is 55. Comment on the performance of these two models. [output column is not scaled or transformed]
# Step 1 — Recognize the trap
# RMSE has the same units as the target variable y . The two models predict completely different things on completely different scales. Direct comparison of raw RMSEs is meaningless.
# Step 2 — Evaluate each in context
# Model 1: CTC salary, RMSE = 12,324
# Indian CTC values typically range from 3,00,000 to 50,00,000+.
# Suppose mean CTC ≈ 6,00,000.
# %RMSE = 12,324 / 6,00,000 × 100 ≈ 2.05%
# An average error of 2% on salary predictions is very good .
# Model 2: Age, RMSE = 55
# Human ages typically range from 18 to 80.
# Suppose mean age ≈ 35.
# %RMSE = 55 / 35 × 100 ≈ 157%
# An RMSE of 55 is larger than the entire reasonable range of ages . The model is essentially useless — it might as well predict random numbers.
# Step 3 — Use scale-free metrics for fair comparison
# For comparing models predicting different ys, use:
# R² (coefficient of determination) — fraction of variance explained, range (−∞, 1]. A salary model with R² = 0.9 is comparable to an age model with R² = 0.9.
# MAPE — mean absolute percentage error, in %. Already scale-free.
# %RMSE = RMSE / mean(y) × 100 — quick rule of thumb.
# Step 4 — Final inference
# The CTC model performs excellently (relative error ≈ 2%). The age model performs terribly (relative error far exceeds the data range). The raw RMSE numbers (12,324 vs 55) are misleading — without converting to a scale-free metric, you'd wrongly think the age model is better. Always interpret RMSE relative to the magnitude of y.
# Practice Problem 1: VIF Calculation
# Practice problem
# In a regression with 5 features (x₁, …, x₅), suppose when you regress x₁ on the other four features you get R²₁ = 0.85. Compute VIF for x₁ and interpret.
# Solution
# VIF₁ = 1 / (1 − R²₁) = 1 / (1 − 0.85) = 1 / 0.15 ≈ 6.67
# Interpretation: the variance of β̂₁ is about 6.67× larger than it would be if x₁ were uncorrelated with x₂…x₅. Since 6.67 > 5, this is moderate-to-severe multicollinearity . Recommendation: drop x₁ if redundant, or merge with the most correlated companion feature, or use Ridge regression.
# Practice Problem 2: Manual β computation
# Practice problem
# You have 5 data points: (1, 2), (2, 4), (3, 5), (4, 4), (5, 5). Fit a simple linear regression by hand and compute β₀, β₁.
# Solution
# Step 1: means. x̄ = (1+2+3+4+5)/5 = 3, ȳ = (2+4+5+4+5)/5 = 4.
# Step 2: deviations.
# x y x − x̄ y − ȳ (x−x̄)(y−ȳ) (x−x̄)²
# 1 2 −2 −2 4 4
# 2 4 −1 0 0 1
# Sum 6 10
# Step 3: β₁. β₁ = 6 / 10 = 0.6
# Step 4: β₀. β₀ = ȳ − β₁·x̄ = 4 − 0.6·3 = 4 − 1.8 = 2.2
# Final equation: ŷ = 2.2 + 0.6·x
# Verify: predict for x = 3 → ŷ = 2.2 + 1.8 = 4.0 (passes through the centroid (3, 4) as expected).
# Practice Problem 3: Bias/Variance from CV
# Practice problem
# 5-fold CV gives R² scores of [0.82, 0.78, 0.85, 0.80, 0.79]. Compute bias and variance errors, and interpret.
# Solution
# Mean R² = (0.82 + 0.78 + 0.85 + 0.80 + 0.79) / 5 = 4.04 / 5 = 0.808
# Bias error = 1 − 0.808 = 0.192
# Standard deviation = √[((0.82−0.808)² + (0.78−0.808)² + (0.85−0.808)² + (0.80−0.808)² + (0.79−0.808)²) / 5] ≈ √(0.000688) ≈ 0.026
# Variance error = 0.026.
# Interpretation: the model explains about 80.8% of variance — decent but improvable. The low std-dev (0.026) indicates stable performance across folds — no overfitting concern. Bias (1−R²) is moderate at 0.192 — could try richer features or polynomial terms to reduce it.
# Quick numerical-problem checklist
# Solving recipe
# Identify the equation form — linear, log-linear, log-log, polynomial.
# Identify what's asked — predict y, compute Δy, find Δx, test a hypothesis.
# Substitute the given numbers carefully.
# Show every step — calculation by calculation. Examiners give partial marks.
# State units — ounces, %, GPA points, .
# Interpret — translate the number back into plain English.
# State caveats — "this is correlation, not causation"; "valid only if assumptions hold."
# Simple linear regression questions: substitute in ŷ = β₀ + β₁x.
# Log-linear questions: 100·β gives the % effect per unit change.
# Hypothesis tests: t = β̂ / SE; reject H₀ if |t| > critical value (or p < α).
# RMSE comparisons across different ys are meaningless — use R² or MAPE.
# VIF = 1/(1−R²_j); show every digit of the calculation.

#==============================================================================
# TOPIC 18: Exam Questions by Topic
#==============================================================================

# Machine Learning Fundamentals & Pipelines
# Linear Regression Assumptions
# Multicollinearity & VIF
# Bias-Variance Tradeoff & Cross-Validation
# Regularization (Ridge/Lasso/ElasticNet)
# Gradient Descent
# Evaluation Metrics (R²/Adj R²/RMSE/MAPE)
# Feature Selection
# Data Transformation & Feature Engineering
# Hyperparameter Tuning & Optimization
# Numerical Problems on Regression Models
# OLS Linear Regression & Model Building
# Data Preprocessing (Missing Values, Outliers, Encoding, Scaling)
# DataFrame Operations (Pandas)
# Exploratory Data Analysis (EDA)
# Open-ended Modeling & Business Interpretation
# Problem Statement / Context
# How to use
# Index of all 138 unique exam questions
# Every distinct question from your 8 ESA papers, grouped by topic. Each card shows the verbatim question, its source, dataset, and marks. Click the topic header to jump to the corresponding learning chapter for the full theory.
# Topic Question count Linked chapter
# Machine Learning Fundamentals & Pipelines 3 → Chapter
# Linear Regression Assumptions 10 → Chapter
# Multicollinearity & VIF 6 → Chapter
# Bias-Variance Tradeoff & Cross-Validation 9 → Chapter
# Regularization (Ridge/Lasso/ElasticNet) 14 → Chapter
# Gradient Descent 1 → Chapter
# Evaluation Metrics (R²/Adj R²/RMSE/MAPE) 7 → Chapter
# Feature Selection 5 → Chapter
# Data Transformation & Feature Engineering 5 → Chapter
# Hyperparameter Tuning & Optimization 6 → Chapter
# Numerical Problems on Regression Models 6 → Chapter
# OLS Linear Regression & Model Building 14 → Chapter
# Data Preprocessing (Missing Values, Outliers, Encoding, Scaling) 42 → Chapter
# DataFrame Operations (Pandas) 28 → Chapter
# Exploratory Data Analysis (EDA) 24 → Chapter
# Open-ended Modeling & Business Interpretation 5 → Chapter
# Problem Statement / Context 6 —
# Total 191
# Machine Learning Fundamentals & Pipelines → Open chapter
# Topic basics: definition of ML, supervised vs unsupervised vs reinforcement, regression vs classification, the LECESSTE pipeline. Full answers in chapter 01.
# 1d (UE20CS905)
# Describe the key steps in building a supervised machine learning pipeline from data ingestion to model deployment. Include tools or techniques relevant at each stage.
# 1e (UE20CS905)
# What is the difference between the Classification and Regression problem?
# 1a (UE20CS905)
# What is Machine learning? State any two types of machine learning.
# Linear Regression Assumptions → Open chapter
# Topic basics: LINER (Linearity, Independence, Normality, Equal variance, no multicollinearity). Each verified visually + statistically (Breusch-Pagan, Durbin-Watson, Shapiro-Wilk). Full answers in chapter 07.
# 5b Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check assumptions of linear regression. Write your inferences.
# 1a (UE20CS905)
# Describe the key assumptions of linear regression. For each assumption, explain how it can be verified using visual or statistical techniques, and the potential impact if the assumption is violated.
# 5b (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Check assumptions of linear regression. Write your inferences.
# 1c (UE20CS905)
# Explain the assumptions of linear regression.
# 5b (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Use OLS statsmodels package to build the Linear Regression model (Without multicollinearity feature) on the train set. Generate the summary report. check assumptions of linear regression. Write your inferences.
# 1a (UE20CS905)
# Explain Heteroscedasticity and Multicollinearity in Linear Regression.
# 1d (UE20CS905)
# How can you deal with autocorrelation of errors?
# 1c (UE20CS905)
# State the assumptions of linear regression algorithm.
# 3(ii) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Explore the statistical significance of the model build and comment about all the assumptions.
# 5b (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Use OLS statsmodels package to build the Linear Regression model (Without multicollinearity feature) on the train set. Generate the summary report. check assumptions of linear regression. Write your inferences.
# Multicollinearity & VIF → Open chapter
# Topic basics: VIF = 1/(1−R²_j); < 5 OK, > 10 severe. Detect via correlation matrix and VIF. Fix by dropping, combining, Ridge, or PCA. Full answers in chapter 08.
# 4f Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# check and reduce multicollinearity using VIF.
# 4f (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# check and reduce multicollinearity using VIF.
# 1a (UE20CS905)
# What is Multicollinearity? How to detect the presence of multicollinearity and which variables are involved in it?
# 1a (UE20CS905)
# What is Multicollinearity? How to detect the presence of multicollinearity and which variables are involved in it?
# 4i (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check and reduce multicollinearity using VIF.
# 4h (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Drop columns that are not needed, then evaluate multicollinearity with VIF and reduce it where possible.
# Bias-Variance Tradeoff & Cross-Validation → Open chapter
# Topic basics: Error = Bias² + Variance + Noise. Operationally: bias = 1 − mean(R²), variance = std(R²) from k-fold CV. Full answers in chapters 09 and 11.
# 6a Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Train a Linear Regression model using sklearn on the training data and calculate the bias error (1 - mean R²) and variance error (standard deviation of R²) by performing 5-fold cross-validation.
# 6a (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Train a Linear Regression model using sklearn on the training data and calculate the bias error (1 - mean R²) and variance error (standard deviation of R²) by performing 5-fold cross-validation.
# 1b (UE20CS905)
# Explain the procedure involved in k-fold cross validation.
# 1e (UE20CS905)
# How the problem of overfitting can be reduced in Linear regression? What is bias variance trade off?
# 1b (UE20CS905)
# Explain the procedure involved in k-fold cross validation.
# 1e (UE20CS905)
# What strategies can be employed to mitigate overfitting in Linear Regression? Provide an explanation of various forms of Linear Regression that address the issue of overfitting.
# 6a (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Using sklearn's linear regression model train model on the train set compute bias error (mean r2) and variance error (standard deviation r2) across 5 fold cross validation.
# 1b (UE20CS905)
# How can you handle overfitting and underfitting?
# 6b (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Using sklearn's linear regression model train model on the train set compute bias error (mean r2) and variance error (standard deviation r2) across 5 fold cross validation.
# Regularization (Ridge/Lasso/ElasticNet) → Open chapter
# Topic basics: Ridge L2 (shrinks all), Lasso L1 (zeros some), ElasticNet (mix). All add α·penalty to MSE. Tune α via CV. Full answers in chapter 10.
# 1a Feb 2025 ESA (UE20CS905)
# What role does regularization play in improving Linear Regression models?
# 6 Feb 2025 ESA (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Model Comparisons and Hyperparameter tuning
# 6b Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Train below models and obtain values using 5 fold cross validation on train data and 'rmse' metric. Find the metric score in the test set and suggest the best model. - ElasticNet(alpha=0.1, l1_ratio=0.5) (5 marks) - Lasso(alpha=0.01, max_iter=500) (5 marks)
# 1b (UE20CS905)
# What is regularization in linear regression? Compare and contrast Lasso and Ridge regression in terms of mathematical formulation, impact on coefficients, and use cases.
# 6 (UE20CS905) · — marks · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Model Comparisons and Hyperparameter tuning
# 6b (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Train below models and obtain values using 5 fold cross validation on train data and 'rmse' metric. Find the metric score in the test set and suggest the best model. - ElasticNet(alpha=0.1, l1_ratio=0.5) (5 marks) - Lasso(alpha=0.01, max_iter=500) (5 marks)
# 3(ii) (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Model Comparisons and Hyperparameter tuning
# 3(ii).1 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Train below models and obtain values using 5 fold cross validation on train data and 'RMSE' metric. Find the metric (RMSE) score in test set and suggest the best model. - Ridge(alpha=1, max_iter=500) (5 marks) - Lasso(alpha=0.01, max_iter=500) (5 marks) - ElasticNet(alpha=0.1, l1_ratio=0.01, max_iter=500) (5 marks)
# 6 (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Model Comparisons and Hyperparameter tuning
# 6b (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Train below models and obtain values using 5 fold cross validation on train data and 'rmse' metric. Find the metric score in the test set and suggest the best model. - Ridge(alpha=1, max_iter=500) - Lasso(alpha=0.01, max_iter=500)
# 1a (UE20CS905)
# Write the expression for the cost function, which need to be minimized in Linear regression with RIDGE regularization.
# 1e (UE20CS905)
# If we increase the value of lambda, what will happen to the estimated coefficients in RIDGE model?
# 6 (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Model Comparisons and Hyperparameter tuning
# 6c (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Train below models and obtain values using 5 fold cross validation on train data and 'rmse' metric. Find the metric score in test set and suggest the best model. - Ridge(alpha=1, max_iter=500) (5 marks) - Lasso(alpha=0.01, max_iter=500) (5 marks)
# Gradient Descent → Open chapter
# Topic basics: iterative minimization, β := β − α·∂J/∂β. Variants: Batch, SGD, Mini-Batch. Full answer in chapter 06.
# 2c (UE20CS905)
# Explain Gradient Descent in brief.
# Evaluation Metrics (R²/Adj R²/RMSE/MAPE) → Open chapter
# Topic basics: R² explains variance; Adj R² penalizes feature count; RMSE in y units (outlier-sensitive); MAPE is %. Full answers in chapter 12.
# 1b Feb 2025 ESA (UE20CS905)
# What is the difference between R² and Adjusted R², and when should each be used?
# 5c Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Predict the values using test set, Compute measures of RMSE, MAPE, R-square for test set.
# 5c (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Predict the values using test set, Compute measures of RMSE, MAPE, R-square for test set.
# 5d (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Compute measures of RMSE, MAPE, R-square for test set.
# 1b (UE20CS905)
# How adjusted R-square is differing from R-square? Brief the role of adjusted R-square in feature selection process.
# 1d (UE20CS905) · RMSE comparison numerical example
# The RMSE of the regression model which predicting the CTC salary is 12324 and the RMSE of the other regression model which predicting the age of the person is 55. Comment on the performance of these two models. [output column is not scaled or transformed]
# 5d (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Compute measures of RMSE, MAPE, R-square for test set.
# Feature Selection → Open chapter
# Topic basics: Filter (correlation, VIF), Wrapper (Forward/Backward/RFE), Embedded (Lasso). Full answers in chapter 14.
# 1c Feb 2025 ESA (UE20CS905)
# What are Wrapper Methods in feature selection, and how are they applied in Linear Regression?
# 1c (UE20CS905)
# What is Recursive Feature Elimination (RFE)? Explain how it works, its advantages and limitations, and how it can be used to improve model performance in linear regression.
# 1d (UE20CS905)
# Explain the procedure involved in Forward Feature Selection.
# 1d (UE20CS905)
# Explain the procedure involved in Forward Feature Selection.
# 6a (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Perform backward elimination for selecting the "best" features, you can use SequentialFeatureSelector (SFS) from mlxtend.
# Data Transformation & Feature Engineering → Open chapter
# Topic basics: log, Box-Cox, Yeo-Johnson, polynomial features, interactions, datetime extraction, binning. Full answers in chapter 14.
# 2(iii).5 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Convert the feature 'size' to int by removing alphabetic content and keep only numeric content. In case of missing/null content replace by constant numeric value 2.
# 2(iii).6 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Convert the feature 'total_sqft' to numerical using 'to_numeric' method. Also, replace all its missing entries by mean.
# 1c (UE20CS905)
# Discuss the need for data transformations in a linear regression model. Also write about various techniques employed.
# 3(iii) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Make the model more reliable by performing appropriate feature engineering techniques.
# 3(iv) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Explore the possibility of improving the model performance by introducing new interactive features.
# Hyperparameter Tuning & Optimization → Open chapter
# Topic basics: Grid (exhaustive), Random (sampled), Bayesian (smart-sampled). All score via CV. Full answers in chapter 16.
# 1d Feb 2025 ESA (UE20CS905)
# How does Bayesian Optimization work, and how can it be used to tune the hyperparameters of a Linear Regression model?
# 6c Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Using Grid search on the ridge model, find the best value of alpha and corresponding rmse value on the test set.
# 6c (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Using Grid search on the ridge model, find the best value of alpha and corresponding rmse value on the test set.
# 3(ii).2 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Using Random search on Lasso model find the best value of alpha and corresponding RMSE value on test set.
# 6c (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Using Grid search on Lasso model find the best value of alpha and corresponding rmse value on test set.
# 6d (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Using Grid serach on Lasso model find the best value of alpha and corresponding rmse value on test set.
# Numerical Problems on Regression Models → Open chapter
# These appear primarily in the paper. Step-by-step solutions for every numerical in chapter 17.
# 1b (UE20CS905) · Birth Weight regression — n=1,388 births (textbook example)
# Below is the equation of the births given by women in the United States. Two variables of interest are the dependent variable, infant birth weight in ounces (bwght), and an explanatory variable, average number of cigarettes the mother smoked per day during pregnancy (cigs). The following simple regression was estimated using data on n = 1,388 births: pred_bwght = 119.77 - 0.514*cigs What is the predicted birth weight when cigs = 0? What about when cigs = 20 (one pack per day)? Comment on the difference.
# 1c (UE20CS905) · GPA2 college students dataset — n=4,137 (textbook example)
# Using the data in GPA2 on 4,137 college students, the following equation was estimated by OLS: colgpa = 1.392 - 0.0135*hsperc + 0.00148*sat where colgpa is measured on a four-point scale, hsperc is the percentile in the high school graduating class (defined so that, for example, hsperc = 5 means the top 5% of the class), and sat is the combined math and verbal scores on the student achievement test. • Why does it make sense for the coefficient on hsperc to be negative? • Suppose that two high school graduates, A and B, graduated in the same percentile from high school, but Student A's SAT score was 140 points higher (about one standard deviation in the sample). What is the predicted difference in college GPA for these two students? Is the difference large? • Holding hsperc fixed, what difference in SAT scores leads to a predicted colgpa difference of .50, or one-half of a grade point? Comment on your answer.
# 2a (UE20CS905) · CEO salary regression — n=209 firms (textbook example)
# 2b (UE20CS905) · Numerical example (coefficients given)
# If y = 2x1 + 12x2 + 3x3 + 5 is the linear regression equation, then explain how the coefficients of x2 and x3 affect the value of y.
# 1d (UE20CS905) · Numerical example (coefficients given)
# If y = 2x1 + 12x2 + 3x3 + 5 is the linear regression equation, then explain how the coefficients of x1 and x2 affect the value of y.
# 1c (UE20CS905) · Mobile-phone sales numerical example
# A linear regression model is build with three independent variable price, advertisement cost and promotion cost to predict unit sales of mobile phone. Say the p value for the t-test of the variable 'advertisement cost' is 0.02. What is your inference on this?
# OLS Linear Regression & Model Building → Open chapter
# Topic basics: ŷ = β₀ + Σβⱼxⱼ; OLS normal equation β̂ = (XᵀX)⁻¹Xᵀy; statsmodels.OLS for full report. See chapters 02, 03, 13.
# 5 Feb 2025 ESA (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Perform Below Modeling Tasks
# 5a Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Use OLS statsmodels package to build the Linear Regression model (Without multicollinearity feature) on the train set to ensure feature 'Weight' as target(y). Generate the summary report.
# 5 (UE20CS905) · — marks · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Perform Below Modeling Tasks
# 5a (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Use OLS statsmodels package to build the Linear Regression model (Without multicollinearity feature) on the train set to ensure feature 'Weight' as target(y). Generate the summary report. (Note: question text says 'Weight' as target — paper appears to be re-using the Feb 2025 wording; in context the target is laptop Price.)
# 3(i) (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Perform Below Modeling Tasks
# 3(i).2 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Use OLS statsmodels package to build the Linear Regression model on the train set. Also, generate the summary report.
# 3(i).3 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Using sklearn's linear regression model train model on the train set and interpret the coefficients.
# 5 (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Perform Below Modeling Tasks
# 5c (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Predict the values using test set.
# 3b (UE20CS905) · Admission / Student Placement dataset — SlNo, Gender, Percent_SSC/HSC/Degree/MBA, Boards, Streams, Course, Experience_Yrs, Entrance_Test, Percentile_ET, Specialization_MBA, Marks Communication, Marks_Projectwork, Placement, Salary
# Fit a base model. Please write your key observations. i. What is the overall R²? Please comment on whether it is good or not. ii. What is the adjusted R²? Is it different from R²? Why? iii. Which variables are significant. Explain the Feature Selection Technique used? iv. Is there multicollinearity, Suggest ways to remove it. v. Which other key model output parameters do you want to look at?
# 2b (UE20CS905) · Airbnb NYC dataset — id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365
# Fit a base model. Please write your key observations. i. What is the overall R²? Please comment on whether it is good or not. (2 marks) ii. What is the adjusted R²? Is it different from R²? Why? (3 marks) iii. Which variables are significant? (4 marks) iv. Is there multicollinearity? (4 marks) v. Which other key model output parameters do you want to look at? (2 marks)
# 3(i) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Build the linear regression to predict the 'traffic_volume'. Evaluate the base model performance using appropriate measures.
# 5 (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Perform Below Modeling Tasks
# 5c (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Use sklearn library to Predict the values using test set.
# Data Preprocessing (Missing Values, Outliers, Encoding, Scaling) → Open chapter
# Topic basics: 5 sub-steps — handle missing (mean/median/mode/drop), outliers (IQR/Z-score/clip/drop), encoding (label/dummy n-1), scaling (StandardScaler), splitting. Full answers in chapter 15.
# 4 Feb 2025 ESA (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Perform Data pre-processing as Mentioned Below.
# 4a Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check for the presence of missing values across features and represent them visually also treat it
# 4b Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Examine the numerical features for any outliers and provide visual evidence and also treat it with dropping.
# 4c Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Perform n-1 dummy encoding to convert categorical features into numerical, followed by StandardScaler transformation on the numerical data.
# 4d Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Split the pre-processed dataframe into 2 parts y (output), x (input) features.
# 4e Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Plot output feature and print skewness. Describe your observations.
# 4 (UE20CS905) · — marks · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Perform Data pre-processing as Mentioned Below.
# 4a (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Check for the presence of missing values across features and represent them visually also treat it
# 4b (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Examine the numerical features for any outliers and provide visual evidence and also treat it with dropping.
# 4c (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Perform label encoding to convert categorical features into numerical, followed by StandardScaler transformation on the numerical data.
# 4d (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Split the pre-processed dataframe into 2 parts y (output), x (input) features.
# 4e (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Plot output feature and print skewness. Describe your observations.
# 2(iii) (UE20CS905) · — marks · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Pre-process the Dataframe as Mentioned Below.
# 2(iii).1 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Replace missing values of the feature 'balcony' with numerical value 0 and convert its feature type to int.
# 2(iii).2 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Replace missing values of the feature 'bath' missing values with numerical 1 and convert feature type to int.
# 2(iii).3 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Replace missing values of the feature 'location' with a constant "missing".
# 2(iii).4 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Replace missing values of the feature 'society' with a constant "missing".
# 2(iii).7 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Eliminate all the outlies records/rows from Dataframe with respect to feature 'bath'.
# 2(iii).8 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# convert 3 categorical features i.e. 'availability', 'location' and 'society' into numerical using label encoding.
# 2(iii).9 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Perform one hot encoding on feature 'area_type', also ensure output columns are of type int.
# 3(i).1 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Split the processed Dataframe into 2 parts train and test with ratio as 70:30. Ensure feature 'price' as target(y).
# 4 (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Perform Data pre-processing as Mentioned Below.
# 4a (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check and visualize if there are any missing values feature wise.
# 4b (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Implement a strategy to deal with the missing values with reason.
# 4c (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check and visualize if there are any outliers present in the numerical features.
# 4d (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Treat the outlies records/rows from Dataframe, Use IQR and Drop the outliers in the feature.
# 4e (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Convert the categorical features into numerical using n-1 dummy encoding techniques.
# 4f (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Perform standardscaler on numerical data.
# 4g (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Split the pre-processed data frame into 2 parts y (output), x (input) features.
# 4h (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Plot output feature, input feature and print skewness.
# 5a (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Split the pre-processed data frame into 2 parts train and test with a ratio as 80:20. Ensure feature 'Weight' as target(y).
# 1e (UE20CS905)
# Explain any two of the data preprocessing steps.
# 2(ii) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Perform required pre-processing techniques on the dataset, which are required for building the Machine Learning model. Justify the approaches/techniques used for pre-processing. Explain/type the clear reason for the choice of your techniques for the different pre-processing techniques.
# 4 (UE20CS905) · — marks · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Perform Data pre-processing as Mentioned Below.
# 4a (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Examine the presence of missing values across features, visualize them, and handle accordingly.
# 4b (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Analyze each numerical feature for potential outliers and visualize the findings.
# 4c (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Treat the outlies records/rows from Dataframe, Use IQR and Drop the outliers in the feature.
# 4d (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Convert the categorical features into numerical using n-1 dummy encoding techniques.
# 4e (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Perform StandardScaler on numerical data.
# 4f (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Split the pre-processed dataframe into 2 parts y (output), x (input) features.
# 4g (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Plot output, input feature and print skewness.
# 5a (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Split the pre-processed dataframe into 2 parts train and test with ratio as 80:20. Ensure feature 'totlngth' as target(y).
# DataFrame Operations (Pandas) → Open chapter
# Topic basics: read_csv, head/info/describe, dtype changes, groupby, value_counts, isnull, dropna, fillna, get_dummies, indexing. Code patterns in chapter 20.
# 2a Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print the dimensions of the dataset i.e. no of rows and columns.
# 2b Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print the data types of all the features.
# 2c Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Does any feature need type casting? if yes, perform it.
# 2d Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print statistical summary of all the numeric as well as categorical features and drop unnecessary features.
# 2e Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Find out how many unique categories are available and number of instances in each of the categorical features.
# 2a (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Print the dimensions of the dataset i.e. no of rows and columns.
# 2b (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Print the data types of all the features.
# 2c (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Does any feature need type casting? if yes, perform it.
# 2d (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Print statistical summary of all the numeric as well as categorical features and drop unnecessary features.
# 2e (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Find out how many unique categories are available and number of instances in each of the categorical features.
# 2(i).1 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Read/load the dataset as a pandas Dataframe.
# 2(i).2 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Print/show the dimensions of Dataframe i.e., no of rows and columns.
# 2(i).3 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Print/show the data types of all the features/columns.
# 2(i).4 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Print/show statistical summary of all the numeric features.
# 2(i).5 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Print/show statistical summary for all the categorical variable.
# 2(i).6 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Find out Feature wise Missing value counts.
# 2a (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Read/load the dataset.
# 2b (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print the dimensions of the dataset i.e. no of rows and columns.
# 2c (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print the data types of all the features.
# 2d (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Does any feature need type casting? if yes, perform the same and change the datatype to the correct type.
# 2e (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print statistical summary of all the numeric as well as categorical features and drop unnecessary features.
# 2f (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Find out how many unique categories are available and number of instances in each of the categorical features.
# 2a (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Read/load the dataset.
# 2b (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Print the dimensions of the dataset i.e. no of rows and columns.
# 2c (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Print the data types of all the features.
# 2d (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Does any feature need type casting? if yes, perform the same and change the datatype to the correct type.
# 2e (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Print statistical summary of all the numeric as well as categorical features and drop unnecessary features.
# 2f (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Determine the number of distinct categories in each categorical feature and the instance count for each category.
# Exploratory Data Analysis (EDA) → Open chapter
# Topic basics: histograms, boxplots, scatterplots, correlation heatmap, value counts, descriptive stats. Code patterns in chapter 20.
# 3 Feb 2025 ESA (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# EDA (Exploratory data Analysis)
# 3a Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Explore the associations between the numerical predictors and the target feature using visualizations. Describe your observations.
# 3b Feb 2025 ESA (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Examine how the categorical features are associated with the target variable. Use visualizations and provide your interpretations.
# 3 (UE20CS905) · — marks · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# EDA (Exploratory data Analysis)
# 3a (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Explore the associations between the numerical predictors and the target feature using visualizations. Describe your observations.
# 3b (UE20CS905) · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Examine how the categorical features are associated with the target variable. Use visualizations and provide your interpretations.
# 2(ii) (UE20CS905) · — marks · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Perform Below Exploratory Data Analysis(EDA) Tasks.
# 2(ii).1 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Show/Visualize the relationship between features 'bath' and 'price' using scattered plot.
# 2(ii).2 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Show/Visualize the relationship between features 'balcony' and 'price' using scattered plot.
# 2(ii).3 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# show/Visualize the relationship between features 'bath','balcony' and 'price' using 3D Scatterplot.
# 2(ii).4 (UE20CS905) · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Show outliers distribution of variable 'bath' by drawing Boxplot.
# 3 (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# EDA (Exploratory data Analysis)
# 3a (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check/Visualize the relationship between the numerical features with the target feature. State the inferences.
# 3b (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Visualize the relationship between 'target' and 'V_length'.
# 3c (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Check/Visualize the relationships between categorical features and the target feature. State the inferences.
# 3d (UE20CS905) · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Print skewness of numerical feature.
# 3a (UE20CS905) · Admission / Student Placement dataset — SlNo, Gender, Percent_SSC/HSC/Degree/MBA, Boards, Streams, Course, Experience_Yrs, Entrance_Test, Percentile_ET, Specialization_MBA, Marks Communication, Marks_Projectwork, Placement, Salary
# DATA DESCRIPTION: The data set consists of complete educational details of students right from their schooling to MBA and previous work experience. Our main objective is to predict the Salary of the students based on the info available.
ATTRIBUTES: SlNo, Gender, Percent_SSC, Board_SSC, Percent_HSC, Board_HSC, Stream_HSC, Percent Degree, Course_Degree, Experience_Yrs, Entrance_Test, Percentile_ET, Percent_MBA, Specialization_MBA, Marks Communication, Marks_Projectwork, Placement, Salary. Perform Exploratory data analysis and summarize important observations from the data set. Some pointers which would help you, but don't be limited by these: i. What are the number of rows; no. & types of variables (continuous, categorical etc.) ii. Calculate five-point summary for numerical variables iii. Summarize observations for categorical variables — no. of categories, % observations in each category iv. Check for defects in the data. Perform necessary actions to 'fix' these defects. check for numerical/categorical variable (wrong representation), missing values, outlier treatment, skewness, encoding v. Summarize relationships among variables. vi. Split dataset into train and test (70:30)
# 2a (UE20CS905) · Airbnb NYC dataset — id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365
# 2(i) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Understand the relation between each input and output variables. Support the finding with abstract tables and graphs. Summarize 5 important key findings (understanding) about the dataset.
# 3 (UE20CS905) · — marks · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# EDA (Exploratory data Analysis)
# 3a (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Explore the relationships between numerical features and the target feature through visualization, and provide your observations.
# 3b (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Visualize the relationship between 'belly' and 'totlngth'.
# 3c (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Check/Visualize the relationships between categorical features and the target feature using violinplot. State the inferences.
# 3d (UE20CS905) · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Print skewness of numerical feature.
# Open-ended Modeling & Business Interpretation → Open chapter
# These typically end Section C. Apply: build model → evaluate → interpret coefficients → check assumptions → recommend. Pipeline template in chapter 20.
# 4a (UE20CS905) · Admission / Student Placement dataset — SlNo, Gender, Percent_SSC/HSC/Degree/MBA, Boards, Streams, Course, Experience_Yrs, Entrance_Test, Percentile_ET, Specialization_MBA, Marks Communication, Marks_Projectwork, Placement, Salary
# How do you improve the accuracy of the model? Write clearly the changes that you will make before re-fitting the model. Fit the final model. Please feel free to have any number of iterations to get to the final answer. Marks are awarded based on the quality of the final model you are able to achieve.
# 4b (UE20CS905) · Admission / Student Placement dataset — SlNo, Gender, Percent_SSC/HSC/Degree/MBA, Boards, Streams, Course, Experience_Yrs, Entrance_Test, Percentile_ET, Specialization_MBA, Marks Communication, Marks_Projectwork, Placement, Salary
# Summarize as follows: i. Summarize the overall fit of the model and list down the measures to prove that it is a good model. ii. Write down a business interpretation/explanation of the model — which variables are affecting the target the most and explain the relationship. Feel free to use charts or graphs to explain. iii. What changes from the base model had the most effect on model performance? iv. What are the key risks to your results and interpretation?
# 3a (UE20CS905) · Airbnb NYC dataset — id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365
# How do you improve the accuracy of the model? Write clearly the changes that you will make before re-fitting the model. Fit the final model. • Feature Engineering / Feature Selection • Regularization • Cross Validation
Please feel free to have any number of iterations to get to the final answer. Marks are awarded based on the quality of the final model you are able to achieve.
# 3b (UE20CS905) · Airbnb NYC dataset — id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365
# Summarize as follows: i. Summarize the overall fit of the model and list down the measures to prove that it is a good model. ii. Write down a business interpretation/explanation of the model — which variables are affecting the target the most and explain the relationship. Feel free to use charts or graphs to explain. iii. What changes from the base model had the most effect on model performance? iv. What are the key risks to your results and interpretation? • Justification for selecting a model.
# 3(v) (UE20CS905) · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# Write the business inferences through the model parameters.
# Problem Statement / Context
# These are dataset descriptions, not standalone questions. They tell you which dataset Section B/C uses. Refer to the dataset notes in the index.
# 2 Feb 2025 ESA (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Problem Statement: Fish Weight Prediction. With a dataset of fish species, with some of its characteristics like vertical, diagonal, length, height, and width. Try to predict the weight of the fish based on their characteristics. We will use the Linear Regression Method to see whether the weight of the fish is related to their characteristic. Basic Perform below Pandas DataFrame Operations to understand the data.
# 2 (UE20CS905) · — marks · Laptop dataset (laptop_data.csv) — features: brand, processor type, RAM, storage configuration, graphics card, display, OS
# Problem Statement: The objective here is to build a regression model that can accurately predict the price of a laptop based on its key features such as brand, processor type, RAM size, storage configuration, graphics card, display specifications, and operating system. This model can assist consumers in making informed purchase decisions and help retailers in dynamic pricing.
# 2 (UE20CS905) · — marks · Bengaluru House Data (bengaluru_house_prices.csv) — area_type, availability, location, size, society, total_sqft, bath, balcony, price
# Problem Statement: Housing price dataset of Bengaluru city is provided. Based on the given details predict the price of the house.
Features: area_type, availability, location, size (BHK), society (encrypted), total_sqft, bath, balcony, price (target, in Lakhs).
# 2 (UE20CS905) · — marks · Fish dataset (Category, Species, Weight, Length1/2/3, Height, Width)
# Problem Statement: Fish Weight Prediction. With a dataset of fish species, with some of its characteristics like vertical, diagonal, length, height, and width. Try to predict the weight of the fish based on their characteristics. We will use the Linear Regression Method to see whether the weight of the fish is related to their characteristic. Basic Perform below Pandas DataFrame Operations to understand the data.
# 2 (UE20CS905) · — marks · Metro Interstate Traffic dataset (between Minneapolis and St Paul) — holiday, temp, rain_1h, snow_1h, clouds_all, weather_main, weather_description, date_time, traffic_volume
# 2 (UE20CS905) · — marks · Possum dataset (104 mountain brushtail possums) — case, site, population, sex, age, head length, skull width, totlngth (target), tail length, foot length, ear conch length, eye size, chest girt, belly girt
# Problem Statement: Predicting a Possum's total length using Linear Regression. you use your regression skills to predict the total length of a possum, its head length, whether it is male or female? etc. This classic practice regression dataset. The possum data frame consists of morphometric measurements on each of 104 mountain brushtail possums, trapped at seven sites from Southern Victoria to central Queensland. Basic Pandas DataFrame Operations to understand the data.
# How to use this index
# Get familiar with the breadth. Scroll through every topic — note which appear most often.
# For each topic that appears 5+ times (Assumptions, Regularization, OLS, Preprocessing) — make sure you can answer ANY of those questions cold.
# For each topic that appears 1-2 times — read the corresponding chapter once, but don't over-invest.
# Click "Open chapter" to read full theory, formulas, code, and worked examples.

#==============================================================================
# TOPIC 19: Most Important Topics
#==============================================================================

# How to read this page
# Section A — 1-mark questions
# Section B — Q2/Q3 patterns
# Section C — big questions
# Topic frequency table
# Hot-10 topics for ESA
# Common traps & mistakes
# 3-day final revision plan
# How to read this page
# I went through every Section-A, Section-B, and Section-C question across 8 ESA papers (, ML-1 Sample, Nov 2021, Aug 2023, , Nov 2024, Feb 2025, ) and counted
how often each topic appeared. The result is a ranked list of topics that actually show up,
not just topics that look important in a textbook.
# The big lesson — six topics dominate Section A. If you master them, you nearly
always score 4–5 out of 5 on Section A. The rest comes from Sections B and C, where everyone
loses marks on careful reading.
#  Section A — five 1-mark questions (5 marks total)
# Section A is five short questions , often labelled 1a, 1b, 1c, 1d, 1e.
Each is 1 mark. They mostly test:
# One-line definitions ("Define multicollinearity")
# One-line "why" answers ("Why use VIF?")
# Quick numerical readings of OLS output
# True/False with one-line justification
# What appeared in Section A across 8 papers
# Topic Times asked Papers
# LR Assumptions (LINER) 5 Mar21, Sample, Aug23, May25, Mar24
# Multicollinearity / VIF 4 Sample, Aug23, Mar24, (Nov24)
# Bias–Variance / Overfitting 4 Sample, Aug23, Mar24, May25
# Cross-Validation 3 Aug23, Mar24, May25
# Forward / Feature Selection 3 Aug23, Mar24, Feb25
# Regularization (Ridge/Lasso/EN) 4 Nov21 (×2), Feb25, May25
# Evaluation Metrics (R², RMSE, p-value) 5 Nov21 (×3), Feb25, May25
# Hyperparameter Tuning (Grid/Random/Bayes) 2 Feb25, (other)
# Numerical reading of regression coefficients 3 Mar21 (×3 — bwght, gpa, ceo)
# Pattern — almost every paper has at least one Section A from each of these three
buckets: (1) an assumption / theory question , (2) a multicollinearity or
overfitting question , (3) a numerical or metric question .
#  Section B — Q2 and Q3 (15 marks total)
# Q2 (8 marks) is almost always about DataFrame operations / pandas —
load data, drop columns, group-by, slice, head/tail, info, describe. You write small code
snippets or describe what each line does.
# Q3 (7 marks) is EDA — Exploratory Data Analysis : plot the data,
boxplots, pairplots, correlation heatmap, identify outliers, comment on skewness.
# Question Marks Almost always asks for…
# Q2 8 pandas operations on a CSV — read_csv, head, info, describe, drop, group-by, value_counts
# Q3 7 EDA — visualisations, missing values, outliers, comment on distribution
# Strategy: learn the 10 most common pandas one-liners (see File 20: Python Pipeline ) and you can answer Q2 confidently.
For Q3, remember the EDA recipe: SHAPE → HEAD → INFO → DESCRIBE → MISSING → BOX → CORR .
# Section C — Q4, Q5, Q6 (60 marks total — the bulk of the paper)
# Section C is where most marks live, and it has a very predictable structure.
# Question Marks Theme
# Q4 20–25 Pre-modelling pipeline : missing values, outliers, encoding, scaling, train/test split, multicollinearity check (VIF), feature transformations, feature selection
# Q5 20 OLS / linear regression model building : fit OLS, read summary, check assumptions, residual diagnostics, interpret coefficients
# Q6 20 Model comparison and tuning : build multiple models (Linear, Ridge, Lasso, ElasticNet, Polynomial), compare with R²/RMSE, hyperparameter tuning (GridSearch / RandomSearch / Bayesian), final business interpretation
# Q4 sub-parts that appear almost every paper
# 4a/4b/4c: read & describe data, handle missing values
# 4d/4e: outlier detection (IQR / boxplot / Z-score)
# 4f/4g: encoding categorical variables (one-hot, label, ordinal)
# 4h/4i: multicollinearity check using VIF, drop or transform
# 4j: feature scaling (StandardScaler / MinMaxScaler)
# 4k: train/test split
# Q5 sub-parts
# Fit OLS using statsmodels, print summary
# Identify significant variables (p-value < 0.05)
# Check assumptions: linearity, normality of residuals, homoscedasticity, independence
# Compute and interpret R², Adjusted R², F-statistic
# Residual plots — Q-Q plot, residuals vs fitted
# Q6 sub-parts
# Compare Linear vs Ridge vs Lasso vs ElasticNet
# Use cross-validation (k-fold, k=5 or 10) to evaluate
# Apply GridSearchCV / RandomizedSearchCV for tuning alpha
# Interpret final model in business terms
# The 70% rule — if you can confidently do Q4 (preprocessing) and Q5 (OLS + assumptions),
you have already secured 40+ marks out of 60 in Section C. That's the difference between failing and
a B grade.
# Topic frequency table — overall
# Across all 8 papers, all sections combined, here is how often each topic was tested:
# Rank Topic Approx times asked Total marks across papers
# 1 Pandas / DataFrame operations 8 (every paper) ~64 marks
# 2 OLS Regression + Summary interpretation 8 ~120 marks
# 3 Multicollinearity & VIF 7 ~30 marks
# 4 Assumptions of LR (LINER) 6 ~25 marks
# 5 Regularization (Ridge / Lasso / ElasticNet) 6 ~80 marks
# 6 Cross-validation 5 ~20 marks
# 7 EDA & data visualisations 8 ~56 marks
# 8 Bias-Variance / Overfitting 5 ~15 marks
# 9 Feature engineering / transformations 5 ~30 marks
# 10 Feature selection (Forward / RFE / Wrapper) 4 ~15 marks
# 11 Hyperparameter tuning (Grid/Random/Bayes) 4 ~30 marks
# 12 Evaluation metrics (R², RMSE, MAPE, MAE) 6 ~25 marks
# 13 Outlier detection (IQR / boxplot) 5 ~20 marks
# 14 Encoding (one-hot, label, ordinal) 5 ~20 marks
# 15 Numerical reading of regression coefficients 4 ~16 marks
# 16 Polynomial regression 3 ~15 marks
# 17 Gradient descent 2 ~5 marks
# The Hot-10 — concepts you must NOT skip
# If you have only a few days, master these ten topics. Together they cover ~80% of all marks.
# # Topic Why it's hot Where to study
# 1 OLS regression + statsmodels summary Q5 every paper, 20 marks; you must read p-values, R², coefficients File 02 , File 13
# 2 Multicollinearity & VIF 4f/4h/4i in Q4 every paper; also a 1-mark Section A File 08
# 3 LINER assumptions 1-mark Section A almost every paper + appears in Q5 File 07
# 4 Ridge / Lasso / Elastic Net 20 marks in Q6 every paper; 1-mark in Section A repeatedly File 10
# 5 Cross-validation (k-fold) Section A + appears in Q6 tuning File 11
# 6 Pandas one-liners Q2 every paper; 8 marks each File 20
# 7 EDA recipe Q3 every paper; 7 marks each File 20
# 8 Outlier handling + Encoding + Scaling Q4 every paper; 10–15 marks each File 15
# 9 R², Adjusted R², RMSE, p-value reading 1-mark and Section C interpretation File 12
# 10 Hyperparameter tuning (GridSearchCV) Q6 part of Section C File 16
# Hot-10 mnemonic — "OMLR-CPE-OEH":
# O LS · M ulticollinearity · L INER · R egularization · C V · P andas · E DA · O utliers/Encoding/Scaling · E valuation metrics · H yperparameters
#  Common traps that lose marks
# Several mistakes appear again and again in how students answer ESA questions. Avoid these and
you'll score noticeably higher with the same knowledge.
# Trap What goes wrong The fix
# Comparing RMSEs across different targets Says "model A is better because RMSE 55 < RMSE 12324" when the targets are age vs CTC RMSE has same units as target. Different targets → not comparable. Use %RMSE / mean target instead.
# Dummy-variable trap One-hot encodes a 3-level category and creates 3 columns → causes multicollinearity Always use drop_first=True in pd.get_dummies or drop="first" in OneHotEncoder
# Treating ordinal as nominal One-hot encodes "Low/Medium/High" instead of mapping 1/2/3 Use OrdinalEncoder when an order exists; one-hot when it doesn't
# Scaling before train/test split Fits scaler on full data → information leak from test set Split first, then fit_transform on train only, transform on test
# Imputing on whole dataset Same data leak as above Fit imputer on train only
# R² always means "good model" High R² on training is meaningless if test R² is much lower (overfit) Always report Adjusted R² and a held-out / CV score, not just train R²
# p-value > 0.05 means "no relationship" Says "x has no effect on y" Better: "with this data, we fail to reject H₀; we don't have evidence of a non-zero effect"
# Confusing VIF threshold Uses VIF > 0.05 (mixing it up with p-value) VIF > 5 is a warning, > 10 is serious. Range starts at 1, no upper limit.
# Ridge "selects features" Says Ridge does feature selection like Lasso Ridge shrinks coefficients toward zero but rarely to zero. Lasso can. Elastic Net does both.
# Forgetting to scale before Ridge/Lasso Penalty is dominated by features with large units (e.g. salary in lakhs vs age in years) Always StandardScale features before any regularised regression
# Using R² to compare different-sized feature sets R² always increases when you add features Use Adjusted R² or held-out RMSE for comparison
# "Linear regression assumes the data is linear" Vague phrasing It assumes a linear relationship between predictors and target , in the chosen form. You can include polynomial or log terms and still call it "linear regression".
# 3-day final revision plan
# If you have only 3 days before the ESA, here is a tight schedule:
# Morning: File 01 + File 02 + File 03
# Afternoon: File 07 (LINER) + File 08 (VIF) + File 09
# Evening: File 10 (Ridge/Lasso/EN) + File 11 + File 12
# Last hour: re-read File 18 Section-A questions only — do them on paper.
# Morning: File 17 — work through every numerical with pen on paper
# Afternoon: File 13 + File 14 + File 15 + File 16
# Evening: File 20 — write out the full pandas + sklearn pipeline 2 times from memory
# Morning: pick the latest paper () from File 18 and attempt it timed (3 hours)
# Afternoon: review answers, list weaknesses
# Night before: re-read File 21 (Cheatsheet) only — high-yield mnemonics, formulas, one-liners
# The night before — DO NOT learn anything new. Just re-read File 21 (cheatsheet),
sleep 7+ hours. Tired brains forget things faster than well-rested ones.

#==============================================================================
# TOPIC 20: Python Pipeline
#==============================================================================

# Step 0 — Imports
# Step 1 — Load data (Q2)
# Step 2 — EDA (Q3)
# Step 3 — Missing values (Q4)
# Step 4 — Outlier handling (Q4)
# Step 5 — Encoding (Q4)
# Step 6 — Scaling (Q4)
# Step 7 — Train/test split (Q4)
# Step 8 — Multicollinearity / VIF (Q4)
# Step 9 — Feature selection (Q4)
# Step 10 — OLS / statsmodels (Q5)
# Step 11 — Assumption checks (Q5)
# Step 12 — Model comparison (Q6)
# Step 13 — Hyperparameter tuning (Q6)
# Step 14 — Final interpretation (Q6)
# Quick snippets cheatsheet
# How to use this file
# This is the full pipeline for any regression Section C question. The order
matches how Q4 → Q5 → Q6 are structured in the ESA. You can literally read this top-to-bottom
during the exam and answer most questions.
# Every section has:
# What this step does (one paragraph in plain English)
# The code with comments on every line
# What the output looks like
# How to read it for the exam
# Memorize the order, not the syntax. If you remember the 14 steps in sequence,
you'll never blank during a Section C question. The exact pandas function name can be looked up.
# Step 0 — Imports (always at the top)
# Standard imports for every regression task. Memorize these — they appear in every Section C answer.
# # Data handling import pandas as pd import numpy as np # Visualization import matplotlib.pyplot as plt import seaborn as sns # sklearn — preprocessing from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV, RandomizedSearchCV from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, OrdinalEncoder from sklearn.impute import SimpleImputer # sklearn — models from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet from sklearn.preprocessing import PolynomialFeatures from sklearn.feature_selection import RFE, SequentialFeatureSelector # sklearn — metrics from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_absolute_percentage_error # statsmodels for OLS summary tables import statsmodels.api as sm from statsmodels.stats.outliers_influence import variance_inflation_factor # Set figure defaults plt.rcParams[ "figure.figsize" ] = ( 8 , 5 )
sns.set_style( "whitegrid" )
# Step 1 — Load data (Q2 territory)
# Goal: read the CSV, get a feel for size and types, look at a few rows.
This is exactly what Q2 (8 marks) tests.
# EDA recipe (Q3, 7 marks) — the standard 7-step exploratory approach is SHAPE → HEAD → INFO → DESCRIBE → MISSING → BOX → CORR .
# Step 2 — Exploratory Data Analysis (Q3, 7 marks)
# Goal: visually understand the data. Find skewness, outliers, relationships.
# # Histogram for one feature — see the distribution shape df[ "price" ].hist(bins= 30 )
plt.title( "Distribution of Price" )
plt.xlabel( "Price" ); plt.ylabel( "Frequency" )
plt.show() # All numeric features at once df.hist(bins= 30 , figsize=( 12 , 8 ))
plt.tight_layout(); plt.show() # Boxplot — see outliers and quartiles sns.boxplot(x=df[ "price" ])
plt.show() # Pairplot — relationships between every pair (use only when small # of features) sns.pairplot(df[[ "price" , "area" , "bedrooms" , "bathrooms" ]])
plt.show() # Correlation heatmap — find multicollinearity hints + relationships with target corr = df.corr(numeric_only= True )
sns.heatmap(corr, annot= True , cmap= "coolwarm" , fmt= ".2f" )
plt.show() # Scatter — relationship between one feature and target sns.scatterplot(x= "area" , y= "price" , data=df)
plt.show() # Skewness — is the column heavily skewed (> 1 or < -1 is a flag)? df[ "price" ].skew() # Count of categorical values sns.countplot(x= "city" , data=df); plt.xticks(rotation= 45 ); plt.show()
# Step 3 — Missing values (Q4 sub-part)
# Goal: find missing entries and decide how to handle them.
# Trap: if you fill missing values before train/test split, you leak info
from the test set into the train set. Always split first, then impute on train, then apply the
same imputer to test.
# Step 4 — Outlier detection & treatment (Q4 sub-part)
# Goal: find rows whose values lie way outside the normal range. Decide whether
to drop, cap, or transform.
# # Method 1: IQR (Interquartile Range) — most common for ESA Q1 = df[ "price" ].quantile( 0.25 )
Q3 = df[ "price" ].quantile( 0.75 )
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR # Boolean mask of outliers mask_outlier = (df[ "price" ] < lower) | (df[ "price" ] > upper)
print( "Outlier count:" , mask_outlier.sum()) # Strategy A: drop them df_no_out = df[~mask_outlier] # Strategy B: cap (winsorize) — keep the row but clip extreme value df[ "price" ] = df[ "price" ].clip(lower=lower, upper=upper) # Method 2: Z-score (assumes near-normal distribution) from scipy.stats import zscore
z = np.abs(zscore(df[ "price" ]))
mask = z > 3 # > 3 sigma # Method 3: just look — boxplot sns.boxplot(x=df[ "price" ])
#  Step 5 — Encoding categoricals (Q4 sub-part)
# Goal: ML models need numbers. Convert text categories into numeric form.
# # A) One-hot encoding — for nominal (no order) categories # IMPORTANT: drop_first=True avoids the dummy variable trap df = pd.get_dummies(df, columns=[ "city" , "furnishing" ], drop_first= True , dtype= int ) # sklearn version (preferred in pipelines) ohe = OneHotEncoder(drop= "first" , sparse_output= False )
encoded = ohe.fit_transform(df[[ "city" ]]) # B) Ordinal encoding — when categories have a natural order (Low < Medium < High) order = [[ "Low" , "Medium" , "High" ]]
oe = OrdinalEncoder(categories=order)
df[ "quality_enc" ] = oe.fit_transform(df[[ "quality" ]]) # C) Manual mapping (when you know the levels) mp = {{ "yes" : 1 , "no" : 0 }}
df[ "has_garage" ] = df[ "has_garage" ].map(mp) # D) Label encoding — typically for the target column only from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df[ "target_enc" ] = le.fit_transform(df[ "target" ])
# Trap (dummy-variable trap): if a category has k levels and you create k dummies, they sum to 1 → perfect multicollinearity. Always drop one level.
#  Step 6 — Feature scaling (Q4 sub-part)
# Goal: bring all features onto a comparable range. Required before
Ridge/Lasso/ElasticNet, KNN, gradient descent. Not strictly required for plain OLS.
# # StandardScaler — mean 0, std 1 (most common) scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train) # fit only on TRAIN X_test_sc = scaler.transform(X_test) # reuse same scaler on TEST # MinMaxScaler — squeeze into [0, 1] mm = MinMaxScaler()
X_train_mm = mm.fit_transform(X_train)
X_test_mm = mm.transform(X_test)
# Order matters! Always: (1) split → (2) fit scaler on train → (3) transform train,
(4) transform test. Never fit_transform on test data.
#  Step 7 — Train/test split (Q4 sub-part)
# X = df.drop(columns=[ "price" ]) # features y = df[ "price" ] # target X_train, X_test, y_train, y_test = train_test_split( X, y, test_size= 0.2 , # 80% train / 20% test random_state= 42 # reproducibility — same split every time ) print(X_train.shape, X_test.shape)
# Step 8 — Multicollinearity / VIF (Q4 sub-part)
# Goal: detect features that are too correlated with each other.
VIF > 5 is a warning, > 10 is serious. Drop or combine those features.
# # Add a constant column (statsmodels needs it) X_const = sm.add_constant(X_train) # Compute VIF for each column vif = pd.DataFrame()
vif[ "feature" ] = X_const.columns
vif[ "VIF" ] = [variance_inflation_factor(X_const.values, i) for i in range(X_const.shape[ 1 ])]
print(vif.sort_values( "VIF" , ascending= False )) # Strategy: drop the column with highest VIF, recompute, repeat until all < 5 X_train = X_train.drop(columns=[ "highest_vif_col" ])
# How to read the output:
# VIF value Meaning
# 1 No correlation with other predictors
# 1–5 Moderate, usually OK
# 5–10 High — investigate / drop
# > 10 Serious multicollinearity — drop
# Step 9 — Feature selection (Q4 sub-part)
# # A) Forward Selection — add one variable at a time sfs = SequentialFeatureSelector( LinearRegression(), n_features_to_select= 5 , direction= "forward" , scoring= "r2" , cv= 5 )
sfs.fit(X_train, y_train)
selected = X_train.columns[sfs.get_support()].tolist() # B) Backward Elimination — start with all, drop the worst at each step sfs_b = SequentialFeatureSelector( LinearRegression(), n_features_to_select= 5 , direction= "backward" , scoring= "r2" , cv= 5 ) # C) RFE — Recursive Feature Elimination rfe = RFE(LinearRegression(), n_features_to_select= 5 )
rfe.fit(X_train, y_train)
selected_rfe = X_train.columns[rfe.support_].tolist() # D) Filter — correlation with target corr_with_target = X_train.corrwith(y_train).abs().sort_values(ascending= False )
# Step 10 — OLS / statsmodels (Q5, 20 marks!)
# This is the most important step in Section C. The summary table is the source
of half the marks in Q5.
# # statsmodels — gives you a full summary table X_const = sm.add_constant(X_train) # add intercept column model = sm.OLS(y_train, X_const).fit()
print(model.summary()) # Pull out individual values model.params # coefficients model.pvalues # p-values model.rsquared # R² model.rsquared_adj # Adjusted R² model.fvalue # F-statistic model.f_pvalue # p-value of F-statistic # Predict on test X_test_const = sm.add_constant(X_test)
y_pred = model.predict(X_test_const)
# How to read the OLS summary table (this is gold for the exam)
# Field Means What's "good"
# R-squared % of variance in y explained Higher is better; 0–1
# Adj. R-squared R² penalised for #features Use this when comparing models with different feature counts
# F-statistic / Prob (F) Joint significance of all predictors Prob < 0.05 → at least one predictor matters
# coef How much y changes per unit increase in x Sign and magnitude tell direction and strength
# std err Uncertainty around the coefficient Smaller is better
# t coef / std err |t| > 2 ≈ significant
# P>|t| p-value of that coefficient < 0.05 → significant
# [0.025, 0.975] 95% confidence interval for the coef Doesn't include 0 → significant
# Durbin-Watson Autocorrelation in residuals ~ 2 ideal; < 1.5 or > 2.5 = trouble
# Jarque-Bera (JB) Normality of residuals Prob > 0.05 → residuals look normal
# Cond. No. Multicollinearity indicator > 30 = warning
# Step 11 — Assumption checks (Q5 sub-part)
# # Residuals (errors) resid = model.resid
fitted = model.fittedvalues # 1. Linearity & Homoscedasticity — residuals vs fitted should look random plt.scatter(fitted, resid, alpha= 0.5 )
plt.axhline( 0 , color= "red" , linestyle= "--" )
plt.xlabel( "Fitted" ); plt.ylabel( "Residuals" )
plt.title( "Residuals vs Fitted" )
plt.show() # 2. Normality — Q-Q plot sm.qqplot(resid, line= "45" )
plt.title( "Q-Q Plot" ); plt.show() # Statistical normality test — Shapiro-Wilk from scipy.stats import shapiro
stat, p = shapiro(resid) # p > 0.05 → residuals look normal # 3. Homoscedasticity formal test — Breusch-Pagan from statsmodels.stats.diagnostic import het_breuschpagan
bp = het_breuschpagan(resid, X_const) # bp[1] is the p-value; > 0.05 → no heteroscedasticity # 4. Independence — Durbin-Watson from statsmodels.stats.stattools import durbin_watson
dw = durbin_watson(resid) # dw ≈ 2 → no autocorrelation
# Step 12 — Model comparison (Q6 part)
# Goal: build several models, compare them with the same metric, pick the best.
# # 1. Linear Regression — baseline lr = LinearRegression().fit(X_train_sc, y_train)
pred_lr = lr.predict(X_test_sc) # 2. Ridge — L2 penalty ridge = Ridge(alpha= 1.0 ).fit(X_train_sc, y_train)
pred_ridge = ridge.predict(X_test_sc) # 3. Lasso — L1 penalty (does feature selection) lasso = Lasso(alpha= 0.1 ).fit(X_train_sc, y_train)
pred_lasso = lasso.predict(X_test_sc) # 4. ElasticNet — mix of L1 and L2 en = ElasticNet(alpha= 0.1 , l1_ratio= 0.5 ).fit(X_train_sc, y_train)
pred_en = en.predict(X_test_sc) # 5. Polynomial — for non-linear patterns poly = PolynomialFeatures(degree= 2 , include_bias= False )
X_train_poly = poly.fit_transform(X_train_sc)
X_test_poly = poly.transform(X_test_sc)
poly_lr = LinearRegression().fit(X_train_poly, y_train)
pred_poly = poly_lr.predict(X_test_poly) # Compare def evaluate(y_true, y_pred, name): print(f "{{name}}" ) print(f " R² : {{r2_score(y_true, y_pred):.4f}}" ) print(f " RMSE : {{np.sqrt(mean_squared_error(y_true, y_pred)):.2f}}" ) print(f " MAE : {{mean_absolute_error(y_true, y_pred):.2f}}" ) print() evaluate(y_test, pred_lr, "Linear" )
evaluate(y_test, pred_ridge, "Ridge" )
evaluate(y_test, pred_lasso, "Lasso" )
evaluate(y_test, pred_en, "ElasticNet" )
evaluate(y_test, pred_poly, "Polynomial-2" )
#  Step 13 — Hyperparameter tuning (Q6 part)
# # A) GridSearchCV — exhaustive search over a grid param_grid = {{ "alpha" : [ 0.001 , 0.01 , 0.1 , 1 , 10 , 100 ]}}
grid = GridSearchCV(Ridge(), param_grid, cv= 5 , scoring= "neg_mean_squared_error" )
grid.fit(X_train_sc, y_train)
print( "Best alpha:" , grid.best_params_)
print( "Best CV RMSE:" , np.sqrt(-grid.best_score_))
best_ridge = grid.best_estimator_ # B) RandomizedSearchCV — random sample of the grid (faster for big grids) from scipy.stats import uniform
rs = RandomizedSearchCV( ElasticNet(), {{ "alpha" : uniform( 0.001 , 10 ), "l1_ratio" : uniform( 0 , 1 )}}, n_iter= 50 , cv= 5 , scoring= "r2" , random_state= 42 )
rs.fit(X_train_sc, y_train)
print( "Best params:" , rs.best_params_) # C) Bayesian Search — smart, builds a probabilistic model of the search space # pip install scikit-optimize from skopt import BayesSearchCV
bayes = BayesSearchCV( Ridge(), {{ "alpha" : ( 1e-3 , 1e2 , "log-uniform" )}}, n_iter= 30 , cv= 5 )
bayes.fit(X_train_sc, y_train)
# Step 14 — Final business interpretation (Q6 part)
# The last sub-part of Q6 typically asks for business interpretation . Use this template:
# Template answer (adapt to the dataset):
# State the chosen model and its CV-RMSE / R² on the test set.
# Pick the 2–3 features with the largest standardised coefficients. State the direction (sign).
# Translate the coefficient into a one-sentence business statement : "A 1-unit increase in area is associated with an expected X change in price, holding other features constant."
# Mention which features the model dropped (if Lasso) or de-emphasised (Ridge) — these are
candidates the business can de-prioritise.
# State a caveat: "These are associations under the LR assumptions; not causal claims."
# # Save coefficients with feature names for interpretation coef_df = pd.DataFrame({{ "feature" : X_train.columns, "coef" : best_ridge.coef_
}}).sort_values( "coef" , key=abs, ascending= False )
print(coef_df.head( 10 ))
# Quick snippets cheatsheet
# Pandas one-liners
# df.shape # (rows, cols) df.head(); df.tail(); df.sample( 5 )
df.info(); df.describe()
df.isnull().sum() # missing per col df.dropna(); df.fillna( 0 )
df[ "col" ].mean(), .median(), .std(), .skew()
df.groupby( "city" )[ "price" ].mean()
df[ "city" ].value_counts()
df.corr(numeric_only= True )
df.sort_values( "price" , ascending= False )
df.drop(columns=[ "id" ])
df.rename(columns={{ "old" : "new" }})
pd.get_dummies(df, drop_first= True )
# Numpy quick
# np.mean(arr); np.median(arr); np.std(arr)
np.sqrt(x); np.log(x); np.log1p(x)
np.where(cond, a, b)
np.percentile(arr, [ 25 , 50 , 75 ])
# Sklearn essentials
# # Fit pattern is the SAME for every estimator model = SomeEstimator(...)
model.fit(X_train, y_train)
preds = model.predict(X_test)
score = model.score(X_test, y_test) # CV one-liner scores = cross_val_score(LinearRegression(), X, y, cv= 5 , scoring= "r2" )
print( "Mean R²:" , scores.mean(), "+/-" , scores.std())
# Metrics one-liners
# r2_score(y_true, y_pred)
mean_squared_error(y_true, y_pred)
np.sqrt(mean_squared_error(y_true, y_pred)) # RMSE mean_absolute_error(y_true, y_pred)
mean_absolute_percentage_error(y_true, y_pred)
# Full pipeline in one go (paste-and-go)
# If a Section C question says "build a complete regression pipeline for this dataset", here is the full skeleton in 50 lines:
# You can quote-paste this 50-line skeleton in any Section C answer that says
"build a regression model end-to-end". Adjust the column names and you have all 60 marks of
Section C in front of you.

#==============================================================================
# TOPIC 21: Cheatsheet and Mnemonics
#==============================================================================

# Mnemonics master list
# Every formula on one page
# Concept one-liners
# Model one-liners
# When to use what
# Red-flag values to memorize
#  Common traps
# How to read OLS / numbers
#  Pipeline steps you must remember
# Answer templates
# Mnemonics master list
# Mnemonic Stands for Used in
# LINER L inearity · I ndependence · N ormality of residuals · E qual variance (homoscedasticity) · R esiduals uncorrelated with predictors (≈ no multicollinearity) 5 assumptions of Linear Regression
# LECESSTE L oad · E DA · C lean · E ncode · S cale · S plit · T rain · E valuate ML pipeline steps
# SHID-BC S hape · H ead · I nfo · D escribe · B oxplot · C orrelation EDA recipe (Q3, 7 marks)
# R-MAE-MAPE-MSE-RMSE R² · MAE · MAPE · MSE · RMSE Five regression metrics (in increasing penalty for big errors)
# OMLR-CPE-OEH O LS · M ulticollinearity · L INER · R egularization · C V · P andas · E DA · O utliers · E ncoding · H yperparameters Hot-10 exam topics
# "Lasso = Less" "Ridge = Reduce" Lasso eliminates features (coefs to zero), Ridge reduces them but keeps all Telling Lasso vs Ridge apart
# "VIF over 5? Drive feature alive." (i.e. drop it) VIF > 5 → warning, > 10 → drop Multicollinearity threshold
# "R² always grows; Adj R² won't snow" R² never decreases when you add features; Adj R² can Comparing models with different #features
# "Bias is big-picture wrong; Variance is bouncy along" High bias = model too simple (consistently off); high variance = model too complex (jumps with data) Bias-variance tradeoff
# "Train low, test high → overfit cry" Training error tiny but test error big = overfitting Diagnosing overfit vs underfit
# "DROP-first to avoid the trap" Use drop_first=True in get_dummies to avoid dummy-variable trap One-hot encoding
# "Split-Fit-Transform" Split first, fit scaler/imputer on train, transform test Avoiding data leakage
# "DW close to 2 → independence is true" Durbin-Watson ≈ 2 means no autocorrelation Reading OLS summary
# "p < 0.05 → keep alive" p-value < 0.05 → coefficient significant, keep variable Reading OLS summary
# "Grid is greedy, Random is rapid, Bayes is brainy" GridSearch tries everything (slow), RandomSearch samples (faster), Bayesian models the search space (smartest) Hyperparameter tuning methods
# "K-fold shuffles trust" k-fold CV gives a more trustworthy estimate than a single train/test split Why use cross-validation
# Every formula on one page
# Regression form
# Simple LR: y = β₀ + β₁x + ε
# Multiple LR: y = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ + ε
# Polynomial: y = β₀ + β₁x + β₂x² + ... + βₖxᵏ + ε
# Matrix form: Y = Xβ + ε
# OLS estimation
# Normal equation: β̂ = (XᵀX)⁻¹Xᵀy
# Slope (SLR): β₁ = Σ(xᵢ−x̄)(yᵢ−ȳ) / Σ(xᵢ−x̄)²
# Intercept (SLR): β₀ = ȳ − β₁x̄
# Cost functions
# MSE: (1/n) · Σ(yᵢ − ŷᵢ)²
# RMSE: √MSE — same units as the target
# MAE: (1/n) · Σ|yᵢ − ŷᵢ|
# MAPE: (100/n) · Σ|yᵢ − ŷᵢ| / |yᵢ|
# Evaluation
# R²: 1 − (SS res / SS tot ) = 1 − (Σ(y−ŷ)² / Σ(y−ȳ)²)
# Adjusted R²: 1 − [(1−R²)(n−1) / (n−p−1)]
# where n = #samples, p = #predictors
# Gradient descent
# Update rule: β j := β j − α · ∂J/∂β j
# α = learning rate
# Regularization (with shrinkage penalty)
# Ridge (L2): minimize Σ(y − ŷ)² + λ·Σβⱼ²
# Lasso (L1): minimize Σ(y − ŷ)² + λ·Σ|βⱼ|
# ElasticNet: minimize Σ(y − ŷ)² + λ·[α·Σ|βⱼ| + (1−α)·Σβⱼ²]
# Multicollinearity
# VIF for feature j: VIF j = 1 / (1 − R j ²)
# where R j ² = R² of regressing x j on all other predictors
# Tolerance: 1 / VIF (alternative form)
# Inference
# t-statistic: t = β̂ / SE(β̂)
# F-statistic: F = [(SS tot − SS res )/p] / [SS res /(n−p−1)]
# 95% CI for coef: β̂ ± 1.96·SE(β̂) (large n)
# Bias-Variance from cross-validation
# Operational bias: 1 − mean(R² across folds)
# Operational variance: std(R² across folds)
# Train/test split & CV
# k-fold CV: split into k parts; train on k−1, test on 1; rotate; average score
# Concept one-liners
# Concept One-line definition
# Supervised learning Learning a function from input → output using labeled data.
# Regression Supervised learning where the target is continuous (e.g. price, salary).
# Linear regression Fit a straight line (or hyperplane) that minimises sum of squared residuals.
# OLS Ordinary Least Squares — the classic method that gives a closed-form β̂ = (XᵀX)⁻¹Xᵀy.
# Polynomial regression Linear regression on polynomial-transformed features; still linear in coefficients.
# Cost function Number that measures how wrong the model's predictions are; we minimise it.
# MSE Average squared error — penalises big mistakes more.
# RMSE Square root of MSE — same units as the target, easier to interpret.
# MAE Average absolute error — robust to outliers, easier to read.
# R² Proportion of variance in y explained by the model. 1 = perfect, 0 = useless.
# Adjusted R² R² penalised for adding more predictors. Use this to compare different-sized models.
# Residual y true − y pred . The error the model makes on each point.
# Gradient descent Iteratively update parameters in the direction that reduces the cost.
# Learning rate (α) Step size in gradient descent. Too big → diverge; too small → slow.
# Linearity Relationship between predictors and target is approximately a straight line.
# Independence (of errors) Errors at different observations are uncorrelated.
# Normality (of residuals) Residuals follow a normal (bell-curve) distribution.
# Homoscedasticity Variance of residuals is constant across all fitted values.
# Heteroscedasticity Variance of residuals changes with fitted value (funnel shape).
# Multicollinearity Two or more predictors are highly correlated; coefficients become unstable.
# VIF Variance Inflation Factor — measures how much a coefficient variance is inflated by multicollinearity.
# Underfitting (high bias) Model too simple; misses the pattern. Train and test error both high.
# Overfitting (high variance) Model too complex; memorises noise. Train low, test high.
# Bias-variance tradeoff Reducing one tends to raise the other; we seek the sweet spot.
# Regularization Add a penalty on coefficient size to fight overfitting.
# Ridge (L2) Penalty = λ·Σβ². Shrinks coefficients toward zero but keeps them all.
# Lasso (L1) Penalty = λ·Σ|β|. Can shrink coefficients exactly to zero → does feature selection.
# ElasticNet Mix of L1 and L2; useful when many features are correlated.
# α (alpha) in Ridge/Lasso Strength of penalty. α = 0 → no penalty. Higher α → more shrinkage.
# Cross-validation Split data into k folds; train on k−1, test on 1; rotate; average.
# Hyperparameter A parameter you set before training (like alpha or k) — not learned.
# Q-Q plot Plot of residual quantiles vs theoretical normal quantiles. Straight line → normal.
# p-value Probability of seeing such a result if the true coefficient were 0. < 0.05 → significant.
# Feature engineering Transforming or creating features (log, polynomial, interaction) to help the model.
# Feature selection Picking the most useful subset of features (forward, backward, RFE).
# StandardScaler Subtract mean, divide by std. Brings each feature to mean 0, std 1.
# One-hot encoding Convert a k-level category into k−1 binary columns (drop one level).
# Dummy-variable trap Keeping all k dummies → perfect multicollinearity with the intercept.
# Model one-liners — when each shines
# Model Best for Watch out for
# Linear Regression (OLS) Interpretable baseline; small to medium n; LINER assumptions roughly hold Multicollinearity, non-linearity
# Ridge Many correlated features; you want to keep all features in the model Doesn't do feature selection
# Lasso Many features, suspect most are useless; want a sparse model Among correlated features it picks one randomly
# ElasticNet Many correlated features AND want some selection Two hyperparameters (alpha, l1_ratio)
# Polynomial Regression Clearly non-linear pattern; one or two key features Easy to overfit at high degree; explodes feature count
# When to use what — quick decisions
# Situation What to use
# Continuous target (price, salary) Regression
# Categorical target (yes/no, class) Classification (out of scope for this exam)
# Many features, > 100, suspect lots of irrelevant ones Lasso
# Many correlated features, want them all Ridge
# Mixed — many correlated, also want sparsity ElasticNet
# Visible curved pattern Polynomial regression
# Compare 2 models with different #features Adjusted R² (not R²)
# Compare 2 models predicting same target RMSE / MAE / R² on test set
# Compare 2 models predicting different targets (e.g. age vs CTC) Cannot compare RMSE directly. Use %RMSE / mean target, or R².
# Outliers heavily affect results MAE (more robust than MSE/RMSE)
# Errors of large magnitude must be punished MSE / RMSE
# Need to interpret coefficients statsmodels OLS (gives full summary)
# Need to predict only sklearn LinearRegression / Ridge / Lasso
# Small dataset (n < 100) k-fold CV with k=5; avoid deep models
# Want robust estimate of generalisation Cross-validation, not single train/test split
# Tuning 1–2 hyperparameters with small ranges GridSearchCV
# Tuning many hyperparameters or large ranges RandomizedSearchCV / Bayesian
# Heavy-tailed target distribution Try log(y) transformation
# Funnel-shaped residuals Heteroscedasticity → log-transform y or use weighted LS
# Red-flag values to memorize
# Quantity Healthy Warning Action
# p-value < 0.05 0.05 – 0.10 > 0.05 → not significant
# VIF 1 – 5 5 – 10 > 10 → drop / combine feature
# Durbin-Watson 1.5 – 2.5 (≈2) 1.0 – 1.5 or 2.5 – 3.0 < 1 or > 3 → autocorrelation
# R² Higher (context dependent) — Always pair with Adjusted R²
# Skewness −1 to 1 ±1 to ±2 Beyond ±2 → consider log/Box-Cox
# Condition number (in OLS) < 30 30 – 100 > 100 → severe multicollinearity
# Train R² vs Test R² Close Test ~ 5–10% lower Big gap → overfitting
# k for k-fold CV 5 or 10 — Standard choices; avoid k=2
# α (Ridge/Lasso) Tuned via CV — Try {0.001, 0.01, 0.1, 1, 10, 100}
# Test set size 20–30% — Below 10% → unreliable estimates
#  Common traps
# Don't compare RMSE across different targets. RMSE has the units of the target. RMSE 55 (age in years) is not better than RMSE 12,324 (CTC in ). Use %RMSE relative to mean(y), or use R².
# Always drop_first=True for one-hot. Otherwise you get the dummy-variable trap (perfect multicollinearity).
# Scale and impute on TRAIN only. Splitting after scaling/imputing leaks info from test → over-optimistic scores.
# Ridge does not do feature selection. It shrinks coefficients toward zero but rarely to zero. Lasso can. Elastic Net does both.
# Regularised models need scaled features. Without scaling, the penalty unfairly punishes features measured on larger scales (e.g., salary in lakhs vs age in years).
# R² always increases with more features. So R² is bad for comparing models with different numbers of predictors. Use Adjusted R² or held-out RMSE.
# "Linear" in Linear Regression refers to the coefficients, not x. y = β₀ + β₁x + β₂x² is still called "linear regression" (linear in β).
# p-value > 0.05 ≠ "no relationship". It means we don't have enough evidence to reject the null. Underpowered samples can hide real effects.
# VIF threshold is 5/10, not 0.05. Don't confuse VIF with p-value.
# k-fold CV with shuffle is essential when the data is ordered (e.g. by date or by class). Otherwise folds become biased.
# GridSearchCV's best_score_ is on the validation folds, not the held-out test set. Always score the final tuned model on a separate test set.
# Feature scaling does not change the fit of plain OLS. The coefficients change but R²/RMSE don't. Scaling matters for Ridge/Lasso/EN/SGD.
# Don't use only training error to choose models. Always evaluate on held-out data or via cross-validation.
# Outlier removal must be justified. "Just delete points outside 1.5·IQR" can throw away genuine signal. Investigate first.
# Imputing with mean for skewed data is a bad idea. Use median for skewed numeric columns; mode for categorical.
# How to read OLS / numbers in 60 seconds
# Reading a coefficient
# If area has coefficient +125.3 and y is price () :
# "Holding all other features constant, a one-unit increase in area is associated with an
expected increase of 125.3 in price."
# Reading a p-value
# p = 0.02 (less than 0.05): "reject the null hypothesis that this coefficient is zero — the
variable is statistically significant at the 5% level."
# p = 0.30 (more than 0.05): "fail to reject the null — we don't have enough evidence to claim
this variable has a non-zero effect."
# Reading R²
# R² = 0.78: "about 78% of the variance in y is explained by this model."
# Reading Adjusted R²
# If R² = 0.81 but Adj R² = 0.62 → many features added with little real value.
# Closer Adj R² to R² → features are pulling their weight.
# Reading the F-statistic
# Prob(F) < 0.05 → at least one predictor is significant. Prob(F) > 0.05 → none are; the model
overall is no better than just predicting the mean of y.
# Reading VIF
# VIF = 8.4 for x : "the variance of x's coefficient is inflated 8.4× compared to a
no-multicollinearity scenario. Strong multicollinearity — investigate or drop."
# Reading log-coefficients
# If model is log(salary) = α + β·log(sales) and β = 0.28:
# "a 1% increase in sales is associated with a 0.28% increase in salary."
# If model is log(salary) = α + β·roe and β = 0.0174:
# "a 1-unit increase in roe is associated with a (approximately) 1.74% increase in salary."
#  Pipeline steps you must remember (LECESSTE)
# L oad — pd.read_csv → df.shape, df.head, df.info, df.describe
# E DA — histograms, boxplots, pairplot, correlation heatmap
# C lean — handle missing (drop / median / mode), handle outliers (IQR / clip)
# E ncode — one-hot for nominal (drop_first=True), ordinal for ordered, label for target
# S cale — StandardScaler (fit on train only)
# S plit — train_test_split (test_size=0.2, random_state=42)
# T rain — fit model(s); compare Linear / Ridge / Lasso / EN / Polynomial; tune via CV
# E valuate — R², Adjusted R², RMSE, MAE; residual plots; assumption checks
# Answer templates for common ESA prompts
# Template 1 — "Define X and explain why it is used"
# Definition: X is <one sentence>.
# Why used: It addresses <problem> by <mechanism>.
# Example: e.g. predicting house prices, X helps because...
# Caveat: X assumes / can fail when ...
# Template 2 — "Differentiate between A and B"
# Two-column comparison covering: definition · math form · effect on coefficients · feature
selection? · scaling required? · best for
# Template 3 — "Comment on this OLS summary"
# Fit quality: R² = X, Adj R² = Y → model explains X% of variance.
# Joint significance: Prob(F) = Z → at least one predictor significant.
# Significant variables: <list features with p < 0.05> with sign and rough magnitude.
# Insignificant variables: <list with p > 0.05> — candidates to drop.
# Diagnostics: DW = ?, JB p-value = ?, Cond. No. = ? — flag any concerns.
# Business read: One sentence translating the biggest coefficient into plain English.
# Template 4 — "Build a regression model end-to-end"
# 1. Load + EDA (head, info, describe, corr heatmap).
# 2. Handle missing (median for numeric, mode for categorical).
# 3. Outlier check (IQR; cap or drop).
# 4. Encode categoricals (get_dummies, drop_first=True).
# 5. Train/test split (test_size=0.2, random_state=42).
# 6. Scale (StandardScaler, fit on train).
# 7. Check VIF; drop features with VIF > 10.
# 8. Fit OLS; read summary; check assumptions via residuals + Q-Q.
# 9. Compare Linear / Ridge / Lasso / EN with 5-fold CV.
# 10. GridSearchCV to tune the chosen model's α.
# 11. Report final test R², RMSE, MAE.
# 12. Interpret top 3 coefficients in business terms.
# Template 5 — "How would you handle multicollinearity?"
# 1. Detect: pairwise correlations + VIF (> 5 warning, > 10 serious).
# 2. Diagnose: identify the offending pair / cluster.
# 3. Fix:
# Drop one of the highly-correlated pair
# Combine: average or PCA the cluster
# Use Ridge regression — handles multicollinearity gracefully
# Re-collect data if a structural duplicate exists
# 4. Verify: recompute VIF; ensure all < 5.
# Template 6 — "Detect and treat overfitting"
# Detect: training R² >> test R² (or low CV score with high variance across folds).
# Treat:
# Add regularization (Ridge / Lasso)
# Reduce model complexity (lower polynomial degree)
# Reduce feature count (Lasso, RFE, forward selection)
# Get more training data
# Use cross-validation for honest evaluation
# The night-before mantra
# LINER — five LR assumptions.
# VIF > 10 = drop ; alpha tuned by CV; scale before regularizing.
# Lasso = Less features; Ridge = Reduce sizes; ElasticNet = both.
# R² always grows; Adj R² wins for fair comparisons.
# RMSE only compares same target; otherwise use R².
# Bias = simple-wrong; Variance = bouncy.
# p < 0.05 → keep alive; DW ≈ 2 → independence true.
# Split → fit → transform. No leakage.
# LECESSTE — full pipeline order.
# Q4 = Preprocess. Q5 = OLS. Q6 = Compare + tune.
# Read this list once before sleep. Sleep 7+ hours. You're ready.
# All the best, Rajesh!
# ← Previous 20. Python Pipeline
