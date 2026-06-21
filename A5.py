# ==============================================================================
# TOPIC 14: Feature Engineering and Selection
# ==============================================================================

"""
Engineering vs Selection
Engineering techniques
Selection methods
Feature Engineering vs Feature Selection
Term
Goal
Feature Engineering
Create new, more informative features
log-transform, polynomial features, interaction terms, datetime parts
Feature Selection
Pick the most useful features from existing ones
Forward selection, RFE, Lasso, VIF-based dropping
Feature Engineering techniques
1. Log Transformation
Use when: y or a feature is right-skewed (lots of small values, few huge ones — common in prices, salaries, counts).
Effect: compresses the range, makes the distribution more symmetric / closer to normal, often makes a non-linear relationship more linear.
2. Box-Cox / Yeo-Johnson Transformation
Generalization of log: tries to find the best power transformation. Box-Cox needs y > 0; Yeo-Johnson works for any y.
3. Polynomial Features & Interactions
Add x², x·z, x³ etc. to capture non-linear and interaction effects.
4. Binning / Discretization
Convert a continuous feature into bins (e.g., age → "young/middle/senior"). Useful when relationship is non-monotonic.
5. Datetime feature extraction
From a single datetime column, extract: year, month, day, day-of-week, hour, is_weekend, days_since_event. Hugely useful for time-aware predictions (e.g., metro traffic in Nov 2021 paper).
Feature Selection methods
Method family
How it picks features
Filter methods
Correlation, VIF, mutual information, ANOVA F-test
Score features in isolation; doesn't use the model
Wrapper methods
Forward, Backward, Recursive Feature Elimination (RFE)
Try subsets, score with the actual model
Embedded methods
Lasso, ElasticNet, Tree feature importance
Selection happens during model training
Forward Selection (Wrapper)
Start with no features.
For each remaining feature, fit a model with the current set + that feature; record the score (R², Adj R², or AIC).
Add the single feature that improved the score the most.
Stop when no further addition improves the score.
Backward Elimination (Wrapper)
Start with all features.
Fit the model. Find the feature with the highest p-value (or smallest contribution).
Remove that feature if its p-value > 0.05 (or threshold).
Repeat until all remaining features are significant.
Recursive Feature Elimination (RFE)
Train a model with all features.
Rank features by importance (e.g., absolute coefficient size or feature_importance_).
Remove the least important feature.
Repeat until a target number of features remains.
SequentialFeatureSelector (mlxtend / sklearn)
Exam questions on this topic
1d 1d
Explain the procedure involved in Forward Feature Selection.
Forward Feature Selection is a stepwise (wrapper) feature-selection technique that starts with no features and adds one at a time, picking the most useful at each step.
Procedure:
Start with an empty feature set .
For each candidate feature not yet in the model:
Fit the regression model using {current set} + {candidate}.
Record the score (R² / Adjusted R² / AIC / cross-validation score).
Add the candidate that improved the score the most to the model.
Repeat steps 2-3 until either: (a) no remaining candidate improves the score, or (b) you reach a desired number of features, or (c) all features are added.
The final feature set is the chosen subset.
Pros: simple, interpretable, gives a small model.
Cons: greedy — can miss feature combinations that only help when chosen together; computationally expensive when k is large.
What are Wrapper Methods in feature selection, and how are they applied in Linear Regression?
Wrapper methods are feature selection techniques that "wrap around" a learning algorithm — they evaluate feature subsets by training the actual model and measuring its performance, choosing the subset that gives the best score.
Three main wrapper methods:
Forward Selection — start empty, add the most-useful feature one at a time.
Backward Elimination — start with all features, drop the least-significant one at a time.
Recursive Feature Elimination (RFE) — start with all, repeatedly drop the lowest-ranked feature based on coefficient importance.
Applied to Linear Regression:
Use the linear model (e.g., LinearRegression ) as the base estimator.
Score subsets via Adjusted R², AIC/BIC, or cross-validated RMSE.
Implementations: SequentialFeatureSelector from mlxtend or sklearn; RFE / RFECV from sklearn.
Pros: often find better subsets than filter methods; capture feature interactions in the model context.
Cons: computationally expensive (model fit per subset); risk of overfitting to validation set.
What is Recursive Feature Elimination (RFE)? Explain how it works, its advantages and limitations, and how it can be used to improve model performance in linear regression.
RFE is a wrapper feature-selection method that ranks features by importance and removes them one at a time (or in batches) using the trained model itself.
How it works:
Train the linear regression model with all features.
Rank features by importance — typically the absolute value of the coefficients (or coefficients on standardized features).
Remove the feature with the lowest rank.
Re-train the model on the remaining features.
Repeat steps 2–4 until you reach the target number of features (or use RFECV to let CV pick the optimal count).
Advantages:
Considers multivariate feature importance (uses the actual model's coefficients).
Often outperforms simple filter methods.
Can be combined with cross-validation (RFECV) to auto-pick the best feature count.
Limitations:
Computationally expensive — fits the model many times.
Sensitive to feature scaling — must standardize before applying with linear models.
Coefficient-based ranking unreliable when features are highly correlated.
Greedy — doesn't explore all subsets.
How it improves linear regression: reduces overfitting, eliminates noise features, makes the model more interpretable, and often gives better test-set performance.
Discuss the need for data transformations in a linear regression model. Also write about various techniques employed.
Why data transformations are needed:
Fix non-linearity — straighten curved relationships so a linear model fits well.
Reduce skewness — bring features/target closer to normal distribution.
Stabilize variance — fix heteroscedasticity (residual variance varying with ŷ).
Bring features to comparable scales — required for regularization and for fair coefficient comparison.
Handle outliers — log/sqrt compress extreme values without dropping them.
Improve normality of residuals — makes p-values reliable.
Techniques:
Technique
Use case
Log / log1p
Right-skewed positive data (prices, salaries, counts)
Square root / Cube root
Mildly skewed positive data
Box-Cox
Auto-pick best power transformation; needs y > 0
Yeo-Johnson
Generalisation of Box-Cox for any y
Reciprocal (1/x)
Heavy right tail
StandardScaler
(x − μ) / σ — for distance-based or regularized models
MinMaxScaler
(x − min) / (max − min) → [0, 1]
RobustScaler
(x − median) / IQR — outlier-robust
Polynomial features
Capture x², x³, x·z relationships
Encoding (label, one-hot)
Convert categorical features to numeric
Binning
Convert continuous to categorical when relationship is non-monotonic
Engineering creates new features. Selection picks the best of existing ones.
Filter methods score features alone; Wrapper methods use the model; Embedded methods (Lasso) do both.
Forward / Backward / RFE are the three core wrapper methods.
Always scale features before RFE with linear models.
"""

# --- Code ---

df['log_price'] = np.log1p(df['price'])  # log(1+x) handles zeros

from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer(method='yeo-johnson')
X_transformed = pt.fit_transform(X)

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, interaction_only=False)
X_poly = poly.fit_transform(X)

from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
selector = RFE(LinearRegression(), n_features_to_select=5)
selector.fit(X_train, y_train)
selected = X.columns[selector.support_]
print("Selected features:", list(selected))

from mlxtend.feature_selection import SequentialFeatureSelector
sfs = SequentialFeatureSelector(LinearRegression(),
                                k_features='best',
                                forward=False,    # False = backward elimination
                                scoring='r2', cv=5)
sfs.fit(X_train, y_train)
print("Best features:", sfs.k_feature_names_)


# ==============================================================================
# TOPIC 15: Data Preprocessing
# ==============================================================================

"""
Why preprocess?
Missing Values
Outliers
Encoding
Scaling
Train-Test Split
Why preprocess data?
Real datasets are messy. They have missing values, outliers, mixed types, wrong scales, text categories. Models can't directly digest any of that. Preprocessing is the cleanup step that gets your data into a model-friendly state.
Section B Q4 of nearly every ML-1 paper is dedicated to this — typically worth 25 marks . The five subtasks recur identically across papers: missing values, outliers, encoding, scaling, splitting .
1. Missing Values
Detect
Treat
Strategy
When to use
Code
Drop rows
Few rows have NaN; data is plentiful
df.dropna()
Drop column
Column is > 50% missing
df.drop(columns=['col'])
Fill with mean
Numeric, roughly normal distribution
df['col'].fillna(df['col'].mean())
Fill with median
Numeric, skewed or has outliers
df['col'].fillna(df['col'].median())
Fill with mode
Categorical features
df['col'].fillna(df['col'].mode()[0])
Forward / backward fill
Time-series data
df.ffill() / df.bfill()
Constant value
"missing" itself is meaningful
df.fillna('missing') or df.fillna(0)
KNN imputation
Missing-at-random patterns
sklearn.impute.KNNImputer()
Iterative imputer
Multivariate dependencies
sklearn.impute.IterativeImputer()
2. Outliers
Detect
Visual: boxplot — points outside the whiskers; histogram with extreme tails; scatter plot vs y.
Statistical:
IQR method: Q1 − 1.5·IQR < outlier > Q3 + 1.5·IQR (where IQR = Q3 − Q1).
Z-score method: |z| > 3 → outlier.
Treat (in order of preference)
Investigate first. Are they real values or data-entry errors?
Cap (winsorize) — clip values to the IQR boundary or a percentile (e.g., 1st-99th).
Transform — log or square-root often pulls outliers in.
Drop — only when you're sure they're errors. Used by every Section B Q4 in your papers ("treat with dropping").
Use a robust model — Huber regression, RANSAC.
3. Encoding categorical features
Method
How it works
Pros
Cons
Label Encoding
Map categories to integers (0, 1, 2, …)
Compact; one column
Implies ordering — wrong for nominal data!
One-Hot Encoding
One binary column per category
No false ordering
Many columns if high cardinality
Dummy Encoding (n−1)
Like one-hot but drop one column
Avoids dummy variable trap
One category becomes the "reference"
Ordinal Encoding
Map to integers in a meaningful order
Captures real ordering
Need to specify the order
Target Encoding
Replace category with mean(y) for that category
Captures relationship to y
Risk of leakage; needs CV
The Dummy Variable Trap
If you have a categorical feature with k categories and create k one-hot columns, the columns sum to 1 — perfectly collinear with the intercept. OLS fails. Always drop one category (use n-1 dummies) or use drop_first=True in pandas.
Code
4. Feature Scaling
Scaler
Output range
Use when
StandardScaler
(x − μ) / σ
Mean 0, Std 1
Default; data roughly normal; required before regularization
MinMaxScaler
(x − min) / (max − min)
[0, 1]
You need a bounded range (e.g., neural nets)
RobustScaler
(x − median) / IQR
Centered around 0
Data has outliers
MaxAbsScaler
x / max(|x|)
[−1, 1]
Sparse data
The cardinal scaling rule
fit on training data only. Then transform both train and test using the same scaler — never re-fit on test data. Fitting on full data leaks test info into training.
5. Train-Test Split
Exam questions on this topic
Explain any two of the data preprocessing steps.
Answer (pick any two)
1. Handling missing values — replace NaNs with mean (numeric), median (skewed numeric), or mode (categorical); or drop rows/columns when too many are missing. Visualize first with df.isnull().sum() or a heatmap. Choice depends on % missing and the distribution.
2. Encoding categorical features — convert text categories to numeric so the model can use them. Use Label Encoding for ordinal data (e.g., 'low/medium/high' → 0/1/2) and One-Hot or n-1 Dummy Encoding for nominal data (e.g., 'red'/'green'/'blue' → three or two binary columns). Always drop one category to avoid the dummy variable trap.
3. Outlier treatment — detect via boxplots, IQR rule (1.5×IQR boundary), or Z-scores (|z| > 3). Treat by capping (winsorize), dropping, or log-transformation. Outliers can dominate OLS regression if untreated.
4. Feature scaling — bring features to comparable magnitudes. Use StandardScaler (mean 0, std 1) for most cases; MinMaxScaler for [0,1] range; RobustScaler when outliers exist. Required before regularization (Ridge/Lasso) and most distance-based algorithms.
Five core preprocessing steps: missing values, outliers, encoding, scaling, splitting.
Section B Q4 of every paper tests these — worth ~25 marks.
Always fit scalers/encoders on training data only; transform test using the fitted version.
Use n-1 dummy encoding to avoid the dummy variable trap.
"""

# --- Code ---

df.isnull().sum()                    # count of NaNs per column
df.isnull().sum() / len(df) * 100     # % missing per column
import seaborn as sns
sns.heatmap(df.isnull(), cbar=False)  # visual map of NaNs

# IQR-based dropping (the standard exam approach)
Q1 = df['col'].quantile(0.25)
Q3 = df['col'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df = df[(df['col'] >= lower) & (df['col'] <= upper)]

# Label encoding (use only for ordinal categories)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['gender_encoded'] = le.fit_transform(df['gender'])

# One-hot encoding (n columns)
df_encoded = pd.get_dummies(df, columns=['category'], drop_first=False)

# n-1 dummy encoding (avoids the trap) — used in Feb 2025, Mar 2024, Nov 2024
df_encoded = pd.get_dummies(df, columns=['category'], drop_first=True)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # learn μ, σ from train
X_test_scaled = scaler.transform(X_test)        # apply same μ, σ to test

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2,         # 80:20 (Feb 2025, Mar 2024, Nov 2024); use 0.3 for 70:30
    random_state=42            # for reproducibility
)


# ==============================================================================
# TOPIC 16: Hyperparameter Tuning
# ==============================================================================

"""
Parameters vs Hyperparameters
Grid Search
Random Search
Bayesian Optimization
Comparison
Parameters vs Hyperparameters
Parameters
Hyperparameters
Learned from data during training
Set by you before training
Examples: β₀, β₁, …, βₖ in linear regression
Examples: alpha in Ridge, l1_ratio in ElasticNet, k in k-fold CV, max_iter
Found via OLS or gradient descent
Found via Grid Search, Random Search, Bayesian Optimization
Grid Search
Try every combination of hyperparameters from a predefined list. Pick the one that gives the best cross-validation score.
Pros: exhaustive — guaranteed to find the best in your grid.
Cons: exponential cost. With 4 hyperparameters of 5 values each = 5⁴ = 625 fits × 5 folds = 3,125 model trainings. Slow.
Random Search
Sample random combinations from a distribution. Often finds nearly-best results in a fraction of the time.
Pros: faster than grid; explores continuous ranges; often finds good combos quickly.
Cons: not exhaustive — you might miss the global optimum (though usually not by much).
Bayesian Optimization
Smarter still: build a probabilistic model (typically a Gaussian Process) of "score as a function of hyperparameters" , and use it to pick the next promising point to try.
How it works
Initialize by trying a few random points; record their scores.
Fit a surrogate model (e.g., Gaussian Process) that predicts the score at any unseen hyperparameter point, plus uncertainty.
Acquisition function (Expected Improvement / Upper Confidence Bound) decides where to evaluate next — balancing exploration (uncertain regions) and exploitation (regions with predicted high score).
Train and score the model at that point; update the surrogate.
Repeat until budget exhausted.
Tools: scikit-optimize ( BayesSearchCV ), Optuna , Hyperopt .
Pros: finds excellent hyperparameters with few evaluations; great when each model fit is expensive.
Cons: more complex setup; the surrogate model itself takes a moment per iteration.
Comparison
Method
How it explores
Best for
Cost
Grid Search
Every combination
Few hyperparameters with discrete values
Exponential in #params
Random Search
Random sampling
Many hyperparameters, large ranges
Linear in #iterations
Bayesian Optimization
Smart sampling, learns from past trials
Expensive-to-train models, want best result with minimum cost
Linear, but each step has surrogate-fitting overhead
Exam questions on this topic
How does Bayesian Optimization work, and how can it be used to tune the hyperparameters of a Linear Regression model?
Bayesian Optimization is an intelligent hyperparameter tuning technique that uses a probabilistic surrogate model to choose the next set of hyperparameters to try, balancing exploration and exploitation.
How it works:
Initialize with a few random hyperparameter samples; train and score each via cross-validation.
Build a surrogate model (typically a Gaussian Process) that maps hyperparameters → CV score, with uncertainty estimates at every point in the search space.
Use an acquisition function — such as Expected Improvement (EI) or Upper Confidence Bound (UCB) — to choose the next hyperparameter point. The acquisition function trades off:
Exploitation — points where the surrogate predicts a high score.
Exploration — points where the surrogate is uncertain.
Train the model at the chosen point and record the actual CV score.
Update the surrogate with this new observation.
Repeat steps 3–5 until the evaluation budget is exhausted.
Applied to Linear Regression hyperparameter tuning:
For Ridge: tune alpha over a log-uniform range like (1e-4, 1e2).
For ElasticNet: tune alpha AND l1_ratio simultaneously.
For polynomial regression: tune degree .
Use BayesSearchCV from scikit-optimize , or Optuna , or Hyperopt .
Advantages over Grid/Random Search:
Reaches near-optimal hyperparameters in many fewer trials — important when each fit is expensive.
Handles continuous, log-scale, and discrete hyperparameters together.
Provides uncertainty estimates of the score landscape.
Hyperparameters are settings you choose; parameters are learned from data.
Grid Search: exhaustive, slow.
Random Search: sample randomly, faster.
Bayesian Optimization: smart sampling using a surrogate model — best for expensive models.
All use cross-validation to score each candidate setting.
"""

# --- Code ---

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

param_grid = {'alpha': [0.001, 0.01, 0.1, 1, 10, 100]}
grid = GridSearchCV(Ridge(max_iter=500),
                    param_grid,
                    cv=5,                          # 5-fold CV
                    scoring='neg_root_mean_squared_error',
                    n_jobs=-1)                      # parallel across cores
grid.fit(X_train_scaled, y_train)

print(f"Best alpha: {grid.best_params_['alpha']}")
print(f"Best CV score: {-grid.best_score_:.3f}")
y_pred = grid.predict(X_test_scaled)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Test RMSE: {test_rmse:.3f}")

from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import loguniform

param_dist = {'alpha': loguniform(0.001, 100)}
rnd = RandomizedSearchCV(Lasso(max_iter=500),
                         param_dist,
                         n_iter=20,                # try 20 random alphas
                         cv=5,
                         scoring='neg_root_mean_squared_error',
                         random_state=42)
rnd.fit(X_train_scaled, y_train)
print(f"Best alpha: {rnd.best_params_['alpha']}")

from skopt import BayesSearchCV
from sklearn.linear_model import Ridge
opt = BayesSearchCV(Ridge(),
                    {'alpha': (1e-4, 1e2, 'log-uniform')},
                    n_iter=25, cv=5)
opt.fit(X_train_scaled, y_train)
print(f"Best alpha: {opt.best_params_['alpha']:.4f}")


# ==============================================================================
# TOPIC 17: Numerical Problems Solved
# ==============================================================================

"""
Index of problems
P1: Birth Weight
P2: College GPA
P3: CEO Salary
P4: Coefficient interpretation
P5: Mobile p-value
P6: RMSE comparison
Practice 1: VIF
Practice 2: Manual β
Practice 3: Bias/Variance
Solving checklist
What's in this chapter
Every numerical problem from your past papers, solved step-by-step . Read each one twice — first to follow the answer, second to internalize the method so you can adapt it to a new problem.
Numerical problems index
Birth Weight Prediction — Mar 2021 1b
College GPA from SAT and HS percentile — Mar 2021 1c
CEO Salary log model — Mar 2021 2a
Coefficient interpretation y = 2x₁ + 12x₂ + 3x₃ + 5 — Mar 2021 2b / Sample 1d · 2-4 marks
Mobile sales p-value interpretation — Nov 2021 1c
RMSE comparison: salary vs age — Nov 2021 1d
VIF calculation — practice problem
Manual β computation — practice problem
Problem 1: Birth Weight Prediction
Below is the equation of the births given by women in the United States. Two variables of interest are the dependent variable, infant birth weight in ounces (bwght), and an explanatory variable, average number of cigarettes the mother smoked per day during pregnancy (cigs). The following simple regression was estimated using data on n = 1,388 births: pred_bwght = 119.77 - 0.514*cigs What is the predicted birth weight when cigs = 0? What about when cigs = 20 (one pack per day)? Comment on the difference.
Step 1 — Identify the model
This is a simple linear regression with form ŷ = β₀ + β₁·x where:
x = cigs (cigarettes per day)
ŷ = pred_bwght (predicted birth weight in ounces)
β₀ = 119.77 (intercept)
β₁ = −0.514 (slope)
Step 2 — Predict at cigs = 0
Substitute x = 0:
pred_bwght = 119.77 − 0.514 × 0 = 119.77 ounces
So a non-smoking mother is predicted to have a baby weighing 119.77 oz ≈ 7.49 lbs ≈ 3.40 kg.
Step 3 — Predict at cigs = 20
pred_bwght = 119.77 − 0.514 × 20 = 119.77 − 10.28 = 109.49 ounces
A mother smoking a pack/day is predicted to have a baby weighing 109.49 oz ≈ 6.84 lbs ≈ 3.10 kg.
Step 4 — Comment on the difference
Difference = 119.77 − 109.49 = 10.28 ounces .
That's roughly 8.6% of the non-smoking baseline weight.
Babies of pack-a-day smokers are predicted to weigh about 10 ounces less on average — a practically significant reduction.
This is consistent with public-health findings linking maternal smoking to lower birth weight.
Caveat: this is a simple regression — other variables (nutrition, prenatal care, alcohol) are not controlled for. Causation cannot be established from a single regression.
Problem 2: College GPA from SAT and High School Percentile
The following equation has been obtained for college Grade Point Average (colgpa) at a US university, colgpa = 1.392 - 0.0135*hsperc + 0.00148*sat where hsperc is percentile in the high school graduating class (defined so that, for example, hsperc=5 means the top 5% of the class) and sat is the combined SAT score.
(a) Why does it make sense for the coefficient on hsperc to be negative?
(b) What is the predicted change in colgpa for a difference in SAT of 140 points (about one standard deviation)?
(c) What change in SAT score would be required to produce a 0.50 increase in colgpa?
Part (a) — Why is hsperc coefficient negative?
The variable hsperc is inverted compared to academic performance:
hsperc = 5 means top 5% of the class — a strong student.
hsperc = 95 means bottom 5% of the class — a weak student.
So lower hsperc → better student → higher college GPA. Mathematically, the coefficient on hsperc must be negative to reflect: as percentile rank goes up (worse rank), predicted college GPA goes down. The β = −0.0135 says: each one-unit drop in class rank reduces predicted college GPA by about 0.0135 points .
Part (b) — Predicted change in colgpa for ΔSAT = 140
Coefficient on SAT is β_sat = 0.00148. Holding hsperc constant:
Δcolgpa = β_sat × ΔSAT = 0.00148 × 140 = 0.2072
Inference: a 140-point higher SAT (about one standard deviation) is associated with an increase of about 0.21 GPA points — meaningful but not huge.
Part (c) — ΔSAT needed for Δcolgpa = 0.50
Solve 0.50 = 0.00148 × ΔSAT for ΔSAT:
ΔSAT = 0.50 / 0.00148 ≈ 337.84 points
Inference: to gain 0.5 GPA units, a student would need to raise their SAT by roughly 338 points — that's about 2.4 standard deviations, a very large change. SAT alone has a relatively modest effect on college GPA in this model.
Problem 3: CEO Salary log model — most important problem
Following equation has been obtained using a CEO Salary database for 209 CEOs of US companies: log(Salary) = 4.32 + 0.280*log(sales) + 0.0174*roe + 0.00024*ros SE values: (0.32) (0.035) (0.0041) (0.00054) where Salary in 1000s of dollars, sales in millions of dollars, return on the firm's equity (roe) in percent, and ros is return on the firm's stock (in percent).
(a) For this regression, what is the predicted percentage increase in salary if the ros increases by 50 points?
(b) Test the null hypothesis that ros has no effect on salary against the alternative that ros has a positive effect. Carry out the test at the 10% significance level. (Reject if t > 1.282)
(c) Would you include ros in a final model explaining CEO compensation in terms of firm performance? Explain.
Part (a) — % salary change for Δros = 50
Note: this is a log-linear model — the dependent variable is log(Salary) but ros enters in levels , not log. Because of the log-linear form, the coefficient β_ros = 0.00024 has the interpretation: "a 1-unit increase in ros leads to approximately a 100·β_ros = 0.024% increase in salary."
For a 50-unit change:
% Δ Salary ≈ 100 × β_ros × Δros = 100 × 0.00024 × 50 = 1.2%
So a 50-point increase in ros is associated with about a 1.2% increase in CEO salary . (For exact percentages with larger Δ, use 100·(e^(β·Δros) − 1), but for small β, the linear approximation is fine.)
Part (b) — Hypothesis test on β_ros (one-tailed at 10%)
Hypotheses:
H₀: β_ros = 0 (ros has no effect on salary)
H₁: β_ros > 0 (ros has a positive effect)
Test statistic:
t = β̂_ros / SE(β̂_ros) = 0.00024 / 0.00054 ≈ 0.444
Decision rule: reject H₀ if t > 1.282 (the critical value at α = 0.10 for a one-tailed test).
Comparison: 0.444 < 1.282 → fail to reject H₀ .
Conclusion: at the 10% significance level, there is insufficient evidence to conclude that ros has a positive effect on CEO salary. The coefficient on ros is not statistically distinguishable from zero.
Part (c) — Should ros be in the final model?
Reasons to drop ros:
The hypothesis test (part b) shows the coefficient is not statistically significant even at the lenient 10% level.
The economic effect is very small — a 50-point change in ros gives only a 1.2% salary change.
Keeping a noisy non-significant predictor wastes a degree of freedom and inflates uncertainty in the other coefficients.
Reasons to keep ros:
If it's of theoretical interest (does stock return affect CEO pay?), reporting "no significant effect" is itself a finding.
Adjusted R² and out-of-sample MSE could decide empirically.
Conclusion: based purely on this regression, I would not include ros in the final model — it's not statistically significant and the effect size is small. log(sales) and roe are the meaningful predictors of CEO salary here.
Problem 4: Coefficient interpretation
If y = 2x1 + 12x2 + 3x3 + 5 is the linear regression equation, then explain how the coefficients of x1, x2, x3 affect the value of y.
Step 1 — Rewrite in standard form
y = 5 + 2·x₁ + 12·x₂ + 3·x₃
So β₀ = 5, β₁ = 2, β₂ = 12, β₃ = 3.
Step 2 — Apply the universal interpretation rule
"Holding all other features constant, a 1-unit increase in xⱼ is associated with a βⱼ-unit change in y."
Coefficient
Sign & magnitude
Interpretation
β₁ = 2
Positive, smallest
1 unit ↑ in x₁ → 2 units ↑ in y (smallest positive effect)
β₂ = 12
Positive, largest
1 unit ↑ in x₂ → 12 units ↑ in y (most influential predictor)
β₃ = 3
Positive, medium
1 unit ↑ in x₃ → 3 units ↑ in y (modest positive effect)
Step 3 — Comparison & caveats
Order of influence (raw): x₂ > x₃ > x₁ (12 vs 3 vs 2).
x₂ is 6× more influential than x₁ (12/2 = 6) and 4× more than x₃ (12/3 = 4).
The intercept β₀ = 5 is the predicted y when all x's = 0. May or may not be physically meaningful.
Caveat: coefficient comparisons are only valid if x₁, x₂, x₃ are on the same scale (e.g., all in standardized form). If features have different units, use standardized coefficients .
Problem 5: p-value interpretation (Mobile phone sales)
A linear regression model is build with three independent variable price, advertisement cost and promotion cost to predict unit sales of mobile phone. Say the p value for the t-test of the variable 'advertisement cost' is 0.02. What is your inference on this?
Step 1 — State the hypotheses
For each coefficient in a regression, the t-test asks whether that coefficient is statistically distinguishable from zero:
H₀: β_ad = 0 — advertisement cost has no effect on unit sales.
H₁: β_ad ≠ 0 — advertisement cost has a (non-zero) effect.
Step 2 — Interpret the p-value
The p-value is the probability of seeing a coefficient at least as extreme as the observed one, if H₀ were true . Here p = 0.02 = 2%.
Step 3 — Compare against significance levels
Significance level α
Threshold
Decision
10%
0.02 < 0.10 → reject H₀
5% (most common)
0.02 < 0.05 → reject H₀
1%
0.02 > 0.01 → fail to reject H₀
Step 4 — Stated inference
At the conventional 5% significance level, we reject H₀ . Advertisement cost is a statistically significant predictor of mobile phone unit sales. The probability of observing this β value by chance alone (if advertising truly had no effect) is only 2%.
At the stricter 1% level, the result would not be significant. So we'd say: "significant at the 5% level but not at the 1% level."
Practical implication: keep advertisement cost in the model. The t-test alone doesn't tell you the magnitude of the effect — you'd want to look at the coefficient value and its confidence interval too.
Problem 6: RMSE comparison (CTC vs Age)
The RMSE of the regression model which predicting the CTC salary is 12324 and the RMSE of the other regression model which predicting the age of the person is 55. Comment on the performance of these two models. [output column is not scaled or transformed]
Step 1 — Recognize the trap
RMSE has the same units as the target variable y . The two models predict completely different things on completely different scales. Direct comparison of raw RMSEs is meaningless.
Step 2 — Evaluate each in context
Model 1: CTC salary, RMSE = 12,324
Indian CTC values typically range from ₹3,00,000 to ₹50,00,000+.
Suppose mean CTC ≈ ₹6,00,000.
%RMSE = 12,324 / 6,00,000 × 100 ≈ 2.05%
An average error of 2% on salary predictions is very good .
Model 2: Age, RMSE = 55
Human ages typically range from 18 to 80.
Suppose mean age ≈ 35.
%RMSE = 55 / 35 × 100 ≈ 157%
An RMSE of 55 is larger than the entire reasonable range of ages . The model is essentially useless — it might as well predict random numbers.
Step 3 — Use scale-free metrics for fair comparison
For comparing models predicting different ys, use:
R² (coefficient of determination) — fraction of variance explained, range (−∞, 1]. A salary model with R² = 0.9 is comparable to an age model with R² = 0.9.
MAPE — mean absolute percentage error, in %. Already scale-free.
%RMSE = RMSE / mean(y) × 100 — quick rule of thumb.
Step 4 — Final inference
The CTC model performs excellently (relative error ≈ 2%). The age model performs terribly (relative error far exceeds the data range). The raw RMSE numbers (12,324 vs 55) are misleading — without converting to a scale-free metric, you'd wrongly think the age model is better. Always interpret RMSE relative to the magnitude of y.
Practice Problem 1: VIF Calculation
Practice problem
In a regression with 5 features (x₁, …, x₅), suppose when you regress x₁ on the other four features you get R²₁ = 0.85. Compute VIF for x₁ and interpret.
Solution
VIF₁ = 1 / (1 − R²₁) = 1 / (1 − 0.85) = 1 / 0.15 ≈ 6.67
Interpretation: the variance of β̂₁ is about 6.67× larger than it would be if x₁ were uncorrelated with x₂…x₅. Since 6.67 > 5, this is moderate-to-severe multicollinearity . Recommendation: drop x₁ if redundant, or merge with the most correlated companion feature, or use Ridge regression.
Practice Problem 2: Manual β computation
Practice problem
You have 5 data points: (1, 2), (2, 4), (3, 5), (4, 4), (5, 5). Fit a simple linear regression by hand and compute β₀, β₁.
Solution
Step 1: means. x̄ = (1+2+3+4+5)/5 = 3, ȳ = (2+4+5+4+5)/5 = 4.
Step 2: deviations.
x
y
x − x̄
y − ȳ
(x−x̄)(y−ȳ)
(x−x̄)²
−2
−1
Sum
Step 3: β₁. β₁ = 6 / 10 = 0.6
Step 4: β₀. β₀ = ȳ − β₁·x̄ = 4 − 0.6·3 = 4 − 1.8 = 2.2
Final equation: ŷ = 2.2 + 0.6·x
Verify: predict for x = 3 → ŷ = 2.2 + 1.8 = 4.0 (passes through the centroid (3, 4) as expected).
Practice Problem 3: Bias/Variance from CV
Practice problem
5-fold CV gives R² scores of [0.82, 0.78, 0.85, 0.80, 0.79]. Compute bias and variance errors, and interpret.
Solution
Mean R² = (0.82 + 0.78 + 0.85 + 0.80 + 0.79) / 5 = 4.04 / 5 = 0.808
Bias error = 1 − 0.808 = 0.192
Standard deviation = √[((0.82−0.808)² + (0.78−0.808)² + (0.85−0.808)² + (0.80−0.808)² + (0.79−0.808)²) / 5] ≈ √(0.000688) ≈ 0.026
Variance error = 0.026.
Interpretation: the model explains about 80.8% of variance — decent but improvable. The low std-dev (0.026) indicates stable performance across folds — no overfitting concern. Bias (1−R²) is moderate at 0.192 — could try richer features or polynomial terms to reduce it.
Quick numerical-problem checklist
Solving recipe
Identify the equation form — linear, log-linear, log-log, polynomial.
Identify what's asked — predict y, compute Δy, find Δx, test a hypothesis.
Substitute the given numbers carefully.
Show every step — calculation by calculation. Examiners give partial marks.
State units — ounces, %, GPA points, ₹.
Interpret — translate the number back into plain English.
State caveats — "this is correlation, not causation"; "valid only if assumptions hold."
Simple linear regression questions: substitute in ŷ = β₀ + β₁x.
Log-linear questions: 100·β gives the % effect per unit change.
Hypothesis tests: t = β̂ / SE; reject H₀ if |t| > critical value (or p < α).
RMSE comparisons across different ys are meaningless — use R² or MAPE.
VIF = 1/(1−R²_j); show every digit of the calculation.
"""



